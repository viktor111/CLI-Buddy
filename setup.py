import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='CLI-Buddy',  

     version='0.1',

     scripts=['CLI-Buddy'] ,

     author="Viktor Draganov",

     author_email="swifrorlilko@gmail.com",

     description="Helper tool for making consoles",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/viktor111/CLI-Buddy.git",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
