OS Windows 10 was used. Version 21H1.
Python version - Python 3.10.7.

You can clone the script from Github.

Then in the project folder you need to create a virtual environment. This requires the command:
python(3) -m venv <environment name>

Then you need to activate this:
source <environment name>/Scripts/activate

You can install all required packages from requirements.txt with command:
pip install -r requirements.txt

And you can run the script:
python pain.py

To exit the environment, enter the command:
deactivate.

The following modules were installed to create the requirements.txt:
1. 'google': 
pip install google-api-python-client
pip install google
2. 'kivy':
python -m pip install "kivy[base]" kivy_examples
3. 'Bio'
pip install biopython 
Biopython also contains 'numpy' module.
4. 'aiohttp'
pip install aiohttp
5. 'pandas'
pip install pandas
6. 'scipy'
pip install scipy
7. 'pip install'
pip install scanpy
8. 'cv2'
pip install opencv-python
9. 'lxml'
pip install lxml
10. 'typing'
pip install typing


