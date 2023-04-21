
# Online Python - IDE, Editor, Compiler, Interpreter

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import pandas as pd

# list of tasks to execute
def extract_data():
    print("downloading a data from database...")

def preprocess_data():
    print("executing a preprocessing of data (Przeprowadzanie wstępnego przetwarzania danych)..")

def process_data():
    print("executing the advanced processing of data (Przeprowadzanie zaawansowanego przetwarzania danych)...")

def analyze_data():
    print("executing data analysis (Przeprowadzanie analizy danych)...")

def generate_report():
    print("report generate (Generowanie raportu)...")

#default arguments with parameters for DAG
default_arguments = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 04, 21,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'dataflow_dag_dawid',
    default_args=default_arguments,
    description='Instance of DAG with 5 tasks (Przykładowy DAG złożony z pięciu zadań)',
    schedule_interval=timedelta(days=1),
)

t1 = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

t2 = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag,
)

t3 = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag,
)

t4 = PythonOperator(
    task_id='analyze_data',
    python_callable=analyze_data,
    dag=dag,
)

t5 = PythonOperator(
    task_id='generate_report',
    python_callable=generate_report,
    dag=dag,
)

t1 >> t2 >> t3 >> t4 >> t5