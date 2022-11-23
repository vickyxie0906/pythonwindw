import datasource as ds
from secrets import api_key 
import tkinter as tk


class Window(tk.Tk):
    def __init__(self,cities_dict):
        super().__init__()
        title_Label = tk.Label(self, text="各縣市4天天氣預測", font=(
            "Arial", 20)).pack(padx=30, pady=30)

        #建立存放按鈕的容器
        buttons_frame=tk.Frame(self)
        buttons_frame.pack(padx=50,pady=(0,30))

        for  index,key in enumerate(cities_dict):
            # print(index,key)
            tk.Button(buttons_frame, text=key, font=("Arial",15),padx=20, pady=5).grid(row=index % 3, column=index//3)
            # (row=index%4 餘數 ,column=index//4)
        
        # for key in cities_dict:
        #     tk.Button(buttons_frame, text=key).pack(side=tk.LEFT)
            # print(key)
        



def main():
    # print("這裡是MAIN FUNCTION")
    window=Window(ds.tw_county_names)
    window.title("各縣市4天天氣預測")
    window.mainloop()



    '''
    try:
        list_data=ds.get_forcast_data(ds.tw_county_names["金門"],api_key)
    except Exception as e:
        print(e)
        return
    
    for item in list_data:
        print(item["dt_txt"])
    '''   
    # print(type(list_data))

if __name__ =="__main__":
    # print("這裡是程式的執行點")
    main()