"""
The 'cutienator.QtMultimediaQuick' package provides the cute classes of
the part of Qt named QtMultimediaQuick, under the name PySide6 has for
it.

  from cutienator.QtMultimediaQuick import QQuickImagePreviewProvider, QQuickSoundEffect

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
    'QQuickImagePreviewProvider',
    'QQuickSoundEffect',
    'QQuickVideoSink',
    'QSGVideoTexture',
    'QQuickImageCapture',
    'QQuickMediaPlayer',
    'QQuickScreenCapture',
    'QQuickWindowCapture',
    'QQuickGStreamerVideoSource',
    'QQuickVideoOutput',
    'QSGVideoNode',
    'QMultimediaPrivate',
    'QtMultimediaPrivate',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_quick_image_preview_provider import QQuickImagePreviewProvider
  from ._q_quick_sound_effect import QQuickSoundEffect
  from ._q_quick_video_sink import QQuickVideoSink
  from ._q_s_g_video_texture import QSGVideoTexture
  from ._q_quick_image_capture import QQuickImageCapture
  from ._q_quick_media_player import QQuickMediaPlayer
  from ._q_quick_screen_capture import QQuickScreenCapture
  from ._q_quick_window_capture import QQuickWindowCapture
  from ._q_quick_g_streamer_video_source import QQuickGStreamerVideoSource
  from ._q_quick_video_output import QQuickVideoOutput
  from ._q_s_g_video_node import QSGVideoNode
  from . import QMultimediaPrivate
  from . import QtMultimediaPrivate
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQuickImagePreviewProvider': '_q_quick_image_preview_provider',
      'QQuickSoundEffect': '_q_quick_sound_effect',
      'QQuickVideoSink': '_q_quick_video_sink',
      'QSGVideoTexture': '_q_s_g_video_texture',
      'QQuickImageCapture': '_q_quick_image_capture',
      'QQuickMediaPlayer': '_q_quick_media_player',
      'QQuickScreenCapture': '_q_quick_screen_capture',
      'QQuickWindowCapture': '_q_quick_window_capture',
      'QQuickGStreamerVideoSource': '_q_quick_g_streamer_video_source',
      'QQuickVideoOutput': '_q_quick_video_output',
      'QSGVideoNode': '_q_s_g_video_node',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QMultimediaPrivate', 'QtMultimediaPrivate',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtMultimediaQuick import QSGVideoNode'. Python calls
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
