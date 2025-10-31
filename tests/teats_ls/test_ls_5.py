import pytest
from unittest.mock import Mock, patch
def test_ls_path():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.listdir') as m_listdir,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom:
        mto_correct.return_value = '/neccor/path'
        m_exists.return_value = 0
        m_listdir.return_value = ['file1.txt','file2.cpp','file3.js','read.md']
        from src.ls import ls
        ls('/neccor/path', '')
        mto_correct.assert_called_once_with('/neccor/path')
        m_print.assert_called_once_with('ERROR: Данный путь не существует /neccor/path')
        arg=m_print.call_args[0][0]
        assert "ERROR:" in arg
        assert "Данный путь не существует /neccor/path" in arg
        m_logcom.assert_called_once_with('ls /neccor/path', 0, 'Данный путь не существует /neccor/path')