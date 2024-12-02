import unittest
from unittest.mock import patch, MagicMock
from services import api_pipefy
    

class TestYourModule(unittest.TestCase):

    @patch('requests.post')
    def test_create_pipe(self, mock_post):
        # Configurando o mock
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"data": {"createPipe": {"clientMutationId": "123"}}})

        result = api_pipefy.create_pipe("Test Pipe", 1)
        self.assertEqual(result, {"data": {"createPipe": {"clientMutationId": "123"}}})
        mock_post.assert_called_once()

    @patch('requests.post')
    def test_update_pipe(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"data": {"updatePipe": {"pipe": {"id": "1"}}}})

        result = api_pipefy.update_pipe(1, "Updated Pipe")
        self.assertEqual(result, {"data": {"updatePipe": {"pipe": {"id": "1"}}}})
        mock_post.assert_called_once()

    @patch('requests.post')
    def test_delete_pipe(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"data": {"deletePipe": {"success": True}}})

        result = api_pipefy.delete_pipe(1)
        self.assertEqual(result, {"data": {"deletePipe": {"success": True}}})
        mock_post.assert_called_once()

    @patch('requests.post')
    def test_get_pipe_reports(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"data": {"pipe": {"reports": []}}})

        result = api_pipefy.get_pipe_reports(1)
        self.assertEqual(result, {"data": {"pipe": {"reports": []}}})
        mock_post.assert_called_once()

    @patch('requests.post')
    def test_export_pipe_report(self, mock_post):
        mock_post.return_value = MagicMock(status_code=200, json=lambda: {"data": {"exportPipeReport": {"pipeReportExport": {"id": "report_id"}}}})

        result = api_pipefy.export_pipe_report(1, 1)
        self.assertEqual(result, {"data": {"exportPipeReport": {"pipeReportExport": {"id": "report_id"}}}})
        mock_post.assert_called_once()

    # Adicione mais testes para outras funções conforme necessário
if __name__ == '__main__':
    unittest.main()