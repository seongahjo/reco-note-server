import io
import os

# Imports the Google Cloud client library
from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech_v1p1beta1 import enums
from google.cloud.speech_v1p1beta1 import types


def read(file_name, result_file):
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    file_name = os.path.join(
        os.path.dirname(__file__),
        file_name)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=2,
        sample_rate_hertz=44100,
        enable_speaker_diarization=True,
        diarization_speaker_count=2,
        language_code='ko-KR')

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        with io.open(result_file, 'w') as f:
            read_file_byte = 44100 * 2 * 50

            while True:
                content = audio_file.read(read_file_byte)
                if not content:
                    break
                audio = types.RecognitionAudio(content=content)
                response = client.recognize(config, audio)

                for result in response.results:
                    f.write(result.alternatives[0].transcript)
                    print(result.alternatives[0])
                    print('Transcript: {}'.format(result.alternatives[0].transcript))


if __name__ == "__main__":
    read('multi.wav','test.txt')
