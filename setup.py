from setuptools import setup, find_packages

setup(
    name='ai-git',
    version='0.1.0',
    description='A CLI tool that uses an LLM to automatically generate semantic Git commits.',
    author='AI Assistant',
    packages=find_packages(),
    py_modules=[
        'main', 'cli', 'config', 'git_utils', 'diff_parser', 
        'llm_commit_generator', 'commit_classifier'
    ],
    install_requires=[
        'openai>=1.0.0',
        'PyYAML>=6.0',
        'python-dotenv>=1.0.0'
    ],
    entry_points={
        'console_scripts': [
            'ai-git=main:main',
        ],
    },
)
