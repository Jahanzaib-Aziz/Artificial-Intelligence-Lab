Driving Risk Predictor Description file
THE SUPERIOR UNIVERSITY LAHORE
SUBMITTED BY:MUHAMMAD JAHANZAIB 
Roll No: SU92-BSAIM-S25-047 
Section: BS AI 3A
Submitted to: Mr. RASIKH ALI

Step 1: Data Loading
The dataset used in this project is the Driver Behavior & Route Anomaly Dataset with Derived Features, which contains vehicle sensor readings, GPS coordinates, route information, and behavioral signals collected from real-world driving trips. The dataset comprises 120,000 records, making it a large-scale dataset suitable for training robust machine learning models.
The dataset was loaded using the Pandas library in Python, which provides efficient tools for reading and manipulating structured data. The file was read in CSV (Comma-Separated Values) format using the pd.read_csv() function. Upon successful loading, a confirmation message was printed displaying the total number of rows and columns, confirming that the dataset was imported without errors.
The dataset was loaded into a Pandas DataFrame object named data, which served as the primary data structure for all subsequent exploration and preprocessing steps. The successful load confirmed the availability of all 120,000 records along with their corresponding feature columns.
Kaggle Dataset Link:
https://www.kaggle.com/datasets/datasetengineer/driver-behavior-and-route-anomaly-dataset-dbra24

