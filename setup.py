import setuptools
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deepfake_voice_detection",
    version="0.1",
    author="desiCoders",
    author_email="rahilahmed1720@gmail.com",
    description="A package which will detect that the voice is real or deepfake.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rahilahmed20/deepfake_audio_detection",
    project_urls={
        "Bug Tracker": "https://github.com/rahilahmed20/deepfake_audio_detection/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires = [
        'Flask==3.0.2',
        'Flask_Cors==4.0.0',
        'keras==3.0.5',
        'librosa==0.10.1',
        'numpy==1.26.4',
        'tensorflow',
        'resampy'
    ]
)