import mido

print(mido.get_input_names())
print(mido.get_output_names())


# Create a MIDI input port
inport = mido.open_input('Midi Through Port-2')

# Create a MIDI output port
# outport = mido.open_output('Midi Through Port-1') # Use the correct output port name for your system

# Loop to continuously listen for MIDI messages
try:
    while True:
        for msg in inport.iter_pending():
            print(msg)
            # Check if the message is a 'note_on' message
            # if msg.type == 'note_on':
            #     # Send the received 'note_on' message to the output port
            #     outport.send(msg)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    inport.close()
    # outport.close()
