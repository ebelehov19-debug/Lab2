import pytest
from unittest.mock import patch
def test_mv_fake():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_dir,patch('os.path.exists') as mexists, patch('builtins.print') as mprint,\
        patch('os.path.dirname') as m_d,patch('os.rename') as m_r, patch('src.loggining.logcom') as m_logcom, patch('os.path.join') as m_j,patch('os.path.exists') as m_exists:
        mto_correct.side_effect=['/ll/fake.txt','priv.txt']
        m_exists.return_value=0
        m_d.return_value='/ll/'
        m_j.return_value='priv.txt'
        from src.mv import mvi
        mvi('/ll/fake.txt','priv.txt')
        assert mto_correct.call_count==2
        mto_correct.assert_any_call('/ll/fake.txt')
        mto_correct.assert_any_call('priv.txt')
        mprint.assert_called_once_with("ERROR:Данного пути не существует!!")
        m_logcom("mv /ll/fake.txt priv.txt",0,'ERROR:Данного пути не существует!!')




        




        



        




        


