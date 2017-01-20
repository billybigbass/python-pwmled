from setuptools import setup, find_packages

setup(
    name='pwmled',
    version='1.0.0',
    description='Control LimitlessLED products.',
    url='https://github.com/soldag/python-pwmled/',
    license='MIT',
    author='soldag',
    author_email='soren.oldag@gmail.com',
    packages=find_packages(),
    install_requires=[
        'RPi.GPIO',
        'adafruit-pca9685'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)
