# Movies-Recommender-System

# 🎬 Movies-Recommender-System

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange?logo=scikit-learn)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)

## 🔗 Live Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movies-recommender-system-qzmucjbr5x9dbccyzmejdz.streamlit.app/)

---

## 📌 Project Overview
A **content-based movie recommendation system** that suggests similar movies using metadata such as genres, keywords, cast, crew, and overview.  
The app applies **Natural Language Processing (NLP)**, **vectorization**, and **cosine similarity** to generate recommendations.  
Movie posters are fetched dynamically using the **TMDB API**.  

---

## 🛠 Features
- 🎯 Content-based filtering using textual metadata  
- 🧠 NLP preprocessing with stemming (PorterStemmer) and stopword removal  
- 📝 Vectorization with **CountVectorizer** (Bag-of-Words model, 5000 features)  
- 📐 Cosine similarity for finding the most similar movies  
- 🖼 Dynamic poster fetching from TMDB API  
- 🌐 Deployed on Streamlit Cloud with secure API key management  

---

## 📊 Dataset
- **Source**: Merged dataset of movies metadata and credits  
- **Selected Features**:
  - `title`  
  - `genres`  
  - `overview`  
  - `keywords`  
  - `cast` (top 3 actors)  
  - `crew` (director)  

---

## 🧠 Model & Processing Details
- **Data Cleaning**: Removed nulls/duplicates, parsed JSON-like fields  
- **Feature Engineering**: Combined genres, overview, keywords, cast, crew into a `tags` column  
- **Text Processing**:
  - Lowercasing  
  - Removing spaces in multi-word entities  
  - **Stemming** to unify word forms  
- **Vectorization**: CountVectorizer with `max_features=5000`, English stopwords removed  
- **Similarity Measure**: Cosine similarity between vectorized movie tags  

---

## 📦 Requirements
- Python 3.10  
- pandas, numpy  
- scikit-learn  
- nltk  
- requests  
- streamlit  
- python-dotenv  

---

## 🙌 Acknowledgements
- [Streamlit](https://streamlit.io)  
- [scikit-learn](https://scikit-learn.org)  
- [NLTK](https://www.nltk.org)  
- [TMDB API](https://www.themoviedb.org/documentation/api)  

---

## 📄 License
No license
