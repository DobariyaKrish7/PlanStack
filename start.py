#!/usr/bin/env python3
"""
Flask Todo App Startup Script
This script checks dependencies and starts the Flask application.
"""

import sys
import subprocess
import os

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required.")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_requirements():
    """Install required packages."""
    try:
        print("📦 Installing requirements...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements.")
        return False

def check_flask():
    """Check if Flask is available."""
    try:
        import flask
        print("✅ Flask is available")
        return True
    except ImportError:
        print("❌ Flask not found. Installing requirements...")
        return install_requirements()

def main():
    """Main startup function."""
    print("🚀 Starting Flask Todo App...")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check Flask
    if not check_flask():
        return
    
    print("\n🎯 Starting the application...")
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the application")
    print("=" * 40)
    
    # Start the Flask app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user.")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")

if __name__ == "__main__":
    main()
