from flask import Flask, request, jsonify, render_template, redirect
import random

app = Flask(__name__)

# --- Mock Engines (From your architecture) ---
def integrity_firewall(query):
    restricted_keywords = ["write my essay", "what is the answer to", "give me the code"]
    if any(keyword in query.lower() for keyword in restricted_keywords):
        return False, "Integrity Alert: Direct answers cannot be provided. Let's work through the concept together."
    return True, "Safe Input"

def knowledge_vault_rag(query):
    mock_academic_corpus = {
        "mitosis": "Mitosis is a part of the cell cycle in which replicated chromosomes are separated into two new nuclei.",
        "machine learning": "Machine learning involves using data and algorithms to imitate the way humans learn."
    }
    for key, context in mock_academic_corpus.items():
        if key in query.lower():
            return context
    return "No approved faculty content found for this query."

# --- Routes ---
@app.route('/')
def student_interface():
    # Renders the HTML file from the templates folder
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get('query', '')
    
    is_safe, fw_message = integrity_firewall(query)
    if not is_safe:
        return jsonify({"status": "blocked", "message": fw_message})

    context = knowledge_vault_rag(query)
    
    return jsonify({
        "status": "success", 
        "feedback": f"Based on course materials: '{context}'. How does this apply to your assignment?",
        "mastery": {"score": round(random.uniform(0.4, 0.9) * 100, 1)}
    })

@app.route('/faculty')
def faculty_dashboard():
    # Redirects straight to your Streamlit app
    return redirect("https://educhamp.streamlit.app/")

if __name__ == '__main__':
    app.run(debug=True, port=5000)