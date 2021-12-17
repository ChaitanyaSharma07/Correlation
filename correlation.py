import csv
import plotly.express as px
import numpy as np
import pandas 
import plotly.express as px

def plot_figure(data_path):
    with open(data_path, 'r+') as file:
        data = pandas.read_csv("marks.csv")

        fig = px.scatter(data, x="Days Present", y="Marks In Percentage", color="Roll No")
        fig.show()



def get_data_source(data_path):
    marks_in_percentage = []
    days_present = []

    with open(data_path, 'r+') as file:
        file_dict = csv.DictReader(file)

        for i in file_dict :
            marks_in_percentage.append(float(i["Marks In Percentage"]))
            days_present.append(float(i["Days Present"]))

        return {"x": marks_in_percentage, "y": days_present}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("correlation between days present and marks in percentage: " + str(correlation[0, 1]))

def setup():
    data_path = "marks.csv"
    data_source = get_data_source(data_path)
    find_correlation(data_source)

setup()

