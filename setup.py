"""Setup"""
import setuptools

with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="pycfdnsv6",
    version="0.0.0",
    author="Joakim Sorensen",
    author_email="hi@ludeeus.dev",
    description="Update Cloudflare DNS A-records.",
    install_requires=["aiohttp>=3.6.1,<4.0", "async-timeout<4.0,>=3.0"],
    long_description=LONG,
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/pycfdns",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
