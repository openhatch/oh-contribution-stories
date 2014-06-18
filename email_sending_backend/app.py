from flask import Flask
import types
app = Flask(__name__)

FROM_ADDR = 'noreply+mergestories@linode.openhatch.org'
SUBJECT = 'A new merge story'
TO = 'mergestories@localhost'

def post_to_meaningful_data(d):
    just_useful_data = {}
    out = {}

    for k, v in d.items():
        if not k.startswith('entry.'):
            continue

        if type(v) not in types.StringTypes:
            v = v[0]  # for unpacking a list, for example

        # Make sure we did it right
        assert type(v) in types.StringTypes

        # Make sure it's glorious pure Python Unicode
        if type(v) != unicode:
            v = unicode(v, 'utf-8', 'ignore')  # utf-8 or bust

        just_useful_data[k] = v

    # Now, filter for the key names we want
    input_to_output_keys = {
        'entry.235795032': 'link',
        'entry.1389151802': 'step 0',
        'entry.1919080730': 'email',
        'entry.2023565106': 'name',
        'entry.603062675': 'step 1',
        'entry.300556150': 'project',
        'entry.690550334': 'tags',
        'entry.1363522345': 'title',
        'entry.178508708': 'step 2',
        'entry.1954301530': 'step 3',
        'entry.731379118': 'step 4',
        'entry.1448384929': 'step 5',
        'entry.1224977072': 'step 6',
        'entry.2073139872': 'step 7',
        'entry.1771949325': 'step 8',
        'entry.1419921080': 'step 9',
        'entry.65011868': 'step 10',
        'entry.122349419': 'step 11',
        'entry.1515341332': 'step 12',
        'entry.441925640': 'step 13',
        'entry.441127551': 'step 14',
        'entry.1660802530': 'step 15',
        'entry.807514746': 'step 16',
    }

    step_dict = {}

    for k in just_useful_data:
        if k not in input_to_output_keys:
            continue

        v = just_useful_data[k]
        output_key = input_to_output_keys[k]
        if output_key.startswith('step '):
            step_dict[output_key[len('step '):]] = v
        else:
            out[input_to_output_keys[k]] = v

    # Now, make the steps a list
    sorted_step_items = sorted(step_dict.items(), key=lambda x: int(x[0]))
    if sorted_step_items:
        out['steps'] = [v for k, v in sorted_step_items]

    return out

def format_as_email(nice_data_dict):
    if 'steps' in nice_data_dict:
        steps = nice_data_dict.pop('steps')
    dict_as_str = u''
    for k, v in sorted(nice_data_dict.items(), key=lambda i: i[0]):
        if type(k) != unicode:
            k = unicode(k, 'utf-8', 'ignore')

        assert type(v) == unicode
        dict_as_str +=  k.title() + ': ' + v + '\n'

    s = '''Hi there,

There was a new Merge Stories submission!

%s''' % (dict_as_str,)
    if steps:
        s += '\nSteps:\n\n'
        s += '\n\n'.join(steps)
        s += '\n'
    return s

@app.route('/')
def index():
    if request.method == 'POST':
        # Copy the request.form into a vanilla dict
        d = {}
        for key in request.form:
            d[unicode(key, 'utf-8', 'ignore')]  = request.form[key]
        nice_data_dict = post_to_meaningful_data(d)
        _send_email(msg)

def _send_email(msg):
    import pdb; pdb.set_trace()
    # This function is tested manually.
    return

