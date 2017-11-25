-from tkinter import *
-
-def checked(i) :
-      global player
-      button = list[i]
-
-      if button["text"] != "     " :
-            return
-      button["text"] = player 
-      button["bg"] = "yellow"
-
-      if player == "X" :
-            player = "O"
-            button["bg"] = "yellow"
-      else :
-            player = "X"
-            button["bg"] = "lightgreen"
-
-window = Tk()
-player = "X"
-list= []
-
-for i in range(9) :
-      b = Button(window, text="     ", command=lambda k=i: checked(k))
-      b.grid(row=i//3, column=i%3)
-      list.append(b)
-
-window.mainloop()
-


 +from tkinter import * #module call.
 +import tkinter.messagebox #messagebox definition
 +
 +def checked(i) :
 +      global player
 +      button = list[i]
 + # checked function - button is supressed action.     
 + #winner distinction condition.
 +      win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
 +  
 +
 +      if button["text"] != "     " :
 +            return
 +  #button(X,O)exist -reutrn     
 +      button["text"] = player  #button(X,O)not exist-(X or O) select.
 +      button["bg"] = "yellow"
 +
 +      for a in win:
 +            if player == list[a[0]]["text"] == list[a[1]]["text"] == list[a[2]]["text"]:
 +                   tkinter.messagebox.showinfo("game over", "{0}is winner".format(player))
 +                   quit()
 +#player turn confirm 
 +      if player == "X" :
 +            player = "O"
 +            button["bg"] = "yellow"
 +      else :
 +            player = "X"
 +            button["bg"] = "lightgreen"
 +#a conditional sentence.
 +def quit():
 +      for b in list:
 +            b["command"] = ""
 +
 +
 +window = Tk() #game initialization
 +player = "X"
 +list= []
 +#event happen-checked call and list.append(b) - list append.
 +for i in range(9) : #loop 9 time.
 +
 +      b = Button(window, text="     ", command=lambda k=i: checked(k))
 +      b.grid(row=i//3, column=i%3)
 +      list.append(b)
 +
 +window.mainloop()
 +#game end.
 +

