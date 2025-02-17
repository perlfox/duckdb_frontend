# DuckDB Frontend (ddbfe.py)

## Overview
`ddbfe.py` is a Python script designed to provide a frontend interface for interacting with DuckDB, an in-process SQL OLAP database management system. This script allows users quickly view the structure and data of a DuckDB data file.

## Features
- Connect to DuckDB databases
- Execute SQL queries
- Fetch and display query results
- Handle database transactions

## Requirements
- Python 3.6 or higher
- DuckDB Python package

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/perlfox/duckdb_frontend.git
    ```
2. Navigate to the project directory:
    ```sh
    cd duckdb_frontend
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
     ```

## Usage
1. Run the script:
    ```sh
    stramlit run ddbfe.py
    ```
2. Follow the on-screen instructions to connect to your DuckDB database and execute SQL queries.

## Example
```python
import duckdb

# Connect to DuckDB
con = duckdb.connect('my_database.db')

# Execute a query
con.execute('SELECT * FROM my_table')

# Fetch results
results = con.fetchall()
print(results)
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please open an issue on GitHub.
