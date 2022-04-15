import tkinter
from tkinter import *


from client import Client


class Window(object):
    """シュミレーターの画面部分のみを作っているクラス"""

    def __init__(self):

        # ここから下がGUI画面作成コード ===========================================================================
        root = Tk()
        root.title('上位伝送シミュレータ')
        root.geometry("600x650")

        # ラベル作成----------------------------------------------------------------------------------------------
        info_label = Label(text='接続先情報')
        info_label.place(x=90, y=10)

        ip_label = Label(text='IPアドレス')
        ip_label.place(x=30, y=50)
        port_label = Label(text='Port番号')
        port_label.place(x=30, y=70)

        self.string_variable = tkinter.StringVar()
        self.string_variable.set('接続状態')
        connection_label = Label(textvariable=self.string_variable, background='#778899')
        connection_label.place(x=30, y=135, width=200)

        send_message_label = Label(text='送信メッセージ')
        send_message_label.place(x=30, y=255)

        receive_message_label = Label(text='受信メッセージ')
        receive_message_label.place(x=300, y=255)

        # Entry作成（一行入力ボックス表示の部分）---------------------------------------------------------------------------
        ip_entry = Entry()
        ip_entry.insert(tkinter.END, '192.168.8.225')  # のちに削除
        ip_entry.place(x=100, y=50, width=130)
        self.ip_entry_value = ip_entry.get()

        port_entry = Entry()
        port_entry.insert(tkinter.END, '50000')  # のちに削除
        port_entry.place(x=100, y=70, width=130)
        self.port_entry_value = int(port_entry.get())

        # ボタン作成（接続, 送信、切断、送信b、クリア)--------------------------------------------------------------------
        self.client = Client(self.ip_entry_value, self.port_entry_value, )

        connect_button = Button(text='接続 (CL)',
                                command=self.client.connect(self.ip_entry_value, self.port_entry_value))
        connect_button.place(x=30, y=100, width=200)

        send_button = Button(text='送信', command=TODO)  # 引数をとるメソッドの場合lambda のしないと
        send_button.place(x=30, y=170, width=90)

        disconnect_button = Button(text='切断', command=TODO)
        disconnect_button.place(x=140, y=170, width=90)

        send_b_button = Button(text='送信（ｂ）', command=TODO)
        send_b_button.place(x=30, y=200, width=90)

        clear_button = Button(text='クリア', command=TODO)
        clear_button.place(x=140, y=200, width=90)

        # テキストエリア作成------------------------------------------------------------------------------------------
        send_textarea = tkinter.Text(root)
        send_textarea.insert(1.0, '送信テスト')
        send_textarea.place(x=30, y=280, width=240)

        receive_textarea = tkinter.Text(root)
        receive_textarea.insert(1.0, '受信テスト')
        receive_textarea.place(x=300, y=280, width=240)

        log_textarea = tkinter.Text(root)
        log_textarea.insert(1.0, '通信解析ログ')
        log_textarea.place(x=260, y=135, width=300, height=100)

        # スクロールバーの作成---------------------------------------------------------------------------------------
        send_y_scrollbar = tkinter.Scrollbar(
            send_textarea,
            orient=tkinter.VERTICAL
        )
        send_y_scrollbar.place(x=222, y=0)
        send_y_scrollbar.configure(command=send_textarea.yview)
        send_textarea.config(yscrollcommand=send_y_scrollbar.set)

        receive_y_scrollbar = tkinter.Scrollbar(
            receive_textarea,
            orient=tkinter.VERTICAL
        )
        receive_y_scrollbar.place(x=220, y=0)
        receive_y_scrollbar.configure(command=receive_textarea.yview)
        receive_textarea.config(yscrollcommand=send_y_scrollbar.set)

        # チェックボックス作成-------------------------------------------------------------------------------------------
        self.check_value = tkinter.BooleanVar(value=False)
        checkbox = tkinter.Checkbutton(
            root,
            text='自動送信',
            command=TODO,
            variable=self.check_value
        )
        checkbox.place(x=450, y=100)

        # リストボックス作成-----------------------------------------------------------------------------------------
        with open('b.csv', 'rb') as f:
            f.read()

        v = StringVar(value=list)
        list_box = Listbox(
            root,
            listvariable=v,
            selectmode='single',
            height=4
        )
        list_box.place(x=260, y=60, width=190)

        # GUI表示させる---------------------------------------------------------------------------------------------
        root.mainloop()


def TODO():
    """
    in the button command,
    you can write client side method.
    like as connect, close, and so on
    """
    pass


if __name__ == '__main__':
    win = Window()
