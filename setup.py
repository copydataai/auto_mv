from setuptools import setup, find_packages

setup(
    name='auto_mv',
    version='0.1.0',
    author='copydataai',
    packages=find_packages(),
    include_package_data=True,
    author_email='copydataai@gmail.com',
    license='MIT',
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'aumv=auto_mv.scripts.auto_mv:auto_mv',
            'auto=auto_mv.scripts.auto_mv:auto_mv',
        ]
    },
    python_requires='>=3.6',
    project_repo='https://github.com/copydataai/auto_mv'
)
