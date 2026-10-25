# AI Data Analyst

CSV profiling and safe, deterministic data analysis with downloadable summaries.

## Status
Portfolio MVP / learning project. It is not represented as production-deployed. Before real-world use, review security, privacy, evaluation, reliability, and deployment requirements.

## Setup (Windows PowerShell)
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run
See the command in the project section below. This starter is designed to run locally with demo/sample data and no API key.

## Engineering checklist
- [ ] Run the app locally and capture a screenshot
- [ ] Run tests: `python -m pytest`
- [ ] Add real evaluation examples and report results
- [ ] Review input validation, error handling, logging, and secrets
- [ ] Add a deployment guide only after testing deployment
- [ ] Update this README with verified behavior and limitations

## Run
```powershell
streamlit run app.py
```

Upload a CSV to inspect rows, missing values, summary statistics, and a basic chart. Do not upload sensitive or confidential data.


## Recommended real AI integration
- **Framework choice:** Pandas + constrained tools; optional LangGraph
- **Integration pattern:** CSV profiling, safe chart/table tools, deterministic calculations
- **Validation:** pytest + golden CSV cases

Use a provider adapter and typed outputs. Do not install every framework into every app: choose the smallest appropriate set to reduce dependency conflicts and demonstrate intentional engineering decisions.
