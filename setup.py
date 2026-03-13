from setuptools import setup, find_packages

setup(
    name='diffsense',
    version='0.1.0',
    description='A CLI tool that uses an LLM to automatically generate semantic Git commits.',
    author='AI Assistant',
    packages=find_packages(),
    install_requires=[
        'openai>=1.0.0',
        'PyYAML>=6.0',
        'python-dotenv>=1.0.0'
    ],
    entry_points={
        'console_scripts': [
            'diffsense=diffsense.cli:main',
        ],
    },
)
