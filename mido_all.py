import mido
from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file
mid = MidiFile()

# Create a new MIDI track
track = MidiTrack()
mid.tracks.append(track)

# Add a note on message
track.append(Message('note_on', note=60, velocity=64, time=0))

# Add a note off message
track.append(Message('note_off', note=60, velocity=127, time=100))

# Save the MIDI file
mid.save('new_song.mid')

# Play the MIDI file
mid.play()
