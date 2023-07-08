import wave
import numpy as np
import threading
import time
from dataclasses import dataclass, asdict
import easygui
import pyaudio
from cli_interface import get_input_path_from_cli


@dataclass
class StreamParams:
    format: int = pyaudio.paInt16
    channels: int = 2
    rate: int = 44100
    frames_per_buffer: int = 1024
    input: bool = True
    output: bool = True

    def to_dict(self) -> dict:
        return asdict(self)


class Recorder:
    MIN_RECORDING_TIME = 5  # seconds
    MAX_RECORDING_TIME = 60  # seconds

    def __init__(self, stream_params: StreamParams) -> None:
        self.stream_params = stream_params
        self.is_recording = threading.Event()
        self.start_time = None
        self.stop_time = None
        self._pyaudio = None
        self._input_stream = None
        self._output_stream = None
        self._wav_file = None

    def start_recording(self, save_path: str) -> None:
        try:
            print("Start recording...")
            self.is_recording.set()
            self.start_time = time.time()
            self._create_audio_stream()
            self._create_wav_file(save_path)
            threading.Thread(target=self._write_wav_file_reading_from_stream_and_playback).start()
            threading.Timer(self.MAX_RECORDING_TIME, self.stop_recording).start()
        except Exception as e:
            print(f"Failed to start recording: {e}")

    def stop_recording(self) -> None:
        try:
            self.stop_time = time.time()
            elapsed_time = self.stop_time - self.start_time
            if elapsed_time < self.MIN_RECORDING_TIME:
                time.sleep(self.MIN_RECORDING_TIME - elapsed_time)
            print("Stop recording")
            self.is_recording.clear()
            self._close_recording_resources()
            print(f"Recording duration: {time.time() - self.start_time} seconds")
        except Exception as e:
            print(f"Failed to stop recording: {e}")

    def _create_audio_stream(self) -> None:
        self._pyaudio = pyaudio.PyAudio()
        self._input_stream = self._pyaudio.open(**self.stream_params.to_dict())
        self._output_stream = self._pyaudio.open(**self.stream_params.to_dict())

    def _create_wav_file(self, save_path: str) -> None:
        self._wav_file = wave.open(save_path, "wb")
        self._wav_file.setnchannels(self.stream_params.channels)
        self._wav_file.setsampwidth(self._pyaudio.get_sample_size(self.stream_params.format))
        self._wav_file.setframerate(self.stream_params.rate)

    def _write_wav_file_reading_from_stream_and_playback(self) -> None:
        while self.is_recording.is_set():
            audio_data = self._input_stream.read(self.stream_params.frames_per_buffer)
            amplified_audio_data = np.frombuffer(audio_data, dtype=np.int16) * 2

            self._output_stream.write(amplified_audio_data.tobytes())
            self._wav_file.writeframes(amplified_audio_data.tobytes())

    def _close_recording_resources(self) -> None:
        self._input_stream.close()
        self._output_stream.close()
        self._pyaudio.terminate()


if __name__ == "__main__":
    path = get_input_path_from_cli()
    stream_params = StreamParams()
    recorder = Recorder(stream_params)
    while True:
        button = easygui.buttonbox("Click on the buttons", choices=["Start", "Stop"])
        if button == "Start":
            recorder.start_recording(str(path))
        elif button == "Stop":
            recorder.stop_recording()
        else:
            break



