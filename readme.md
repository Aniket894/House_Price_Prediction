# House Price Prediction 

## Table of Contents

Introduction
Project Overview
Data Preprocessing
Feature Engineering
Modeling
Model Evaluation
Conclusion
App Structure

## Introduction
The House Price Prediction project aims to predict the final prices of houses in Ames, Iowa, based on various features. This problem is a well-known regression task where the goal is to accurately estimate house prices given the attributes of the houses.


## Project Overview

Objective: Predict house prices using features such as size, neighborhood, and other house characteristics.

Dataset: The dataset consists of 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa.

Source: Kaggle House Prices - Advanced Regression Techniques.


**Features**


Property Details

MSSubClass: The building class

MSZoning: The general zoning classification

LotFrontage: Linear feet of street connected to property

LotArea: Lot size in square feet

Street: Type of road access

Alley: Type of alley access

LotShape: General shape of property

LandContour: Flatness of the property

Utilities: Type of utilities available

LotConfig: Lot configuration

LandSlope: Slope of property

Neighborhood: Physical locations within Ames city limits

Condition1: Proximity to main road or railroad

Condition2: Proximity to main road or railroad (if a second is present)

HouseStyle: Style of dwelling

OverallQual: Overall material and finish quality

OverallCond: Overall condition rating

YearBuilt: Original construction date

YearRemodAdd: Remodel date

RoofStyle: Type of roof

RoofMatl: Roof material

Exterior1st: Exterior covering on house

MasVnrType: Masonry veneer type

MasVnrArea: Masonry veneer area in square feet

ExterQual: Exterior material quality

ExterCond: Present condition of the material on the exterior

Foundation: Type of foundation

BsmtQual: Height of the basement

BsmtCond: General condition of the basement

BsmtExposure: Walkout or garden level basement walls

BsmtFinType1: Quality of basement finished area

BsmtFinSF1: Type 1 finished square feet

BsmtFinType2: Quality of second finished area (if present)

BsmtFinSF2: Type 2 finished square feet

BsmtUnfSF: Unfinished square feet of basement area

TotalBsmtSF: Total square feet of basement area

Heating: Type of heating

HeatingQC: Heating quality and condition

CentralAir: Central air conditioning

Electrical: Electrical system

2ndFlrSF: Second floor square feet

LowQualFinSF: Low quality finished square feet (all floors)

GrLivArea: Above grade (ground) living area square feet

BsmtFullBath: Basement full bathrooms

BsmtHalfBath: Basement half bathrooms

FullBath: Full bathrooms above grade

HalfBath: Half baths above grade

BedroomAbvGr: Bedrooms above grade (does NOT include basement bedrooms)

KitchenAbvGr: Kitchens above grade

KitchenQual: Kitchen quality

Functional: Home functionality rating

Fireplaces: Number of fireplaces

FireplaceQu: Fireplace quality

GarageType: Garage location

GarageFinish: Interior finish of the garage

GarageCars: Size of garage in car capacity

GarageQual: Garage quality

GarageCond: Garage condition

PavedDrive: Paved driveway

WoodDeckSF: Wood deck area in square feet

OpenPorchSF: Open porch area in square feet

EnclosedPorch: Enclosed porch area in square feet

3SsnPorch: Three season porch area in square feet

ScreenPorch: Screen porch area in square feet

PoolArea: Pool area in square feet

PoolQC: Pool quality

Fence: Fence quality

MiscFeature: Miscellaneous feature not covered in other categories

MiscVal: Value of miscellaneous feature

MoSold: Month Sold (MM)

YrSold: Year Sold (YYYY)

SaleType: Type of sale

SaleCondition: Condition of sale


## Data Preprocessing

**Handling Missing Values**

Imputed missing values using the most frequent value for categorical features and the median for numerical features.

**Feature Engineering**

Select most important features and remove highly correlated features by a function.

**Encoding Categorical Features**

Applied label encoding to categorical features to convert them into numerical values.

**Scaling**

Used a StandardScaler to scale the numerical features to a standard normal distribution.


## Models and Hyperparameter Tuning

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor

XGBoost Regressor


Randomized search was employed to find the best parameters for each regression model. The following parameter ranges were used:

Decision Tree Regressor: max_depth (2 to 32), min_samples_split (2 to 20), min_samples_leaf (1 to 20)

Random Forest Regressor: n_estimators (10 to 1000), max_depth (2 to 32), min_samples_split (2 to 20), min_samples_leaf (1 to 20)

Gradient Boosting Regressor: n_estimators (10 to 1000), learning_rate (0.01 to 0.3), max_depth (2 to 32), min_samples_split (2 to 20), min_samples_leaf (1 to 20)

XGBoost Regressor: n_estimators (10 to 1000), learning_rate (0.01 to 0.3), max_depth (2 to 32), subsample (0.5 to 1), colsample_bytree (0.5 to 1)


## Model Evaluation

After tuning the hyperparameters, the models were evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² score. The best performing model was selected based on these metrics and used for final predictions.

After Evaluation the Results of all model by r2 score , Gradient Boosting Regressor is the best model


## Conclusion
This documentation provides an overview of the house price prediction project, detailing the features used, preprocessing steps, regression models, hyperparameters, and the process of hyperparameter tuning with randomized search. The final model's performance highlights the effectiveness of using multiple regression techniques and tuning them to achieve accurate predictions.


## App Structure

project/
│
├── app/
│   ├── __init__.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── results.html
│   ├── static/
│   │   ├── style.css
│   │   ├── house.jpeg
│
├── notebooks/
|   ├── house_price_prediction.ipynb
|   ├── dataset(train.csv)
│   ├── scaler.pkl
│   ├── model.pkl
│
├── app.py
├── requirements.txt
