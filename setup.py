"""
Setup script for the langchain-demo package.
"""

from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt', encoding='utf-8') as f:
    required = f.read().splitlines()

setup(
    name='langchain-demo',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
    author='Santosh KV',
    author_email='gyannetics@gmail.com',
    description='A short description of your project',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/gyannetics/llm-end-to-end',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        # Additional classifiers as needed
    ],
    keywords='chatbot, langchain, openai',  # Add more relevant keywords
    # include_package_data=True,
    # package_data={...},
    # More metadata as needed
)
