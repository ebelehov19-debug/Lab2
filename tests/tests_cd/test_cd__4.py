import pytest
from unittest.mock import patch
def test_cd_file():
     with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_istdir,patch('os.path.exists') as m_exists,patch('builtins.print') as m_print, patch('src.loggining.logcom') as m_logcom,patch('os.chdir') as m_ch,\
        patch('os.getcwd') as m_g, patch('os.path.dirname') as m_d:
        m_g.return_value='ll/ld/path'
        m_d.return_value='/ll/ld'
        m_exists.return_value=1
        m_istdir.return_value=1
        from src.cd import cd
        cd('..')
        m_ch.assert_called_once_with('/ll/ld')
        m_logcom.assert_called_once_with('cd /ll/ld',1,'')
          



