# Copyright 2023 Google LLC
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
#
"""Classes for working with the Gemini models."""

# We just want to re-export certain classes
# pylint: disable=g-multiple-import,g-importing-member
from vertexai.generative_models._generative_models import (
    grounding,
    _PreviewGenerativeModel,
    _PreviewChatSession,
    GenerationConfig,
    GenerationResponse,
    Candidate,
    Content,
    FinishReason,
    FunctionDeclaration,
    HarmCategory,
    HarmBlockThreshold,
    Image,
    Part,
    ResponseBlockedError,
    ResponseValidationError,
    Tool,
)


class GenerativeModel(_PreviewGenerativeModel):
    __doc__ = _PreviewGenerativeModel.__doc__


class ChatSession(_PreviewChatSession):
    __doc__ = _PreviewChatSession.__doc__


__all__ = [
    "grounding",
    "GenerationConfig",
    "GenerativeModel",
    "GenerationResponse",
    "Candidate",
    "ChatSession",
    "Content",
    "FinishReason",
    "FunctionDeclaration",
    "HarmCategory",
    "HarmBlockThreshold",
    "Image",
    "Part",
    "ResponseBlockedError",
    "ResponseValidationError",
    "Tool",
]
