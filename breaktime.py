import time
import webbrowser

total_breaks =3
break_count = 0

print ("This program is started"+time.ctime())

while(break_count < total_breaks):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=eK0IIyBlYew&list=RDswK9YJrUbsY&index=2")
    break_count = break_count + 1
