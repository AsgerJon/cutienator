"""
The namespace 'QtMultimediaPrivate' of Qt, a package of 'cutienator.QtMultimediaQuick':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtMultimediaQuick import QtMultimediaPrivate
  QtMultimediaPrivate.QAudioDeviceForeign

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QAudioDeviceForeign',
    'QAudioInputForeign',
    'QAudioOutputForeign',
    'QCameraDeviceForeign',
    'QCameraForeign',
    'QCameraFormatForeign',
    'QCapturableWindowForeign',
    'QGStreamerVideoSourceForeign',
    'QImageCaptureForeign',
    'QMediaCaptureSessionForeign',
    'QMediaDevicesForeign',
    'QMediaFormatForeign',
    'QMediaMetaDataForeign',
    'QMediaRecorderForeign',
    'QScreenCaptureForeign',
    'QWindowCaptureForeign',
    'QAudioDeviceDerived',
    'QCameraDeviceDerived',
    'QMediaFormatDerived',
    'QMediaMetaDataDerived',
    'QPlaybackOptionsDerived',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt_multimedia_private__q_audio_device_foreign import QAudioDeviceForeign
  from .._qt_multimedia_private__q_audio_input_foreign import QAudioInputForeign
  from .._qt_multimedia_private__q_audio_output_foreign import QAudioOutputForeign
  from .._qt_multimedia_private__q_camera_device_foreign import QCameraDeviceForeign
  from .._qt_multimedia_private__q_camera_foreign import QCameraForeign
  from .._qt_multimedia_private__q_camera_format_foreign import QCameraFormatForeign
  from .._qt_multimedia_private__q_capturable_window_foreign import QCapturableWindowForeign
  from .._qt_multimedia_private__q_g_streamer_video_source_foreign import QGStreamerVideoSourceForeign
  from .._qt_multimedia_private__q_image_capture_foreign import QImageCaptureForeign
  from .._qt_multimedia_private__q_media_capture_session_foreign import QMediaCaptureSessionForeign
  from .._qt_multimedia_private__q_media_devices_foreign import QMediaDevicesForeign
  from .._qt_multimedia_private__q_media_format_foreign import QMediaFormatForeign
  from .._qt_multimedia_private__q_media_meta_data_foreign import QMediaMetaDataForeign
  from .._qt_multimedia_private__q_media_recorder_foreign import QMediaRecorderForeign
  from .._qt_multimedia_private__q_screen_capture_foreign import QScreenCaptureForeign
  from .._qt_multimedia_private__q_window_capture_foreign import QWindowCaptureForeign
  from .._qt_multimedia_private__q_audio_device_derived import QAudioDeviceDerived
  from .._qt_multimedia_private__q_camera_device_derived import QCameraDeviceDerived
  from .._qt_multimedia_private__q_media_format_derived import QMediaFormatDerived
  from .._qt_multimedia_private__q_media_meta_data_derived import QMediaMetaDataDerived
  from .._qt_multimedia_private__q_playback_options_derived import QPlaybackOptionsDerived
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'QAudioDeviceForeign': '_qt_multimedia_private__q_audio_device_foreign',
      'QAudioInputForeign': '_qt_multimedia_private__q_audio_input_foreign',
      'QAudioOutputForeign': '_qt_multimedia_private__q_audio_output_foreign',
      'QCameraDeviceForeign': '_qt_multimedia_private__q_camera_device_foreign',
      'QCameraForeign': '_qt_multimedia_private__q_camera_foreign',
      'QCameraFormatForeign': '_qt_multimedia_private__q_camera_format_foreign',
      'QCapturableWindowForeign': '_qt_multimedia_private__q_capturable_window_foreign',
      'QGStreamerVideoSourceForeign': '_qt_multimedia_private__q_g_streamer_video_source_foreign',
      'QImageCaptureForeign': '_qt_multimedia_private__q_image_capture_foreign',
      'QMediaCaptureSessionForeign': '_qt_multimedia_private__q_media_capture_session_foreign',
      'QMediaDevicesForeign': '_qt_multimedia_private__q_media_devices_foreign',
      'QMediaFormatForeign': '_qt_multimedia_private__q_media_format_foreign',
      'QMediaMetaDataForeign': '_qt_multimedia_private__q_media_meta_data_foreign',
      'QMediaRecorderForeign': '_qt_multimedia_private__q_media_recorder_foreign',
      'QScreenCaptureForeign': '_qt_multimedia_private__q_screen_capture_foreign',
      'QWindowCaptureForeign': '_qt_multimedia_private__q_window_capture_foreign',
      'QAudioDeviceDerived': '_qt_multimedia_private__q_audio_device_derived',
      'QCameraDeviceDerived': '_qt_multimedia_private__q_camera_device_derived',
      'QMediaFormatDerived': '_qt_multimedia_private__q_media_format_derived',
      'QMediaMetaDataDerived': '_qt_multimedia_private__q_media_meta_data_derived',
      'QPlaybackOptionsDerived': '_qt_multimedia_private__q_playback_options_derived',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QtMultimediaPrivate.QAudioDeviceForeign'. Python calls
    this for a name the package does not hold yet, and what it gives is kept
    here for the next time.

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
    return [*__all__]
