from setuptools import setup

setup(
    name="motd_ext",
    entry_points={
        "motd_messages": [
            "motd_messages = motd_ext:messages"
        ],
    }
)
