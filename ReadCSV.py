#note keep RICStudentCSV.csv file and program in the same directory
import pandas as pd
marks = pd.read_csv('Demo.csv')
print(marks)
print("Summary of data")
print(marks.describe())
