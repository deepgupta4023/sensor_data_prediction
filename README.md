# sensor_data_prediction.prediction
Using Data ETL and Machine Learning on real life data from sensors of a Centrifugal Pump

To test your file on the model import file 'prediction.py
use the function 'predict(test_file,model_path)

test_file:  json test file

model_path: path to our Machine Learning Model. 
            Suppose the model is in 'C:\Documents' provide path as 'C:\\Documents\\Model'
            Provide the model name i,e 'model'  if it is in the same directory.
            


fetching_data.ipynb: Shows the method of data collection from mongodb database into tabular format for better readability and understanding

finalyzing_raw_data.ipynb: Checking data for consistencies, repetition pattern of sensors and other details

training_testing.ipynb: Studying the relationship between different sensors dropping redundant variables and dealing with null values. and trying out which ML algorithm                          works best in our case 

