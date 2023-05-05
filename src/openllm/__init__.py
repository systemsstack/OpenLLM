# Copyright 2023 BentoML Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
OpenLLM
=======

OpenLLM: Your one stop-and-go-solution for serving any Open Large-Language Model

- StableLM, Llama, Alpaca, Dolly, Flan-T5, and more
- Powered by BentoML 🍱 + HuggingFace 🤗
"""
from __future__ import annotations

import typing as t

from .__about__ import __version__ as __version__
from .exceptions import MissingDependencyError
from .utils import LazyModule as _LazyModule
from .utils import import_utils_shim as imports

_import_structure = {
    "build_utils": [],
    "cli": [],
    "configuration_utils": ["LLMConfig"],
    "exceptions": [],
    "runner_utils": ["LLMRunner", "LLMRunnable", "generate_tokenizer_runner"],
    "schema": ["PromptTemplate"],
    "server_utils": ["start", "start_grpc"],
    "types": [],
    "utils": [],
    "models": [],
    "client": [],
    # NOTE: models
    "models.auto": [
        "AutoConfig",
        "CONFIG_MAPPING",
        "AutoTokenizer",
        "TOKENIZER_MAPPING",
        "TOKENIZER_MAPPING_NAMES",
    ],
    "models.flan_t5": ["FlanT5Config", "START_FLAN_T5_COMMAND_DOCSTRING"],
}

try:
    if not imports.is_torch_available():
        raise MissingDependencyError
except MissingDependencyError:
    pass
else:
    _import_structure["models.flan_t5"].extend(["FlanT5", "FlanT5WithTokenizer", "FlanT5Tokenizer"])
    _import_structure["models.auto"].extend(
        [
            "AutoLLM",
            "AutoLLMWithTokenizer",
            "MODEL_MAPPING_NAMES",
            "MODEL_WITH_TOKENIZER_MAPPING_NAMES",
            "MODEL_MAPPING",
            "MODEL_WITH_TOKENIZER_MAPPING",
        ]
    )

try:
    if not imports.is_flax_available():
        raise MissingDependencyError
except MissingDependencyError:
    pass
else:
    _import_structure["models.flan_t5"].extend(["FlaxFlanT5", "FlaxFlanT5WithTokenizer"])
    _import_structure["models.auto"].extend(
        [
            "AutoFlaxLLM",
            "AutoFlaxLLMWithTokenizer",
            "MODEL_FLAX_MAPPING_NAMES",
            "MODEL_FLAX_WITH_TOKENIZER_MAPPING_NAMES",
            "MODEL_FLAX_MAPPING",
            "MODEL_FLAX_WITH_TOKENIZER_MAPPING",
        ]
    )

try:
    if not imports.is_tf_available():
        raise MissingDependencyError
except MissingDependencyError:
    pass
else:
    _import_structure["models.flan_t5"].extend(["TFFlanT5", "TFFlanT5WithTokenizer"])
    _import_structure["models.auto"].extend(
        [
            "AutoTFLLM",
            "AutoTFLLMWithTokenizer",
            "MODEL_TF_MAPPING_NAMES",
            "MODEL_TF_WITH_TOKENIZER_MAPPING_NAMES",
            "MODEL_TF_MAPPING",
            "MODEL_TF_WITH_TOKENIZER_MAPPING",
        ]
    )


# declaration for OpenLLM-related modules
if t.TYPE_CHECKING:
    from . import build_utils as build_utils
    from . import cli as cli
    from . import client as client
    from . import configuration_utils as configuration_utils
    from . import exceptions as exceptions
    from . import models as models
    from . import runner_utils as runner_utils
    from . import schema as schema
    from . import server_utils as server_utils
    from . import types as types
    from . import utils as utils
    # Specific types import
    from .configuration_utils import LLMConfig as LLMConfig
    from .models.auto import CONFIG_MAPPING as CONFIG_MAPPING
    from .models.auto import TOKENIZER_MAPPING as TOKENIZER_MAPPING
    from .models.auto import TOKENIZER_MAPPING_NAMES as TOKENIZER_MAPPING_NAMES
    from .models.auto import AutoConfig as AutoConfig
    from .models.auto import AutoTokenizer as AutoTokenizer
    from .models.flan_t5 import \
        START_FLAN_T5_COMMAND_DOCSTRING as START_FLAN_T5_COMMAND_DOCSTRING
    from .models.flan_t5 import FlanT5Config as FlanT5Config
    from .runner_utils import LLMRunnable as LLMRunnable
    from .runner_utils import LLMRunner as LLMRunner
    from .runner_utils import \
        generate_tokenizer_runner as generate_tokenizer_runner
    from .schema import PromptTemplate as PromptTemplate
    from .server_utils import start as start
    from .server_utils import start_grpc as start_grpc

    try:
        if not imports.is_torch_available():
            raise MissingDependencyError
    except MissingDependencyError:
        pass
    else:
        from .models.auto import MODEL_MAPPING as MODEL_MAPPING
        from .models.auto import MODEL_MAPPING_NAMES as MODEL_MAPPING_NAMES
        from .models.auto import \
            MODEL_WITH_TOKENIZER_MAPPING as MODEL_WITH_TOKENIZER_MAPPING
        from .models.auto import \
            MODEL_WITH_TOKENIZER_MAPPING_NAMES as \
            MODEL_WITH_TOKENIZER_MAPPING_NAMES
        from .models.auto import AutoLLM as AutoLLM
        from .models.auto import AutoLLMWithTokenizer as AutoLLMWithTokenizer
        from .models.flan_t5 import FlanT5 as FlanT5
        from .models.flan_t5 import FlanT5Tokenizer as FlanT5Tokenizer
        from .models.flan_t5 import FlanT5WithTokenizer as FlanT5WithTokenizer

    try:
        if not imports.is_flax_available():
            raise MissingDependencyError
    except MissingDependencyError:
        pass
    else:
        from .models.auto import MODEL_FLAX_MAPPING as MODEL_FLAX_MAPPING
        from .models.auto import \
            MODEL_FLAX_MAPPING_NAMES as MODEL_FLAX_MAPPING_NAMES
        from .models.auto import \
            MODEL_FLAX_WITH_TOKENIZER_MAPPING as \
            MODEL_FLAX_WITH_TOKENIZER_MAPPING
        from .models.auto import \
            MODEL_FLAX_WITH_TOKENIZER_MAPPING_NAMES as \
            MODEL_FLAX_WITH_TOKENIZER_MAPPING_NAMES
        from .models.auto import AutoFlaxLLM as AutoFlaxLLM
        from .models.auto import \
            AutoFlaxLLMWithTokenizer as AutoFlaxLLMWithTokenizer
        from .models.flan_t5 import FlaxFlanT5 as FlaxFlanT5
        from .models.flan_t5 import \
            FlaxFlanT5WithTokenizer as FlaxFlanT5WithTokenizer

    try:
        if not imports.is_tf_available():
            raise MissingDependencyError
    except MissingDependencyError:
        pass
    else:
        from .models.auto import MODEL_TF_MAPPING as MODEL_TF_MAPPING
        from .models.auto import \
            MODEL_TF_MAPPING_NAMES as MODEL_TF_MAPPING_NAMES
        from .models.auto import \
            MODEL_TF_WITH_TOKENIZER_MAPPING as MODEL_TF_WITH_TOKENIZER_MAPPING
        from .models.auto import \
            MODEL_TF_WITH_TOKENIZER_MAPPING_NAMES as \
            MODEL_TF_WITH_TOKENIZER_MAPPING_NAMES
        from .models.auto import AutoTFLLM as AutoTFLLM
        from .models.auto import \
            AutoTFLLMWithTokenizer as AutoTFLLMWithTokenizer
        from .models.flan_t5 import TFFlanT5 as TFFlanT5
        from .models.flan_t5 import \
            TFFlanT5WithTokenizer as TFFlanT5WithTokenizer

else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
        extra_objects={"__version__": __version__},
    )
