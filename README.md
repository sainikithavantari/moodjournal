# Mood Journal Application

## Overview
The Mood Journal Application is a simple web-based tool that allows users to track their moods and thoughts over time. Built with Flask (a Python web framework) and SQLite (a lightweight database), this application enables users to add mood entries, view past entries, and analyze mood trends.

## Features
- **Add Mood Entries**: Users can log their mood and add a note describing their feelings.
- **View Past Entries**: Users can view all past mood entries in chronological order.
- **Mood Trend Analysis**: Users can visualize their mood trends over time using a simple graph.
- **Lightweight and Easy to Use**: The application is simple, intuitive, and requires minimal setup.

## Requirements
- Python 3.x
- Flask (`flask`)
- SQLite3 (comes pre-installed with Python)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mood-journal.git
   cd mood-journal
   ```

2. Install the required dependencies:
   ```bash
   pip install flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage
1. **Home Page**: The home page provides an interface to add a new mood entry.
2. **Add Entry**: Enter your mood (e.g., "Happy", "Sad", "Neutral") and a note describing your feelings. Click "Add Entry" to save.
3. **View Entries**: Navigate to the "View Entries" section to see all past mood entries sorted by date.
4. **Mood Trend**: Check the "Mood Trend" section to visualize your mood trends over time.

## Directory Structure
```
mood-journal/
│
├── app.py                  # Main application script
├── mood_journal.db         # SQLite database file
├── templates/              # HTML templates
│   └── index.html          # Home page template
└── README.md               # Project documentation
```

## API Endpoints
- **GET `/`**: Renders the home page.
- **GET `/entries`**: Returns a JSON list of all mood entries.
- **POST `/add-entry`**: Adds a new mood entry to the database.
- **GET `/mood-trend`**: Returns mood trend data (dates and moods) for visualization.

## Example JSON Responses
- **GET `/entries`**:
  ```json
  [
    {"date": "2023-10-01", "mood": "Happy", "note": "Had a great day!"},
    {"date": "2023-10-02", "mood": "Sad", "note": "Feeling a bit down today."}
  ]
  ```

- **GET `/mood-trend`**:
  ```json
  {
    "dates": ["2023-10-01", "2023-10-02"],
    "moods": ["Happy", "Sad"]
  }
  ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [SQLite](https://www.sqlite.org/) for the lightweight database.

## Contact
For any questions or feedback, please contact [Mail](mailto:sainikithavantari@gmail.com).
