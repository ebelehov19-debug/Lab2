import pytest
from unittest.mock import patch
def test_cat_fkpath():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_d,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom,\
        patch('os.path.isfile') as m_f,patch('builtins.open') as m_o:
        mto_correct.return_value = '/ll/fke'
        m_exists.return_value=0
        from src.cat import catti
        catti('/ll/fke')
        mto_correct.assert_called_once_with('/ll/fke')
        m_print.assert_called_once_with('Данного пути не существует')
        m_logcom('cat /ll/fke',0,'Данного пути не существует')
