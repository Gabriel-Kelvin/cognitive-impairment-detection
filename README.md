
# 🧠 Cognitive Impairment Detection from Speech

This project explores early detection of cognitive impairments by analyzing speech features from audio recordings of children using unsupervised machine learning techniques.

## 📂 Dataset

We used a real-world dataset collected by LANNA (Czech Technical University) in collaboration with Charles University and Motol Hospital.

**📥 Download the Dataset:**  
[SLI Corpus on LINDAT Repository](https://lindat.mff.cuni.cz/repository/xmlui/handle/11372/LRT-1597)

The dataset contains:
- Recordings of healthy children and those with Speech Language Impairment (SLI)
- Age range: 4–12 years
- Realistic environmental recordings
- Multiple severity levels of SLI

## 🛠 Features Extracted

- Pauses per sentence
- Hesitation markers ("uh", "um")
- Word recall errors
- Speech rate
- Pitch variability
- Sentence completion success

## 🤖 ML Techniques Used

- Isolation Forest (Anomaly Detection)
- KMeans Clustering
- PCA for Visualization

## 📈 Outputs

The notebook generates visual insights such as:
- Heatmaps
- PCA projections
- Risk score distributions
- Feature comparison plots

## 🚀 API Ready

An API-ready function is included to process `.wav` files and return a risk score, suitable for deployment via Flask or FastAPI.

---

© Developed for research and educational purposes.
