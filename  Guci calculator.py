print("Name: RITIK\nRoll No.: 25513\nBranch: ECS") 
import tkinter as tk
root = tk.Tk()
root.title("Calculator")
output_label = tk.Label(root, text="0", width=15, height=2, font=('Arial', 20)) 
output_label.grid(row=0, column=0, columnspan=4)
def button_click(button_text):
 current = output_label.cget("text") 
 if current == "0":
  output_label.config(text=button_text) 
 else:
  output_label.config(text=current + button_text)
buttons = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", ".", "=", "/"] 
row = 1
col = 0
for button_text in buttons:
 button = tk.Button(root, text=button_text, width=5, height=2, 
        font=('Arial', 20), command=lambda x=button_text: button_click(x))
button.grid(row=row, column=col) 
col += 1
if col > 3:
 col = 0
 row += 1 
 root.mainloop()