
# VSTAR
```VSTAR = VS-code Tex Auto Restart``` is a minimal auto refresher tool for writing LaTeX in VS-code without having to manually refresh the page each time.

### Requirements
1. Python ::: 3
2. Selenium ::: 3.141.0
3. A Chrome webdriver that is compatible with your Chrome version
    - preferably located in '`C:\Program Files (x86)\chromedriver.exe`'

### How to use
1. Assuming that the requirements above have all been installed, just run `pip install VSTAR` - see '`https://pypi.org/project/VSTAR/0.1.0/`'
2. Then, in your latex project folder, create a `.tex` file and it's corresponding `.pdf` file (e.g. using `pdflatex ___.tex`)
3. Now, while in the project folder, run `vstar _____.tex`





