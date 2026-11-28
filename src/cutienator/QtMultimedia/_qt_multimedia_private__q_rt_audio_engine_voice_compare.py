"""
QtMultimediaPrivate::QRtAudioEngineVoiceCompare binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::QRtAudioEngineVoiceCompare to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QRtAudioEngineVoiceCompare(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMultimediaPrivate::QRtAudioEngineVoiceCompare: a
  plain Python object standing in front of one C++
  QtMultimediaPrivate::QRtAudioEngineVoiceCompare.

  C++ hands a QtMultimediaPrivate::QRtAudioEngineVoiceCompare around as a
  copy, so every C++ QtMultimediaPrivate::QRtAudioEngineVoiceCompare behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QtMultimediaPrivate::QRtAudioEngineVoiceCompare yet.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'uint64_t
    QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(const
    QRtAudioEngineVoice &arg)': takes a type Python has no way to hand over
    yet.
  - Qt's 'uint64_t
    QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(const
    std::shared_ptr<QRtAudioEngineVoice> &arg)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QtMultimediaPrivate::QRtAudioEngineVoiceCompare::
    ~QRtAudioEngineVoiceCompare()': the destructor: Python removes its C++
    QtMultimediaPrivate::QRtAudioEngineVoiceCompare by it, and has no other
    use for it.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 a template; 1 takes or gives a number
  that is not equally wide on every system.

  What to expect
  --------------

  - The C++ QtMultimediaPrivate::QRtAudioEngineVoiceCompare is created at the
    first use, not by 'QtMultimediaPrivate::QRtAudioEngineVoiceCompare(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtMultimediaPrivate::QRtAudioEngineVoiceCompare back
    gives a copy the ritual made for Python, in a new cute
    QtMultimediaPrivate::QRtAudioEngineVoiceCompare.
  - Each name of Qt's QtMultimediaPrivate::QRtAudioEngineVoiceCompare that
    has no cute function yet, 'getId', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMultimediaPrivate::QRtAudioEngineVoiceCompare'

  #  Qt's '~QtMultimediaPrivate::QRtAudioEngineVoiceCompare()'. Naming it
  #  makes this a value class: Python owns every C++
  #  QtMultimediaPrivate::QRtAudioEngineVoiceCompare behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN19QtMultimediaPrivate26QRtAudioEngineVoiceCompareD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getId(*__, **_) -> Never:
    """
    - Qt's 'uint64_t
      QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(const
      QRtAudioEngineVoice &arg)': takes a type Python has no way to hand over
      yet.
    - Qt's 'uint64_t
      QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(const
      std::shared_ptr<QRtAudioEngineVoice> &arg)': takes a type Python has no
      way to hand over yet.
    - Qt's 'uint64_t
      QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(VoiceId arg)':
      takes or gives a number that is not equally wide on every system:
      QtMultimediaPrivate::VoiceId.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QRtAudioEngineVoiceCompare.getId' has no cute "
        "function yet. Qt's 'uint64_t "
        "QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(const "
        "QRtAudioEngineVoice &arg)': takes a type Python has no way to hand "
        "over yet. Qt's 'uint64_t "
        "QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(const "
        "std::shared_ptr<QRtAudioEngineVoice> &arg)': takes a type Python "
        "has no way to hand over yet. Qt's 'uint64_t "
        "QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(VoiceId "
        "arg)': takes or gives a number that is not equally wide on every "
        "system: QtMultimediaPrivate::VoiceId.")
