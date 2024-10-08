

# gen-cv-manager

`gen-cv-manager` is a Python package designed to simplify the creation and management of Cover Letters (CVs) and Resumes. This tool is particularly useful for students and professionals who want to generate professional CVs and resumes by providing necessary details such as education, experience, skills, and projects.


## Installation

You can install `gen-cv-manager` using pip:

```bash
pip install gen-cv-manager
```

### Setup .env
```
!pip install python-docx
!pip install PyPDF2

import os
from docx import Document
from PyPDF2 import PdfReader  
import shutil   
```

## Use-Case

Here’s a quick example of how to use the `gen-cv-manager` package:

```python
!pip install gen-cv-manager==0.0.3

# Import the module
import gen_cv_manager as g

# Call the createResume function
from g.resumeGenerator import createResume

# Now you can use the createResume function
createResume()  

```



This will display your resume data in the command line. The package is designed for easy customization, and future versions will include additional features such as exporting to various formats and enhanced customization options.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these guidelines:

1. **Fork the Repository**: Create your own fork of the repository.
2. **Clone Your Fork**: Clone the forked repository to your local machine.
3. **Create a Branch**: Create a new branch for your changes.
4. **Make Changes**: Implement your changes or new features.
5. **Submit a Pull Request**: Push your changes to your fork and submit a pull request to the main repository.

Please ensure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please contact:

- **Author**: Ankit Kumar
- **Mail to**: [ankit127iitp@gmail.com](mailto:ankit127iitp@gmail.com)

