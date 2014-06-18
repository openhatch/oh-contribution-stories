import flask
import app
import unittest

class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_convert_post_to_meaningful_data(self):
        sample_data = {
            'entry.1954301530': ['next step 3'],
            'fbzx': ['-6022307322665735255'],
            'entry.235795032': ['link '],
            'entry.178508708': ['next step 2'],
            'pageHistory': ['0'],
            'entry.1389151802': ['The first step'],
            'draftResponse': ['[,,"-6022307322665735255"]'],
            'submit': ['Submit'],
            'entry.1919080730': ['email'],
            'entry.300556150': ['project'],
            'entry.603062675': ['next step 1'],
            'entry.2023565106': ['Asheesh Just Testing'],
            'entry.690550334': ['Comma,delimited,tags'],
            'entry.1363522345': ['title'],
        }
        got = app.post_to_meaningful_data(sample_data)
        expected = {
            'name': 'Asheesh Just Testing',
            'tags': 'Comma,delimited,tags',
            'title': 'title',
            'steps': [
                'The first step',
                'next step 1',
                'next step 2',
                'next step 3',
                ],
            'email': 'email',
            'link': 'link ',
            'project': 'project',
            }
        self.assertEqual(sorted(got.items()),
                         sorted(expected.items()))

    #def test_post_calls_email_sender(self):
    #    rv = self.app.post('/', post={})
    #    import pdb; pdb.set_trace()
            

    
        
