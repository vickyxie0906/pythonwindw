import datasource as ds
from secrets import api_key 


def main():
    print("這裡是MAIN FUNCTION")
    list_data=ds.get_forcast_data(ds.tw_county_names["基隆"],api_key)
    for item in list_data:
        print(item["dt_txt"])
    # print(type(list_data))

if __name__ =="__main__":
    print("這裡是程式的執行點")
    main()