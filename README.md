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
###    SCHEDULER    ###
#######################

SCHEDULER_USER="Your Username"
SCHEDULER_FNAME="Your First Name"
SCHEDULER_LNAME="Your Last Name"
SCHEDULER_ROLE=Admin
SCHEDULER_EMAIL="Your Email"
SCHEDULER_PASSWORD="Your Password"
```

After that execute `./01_build_n_run.sh`. That will permissions and ownership of log directory and build the containers.