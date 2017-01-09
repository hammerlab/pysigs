try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.0.1"

setup(
    name="pysigs",
    version=version,
    author="Tim O'Donnell",
    author_email="timodonnell@gmail.com",
    packages=["pysigs"],
    url="https://github.com/hammerlab/pysigs",
    license="Apache License",
    description="Mutational signature deconvolution onto known signatures",
    long_description=open('README.rst').read(),
    download_url='https://github.com/hammerlab/pysigs/tarball/%s' % version,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
    ],
    entry_points={
        'console_scripts': [
        ]
    },
    install_requires=[
        "six",
        "nose>=1.3.1",
    ]
)
