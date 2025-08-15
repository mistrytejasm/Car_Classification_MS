# 🚗 **Maruti Suzuki Car Models Classification**  

[![FastAPI](https://img.shields.io/badge/FastAPI-0.116.x-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch)](https://pytorch.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://render.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> A specialized machine learning web application for classifying **Maruti Suzuki car models** using deep learning and computer vision.

## 🌐 Live Demo
**[Try it live here →](https://car-classification-ms.onrender.com/)**

---

## 📖 About

This project is a specialized machine learning web application designed to classify **Maruti Suzuki car models** with high accuracy. The system combines:
- **PyTorch deep learning model** trained specifically on Maruti Suzuki vehicles
- **FastAPI backend** serving REST API endpoints
- **Responsive web frontend** for easy image uploads
- **Real-time predictions** with confidence scores

Upload any Maruti Suzuki car image and get instant model classification results!

## 🚗 Supported Car Models

This application classifies the following **4 Maruti Suzuki models**:

| Model | Classification Label |
|-------|---------------------|
| **Baleno** | `Maruti_Suzuki_Baleno` |
| **Brezza** | `Maruti_Suzuki_Brezza` |
| **Swift** | `Maruti_Suzuki_Swift` |
| **WagonR** | `Maruti_Suzuki_WagonR` |

> **Note**: This model is specifically trained for Maruti Suzuki vehicles and may not accurately classify other car brands or models.

## ✨ Features

- 🤖 **AI-Powered Classification** - Identify specific Maruti Suzuki models
- 🖼️ **Image Upload Interface** - Drag & drop or browse files
- 📊 **Confidence Scores** - See prediction reliability
- 🔄 **Real-time Processing** - Instant results
- 📱 **Responsive Design** - Works on all devices
- 🚀 **Fast API** - High-performance backend
- 📚 **Auto-generated Docs** - Interactive API documentation
- 🎯 **Specialized Model** - Focused on Maruti Suzuki accuracy

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | FastAPI, Uvicorn |
| **ML Framework** | PyTorch |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Deployment** | Render |
| **Image Processing** | PIL, OpenCV |

## 📁 Project Structure

```

Car_Classification_MS/
│
├── 📄 main.py                 # FastAPI application entry point
├── 📁 models/
│   └── car_classifier.py      # ML model class and prediction logic
├── 📁 saved_models/           # Trained PyTorch model files
│   ├── model.pth
│   └── metadata.json
├── 📁 static/                 # Frontend files
│   ├── index.html             # Main web interface
│   ├── style.css              # Styling
│   └── script.js              # Frontend logic
├── 📁 uploads/                # Temporary file storage
├── 📄 requirements.txt        # Python dependencies
└── 📄 README.md               # Project documentation

```

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Git

### Installation

1. **Clone the repository**
```

git clone https://github.com/mistrytejasm/Car_Classification_MS.git
cd Car_Classification_MS

```

2. **Set up virtual environment**
```

python -m venv .venv

# Windows

.venv\Scripts\activate

# macOS/Linux

source .venv/bin/activate

```

3. **Install dependencies**
```

pip install -r requirements.txt

```

4. **Run the application**
```

python main.py

```

5. **Open in browser**
- Main App: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 📡 API Reference

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serve web interface |
| `POST` | `/predict` | Upload image for Maruti Suzuki classification |
| `GET` | `/classes` | Get supported Maruti Suzuki models |
| `GET` | `/health` | Check API health status |

### Example Usage

**Predict Maruti Suzuki model from image:**
```

curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: multipart/form-data" \
-F "file=@maruti_car.jpg"

```

**Response:**
```

{
"success": true,
"filename": "maruti_car.jpg",
"prediction": {
"predicted_class": "Maruti_Suzuki_Swift",
"confidence": 0.92
}
}

```

## 🔧 Want to Add More Car Models?

**Interested in extending this classifier to support additional car brands or models?**

I've created a dedicated deep learning training repository that allows you to train your own custom car classification model with your specific dataset.

### 🎯 Training Repository
**[Car Model Classification with Deep Learning →](https://github.com/mistrytejasm/Car_Model_Classification_with_Deep-Learning)**

### Simple Steps to Extend:

1. **Visit the training repository** above
2. **Add your car images** to the `datasets/` directory (organized by car model folders)
3. **Run the training notebook**: [`Car_Model_Classification_Using_OOD.ipynb`](https://github.com/mistrytejasm/Car_Model_Classification_with_Deep-Learning/blob/main/Car_Model_Classification_Using_OOD.ipynb)
4. **Replace the trained model** in this project's `saved_models/` directory
5. **Update class labels** and deploy your custom classifier

### What You Can Build:
- **Multi-Brand Classifiers**: BMW, Audi, Honda, Toyota, Ford, etc.
- **Specific Use Cases**: Vintage cars, luxury vehicles, trucks, motorcycles
- **Regional Models**: Cars popular in your specific country/region
- **Custom Categories**: Electric vehicles, SUVs, sedans, etc.

### Requirements:
- **Dataset**: Minimum 100+ images per car model for good accuracy
- **Computing**: GPU access recommended (Google Colab works perfectly)
- **Knowledge**: Basic understanding of Python and Jupyter notebooks

> **💡 Note**: The training repository includes a complete end-to-end pipeline with data preprocessing, model training, and validation - just update the dataset and run the notebook!

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Tejas Mistry** - *AI/ML Engineer*
- GitHub: [@mistrytejasm](https://github.com/mistrytejasm)
- Project Repository: [Car Classification MS](https://github.com/mistrytejasm/Car_Classification_MS)
- Training Repository: [Car Model Classification with Deep Learning](https://github.com/mistrytejasm/Car_Model_Classification_with_Deep-Learning)

## 🙏 Acknowledgments

- **PyTorch Team** for the robust deep learning framework
- **FastAPI Community** for the high-performance web framework  
- **Render Platform** for reliable deployment infrastructure
- **Maruti Suzuki** for inspiring this specialized automotive classifier

---

<div align="center">
  <p>Made with ❤️ by Tejas Mistry</p>
  <p>⭐ Star this repo if you found it helpful!</p>
  <p><strong>Specialized for Maruti Suzuki Classification</strong></p>
  <p>🚀 <a href="https://github.com/mistrytejasm/Car_Model_Classification_with_Deep-Learning">Train Your Own Models</a></p>
</div>


