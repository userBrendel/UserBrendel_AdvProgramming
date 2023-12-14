# WORKING WITH JSON FILE
import json #  module for working with JSON data.

# Function to write data to a JSON file
def write_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2) #  Writes the contents of the data dictionary to the opened JSON file

# Function to read data from a JSON file when data on json file
def read_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file) # Reads the JSON data from the opened file and converts it into a Python dictionary .
    return data

# Get user input and write to JSON file
student_data = {
    "Name": input("Enter student name: "),
    "ID": int(input("Enter student ID: ")),
    "course": input("Enter student course: ")
}

file_path = 'StudentJson.json' # File name
write_json(file_path, student_data) # using function to write

# Read and display individual values from the JSON file
read_data = read_json(file_path) # to read

print("\nDetails of the Student:")
print(f"\tName: {read_data['Name']}")
print(f"\tID: {read_data['ID']}")
print(f"\tcourse: {read_data['course']}")

# Appending and update CourseDetails
course_details = {
    "CourseDetails": {
        "Group": input("Enter student group: "),
        "Year": int(input("Enter student year: "))
    }
}

# Updating the existing data with new CourseDetails
read_data.update(course_details)
write_json(file_path, read_data)

# Displaying individual values with updated CourseDetails
print("\nDetails of the Student:")
print(f"\tName: {read_data['Name']}")
print(f"\tID: {read_data['ID']}")
print(f"\tcourse: {read_data['course']}")
print(f"\tGroup: {read_data['CourseDetails']['Group']}")
print(f"\tYear: {read_data['CourseDetails']['Year']}")

