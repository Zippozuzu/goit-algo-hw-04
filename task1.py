import re
import sys

def total_salary(path):
    try:
        with open(path, 'r') as fh:
         content = fh.read()
    except FileNotFoundError:
       print(f"There is no {path} file")
       sys.exit(1)
       

    salary_list = re.findall(r'-?\d+\.?\d*', content)  #digits from the txt file
    modify_salary_list = [eval(salary) for salary in salary_list]  #str to int

    total = sum(modify_salary_list)
    average = int(total/len(modify_salary_list))

    return total, average