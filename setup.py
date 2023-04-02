from setuptools import setup, find_packages

setup(
    name='django_query_profiler',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Tool to Profile Django Queries',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Anton Polevanov',
    author_email='alulimmerkar@gmail.com',
    url='https://github.com/APolevanov/django-admin-filters',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'Django>=2.2',
    ],
)