from setuptools import setup, find_packages

setup(
    name="personscope",
    version="1.0.0",
    author="Dudditz",
    description="An ethical OSINT tool for generating dorks and searching identities across multiple engines.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=["person_scope", "banner", "helptext", "dudditz_ascii"],
    install_requires=["rich"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "Topic :: Utilities",
        "Environment :: Console"
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "personscope=person_scope:main"
        ]
    },
)

