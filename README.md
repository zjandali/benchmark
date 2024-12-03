# Legal Case Outcome Prediction Benchmark

## Overview

This project implements a comprehensive benchmark system for evaluating large language models' (LLMs) ability to predict legal case outcomes in contract law. The benchmark uses a dataset of 100 contract dispute cases from the California jurisdiction, focusing on marketing service agreements between tech startups and marketing firms. The dataset was generated using Claude and tested on GPT-4o-Mini to make things interesting.

## Dataset Structure

### Contract Case Summaries

The dataset (`contract_case_summaries.json`) contains detailed case information including:

- Case titles and jurisdictions
- Party information (tech startups vs marketing firms)
- Contract details
  - Delivery dates
  - Payment terms
  - Performance obligations
- Timeline of events
- Legal issues
- Arguments from both parties
- Actual outcomes and reasoning
- Metadata (complexity, statutes, precedents)

Example of dataset structure:

```json:contract_case_summaries.json
{
        "case_title": "Case Title 4",
        "jurisdiction": "United States District Court for California",
        "facts": {
            "parties": {
                "plaintiff": "Plaintiff Company 4, a tech startup.",
                "defendant": "Defendant Agency 4, a marketing firm."
            },
            "contract_details": {
                "type": "Service Agreement for Marketing Campaign",
                "key_terms": {
                    "delivery_date": "December 5, 2022",
                    "payment": "$30000 upon delivery of services",
                    "performance_obligations": "Execution of a targeted advertising campaign for product 4."
                }
            },
            "timeline_of_events": [
                {
                    "date": "July 5, 2022",
                    "event": "Contract signed."
                },
                {
                    "date": "September 14, 2022",
                    "event": "Defendant requests delay; plaintiff refuses."
                },
                {
                    "date": "December 5, 2022",
                    "event": "Defendant fails to deliver services."
                },
                {
                    "date": "December 9, 2022",
                    "event": "Plaintiff files lawsuit."
                }
            ]
        },
        "legal_issues": {
            "primary_issues": [
                "Did Defendant Agency 4 breach the contract by failing to deliver services by the specified date?",
                "Is Plaintiff Company 4 entitled to damages for losses incurred?"
            ],
            "secondary_issues": [
                "Does the defendant's staffing issues qualify as a valid excuse under force majeure?"
            ]
        },
        "plaintiff_arguments": [
            "Defendant failed to deliver on time, constituting a material breach.",
            "Plaintiff seeks damages for business losses incurred.",
            "Rejection of extension was reasonable given the time sensitivity."
        ],
        "defendant_arguments": [
            "Force majeure excuses delays due to unforeseen circumstances.",
            "Plaintiff failed to mitigate damages.",
            "Losses were not directly caused by the breach."
        ],
        "outcome": {
            "decision": "Judgment in favor of Plaintiff Company 4.",
            "legal_reasoning": [
                "Defendant breached the contract by failing to deliver.",
                "Force majeure was deemed inapplicable.",
                "Losses were foreseeable and directly linked to the breach."
            ],
            "remedies_awarded": {
                "damages": "$90000 for lost business opportunities.",
                "attorney_fees": "Defendant to pay legal costs.",
                "interest": "Pre-judgment interest applied."
            }
        },
        "metadata": {
            "complexity": "Moderate",
            "relevant_statutes": [
                "California Commercial Code \u00a7 3300"
            ],
            "precedents_cited": [
                "Precedent Case 4"
            ],
            "date": "February 14, 2023"
    }
}
```

## Project Components

### 1. Environment Setup

The project uses Poetry for dependency management with the following key dependencies:

```toml:pyproject.toml
[tool.poetry.dependencies]
python = "^3.13"
python-dotenv = "^1.0.1"
openai = "^1.56.0"
pandas = "^2.2.3"
matplotlib = "^3.9.3"
seaborn = "^0.13.2"
scikit-learn = "^1.5.2"
```

### 2. Data Processing Pipeline

The benchmark notebook (`benchmark.ipynb`) implements the following workflow:

1. Data loading and preprocessing
2. Prompt generation
3. Model evaluation
4. Results analysis and visualization

### 3. Evaluation Metrics

The benchmark evaluates LLM performance on multiple dimensions:

- Decision accuracy (binary outcome prediction)
- Legal reasoning alignment
- Damages amount prediction accuracy
- Statutory citation relevance
- Precedent application accuracy

## Case Pattern Analysis

### Common Characteristics

1. **Timeline Pattern**:

   - Contracts signed: July 2022
   - Delay requests: September 2022
   - Service failures: December 2022
   - Lawsuits filed: Within 4-5 days of failure

2. **Dispute Pattern**:
   - Consistent force majeure defense
   - Similar breach patterns
   - Standardized damage calculations

### Legal Principles Tested

- Contract breach determination
- Force majeure applicability
- Damage calculation methodology
- Duty to mitigate
- Foreseeability of losses

## Technical Implementation

### Data Processing

The project uses pandas for data manipulation and analysis:

```python:benchmark.ipynb
import openai
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
with open('contract_case_summaries.json', 'r') as file:
    ground_truth_cases = json.load(file)

ground_truth_df = pd.DataFrame(ground_truth_cases)
```

### Visualization

Implements matplotlib and seaborn for result visualization:

- Decision distribution plots
- Damages correlation analysis
- Timeline pattern visualization
- Legal reasoning consistency metrics

## Research Applications

### Primary Use Cases

1. **Legal AI Development**:

   - Training data for legal prediction models
   - Benchmark for legal reasoning capabilities
   - Testing for bias in legal AI systems

2. **Legal Education**:

   - Case study material
   - Pattern recognition training
   - Legal reasoning assessment

3. **Legal Practice Analysis**:
   - Contract dispute pattern identification
   - Risk assessment metrics
   - Settlement value estimation

## Limitations and Considerations

### Dataset Constraints

1. **Jurisdictional Limitation**:

   - California-specific cases
   - Single industry focus (tech/marketing)
   - Limited time period (2022-2023)

2. **Case Complexity**:
   - Moderate complexity level
   - Similar fact patterns
   - Limited variety in legal issues

### Ethical Considerations

1. **AI Decision Making**:

   - Not intended for autonomous legal decisions
   - Supplementary tool only
   - Requires human oversight

2. **Bias Mitigation**:
   - Regular dataset audits
   - Diversity in case selection
   - Transparent evaluation metrics

## Future Development

### Planned Enhancements

1. **Dataset Expansion**:

   - Multiple jurisdictions
   - Diverse industry sectors
   - Various complexity levels

2. **Model Integration**:

   - Multiple LLM support
   - Custom model training
   - Hybrid evaluation systems

3. **Analysis Tools**:
   - Advanced visualization
   - Statistical analysis
   - Pattern recognition

## License

This project is for educational and research purposes only. The case data, while synthetic, is structured to reflect real-world legal patterns and should be used accordingly.
