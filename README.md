<h1>COVID-19 Streaming Dashboard</h2>

<h2>Repository Structure</h2>

```
├── consumer
│   ├── requirements.txt
│   └── script.py
├── dashboard
│   ├── dash.R
│   ├── Dockerfile
│   └── source.R
├── docker-compose.yml
├── producer
│   ├── requirements.txt
│   └── script.py
└── README.md
```

The repository contains three folders (one for the producer, consumer and dashboard)
as well as a ```docker-compose.yml``` file for running the Kakfa, Zookeeper and dashboard.
The ```producer``` and the ```consumer``` folders both contain python scripts designed
to be ran locally, as well as requirements files listing the dependencies for them.

<h2>How to run the code</h2>

To run the code, ensure that ports **2181** and **9092** are free for use by the Kafka
and Zookeeper instances that will stream the data to the consumer and be used in the
dashboard.

After you have checked that the ports are free, edit the ```.env``` files in the
**consumer** and **producer** folders to contain credentials specific to your
AWS account so that the file can be produced and accessed by the dashboard.

Once these environment variables have been set, run ```docker-compose up --build```
to create the Kafka, Zookeeper and dashboard instances - then run the ```producer/script.py```
and the ```consumer/script.py``` Python scripts in that order. 

Once the producer and consumer scripts are running, visit ```0.0.0.0:3838``` in your
browser and the dashboard will be running, with data being retrieved via a .csv
file in S3 being populated by the Kafka topic.  
