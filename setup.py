from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'wsol',
    version = '3.0.2',
    author = 'NEO',
    author_email = 'neo89ucsc@gmail.com',
    description = 'This custom tool provide basic support to WSOL kubeCtl',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/source369/wsolkube',
    py_modules = ['wsol', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=2.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        wsol=wsol:init
      '''
)
