import torchaudio
import torch
import random
from pydub import AudioSegment
from tqdm import tqdm


def read_audio_files(file_paths):
    audio_data = []
    for file_path in file_paths:
        audio = AudioSegment.from_file(file_path)
        waveform = torch.Tensor(audio.get_array_of_samples())
        audio_data.append(waveform)
    return audio_data


def random_morph(audio_data, segment_length, total_len):
    result = torch.tensor([])
    total_segments = int(total_len)

    for _ in tqdm(range(total_segments)):
        index = random.randint(0, 3)
        chosen_sound = audio_data[index]
        segment_start = random.randint(0, len(chosen_sound) - segment_length)
        sample = chosen_sound[segment_start : segment_start + segment_length]
        sample = torch.unsqueeze(sample, dim=0)  # Convert to 2D tensor
        result = torch.cat((result, sample), dim=1)

    return result


def main():
    file_paths = ["1.mp3", "2.mp3", "3.mp3", "4.mp3"]
    audio_data = read_audio_files(file_paths)

    segment_length = 44100 * 4  # Adjust the desired length of each segment
    need_min = 60
    sample_rate = 44100
    total_len = need_min * sample_rate / segment_length

    result = random_morph(audio_data, segment_length, total_len)

    file_path = "output-2.wav"

    torchaudio.save(file_path, result, sample_rate)


if __name__ == "__main__":
    main()
