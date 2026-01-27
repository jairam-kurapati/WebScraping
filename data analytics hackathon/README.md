# 📱 Flipkart Mobile Phones Web Scraping & Data Analysis

## 📌 Project Description
This project demonstrates **web scraping and basic data analytics** by extracting mobile phone information from **Flipkart** for products priced under **₹50,000**.  
The scraped data is cleaned, structured, and stored in a **CSV file** for further analysis or visualization.

The project is built using **Python**, leveraging industry-standard libraries such as **Requests**, **BeautifulSoup**, and **Pandas**.

---

## 🎯 Objectives
- Scrape mobile phone data from multiple Flipkart search result pages  
- Extract key product attributes:
  - Product Name  
  - Price  
  - Description (key features)  
  - Reviews  
- Store the collected data in a structured CSV format  
- Enable further analysis using data analytics tools  

---

## 🛠️ Tech Stack & Libraries Used

| Technology | Purpose |
|---------|--------|
| **Python** | Core programming language |
| **Requests** | Fetch web pages via HTTP |
| **BeautifulSoup (bs4)** | Parse and extract HTML data |
| **Pandas** | Data cleaning, structuring, and CSV export |
| **lxml** | Fast HTML parsing |

---

## 📂 Project Structure
```
📁 Flipkart-Web-Scraping
│
├── main.py
├── flipkart_mobiles_under_50000.csv
└── README.md
```

---

## 🔄 How the Code Works

### 1️⃣ Pagination Handling
Scrapes multiple pages instead of a single page to collect a larger dataset.

### 2️⃣ Sending HTTP Requests
Uses the `requests` library to fetch HTML content from Flipkart.

### 3️⃣ HTML Parsing
BeautifulSoup parses raw HTML into a searchable structure.

### 4️⃣ Data Extraction
The script extracts:
- Product Name  
- Price  
- Description  
- Reviews  

Each value is appended to Python lists.

### 5️⃣ DataFrame Creation
Raw lists are converted into a structured Pandas DataFrame.

### 6️⃣ Export to CSV
The final dataset is saved as a CSV file.

---

## 📊 Output
- **CSV File:** `flipkart_mobiles_under_50000.csv`
- Compatible with Excel, Google Sheets, and Python analysis tools

---

## ⚠️ Limitations
- Flipkart frequently changes class names  
- Requests without headers may be blocked  
- Some products may have missing data  

---

## 🔮 Future Improvements
- Add request headers & retry logic  
- Improve missing data handling  
- Scrape ratings and review counts  
- Add data visualization  
- Build a Flask dashboard  

---

## 📚 Learning Outcomes
- Web scraping fundamentals  
- Working with real-world HTML  
- Data cleaning using Pandas  
- Pagination handling  

---

## ⚖️ Disclaimer
This project is for **educational purposes only**.  
All data belongs to **Flipkart** and is publicly accessible.

---

## 🙌 Author
**Jairam Kurapati**  
B.Tech (AI & ML)  
India
