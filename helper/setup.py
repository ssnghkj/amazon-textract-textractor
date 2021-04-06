import os
import sys
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = [
    'boto3', 'botocore', 'amazon-textract-response-parser', 'amazon-textract-caller', 'amazon-textract-overlayer',
    'amazon-textract-prettyprinter', 'Pillow==8.1.2', 'PyPDF2==1.26.0'
]

if sys.argv[-1] == 'publish-test':
    os.system(f"cd {os.path.dirname(__file__)}")
    os.system('rm dist/*')
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine check dist/*')
    os.system('twine upload --repository pypitest dist/*')
    sys.exit()

if sys.argv[-1] == 'publish':
    os.system(f"cd {os.path.dirname(__file__)}")
    os.system('rm dist/*')
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine check dist/*')
    os.system('twine upload --repository pypi dist/*')
    sys.exit()

setup(name='amazon-textract-helper',
      packages=['textracthelper'],
      include_package_data=True,
      version='0.0.11',
      description='Amazon Textract Helper tools',
      install_requires=requirements,
      scripts=['bin/amazon-textract'],
      long_description_content_type='text/markdown',
      long_description=read('README.md'),
      author='Amazon Rekognition Textract Demoes',
      author_email='rekognition-textract-demos@amazon.com',
      url='https://github.com/aws-samples/amazon-textract-textractor',
      keywords='amazon-textract-textractor amazon textract textractor helper',
      license="Apache License Version 2.0",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Utilities",
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      python_requires='>=3.6')