Step 2: Data Exploration
Data Exploration is the process of examining and understanding the structure, content, and statistical properties of the dataset before applying any transformations or machine learning algorithms. This step helps identify patterns, anomalies, data types, missing values, and the overall quality of the data.
2.1 Viewing Initial and Final Records
The first five and last five rows of the dataset were inspected using data.head() and data.tail() respectively. This provides a quick visual overview of the column names, sample values, and the general structure of the data. It helps confirm that the file was read correctly and that the data appears in the expected format.
2.2 Dataset Shape
The shape of the dataset was examined using data.shape, which returned the total number of rows and columns. This confirmed that the dataset contains 120,000 rows and multiple feature columns covering sensor readings, environmental conditions, route metrics, and behavioral indicators.
2.3 Column Names
All column names were listed using data.columns. The dataset includes features such as speed, acceleration, steering_angle, heading, rpm, brake_usage, lane_deviation, fuel_consumption, trip_duration, trip_distance, latitude, longitude, weather_conditions, road_type, traffic_condition, route_deviation_score, acceleration_variation, behavioral_consistency_index, route_anomaly, anomalous_event, geofencing_violation, trip_id, driver_id, vehicle_id, and timestamp.
2.4 Non-Null Count per Column
The count of non-null values per column was checked using data.count(). This provides an initial indication of how complete each column is. Any column with a count significantly less than 120,000 would indicate the presence of missing values requiring attention during preprocessing.
2.5 Unique Values per Column
The number of unique values in each column was examined using data.nunique(). This helps distinguish between continuous numerical features (which typically have many unique values) and categorical or binary features (which have a limited number of distinct values). Understanding the cardinality of columns guides decisions about encoding and feature treatment.
2.6 Unique Categories in Categorical Columns
The unique category labels present in the three key categorical columns were explicitly printed:
weather_conditions: Contains values such as Sunny, Cloudy, Foggy, and Rainy, representing the environmental weather during each trip.
road_type: Contains values such as Urban, Highway, and Rural, describing the type of road on which the trip took place.
traffic_condition: Contains values such as Light, Moderate, and Heavy, indicating the level of traffic encountered.
This step confirmed the exact category labels available in the dataset, which is important for later encoding and for building the user input interface in the application phase.
2.7 Statistical Summary
A statistical summary of all numerical columns was generated using data.describe(). This function returns key descriptive statistics for each numerical feature, including the count, mean, standard deviation, minimum value, 25th percentile (Q1), median (50th percentile), 75th percentile (Q3), and maximum value. This summary is essential for understanding the distribution and spread of each feature, identifying potential outliers, and detecting any unusual values that may need to be addressed.
2.8 Data Types and Memory Usage
The data types of all columns and memory usage information were examined using data.info(). This revealed the data type assigned to each column (such as float64, int64, or object) and confirmed the total number of non-null entries in the dataset. Identifying incorrect data types at this stage ensures that appropriate type conversion steps are taken during preprocessing.
2.9 Missing Values
The total number of missing (null) values in each column was calculated using data.isnull().sum(). This is a critical step in data exploration because missing values can significantly affect model performance if not handled properly. The output indicated which columns contained missing values and their respective counts, forming the basis for the imputation strategy applied in the preprocessing step.
Step 3: Data Pre-Processing
Data Pre-Processing is one of the most critical phases in any machine learning pipeline. Raw data collected from real-world sources is rarely clean or ready for direct use in a model. This step involves transforming the raw dataset into a structured, clean, and model-ready format by handling missing values, removing irrelevant columns, engineering new features, treating outliers, converting data types, creating the target variable, and encoding categorical columns.
3.1 Initial Inspection Before Processing
Before applying any transformations, the dataset was re-inspected using data.info() and data.isnull().sum() to confirm the data types and the exact count of missing values in each column. The shape was also re-checked using data.shape to confirm that the full 120,000 records were still intact before any modifications began.
3.2 Dropping Identifier Columns
Three columns — trip_id, driver_id, and vehicle_id — were removed from the dataset using data.drop() with inplace=True. These columns serve only as unique identifiers for records and do not carry any meaningful predictive information. Including them in the model would not improve accuracy and could introduce noise. After dropping these columns, the remaining number of columns was printed to confirm the operation.
3.3 Timestamp Feature Engineering
The timestamp column, which was stored as a string object, was converted into a proper datetime format using pd.to_datetime(). From this parsed timestamp, four new time-based features were derived:
hour: The hour of the day (0–23), which captures time-of-day driving patterns.
day_of_week: The day of the week (0 = Monday, 6 = Sunday), which captures weekly behavioral patterns.
is_weekend: A binary flag (1 = weekend, 0 = weekday), engineered from day_of_week, to distinguish weekend driving behavior from weekday driving.
is_night: A binary flag (1 = night, 0 = day), set to 1 when the hour falls between 10 PM and 5 AM, to identify nighttime driving which typically carries higher risk.
After extracting these features, the original timestamp column was dropped as it was no longer needed in its raw form.
3.4 Handling Missing Values — Mean Imputation
Missing values in numerical continuous columns were filled using the mean imputation strategy. A custom function fillnaMean() was defined and applied to the following columns: speed, acceleration, heading, trip_duration, trip_distance, fuel_consumption, rpm, lane_deviation, route_deviation_score, acceleration_variation, behavioral_consistency_index, latitude, and longitude. Mean imputation is suitable for continuous numerical features as it preserves the overall distribution of the data without introducing extreme values.
3.5 Handling Missing Values — Mode Imputation
Missing values in categorical and integer columns were filled using the mode imputation strategy. A custom function fillnaMode() was defined and applied to columns including steering_angle, brake_usage, stop_events, geofencing_violation, anomalous_event, route_anomaly, weather_conditions, road_type, traffic_condition, hour, day_of_week, is_weekend, and is_night. Mode imputation replaces missing values with the most frequently occurring value, which is the most appropriate strategy for categorical and discrete integer fields.
3.6 Outlier Treatment using IQR Capping
Outliers in numerical columns were treated using the Interquartile Range (IQR) method. A custom function cap_outliers_iqr() was defined to calculate the lower and upper bounds for each column using the formula:
Lower Bound = Q1 − 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
Any values falling outside this range were capped (clipped) to the boundary values rather than removed. This approach retains all 120,000 records while reducing the effect of extreme outliers on model training. The function was applied to the following columns: speed, acceleration, rpm, fuel_consumption, trip_duration, trip_distance, lane_deviation, route_deviation_score, acceleration_variation, behavioral_consistency_index, and brake_usage. For each column, the number of outliers detected and the capping bounds were printed to provide transparency.
3.7 Data Type Conversion to Integer
Several columns that should logically be integer values were explicitly converted to int64 data type using a custom function changetoInt64(). These columns included steering_angle, brake_usage, stop_events, geofencing_violation, anomalous_event, route_anomaly, hour, day_of_week, is_weekend, and is_night. This conversion ensures type consistency and prevents any unintended floating-point operations during model training.
3.8 Creating the Target Variable: risk_level
Since the dataset did not contain a pre-defined target column, the target variable risk_level was engineered using domain-knowledge-based rules applied to existing features. The classification logic was as follows:
Risk Level	Condition
Low	Default — normal, safe driving behavior
Medium	Speed, lane deviation, route deviation score, acceleration variation, or brake usage exceeds the 75th percentile
High	Presence of route anomaly, anomalous event, or geofencing violation; OR combination of very high speed (above 90th percentile) with very low behavioral consistency (below 10th percentile)
The assignment was done in two passes — Medium conditions were applied first, then High conditions overrode where applicable. This rule-based target engineering ensured meaningful, interpretable class labels for the supervised learning task.
3.9 Dropping Leakage Columns
After creating the risk_level target variable, the three columns used in the High-risk rule — route_anomaly, anomalous_event, and geofencing_violation — were dropped from the dataset. Retaining these columns would cause data leakage, as the model would have direct access to the exact conditions used to define the target variable, resulting in artificially inflated accuracy that would not generalize to real-world data.
3.10 Label Encoding of Categorical Columns
Categorical string columns were converted into numerical format using Label Encoding. A custom function encodeCols() was defined, which fitted a LabelEncoder on each column and transformed the string values into integer codes. The following columns were encoded: weather_conditions, road_type, traffic_condition, and the target column risk_level. All fitted encoder objects were stored in a dictionary named encoders and saved to disk as encoders.pkl using joblib. This saved file is later used in the application phase to decode the model's predictions back to human-readable labels.
3.11 Saving the Cleaned Dataset
After completing all preprocessing steps, the final cleaned dataset was saved to a new CSV file named cleaned_data.csv using data.to_csv(). This ensures that the preprocessing work is preserved and the cleaned data can be directly loaded for model training without repeating any preprocessing steps.

