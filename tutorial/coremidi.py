import mido
import rtmidi
import time


# Open a virtual MIDI output port

# List available output ports
print(mido.get_output_names())

# List available input ports
print(mido.get_input_names())

def send_note_on():
    midi_out = rtmidi.MidiOut()
    midi_out.open_virtual_port("RtMidiIn Client:RtMidi output 128:0")
    midi_out.send_message([0x90, 60, 127]) # Note on, middle C, velocity 127

    # with mido.open_output('RtMidiIn Client:RtMidi input 128:0') as outport:
    #     msg = mido.Message('note_on', note=60, velocity=64)
    #     outport.send(msg)

# List available output ports
print(mido.get_output_names())

# List available input ports
print(mido.get_input_names())


def receive_midi_messages():
    port_name = 'RtMidiIn Client:RtMidi input 128:0'
    while True:
        if port_name in mido.get_input_names():
            with mido.open_input(port_name) as inport:
                for msg in inport:
                    print(msg)
                    if msg.type == 'note_on':
                        break
            break
        else:
            print(f"Port {port_name} not available. Retrying...")
            time.sleep(1) # Wait for 1 second before checking again

# Call your function
receive_midi_messages()


# List available output ports
print(mido.get_output_names())

# List available input ports
print(mido.get_input_names())


# Send a MIDI Note On signal
send_note_on()
# List available output ports
print(mido.get_output_names())

# List available input ports
print(mido.get_input_names())

# Wait for a short period to ensure the Note On message is sent
import time
time.sleep(1)
# List available output ports
print(mido.get_output_names())

# List available input ports
print(mido.get_input_names())

# Receive MIDI messages
receive_midi_messages()
# List available output ports
print(mido.get_output_names())

# List available input ports
print(mido.get_input_names())