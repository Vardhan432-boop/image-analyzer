# 🔥 Smart Image Analyzer

A Streamlit web app that uses a pretrained CNN (ResNet) to classify images.

---

## 🚀 Features

* 📂 Upload images
* 🌐 Paste image URL
* 🧠 Top-3 predictions
* 📊 Confidence visualization
* ❌ Clear input button

---

## 🧠 How it works

* Uses **ResNet18 (pretrained on ImageNet)**
* Image is processed into tensor format
* Model predicts probabilities for 1000 classes
* Top predictions are displayed

---

## 📂 Project Structure

```
image-analyzer/
│
├── app.py
├── model.py
├── imagenet_classes.txt
```

---

## ⚙️ Installation

```
pip install torch torchvision transformers pillow streamlit
```

---

## ▶️ Run

```
streamlit run app.py
```

---

## 📸 Screenshots

<img width="638" height="898" alt="image_analyzer" src="https://github.com/user-attachments/assets/73030183-441e-4e1e-9dc6-6ee33186b4c9" />


---
## Live Link
https://image-analyzer-55alapzmrfydksv9je.streamlit.app/

## 🧑‍💻 Author

balaji vardhan
