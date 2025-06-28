import openai
import spacy

def analyze_with_ai(data, openai_api_key=None):
    """Analyzes collected data using AI for threat prediction and NER."""
    threat_prediction = "unknown"
    entities = []

    # Combine all collected data into a single text for AI analysis
    combined_text = ""
    for module, module_data in data.items():
        if isinstance(module_data, dict):
            for key, value in module_data.items():
                combined_text += f"{key}: {value}\n"
        elif isinstance(module_data, list):
            combined_text += f"{module}: {', '.join(module_data)}\n"
        else:
            combined_text += f"{module}: {module_data}\n"

    # AI-based Threat Vector Prediction using OpenAI (if API key is provided)
    if openai_api_key and combined_text:
        try:
            openai.api_key = openai_api_key
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an OSINT analysis assistant. Analyze the provided OSINT data and predict potential threat vectors (e.g., low, medium, high) and identify key entities."},
                    {"role": "user", "content": f"Analyze the following OSINT data and provide a threat prediction (low, medium, high) and extract named entities:\n\n{combined_text}"}
                ]
            )
            ai_response = response.choices[0].message.content
            
            # Simple parsing of AI response for threat prediction and entities
            if "threat prediction: high" in ai_response.lower():
                threat_prediction = "high"
            elif "threat prediction: medium" in ai_response.lower():
                threat_prediction = "medium"
            else:
                threat_prediction = "low"
            
            # Attempt to extract entities from AI response or use SpaCy
            # For now, let\"s rely on SpaCy for NER as it\"s more structured

        except Exception as e:
            print(f"Error during OpenAI analysis: {e}")
            threat_prediction = "error_openai"

    # Named Entity Recognition (NER) using SpaCy
    try:
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(combined_text)
        for ent in doc.ents:
            entities.append({"text": ent.text, "label": ent.label_})
    except Exception as e:
        print(f"Error during SpaCy NER: {e}")
        entities.append({"error": "spacy_ner_failed"})

    return {"threat_prediction": threat_prediction, "entities": entities}


