import csv
import numpy as np

def getDatasource(data_path):
    coffee=[]
    sleep=[]

    with open(data_path) as f:
        Reader=csv.DictReader(f)
        for row in Reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x":coffee,"y":sleep}

def findCorelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("The corelation between the coffee in ml and sleep in hours: ",correlation[0,1])


def setup():
    data_path="cups of coffee vs hours of sleep.csv"
    ds=getDatasource(data_path)
    findCorelation(ds)

setup()