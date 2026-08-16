# Blueprint

Blueprint is a local Streamlit app for finding a short, honest path from an idea to a goal. It combines a founder-specific reality check, a step-by-step plan, gap layers, and a live cost ledger.

## Run locally

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your Groq API key to .env
streamlit run app.py
```

The app includes a deterministic demo fallback when no API key is configured, so the full flow can be reviewed locally without making an API call.

## Data

Bundled CSV files under `data/` provide reference journeys, cost templates, and gap examples. They are loaded at runtime and are not regenerated automatically.

