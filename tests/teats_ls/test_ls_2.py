import pytest
from unittest.mock import patch
def test_ls_path():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.listdir') as m_listdir,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom:
        mto_correct.return_value = '/ll/path'
        m_exists.return_value = 1
        m_listdir.return_value = ['file1.txt','file2.cpp','file3.js','read.md']
        from src.ls import ls
        ls('/ll/path', '')
        mto_correct.assert_called_once_with('/ll/path')
        m_print.assert_any_call('file1.txt')
        m_print.assert_any_call('file2.cpp')
        m_print.assert_any_call('file3.js')
        m_print.assert_any_call('read.md')
        m_logcom.assert_called_once_with('ls  /ll/path',1, '')