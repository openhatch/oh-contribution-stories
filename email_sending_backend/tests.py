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
                u'The first step',
                u'next step 1',
                u'next step 2',
                u'next step 3',
                ],
            'email': 'email',
            'link': 'link ',
            'project': 'project',
            }
        self.assertEqual(sorted(got.items()),
                         sorted(expected.items()))

    def test_turn_meaningful_data_into_string_for_email(self):
        data = {
            'name': u'Asheesh Just Testing',
            'tags': u'Comma,delimited,tags',
            'title': u'title',
            'steps': [
                u'The first step',
                u'next step 1',
                u'next step 2',
                u'next step 3',
                ],
            'email': u'email',
            'link': u'link ',
            'project': u'project',
        }
        email_body = '''Hi there,

There was a new Merge Stories submission!

Email: email
Link: link 
Name: Asheesh Just Testing
Project: project
Tags: Comma,delimited,tags
Title: title

Steps:

The first step

next step 1

next step 2

next step 3
'''
        self.assertEqual(app.format_as_email(data),
                         email_body)
