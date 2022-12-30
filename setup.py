import os
from setuptools import setup


lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = []

# Obtain list of requirements
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

# Obtain readme text for long description
with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name='wrapper-rabbitmq-client',
    version='0.0.3',
    license='MIT License',
    author='Tatianno Alves',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='tferreiraalves@gmail.com',
    keywords='asterisk ami rabbitmq producer',
    description=u'Wrapper for RabbitMQ client',
    packages=['wrapper_rabbitmq_client'],
    install_requires=install_requires,
)