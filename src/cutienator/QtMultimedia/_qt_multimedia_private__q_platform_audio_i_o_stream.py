"""
QtMultimediaPrivate::QPlatformAudioIOStream binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_platform_stream_support_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtMultimediaPrivate::QPlatformAudioIOStream to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QPlatformAudioIOStream(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtMultimediaPrivate::QPlatformAudioIOStream: a plain
  Python object standing in front of one C++
  QtMultimediaPrivate::QPlatformAudioIOStream.

  What exists
  -----------

  Every function of Qt's QtMultimediaPrivate::QPlatformAudioIOStream that has
  a ritual and that Python can call so far, 4 names in all: 'setVolume',
  'volume', 'ringbufferSizeInBytes', 'requestStop'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qsizetype
    QtMultimediaPrivate::QPlatformAudioIOStream::inferRingbufferFrames(const
    std::optional<int> &ringbufferSize, const
    std::optional<NativePeriodFrames> &nativePeriodFrames, const QAudioFormat
    &a2)': takes a type Python has no way to hand over yet.
  - Qt's 'qsizetype
    QtMultimediaPrivate::QPlatformAudioIOStream::inferRingbufferBytes(const
    std::optional<int> &ringbufferSize, const
    std::optional<NativePeriodFrames> &nativePeriodFrames, const QAudioFormat
    &a2)': takes a type Python has no way to hand over yet.
  - Qt's
    'QtMultimediaPrivate::QPlatformAudioIOStream::QPlatformAudioIOStream(
    QAudioDevice m_audioDevice, QAudioFormat m_format, std::optional<int>
    ringbufferSize, std::optional<NativePeriodFrames> nativePeriodFrames,
    float volume)': takes a type Python has no way to hand over yet.
  - Qt's
    'QtMultimediaPrivate::QPlatformAudioIOStream::~QPlatformAudioIOStream()':
    the destructor: Python never removes a C++
    QtMultimediaPrivate::QPlatformAudioIOStream.
  - Qt's 'void
    QtMultimediaPrivate::QPlatformAudioIOStream::prepareRingbuffer(std::
    optional<int> ringbufferSize)': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool
    QtMultimediaPrivate::QPlatformAudioIOStream::isStopRequested(std::
    memory_order memory_order) const': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  6 of the 16 functions Qt declares: 4 forbidden; 2 a template.

  What to expect
  --------------

  - The C++ QtMultimediaPrivate::QPlatformAudioIOStream is created at the
    first use, not by 'QtMultimediaPrivate::QPlatformAudioIOStream(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtMultimediaPrivate::QPlatformAudioIOStream.
  - Each name of Qt's QtMultimediaPrivate::QPlatformAudioIOStream that has no
    cute function yet, '__init__', 'inferRingbufferBytes',
    'inferRingbufferFrames', 'isStopRequested', 'prepareRingbuffer',
    'visitRingbuffer', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QtMultimediaPrivate::QPlatformAudioIOStream,
  #  each a class in here as in C++, and the names Qt has for the
  #  combinations of its flags enums.

  class ShutdownPolicy(CuteNum, scoped=True):
    """
    The enum 'QtMultimediaPrivate::QPlatformAudioIOStream::ShutdownPolicy' of
    Qt, with the 2 names Qt gives in it. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    DrainRingbuffer = Kee[int](0)
    DiscardRingbuffer = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtMultimediaPrivate::QPlatformAudioIOStream'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def volume(self) -> float:
    """
    Calls Qt's 'float QtMultimediaPrivate::QPlatformAudioIOStream::volume()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qplatformaudioiostream.html
    """
    #  float QtMultimediaPrivate::QPlatformAudioIOStream::volume() const
    return self.uglySide.call(
        'ritual_ZNK19QtMultimediaPrivate22QPlatformAudioIOStream6volumeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setVolume(self, a0: float) -> None:
    """
    Calls Qt's 'void
    QtMultimediaPrivate::QPlatformAudioIOStream::setVolume(float a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qplatformaudioiostream.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QtMultimediaPrivate::QPlatformAudioIOStream::setVolume(float a0)
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStream9setVolumeEf',
        a0,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QtMultimediaPrivate::QPlatformAudioIOStream::QPlatformAudioIOStream(
    QAudioDevice m_audioDevice, QAudioFormat m_format, std::optional<int>
    ringbufferSize, std::optional<NativePeriodFrames> nativePeriodFrames,
    float volume)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QPlatformAudioIOStream.__init__' has no cute "
        "function yet. Qt's "
        "'QtMultimediaPrivate::QPlatformAudioIOStream::QPlatformAudioIOStrea"
        "m(QAudioDevice m_audioDevice, QAudioFormat m_format, "
        "std::optional<int> ringbufferSize, "
        "std::optional<NativePeriodFrames> nativePeriodFrames, float "
        "volume)': takes a type Python has no way to hand over yet.")

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

  def ringbufferSizeInBytes(self) -> int:
    """
    Calls Qt's 'int
    QtMultimediaPrivate::QPlatformAudioIOStream::ringbufferSizeInBytes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qplatformaudioiostream.html
    """
    #  int QtMultimediaPrivate::QPlatformAudioIOStream::
    #      ringbufferSizeInBytes()
    return self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStream21ringbuffer'
        'SizeInBytesEv',
    )

  def requestStop(self) -> None:
    """
    Calls Qt's 'void
    QtMultimediaPrivate::QPlatformAudioIOStream::requestStop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtmultimediaprivate-qplatformaudioiostream.html
    """
    #  void QtMultimediaPrivate::QPlatformAudioIOStream::requestStop()
    self.uglySide.call(
        'ritual_ZN19QtMultimediaPrivate22QPlatformAudioIOStream11requestSto'
        'pEv',
    )

  @staticmethod
  def inferRingbufferBytes(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QtMultimediaPrivate::QPlatformAudioIOStream::inferRingbufferBytes(const
    std::optional<int> &ringbufferSize, const
    std::optional<NativePeriodFrames> &nativePeriodFrames, const QAudioFormat
    &a2)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QPlatformAudioIOStream.inferRingbufferBytes' "
        "has no cute function yet. Qt's 'qsizetype "
        "QtMultimediaPrivate::QPlatformAudioIOStream::inferRingbufferBytes(c"
        "onst std::optional<int> &ringbufferSize, const "
        "std::optional<NativePeriodFrames> &nativePeriodFrames, const "
        "QAudioFormat &a2)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def inferRingbufferFrames(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QtMultimediaPrivate::QPlatformAudioIOStream::inferRingbufferFrames(const
    std::optional<int> &ringbufferSize, const
    std::optional<NativePeriodFrames> &nativePeriodFrames, const QAudioFormat
    &a2)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QPlatformAudioIOStream.inferRingbufferFrames' "
        "has no cute function yet. Qt's 'qsizetype "
        "QtMultimediaPrivate::QPlatformAudioIOStream::inferRingbufferFrames("
        "const std::optional<int> &ringbufferSize, const "
        "std::optional<NativePeriodFrames> &nativePeriodFrames, const "
        "QAudioFormat &a2)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def isStopRequested(*__, **_) -> Never:
    """
    Qt's 'bool
    QtMultimediaPrivate::QPlatformAudioIOStream::isStopRequested(std::
    memory_order memory_order) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QPlatformAudioIOStream.isStopRequested' has "
        "no cute function yet. Qt's 'bool "
        "QtMultimediaPrivate::QPlatformAudioIOStream::isStopRequested(std::m"
        "emory_order memory_order) const': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def prepareRingbuffer(*__, **_) -> Never:
    """
    Qt's 'void
    QtMultimediaPrivate::QPlatformAudioIOStream::prepareRingbuffer(std::
    optional<int> ringbufferSize)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QPlatformAudioIOStream.prepareRingbuffer' has "
        "no cute function yet. Qt's 'void "
        "QtMultimediaPrivate::QPlatformAudioIOStream::prepareRingbuffer(std:"
        ":optional<int> ringbufferSize)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def visitRingbuffer(*__, **_) -> Never:
    """
    Qt's 'QtMultimediaPrivate::QPlatformAudioIOStream::visitRingbuffer': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QtMultimediaPrivate.QPlatformAudioIOStream.visitRingbuffer' has "
        "no cute function yet. Qt's "
        "'QtMultimediaPrivate::QPlatformAudioIOStream::visitRingbuffer': a "
        "template: a pattern and no single function.")
