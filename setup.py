from setuptools import setup

setup(
    name="dupgee",
    version="0.2",
    packages=["dupgee", "dupgee.base", "dupgee.base.dupgee"],
    url="https://github.com/ahmetkotan/dupgee",
    license="",
    author="ahmetkotan",
    author_email="ahmtkotan@gmail.com",
    description="Mini Web Framework on MicroPython (Esp8266)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["dupgee = dupgee.manage:execute"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: Implementation :: MicroPython",
    ],
)
