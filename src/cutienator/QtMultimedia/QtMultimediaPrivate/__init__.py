"""
The namespace 'QtMultimediaPrivate' of Qt, a package of 'cutienator.QtMultimedia':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtMultimedia import QtMultimediaPrivate
  QtMultimediaPrivate.DmaBufPlane

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._qt_multimedia_private import QtMultimediaPrivate as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'DmaBufPlane',
    'EnumName',
    'QEglImageFunctions',
    'QRtAudioEngineVoice',
    'QRtAudioEngineVoiceCompare',
    'QTlsfMemoryResource',
    'QrcMedia',
    'DeleteLaterDeleter',
    'QPlatformAudioIOStream',
    'QRtAudioEngine',
    'QSoundEffectVoice',
    'QPlatformAudioSinkStream',
    'QPlatformAudioSourceStream',
    'QSoundEffectPrivateWithPlayer',
    'DmaBufEglContext',
    'DmaBufTextureHandles',
    'QDmaBufVideoBuffer',
    'ranges',
    'views',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt_multimedia_private__dma_buf_plane import DmaBufPlane
  from .._qt_multimedia_private__enum_name import EnumName
  from .._qt_multimedia_private__q_egl_image_functions import QEglImageFunctions
  from .._qt_multimedia_private__q_rt_audio_engine_voice import QRtAudioEngineVoice
  from .._qt_multimedia_private__q_rt_audio_engine_voice_compare import QRtAudioEngineVoiceCompare
  from .._qt_multimedia_private__q_tlsf_memory_resource import QTlsfMemoryResource
  from .._qt_multimedia_private__qrc_media import QrcMedia
  from .._qt_multimedia_private__delete_later_deleter import DeleteLaterDeleter
  from .._qt_multimedia_private__q_platform_audio_i_o_stream import QPlatformAudioIOStream
  from .._qt_multimedia_private__q_rt_audio_engine import QRtAudioEngine
  from .._qt_multimedia_private__q_sound_effect_voice import QSoundEffectVoice
  from .._qt_multimedia_private__q_platform_audio_sink_stream import QPlatformAudioSinkStream
  from .._qt_multimedia_private__q_platform_audio_source_stream import QPlatformAudioSourceStream
  from .._qt_multimedia_private__q_sound_effect_private_with_player import QSoundEffectPrivateWithPlayer
  from .._qt_multimedia_private__dma_buf_egl_context import DmaBufEglContext
  from .._qt_multimedia_private__dma_buf_texture_handles import DmaBufTextureHandles
  from .._qt_multimedia_private__q_dma_buf_video_buffer import QDmaBufVideoBuffer
  from . import ranges
  from . import views
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'DmaBufPlane': '_qt_multimedia_private__dma_buf_plane',
      'EnumName': '_qt_multimedia_private__enum_name',
      'QEglImageFunctions': '_qt_multimedia_private__q_egl_image_functions',
      'QRtAudioEngineVoice': '_qt_multimedia_private__q_rt_audio_engine_voice',
      'QRtAudioEngineVoiceCompare': '_qt_multimedia_private__q_rt_audio_engine_voice_compare',
      'QTlsfMemoryResource': '_qt_multimedia_private__q_tlsf_memory_resource',
      'QrcMedia': '_qt_multimedia_private__qrc_media',
      'DeleteLaterDeleter': '_qt_multimedia_private__delete_later_deleter',
      'QPlatformAudioIOStream': '_qt_multimedia_private__q_platform_audio_i_o_stream',
      'QRtAudioEngine': '_qt_multimedia_private__q_rt_audio_engine',
      'QSoundEffectVoice': '_qt_multimedia_private__q_sound_effect_voice',
      'QPlatformAudioSinkStream': '_qt_multimedia_private__q_platform_audio_sink_stream',
      'QPlatformAudioSourceStream': '_qt_multimedia_private__q_platform_audio_source_stream',
      'QSoundEffectPrivateWithPlayer': '_qt_multimedia_private__q_sound_effect_private_with_player',
      'DmaBufEglContext': '_qt_multimedia_private__dma_buf_egl_context',
      'DmaBufTextureHandles': '_qt_multimedia_private__dma_buf_texture_handles',
      'QDmaBufVideoBuffer': '_qt_multimedia_private__q_dma_buf_video_buffer',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('ranges', 'views',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QtMultimediaPrivate.DmaBufPlane'. Python calls this for
    a name the package does not hold yet, and what it gives is kept here for
    the next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
