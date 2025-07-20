# Chest-X-ray-Diagnosis-with-AI

Overview

Health.AI is an AI-powered web application for instant chest X-ray analysis.
It uses deep learning to detect lung diseases, providing healthcare professionals with faster, smarter, and more accurate diagnostic support.
Features

    🩺 AI-Powered Diagnosis – Classifies chest X-rays into COVID-19, Pneumonia, Tuberculosis, and more.

    ⚡ Real-Time Analysis – Instant predictions with confidence scores.

    🔒 Secure & Compliant – HIPAA-ready system for safe medical data handling.

    📊 Reports & Dashboard – Easily manage and view diagnostic reports.

    🌐 Web-Based – Simple drag & drop X-ray upload interface.

Tech Stack
Technology	Usage
Flask	Backend server & routing
TensorFlow / Keras	Deep learning model
HTML / CSS / Tailwind	Frontend design
Pillow / NumPy	Image processing
Docker (Optional)	Containerization
Installation
1️⃣ Clone the Repository:

git clone https://github.com/yourusername/health-ai.git
cd health-ai

2️⃣ Create a Virtual Environment:

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies:

pip install -r requirements.txt

4️⃣ Add Your Model:

Place your trained model file in the root directory as:

chest_disease_model.keras

5️⃣ Run the App:

python app.py

Open http://localhost:5000 in your browser.
Usage

    Go to the Upload X-ray page.

    Drag & drop or browse chest X-ray images (.jpg, .png, .jpeg).

    Click Start AI Analysis.

    View the predicted class and confidence score.

Folder Structure

├── app.py
├── templates/
│   ├── index.html
│   ├── upload.html
│   └── result.html
├── static/
│   └── images/
├── chest_disease_model.keras
├── README.md
└── requirements.txt

Demo Screenshots
Upload X-ray	AI Result
	
License

This project is licensed under the MIT License.
Feel free to fork, modify, and use for educational or research purposes.
Contributors

    Vinod Nanattil – Project Lead & Developer

    OpenAI GPT for AI assistance

Contact

For queries or collaborations, reach out at:
📧 vinod.nanattil@example.com (Replace with your email)
Star ⭐ the repo if you find this project helpful!
