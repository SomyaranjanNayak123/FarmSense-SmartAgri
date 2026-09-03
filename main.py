"""
Smart Agriculture System - Entry Point
Run backend: uvicorn backend.server:app --reload
Run frontend: streamlit run frontend/app.py
"""
import subprocess
import sys

def main():
    print("Smart Agriculture System")
    print("1. Start Backend  -> uvicorn backend.server:app --reload --port 8000")
    print("2. Start Frontend -> streamlit run frontend/app.py")

if __name__ == "__main__":
    main()
