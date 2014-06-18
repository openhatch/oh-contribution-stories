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
        'entry.178508708': 'step 2',
        'entry.1389151802': 'step 0',
        'entry.1954301530': 'step 3',
        'entry.1919080730': 'email',
        'entry.2023565106': 'name',
        'entry.603062675': 'step 1',
        'entry.300556150': 'project',
        'entry.690550334': 'tags',
        'entry.1363522345': 'title',
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

@app.route('/')
def index():
    if request.method == 'POST':
        _send_email(post_dict)

def _send_email(from_addr, subject, post_dict):
    # This function is tested manually.
    return

