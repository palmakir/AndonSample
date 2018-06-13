import tkinter as tk
import time
import json
from tkinter import *
from datetime import datetime
from winsound import *
import urllib
from urllib.parse import urlencode
import requests
from urllib.request import Request,urlopen

class A:
    cflag=0;
    tflag=0;
    def restart_program(self):
        try:
            root.destroy()
        except:
            self.tflag=1;
        root2 = tk.Tk()
        A(root2)
        root2.mainloop()
    def __init__(self,master):
        try:        
            master.geometry("1200x650")
            
            self.frame2=tk.Frame(master, bg='black')
            self.frame2.pack(side="top",fill="both", expand=True)

                
            self.frame5=tk.Frame(master,bg='black')
            self.frame5.pack(side="top",fill="both", expand=True)
            
            self.frame=tk.Frame(master,bg='black')
            self.frame.pack(side="top",fill="both", expand=True)
            
            self.frame3=tk.Frame(master,bg='black')
            self.frame3.pack(side="top",fill="both", expand=True)
            
        
            self.frame4=tk.Frame(master,bg='black')
            self.frame4.pack(side="top",fill="both", expand=True)
            

            #2
            self.label3=tk.Label(self.frame2, borderwidth=2, relief="sunken",width=10,height=1)
            self.label3.configure(text='SIEMENS',fg='cyan',bg='black',font=("Gill Sans", 15))

            self.label8=tk.Label(self.frame2, borderwidth=2, relief="sunken",width=50,height=1)
            self.label8.configure(text='Company Name',fg='Red',bg='black',font=("Gill Sans", 15))

            self.label8.pack(side="left", fill="both",expand=True)
            self.label3.pack(side="left", fill="both",expand=True)

            #2nd from top
            self.label12=tk.Label(self.frame5, borderwidth=0, relief="sunken",width=10,height=1)
            self.label12.configure(text='Plan',fg='red',bg='black',font=("Gill Sans", 15))

            self.label13=tk.Label(self.frame5, borderwidth=0, relief="sunken",width=45,height=1)
            self.label13.configure(text='Current Takt Balance(mm:ss)\n',fg='Red',bg='black',font=("Gill Sans", 15))

            self.label14=tk.Label(self.frame5, borderwidth=0, relief="sunken",width=10,height=1)
            self.label14.configure(text='Date and \nTime(hh:mm:ss)',fg='Red',bg='black',font=("Gill Sans", 15))

            self.label12.pack(side="left", fill="both",expand=True)
            self.label13.pack(side="left", fill="both",expand=True)
            self.label14.pack(side="left", fill="both",expand=True)

            #1
            self.label=tk.Label(self.frame, borderwidth=2, relief="sunken",width=11)
            self.label.configure(text='Time',fg='Red',bg='black',font=("Courier", 15))
            self.count = str(datetime.now())
            self.update_label()
            #1b
            self.label6=tk.Label(self.frame, borderwidth=2, relief="sunken",width=8)
            self.label6.configure(text='NA',fg='Red',bg='black',font=("Courier", 20))
            #self.update_label6()
            #1c
            self.label7=tk.Label(self.frame, borderwidth=2, relief="sunken",width=10,height=3)
            self.label7.configure(text='NA',fg='Red',bg='black',font=("Courier", 75))
            #self.update_label7()
            
            self.label6.pack(side="left",fill="both", expand=True)
            self.label7.pack(side="left", fill="both",expand=True)
            self.label.pack(side="left", fill="both",expand=True)
            
            #3
            self.label2=tk.Label(self.frame3, borderwidth=2, relief="ridge",width=10)
            self.label2.configure(text='NA\nNA',fg='Red',bg='black',font=("Courier", 15))
            self.update_label2()
            #4
            self.label4=tk.Label(self.frame3, borderwidth=2, relief="ridge",width=10)
            self.label4.configure(text='NA\nNA',fg='Red',bg='black',font=("Courier", 15))
            self.update_label4()
            #5
            self.label5=tk.Label(self.frame3, borderwidth=2, relief="ridge",width=10)
            self.label5.configure(text='NA\nNA',fg='Red',bg='black',font=("Courier", 15))
            self.update_label5()
            #2nd last bottom left,right
            self.label10=tk.Label(self.frame3, borderwidth=2, relief="ridge",width=15)
            self.label10.configure(text='Actual\n2',fg='Red',bg='black',font=("Courier", 15))
            #self.update_label10()
            
            self.label11=tk.Label(self.frame3, borderwidth=2, relief="ridge",width=15,height=4)
            self.label11.configure(text='Downtime(mm:ss)\n/plant running shift\n\n',fg='Red',bg='black',font=("Courier", 15))
            self.update_label11()
            
            self.label10.pack(side="left",fill="both", expand=True)
            self.label2.pack(side="left",fill="both", expand=True)
            self.label4.pack(side="left",fill="both", expand=True)
            self.label5.pack(side="left", fill="both",expand=True)
            self.label11.pack(side="left",fill="both", expand=True)
            #lastlabel,i.e.bottom
            self.label9=tk.Label(self.frame4, borderwidth=2, relief="ridge",width=10)
            self.label9.configure(text='NA',fg='Red',bg='black',font=("Courier", 15),anchor=W,justify=LEFT)
            self.update_label9()
            self.label9.pack(side="left", fill="both",expand=True)
        except:
            c=0
            try:
                d=root.winfo_x();
            except:
                c=1
            self.frame6=tk.Frame(master,bg='black')
            self.frame6.pack(side="top",fill="both", expand=True)
            self.labelerr=tk.Label(self.frame6, borderwidth=2, relief="sunken",width=50,height=1)
            if(c==0):
                self.labelerr.configure(text='Internet Connection Unavailable',fg='Blue',bg='black',font=("Gill Sans", 15))                    
                self.retryb = tk.Button(self.frame6, text="Click to Retry",borderwidth=2, relief="raise",command=self.restart_program)
                self.retryb.configure(fg='Red',bg='black',font=("Courier", 15))
                self.retryb.pack(side="left", fill="both",expand=True)
                c=1;
            else:
                self.labelerr.configure(text='Close the system and turn on again',fg='Blue',bg='black',font=("Gill Sans", 15))
                
            self.labelerr.pack(side="left", fill="both",expand=True)
    
    def update_label(self):
            self.label.configure(text = '{}'.format(self.count))
            self.label.after(2000, self.update_label) # call this method again in 2,000 milliseconds
            self.count =str(datetime.now())[:10]+"\n"+str(datetime.now())[11:16]
    def update_label2(self):

            try:
                url='http://pruthveshdesai.000webhostapp.com/receive2.php'
                jsond=urlopen(url).read().decode()
                sconc=""
                data  = json.loads(jsond)
                if(len(data)>=1):
                    sconc=data[len(data)-1]['body']
                    sconcb=''
                    if(len(sconc)>15):
                        j=len(sconc)
                        k=0
                        while(j>15):
                            sconcb=sconcb+sconc[k:k+16]+"\n"
                            j=j-15
                            k=k+16
                        sconcb=sconcb+sconc[k:len(sconc)]
                        sconc=sconcb
                    self.label2.configure(text = data[len(data)-1]['title']+"\n"+sconc)
                
                self.label2.after(50000, self.update_label2)                    
            except:
                self.update_label2()
    #NOTredundant method check update_label2
    def update_label4(self):
            url='http://pruthveshdesai.000webhostapp.com/receive2.php'
            jsond=urlopen(url).read().decode()
            sconc=""
            data  = json.loads(jsond)
            if(len(data)>=2):
                sconc=data[len(data)-2]['body']
                sconcb=''
                if(len(sconc)>15):
                    j=len(sconc)
                    k=0
                    while(j>15):
                        sconcb=sconcb+sconc[k:k+16]+"\n"
                        j=j-15
                        k=k+16
                    sconcb=sconcb+sconc[k:len(sconc)]
                    sconc=sconcb
                self.label4.configure(text = data[len(data)-2]['title']+"\n"+sconc)
            self.label4.after(50000, self.update_label4)
    #NOTredundant method check update_label2
    def update_label5(self):
            url='http://pruthveshdesai.000webhostapp.com/receive2.php'
            jsond=urlopen(url).read().decode()
            sconc=""
            data  = json.loads(jsond)
            if(len(data)>=3):
                sconc=data[len(data)-3]['body']
                sconcb=''
                if(len(sconc)>15):
                    j=len(sconc)
                    k=0
                    while(j>15):
                        sconcb=sconcb+sconc[k:k+16]+"\n"
                        j=j-15
                        k=k+16
                    sconcb=sconcb+sconc[k:len(sconc)]
                    sconc=sconcb
                self.label5.configure(text = data[len(data)-3]['title']+"\n"+sconc)
            self.label5.after(50000, self.update_label5)
    def update_label9(self):
            url='http://pruthveshdesai.000webhostapp.com/receive3.php'
            jsond=urlopen(url).read().decode()
            sconc=""
            data  = json.loads(jsond)
            if(len(data)>=1):
                sconc=data[0]['msg']
                self.label9.configure(text = sconc)
                self.label9.after(10000, self.update_label9)
            if(sconc[0:13]=='Xdistress123X' and self.cflag==0):
                PlaySound('alarmsound.wav', SND_FILENAME)
                self.cflag=self.cflag+1;
                self.label9.configure(text=sconc)
            if(sconc[0:13]!='Xdistress123X'):
                self.cflag=0;
            if(sconc[0:13]=='Xshutdown123X'):
                data = {'msg':'Turned On by System'}
                requests.post(url = 'http://pruthveshdesai.000webhostapp.com/add_siemens3.php', data = data)
                root.destroy()

    def update_label11(self):
        url='http://pruthveshdesai.000webhostapp.com/receive4.php'
        jsond=urlopen(url).read().decode()
        sconc='Downtime(mm:ss)\n/plant running shift\n\n'
        data  = json.loads(jsond)
        if(len(data)>=1):
            sconc=sconc+data[0]['dt']
            sconc2='Actual\n'+data[0]['actual']
            sconc3=data[0]['plan']
            sconc4=data[0]['tlkt']
            self.label10.configure(text = sconc2)            
            self.label6.configure(text = sconc3)            
            self.label7.configure(text = sconc4)
            self.label11.configure(text = sconc)
            self.label11.after(10000, self.update_label11)
    #redundant method check update_label11
    def update_label10(self):
        url='http://pruthveshdesai.000webhostapp.com/receive4.php'
        jsond=urlopen(url).read().decode()
        sconc='Actual\n'
        data  = json.loads(jsond)
        if(len(data)>=1):
            sconc=sconc+data[0]['actual']
            self.label10.configure(text = sconc)
            self.label10.after(10000, self.update_label10)
    #redundant method check update_label11        
    def update_label6(self):
        url='http://pruthveshdesai.000webhostapp.com/receive4.php'
        jsond=urlopen(url).read().decode()
        sconc=''
        data  = json.loads(jsond)
        if(len(data)>=1):
            sconc=sconc+data[0]['plan']
            self.label6.configure(text = sconc)
            self.label6.after(10000, self.update_label6)
    #redundant method check update_label11        
    def update_label7(self):
        url='http://pruthveshdesai.000webhostapp.com/receive4.php'
        jsond=urlopen(url).read().decode()
        sconc=''
        data  = json.loads(jsond)
        if(len(data)>=1):
            sconc=sconc+data[0]['tlkt']
            self.label7.configure(text = sconc)
            self.label7.after(10000, self.update_label7)
    
root = tk.Tk()

A(root)
root.mainloop()
