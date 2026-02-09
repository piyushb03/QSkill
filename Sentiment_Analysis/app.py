from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment_result = None
    
    if request.method == 'POST':
        # Get text from the HTML form
        text = request.form['user_text']
        
        if text.strip():
            blob = TextBlob(text)
            
            # Extract scores
            polarity = round(blob.sentiment.polarity, 2)
            subjectivity = round(blob.sentiment.subjectivity, 2)
            
            # Determine Label
            if polarity > 0:
                sentiment = "Positive 😊"
                css_class = "is-success"
            elif polarity < 0:
                sentiment = "Negative 😠"
                css_class = "is-danger"
            else:
                sentiment = "Neutral 😐"
                css_class = "is-info"
                
            sentiment_result = {
                "text": text,
                "polarity": polarity,
                "subjectivity": subjectivity,
                "label": sentiment,
                "css_class": css_class
            }

    return render_template('index.html', result=sentiment_result)

if __name__ == '__main__':
    app.run(debug=True)