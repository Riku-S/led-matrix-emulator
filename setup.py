import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

with open("requirements.txt", 'r') as f:
    requires = f.read().split()

setuptools.setup(
    name='pynq_emulator',
    version='1.3',
    author='Riku Salminen',
    author_email='riku.salminen@tuni.fi',
    description="An emulator for TUNI students' PYNQ exercises",
    packages=setuptools.find_packages(),
    scripts=[],
    url="https://github.com/Riku-S/led-matrix",
    download_url="https://github.com/Riku-S/led-matrix/archive/master.zip",
	
    classifiers = [
                  'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.5',
                  'Programming Language :: Python :: 3.6',
                  'Programming Language :: Python :: 3.7',
              ],
    python_requires='>=3.6',
)