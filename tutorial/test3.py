import jack

# Create a new JACK client
client = jack.Client('MyAudioApp')

# Register audio input and output ports
input_port = client.inports.register('input_1')
output_port = client.outports.register('output_1')

# Activate the client
client.activate()

# Connect the input port to the output port
client.connect(input_port, output_port)

# Your application logic here

# Deactivate and close the client when done
client.deactivate()
client.close()
