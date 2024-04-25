import time
import rtmidi
from rtmidi.midiutil import open_midiinput, open_midioutput

# Function to handle incoming MIDI messages
def midi_in_callback(message, time_stamp):
    print(f"Received MIDI message: {message}")

# Open a virtual output port for sending
mo, _ = open_midioutput(use_virtual=True)

# Open a virtual input port for receiving
mi, _ = open_midiinput(use_virtual=True)

# Set the callback function for the input port
mi.set_callback(midi_in_callback)

# Send a MIDI message
mo.send_message([0x90, 60, 127]) # Note on, middle C, velocity 127

# Wait for a moment to receive the message
time.sleep(1)

# Close the ports
mo.close_port()
mi.close_port()
