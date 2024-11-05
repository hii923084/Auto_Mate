# Vulnerability Scanner

## Overview

The **Vulnerability Scanner** is a command-line tool designed to retrieve and display known vulnerabilities for specific software products based on product name and version. Utilizing the Vulners API, this tool allows users to quickly identify potential security issues along with essential details like CVSS scores, severity ratings, and publication dates.

## Features

- **Vulnerability Search**: Finds vulnerabilities based on product name and version input.
- **CVSS Scoring**: Provides CVSS scores for quick severity assessment.
- **Detailed Information**: Displays vulnerability descriptions, severity, publication dates, and URLs for further information.
- **Sorted Output**: Results are displayed in descending order of CVSS score for easy prioritization.

## Prerequisites

1. **Python**: Ensure Python 3.6 or higher is installed. You can download it from [python.org](https://www.python.org/).
2. **Vulners API Key**: Obtain an API key from [Vulners](https://vulners.com/) by creating a free account and generating an API key under the "API Keys" section in your account dashboard.
3. **Requests Library**: Install the `requests` library, if not already installed.

   ```bash
   pip install requests
   ```

## Installation and Setup

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```bash
   git clone git@github.com:hii923084/Auto_Mate.git
   cd vulnerability-scanner
   ```

2. **Add Your API Key**: Open the file `vulnerability_scanner.py` and replace the placeholder `YOUR_API_KEY` with your actual Vulners API key.

## Usage

1. **Run the Application**: Execute the script using Python:

   ```bash
   python vulnerability_scanner.py
   ```

2. **Input Parameters**:
   - You will be prompted to enter:
     - **Product Name**: Name of the software product (e.g., `MySQL`).
     - **Product Version**: Version of the software product (e.g., `2.3.4`).

3. **View Results**: The application will display the top vulnerabilities found for the specified product and version, sorted by CVSS score.

### Example Output

```plaintext
Top 10 vulnerabilities for MySQL version 2.3.4:

1. Title: UBUNTU-CVE-2023-24531
   Description: Command go env is documented as outputting a shell script...
   CVSS Score: 9.8
   Severity: CRITICAL
   Published Date: 2024-07-02
   URL: https://osv.dev/vulnerability/UBUNTU-CVE-2023-24531
--------------------------------------------------------------------------------
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments

- Special thanks to [Vulners](https://vulners.com/) for providing comprehensive vulnerability data.
- Thanks to the open-source community for their ongoing support and contributions.

---
