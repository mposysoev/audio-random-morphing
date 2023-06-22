import torch
import torchaudio

def calculate_average_sound(segment1, segment2):
    # Load the audio segments
    audio1, _ = torchaudio.load(segment1, normalize=True)
    audio2, _ = torchaudio.load(segment2, normalize=True)


    # Make sure the audio segments have the same length
    duration = min(audio1.size(1), audio2.size(1))
    audio1 = audio1[:, :duration]
    audio2 = audio2[:, :duration]

    # Calculate the average sound
    average_sound = (audio1 + audio2) / 2

    return average_sound


# Provide the paths to your audio segments
segment1_path = "2.wav"
segment2_path = "4.wav"

# Calculate the average sound
average_sound = calculate_average_sound(segment1_path, segment2_path)

# Save the average sound to a file
torchaudio.save(
    f"average_sound_of{segment1_path}{segment2_path}.wav",
    average_sound,
    sample_rate=48000,
)
