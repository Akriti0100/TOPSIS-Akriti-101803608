from setuptools import setup

setup(
    name="TOPSIS-Akriti-101803608",
    packages=["TOPSIS-Akriti-101803608"],
    version="1.0.0",
    license="MIT",
    description="A Python package to get best alternative available using TOPSIS method.",
    author="Akriti Singhal",
    author_email="akritisinghal1663@gmail.com",
    url="https://github.com/Akriti0100/TOPSIS-Akriti-101803608",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["pandas"],
    entry_points={
        "console_scripts": [
            "TOPSIS-Akriti-101803608=TOPSIS_Akriti_101803608.topsis:main",
        ]
    },
)