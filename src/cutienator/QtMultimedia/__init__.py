"""
The 'cutienator.QtMultimedia' package provides the cute classes of the
part of Qt named QtMultimedia, under the name PySide6 has for it.

  from cutienator.QtMultimedia import Fraction, QAbstractPlatformSpecificInterface

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
    'Fraction',
    'QAbstractPlatformSpecificInterface',
    'QAudioFormat',
    'QMediaInputEncoderInterface',
    'QMediaRecorderPrivate',
    'QMediaTimeRange',
    'QPlatformAudioResampler',
    'SymbolsResolver',
    'VideoTransformation',
    'QAudioBuffer',
    'QAudioBufferOutput',
    'QAudioBufferSource',
    'QAudioDecoder',
    'QAudioDevice',
    'QAudioDevicePrivate',
    'QCameraDevice',
    'QCameraDevicePrivate',
    'QCameraFormat',
    'QCameraFormatPrivate',
    'QMediaDevices',
    'QMediaFormat',
    'QMediaMetaData',
    'QPlatformMediaPlugin',
    'QPlaybackOptions',
    'QSample',
    'QSampleCache',
    'QVideoOutputOrientationHandler',
    'QWaveDecoder',
    'QAlsaAudioDeviceInfo',
    'QAndroidAudioDevice',
    'QAudioDecoderPrivate',
    'QAudioDevicePrivateAllMembersEqual',
    'QAudioInput',
    'QAudioOutput',
    'QAudioSink',
    'QAudioSource',
    'QCameraPrivate',
    'QCoreAudioDeviceInfo',
    'QOhosAudioDevice',
    'QPlatformAudioBufferInput',
    'QPlatformAudioDecoder',
    'QPlatformAudioDevices',
    'QPlatformAudioEndpointBase',
    'QPlatformMediaFormatInfo',
    'QPulseAudioDevicePrivate',
    'QQnxSndAudioDeviceInfo',
    'QSoundEffect',
    'QWasmAudioDevice',
    'QnxAudioDeviceInfo',
    'QAlsaAudioDevices',
    'QAndroidAudioDevices',
    'QCoreAudioDevices',
    'QDrWavAudioDecoder',
    'QPlatformAudioInput',
    'QPlatformAudioOutput',
    'QPlatformAudioSink',
    'QPlatformAudioSource',
    'QPulseAudioDevices',
    'QQnxAudioDevices',
    'QQnxSndAudioDevices',
    'QSoundEffectPrivate',
    'QAbstractVideoBuffer',
    'QVideoFrame',
    'QVideoFrameFormat',
    'QSoundEffectPrivateSynchronous',
    'QImageVideoBuffer',
    'QMemoryVideoBuffer',
    'QVideoFramePrivate',
    'QVideoFrameTextures',
    'QCapturableWindow',
    'QCapturableWindowPrivate',
    'QVideoWindow',
    'QPlatformCapturableWindows',
    'QRhiCallback',
    'QVideoFrameTexturePool',
    'QVideoFrameTexturesHandles',
    'QVideoSink',
    'QVideoWindowPrivate',
    'QAudioBufferInput',
    'QCamera',
    'QImageCapture',
    'QMediaCaptureSession',
    'QMediaRecorder',
    'QScreenCapture',
    'QVideoFrameInput',
    'QWindowCapture',
    'QHwVideoBuffer',
    'QMediaPlayer',
    'QPlatformVideoSink',
    'QAudioBufferOutputPrivate',
    'QGStreamerInterface',
    'QGStreamerVideoSource',
    'QImageEncoderSettings',
    'QMediaCaptureSessionPrivate',
    'QMediaEncoderSettings',
    'QMediaFrameInputPrivate',
    'QPlatformMediaPlayer',
    'QWindowCapturePrivate',
    'QGStreamerVideoSourcePrivate',
    'QMediaPlayerPrivate',
    'QPlatformMediaIntegration',
    'QPlatformMediaRecorder',
    'QPlatformMediaCaptureSession',
    'QPlatformVideoSource',
    'QPlatformSurfaceCapture',
    'QPlatformVideoFrameInput',
    'QPlatformVideoDevices',
    'QSurfaceCaptureGrabber',
    'QAudio',
    'QAudioHelperInternal',
    'QMultimediaPrivate',
    'QVideoTextureHelper',
    'QtMultimediaPrivate',
    'QtPipeWire',
    'QtPrivate',
    'QtVideo',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._fraction import Fraction
  from ._q_abstract_platform_specific_interface import QAbstractPlatformSpecificInterface
  from ._q_audio_format import QAudioFormat
  from ._q_media_input_encoder_interface import QMediaInputEncoderInterface
  from ._q_media_recorder_private import QMediaRecorderPrivate
  from ._q_media_time_range import QMediaTimeRange
  from ._q_platform_audio_resampler import QPlatformAudioResampler
  from ._symbols_resolver import SymbolsResolver
  from ._video_transformation import VideoTransformation
  from ._q_audio_buffer import QAudioBuffer
  from ._q_audio_buffer_output import QAudioBufferOutput
  from ._q_audio_buffer_source import QAudioBufferSource
  from ._q_audio_decoder import QAudioDecoder
  from ._q_audio_device import QAudioDevice
  from ._q_audio_device_private import QAudioDevicePrivate
  from ._q_camera_device import QCameraDevice
  from ._q_camera_device_private import QCameraDevicePrivate
  from ._q_camera_format import QCameraFormat
  from ._q_camera_format_private import QCameraFormatPrivate
  from ._q_media_devices import QMediaDevices
  from ._q_media_format import QMediaFormat
  from ._q_media_meta_data import QMediaMetaData
  from ._q_platform_media_plugin import QPlatformMediaPlugin
  from ._q_playback_options import QPlaybackOptions
  from ._q_sample import QSample
  from ._q_sample_cache import QSampleCache
  from ._q_video_output_orientation_handler import QVideoOutputOrientationHandler
  from ._q_wave_decoder import QWaveDecoder
  from ._q_alsa_audio_device_info import QAlsaAudioDeviceInfo
  from ._q_android_audio_device import QAndroidAudioDevice
  from ._q_audio_decoder_private import QAudioDecoderPrivate
  from ._q_audio_device_private_all_members_equal import QAudioDevicePrivateAllMembersEqual
  from ._q_audio_input import QAudioInput
  from ._q_audio_output import QAudioOutput
  from ._q_audio_sink import QAudioSink
  from ._q_audio_source import QAudioSource
  from ._q_camera_private import QCameraPrivate
  from ._q_core_audio_device_info import QCoreAudioDeviceInfo
  from ._q_ohos_audio_device import QOhosAudioDevice
  from ._q_platform_audio_buffer_input import QPlatformAudioBufferInput
  from ._q_platform_audio_decoder import QPlatformAudioDecoder
  from ._q_platform_audio_devices import QPlatformAudioDevices
  from ._q_platform_audio_endpoint_base import QPlatformAudioEndpointBase
  from ._q_platform_media_format_info import QPlatformMediaFormatInfo
  from ._q_pulse_audio_device_private import QPulseAudioDevicePrivate
  from ._q_qnx_snd_audio_device_info import QQnxSndAudioDeviceInfo
  from ._q_sound_effect import QSoundEffect
  from ._q_wasm_audio_device import QWasmAudioDevice
  from ._qnx_audio_device_info import QnxAudioDeviceInfo
  from ._q_alsa_audio_devices import QAlsaAudioDevices
  from ._q_android_audio_devices import QAndroidAudioDevices
  from ._q_core_audio_devices import QCoreAudioDevices
  from ._q_dr_wav_audio_decoder import QDrWavAudioDecoder
  from ._q_platform_audio_input import QPlatformAudioInput
  from ._q_platform_audio_output import QPlatformAudioOutput
  from ._q_platform_audio_sink import QPlatformAudioSink
  from ._q_platform_audio_source import QPlatformAudioSource
  from ._q_pulse_audio_devices import QPulseAudioDevices
  from ._q_qnx_audio_devices import QQnxAudioDevices
  from ._q_qnx_snd_audio_devices import QQnxSndAudioDevices
  from ._q_sound_effect_private import QSoundEffectPrivate
  from ._q_abstract_video_buffer import QAbstractVideoBuffer
  from ._q_video_frame import QVideoFrame
  from ._q_video_frame_format import QVideoFrameFormat
  from ._q_sound_effect_private_synchronous import QSoundEffectPrivateSynchronous
  from ._q_image_video_buffer import QImageVideoBuffer
  from ._q_memory_video_buffer import QMemoryVideoBuffer
  from ._q_video_frame_private import QVideoFramePrivate
  from ._q_video_frame_textures import QVideoFrameTextures
  from ._q_capturable_window import QCapturableWindow
  from ._q_capturable_window_private import QCapturableWindowPrivate
  from ._q_video_window import QVideoWindow
  from ._q_platform_capturable_windows import QPlatformCapturableWindows
  from ._q_rhi_callback import QRhiCallback
  from ._q_video_frame_texture_pool import QVideoFrameTexturePool
  from ._q_video_frame_textures_handles import QVideoFrameTexturesHandles
  from ._q_video_sink import QVideoSink
  from ._q_video_window_private import QVideoWindowPrivate
  from ._q_audio_buffer_input import QAudioBufferInput
  from ._q_camera import QCamera
  from ._q_image_capture import QImageCapture
  from ._q_media_capture_session import QMediaCaptureSession
  from ._q_media_recorder import QMediaRecorder
  from ._q_screen_capture import QScreenCapture
  from ._q_video_frame_input import QVideoFrameInput
  from ._q_window_capture import QWindowCapture
  from ._q_hw_video_buffer import QHwVideoBuffer
  from ._q_media_player import QMediaPlayer
  from ._q_platform_video_sink import QPlatformVideoSink
  from ._q_audio_buffer_output_private import QAudioBufferOutputPrivate
  from ._q_g_streamer_interface import QGStreamerInterface
  from ._q_g_streamer_video_source import QGStreamerVideoSource
  from ._q_image_encoder_settings import QImageEncoderSettings
  from ._q_media_capture_session_private import QMediaCaptureSessionPrivate
  from ._q_media_encoder_settings import QMediaEncoderSettings
  from ._q_media_frame_input_private import QMediaFrameInputPrivate
  from ._q_platform_media_player import QPlatformMediaPlayer
  from ._q_window_capture_private import QWindowCapturePrivate
  from ._q_g_streamer_video_source_private import QGStreamerVideoSourcePrivate
  from ._q_media_player_private import QMediaPlayerPrivate
  from ._q_platform_media_integration import QPlatformMediaIntegration
  from ._q_platform_media_recorder import QPlatformMediaRecorder
  from ._q_platform_media_capture_session import QPlatformMediaCaptureSession
  from ._q_platform_video_source import QPlatformVideoSource
  from ._q_platform_surface_capture import QPlatformSurfaceCapture
  from ._q_platform_video_frame_input import QPlatformVideoFrameInput
  from ._q_platform_video_devices import QPlatformVideoDevices
  from ._q_surface_capture_grabber import QSurfaceCaptureGrabber
  from . import QAudio
  from . import QAudioHelperInternal
  from . import QMultimediaPrivate
  from . import QVideoTextureHelper
  from . import QtMultimediaPrivate
  from . import QtPipeWire
  from . import QtPrivate
  from . import QtVideo
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'Fraction': '_fraction',
      'QAbstractPlatformSpecificInterface': '_q_abstract_platform_specific_interface',
      'QAudioFormat': '_q_audio_format',
      'QMediaInputEncoderInterface': '_q_media_input_encoder_interface',
      'QMediaRecorderPrivate': '_q_media_recorder_private',
      'QMediaTimeRange': '_q_media_time_range',
      'QPlatformAudioResampler': '_q_platform_audio_resampler',
      'SymbolsResolver': '_symbols_resolver',
      'VideoTransformation': '_video_transformation',
      'QAudioBuffer': '_q_audio_buffer',
      'QAudioBufferOutput': '_q_audio_buffer_output',
      'QAudioBufferSource': '_q_audio_buffer_source',
      'QAudioDecoder': '_q_audio_decoder',
      'QAudioDevice': '_q_audio_device',
      'QAudioDevicePrivate': '_q_audio_device_private',
      'QCameraDevice': '_q_camera_device',
      'QCameraDevicePrivate': '_q_camera_device_private',
      'QCameraFormat': '_q_camera_format',
      'QCameraFormatPrivate': '_q_camera_format_private',
      'QMediaDevices': '_q_media_devices',
      'QMediaFormat': '_q_media_format',
      'QMediaMetaData': '_q_media_meta_data',
      'QPlatformMediaPlugin': '_q_platform_media_plugin',
      'QPlaybackOptions': '_q_playback_options',
      'QSample': '_q_sample',
      'QSampleCache': '_q_sample_cache',
      'QVideoOutputOrientationHandler': '_q_video_output_orientation_handler',
      'QWaveDecoder': '_q_wave_decoder',
      'QAlsaAudioDeviceInfo': '_q_alsa_audio_device_info',
      'QAndroidAudioDevice': '_q_android_audio_device',
      'QAudioDecoderPrivate': '_q_audio_decoder_private',
      'QAudioDevicePrivateAllMembersEqual': '_q_audio_device_private_all_members_equal',
      'QAudioInput': '_q_audio_input',
      'QAudioOutput': '_q_audio_output',
      'QAudioSink': '_q_audio_sink',
      'QAudioSource': '_q_audio_source',
      'QCameraPrivate': '_q_camera_private',
      'QCoreAudioDeviceInfo': '_q_core_audio_device_info',
      'QOhosAudioDevice': '_q_ohos_audio_device',
      'QPlatformAudioBufferInput': '_q_platform_audio_buffer_input',
      'QPlatformAudioDecoder': '_q_platform_audio_decoder',
      'QPlatformAudioDevices': '_q_platform_audio_devices',
      'QPlatformAudioEndpointBase': '_q_platform_audio_endpoint_base',
      'QPlatformMediaFormatInfo': '_q_platform_media_format_info',
      'QPulseAudioDevicePrivate': '_q_pulse_audio_device_private',
      'QQnxSndAudioDeviceInfo': '_q_qnx_snd_audio_device_info',
      'QSoundEffect': '_q_sound_effect',
      'QWasmAudioDevice': '_q_wasm_audio_device',
      'QnxAudioDeviceInfo': '_qnx_audio_device_info',
      'QAlsaAudioDevices': '_q_alsa_audio_devices',
      'QAndroidAudioDevices': '_q_android_audio_devices',
      'QCoreAudioDevices': '_q_core_audio_devices',
      'QDrWavAudioDecoder': '_q_dr_wav_audio_decoder',
      'QPlatformAudioInput': '_q_platform_audio_input',
      'QPlatformAudioOutput': '_q_platform_audio_output',
      'QPlatformAudioSink': '_q_platform_audio_sink',
      'QPlatformAudioSource': '_q_platform_audio_source',
      'QPulseAudioDevices': '_q_pulse_audio_devices',
      'QQnxAudioDevices': '_q_qnx_audio_devices',
      'QQnxSndAudioDevices': '_q_qnx_snd_audio_devices',
      'QSoundEffectPrivate': '_q_sound_effect_private',
      'QAbstractVideoBuffer': '_q_abstract_video_buffer',
      'QVideoFrame': '_q_video_frame',
      'QVideoFrameFormat': '_q_video_frame_format',
      'QSoundEffectPrivateSynchronous': '_q_sound_effect_private_synchronous',
      'QImageVideoBuffer': '_q_image_video_buffer',
      'QMemoryVideoBuffer': '_q_memory_video_buffer',
      'QVideoFramePrivate': '_q_video_frame_private',
      'QVideoFrameTextures': '_q_video_frame_textures',
      'QCapturableWindow': '_q_capturable_window',
      'QCapturableWindowPrivate': '_q_capturable_window_private',
      'QVideoWindow': '_q_video_window',
      'QPlatformCapturableWindows': '_q_platform_capturable_windows',
      'QRhiCallback': '_q_rhi_callback',
      'QVideoFrameTexturePool': '_q_video_frame_texture_pool',
      'QVideoFrameTexturesHandles': '_q_video_frame_textures_handles',
      'QVideoSink': '_q_video_sink',
      'QVideoWindowPrivate': '_q_video_window_private',
      'QAudioBufferInput': '_q_audio_buffer_input',
      'QCamera': '_q_camera',
      'QImageCapture': '_q_image_capture',
      'QMediaCaptureSession': '_q_media_capture_session',
      'QMediaRecorder': '_q_media_recorder',
      'QScreenCapture': '_q_screen_capture',
      'QVideoFrameInput': '_q_video_frame_input',
      'QWindowCapture': '_q_window_capture',
      'QHwVideoBuffer': '_q_hw_video_buffer',
      'QMediaPlayer': '_q_media_player',
      'QPlatformVideoSink': '_q_platform_video_sink',
      'QAudioBufferOutputPrivate': '_q_audio_buffer_output_private',
      'QGStreamerInterface': '_q_g_streamer_interface',
      'QGStreamerVideoSource': '_q_g_streamer_video_source',
      'QImageEncoderSettings': '_q_image_encoder_settings',
      'QMediaCaptureSessionPrivate': '_q_media_capture_session_private',
      'QMediaEncoderSettings': '_q_media_encoder_settings',
      'QMediaFrameInputPrivate': '_q_media_frame_input_private',
      'QPlatformMediaPlayer': '_q_platform_media_player',
      'QWindowCapturePrivate': '_q_window_capture_private',
      'QGStreamerVideoSourcePrivate': '_q_g_streamer_video_source_private',
      'QMediaPlayerPrivate': '_q_media_player_private',
      'QPlatformMediaIntegration': '_q_platform_media_integration',
      'QPlatformMediaRecorder': '_q_platform_media_recorder',
      'QPlatformMediaCaptureSession': '_q_platform_media_capture_session',
      'QPlatformVideoSource': '_q_platform_video_source',
      'QPlatformSurfaceCapture': '_q_platform_surface_capture',
      'QPlatformVideoFrameInput': '_q_platform_video_frame_input',
      'QPlatformVideoDevices': '_q_platform_video_devices',
      'QSurfaceCaptureGrabber': '_q_surface_capture_grabber',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QAudio', 'QAudioHelperInternal', 'QMultimediaPrivate', 'QVideoTextureHelper', 'QtMultimediaPrivate', 'QtPipeWire', 'QtPrivate', 'QtVideo',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtMultimedia import QSurfaceCaptureGrabber'. Python calls
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
