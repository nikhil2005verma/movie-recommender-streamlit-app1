# Movie Recommender System

A Machine Learning-based Movie Recommender System built using **Python** and **Streamlit** that suggests movies based on user preferences.

---

## Demo

(Add your deployed link here – Streamlit Cloud / Render)

---

## 📌 Features

* Search for any movie
* Get top 5 similar movie recommendations
* Movie posters displayed using TMDB API
* Fast and interactive UI using Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **TMDB API**

---

## 📂 Project Structure

```
movie-recommender-system/
│
├── app.py                  # Streamlit app
├── model.pkl              # Trained similarity model
├── movies.pkl             # Movie dataset
├── requirements.txt       # Dependencies
└── README.md
```

---

## ⚙️ How It Works

* Uses **Content-Based Filtering**
* Calculates similarity between movies using **cosine similarity**
* Recommends movies based on selected input

---

## Installation & Run Locally

1️⃣ Clone the repository

```
git clone https://github.com/your-username/movie-recommender-system.git
```

2️⃣ Navigate to folder

```
cd movie-recommender-system
```

3️⃣ Install dependencies

```
pip install -r requirements.txt
```

4️⃣ Run the app

```
streamlit run app.py
```

---

## API Setup (TMDB)

* Create account on https://www.themoviedb.org/
* Generate API key


## Screenshots

![App Screenshot](images/recommend_app.png)


## 📈 Future Improvements

* Add user-based recommendations
* Deploy on cloud (AWS / Streamlit Cloud)
* Improve UI/UX
* Add login system

---


