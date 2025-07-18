# 🧸 Amazon Soft Toys Sponsored Product Analysis

This project showcases a complete data analysis workflow — from scraping real product listings on [Amazon.in](https://www.amazon.in/) to visualizing brand performance, price-to-rating trends, and review analytics using Python, Jupyter Notebook, and pandas.

> 📌 **Focus Keyword:** `"soft toys"`  
> 📌 **Target:** **Sponsored products** (first-page listings on Amazon India)  
> 📌 **Tools Used:** `requests`, `BeautifulSoup`, `pandas`, `matplotlib`, `seaborn`

---

## 📁 Project Structure
amazon-soft-toys-analysis/
│
├── amazon_scrapper.py # Amazon scraper script for sponsored products
├── amazon_analysis.ipynb # Jupyter notebook for data cleaning and visualization
├── soft_toys_sponsored.csv # Raw scraped product data (CSV)
├── soft_toys_sponsored_cleaned.xlsx # Final cleaned dataset (ready for analysis)

---

## 🔧 Setup Instructions

### ✅ Requirements

Install the Python packages used in this project:
pip install requests beautifulsoup4 pandas matplotlib seaborn openpyxl

### ▶️ How to Run
Step 1 - Scrape the data
python amazon_scrapper.py

Step 2 - Open and run Jupyter notebook
jupyter notebook

### Then open amazon_analysis.ipynb


---

## 📊 Data Fields Collected

Each product record contains:

| Field          | Description                                                                 |
|----------------|------------------------------------------------------------------------------|
| `Title`        | Full name/title of the soft toy product                                      |
| `Brand`        | Brand or seller name (fallback: first keyword from the product title)        |
| `Rating`       | Average customer rating out of 5                                             |
| `Reviews`      | Number of verified customer reviews                                           |
| `Price`        | Current selling price (₹ INR)                                                |
| `Image URL`    | URL to the product thumbnail image                                           |
| `Product URL`  | Direct link to the product on Amazon.in                                      |

---

## 🧽 Data Cleaning

Performed in `amazon_analysis.ipynb`:

- Removed duplicate products using `Title + Product URL`
- Converted:
  - `Price` → `float` (₹ removed, commas cleaned)
  - `Rating` → `float` (converted from text)
  - `Reviews` → `int` (with blanks converted to 0)
- Standardized empty/missing `Brand` values as `"Unknown"`

---

## 📈 Visual Analysis & Insights

The notebook analyzes and visualizes the following:

### 🔹 Brand Performance

- Top 5 brands by sponsored product count (bar chart)
- Top 5 brands by average rating (bar chart & table)
- Pie chart showing overall brand share

### 🔸 Price vs. Rating Relationship

- Scatter plot showing how product price relates to rating
- Identifies high-value outliers (low price + high rating)

### 🔸 Review & Rating Distribution

- Top 5 products with most reviews (bar chart)
- Top 5 highest-rated products (minimum 10 reviews)

---

## 📋 Key Takeaways

- 🏆 **Vaishno** appears multiple times, showing large brand presence among sponsored listings.
- 🌟 Some “less frequent brands” like **LOVEY** and **TechMax** have high rating products, indicating opportunity.
- 💰 Price does **not always equal quality**. Several highly rated products are very affordable (e.g., under ₹1,000).
- 🏅 The most reviewed product had over **34,000+ verified reviews**, making it a clear best-seller in the soft toys segment.

---

## 📂 Files for Review

| File                             | Description                                  |
|----------------------------------|----------------------------------------------|
| `amazon_scrapper.py`            | Python script that scrapes product data       |
| `amazon_analysis.ipynb`         | Notebook containing full data analysis        |
| `soft_toys_sponsored.csv`       | Raw scraped data in tabular format            |
| `soft_toys_sponsored_cleaned.xlsx` | Cleaned + ready-to-analyze dataset         |
| `README.md`                     | This documentation                           |

---

## 🚀 Future Improvements

- Use Selenium or Playwright to scrape dynamically-rendered sponsored tags
- Extend scraper to multiple search result pages
- Make dashboard using Streamlit for visual insights

---

## 👨‍💻 Created By

**Satyabrat Sahu**  
satyabratsahu71@gmail.com

---

> **Note**: This project was created as part of an internship assignment. Sponsored product data was simulated where necessary due to JavaScript-based rendering by Amazon.
