import pytest
from unittest.mock import patch
def test_cd_corr():
     with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_istdir,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom,patch('os.chdir') as m_ch:
        mto_correct.return_value ='/ll/path'
        m_exists.return_value=1
        m_istdir.return_value=1
        from src.cd import cd
        cd('/ll/path')
        mto_correct.assert_called_once_with('/ll/path')
        m_istdir.assert_called_once_with('/ll/path')
        m_ch.assert_called_once_with('/ll/path')
        m_logcom.assert_called_once_with('cd /ll/path',1,'')
          


