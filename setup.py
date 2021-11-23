from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name="ezztui",
  version="1.0.0",
  scripts=["ezztui.py"],
  author="BarsTiger",
  description="Easy TextUI creating package",
  long_description=long_description,
  py_modules=["ezztui"]
)