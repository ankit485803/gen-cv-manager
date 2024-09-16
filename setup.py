
from setuptools import setup, find_packages

import os
import codecs



#SUPPORTIVE DEVICES OPTIONS
# Define classifiers to categorize the package
CLASSIFIERS = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',

  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]


# Read the long description from a separate file (optional but recommended for readability)
with open('README.md', 'r', encoding='utf-8') as file:
    LONG = file.read()

# Define package details
VERSION = '0.0.2'
DESCRIPTION = 'gen-cv-manager` is a Python package designed to help students and professionals create and manage their Cover Letters (CVs) and Resumes with ease. This package provides a straightforward way to generate professional-looking CVs by filling in relevant details such as education, experience, skills, and projects.'
LONG_DESCRIPTION = LONG


# Setup configuration
setup(
  name = 'gen-cv-manager',
  version = VERSION,
  author = "Ankit Kumar",
  author_email = 'ankit127iitp@gmail.com',
  description = DESCRIPTION,

  long_description_content_type = "text/markdown",
  long_description = LONG_DESCRIPTION,

  # REQUIRED
    packages = find_packages(),     # Automatically discover packages
    install_requires = [],   # List external dependencies here if any


  license='MIT', 
  classifiers = CLASSIFIERS,
  keywords = ["Cover Letter", "CV", "Resume", "Resume Manager", "CV Building"], 
  url='https://github.com/ankit485803/gen-cv-manager',  # Homepage URL
  project_urls={
        'Documentation': 'https://github.com/ankit485803/gen-cv-manager/blob/main/README.md',
        'Source': 'https://github.com/ankit485803/gen-cv-manager',
    }, 
    
)

