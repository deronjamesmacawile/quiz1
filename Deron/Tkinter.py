import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

frame = tk.Frame(root)
frame.pack()

canvas = tk.Canvas(frame, width=300, height=300, highlightthickness=0)
canvas.place(x=0, y=0)

def draw_winning_line(start_row, start_col, end_row, end_col):
    x1 = start_col * 100 + 50
    y1 = start_row * 100 + 50
    x2 = end_col * 100 + 50
    y2 = end_row * 100 + 50
    canvas.create_line(x1, y1, x2, y2, width=6, fill="blue")

def highlight_winner(cells):
    for row, col in cells:
        buttons[row][col].config(fg="gold")

def check_winner():
    # Rows
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            draw_winning_line(i, 0, i, 2)
            highlight_winner([(i,0),(i,1),(i,2)])
            return True

    # Columns
    for i in range(3):
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            draw_winning_line(0, i, 2, i)
            highlight_winner([(0,i),(1,i),(2,i)])
            return True

    # Diagonal \
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        draw_winning_line(0, 0, 2, 2)
        highlight_winner([(0,0),(1,1),(2,2)])
        return True

    # Diagonal /
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        draw_winning_line(0, 2, 2, 0)
        highlight_winner([(0,2),(1,1),(2,0)])
        return True

    return False

def check_draw():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

def button_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        buttons[row][col]["fg"] = "red" if current_player == "X" else "green"

        if check_winner():
            disable_buttons()
            messagebox.showinfo("Game Over", f"🎉 Player {current_player} Wins!")
            return

        if check_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            return

        current_player = "O" if current_player == "X" else "X"

def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state="disabled")

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(
            frame,
            text="",
            font=("Arial", 32, "bold"),
            width=4,
            height=2,
            command=lambda r=row, c=col: button_click(r, c)
        )
        buttons[row][col].grid(row=row, column=col)

root.mainloop()
