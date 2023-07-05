# Recorder echo

This is a project for a audio recorder with a specific frequency filter. The recorder can capture sounds from a range of frequencies defined by the user. For instance, if you set the frequency range to 20 to 50 Hz, the recorder will only pick up sounds within that range.

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
