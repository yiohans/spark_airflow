# Apache Spark and Apache Airflow

This project has a Docker Compose Structure to run Apache Airflow to orchestrate Python scripts and using Apache Spark to Data processing.

To run this project, you have to create a `.env` file with this information:

```
#######################
###     POSTGRES    ###
#######################

POSTGRES_USER="Your Username"
POSTGRES_PASSWORD="Your Password"
POSTGRES_DB="Your DB Name"

#######################
###     AIRFLOW     ###
#######################

AIRFLOW_UID=1000
AIRFLOW__SCHEDULER__ENABLE_HEALTH_CHECK=True
AIRFLOW__CORE__LOAD_EXAMPLES=False
AIRFLOW__CORE__EXECUTOR=LocalExecutor
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
AIRFLOW__WEBSERVER_BASE_URL=http://localhost:8080
AIRFLOW__WEBSERVER__SECRET_KEY="Your Secret Key"

#######################
```

After that execute `./01_build_n_run.sh`. That will permissions and ownership of log directory and build the containers.