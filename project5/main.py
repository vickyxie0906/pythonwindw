import datasource

def main():
    print("這裡是MAIN FUNCTION")
    list_data=datasource.get_forcast_data()
    for item in list_data:
        print(item["dt_txt"])
    # print(type(list_data))

if __name__ =="__main__":
    print("這裡是程式的執行點")
    main()