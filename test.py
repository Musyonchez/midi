import rtmidi

# Create a MIDI input and output instance
midi_in = rtmidi.MidiIn()
midi_out = rtmidi.MidiOut()

# Open a virtual MIDI output port
midi_out.open_virtual_port("My Virtual Output")
midi_in.open_virtual_port("My Virtual Input")

# List available MIDI input ports
print("Available MIDI input ports:")
for i in range(midi_in.get_port_count()):
    print(f"{i}: {midi_in.get_port_name(i)}")

# List available MIDI output ports
print("\nAvailable MIDI output ports:")
for i in range(midi_out.get_port_count()):
    print(f"{i}: {midi_out.get_port_name(i)}")

# Close the MIDI input and output instances
midi_in.close_port()
midi_out.close_port()
