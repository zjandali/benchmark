import json

# Function to load JSON file
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to create prompts from JSON data
def create_prompts_from_json(json_cases):
    prompts = []
    for case in json_cases:
        prompt = f"""You are a legal expert specializing in U.S. contract law. Based on the following case details, predict the court's decision and provide the legal reasoning.

---

**Case Title**: {case.get('case_title', 'N/A')}

**Jurisdiction**: {case.get('jurisdiction', 'N/A')}

### **Facts**

#### **Parties**
- **Plaintiff**: {case['facts']['parties'].get('plaintiff', 'N/A')}
- **Defendant**: {case['facts']['parties'].get('defendant', 'N/A')}

#### **Contract Details**
- **Type**: {case['facts']['contract_details'].get('type', 'N/A')}
- **Key Terms**:
"""

        # Add key terms
        key_terms = case['facts']['contract_details'].get('key_terms', {})
        for term, description in key_terms.items():
            prompt += f"  - **{term.replace('_', ' ').title()}**: {description}\n"

        # Add timeline of events
        prompt += "\n#### **Timeline of Events**\n"
        for event in case['facts'].get('timeline_of_events', []):
            prompt += f"- **{event.get('date', 'N/A')}**: {event.get('event', 'N/A')}\n"

        # Add legal issues
        prompt += "\n### **Legal Issues**\n\n"
        primary_issues = case['legal_issues'].get('primary_issues', [])
        if primary_issues:
            prompt += "#### **Primary Issue(s)**\n"
            for idx, issue in enumerate(primary_issues, 1):
                prompt += f"{idx}. {issue}\n"

        secondary_issues = case['legal_issues'].get('secondary_issues', [])
        if secondary_issues:
            prompt += "\n#### **Secondary Issue(s)**\n"
            for idx, issue in enumerate(secondary_issues, 1):
                prompt += f"{idx}. {issue}\n"

        prompt += "\n---\n"
        prompt += "Please provide:\n\n"
        prompt += "1. **Decision**: Should the court rule in favor of the plaintiff or the defendant?\n"
        prompt += "2. **Legal Reasoning**: Explain the reasoning behind the decision, citing relevant legal principles and statutes.\n"

        prompts.append({
            'case_title': case.get('case_title', 'N/A'),
            'prompt': prompt
        })
    return prompts

# Function to save prompts to file
def save_prompts_to_file(prompts, output_file):
    with open(output_file, 'w') as file:
        for prompt in prompts:
            file.write(f"Case Title: {prompt['case_title']}\n\n")
            file.write(prompt['prompt'] + "\n\n")

# Input and output file paths
input_file = "contract_case_summaries.json"
output_file = "generated_prompts.txt"

# Load JSON data
json_data = load_json_file(input_file)

# Generate prompts
prompts = create_prompts_from_json(json_data)

# Save prompts to file
save_prompts_to_file(prompts, output_file)
