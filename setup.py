"""Setup configuration for CadQuery."""

from setuptools import setup, find_packages
import re
import os


def get_version():
    """Read version from cadquery/__init__.py without importing the module."""
    version_file = os.path.join(os.path.dirname(__file__), "cadquery", "__init__.py")
    if not os.path.exists(version_file):
        return "0.0.1"
    with open(version_file, "r") as f:
        content = f.read()
    match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', content, re.MULTILINE)
    if match:
        return match.group(1)
    return "0.0.1"


def get_long_description():
    """Read the long description from README.md."""
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


setup(
    name="cadquery",
    version=get_version(),
    description="A parametric 3D CAD scripting framework based on OCCT",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="CadQuery Contributors",
    url="https://github.com/CadQuery/cadquery",
    license="Apache License 2.0",
    packages=find_packages(exclude=["tests", "tests.*", "doc", "doc.*"]),
    python_requires=">=3.8",
    install_requires=[
        "pyparsing>=2.1.0",
        "nptyping>=1.4.0",
        "typing_extensions>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black",
            "flake8",
            "mypy",
            "sphinx",
            "sphinx-rtd-theme",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
            "sphinx-autodoc-typehints",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=[
        "CAD",
        "3D",
        "parametric",
        "OCCT",
        "OpenCASCADE",
        "modeling",
        "geometry",
    ],
    project_urls={
        "Documentation": "https://cadquery.readthedocs.io",
        "Source": "https://github.com/CadQuery/cadquery",
        "Bug Tracker": "https://github.com/CadQuery/cadquery/issues",
    },
)
