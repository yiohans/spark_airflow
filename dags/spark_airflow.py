from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = "Spark_Airflow",
    default_args = {
        "owner": "Jefferson Leocadio",
        "start_date": days_ago(1)
    },
    schedule_interval = "@daily"
)

start = PythonOperator(
    task_id = "start",
    python_callable = lambda: print("Job Started"),
    dag = dag
)


job = SparkSubmitOperator(
    task_id = "job",
    conn_id = "spark-conn",
    application = "jobs/wordcountjob.py",
    dag = dag
)


end = PythonOperator(
    task_id = "end",
    python_callable = lambda: print("Job completed successfully"),
    dag = dag
)

start >> job >> end