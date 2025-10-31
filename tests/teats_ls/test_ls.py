import pytest
from unittest.mock import patch
def test_ls_bes_pyti():
    with patch('os.getcwd') as mgetcwd,patch('os.listdir') as mlistdir,patch('os.path.exists') as mexists, patch('builtins.print') as mprint, patch('src.loggining.logcom') as mlogcom:
        mgetcwd.return_value = ''
        mexists.return_value = 1
        mlistdir.return_value = ['file1.txt', 'file2.py', 'file3.txt']
        from src.ls import ls
        ls('', '') 
        mprint.assert_any_call('file1.txt')
        mprint.assert_any_call('file2.py')
        mprint.assert_any_call('file3.txt')
        mlogcom.assert_called_once_with('ls  ',1, '')

