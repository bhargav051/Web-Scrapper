## README/ How to run

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
   
2. **Install Dependencies**:
   ```bash
   pip install psycopg2 requests beautifulsoup4 python-dotenv
   ```
   
3. **Run the Scraping Script**:
   ```bash
   python scrape_data.py
   ```
   
4. **Run the CSV Generation Script**:
   ```bash
   python generate_csv.py
   ```
   
5. **Access the PostgreSQL Database**:
   - Ensure PostgreSQL is running and accessible.
   - Check the `config.py` file for database connection settings
