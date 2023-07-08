import os
import time
import unittest
from main import Recorder, StreamParams


class TestRecorder(unittest.TestCase):
    def setUp(self):
        self.recorder = Recorder(StreamParams())
        self.test_file_path = 'test.wav'

    def tearDown(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_start_recording_success(self):
        self.recorder.start_recording(self.test_file_path)
        self.assertTrue(self.recorder.is_recording.is_set())

    def test_stop_recording_success(self):
        self.recorder.start_recording(self.test_file_path)
        time.sleep(5)
        self.recorder.stop_recording()
        self.assertFalse(self.recorder.is_recording.is_set())

    def test_recording_duration_correct(self):
        self.recorder.start_recording(self.test_file_path)
        time.sleep(5)
        self.recorder.stop_recording()
        duration = self.recorder.stop_time - self.recorder.start_time
        self.assertGreaterEqual(duration, self.recorder.MIN_RECORDING_TIME)
        self.assertLessEqual(duration, self.recorder.MAX_RECORDING_TIME)

    def test_wav_file_created_successfully(self):
        self.recorder.start_recording(self.test_file_path)
        time.sleep(5)
        self.recorder.stop_recording()
        self.assertTrue(os.path.exists(self.test_file_path))

    def test_recording_stops_after_MIN_RECORDING_TIME(self):
        self.recorder.start_recording(self.test_file_path)
        time.sleep(2)
        self.recorder.stop_recording()
        duration = self.recorder.stop_time - self.recorder.start_time
        self.assertGreaterEqual(duration, self.recorder.MIN_RECORDING_TIME)

    def test_recording_stops_after_MAX_RECORDING_TIME(self):
        self.recorder.start_recording(self.test_file_path)
        time.sleep(65)
        self.recorder.stop_recording()
        duration = self.recorder.stop_time - self.recorder.start_time
        self.assertLessEqual(duration, self.recorder.MAX_RECORDING_TIME)


if __name__ == "__main__":
    unittest.main()

