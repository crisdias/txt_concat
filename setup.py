from setuptools import setup, find_packages

setup(
    name="txtconcat",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'txtconcat=txtconcat.main:main',
        ],
    },
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    description="Uma ferramenta para concatenar arquivos TXT",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/txtconcat",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
