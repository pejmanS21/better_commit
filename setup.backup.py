from setuptools import setup, find_packages

setup(
    name="simple sum",
    author='pejmans21',
    author_email='pejmans21@mail.com',
    url='https://github.com/pejmans21/better_commit/',
    version='0.0.2',
    description='sum two int',
    packages=find_packages(exclude=('tests*')),
    entry_points={
        'console_scripts': [
            'simsum = simple_sum.sum_function:sum_func'
        ]
    },
)
