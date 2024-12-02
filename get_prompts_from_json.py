import json

# Load JSON data from a file
def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Create prompts from JSON data
def create_prompts(json_data):
    prompts = []
    for case in json_data:
        prompt = f"""
You are a legal expert specializing in U.S. contract law. Generate a synthetic case summary.

---
### Case Title:
{case.get('case_title', 'N/A')}

### Jurisdiction:
{case.get('jurisdiction', 'N/A')}

### Facts:
#### Parties
- Plaintiff: {case.get('facts', {}).get('parties', {}).get('plaintiff', 'N/A')}
- Defendant: {case.get('facts', {}).get('parties', {}).get('defendant', 'N/A')}

#### Contract Details
- Type: {case.get('facts', {}).get('contract_details', {}).get('type', 'N/A')}
- Key Terms:
  - Payment: {case.get('facts', {}).get('contract_details', {}).get('key_terms', {}).get('payment', 'N/A')}
  - Delivery: {case.get('facts', {}).get('contract_details', {}).get('key_terms', {}).get('delivery', 'N/A')}

### Legal Issues:
- Primary Issue: {case.get('legal_issues', {}).get('primary', 'N/A')}
- Secondary Issues: {case.get('legal_issues', {}).get('secondary', 'N/A')}

### Arguments:
#### Plaintiff:
{case.get('arguments', {}).get('plaintiff', 'N/A')}

#### Defendant:
{case.get('arguments', {}).get('defendant', 'N/A')}

### Outcome:
- Decision: {case.get('outcome', {}).get('decision', 'N/A')}
- Legal Reasoning: {case.get('outcome', {}).get('reasoning', 'N/A')}

---
"""
        prompts.append(prompt)
    return prompts

# Save prompts to a file
def save_prompts_to_file(prompts, output_file):
    with open(output_file, 'w') as file:
        for prompt in prompts:
            file.write(prompt + "\n\n")

# Main
if __name__ == "__main__":
    input_file = "contract_case_summaries.json"  # Replace with your file path
    output_file = "generated_prompts.txt"
    
    # Load data from JSON
    json_data = load_json_file(input_file)
    
    # Generate prompts
    prompts = create_prompts(json_data)
    
    # Save prompts to a file
    save_prompts_to_file(prompts, output_file)
    print(f"Prompts saved to {output_file}")
