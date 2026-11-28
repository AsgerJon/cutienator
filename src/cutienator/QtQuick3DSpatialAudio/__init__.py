"""
The 'cutienator.QtQuick3DSpatialAudio' package provides the cute classes
of the part of Qt named QtQuick3DSpatialAudio, under the name PySide6
has for it.

  from cutienator.QtQuick3DSpatialAudio import QQuick3DAmbientSound, QQuick3DAudioEngine

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QQuick3DAmbientSound',
    'QQuick3DAudioEngine',
    'QQuick3DAudioListener',
    'QQuick3DAudioRoom',
    'QQuick3DSpatialSound',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick3_d_ambient_sound import QQuick3DAmbientSound
  from ._q_quick3_d_audio_engine import QQuick3DAudioEngine
  from ._q_quick3_d_audio_listener import QQuick3DAudioListener
  from ._q_quick3_d_audio_room import QQuick3DAudioRoom
  from ._q_quick3_d_spatial_sound import QQuick3DSpatialSound
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuick3DAmbientSound': '_q_quick3_d_ambient_sound',
      'QQuick3DAudioEngine': '_q_quick3_d_audio_engine',
      'QQuick3DAudioListener': '_q_quick3_d_audio_listener',
      'QQuick3DAudioRoom': '_q_quick3_d_audio_room',
      'QQuick3DSpatialSound': '_q_quick3_d_spatial_sound',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQuick3DSpatialAudio import QQuick3DSpatialSound'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
