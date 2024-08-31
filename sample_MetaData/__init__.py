 
#IMPORT REQ LIBRARY
import sys
import time

# CREATING CLASS WITH NAMED RESUME
class Resume:
    def __init__(self):
        # Initialize the resume data
        self.data = {
            "name": "Ankit Kumar",
            "contact": {
                "email": "ankit127iitp@gmail.com",
                "phone": "",
                "github": "https://github.com/ankit485803/",
                "website": "",
                "linkedin": "https://www.linkedin.com/in/ankit127iitp/"
            },
            "education": [
                {
                    "institution": "Indian Institute of Technology (IIT), Patna",
                    "degree": "Bachelor's in Computer Science and Data Analytics",
                    "dates": "May 2023 to Aug 2027"
                },
            ],
            "coursework": [
                "Data Structures & Algorithms",
                "Computer Networks",
            ],
            "skills": {
                "languages": ["Python", "JavaScript"],
                "tools": ["Git/GitHub", "VS Code"],
            },
            "projects": [
                {
                    "name": "ChatCoder’s Haven: A Features Rich, Multilingual Compiler with Integrated Chatbot",
                    "technologies": ["HTML", "CSS", "JS"],
                    "date": "Nov 2023",
                    "description": [
                        "Web-based application for online coding that supports Python, C++, and Java, with dark themes and integrated AI-powered chatbot functionality to assist with coding.",
                    ]
                },
            ],
            "experience": [
                {
                    "role": "Research Intern",
                    "organization": "Indian Institute of Information Technology, Guwahati",
                    "dates": "May - July 2024",
                    "description": "Developed forecasting models for stock market (Finance Eco) using advanced machine learning and deep learning techniques, including ANN, CNN, RNN, LSTM, Transformer, and KNN to analyze and interpret time series data patterns. Dataset used – Yahoo Finance (TCS last 22 years). Worked with software: STATA, EViews."
                }
            ],
            "achievements": [
                "Lead Coding (Tech) Clubs | Indian Institute of Technology, Patna",
                "Gold Badge in Daily Streak & Bronze for Problem Solver | CodeChef"
            ]
        }

    def get_resume_data(self):
        # Return the resume data
        return self.data



# Function to print text slowly with a typewriter effect
def print_slow(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)



# Function to display resume data in the command line
def display_resume_cli():
    resume = Resume()  # Create an instance of Resume
    resume_data = resume.get_resume_data()  # Get resume data

    print("\n")
    print_slow("\033[1;32m" + resume_data['name'].center(50) + "\n")  # Print the name in green and centered
    print("\033[0m")

    # Print contact information
    print_slow("\n\033[1;36mContact Information\033[0m\n")
    for key, value in resume_data['contact'].items():
        print_slow(f"  \033[1;34m- {key.capitalize()}:\033[0m {value}\n")
    print("\n")

    # Print education information
    print_slow("\033[1;36mEducation\033[0m\n")
    for edu in resume_data['education']:
        print_slow(f"  \033[1;34m- {edu['degree']} in {edu['institution']} ({edu['dates']})\033[0m\n")
    print("\n")

    # Print coursework
    print_slow("\033[1;36mCoursework\033[0m\n")
    for course in resume_data['coursework']:
        print_slow(f"  \033[1;34m- {course}\033[0m\n")
    print("\n")

    # Print skills
    print_slow("\033[1;36mSkills\033[0m\n")
    for skill_type, skill_list in resume_data['skills'].items():
        print_slow(f"  \033[1;34m * {skill_type.capitalize()}:\033[0m\n")
        for skill in skill_list:
            print_slow(f"    \033[1;34m- {skill}\033[0m\n")
    print("\n")

    # Print projects
    print_slow("\033[1;36mProjects\033[0m\n")
    for project in resume_data['projects']:
        print_slow(f"  \033[1;34m * {project['name']} ({project['date']})\033[0m\n")
        for desc in project['description']:
            print_slow(f"    \033[1;34m- {desc}\033[0m\n")
    print("\n")

    # Print experience
    print_slow("\033[1;36mExperience\033[0m\n")
    for exp in resume_data['experience']:
        print_slow(f"  \033[1;34m * {exp['role']}, {exp['organization']} ({exp['dates']})\033[0m\n")
        print_slow(f"    \033[1;34m- {exp['description']}\033[0m\n")
    print("\n")

    # Print achievements
    print_slow("\033[1;36mAchievements\033[0m\n")
    for achievement in resume_data['achievements']:
        print_slow(f"  \033[1;34m- {achievement}\033[0m\n")

# Final block to execute the script
if __name__ == "__main__":
    display_resume_cli()


