import pytest
from unittest.mock import patch,Mock
def test_ls_bes_pyti_fl():
    with patch('os.getcwd') as mgetcwd,patch('os.listdir') as mlistdir,patch('os.path.exists') as mexists, patch('builtins.print') as mprint, patch('src.loggining.logcom') as mlogcom,patch('os.stat') as m_st:
        mgetcwd.return_value = ''
        mexists.return_value = 1
        mlistdir.return_value = ['file1.txt']
        res = Mock()
        res.st_size = 8
        res.st_mode = 0o100
        res.st_mtime = 1967148852
        m_st.return_value = res
        from src.ls import ls
        ls('','-l')     
        mprint.assert_called_once()
        arg=mprint.call_args[0][0]
        assert 'file1.txt'in arg
        assert '8' in arg
        assert '100' in arg
        assert '2032-05-03' in arg
        mlogcom.assert_called_once_with('ls -l ',1, '')

