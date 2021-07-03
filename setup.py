import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

requirements = [
    'aiofiles==0.7.0'
]

setup(
    author="Iced Chai",
    name="emojipy",
    description="Async wrapper for the EmojiGG api.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/NextChai/Emojigg",
    project_urls = {
        'Documentation': 'https://github.com/NextChai/Emojigg/wiki',
        'Report a Bug': 'https://github.com/NextChai/Emojigg/issues',
        "Contribute": 'https://github.com/NextChai/Emojigg/pulls'
    },
    version="0.0.2",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["emojigg"],
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "square=square.__main__:main",
        ]
    },
)   