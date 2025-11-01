import pytest
from unittest.mock import patch
def test_cat_dir():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_d,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom,\
        patch('os.path.isfile') as m_f,patch('builtins.open') as m_o:
        mto_correct.return_value = '/ll/fie'
        m_d.return_value=1
        m_f.return_value=0
        m_exists.return_value=1
        from src.cat import catti
        catti('/ll/fie')
        mto_correct.assert_called_once_with('/ll/fie')
        m_print.assert_called_once_with('Является директорией')
        m_logcom('cat /ll/fie',0,'Является директорией')
