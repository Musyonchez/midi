# import mido

# # Open a MIDI input port
# # Replace 'Port Name' with the name of your MIDI input port
# with mido.open_input('Port Name') as inport:
#     for msg in inport:
#         print(msg)


import rtmidi
import time


def handle_input(message, deltatime):
    print(f"Received MIDI message: {message}, deltatime: {deltatime}")


# Initialize the MIDI input system
midi_in = rtmidi.MidiIn()

# Open a virtual MIDI port
midi_in.open_virtual_port("Virtual InPut Port")
print("MIDI input port opened.")

# Set the callback function to handle incoming messages
midi_in.set_callback(handle_input)

# Keep the script running to listen for MIDI messages
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up
    midi_in.close_port()
