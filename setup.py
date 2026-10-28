from setuptools import setup, find_packages

setup(
    name="azuracast-sse-client",  # Package name
    version="0.1.0",       # Initial version
    author="Joe McMahon",
    author_email="joe.mcmahon@example.com",
    description="Python SSE client for Azuracast",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/joemcmahon/azuracast-sse-client",  # Repo URL
    packages=find_packages(),
    install_requires=[
        "aiohappyeyeballs==2.4.4",
        "aiohttp==3.14.4",
        "aiosignal==1.3.2",
        "async-timeout==5.0.1",
        "attrs==24.3.0",
        "certifi==2026.10.18",
        "charset-normalizer==3.4.1",
        "discord.py==2.4.0",
        "discord-webhook==1.3.1",
        "frozenlist==1.5.0",
        "idna==3.10",
        "multidict==6.1.0",
        "pip==26.2",
        "propcache==0.2.1",
        "python-dotenv==1.0.1",
        "requests==2.33.0",
        "setuptools==84.1.0",
        "six==1.17.0",
        "sseclient-py==1.8.0",
        "typing_extensions==4.12.2",
        "tzlocal==5.2",
        "urllib3==2.8.0",
        "yarl==1.18.3",
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",  # Specify Python version compatibility
)

