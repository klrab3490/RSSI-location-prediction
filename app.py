from flask import Flask, render_template, send_from_directory, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__, static_url_path='/static')
df = pd.read_csv('sharing333.csv') # Load the dataset

# Split the dataset into features (X) and target variable (y)
X = df[['rssi(signal)']]
y = df['Location']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # Split the dataset into training and testing sets
knn_classifier = KNeighborsClassifier(n_neighbors=5) # Initialize the kNN classifier
knn_classifier.fit(X_train, y_train) # Train the classifier

# Define the route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for handling location prediction
@app.route('/predict_location', methods=['POST'])
def predict_location():
    if request.method == 'POST':
        rssi_values = float(request.form['rssi_values']) # Get RSSI values from the request
        predicted_location = knn_classifier.predict([[-rssi_values]]) # Use the machine learning model to predict the location
        return render_template('index.html', predicted_location=predicted_location[0]) # Pass the predicted location to the template

# Add a route to serve the map image
@app.route('/static/map.png')
def serve_map_image():
    return send_from_directory('static', 'map.png')

if __name__ == '__main__':
    app.run(debug=True)