from setuptools import setup, find_packages

setup(
    name="videonoise",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "videonoise=videonoise.videonoise:main",
        ],
    },
    install_requires=[
        "numpy",
        "pydub",
        "moviepy",
    ],
    python_requires=">=3.6",
)
