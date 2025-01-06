## Enhancing Money Laundering Detection in Real-time with Machine Learning approach


### Requirements
!pip install torch scikit-learn pandas numpy matplotlib seaborn catboost xgboost scipy

Structure of the project:
```

├── data ( contains the data used in the project)

├── notebooks ( contains the exploratory data analysis and the training of the models)

├── models ( contains the models that were dumped after training)

├── src2 ( contains the source code of the project, can be runned using docker)



To run the project, you can use the following command in src2/ directory, (please ignore the src/ directory):
```
docker-compose up
```

Producer reads the data from data source (csv) and sends to the Consumer through Kafka.
Consumer reads the data from Kafka and sends it to the pre-trained prediction model which is accessed by the REST API (Flask).
The prediction model predicts the probability of the transaction being fraudulent.
The prediction is saved in the database (InfluxDB) and the results are visualized in Streamlit.




