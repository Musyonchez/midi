import mido
import rtmidi

# midi_out = rtmidi.MidiOut()


# Create a MIDI message for a note on event
msg = mido.Message('note_on', note=60, velocity=64)

# Open a MIDI output port
# Replace 'Port Name' with the name of your MIDI output port
# midi_out.open_virtual_port("My Virtual Output")

# # Create a MIDI input and output instance
# midi_out = rtmidi.MidiOut()

# # Open a virtual MIDI output port
# midi_out.open_virtual_port("My Virtual Output")

# # List available MIDI output ports
# print("\nAvailable MIDI output ports:")
# for i in range(midi_out.get_port_count()):
#     print(f"{i}: {midi_out.get_port_name(i)}")

print("Available MIDI output ports:")
for port_name in mido.get_output_names():
    print(port_name)
port = mido.open_output("Midi Through:Midi Through Port-0 14:0")

# Send the MIDI message
port.send(msg)

# Close the port
port.close()


# import time
# import rtmidi

# # Initialize the MIDI output system
# midi_out = rtmidi.MidiOut()

# # Open a virtual MIDI port
# midi_out.open_virtual_port("My Virtual Output")
# print("MIDI output port opened.")

# # Send a note on message
# midi_out.send_message([0x90, 60, 127])  # Note on, middle C, velocity 127
# time.sleep(1.0)  # Wait for 1 second

# # Send a note off message
# midi_out.send_message([0x80, 60, 0])  # Note off, middle C, velocity 0

# # Close the MIDI output port
# midi_out.close_port()
