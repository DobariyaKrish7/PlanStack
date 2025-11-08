# PlanStack App

A beautiful and modern todo application built with Python Flask, featuring a responsive design and full CRUD functionality.

## Features

- ✨ **Modern UI Design** - Beautiful gradient backgrounds and smooth animations
- 📱 **Responsive Layout** - Works perfectly on desktop, tablet, and mobile devices
- ✅ **Full CRUD Operations** - Create, Read, Update, and Delete todos
- 🎯 **Priority Management** - Set low, medium, or high priority for tasks
- 📅 **Due Date Support** - Add due dates to your todos
- 🔄 **Status Toggle** - Mark todos as complete or incomplete
- 💾 **SQLite Database** - Persistent storage with automatic database creation
- 🎨 **Beautiful Icons** - Font Awesome icons for enhanced visual appeal

## Screenshots

The application features a modern design with:
- Gradient header with task management icon
- Clean form for adding new todos
- Beautiful todo cards with priority indicators
- Responsive buttons for all actions
- Smooth hover effects and animations

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project files**
   ```bash
   # If you have git installed
   git clone <repository-url>
   cd flask-todo-app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000` to see your todo app!

## Usage

### Adding a Todo
1. Fill in the task title (required)
2. Add an optional description
3. Select priority level (low, medium, high)
4. Set an optional due date
5. Click "Add Todo"

### Managing Todos
- **Complete/Incomplete**: Click the checkmark button to toggle status
- **Edit**: Click the edit button to modify todo details
- **Delete**: Click the trash button to remove a todo (with confirmation)

### Features
- **Priority Colors**: High (red), Medium (orange), Low (green)
- **Status Indicators**: Completed todos show with strikethrough text
- **Date Display**: Shows creation date and due date if set
- **Responsive Design**: Automatically adapts to different screen sizes

## Project Structure

```
flask-todo-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── templates/         # HTML templates
│   ├── index.html     # Main page with todo list
│   └── edit.html      # Edit todo form
└── todos.db           # SQLite database (created automatically)
```

## Database Schema

The application uses SQLite with the following Todo model:

- `id`: Unique identifier (auto-increment)
- `title`: Todo title (required)
- `description`: Optional detailed description
- `completed`: Boolean status (default: False)
- `priority`: Priority level (low/medium/high)
- `created_at`: Timestamp when todo was created
- `due_date`: Optional due date

## Customization

### Changing the Theme
Modify the CSS variables in the HTML templates to change colors:
- Primary gradient: `#667eea` to `#764ba2`
- Success color: `#28a745`
- Danger color: `#dc3545`
- Secondary color: `#6c757d`

### Adding New Features
The modular Flask structure makes it easy to add new features:
- New routes in `app.py`
- Additional form fields in templates
- Enhanced database models

## Troubleshooting

### Common Issues

1. **Port already in use**
   - Change the port in `app.py`: `app.run(debug=True, port=5001)`

2. **Database errors**
   - Delete `todos.db` and restart the app to recreate the database

3. **Import errors**
   - Ensure you're in the correct directory
   - Verify virtual environment is activated
   - Check that all requirements are installed

### Error Messages
- **"No module named 'flask'"**: Install requirements with `pip install -r requirements.txt`
- **"Address already in use"**: Change port or stop other services using port 5000
- **"Database locked"**: Close other applications that might be accessing the database

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the Flask documentation
3. Check Python and package versions compatibility

---

**Happy Todo-ing! 🎉**
