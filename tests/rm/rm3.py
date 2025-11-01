import pytest
from unittest.mock import patch
def test_rm_delfile():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_dir,patch('os.path.exists') as mexists, patch('builtins.print') as mprint,\
        patch('os.path.dirname') as m_d,patch('os.remove') as m_re, patch('src.loggining.logcom') as m_logcom,patch('os.path.exists') as m_exists,\
        patch('os.path.isfile') as m_fl,patch('builtins.input') as m_inp,patch('shutil.rmtree') as s_rm:
        mto_correct.return_value='/ll/teks'
        m_exists.return_value=1
        m_dir.return_value=1
        m_fl.return_value=0
        m_inp.return_value='y'
        from src.rm import rm
        rm('/ll/teks')
        mto_correct.assert_called_once_with('/ll/teks')
        mprint.assert_called_once_with("ERROR:Не удалось удалить!!!")
        m_logcom.assert_called_once_with("rm /ll/teks",0,'Не удалось удалить!!!')




        




        