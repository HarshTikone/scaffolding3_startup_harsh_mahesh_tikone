from flask import Flask, request, jsonify, render_template
from starter_preprocess import TextPreprocessor

app = Flask(__name__)
preprocessor = TextPreprocessor()


@app.route('/')
def home():
    """Render a simple HTML form for URL input"""
    return render_template('index.html')


@app.route('/health')
def health_check():
    """Simple health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "Text preprocessing service is running"
    })


@app.route('/api/clean', methods=['POST'])
def clean_text():
    """
    API endpoint that accepts a URL and returns cleaned text

    Expected JSON input:
        {"url": "https://www.gutenberg.org/files/1342/1342-0.txt"}

    Returns JSON:
        {
            "success": true/false,
            "cleaned_text": "...",
            "statistics": {...},
            "summary": "...",
            "error": "..." (if applicable)
        }
    """
    try:
        data = request.get_json()
        url = data.get("url")

        if not url.endswith('.txt'):
            return jsonify({
                "success": False,
                "error": "URL must point to a .txt file"
            }), 400

        raw_text = preprocessor.fetch_from_url(url)

        cleaned_text = preprocessor.clean_gutenberg_text(raw_text)

        normalized_text = preprocessor.normalize_text(cleaned_text)

        statistics = preprocessor.get_text_statistics(normalized_text)

        summary = preprocessor.create_summary(normalized_text, num_sentences=3)

        return jsonify({
            "success": True,
            "cleaned_text": cleaned_text,
            "statistics": statistics,
            "summary": summary
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500


@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """
    API endpoint that accepts raw text and returns statistics only

    Expected JSON input:
        {"text": "Your raw text here..."}

    Returns JSON:
        {
            "success": true/false,
            "statistics": {...},
            "error": "..." (if applicable)
        }
    """
    try:
        data = request.get_json()
        raw_text = data.get("text")

        if not raw_text:
            return jsonify({
                "success": False,
                "error": "No text provided"
            }), 400

        normalized_text = preprocessor.normalize_text(raw_text)

        statistics = preprocessor.get_text_statistics(normalized_text)

        return jsonify({
            "success": True,
            "statistics": statistics
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Server error: {str(e)}"
        }), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500


if __name__ == '__main__':
    print("🚀 Starting Text Preprocessing Web Service...")
    print("📖 Available endpoints:")
    print("   GET  /           - Web interface")
    print("   GET  /health     - Health check")
    print("   POST /api/clean  - Clean text from URL")
    print("   POST /api/analyze - Analyze raw text")
    print()
    print("🌐 Open your browser to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")

    app.run(debug=True, port=5000, host='0.0.0.0')
