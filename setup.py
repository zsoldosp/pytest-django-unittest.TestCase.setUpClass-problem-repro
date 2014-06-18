from setuptools import setup, find_packages

setup_kwargs = dict(
    name="sampleapp",
    packages=find_packages(),
)

if __name__ == '__main__':
    setup(**setup_kwargs)

