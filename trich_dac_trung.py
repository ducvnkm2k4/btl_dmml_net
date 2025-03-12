import pandas as pd
import re 

data=pd.read_csv('dataset/raw/data_test_raw.csv')

special_chars = set("`%^&*;@!?#=+$")
common_keywords = [
    "password", "login", "secure", "account", "index", 
    "token", "signin", "update", "verify", "auth", 
    "authentication", "security", "recover", "reset"
]
sensitive_keywords = [
    "confirm", "submit", "payment", "invoice", "billing", 
    "transaction", "transfer", "refund", "wire"
]

short_url_services = ["//bit.ly/", "//goo.gl/", "//tinyurl.com/", "//is.gd/", "//t.co/", "//ow.ly/","//j2team.dev","//cutt.ly/","//short.io/","//t2m.io/"]
#f1: độ dài url
data["length"]=data['url'].str.len()

#f2: mật độ các ký tự đặc biệt trong url = count(ký tự đặc biệt)/length(u)
def compute_f2(url, length):
    count_special = sum(1 for char in url if char in special_chars)
    return count_special / length

data["tachar"]=data.apply(lambda row: compute_f2(row["url"],row["length"]),axis=1)

#f3: url có chứa các từ khóa liên quan đến bảo mật tài khoản

def compute_f3(url):
    return int(any(kw in url.lower() for kw in common_keywords))

data['hasKeyWords']= data.apply(lambda row: compute_f3(row["url"]),axis=1)

#f4: có ký đặc biệt hay không
def compute_f4(url):
    return int(any(char in url for char in special_chars))
data["hasSpecialChar"]=data.apply(lambda row: compute_f4(row["url"]),axis=1)
#f5: có từ khóa liên quan đến giao dịch
def compute_f5(url):
    return int(any(kw in url.lower() for kw in sensitive_keywords))
data["hasspecKW"]=data.apply(lambda row: compute_f5(row["url"]),axis=1)
#f6: có phải là url rút gọn hay không
def compute_f6(url):
    return int(any(char in url for char in short_url_services))

data["tinyUrl"]=data.apply(lambda row: compute_f6(row["url"]),axis=1)
#f7: mật độ ký tự hexa trong url
def compute_f7(url, length):
    hex_pattern = re.compile(r'[a-fA-F0-9]{10,}')  
    matches = re.findall(hex_pattern, url)
    cnt = sum(len(match) for match in matches)
    return cnt / length

data["tahex"]=data.apply(lambda row: compute_f7(row["url"],row["length"]),axis=1)

#f8: mật độ chữ số trong url
def compute_f8(url,length):
    numbers=re.findall(r'\d',url)
    return (len(numbers))/length
data["tadigit"]=data.apply(lambda row: compute_f8(row["url"],row["length"]),axis=1)

#f9: số lượng dấu '.' (dấu chấm)
def compute_f9(url):
    return url.count('.')
data["numDots"]=data.apply(lambda row: compute_f9(row["url"]),axis=1)

#f10: mật độ ký tự '/'
def compute_f10(url,length):
    return (url.count('/'))/length
data["taslash"]=data.apply(lambda row: compute_f10(row["url"],row["length"]),axis=1)

print(data)
#data.to_csv('dataset/feature/data_test.csv',index=False)


