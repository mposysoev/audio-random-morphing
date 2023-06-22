from pydub import AudioSegment
import random


def read_audio_data(file_paths):
    audio_data = []
    for name in file_paths:
        audio = AudioSegment.from_mp3(name)
        audio_data.append(audio)

    return audio_data


def random_sampling(audio_data, duration, segment_len):
    result_audio = audio_data[0][0]
    num_of_iter = int(duration * 1000 / segment_len)
    for _ in range(num_of_iter):
        index = random.randint(0, len(audio_data) - 1)
        segment_start = random.randint(0, len(audio_data[index]) - 1 - segment_len)
        segment = audio_data[index][segment_start : segment_start + segment_len]
        result_audio = result_audio.append(segment, crossfade=1)

    return result_audio


def main():
    input_files = ["1.mp3", "2.mp3", "3.mp3", "4.mp3"]
    # input_files = ["4.mp3"]
    need_len = 30  # in seconds
    segment_len = 2000  # in miliseconds
    output_file = f"averaged_{segment_len}.wav"

    audio_data = read_audio_data(input_files)
    # print(f"{len(audio_data)=}")
    result1 = random_sampling(audio_data, need_len, segment_len)
    result1.export(output_file, format="wav")


if __name__ == "__main__":
    main()
