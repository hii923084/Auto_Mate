
# Vulnerability Scanner

## Overview

The **Vulnerability Scanner** is a command-line tool designed to identify vulnerabilities in specific software products using the [Vulners API](https://vulners.com/). By entering the product name and version, users can retrieve a list of known vulnerabilities, complete with details such as CVSS scores, severity ratings, and publication dates.

## Features

- **Vulnerability Search**: Quickly search for vulnerabilities based on the software product name and version.
- **CVSS Scoring**: Provides the CVSS score for each vulnerability to indicate severity.
- **Formatted Output**: Results are presented in a user-friendly format for easy readability.

## Requirements

- **Python 3.6 or higher**
- **`requests` library**

To install the required library, run:

```bash
pip install requests
```

## Getting an API Key

To access the Vulners API, you need an API key. Follow these steps to obtain one:

1. Visit the [Vulners website](https://vulners.com/).
2. Sign up for an account or log in if you already have one.
3. Navigate to the API section of your account dashboard.
4. Generate a new API key and copy it for later use in the application.

## Usage

### Clone the Repository

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   cd vulnerability-scanner
   ```

### Run the Application

2. Execute the script using Python:

   ```bash
   python vulnerability_scanner.py
   ```

### Input Parameters

3. You will be prompted to enter:
   - **Product Name**: Name of the software product (e.g., `MySQL`).
   - **Product Version**: Version of the software product (e.g., `2`).
   - **API Key**: Enter the API key you obtained from Vulners.

### View Results

4. The application will output the top vulnerabilities found, sorted by CVSS score.

## Example Output

```plaintext
Top 10 vulnerabilities for MySQL version 2:

1. Title: UBUNTU-CVE-2023-24531
   Description: Command go env is documented as outputting a shell script...
   CVSS Score: 9.8
   Severity: CRITICAL
   Published Date: 2024-07-02
   URL: https://osv.dev/vulnerability/UBUNTU-CVE-2023-24531
   --------------------------------------------------------------------------------
```

## Contributing

Contributions are welcome! If you encounter issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the [Vulners API](https://vulners.com/) for providing comprehensive vulnerability data.
- Special thanks to the open-source community for their ongoing support and contributions.
