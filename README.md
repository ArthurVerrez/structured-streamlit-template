# Structured Streamlit Template 🏗️

A simple, opinionated Streamlit template designed to get your apps up and running quickly with a clear structure.

## ✨ Features

- **Structured Layout:** Code is organized into sections (`header`, `body`, `footer`, `sidebar`, `metadata`) for better maintainability.
- **Centralized Configuration:** Key settings like app title, version, links, and session state defaults are managed in `config.py`.
- **Static Files:** Includes basic CSS styling (`static/style.css`) and demonstrates serving static images.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ArthurVerrez/structured-streamlit-template.git
    cd structured-streamlit-template
    ```

2.  **Create and activate a virtual environment (Recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

Once the setup is complete, run the Streamlit application:

```bash
streamlit run app.py
```

The application should open automatically in your web browser.

## 📁 Project Structure

```
.
├── app.py                 # Main Streamlit application script
├── config.py              # Central configuration file
├── README.md              # This file
├── requirements.txt       # Project dependencies (You need to create this)
├── sections/              # Directory for different app sections
│   ├── __init__.py
│   ├── body.py
│   ├── footer.py
│   ├── header.py
│   ├── metadata.py
│   └── sidebar.py
└── static/                # Directory for static assets
    ├── gh_fav_logo.png
    ├── st_fav_logo.png
    └── style.css
```

## 🔧 Customization

- **Configuration:** Modify `config.py` to change the app title, icons, links, version, etc.
- **Content:** Edit the Python files within the `sections/` directory to change the content and layout of each part of the app.
- **Styling:** Update `static/style.css` to customize the appearance.
- **Body:** Replace the placeholder content in `sections/body.py` with your application's main logic and components.