Step 4: Train-Test Splitting
Train-Test Splitting is the process of dividing the cleaned dataset into two separate subsets — a training set used to train the machine learning model, and a testing set used to evaluate its performance on unseen data. This split is essential to assess how well the model generalizes beyond the data it was trained on.
The cleaned dataset was first reloaded from cleaned_data.csv to ensure a fresh, consistent starting point. The feature matrix X was created by dropping the target column risk_level from the dataset, while the target vector y was set to the risk_level column alone.
The train_test_split() function from Scikit-learn was used to split the data with the following parameters:
test_size = 0.2: 20% of the data (24,000 records) was reserved for testing, while the remaining 80% (96,000 records) was used for training.
shuffle = False: The data was not shuffled before splitting, preserving the original sequential order of the records. This is particularly appropriate for time-series or sequentially collected driving data where temporal order may carry meaningful information.
The resulting split produced the following subsets:
Subset	Rows	Columns
train_X	96,000	23 features
train_y	96,000	1 target
test_X	24,000	23 features
test_y	24,000	1 target
The shapes of all four subsets were printed to confirm the split was performed correctly.

Step 5: Model Application
For this project, the Random Forest Classifier was selected as the machine learning algorithm to predict the driving risk level. Random Forest is an ensemble learning method that builds multiple decision trees during training and outputs the class that is the mode of the individual trees' predictions. It is well-suited for this task due to its ability to handle large datasets, manage both numerical and encoded categorical features, resist overfitting through ensemble averaging, and provide robust performance without extensive hyperparameter tuning.
The model was configured and trained with the following parameters:
python
model_rf = RandomForestClassifier(    n_estimators = 100,    random_state = 42,    n_jobs       = -1)model_rf.fit(train_X, train_y)
n_estimators = 100: The forest consists of 100 decision trees, providing a strong ensemble with sufficient diversity.
random_state = 42: A fixed random seed was set to ensure reproducibility of results across different runs.
n_jobs = -1: All available CPU cores were utilized to speed up the training process, which is particularly beneficial given the large dataset size of 96,000 training records.
After training was complete, the model was saved in two formats for portability and future use. It was saved as model_rf.pkl using Python's built-in pickle library and as model_rf.joblib using the joblib library. The model was then reloaded from the .pkl file to verify that saving and loading functioned correctly before proceeding to evaluation.

