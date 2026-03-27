"""
This is a high-quality README file for the api-service project.
"""

__copyright__ = "2023, Your Name"
__license__ = "MIT"
__author__ = "Your Name"
__email__ = "your_email@example.com"

def get_project_info():
    """
    Returns a dictionary containing the project information.
    """
    return {
        "title": "API Service",
        "description": "A RESTful API service built with Python.",
        "author": __author__,
        "email": __email__,
        "license": __license__
    }

def get_development_info():
    """
    Returns a list of dependencies required for development.
    """
    return ["poetry", "pytest", "pylint"]

def get_usage_info():
    """
    Returns a string with usage information for the API service.
    """
    return """
Usage:
  - Run the service with `poetry run python api_service.py`
  - Send a GET request to `http://localhost:8000/` to test the service
"""

if __name__ == "__main__":
    print("Project Information:")
    print(get_project_info())
    print("\nDevelopment Dependencies:")
    print(get_development_info())
    print("\nUsage Information:")
    print(get_usage_info())