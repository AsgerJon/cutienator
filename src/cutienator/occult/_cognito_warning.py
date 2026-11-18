"""
CognitoHazard subclasses 'UserWarning'.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

import os

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class CognitoWarning(UserWarning):
  """
  CognitoHazard subclasses 'UserWarning'.
  """

  __slots__ = ('note',)

  def __init__(self, note: Optional[str] = None) -> None:
    if note is not None:
      self.note = note
    super().__init__(self.__str__())

  def __str__(self) -> str:
    infoSpec: str = """Warning, Cognito Hazard Ahead!%s%s"""
    try:
      noteStr = self.note
    except AttributeError:
      return infoSpec % ('', '')
    else:
      return infoSpec % (os.linesep, noteStr)
