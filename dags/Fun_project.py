from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'ye',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['yedavid144@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

def square(x):
    return x**2

dag = DAG(
    'python_square_operator',
#    description = 'Squaring a number using Airflow',
#    schedule_interval = "0 12 * * *",
#    Start_date = datetime(2017,3,20), catchup = False)
    default_args = default_args,
    Description = 'Squaring a number using Airflow',
    schedule_interval = timedelta(days=1),
)


t1 = PythonOperator(
    task_id = 'square',
    python_callable = square,
    op_kwargs = {"x":13},
    dag = dag
)

t1
