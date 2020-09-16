from videoprocess import *
import tkinter as tk
from tkinter import filedialog,messagebox,ttk

video=Video_model('','',0,0)

def get_file():
    file=filedialog.askopenfilename(filetypes=[('video files', '.mp4')])
    path_text.insert(tk.END, file)
    path_text.update()
    if file:
        video.video_full_path = file
    else:
        video.video_full_path=''


def start_sr():
    print(video.video_full_path)
    if len(path_text.get())==0:
        sr_result = '未选择文件'
    else:
        video.start_time = int(start_input.get())
        video.end_time = int(end_input.get())
        sr_result=video.do_sr()

    tk.messagebox.showinfo("识别结果", sr_result)

root=tk.Tk()
root.title("netease youdao sr test")
frm = tk.Frame(root)
frm.grid(padx='50', pady='50')

btn_get_file = tk.Button(frm, text='选择待识别视频', command=get_file)
btn_get_file.grid(row=0, column=0,  padx='10', pady='20')
path_text = tk.Entry(frm, width='40')
path_text.grid(row=0, column=1)

start_label=tk.Label(frm,text='开始时刻：')
start_label.grid(row=1,column=0)
start_input=tk.Entry(frm)
start_input.grid(row=1,column=1)

end_label=tk.Label(frm,text='结束时刻：')
end_label.grid(row=2,column=0)
end_input=tk.Entry(frm)
end_input.grid(row=2,column=1)

sure_btn=tk.Button(frm, text='开始识别', command=start_sr)
sure_btn.grid(row=3,column=0,columnspan=3)
root.mainloop()