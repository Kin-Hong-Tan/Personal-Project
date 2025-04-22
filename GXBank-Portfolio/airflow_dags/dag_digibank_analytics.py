from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_arguments = {
'owner': 'Kin Hong',
'email': 'khtan47@outlook.com',
'start_date': datetime(2025, 4, 20)
}

with DAG('etl_workflow', default_args=default_arguments) as etl_dag:

with DAG(dag_id='digibank_dashboard_etl',
         start_date=days_ago(1),
         schedule_interval='@daily',
         catchup=False) as dag:

    dbt_run = BashOperator(
        task_id='run_dbt_models',
        bash_command='cd ~/digibank-analytics-portfolio/dbt_project && dbt run'
    )

    notify = BashOperator(
        task_id='notify_completion',
        bash_command='echo "DBT Models Refreshed!"'
    )

    dbt_run >> notify
