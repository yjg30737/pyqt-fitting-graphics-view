from setuptools import setup, find_packages

setup(
    name='pyqt-fitting-graphics-view',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QGraphicsView which always fit the aspect ratio mode as Qt.KeepAspectRatio',
    url='https://github.com/yjg30737/pyqt-fitting-graphics-view.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-single-image-graphics-view @ git+https://git@github.com/yjg30737/pyqt-single-image-graphics-view.git@main'
    ]
)