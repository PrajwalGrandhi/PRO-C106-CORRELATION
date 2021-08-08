import csv
import numpy as np

def getDatasource(data_path):
    marksprecentage=[]
    dayspresent=[]

    with open(data_path) as f:
        Reader=csv.DictReader(f)
        for row in Reader:
            marksprecentage.append(float(row["Marks In Percentage"]))
            dayspresent.append(float(row["Days Present"]))

    return {"x":marksprecentage,"y":dayspresent}

def findCorelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("The corelation between the marks in percentage and the number of days present: ",correlation[0,1])


def setup():
    data_path="Student Marks vs Days Present.csv"
    ds=getDatasource(data_path)
    findCorelation(ds)

setup()