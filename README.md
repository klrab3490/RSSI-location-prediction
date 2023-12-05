# RSSI-Based Location Prediction with Flask

This Flask application serves as a simple location prediction system based on Received Signal Strength Indicator (RSSI) values. It utilizes the k-nearest neighbors (kNN) algorithm to predict the location based on the RSSI values provided.

## How To Run This Code
1. Clone this repository
```bash
git clone  
```
2. Open the Folder
```bash
cd
```
3. Install necessary modules
```bash
pip install Flask pandas scikit-learn
```
4. Run the application
```bash
python app.py
```

## Components

### 1. Flask Setup

The Flask application is initialized with the Flask class. The `static_url_path='/static'` parameter is set to define the URL path for static files (e.g., CSS, images).

### 2. Dataset Loading

The application loads a CSV dataset (`sharing333.csv`) containing RSSI values and corresponding locations using the Pandas library.

### 3. Data Preprocessing

The dataset is split into features (`X`: RSSI values) and the target variable (`y`: Location). The dataset is further split into training and testing sets using `train_test_split` from scikit-learn.

### 4. Machine Learning Model (kNN)

A k-nearest neighbors classifier is initialized with 5 neighbors (`KNeighborsClassifier`). The model is trained on the training data using `fit`.

### 5. Flask Routes

- The main route (`'/'`) renders the `index.html` template.
- The `/predict_location` route is configured to handle POST requests for predicting the location based on provided RSSI values.
- The `/static/map.png` route serves a static map image.

### 6. Main Page (`index.html`)

The main page, rendered at the `'/'` route, likely contains a form for users to input RSSI values. On form submission, the entered RSSI values are sent to the `/predict_location` route via a POST request.

### 7. Location Prediction (`/predict_location`)

RSSI values are obtained from the form submission. The kNN classifier predicts the location based on the provided RSSI values. The predicted location is passed back to the `index.html` template for display.

### 8. Running the Application

The application runs when the script is executed (`if __name__ == '__main__': app.run(debug=True)`). It runs in debug mode for development (`debug=True`).

## Usage Instructions

1. Ensure Flask is installed (`pip install flask`).
2. Have the dataset file (`sharing333.csv`) in the same directory as the script.
3. Run the script (`python script_name.py`).
4. Access the application at `http://127.0.0.1:5000/` in a web browser.

Users can input RSSI values, and the application will predict and display the corresponding location based on the trained kNN model.

---
## Locations 

| RSSI (Signal) | Location   |
|---------------|------------|
| 68            | location1  |
| 67            | location1  |
| 69            | location1  |
| 66            | location1  |
| 67            | location2  |
| 69            | location2  |
| 64            | location2  |
| 63            | location2  |
| 58            | location3  |
| 59            | location3  |
| 60            | location3  |
| 57            | location3  |
| 48            | location4  |
| 47            | location4  |
| 44            | location4  |
| 51            | location4  |
| 56            | location5  |
| 57            | location5  |
| 51            | location5  |
| 54            | location5  |
| 54            | location6  |
| 55            | location6  |
| 53            | location6  |
| 55            | location6  |
| 70            | location7  |
| 76            | location7  |
| 77            | location7  |
| 72            | location7  |
| 64            | location8  |
| 68            | location8  |
| 69            | location8  |
| 70            | location8  |
| 77            | location9  |
| 75            | location9  |
| 76            | location9  |
| 74            | location9  |
| 75            | location10 |
| 76            | location10 |
| 70            | location10 |
| 74            | location10 |
| 75            | location11 |
| 77            | location11 |
| 76            | location11 |
| 75            | location11 |
| 86            | location12 |
| 87            | location12 |
| 82            | location12 |
| 81            | location12 |
| 81            | location13 |
| 83            | location13 |
| 89            | location13 |
| 87            | location13 |

