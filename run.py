import tkinter as tk
import webview

def search():
    # 獲取輸入框中的搜尋詞
    query = entry.get()

    # 構造Google搜尋URL
    search_url = f"https://www.google.com/search?q={query}"

    # 使用預設瀏覽器打開搜尋結果頁面
    webview.create_window("My Webview", search_url)
    webview.start()

# 創建Tkinter視窗
root = tk.Tk()

# 創建輸入框
entry = tk.Entry(root, width=50)
entry.pack()

# 創建搜尋按鈕
button = tk.Button(root, text="搜尋", command=search)
button.pack()

# 運行Tkinter事件迴圈
root.mainloop()

