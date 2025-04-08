from setuptools import setup, find_packages

setup(
    name="pipl-demo",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "colorama>=0.4.6",
    ],
    entry_points={
        'console_scripts': [
            'guess-number=pipl_demo.game:main',
        ],
    },
    author="Maksim Kotelnikov",
    author_email="maks.kotov38@gmail.com",
    description="Интерактивная консольная игра 'Угадай число'",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/1Sting1/pipl-demo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 