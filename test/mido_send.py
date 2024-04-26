import mido
from mido import Message
import time

print(mido.get_output_names())

# Create a MIDI output port
outport = mido.open_output("Midi Through Port-2")


# Function to send a MIDI message
def send_midi_message(note, velocity=64):
    msg = Message("note_on", note=note, velocity=velocity)
    outport.send(msg)
    print(msg)
    # Optionally, send a 'note_off' message to stop the note
    msg_off = Message("note_off", note=note, velocity=velocity)
    outport.send(msg_off)


# Loop to continuously send MIDI messages
try:
    while True:
        # Example: Send a middle C note
        send_midi_message(60)
        # Wait for a short period before sending the next message
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    outport.close()
