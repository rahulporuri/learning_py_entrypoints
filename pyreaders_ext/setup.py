from setuptools import setup

setup(
    name="pyreaders_ext",
    entry_points={
        "pyreader_types": [
            "pyreader_types = pyreaders_ext:file_types"
        ],
    }
)
