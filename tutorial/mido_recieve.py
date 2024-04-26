import mido

print(mido.get_input_names())

# Create a MIDI input port
inport = mido.open_input('Midi Through Port-2')

# Loop to continuously listen for MIDI messages
try:
    while True:
        for msg in inport.iter_pending():
            print(msg)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    inport.close()
