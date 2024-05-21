#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""
import sys
import os
import unittest
from http.server import HTTPServer, SimpleHTTPRequestHandler

def main():
    """Run administrative tasks."""
    if len(sys.argv) < 2:
        print("Usage: script.py <command> [options]")
        sys.exit(1)
    
    command = sys.argv[1]

    if command == 'runserver':
        run_server()
    elif command == 'test':
        run_tests()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: runserver, runtests")
        sys.exit(1)

def run_server():
    """Start the HTTP server."""
    port = 8000  # Default port
    if len(sys.argv) > 2:
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Error: Port number must be an integer.")
            print("Usage: script.py runserver [port]")
            sys.exit(1)

    handler = SimpleHTTPRequestHandler
    httpd = HTTPServer(('0.0.0.0', port), handler)
    print(f"Serving HTTP on 0.0.0.0 port {port} (http://0.0.0.0:{port}/) ...")
    httpd.serve_forever()

def run_tests():
    """Run unit tests."""
    tests_dir = 'tests'  # Directory where your test files are located
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=tests_dir)

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    if not result.wasSuccessful():
        sys.exit(1)

if __name__ == '__main__':
    main()
