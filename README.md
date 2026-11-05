# EV Charging Station Finder

**Case 26 | Software Engineering and Project Management (SEPM)**

A Python-based academic prototype for finding nearby electric vehicle (EV) charging stations and reserving available chargers. The project demonstrates software development, automated testing, continuous integration, Docker hardening, code quality checks, and responsible handling of sample data.

> **Project status:** Academic demonstration prototype. Station availability and reservations use local sample data; this is not a live commercial charging network or production booking service.

## Student details

| Field | Details |
|---|---|
| Name | Kavyashree Visaji |
| Roll number | 26 |
| USN | ENG24CS0094 |
| Case | 26 – EV Charging Station Finder |
| Submission date | 06 November 2026 |
| Repository | [EV-CHARGING-STATION-FINDER](https://github.com/kavyashree-visaji02/EV-CHARGING-STATION-FINDER) |

## Project overview

The assignment scenario describes a startup planning an application that shows the availability of **300 chargers** and lets drivers reserve them. A major concern is avoiding situations where a charger appears available but is already reserved or occupied.

This repository implements a small proof of concept focused on **nearest-charger search** and **reservation conflict handling**. The project follows a **Prototype** process model with **Scrum** practices, as specified in the Case 26 assignment.

## Main features

- Search for nearby charging stations using distance calculations.
- Find a suitable available charger from sample station data.
- Reserve an available charger.
- Reject repeat reservations and unavailable chargers.
- Demonstrate a simple browser flow using Flask and Selenium.
- Run automated unit and integration tests.
- Check code quality, test coverage, and illustrative module risk.
- Use masked example customer data and a basic security-pattern audit.

## Repository guide

| File or path | Purpose |
|---|---|
| `app.py` | Flask demonstration application for search and reservation |
| `charger_search.py` | Charger search logic |
| `distance.py` | Distance calculation helpers |
| `reservation.py` | Charger reservation logic |
| `stations.py` | Sample station information |
| `test_reservation.py` | Reservation unit tests |
| `test_search.py` | Search-related tests |
| `test_integration.py` | Search-to-reservation integration tests |
| `test_selenium.py` | Browser-based end-to-end test |
| `.github/workflows/python-tests.yml` | GitHub Actions test workflow |
| `Dockerfile.original` | Original Docker image configuration |
| `Dockerfile.hardened` | Smaller, non-root Docker image configuration |
| `buggy_functions.py` | Sample functions for defect analysis |
| `ruff_report.txt` | Saved static-analysis output |
| `module_risk.py` | Illustrative module risk assessment |
| `quality_gate.py` | Demonstration of coverage-based quality threshold |
| `performance_comparison.py` | Manual vs. AI-style implementation benchmark |
| `security_audit.py` | Basic scan for selected secret and personal-data patterns |
| `sample_data_masked.json` | Synthetic masked example data |
| `.gitignore` | Excludes local and potentially sensitive files |

## Requirements and setup

Use **Python 3.11+** in a local environment or GitHub Codespaces.

Clone the repository:

```bash
git clone https://github.com/kavyashree-visaji02/EV-CHARGING-STATION-FINDER.git
cd EV-CHARGING-STATION-FINDER
```

Create an optional virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install test and application tools as needed:

```bash
python -m pip install flask pytest pytest-cov selenium ruff
```

**Note:** The repository contains a file named `requirements.py`; it is not a conventional `requirements.txt` dependency manifest. The installation command above lists the tools used in the demonstrated workflow.

## Run the application

Start the Flask prototype:

```bash
python app.py
```

In Codespaces, use the forwarded port or the URL printed by Flask to open the application. The demonstration exposes search and reservation flows; it does not connect to a real charging-provider API.

## Run tests

Unit and integration tests:

```bash
python -m pytest test_reservation.py test_search.py test_integration.py -v
```

Coverage check:

```bash
python -m pytest test_reservation.py test_search.py test_integration.py \
  --cov=reservation --cov=charger_search --cov=distance \
  --cov-report=term-missing
```

For the previously recorded isolated unit/integration run, **8 tests passed** and total coverage was **85.71%** (about 86%):

| Module | Recorded coverage |
|---|---:|
| `charger_search.py` | 100% |
| `distance.py` | 90% |
| `reservation.py` | 75% |

The Selenium test was run separately in the demonstrated workflow:

```bash
python -m unittest test_selenium -v
```

**Recorded Selenium result:** 1 test passed. Browser automation requires Chrome/Chromium and a compatible driver. Running all tests together may require resetting shared sample reservation state between tests.

## Quality and performance checks

Run the threshold demonstration:

```bash
python quality_gate.py
```

In the recorded coverage-based exercise, the **80% threshold passed** and the **90% threshold failed**, using the measured 85.71% coverage. This is a demonstration quality gate, not evidence of a full SonarQube scan.

Run the execution-time comparison:

```bash
python performance_comparison.py
```

One recorded benchmark reported approximately **0.2270 µs per call** for the manual version and **0.2128 µs per call** for the AI-style version, using 100,000 iterations across five repeats. These microbenchmarks vary by environment and are not evidence of production performance.

Run static analysis:

```bash
ruff check .
```

The saved `ruff_report.txt` is the evidence for the earlier static-analysis exercise; review current output before making any claims about the latest code state.

## Docker hardening

The repository compares an original Python-based image with a hardened image using a smaller base and a non-root user.

```bash
docker build -f Dockerfile.original -t ev-finder-original .
docker build -f Dockerfile.hardened -t ev-finder-hardened .
docker run --rm ev-finder-hardened
```

In the recorded exercise, the original image size was approximately **1.6 GB**, compared with approximately **187 MB** for the hardened image; the hardened container run reported **6 tests passed**. Image sizes depend on the Docker environment and build cache.

## Security and privacy

The project includes `.gitignore`, `sample_data_masked.json`, and `security_audit.py` to demonstrate basic privacy safeguards.

```bash
python security_audit.py
```

The recorded audit returned **0 findings for its configured patterns**. This does **not** prove that the repository is free of all secrets or personal data. The sample masked data is synthetic. Do not commit real driver identities, precise location histories, API keys, credentials, or private keys. If a real secret is exposed, revoke or rotate it and address the Git history; adding it to `.gitignore` alone is insufficient.

## Development workflow

- **Process model:** Prototype
- **Agile method:** Scrum
- **Version control:** Git and GitHub
- **CI:** GitHub Actions workflow
- **Testing:** Python unit/integration tests and Selenium
- **Code analysis:** Ruff and manual/AI-assisted review
- **Containerization:** Docker

Some assignment activities, such as classmate review, a three-user usability study, and a SonarQube dashboard, require separate evidence and should not be represented as completed solely because they are described in the report.

## Academic use and AI disclosure

This project was developed for **Case 26 – EV Charging Station Finder**. ChatGPT assisted with planning, drafting, code examples, reviews, and documentation. AI suggestions require human verification and testing. Only actual executed results should be reported as measured outcomes.

**Prepared by:** Kavyashree Visaji  
**USN:** ENG24CS0094  
**Submission date:** 06/11/2026
