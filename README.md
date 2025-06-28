# AI-Repo
# 🔍 ReconAI — AI-Enhanced OSINT Recon Tool

> A powerful Python tool that automates OSINT data collection and enhances it with AI for faster, smarter recon.

## 🚀 Project Overview

ReconAI is an advanced Open-Source Intelligence (OSINT) reconnaissance tool designed to streamline and enhance the process of gathering publicly available information. Leveraging a combination of traditional OSINT techniques and cutting-edge Artificial Intelligence, ReconAI provides a comprehensive solution for security researchers, penetration testers, and investigative journalists to collect, analyze, and report on target data with unprecedented efficiency and insight. The tool aims to transform raw OSINT data into actionable intelligence by identifying patterns, predicting potential threats, and presenting findings in a clear, structured, and easily digestible format.

## 🌟 Key Features

- 🌐 **Domain & Subdomain Enumeration**: Discover all associated domains and subdomains for a given target, providing a broader attack surface view.
- 🕵️ **Social Media Profile Scraper**: Automate the collection of public information from popular social media platforms like LinkedIn, GitHub, and Twitter, offering insights into an individual's or organization's online presence.
- 🧠 **AI-based Threat Vector Prediction**: Utilize advanced AI models to analyze collected data and predict potential threat vectors, vulnerabilities, and attack surfaces, enabling proactive security measures.
- 📊 **Named Entity Recognition (NER)**: Automatically identify and classify key entities (e.g., persons, organizations, locations) within unstructured text data, facilitating deeper analysis and correlation.
- 📄 **Generates Clean, Structured PDF/Markdown Reports**: Produce professional, easy-to-read reports in both PDF and Markdown formats, summarizing findings and providing actionable intelligence.
- 🖥️ **Optional GUI with Streamlit**: An intuitive graphical user interface built with Streamlit for users who prefer a visual interaction over command-line operations.

## 🛠️ Technical Specifications

### Core Technologies

- **Python 3.10+**: The primary programming language for the entire project, chosen for its versatility, extensive libraries, and strong community support.

### Key Libraries & Frameworks

- `requests`: For making HTTP requests to interact with web services and APIs.
- `beautifulsoup4`: For parsing HTML and XML documents, essential for web scraping tasks.
- `whois`: A Python library for retrieving WHOIS information for domain names.
- `shodan`: The official Python library for interacting with the Shodan API, used for identifying internet-connected devices.
- `nltk` (Natural Language Toolkit): A powerful library for working with human language data, used for text processing and analysis.
- `spacy`: An industrial-strength natural language processing (NLP) library, specifically for Named Entity Recognition (NER) and other advanced text analysis.
- `openai`: The official OpenAI Python library, used for integrating with OpenAI's powerful AI models for threat vector prediction and other AI-enhanced features.

### Optional Components

- `streamlit`: A fast way to build and share data apps, used for developing the optional graphical user interface.
- `reportlab`: A powerful open-source Python library for creating PDF documents, used for generating structured PDF reports.
- `llama-cpp-python`: Python bindings for `llama.cpp`, enabling the use of local Large Language Models (LLMs) for AI analysis without relying solely on cloud-based services.

## ⚙️ Installation Guide

To get ReconAI up and running on your system, follow these steps:

### 1. Clone the Repository

First, clone the ReconAI GitHub repository to your local machine using `git`:

```bash
git clone https://github.com/yourusername/reconai.git
cd reconai
```

### 2. Install Dependencies

Navigate into the cloned directory and install the required Python packages. It is highly recommended to use a virtual environment to manage dependencies and avoid conflicts with other Python projects.

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

ReconAI utilizes an `.env` file to securely store API keys and other sensitive configuration details. This file is ignored by Git to prevent accidental exposure of credentials.

Create a `.env` file in the root directory of the project:

```bash
touch .env
```

Open the `.env` file and add your API keys for services like Shodan, OpenAI, etc. (if applicable). Refer to the respective service documentation for obtaining your API keys.

```
# Example .env file content
SHODAN_API_KEY=your_shodan_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Download NLTK Data

Some functionalities, particularly those related to NLP, require NLTK data. You can download the necessary data by running a Python script:

```python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
```

### 5. Download SpaCy Models

For Named Entity Recognition (NER), SpaCy models are required. Download a suitable model, for example, the `en_core_web_sm` model:

```bash
python -m spacy download en_core_web_sm
```

## 🚀 Usage

### Command-Line Interface (CLI)

ReconAI can be run directly from the command line. The main entry point is `reconai.py`. You can specify various options and targets as command-line arguments.

```bash
python reconai.py --target example.com --modules whois,subdomain,social --report pdf
```

Detailed usage instructions and available command-line arguments can be found by running:

```bash
python reconai.py --help
```

### Graphical User Interface (GUI)

For a more interactive experience, you can launch the Streamlit-based GUI:

```bash
streamlit run dashboard/app.py
```

This will open ReconAI in your web browser, providing a user-friendly interface to configure and run reconnaissance tasks.

## 📂 Project Structure

```
ReconAI/
├── reconai.py                    # Main entry point for CLI operations
├── requirements.txt              # Python dependencies for the project
├── README.md                     # Comprehensive project documentation
├── .env                          # Environment variables and API keys (ignored by git)
├── /modules                      # Contains core reconnaissance modules
│   ├── whois_lookup.py           # Module for performing WHOIS lookups
│   ├── subdomain_enum.py         # Module for enumerating subdomains
│   ├── social_scraper.py         # Module for scraping social media profiles
│   ├── shodan_lookup.py          # Module for Shodan API integrations
│   └── ai_analyzer.py            # Module for AI-based threat prediction and NER
├── /utils                        # Houses helper functions and utilities
│   ├── report_generator.py       # Utility for generating various report formats
│   ├── config_loader.py          # Utility for loading configurations and API keys
│   └── logger.py                 # Centralized logging utility
├── /reports                      # Directory for storing generated reconnaissance reports
│   └── targetname_report.pdf     # Example generated PDF report
├── /dashboard                    # Contains files related to the Streamlit GUI
│   ├── app.py                    # Main Streamlit application file
│   └── components.py             # Reusable Streamlit UI components
├── /models                       # Stores optional LLM/NER models
│   └── spacy_ner_model/          # Directory for SpaCy NER models
└── /docs                         # Documentation, diagrams, and research notes
    ├── recon_flowchart.png       # Example architecture diagram
    └── module_notes.md           # Detailed notes on module development
```

## 🤝 Contributing

We welcome contributions to ReconAI! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name` or `bugfix/your-bug-fix-name`.
3.  **Make your changes** and ensure they adhere to the project's coding standards.
4.  **Write clear and concise commit messages.**
5.  **Push your branch** to your forked repository.
6.  **Open a Pull Request** to the `main` branch of the original ReconAI repository, describing your changes in detail.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support & Contact

For any questions, issues, or support, please open an issue on the GitHub repository. We will do our best to assist you.

---

*Authored by Manus AI*


