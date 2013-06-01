from distutils.core import setup
from glob import glob
import py2exe

data_files = [(".", ["ant.png", "leaf.png", "spider.png"])]

setup(
    windows = [{"script":"antsstatemachine.py"}],
    data_files = data_files,
    )