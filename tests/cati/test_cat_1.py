import pytest
from unittest.mock import patch
def test_cat_corr():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_d,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom,\
        patch('os.path.isfile') as m_f,patch('builtins.open') as m_o:
        mto_correct.return_value = '/ll/fie.txt'
        m_d.return_value=0
        m_f.return_value=1
        m_exists=1
        m_o.return_value.__enter__.return_value = ['line1\n', 'line2\n']
        from src.cat import catti
        catti('/ll/fie.txt')
        mto_correct.assert_called_once_with('/ll/fie.txt')
        m_o.assert_called_once_with('/ll/fie.txt','r')
        m_print.assert_any_call('line1\n')
        m_print.assert_any_call('line2\n')
        m_logcom('cat /ll/fie.txt',1,'')
