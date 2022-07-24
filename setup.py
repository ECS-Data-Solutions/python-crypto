import setuptools
import ecrypto

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="ecs-crypto",
    version=ecrypto.__version__,
    author="ECS Data Solutions",
    description="An ECS Data Solutions Driver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["ecrypto", "ecrypto.utils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=requirements,
)
