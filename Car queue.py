import queue
from tkinter import *
from tkinter import ttk
import time
car_queue = []
q = queue.Queue()
def start():
    global car_queue
    global player_co
    global tab1
    tab1 = Tk()
    tab1.geometry("240x90")
    tab1.title("Car registrations")
    player_co = ttk.Entry(tab1, text = "Co-ordinate")
    player_co.place(relx = 0.5,rely = 0.1,anchor = 'center')
    Label = ttk.Label(tab1,text ="Put your cars' registration here!")
    Label.place(relx = 0.5,rely = 0.8,anchor = 'center')
    player_co.pack()
    nice_button = ttk.Button(tab1, text = 'Submit!', command=submit_value)
    nice_button.place(relx = 0.5, rely = 0.4,anchor = 'center')
    root.destroy()
def submit_value():
    x = True
    front = 0
    car_queue.append(player_co.get())
    stop = input(str("want to stop?"))
    if stop == "yes":
        tab1.destroy()
        for queue in car_queue:
            q.put(queue)
            print(q.get(queue))
            print("...")
            time.sleep(3)
        print("the cars have all queued up!")
        print("now, it's their time to go!")
        print("remember the front pointer is always at '1' (or 0 in terms of index)")
        while x == True:
            time.sleep(5)
            rear = len(car_queue)
            rear_pointer = str(rear)
            dequeue = str(car_queue.pop(0))
            print("")
            print(dequeue + " dequeued")
            print("rear pointer points to " + rear_pointer)
            if rear - 1 == front:
                print("all items gone :(, now you have SOME SPACE!!!!!")
                x = False
            else:
                print("still some left")
    else:
        print("continue then!")
root = Tk()
frm = ttk.Frame(root, padding=10)
root.geometry("640x480")
frm.grid()
root.title("My car queue")
Label_middle = ttk.Label(root,text ='Welcome to my car queue')
Label_middle.place(relx = 0.5,rely = 0.1,anchor = 'center')
battleship=PhotoImage(file='car.png')
nice_button = ttk.Button(root, text = 'Click Me !', image = battleship, command=start)
nice_button.place(relx = 0.5, rely = 0.5,anchor = 'center')
root.mainloop()
