"""
The 'cutienator.QtSpatialAudio' package provides the cute classes of the
part of Qt named QtSpatialAudio, under the name PySide6 has for it.

  from cutienator.QtSpatialAudio import QAmbisonicDecoder, QAudioEngine

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
    'QAmbisonicDecoder',
    'QAudioEngine',
    'QAmbientSound',
    'QSpatialAudioSoundPrivate',
    'QAudioListener',
    'QAudioRoom',
    'QSpatialSound',
    'QAudioEnginePrivate',
    'QAudioEngineThreaded',
    'QAudioEngineWithPlayer',
    'QSpatialAudioPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_ambisonic_decoder import QAmbisonicDecoder
  from ._q_audio_engine import QAudioEngine
  from ._q_ambient_sound import QAmbientSound
  from ._q_spatial_audio_sound_private import QSpatialAudioSoundPrivate
  from ._q_audio_listener import QAudioListener
  from ._q_audio_room import QAudioRoom
  from ._q_spatial_sound import QSpatialSound
  from ._q_audio_engine_private import QAudioEnginePrivate
  from ._q_audio_engine_threaded import QAudioEngineThreaded
  from ._q_audio_engine_with_player import QAudioEngineWithPlayer
  from . import QSpatialAudioPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QAmbisonicDecoder': '_q_ambisonic_decoder',
      'QAudioEngine': '_q_audio_engine',
      'QAmbientSound': '_q_ambient_sound',
      'QSpatialAudioSoundPrivate': '_q_spatial_audio_sound_private',
      'QAudioListener': '_q_audio_listener',
      'QAudioRoom': '_q_audio_room',
      'QSpatialSound': '_q_spatial_sound',
      'QAudioEnginePrivate': '_q_audio_engine_private',
      'QAudioEngineThreaded': '_q_audio_engine_threaded',
      'QAudioEngineWithPlayer': '_q_audio_engine_with_player',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QSpatialAudioPrivate',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtSpatialAudio import QAudioEngineWithPlayer'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
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
