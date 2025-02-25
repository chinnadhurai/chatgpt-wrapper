from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="chatGPT",
    version="0.1.0",
    author="Mahmoud Mabrouk",
    author_email="mahmoudmabrouk.mail@gmail.com",
    description="A simple Python class for interacting with OpenAI's chatGPT using Playwright",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openai/playwright-chatbot",
    packages=find_packages(),
    install_requires=[
        "playwright",
        "colorama",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "chatgpt = chatgpt_wrapper.chatgpt:main"
        ]
    },
    scripts=["postinstall.sh"],
)
