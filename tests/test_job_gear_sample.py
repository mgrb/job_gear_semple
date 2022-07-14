"""
Tests of main module.
"""
from job_gear_sample import __version__

def test_version():
    """
    Test of version.
    """
    assert __version__ == '0.1.0'
