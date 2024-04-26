import mido

# Load a MIDI file
mid = mido.MidiFile('song.mid')

# Open a MIDI output port
# Replace 'Port Name' with the name of your MIDI output port
port = mido.open_output('Port Name')

# Play the MIDI file
for msg in mid.play():
    port.send(msg)

# Close the port
port.close()
