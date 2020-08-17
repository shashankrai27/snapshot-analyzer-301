from setuptools import setup

setup(
name='snapshot-analyzer-301',
version = '0.1',
author = "Shashank Rai",
author_email = "rai.shashank@gmail.com",
description ="snapshot analyzer 301 is a tool to manage AWS EC2 volume snapshots",
license ="GPLv3+",
packages=['shotty'],
url="https://github.com/shashankrai27/snapshot-analyzer-301",
install_requires=[
    'click',
    'boto3'
],
entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
    ''',
)
