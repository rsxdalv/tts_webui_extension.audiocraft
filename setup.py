import setuptools

setuptools.setup(
    name="extension_audiocraft",
    packages=setuptools.find_namespace_packages(),
    version="0.0.2",
    author="rsxdalv",
    description="Audiocraft provides MusicGen and MAGNeT models for high-quality music and audio generation",
    url="https://github.com/rsxdalv/extension_audiocraft",
    project_urls={},
    scripts=[],
    install_requires=[
        "audiocraft @ https://github.com/rsxdalv/audiocraft/releases/download/v1.4.0a1/audiocraft-1.4.0a1-py3-none-any.whl",
        "spacy>=3.7.6",
        "numpy<2", # higher numpy likely works but breaks other packages
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
