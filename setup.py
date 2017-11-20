from setuptools import setup

setup(
   name='bull-and-bear-api',
   version='1.0',
   description='Predict share value',
   author='siddharth kala',
   author_email='siddharth.kala1989@gmail.com',
   packages=['bull-and-bear-api'],  #same as name
   install_requires=['nsetools','requests','TA-Lib','lxml','beautifulsoup4','numpy','scipy','pandas','nsepy'], #external packages as dependencies
)