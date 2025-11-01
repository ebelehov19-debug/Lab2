import pytest
from unittest.mock import patch
def test_cp_file_to_dir():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_dir,patch('os.path.isfile') as m_file, patch('builtins.print') as mprint,\
        patch('os.path.dirname') as m_d,patch('os.rename') as m_r, patch('src.loggining.logcom') as m_logcom,patch('os.path.exists') as m_exists,\
        patch('shutil.copy2') as s_cp2:
        mto_correct.side_effect=['/ll/teks.txt','/lp/python']
        m_exists.return_value=1
        m_exists.return_value=1
        m_dir.return_value=0
        m_file.return_value=1
        from src.cp import cpi
        cpi('/ll/teks.txt','/lp/python')
        assert mto_correct.call_count==2
        mto_correct.assert_any_call('/ll/teks.txt')
        mto_correct.assert_any_call('/lp/python')
        s_cp2.assert_called_once_with('/ll/teks.txt','/lp/python')
        m_logcom.assert_called_once_with('cp  /ll/teks.txt /lp/python',1,'')



        




        
