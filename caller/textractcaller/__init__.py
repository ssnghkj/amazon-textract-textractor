from ._version import __version__
from .t_call import NotificationChannel, OutputConfig, DocumentLocation, Document, get_job_response, get_full_json_from_output_config, get_full_json, call_textract

import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
