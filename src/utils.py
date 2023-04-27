import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

import numpy as np
def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in models:
            model=models[i]
            # Train the model
            model.fit(X_train,y_train)
            # Predict Testing Data
            y_pred=model.predict(X_test)
             # Get R2 scores for train and test data
            test_model_score = r2_score(y_test,y_pred)
            #report[list(models.keys())[i]] = test_model_score
            report[i]=test_model_score
        return report
    
    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)
