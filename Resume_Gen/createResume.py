import os
from docx import Document
from PyPDF2 import PdfReader  #for pdf viewer i.e. guidlinePDF
import shutil  # for copying files


# Function to modify the resume with user's input
def create_resume(name, education_12th, education_bachelor):
    # Load the template resume document
    template_path = 'Resume_Gen/Template_Resume_YourName.docx'  # Update this path with the actual template location
    doc = Document(template_path)

    # Export the updated resume
    doc_path = os.path.join(os.getcwd(), f"{name.replace(' ', '_')}_Resume.docx")
    doc.save(doc_path)


    # Load the guideline PDF
    guidelinePDF_path = 'Resume_Gen/Guidline_gen-cv-manager.pdf'
    guidelinePDF_copy_path = os.path.join(os.getcwd(), 'Guidline_gen-cv-manager.pdf')
    
    # Copy the guideline PDF to the current working directory
    try:
        shutil.copy(guidelinePDF_path, guidelinePDF_copy_path)
    except FileNotFoundError:
        print(f"File not found: {guidelinePDF_path}")
        guidelinePDF_copy_path = None

    print(f"Your Resume is created successfully! File saved as: {doc_path}")
    if guidelinePDF_copy_path:
        print(f"See the reference guidelines in: {guidelinePDF_copy_path}")




if __name__ == "__main__":
    # User Input
    name = input("Enter your name: ")

    education_bachelor = {
        "degree": input("Enter your bachelor's degree (e.g., Computer Science): "),
        "institution": input("Enter your bachelor's institution: "),
        "dates": input("Enter the year of graduate (e.g., 2028): ")
    }

    education_12th = {
        "institution": input("Enter your 12th school name: "),
        "grade": input("Enter your grade (e.g., A+): "),
        "dates": input("Enter the year of your 12th (e.g., March 2021 - March 2023): ")
    }
    


    # Call the function to create the resume
    create_resume(name, education_bachelor, education_12th)
