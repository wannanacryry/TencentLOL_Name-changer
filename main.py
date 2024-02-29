# 导入所需的库
import tkinter as tk
import psutil
import subprocess
from time import sleep
import tkinter.messagebox as massagebox

# 定义一些常量
LOL_PATH = "E:\\LOL\\LOL\\LeagueClient\\LeagueClient.exe" # LOL的路径
LOL_NAME = "LeagueClient.exe" # LOL的进程名
RIOT_NAME = "RiotClientServices.exe" # Riot的进程名
LOCALE = "zh_CN" # 原始的语言参数
NEW_LOCALE = "fr_FR" # 新的语言参数
killvar = 0
var = 0
pid = 0
# 创建一个窗口
window = tk.Tk()
window.title("LOL Launcher")
window.geometry("400x400")


# 创建一个标签，显示LOL是否在运行
lol_status = tk.StringVar()
lol_status.set("检测中...")
lol_label = tk.Label(window, textvariable=lol_status)
lol_label.pack()

#展示现在的语言
lollangstats = tk.Entry(window)
lollangstats.pack()
lollangstats.insert(tk.END,"目前的语言是" + NEW_LOCALE)

# 创建一个文本框，显示获取到的参数
lol_args = tk.StringVar()
lol_args.set("无")
args_label = tk.Label(window, text="获取到的参数:")
args_text = tk.Text(window, height=5, width=40)
args_text.insert(tk.END, lol_args.get())
args_label.pack()
args_text.pack()
count = tk.Label(window, text=var)

# 创建一个文本框，显示修改后的参数
new_args = tk.StringVar()
new_args.set("无")
new_label = tk.Label(window, text="修改后的参数:")
new_text = tk.Text(window, height=5, width=40)
new_text.insert(tk.END, new_args.get())
new_label.pack()
new_text.pack()


lang_args = tk.StringVar()
lang_args.set(NEW_LOCALE)
lang_label = tk.Label(window, text="需要修改后的语言:")
lang_text = tk.Text(window, height=2, width=25)
lang_text.insert(tk.END, "")
lang_label.pack()
lang_text.pack()

#修改语言按钮事件
def changelang():
    global NEW_LOCALE
    NEW_LOCALE = lang_text.get(tk.END)
    lollangstats.insert(tk.END, "目前的语言是" + NEW_LOCALE)


# 创建一个函数，结束LOL进程
def kill_lol():
    global lol_process
    if lol_process is not None:
        lol_process.kill() # 结束进程
        lol_process = None
        lol_status.set("已结束")

# 创建一个函数，启动新的LOL
def start_lol():
    global lol_process
    lol_process = subprocess.Popen([LOL_PATH] + new_args.get().split()) # 启动进程，添加修改后的参数
    lol_status.set("已启动")




# 创建一个函数，恢复LOL进程
def resume_lol():
    global lol_process
    if lol_process is not None and lol_process.status() == "stopped": # 如果LOL进程存在，且处于暂停状态
        lol_process.resume() # 恢复进程
        lol_status.set("已恢复")
    else: # 如果LOL进程不存在，或者已经被终止
        lol_status.set("无法恢复")

def clearall ():
    global pid
    pid = 0
    args_text.delete(1.0, tk.END)
    new_text.delete(1.0, tk.END)
    check_lol()



# 创建三个按钮，分别绑定上述函数
kill_button = tk.Button(window, text="结束LOL", command=kill_lol)
kill_button.pack(side=tk.LEFT)
start_button = tk.Button(window, text="启动新的LOL", command=start_lol)
start_button.pack(side=tk.RIGHT)
resume_button = tk.Button(window, text="恢复LOL", command=resume_lol)
resume_button.pack(side=tk.TOP)
reset_button = tk.Button(window, text="开始检测", command=clearall)
reset_button.pack(side = tk.TOP),
changelang_button = tk.Button(window, text="修改语言", command=changelang)
changelang_button.pack(side = tk.TOP),

# 创建一个全局变量，存储LOL的进程对象
lol_process = None


def check_lol():
        global lol_process
        global pid
        for process in psutil.process_iter(): # 遍历所有进程
            if process.name() == LOL_NAME: # 如果找到LOL进程
                pid = process.pid
                dosomething(process,pid)
            if pid != 0:

                break

        else: # 如果没有找到LOL进程
            lol_process = None # 清空进程对象
            lol_status.set("未运行") # 更新状态
        window.after(50, check_lol) # 1秒后再次检测LOL状态

def dosomething(process,pid):
    global lol_process
    lol_process = process  # 保存进程对象
    lol_status.set("已运行")  # 更新状态
    args = process.cmdline()  # 获取进程的启动参数
    lol_args.set(" ".join(args))  # 更新参数
    global var
    var = + 1
    print (var)
    new_args.set(" ".join(args).replace(LOCALE, NEW_LOCALE))  # 替换语言参数，更新修改后的参数
    args_text.delete(1.0, tk.END)  # 清空文本框
    args_text.insert(tk.END, lol_args.get())
    new_text.delete(1.0, tk.END)  # 清空文本框
    new_text.insert(tk.END, new_args.get())
    process = psutil.Process(pid)
    process.suspend()  # 暂停进程


window.mainloop()
