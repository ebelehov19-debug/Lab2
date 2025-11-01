import pytest
from unittest.mock import patch
def test_cp_dir_to_dir_fl():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_dir,patch('os.path.isfile') as m_file, patch('builtins.print') as mprint,\
        patch('os.path.dirname') as m_d,patch('os.path.basename') as m_be, patch('src.loggining.logcom') as m_logcom,patch('os.path.exists') as m_exists,patch('shutil.copytree') as s_cp:
        mto_correct.side_effect=['/ll/teks','/lp/python']
        m_exists.return_value=1
        m_exists.return_value=1
        m_dir.return_value=1
        from src.cp import cpi
        cpi('/ll/teks','/lp/python','-i')
        assert mto_correct.call_count==2
        mto_correct.assert_any_call('/ll/teks')
        mto_correct.assert_any_call('/lp/python')
        mprint.assert_called_once_with('Не удалось скопировать!!!')
        m_logcom.assert_called_once_with("cp -i /ll/teks /lp/python",0,"Не удалось скопировать!!!")
        



        




        
