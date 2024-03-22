# Global constants and Enums
from enum import Enum

class Role(Enum):
    USER = 0
    ORGANIZER = 1

YEAR_CATEGORIES = ["1", "2", "3", "PEY", "4", "5", "Other"]
COURSE_CATEGORIES = ["Undergraduate", "Masters", "PhD", "Faculty"]
DEPARTMENT_CATEGORIES = [
    "Chemical Engineering", 
    "Civil Engineering", 
    "Electrical and Computer Engineering", 
    "Industrial Engineering", 
    "Materials Engineering",
    "Mechanical Engineering", 
    "Mineral Engineering", 
    "Engineering Science"
    ]
CAMPUS_CATEGORIES = [
    "St George",
    "Mississauga",
    "Scarborough"
]

EVENT_CATEGORIES = ["Ece", "Chemical", "Civil", "Mechanical", "Computer", "Materials", "Mineral", "Mining", "Engsci", "Indy", "Other"]
PROGRAM_CATEGORIES = ["ECE", "Chemical", "Civil", "Mechanical", "Computer", "Materials", "Mineral", "Mining", "EngSci", "Indy", "Other"]
# List of tags that can be used to sort the event data
# NOTE: Do not add a tag named "clear", since it has a special functionality
# --- prev filters: 
#FILTERS = ["In-Person", "Today", "Free", *EVENT_CATEGORIES, "Past Events"]
FILTERS = ["ECE", "Chemical", "Civil", "Mechanical", "Computer", "Materials", "Mineral", "Mining", "EngSci", "Indy", "Other"]

API_URL = "https://6klrlabk6g.execute-api.us-west-2.amazonaws.com/default/promptEn"
DB_NAME = "database.db"
USE_SIMPLE_SEARCH=True