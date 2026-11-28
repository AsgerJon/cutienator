"""
QPlatformAudioSourceStream stands in for the class
'QtMultimediaPrivate::QPlatformAudioSourceStream' of Qt, which has no cute
class yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_platform_stream_support_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::QPlatformAudioSourceStream to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from ..cute import UnsupportedMeta


class QPlatformAudioSourceStream(metaclass=UnsupportedMeta):
  """
  Qt's class 'QtMultimediaPrivate::QPlatformAudioSourceStream' of
  QtMultimedia: writing its cute class raised ValueError: No name of a
  function of 'QtMultimediaPrivate::QPlatformAudioSourceStream' can be read
  from 'uint64_t (QSpan<const std::byte>, qsizetype,
  std::optional<NativeSampleFormat>) noexcept __attribute__
  QtMultimediaPrivate::QPlatformAudioSourceStream::process(QSpan<const
  std::byte> hostBuffer, qsizetype numberOfFrames,
  std::optional<NativeSampleFormat> a2)'.
  """

  #  The class of Qt this class stands in for.
  __qt_class__ = 'QtMultimediaPrivate::QPlatformAudioSourceStream'
