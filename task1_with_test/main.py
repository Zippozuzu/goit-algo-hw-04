from task1 import total_salary
import os

dirname = "tests/"

def main():
    for file in os.listdir(dirname):
        path = dirname + file
        print(path)
        total, average = total_salary(path)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()
