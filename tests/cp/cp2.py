import pytest
from unittest.mock import patch
def test_cp_file_to_fakedir():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_dir,patch('os.path.isfile') as m_file, patch('builtins.print') as mprint,\
        patch('os.path.dirname') as m_d,patch('os.rename') as m_r, patch('src.loggining.logcom') as m_logcom,patch('os.path.exists') as m_exists,\
        patch('shutil.copy2') as s_cp2:
        mto_correct.side_effect=['/ll/teks.txt','/flp/python']
        m_exists.return_value=1
        m_exists.return_value=0
        from src.cp import cpi
        cpi('/ll/teks.txt','/flp/python')
        assert mto_correct.call_count==2
        mto_correct.assert_any_call('/ll/teks.txt')
        mto_correct.assert_any_call('/flp/python')
        mprint.assert_called_once_with('Данного пути не существует!!')
        m_logcom.assert_called_once_with('cp /ll/teks.txt /flp/python',0,'Данного пути не существует!!')



        




        
