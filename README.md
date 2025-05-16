# Diabetes Data Processing & Clustering Pipeline

> _From raw CSV to cleaned data, exploratory analysis, K-means clusters, and publication-ready visuals — all reproducible with a single command._

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Folder Structure](#folder-structure)
3. [Quick Start](#quick-start)
4. [Detailed Usage](#detailed-usage)
   * [Local run](#local-run)
   * [Docker](#docker)
5. [Scripts Explained](#scripts-explained)
6. [Configuration](#configuration)
7. [Outputs](#outputs)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview
This repository contains a **five-stage data science pipeline** for the _PIMA Indians Diabetes_ dataset (or any CSV with the same schema):

1. **Load** – read raw CSV into a canonical format.  
2. **Pre-process** – clean, impute, encode & discretise data.  
3. **EDA** – compute descriptive statistics & save textual reports.  
4. **Model** – train _K-means_ clusters, export metrics, and persist the model.  
5. **Visualise** – generate publication-ready PNG plots.

The pipeline is fully containerised for reproducibility and can be executed either **locally** (Python 3.9+) or inside **Docker**.

---

## Folder Structure
```
bd-a1/
├── Dockerfile              # Minimal Python image + pipeline entrypoint
├── Bonus.txt               # Optional assignment notes
├── diabetes.csv            # Raw dataset (24 kB)
├── *.py                    # Load, dpre, eda, model, vis scripts
├── final.sh                # Convenience wrapper (build/run/clean)
├── service-result/         # All auto-generated artefacts (git-ignored)
│   ├── eda-in-*.txt        # EDA text dumps
│   ├── k.txt               # Cluster membership counts
│   ├── vis_*.png           # Plots
│   └── …
└── README.md               # ← you are here
```

> **Tip:** change the output directory with `--out <PATH>` or the `RESULTS_DIR` env variable (see below).

---

## Quick Start
```bash
# 1. Clone & enter repo
git clone https://github.com/<you>/bd-a1.git
cd bd-a1

# 2. Create virtualenv & install deps
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Run the entire pipeline
bash final.sh run                # or: python -m pipeline --csv diabetes.csv

# 4. Open results
xdg-open service-result/vis_1.png   # Linux example
```

---

## Detailed Usage
### Local run
Every script is CLI-friendly (built with `argparse`). Typical flags:
```
--csv  <path>     # input CSV  (default: diabetes.csv)
--out  <dir>      # output dir (default: ./service-result)
--log-level INFO  # DEBUG, INFO, WARNING, ERROR
```
Example:
```bash
python dpre.py --csv diabetes.csv --out service-result --log-level DEBUG
```

If you prefer a single entrypoint, use the meta-script:
```bash
python -m pipeline --csv diabetes.csv --out results
```

### Docker
Build once, run anywhere:
```bash
# Build image (tagged bd-a1)
docker build -t bd-a1 .

# Execute pipeline – mounts current repo read-only and writes results to ./service-result
docker run --rm -v "$PWD":/app:ro -v "$PWD/service-result":/service-result bd-a1
```
_Pro tip: customise input/output via environment variables:_
```bash
docker run -e CSV_PATH=/app/diabetes.csv -e RESULTS_DIR=/service-result bd-a1
```

---

## Scripts Explained
| Script      | Purpose (⚡ = performance-critical) |
|-------------|------------------------------------|
| **load.py** | Read raw CSV → `<out>/loaded.csv`; avoid global execution when imported. |
| **dpre.py** | Clean/impute, optional discretisation, export `<out>/clean.csv`; uses `pandas` & `scikit-learn`. ⚡ |
| **eda.py**  | Compute stats (describe, missingness, corr) → `eda-in-*.txt`. |
| **model.py**| Fit K-means, elbow-curve selection, save cluster counts → `k.txt`, serialize model (`.pkl`). ⚡ |
| **vis.py**  | Pair-plots & cluster scatter → `vis_*.png`. |
| **final.sh**| Helper: `build`, `run`, `clean`, `shell` targets. |
| **Dockerfile**| Slim `python:3.9-slim` base, installs only essentials. |

---

## Configuration
Parameterise the pipeline via either **CLI flags** or **environment variables** (take precedence):

| Variable      | Description                     | Default              |
|---------------|---------------------------------|----------------------|
| `CSV_PATH`    | Path to raw CSV                 | `diabetes.csv`       |
| `RESULTS_DIR` | Where to write artefacts        | `service-result`     |
| `N_CLUSTERS`  | Force K value (skip elbow test) | auto-select          |
| `LOG_LEVEL`   | `DEBUG/INFO/WARN/ERROR`         | `INFO`               |

---

## Outputs
All generated files land in **`$RESULTS_DIR`**:

* `loaded.csv` / `clean.csv` – intermediate datasets
* `eda-in-*.txt` – EDA text summaries (nulls, stats, correlations …)
* `k.txt` – table of cluster IDs → counts
* `model.pkl` – pickled `sklearn.cluster.KMeans`
* `vis_1.png`, `vis_2.png` – plots (pairplot, cluster scatter)

> _Feel free to rename or reorganise these; just update `vis.py` accordingly._

---

## Contributing
Pull requests are welcome! Please:
1. **Fork** → feature branch → PR.  
2. Run `pre-commit run --all-files` (black, flake8, isort).  
3. Add / update **pytest** unit tests.

---

## License
This project is licensed under the **MIT License** – see [`LICENSE`](LICENSE) for details.

---

_Questions or feedback? Reach out via the issue tracker – happy hacking!_
