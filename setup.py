from distutils.core import setup

setup(
    name='wkt2shp',
    version='0.0.1',
    author='Pete Gadomski',
    author_email='pete.gadomski@gmail.com',
    packages=[],
    scripts=['bin/wkt2shp'],
    url='https://github.com/gadomski/wkt2shp',
    license='LICENSE.txt',
    description='Convert polygons in well-known text to shapefiles',
    long_description=open('README.txt').read(),
    install_requires=[
        "Fiona == 1.0.2",
        "Shapely == 1.2.18",
    ],
)
