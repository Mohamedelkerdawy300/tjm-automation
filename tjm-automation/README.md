# TJM Automation

A vision-based desktop automation project using BotCity framework to automate Notepad tasks with data fetching capabilities.

## Description

This project demonstrates desktop automation using BotCity's vision-based framework. It:
- Fetches data from JSONPlaceholder API (with fallback data)
- Automatically launches and controls Notepad
- Writes fetched data to text files
- Saves files with automatic naming
- Includes robust error handling and firewall bypass

## Features

- **Vision-based automation**: Uses image recognition to locate and interact with desktop applications
- **Data fetching**: Retrieves data from external APIs with robust fallback mechanism
- **Automated file management**: Creates, saves, and organizes output files
- **Cross-platform support**: Works on Windows desktop environments

## Requirements

- Python >= 3.10
- BotCity Framework Core >= 0.6.0
- Requests >= 2.31.0
- OpenCV Python >= 4.8.0
- PyGetWindow >= 0.0.9

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tjm-automation.git
cd tjm-automation
```

2. Install dependencies using uv or pip:
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

## Usage

Run the main automation script:

```bash
python main.py
```

The script will:
1. Minimize all windows
2. Launch Notepad using vision-based icon detection
3. Fetch data for posts 1-10 from the API
4. Write each post to a separate text file in `~/Desktop/tjm-project/`
5. Close Notepad when complete

## Configuration

Edit the configuration section in `main.py`:

```python
PROJECT_DIR = os.path.join(os.path.expanduser("~"), "Desktop", "tjm-project")
API_BASE_URL = "http://jsonplaceholder.typicode.com/posts"
ICON_LABEL = "Notepad"
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
```

## Project Structure

```
tjm-automation/
├── main.py              # Main automation script
├── test_vision.py       # Vision testing utilities
├── pyproject.toml       # Project dependencies and metadata
└── README.md           # This file
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

