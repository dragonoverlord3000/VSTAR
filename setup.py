from setuptools import setup

setup(
    name='VSTAR',
    version='0.1.0',    
    description='Auto refresh for Latex in VS-code',
    url='https://github.com/dragonoverlord3000/VSTAR.git',
    author='Dragonoverlord3000',
    author_email='hugomn2002@gmail.com',
    packages=['VSTAR'],
    install_requires=['selenium==3.141.0'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.8.1',
    ],

    entry_points = {
        'console_scripts': ['vstar=VSTAR.vstar:main'],
    },
)