Step 6: Model Accuracy
Model evaluation was performed by generating predictions on the test set and comparing them against the actual known labels. The trained Random Forest model was used to predict the risk_level for all 24,000 test records using model_rf.predict(test_X).
The Accuracy Score metric from Scikit-learn was used as the primary evaluation measure. Accuracy is defined as the proportion of correctly predicted instances out of the total number of instances:
Accuracy = (Number of Correct Predictions) / (Total Predictions)
Both training accuracy and testing accuracy were calculated and reported:
python
train_pred = model_rf.predict(train_X)train_acc  = accuracy_score(train_y, train_pred)
Train Accuracy reflects how well the model has learned the patterns in the training data.
Test Accuracy reflects how well the model generalizes to new, unseen data.
Reporting both metrics side by side is important for diagnosing potential overfitting. If training accuracy is significantly higher than test accuracy, the model may have memorized the training data rather than learning generalizable patterns. The results from this model demonstrated strong performance on both sets, confirming that the Random Forest classifier effectively learned the driving risk patterns without significant overfitting.

Step 7: Application Phase
The Application Phase represents the deployment stage of the machine learning pipeline, where the trained model is made usable for real-world predictions. In this phase, the saved model and encoders are loaded, user inputs are collected interactively, and a driving risk prediction is returned along with actionable advice.
7.1 Loading the Saved Model and Encoders
The trained Random Forest model was loaded from model_rf.pkl using pickle.load(), and the saved label encoders were loaded from encoders.pkl using joblib.load(). This ensures that the exact same model and encoding mappings used during training are applied during prediction, maintaining consistency.
7.2 User Input Collection
The application collects 23 feature values from the user through interactive input() prompts. These inputs cover all major aspects of a driving trip, including:
GPS coordinates: Latitude and Longitude
Vehicle sensor readings: Speed, Acceleration, Steering Angle, Heading, RPM, Fuel Consumption
Trip metrics: Trip Duration, Trip Distance, Brake Usage, Stop Events, Lane Deviation
Environmental conditions: Weather Conditions, Road Type, Traffic Condition
Derived risk indicators: Route Deviation Score, Acceleration Variation, Behavioral Consistency Index
Time features: Hour, Day of Week, Is Weekend, Is Night
7.3 Encoding Categorical Inputs
A helper function encode_cols() was defined to encode the categorical string inputs (weather_conditions, road_type, traffic_condition) using the same LabelEncoder objects that were fitted during preprocessing. If a user enters a value that was not seen during training, the function returns -1 to handle unknown categories gracefully rather than crashing.
7.4 Prediction and Output
The collected and encoded user inputs were assembled into a NumPy array and passed to the loaded model's predict() method. The predicted numerical label was then decoded back to its human-readable string form (Low, Medium, or High) using the saved risk_level encoder's inverse_transform() method.
Finally, a context-specific advice message was displayed alongside the predicted risk level:
Predicted Risk Level	Advice
Low	Safe trip. Keep it up!
Medium	Moderate risk. Drive carefully.
High	HIGH RISK! Take immediate precautions.
This end-to-end application demonstrates a complete and functional deployment of the trained machine learning model, from raw user input collection to actionable risk prediction output.
