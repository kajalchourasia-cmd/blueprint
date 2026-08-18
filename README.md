# Blueprint

Blueprint is an evidence-first decision system for turning an unfinished product or business idea into the next provable move.

## Product walkthrough

[Watch the Blueprint demo on Loom](https://www.loom.com/share/de86feccf09e4e1895856799e4a0542b)

Instead of producing a generic plan, Blueprint combines founder context, executable phase actions, planning priors, financial gates, and observed evidence. The interface keeps those sources visibly separate so an estimate is never presented as validation.

## Product flow

1. Describe an unfinished idea on the landing page.
2. Complete eight short onboarding questions about audience, goal, resources, prior work, and constraints.
3. Generate a personalized Roadmap & Progress dashboard.
4. Work through phases from Foundation to Growth & optimization.
5. Expand an action to see what to do, why it matters, a framework, and the done rule.
6. Mark actions complete and watch phase progress update.
7. Open the full Blueprint to inspect the complete system map, dependencies, and decision gates.
8. Review the financial plan, key signals, user inputs, data library, and product case study.

## Main surfaces

- **Landing and onboarding** — an animated idea-to-evidence entry point and an eight-question modal.
- **Roadmap & Progress** — completion, assumptions, positive signals, risks, phase navigation, executable actions, quick notes, and capital planning.
- **Full Blueprint** — a connected system map for phases, actions, dependencies, and return paths.
- **User inputs** — editable project context.
- **Data library** — inspectable CSV-backed planning sources and provenance.
- **Case study** — problem, product thesis, user goals, iterations, processing pipeline, information architecture, strategy, and reflection.

## Data model

Blueprint uses bundled CSV files rather than a database for this MVP:

- `blueprint_idea_master.csv` — idea archetypes and planning attributes.
- `blueprint_phase_actions.csv` — executable phase actions, scripts, deliverables, costs, and decision signals.
- `blueprint_signal_benchmarks.csv` — signal definitions and thresholds.
- `blueprint_financial_models.csv` — budget buckets and release conditions.
- `blueprint_evidence_events.csv` — observed evidence records.
- `founder_journeys.csv` — reference founder journeys.
- `cost_templates.csv` — money, time, relationship, health, and opportunity-cost priors.
- `gap_library.csv` and `evidence_resources.csv` — missing questions, perspectives, frameworks, and learning support.
- `phase_library.csv` — phase structure and completion signals.

The app distinguishes three provenance levels:

- **User input** describes intent and constraints.
- **Planning prior** suggests sequencing, estimates, and targets.
- **Observed evidence** records what happened outside the app and is the only source of market signals.

## Technology

- Python 3.11+
- Streamlit
- Pydantic v2
- Groq SDK and Instructor for optional structured AI generation
- Pandas and bundled CSV data
- Plotly
- Streamlit session state

The app includes a deterministic fallback, so the complete prototype works without an API key. When a Groq key is configured, Blueprint can use structured LLM generation.

## Run locally

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Optional: add a Groq API key to .env
streamlit run app.py
```

Open `http://localhost:8501`.

## Configuration and secrets

Local secrets belong only in `.env` or `.streamlit/secrets.toml`. Both are excluded from Git. Use `.env.example` and `.streamlit/secrets.toml.example` as templates.

For Streamlit Community Cloud, add secrets through the app's Advanced settings instead of committing them.

## Repository structure

```text
blueprint/
├── app.py
├── pages/
│   ├── 1_📝_Questions.py
│   ├── 2_🗺️_Your_Plan.py
│   ├── 3_⚙️_Profile_Settings.py
│   ├── 4_📊_Data_Library.py
│   ├── 5_🎛️_Inputs.py
│   └── 6_🧭_Case_Study.py
├── blueprint/
│   ├── schemas.py
│   ├── llm.py
│   ├── prompts.py
│   ├── reality_check.py
│   ├── plan_generator.py
│   ├── gap_generator.py
│   ├── cost_calculator.py
│   ├── coach.py
│   ├── state.py
│   ├── app_navigation.py
│   ├── blueprint_map.py
│   └── product_dashboard_v2.py
├── data/
├── docs/
├── scripts/
├── .streamlit/config.toml
└── requirements.txt
```

## Documentation

- [Information architecture](docs/information-architecture.md)
- [Recording guide](docs/VIDEO-TRANSCRIPT-CUES.md)
- [Clean walkthrough transcript](docs/VIDEO-TRANSCRIPT.md)
- [Case-study presentation transcript](docs/CASE_STUDY_PRESENTATION_TRANSCRIPT.md)

## Deployment

The production entrypoint is `app.py` on the `main` branch. Streamlit Community Cloud installs dependencies from the root `requirements.txt` file.

## Current scope

This is an MVP. Project state is held in Streamlit session state, and planning data is bundled with the repository. Durable accounts, collaborative projects, version history, and production evidence storage are future iterations.
