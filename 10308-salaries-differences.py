https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=2
# Import your libraries
import pandas as pd

# Start writing code
df = db_employee.groupby('department_id')['salary'].max().reset_index()
df[df['department_id'] == 4]['salary'].values - df[df['department_id'] ==1]['salary'].values
