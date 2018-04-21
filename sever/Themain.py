import json
import tkinter 
import The1,The2,The3,The4,The5
import Data1,Date2

class Main():
    def __init__(self):
        self.isConnect = False
    
    class Login():
        """登录界面"""
        def __init__(self, father):
            self.father = father

        @staticmethod
        def center_window(root, width, height):  
            screenwidth = root.winfo_screenwidth()  
            screenheight = root.winfo_screenheight()  
            size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)  
            root.geometry(size)

        @staticmethod
        def gologin(self,shuru1_text,shuru2_text,loginWindow):
            zhang = shuru1_text.get()
            mima = shuru2_text.get()

            mainFrame = self.father.MainFrame(self.father)
            loginWindow.destroy()
            mainFrame.__main__()

        @staticmethod
        def window(self):
            """登录窗口GUI"""
            k = tkinter.Tk()
            self.center_window(k,300,150)
            k.title('登录界面')
            
            lb=tkinter.Label(k,text="账号",bg='#FFFFFF',width=8)
            lb.place(x=12,y=40)
            shuru1_text = tkinter.Entry()
            shuru1_text.place(x=80,y=40,anchor='nw')
            
            lb=tkinter.Label(k,text="密码",bg='#FFFFFF',width=8)
            lb.place(x=12,y=80)
            shuru2_text = tkinter.Entry()
            shuru2_text.place(x=80,y=80,anchor='nw')
            
            clear = tkinter.Button(k, text = "ENTER",command = lambda : self.gologin(self,shuru1_text,shuru2_text,k))
            clear.place(x = 150, y = 120, anchor = 'center')

            k.mainloop()

        def __main__(self):
            # 建立窗口
            self.window(self)

    class MainFrame():
        SerialNumber = 0

        def __init__(self, father):
            self.father = father

        class Window():
            def __init__(self, father):
                self.father = father

            @staticmethod
            def getchar(self,thestr):
                textArea = self.father.textArea
                textArea.insert('end',thestr)

            @staticmethod
            def gettext(self,user_text,SerialNumber):
                i = SerialNumber[0]
                thestr = user_text.get()
                if i == 1:
                    theone = The1.Main(thestr)
                    self.getchar(self,theone)
                elif i==2:
                    theone = The2.Main(thestr)
                    self.getchar(self,theone)
                elif i==3:
                    theone = The3.Main(thestr)
                    self.getchar(self,theone)
                elif i==4:
                    theone = The4.Main(thestr)
                    self.getchar(self,theone)
                elif i==5:
                    theone = Data1.Main(thestr)
                    self.getchar(self,theone)
                elif i==6:
                    theone = Date2.Main()
                    self.getchar(self,theone)

            @staticmethod
            def changeSendTo(self,listbox,lb_name,SerialNumber):
                lb_name = listbox.get(listbox.curselection())
                SerialNumber[0] = lb_name
                TheString = "无服务"
                if lb_name == 6:
                    TheString = "系数"
                elif lb_name == 5 :
                    TheString = "雷达图"
                elif lb_name == 1:
                    TheString = "请输入你要查询的用户名"
                self.getchar(self,TheString)

            @staticmethod
            def center_window(root, width, height):  
                screenwidth = root.winfo_screenwidth()  
                screenheight = root.winfo_screenheight()  
                size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)  
                root.geometry(size)  

            def __main__(self):
                SerialNumber = [0]
                father = self.father
                tk = tkinter.Tk()
                tk.title('测试窗口')
                self.center_window(tk, 600, 400)    

                # 聊天内容框
                textArea = tkinter.Text(tk, bg = '#FFFFFF', width = 60,height = 22, bd = 0)
                textArea.place(x = 10, y = 10, anchor = 'nw')
                textArea.bind("<KeyPress>", lambda x : "break")
                father.textArea = textArea
                textArea.focus_set()

                # 右侧选择聊天对象
                tkinter.Label(tk, text = "双击选择发送对象:", bg = "#EEEEEE").place(x = 460, y = 10, anchor = 'nw')
                listbox = tkinter.Listbox(tk, width = 13, height = 13, bg = '#FFFFFF')
                listbox.place(x = 460, y = 35, anchor = 'nw')
                for it in range(100):
                    listbox.insert(tkinter.END,it)
                father.listbox = listbox
                lb_name = 0
                listbox.bind('<Double-Button-1>',lambda x : self.changeSendTo(self,listbox,lb_name,SerialNumber))

                # 下方内容输入
                lb = tkinter.Label(tk, text="输入",bg='#FFFFFF',width=8)
                lb.place(x=12,y=360)
                user_text = tkinter.Entry()
                user_text.place(x=90,y=360,anchor = 'nw')

                #按钮
                bt_clear = tkinter.Button(tk, text = "清屏",command = lambda : textArea.delete(0.0, 'end'))
                bt_clear.place(x = 560, y = 372, anchor = 'center')
                bt_send = tkinter.Button(tk, text = "输入",command = lambda : self.gettext(self,user_text,SerialNumber))
                bt_send.place(x = 480, y = 371, anchor = 'center')
                tk.mainloop() 

        def __main__(self):
            # 建立窗口
            window = self.Window(self)
            window.__main__()
            self.window = window

    def __main__(self):
        #pass
        login = Main.Login(self)
        login.__main__()

if __name__ == '__main__':
    main = Main()
    main.__main__()

