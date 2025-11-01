import pytest
from unittest.mock import patch
def test_gr_corr():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_d,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom,\
        patch('os.path.isfile') as m_f,patch('builtins.open') as m_o:
        m_exists.return_value=1
        mto_correct.return_value = '/ll/fie.txt'
        m_d.return_value=0
        m_f.return_value=1
        m_o.return_value.__enter__.return_value = ['AAAAAA\n', 'BBBBBBB\n']
        from src.grep import grep
        grep('[a-z]*','/ll/fie.txt','','-i')
        mto_correct.assert_any_call('/ll/fie.txt')
        m_o.assert_called_once_with('/ll/fie.txt','r')
        assert m_print.call_count==2
        m_print.assert_any_call('/ll/fie.txt 1 AAAAAA\n')
        m_print.assert_any_call('/ll/fie.txt 2 BBBBBBB\n')

