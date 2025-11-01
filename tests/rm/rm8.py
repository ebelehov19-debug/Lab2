import pytest
from unittest.mock import patch
def test_rm_delfile_no():
    with patch('src.pathcorr.to_correct') as mto_correct,patch('os.path.isdir') as m_dir,patch('os.path.exists') as mexists, patch('builtins.print') as mprint,\
        patch('os.path.dirname') as m_d,patch('os.remove') as m_re, patch('src.loggining.logcom') as m_logcom,patch('os.path.exists') as m_exists,\
        patch('os.path.isfile') as m_fl,patch('builtins.input') as m_inp:
        from src.rm import rm
        rm('.')
        mprint.assert_called_once_with('Error: Невозмажно удалить директорию')
        m_logcom.assert_called_once_with("rm .",0,'Невозмажно удалить директорию')

       
        



        




        