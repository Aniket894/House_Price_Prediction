from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the scaler and model
with open('notebooks/scaler (8).pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('notebooks/GradientBoostingRegressor (3).pkl', 'rb') as f:
    model = pickle.load(f)

# Render the main index page
@app.route('/')
def index():
    return render_template('index.html')

# Handle prediction request
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Extract data from the form
        features = [
            float(request.form['MSSubClass']),
            int(request.form['MSZoning']),
            float(request.form['LotFrontage']),
            float(request.form['LotArea']),
            int(request.form['Street']),
            int(request.form['Alley']),
            int(request.form['LotShape']),
            int(request.form['LandContour']),
            int(request.form['Utilities']),
            int(request.form['LotConfig']),
            int(request.form['LandSlope']),
            int(request.form['Neighborhood']),
            int(request.form['Condition1']),
            int(request.form['Condition2']),
            int(request.form['HouseStyle']),
            float(request.form['OverallQual']),
            float(request.form['OverallCond']),
            float(request.form['YearBuilt']),
            float(request.form['YearRemodAdd']),
            int(request.form['RoofStyle']),
            int(request.form['RoofMatl']),
            int(request.form['Exterior1st']),
            int(request.form['MasVnrType']),
            float(request.form['MasVnrArea']),
            int(request.form['ExterQual']),
            int(request.form['ExterCond']),
            int(request.form['Foundation']),
            int(request.form['BsmtQual']),
            int(request.form['BsmtCond']),
            int(request.form['BsmtExposure']),
            int(request.form['BsmtFinType1']),
            float(request.form['BsmtFinSF1']),
            int(request.form['BsmtFinType2']),
            float(request.form['BsmtUnfSF']),
            float(request.form['TotalBsmtSF']),
            int(request.form['Heating']),
            int(request.form['HeatingQC']),
            int(request.form['CentralAir']),
            int(request.form['Electrical']),
            float(request.form['2ndFlrSF']),
            float(request.form['LowQualFinSF']),
            float(request.form['GrLivArea']),
            float(request.form['BsmtFullBath']),
            float(request.form['BsmtHalfBath']),
            float(request.form['FullBath']),
            float(request.form['HalfBath']),
            float(request.form['BedroomAbvGr']),
            float(request.form['KitchenAbvGr']),
            int(request.form['KitchenQual']),
            int(request.form['Functional']),
            float(request.form['Fireplaces']),
            int(request.form['FireplaceQu']),
            int(request.form['GarageType']),
            int(request.form['GarageFinish']),
            float(request.form['GarageCars']),
            int(request.form['GarageQual']),
            int(request.form['GarageCond']),
            int(request.form['PavedDrive']),
            float(request.form['WoodDeckSF']),
            float(request.form['OpenPorchSF']),
            float(request.form['EnclosedPorch']),
            float(request.form['3SsnPorch']),
            float(request.form['ScreenPorch']),
            float(request.form['PoolArea']),
            int(request.form['Fence']),
            int(request.form['MiscFeature']),
            float(request.form['MiscVal']),
            float(request.form['MoSold']),
            float(request.form['YrSold']),
            int(request.form['SaleType']),
            int(request.form['SaleCondition'])
        ]

        # Convert features to numpy array
        features_array = np.array([features])

        # Scale the features
        scaled_features = scaler.transform(features_array)

        # Predict using the model
        prediction = model.predict(scaled_features)

        # Display the prediction
        predicted_price = prediction[0]

        return render_template('results.html', predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
