# Recorder echo

This is a test task: this project performs microphone recording while simultaneously playing back on the output device. It also has a GUI interface for the start-stop command. If the stop button is pressed before 5 seconds, the program will continue recording until it reaches 5 seconds and then stop. The maximum recording duration is 60 seconds. Additionally, the audio will be saved locally to a file.

## Getting Started

These instructions will help you to get a copy of the project and run it on your local machine.

### Prerequisites

To run this project, you'll need to install the following:

You can install these using pip:

```bash
pip install pyproject.toml
```

### Installation

To use the recorder, you need to clone the project to your local machine. You can do this using the following command:

```bash
git clone https://github.com/MontyPython-ManuL/test_taskVoiceRec.git
```

### Usage

To start recording, run the script `main.py`. You'll be presented with a GUI with two buttons: "Start" and "Stop". Press "Start" to begin recording and "Stop" to end the recording. The recording will be saved as a WAV file in the project directory.

```bash
python main.py --path '/home/user/record.wav'
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
