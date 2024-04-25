import time
import rtmidi

# Initialize the MIDI output system
midi_out = rtmidi.MidiOut()

# Open a virtual MIDI port
midi_out.open_virtual_port("My Virtual Output")
print("MIDI output port opened.")

# Send a note on message
midi_out.send_message([0x90, 60, 127])  # Note on, middle C, velocity 127
time.sleep(1.0)  # Wait for 1 second

# Send a note off message
midi_out.send_message([0x80, 60, 0])  # Note off, middle C, velocity 0

# Close the MIDI output port
midi_out.close_port()
