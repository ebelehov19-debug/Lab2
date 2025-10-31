import pytest
from unittest.mock import patch
def test_cd_file():
     with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_istdir,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom,patch('os.chdir') as m_ch:
        mto_correct.return_value ='/ll/path'
        m_exists.return_value=0
        from src.cd import cd
        cd('/ll/path')
        mto_correct.assert_called_once_with('/ll/path')
        m_print.assert_called_once_with('ERROR:Данного пути не существует')
        m_logcom.assert_called_once_with('cd /ll/path',0,'Данного пути не существует')
          



