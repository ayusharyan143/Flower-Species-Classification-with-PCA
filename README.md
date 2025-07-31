# 🌸 Flower Species Classification with PCA

A simple machine learning project to classify **Iris flower species** using **Principal Component Analysis (PCA)** and **K-Nearest Neighbors (KNN)**, wrapped in a web app built with **Flask**, **HTML**, **CSS**, and **JavaScript**.

---

## 📷 Screenshots

<img width="575" height="581" alt="image" src="https://github.com/user-attachments/assets/d4e36b37-3c8c-45fb-a04c-8ee3deccdf4f" />

---

## 🌱 Dataset

This project uses the classic **Iris dataset**, containing 150 samples from three species:

- *Iris setosa*
- *Iris versicolor*
- *Iris virginica*

Each sample includes:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

---

## 📂 Project Structure

```
Flower-Species-Classification-with-PCA/
│
├── Dataset/                          # Contains Iris dataset
├── templates/
│   └── index.html                    # Website using HTML , CSS , JS
│
├── Flower Species Classification with PCA.ipynb  # Jupyter Notebook 
├── iris_pipeline.pkl                # Trained PCA + KNN model saved using joblib
├── app.py                           # Flask backend to serve the model

```

---

## 📌 Features

- 🧠 **PCA for Dimensionality Reduction**
- 👟 **KNN Classifier** trained on reduced dimensions
- 📊 **93.3% Accuracy** on test data
- 🌐 **Interactive Web App** for real-time predictions
- 💡 Clean, responsive UI built with HTML/CSS/JavaScript

---

## 📈 Technologies Used

- Python 
- scikit-learn
- Flask
- HTML5, CSS3, JavaScript
- Jupyter Notebook

---

## 🚀 How to Run the App Locally

### 1. Clone the repository

```bash
git clone https://github.com/ayusharyan143/Flower-Species-Classification-with-PCA.git
cd Flower-Species-Classification-with-PCA
```

### 2. Install dependencies

```bash
pip install flask scikit-learn numpy
```

### 3. Run the app

```bash
python app.py
```

### 4. Open in browser

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Model Performance

- Accuracy: **93.3%**
- PCA explained variance: **~96%**
- Components used: **2 Principal Components**

---

## 💻 Author

**Ayush Aryan**  
GitHub: [@ayusharyan143](https://github.com/ayusharyan143)

---

## 📃 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.

---

## ⭐️ Show Your Support

If you liked this project, feel free to ⭐️ it on GitHub!
