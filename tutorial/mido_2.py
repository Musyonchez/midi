import mido



with mido.open_output('Midi Through:Midi Through Port-0 14:0', virtual=True) as outport:
    outport.send(mido.Message('note_on', note=60, velocity=64))

for port in mido.get_input_names():
    print(port)

with mido.open_input() as inport:
    for msg in inport:
        print(msg)
