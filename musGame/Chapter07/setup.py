from distutils.core import setup
import py2exe

setup(
      windows = [{"script":"antsstatemachine.py"}],
      data_files = [ (".", ["ant.png", "leaf.png", "spider.png"]) ]
)