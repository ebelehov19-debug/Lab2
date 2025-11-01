import pytest
from unittest.mock import patch
def test_mv_dir_to_dir():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_dir, patch('builtins.print') as mprint,\
         patch('src.loggining.logcom') as m_logcom,patch('os.path.exists') as m_exists,patch('shutil.move') as s_mv:
        mto_correct.side_effect=['/ll/teks.txt','priv/path']
        m_exists.return_value=1
        m_dir.return_value=1
        from src.mv import mvi
        mvi('/ll/teks.txt','priv/path')
        assert mto_correct.call_count==2
        mto_correct.assert_any_call('/ll/teks.txt')
        mto_correct.assert_any_call('priv/path')
        s_mv.assert_called_once_with('/ll/teks.txt','priv/path')




        




        