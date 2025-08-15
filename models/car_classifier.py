import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import json
import os

class CarClassifier:
  def __init__(self, model_path, metadata_path = None):
    self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    self.classes = ['Maruti_Suzuki_Baleno', 'Maruti_Suzuki_Brezza',
                    'Maruti_Suzuki_Swift', 'Maruti_Suzuki_WagonR']
    
    # Load metadata if available  
    if metadata_path and os.path.exists(metadata_path):
      with open(metadata_path, 'r') as f:
        metadata = json.load(f)
        if 'class_names' in metadata:
          self.classes = metadata['class_names']
    
    # Load the Model
    self.model = self.load_model(model_path)
    self.model.eval()

    # Define Image Transfromation
    self.transform = transforms.Compose([
      transforms.Resize((224,224)),
      transforms.ToTensor(),
      transforms.Normalize(mean=[0.485, 0.456, 0.406],
                           std=[0.229,0.224, 0.225])
    ])
  
  def load_model(self, model_path):
    """Load PyTorch model on file type in filename."""

    if "_full" in os.path.basename(model_path).lower():
      print(f"Load Full model From {model_path}")
      model = torch.load(model_path, map_location=self.device)
      return model.to(self.device)
    else:
      print(f"Loading STATE DICT from {model_path}")
      model = self.create_model_architecture()
      model.load_state_dict(torch.load(model_path, map_location=self.device))
      return model.to(self.device)
    
  def create_model_architecture(self):
    """Model Architecture"""

    class CarClassifierWithOOD(nn.Module):
      def __init__(self, num_car_classes=4, pretrained=False):
        super(CarClassifierWithOOD, self).__init__()

        # Load EfficientNet-B0 backborn without pretrained weights
        self.backbone = models.efficientnet_b0(weights=None)

        # Remove Original Classifier  
        self.backbone.classifier = nn.Identity()

        # Feature Dimension for EfficientNet-B0
        feature_dim = 1280

        # Car classification head(4 classes)
        self.car_classifier = nn.Sequential(
          nn.Dropout(p=0.5),
          nn.Linear(feature_dim, num_car_classes)
        )

        # OOD Detection Head (Binary: Car or Not-Car)
        self.ood_classifier = nn.Sequential(
          nn.Dropout(p=0.5),
          nn.Linear(feature_dim, 1)
        )

      def forward(self, x):
        # Extract Feature from Backborn
        features = self.backbone(x)

        # Get predictions from both heads
        car_logits = self.car_classifier(features) # [batch_size, 4]
        ood_logits = self.ood_classifier(features) # [batch_size, 1]

        return car_logits, ood_logits
    
    # Instantiate The Model
    model = CarClassifierWithOOD(num_car_classes=len(self.classes), pretrained=False)
    return model.to(self.device)
  
  def preprocess_image(self, image_path):
    """Preprocess image for prediction"""
    image = Image.open(image_path).convert('RGB')
    image_tensor = self.transform(image).unsqueeze(0)
    return image_tensor.to(self.device)
  
  def predict(self, image_path, ood_threshold=0.5):
    """Make prediction on an image with OOD Detection"""
    with torch.no_grad():
      image_tensor = self.preprocess_image(image_path)
      car_logits, ood_logits = self.model(image_tensor)
      ood_prob = torch.sigmoid(ood_logits).item()

      if ood_prob < ood_threshold:
        predicted_class = "Not A Car"
        confidence = 1 - ood_prob
        class_probabilities = None
      else:
        probabilities = torch.nn.functional.softmax(car_logits[0], dim=0)
        predicted_idx = torch.argmax(probabilities).item()
        confidence = probabilities[predicted_idx].item()
        predicted_class = self.classes[predicted_idx]
        class_probabilities = {
          self.classes[i]: float(probabilities[i])
          for i in range(len(self.classes))
        }

    return {
            'predicted_class': predicted_class,
            'confidence': confidence,
            'ood_probability': ood_prob,
            'class_probabilities': class_probabilities
            }
  

## For testing car_classifier.py file

# model_path = "../saved_models/car_classifier_20250731_210809.pth"
# metadata_path = "../saved_models/car_classifier_20250731_210809_metadata.json"

# classifier = CarClassifier(model_path=model_path, metadata_path=metadata_path)
# result = classifier.predict("swift.png", ood_threshold=0.5)
# print(result)

    

      


    




