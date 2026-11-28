"""
QRtAudioEngine stands in for the class 'QtMultimediaPrivate::QRtAudioEngine'
of Qt, which has no cute class yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::QRtAudioEngine to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from ..cute import UnsupportedMeta


class QRtAudioEngine(metaclass=UnsupportedMeta):
  """
  Qt's class 'QtMultimediaPrivate::QRtAudioEngine' of QtMultimedia: writing
  its cute class raised ValueError: No name of a function of
  'QtMultimediaPrivate::QRtAudioEngine' can be read from 'void (QSpan<float>)
  noexcept __attribute__
  QtMultimediaPrivate::QRtAudioEngine::audioCallback(QSpan<float> a0)'.
  """

  #  The class of Qt this class stands in for.
  __qt_class__ = 'QtMultimediaPrivate::QRtAudioEngine'
