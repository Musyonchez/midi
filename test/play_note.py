import itertools
import tkinter as tk
import mido
from mido import Message
import time

outport = mido.open_output("Midi Through Port-2")


def play_note(note, velocity=64):
    msg = Message("note_on", note=note, velocity=velocity)
    outport.send(msg)
    print(msg)
    # Optionally, send a 'note_off' message to stop the note
    msg_off = Message("note_off", note=note, velocity=velocity)
    outport.send(msg_off)
    print(f"Playing note {note}")


# Create the main window
root = tk.Tk()
root.title("Piano Tutorial")

# Create a grid of buttons for the piano keys
for row, col in itertools.product(range(3), range(8)):
    note = row * 8 + col + 21  # Example: Start from C3
    button = tk.Button(
        root, text=f"Key {note}", command=lambda note=note: play_note(note)
    )
    button.grid(row=row, column=col)

# Start the main loop
root.mainloop()
