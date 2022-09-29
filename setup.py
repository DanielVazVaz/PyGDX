from setuptools import setup

with open("README.md", "r", encoding="utf8", errors='ignore') as fh:
    long_description = fh.read()

setup(name='pygdx',
      version='0.1.0',
      description='Read GDX information to Python through GAMS Python API',
      url='https://github.com/DanielVazVaz/PyGDX',
      author='Daniel Vázquez Vázquez',
      author_email='daniel.vazquez.vazquez@chem.ethz.ch',
      license='MIT',
      packages=['pygdx'],
      install_requires=['pandas>=1.4.1'],
      extras_require = {
          "dev": [
              "build",
              "twine",
              "sphinx",
              "sphinx_rtd_theme",
              "check-manifest",
          ],
      },
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
              'Development Status :: 2 - Pre-Alpha',
              'License :: OSI Approved :: MIT License',
              'Programming Language :: Python :: 3 :: Only',
              'Topic :: Scientific/Engineering',
              'Topic :: Scientific/Engineering :: Mathematics'
          ],
)