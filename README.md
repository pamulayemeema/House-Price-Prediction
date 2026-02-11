<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<body>

<div class="header">
    <h1>🏠 House Price Prediction</h1>
    <p>Machine Learning Web Application using Custom Linear Regression (SVD)</p>
    <p><strong>P. Yemeema | Data Science | Vihara Tech</strong></p>
</div>

<div class="container">

<div class="card">
    <h2>📌 Project Overview</h2>
    <p>
        This project predicts house prices using a custom-built Linear Regression model 
        implemented with Singular Value Decomposition (SVD). The model is deployed 
        as a Flask web application for real-time predictions.
    </p>
</div>

<div class="card">
    <h2>📊 Dataset Information</h2>
    <ul>
        <li><strong>Dataset:</strong> House Sales in King County, USA</li>
        <li><strong>Records:</strong> 4800+</li>
        <li><strong>Features Used:</strong> 17</li>
        <li><strong>Source:</strong> Kaggle</li>
    </ul>
</div>

<div class="card">
    <h2>🛠 Technology Stack</h2>
    <ul>
        <li>Python</li>
        <li>Flask</li>
        <li>NumPy & Pandas</li>
        <li>Scikit-learn (train-test split)</li>
        <li>HTML5 & CSS3</li>
        <li>Render (Deployment)</li>
        <li>GitHub (Version Control)</li>
    </ul>
</div>

<div class="card">
    <h2>📂 Project Structure</h2>
<pre>
MINI_PROJECT/
│── app.py
│── data.csv
│── MINI_PROJECT.pkl
│── requirements.txt
│── Procfile
│
├── templates/
│     └── index.html
│
└── static/
      └── images/
</pre>
</div>

<div class="card">
    <h2>📈 Model Development</h2>
    <p>
        The model solves the Normal Equation:
    </p>
    <p><code>β = (XᵀX)⁻¹ XᵀY</code></p>
    <p>
        SVD is used to compute the pseudo-inverse for better numerical stability.
    </p>
</div>

<div class="card">
    <h2>🚀 Deployment</h2>
    <ul>
        <li>Upload project to GitHub</li>
        <li>Connect repository to Render</li>
        <li>Use Procfile: <code>web: gunicorn app:app</code></li>
        <li>Deploy successfully</li>
    </ul>
</div>

<div class="card">
    <h2>🌐 Live Application</h2>
    <p>
        <a href="https://house-price-predictions1.onrender.com/" target="_blank">
            View Deployed Application
        </a>
    </p>
</div>

<div class="card">
    <h2>🔮 Future Enhancements</h2>
    <ul>
        <li>Implement Random Forest & Gradient Boosting</li>
        <li>Add Data Visualization Dashboard</li>
        <li>Docker Containerization</li>
    </ul>
</div>

</div>

<div class="footer">
    © 2026 P. Yemeema | House Price Prediction Project
</div>

</body>
</html>
