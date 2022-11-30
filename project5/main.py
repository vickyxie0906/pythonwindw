import datasource as ds  # 載入datasource 縮寫ds
from secrets import api_key  # 引入secrets 的api_key
import tkinter as tk  # 引入tkinter縮寫tk

#建立框架
class Window(tk.Tk): #繼承TK類別
    def __init__(self,cities_dict): #建構子 (城市字典)
        super().__init__()#呼叫建構子父類別  # 建立視窗內容標題
        title_Label = tk.Label(self, text="各縣市4天天氣預測", font=(
            "Arial", 20)).pack(padx=30, pady=30) #設定標籤文字的大小 字型 間距

        #建立存放按鈕的容器
        buttons_frame=tk.Frame(self) #建立框架
        buttons_frame.pack(padx=50,pady=(0,30)) #左右 下上 間距
        #設定GRID的ROW數量
        grid_row_nums=3
        for index, cities in enumerate(cities_dict.items()):  # enumerate會回傳索引值 將數據組合為索引序列 一般用在迴圈 加上.items()回傳 key value
            # print(index,key)
            cname, ename = cities  # key value變數名 #command 註冊
            tk.Button(buttons_frame, text=f"{cname}\n{ename}", command=self.button_click,font=("Arial", 15),width=8,
                      padx=20, pady=3).grid(row=index % grid_row_nums, column=index//grid_row_nums)
            # tk.Button(buttons_frame, text=key, font=("Arial",15),padx=20, pady=3).grid(row=index % 3, column=index//3)
            # 建立按鈕, 字體 15 寬20 高3. grid 網格容器
            # (row=index% 餘數 ,column=index// 整數除法) 欄(column) 列(row)
        
        # for key in cities_dict:
        #     tk.Button(buttons_frame, text=key).pack(side=tk.LEFT)
            # print(key)
        
    #實體的方法
    def button_click(self):
        print("user click")
        



def main():
    # print("這裡是MAIN FUNCTION")
    window=Window(ds.tw_county_names)#建立視窗物件
    window.title("各縣市4天天氣預測")#視窗標題
    window.mainloop()  # 進入持續處理視窗循環



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

if __name__ =="__main__":#
    # print("這裡是程式的執行點")#印出訊息
    main()#呼叫主函式