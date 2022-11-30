import datasource as ds  # 載入datasource 縮寫ds
from secrets import api_key  # 引入secrets 的api_key
import tkinter as tk  # 引入tkinter縮寫tk
from tkinter import ttk


# 建立框架
class Window(tk.Tk):  # 繼承TK類別
    def __init__(self, cities_dict):  # 建構子 (城市字典)
        super().__init__()  # 呼叫建構子父類別  # 建立視窗內容標題
        title_Label = tk.Label(self, text="各縣市4天天氣預測", font=(
            "Arial", 20)).pack(padx=30, pady=30)  # 設定標籤文字的大小 字型 間距

        # 建立存放按鈕的容器
        buttons_frame = tk.Frame(self)  # 建立框架
        buttons_frame.pack(padx=50, pady=(0, 30))  # 左右 上下 間距
        # 設定GRID的ROW數量
        grid_row_nums = 3
        # enumerate會回傳索引值 將數據組合為索引序列 一般用在迴圈 加上.items()回傳 key value
        for index, cities in enumerate(cities_dict.items()):
            # print(index,key)
            cname, ename = cities  # key value變數名 #command=self.button_click 註冊
            btn = tk.Button(buttons_frame, text=f"{cname}\n{ename}", font=(
                "Arial", 15), width=8, padx=20, pady=3)
            btn.grid(row=index % grid_row_nums, column=index //
                     grid_row_nums, padx=5, pady=5)
            btn.bind("<Button>", self.button_click)
            # <Button-1>滑鼠左鍵點選的座標XY

            # tk.Button(buttons_frame, text=key, font=("Arial",15),padx=20, pady=3).grid(row=index % 3, column=index//3)
            # 建立按鈕, 字體 15 寬20 高3. grid 網格容器
            # (row=index% 餘數 ,column=index// 整數除法) 欄(column) 列(row)

    # 實體的方法

    def button_click(self, event):
        # print(dir(event))查event方法
        btn_text = event.widget['text']  # -->type=tkinter button
        # widget抓按鈕文字 #屬性widget=button,抓資料["text"]取出文字
        name_list = btn_text.split("\n")  # split分割
        cname = name_list[0]
        ename = name_list[1]
        # print(f"{cname}-{ename}")

        try:
         city_forcase = ds.get_forcast_data(ename, api_key)

        except Exception as e:
            #出現錯誤訊息
            return
            
        # print(cname)
        # print(city_forcase)

        if hasattr(self, "displayFrame"):  # 檢查有沒有原框架
            self.displayFrame.destroy()  # 消滅原來顯示資料的框架 重新再建一個

        self.displayFrame = DisplayFrame(
            self, data=city_forcase, text=cname, borderwidth=2, relief=tk.GROOVE)  # 顯示資料的框架 relief按鈕邊框樣式
        self.displayFrame.pack(fill=tk.BOTH, padx=50, pady=(0, 30))


class DisplayFrame(ttk.LabelFrame):  # 繼承ttk.LabelFrame父類別
    def __init__(self, parent, data=None, **kwargs):  # **kwargs是打包上面DisplayFrame()裡self之後的內容
        super().__init__(parent, **kwargs)  # parent為父類別,**kwargs是dict為引數名稱
        self.city_data = data
        # 拆解資料分3份
        totsl_rows = len(self.city_data)
        column_rows = totsl_rows//3+1
        leftData = self.city_data[:column_rows]  # :=>從0開始 到14
        centerData = self.city_data[column_rows:column_rows*2]  # 14不包含 到28
        rightData = self.city_data[column_rows*2:]  # 28到最後

        leftFrame = CustomFrame(self, data=leftData)
        leftFrame.pack(side=tk.LEFT,padx=10)

        centerFrame = CustomFrame(self, data=centerData)
        centerFrame.pack(side=tk.LEFT, padx=10)

        rightFrame = CustomFrame(self, data=rightData)
        rightFrame.pack(side=tk.LEFT, padx=10)


class CustomFrame(tk.Frame):
    def __init__(self, parent, data=None, **kwargs):  # **kwargs是打包上面CustomFrame()裡self之後的內容
        super().__init__(parent, **kwargs)
        self.list_data = data
        print(self.list_data)
        self.tree = ttk.Treeview(self, columns=['#1', '#2', '#3', '#4'],show='headings',height=10)
        # height=14 當頁顯示14筆
        self.tree.pack(side=tk.LEFT)#網頁先靠左(要先寫不然拉霸會先靠左)

        scrollbar=tk.Scrollbar(self)
        scrollbar.pack(side=tk.LEFT,fill=tk.Y)#拉霸再靠左
        self.tree.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree.yview)


        

        self.tree.heading('#1', text='時間')
        self.tree.heading('#2', text='溫度')
        self.tree.heading('#3', text='狀態')
        self.tree.heading('#4', text='濕度')

        self.tree.column('#1', width=130, anchor='center')
        self.tree.column('#2', width=50, anchor='center')
        self.tree.column('#3', width=80, anchor='center')
        self.tree.column('#4', width=50, anchor='center')

        for item in self.list_data:
            self.tree.insert('', tk.END, values=item)


def main():
    # print("這裡是MAIN FUNCTION")
    window = Window(ds.tw_county_names)  # 建立視窗物件
    window.title("各縣市4天天氣預測")  # 視窗標題
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


if __name__ == "__main__":
    # print("這裡是程式的執行點")#印出訊息
    main()  # 呼叫主函式
