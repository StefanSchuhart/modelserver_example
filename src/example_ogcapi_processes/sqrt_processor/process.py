import math
import time

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.0.1',
    'id': 'sqrt_processor',
    'title': {
        'en': 'Calculate square root.',
        'de': 'Quadratwurzel berechnen.'
    },
    'description': {
        'en': 'Calculate square root.',
        'de': 'Quadratwurzel berechnen.'
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['math', 'square root'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'number': {
            'title': 'a number',
            'description': 'a number',
            'schema': {
                'type': 'number'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,  # TODO how to use?
            'keywords': ['number']
        },

    },
    'outputs': {
        'echo': {
            'id': 'sqrt',
            'value': 'The Square root of the input number.',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
            }
        }
    },
    'example': {
        'inputs': {
            'number': 123,
        }
    }
}

class SlowSqrtProcessor(BaseProcessor):
    """My cool sqrt process plugin"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.mycoolsqrtprocess.MyCoolSqrtProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):

        mimetype = 'application/json'
        number = data.get('number')

        if number is None:
            raise ProcessorExecuteError('Cannot process without a number')

        try:
            number = float(data.get('number'))
        except TypeError:
            raise ProcessorExecuteError('Number required')

        time.sleep(10)
        value = math.sqrt(number)

        outputs = {
            'id': 'sqrt',
            'value': value
        }

        return mimetype, outputs

    def __repr__(self):
        return f'<MyCoolSqrtProcessor> {self.name}'
