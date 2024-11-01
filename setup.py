from setuptools import setup, find_packages

setup(
    name="tabs2music",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "midi2audio==0.1.1",
        "MIDIUtil==1.2.1",
    ],
    author="Yusef Ahmed",
    description="Converts guitar tabs (.txt) into audio (.wav)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"
)