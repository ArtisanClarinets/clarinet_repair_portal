# /apps/clarinet_repair_portal/setup.py
from setuptools import setup, find_packages

setup(
    name='clarinet_repair_portal',
    version='0.0.1',
    description='Clarinet Repair Portal',
    author='Dylan Thompson',
    author_email='dylan@example.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe'],
)
