from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='langchain-demo',
    version='0.1',
    packages=find_packages(),
    install_requires=required,  # Use the list from requirements.txt here
    author='Santosh KV',
    author_email='gyannetics@gmail.com',
    description='A short description of your project',
    license='MIT',
    url='https://github.com/gyannetics/llm-end-to-end',
    # More metadata
)
