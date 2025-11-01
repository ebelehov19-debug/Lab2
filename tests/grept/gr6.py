import pytest
from unittest.mock import patch
def test_grrr_dcorr_r():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_d,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom,\
        patch('os.path.isfile') as m_f,patch('builtins.open') as m_o:
        m_exists.return_value=1
        mto_correct.return_value = '/ll/fie.txt'
        m_d.return_value=0
        m_f.return_value=1
        m_o.return_value.__enter__.return_value = ['812\n', 'text52\n']
        from src.grep import grep
        grep('[0-9]*','/ll/fie.txt','-r')
        mto_correct.assert_any_call('/ll/fie.txt')
        m_print.assert_called_once_with("Используйте -r для поиска в директории")

