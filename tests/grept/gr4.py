import pytest
from unittest.mock import patch
def test_gr_dontcorr():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_d,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom,\
        patch('os.path.isfile') as m_f,patch('builtins.open') as m_o:
        m_exists.return_value=0
        mto_correct.return_value = '/l/lfie.txt'
        from src.grep import grep
        grep('[0-9]*','/l/lfie.txt')
        mto_correct.assert_any_call('/l/lfie.txt')
        m_print('Данного пути не существует')
