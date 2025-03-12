import pandas as pd


data1=pd.read_csv("dataset/data 1/malicious_phish.csv")
data1["label"]=0
data1.loc[data1['type']!="benign","label"] = 1
del data1["type"]

data2=pd.read_csv("dataset/data 2/dataset_phishing.csv")
data2=pd.DataFrame(data2,columns=["url","status"])
data2["label"]=0
data2.loc[data2["status"]!="legitimate","label"] = 1
del data2["status"]
data3= pd.read_csv("dataset/data 3/PhiUSIIL_Phishing_URL_Dataset.csv")
data3=pd.DataFrame(data3,columns=["URL","label"])
data3=data3.rename(columns={"URL":"url" })

data13=pd.concat([data1,data3],ignore_index=True)
# print(data1)
# print("-------------------------------------")
# print(data2)
print("-------------------------------------")
print(data13)
print("-----------------")
print(data13.drop_duplicates())
# data2.to_csv("dataset/data_test_raw.csv",index=False)
# data13.to_csv("dataset/data_train_raw.csv",index=False)