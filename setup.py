from setuptools import setup, find_packages

setup(
    name='paysync',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='paysync.cc',
    author_email='paysync@paysync.cc',
    description='A package for interacting with paysync.cc API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/my_package',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
