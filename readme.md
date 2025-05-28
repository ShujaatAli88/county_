# 🕷️ C-Clerk County Crawler

This project is a **web crawler** built to extract structured data from the **C-Clerk County** website. The crawler is designed with a modular approach for scalability and maintainability. Extracted data is stored in **Airtable** for easy access and collaboration.

---

## 📌 Features

- Modular architecture (separate files for requests, parsing, storing)
- Environment variables for secure credentials
- Logs activity using `loguru`
- Stores data in Airtable via Airtable API
- Handles retries and error logging
- Easily extendable for other counties

---

## 🔧 Tech Stack & Tools Used

| Tool/Library         | Purpose                                      |
|----------------------|----------------------------------------------|
| `requests`           | HTTP requests to fetch web pages             |
| `loguru`             | Logging crawler activities and errors        |
| `python-dotenv`      | Load environment variables from `.env` file  |
| `airtable-python-wrapper` | Store and manage data in Airtable       |
| `lxml` (optional) | HTML parsing                                    |
| `os`, `time`, etc.   | Standard Python libraries                    |

---

## 🧩 Project Structure

```
county_/
├── .env                        # Airtable API keys and base info
├── main.py                     # Entry point
├── c_clerk_crawler.py              # Requests logic
├── airtable_handler.py      # Push to Airtable
├── tmp/
│   └── logs.log             # Log file created by loguru
├── requirements.txt            # Python dependencies
└── README.md                   # Documentation
```

---

## ✅ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/ShujaatAli88/county_.git
   cd county_
   ```

2. **Create and activate virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**  
   Create a `.env` file at the root:
   ```
   AIRTABLE_API_KEY=your_airtable_api_key
   AIRTABLE_BASE_ID=your_airtable_base_id
   ```

---

## 🚀 How to Run

```bash
python main.py
```

---

## 📤 Output

- Data is stored in the specified Airtable table.
- Logs are saved in `tmp/logs.log`.

---

## 📬 Contact

For questions or suggestions, reach out to [Shujaat Ali](mailto:shujaatalee888@gmail.com).
