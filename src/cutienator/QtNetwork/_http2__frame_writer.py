"""
Http2::FrameWriter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/http2frames_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Http2::FrameWriter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Http2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArrayView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']


class FrameWriter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Http2::FrameWriter: a plain Python object standing in
  front of one C++ Http2::FrameWriter.

  C++ hands a Http2::FrameWriter around as a copy, so every C++
  Http2::FrameWriter behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Http2::FrameWriter that has a ritual and that Python
  can call so far, 7 names in all: 'start', 'setPayloadSize', 'setType',
  'setFlags', 'addFlag', 'append', 'updatePayloadSize'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Frame &Http2::FrameWriter::outboundFrame()': gives a type Python
    has no way to take yet.
  - Qt's 'void Http2::FrameWriter::setOutboundFrame(Frame &&newFrame)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void Http2::FrameWriter::append(const payload_type &payload)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void Http2::FrameWriter::append(const uchar *begin, const uchar
    *end)': names 'uchar', which has no cute class yet.
  - Qt's 'bool Http2::FrameWriter::write(QIODevice &socket) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool Http2::FrameWriter::writeHEADERS(QIODevice &socket, quint32
    sizeLimit)': takes a type Python has no way to hand over yet.
  - Qt's 'bool Http2::FrameWriter::writeDATA(QIODevice &socket, quint32
    sizeLimit, const uchar *src, quint32 size)': takes a type Python has no
    way to hand over yet.
  - Qt's 'Http2::FrameWriter::~FrameWriter()': the destructor: Python removes
    its C++ Http2::FrameWriter by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 20 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ Http2::FrameWriter is created at the first use, not by
    'Http2::FrameWriter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Http2::FrameWriter back gives a copy the ritual made
    for Python, in a new cute Http2::FrameWriter.
  - Each name of Qt's Http2::FrameWriter that has no cute function yet,
    'outboundFrame', 'setOutboundFrame', 'write', 'writeDATA',
    'writeHEADERS', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Http2::FrameWriter'

  #  Qt's '~Http2::FrameWriter()'. Naming it makes this a value class: Python
  #  owns every C++ Http2::FrameWriter behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN5Http211FrameWriterD1Ev'

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

  @overload(int)
  def setPayloadSize(self, size: int) -> None:
    """
    Calls Qt's 'void Http2::FrameWriter::setPayloadSize(quint32 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/http2-framewriter.html#setPayloadSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void Http2::FrameWriter::setPayloadSize(quint32 size)
    self.uglySide.call(
        'ritual_ZN5Http211FrameWriter14setPayloadSizeEj', size,
    )

  @overload(Http2.FrameType)
  def setType(self, type: Http2.FrameType) -> None:
    """
    Calls Qt's 'void Http2::FrameWriter::setType(FrameType type)'.

    Qt's own words: https://doc.qt.io/qt-6/http2-framewriter.html#setType

    Parameters
    ----------

    type : Http2.FrameType
      Passed on as its number.
    """
    #  void Http2::FrameWriter::setType(FrameType type)
    self.uglySide.call(
        'ritual_ZN5Http211FrameWriter7setTypeENS_9FrameTypeE', type.value,
    )

  @overload(Http2.FrameFlags)
  def setFlags(self, flags: Http2.FrameFlags) -> None:
    """
    Calls Qt's 'void Http2::FrameWriter::setFlags(FrameFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/http2-framewriter.html#setFlags

    Parameters
    ----------

    flags : Http2.FrameFlags
      Passed on as its number.
    """
    #  void Http2::FrameWriter::setFlags(FrameFlags flags)
    self.uglySide.call(
        'ritual_ZN5Http211FrameWriter8setFlagsE6QFlagsINS_9FrameFlagEE',
        flags.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'Http2::FrameWriter::FrameWriter()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/http2-framewriter.html#FrameWriter
    """
    #  Http2::FrameWriter::FrameWriter()
    self._noteCreation(FrameWriter, lambda: Rituals.call(
        'ritual_ZN5Http211FrameWriterC1Ev',
    ))

  @overload(Http2.FrameType, Http2.FrameFlags, int)
  def __init__(
      self,
      type: Http2.FrameType,
      flags: Http2.FrameFlags,
      streamID: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'Http2::FrameWriter::FrameWriter(FrameType
    type, FrameFlags flags, quint32 streamID)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/http2-framewriter.html#FrameWriter

    Parameters
    ----------

    type : Http2.FrameType
      Passed on as its number.

    flags : Http2.FrameFlags
      Passed on as its number.

    streamID : int
      Passed on as it is.
    """
    #  Http2::FrameWriter::FrameWriter(FrameType type, FrameFlags flags,
    #      quint32 streamID)
    self._noteCreation(FrameWriter, lambda: Rituals.call(
        'ritual_ZN5Http211FrameWriterC1ENS_9FrameTypeE6QFlagsINS_9FrameFlag'
        'EEj',
        type.value, flags.value, streamID,
    ))

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

  @overload(Http2.FrameType, Http2.FrameFlags, int)
  def start(
      self,
      type: Http2.FrameType,
      flags: Http2.FrameFlags,
      streamID: int,
  ) -> None:
    """
    Calls Qt's 'void Http2::FrameWriter::start(FrameType type, FrameFlags
    flags, quint32 streamID)'.

    Qt's own words: https://doc.qt.io/qt-6/http2-framewriter.html#start

    Parameters
    ----------

    type : Http2.FrameType
      Passed on as its number.

    flags : Http2.FrameFlags
      Passed on as its number.

    streamID : int
      Passed on as it is.
    """
    #  void Http2::FrameWriter::start(FrameType type, FrameFlags flags,
    #      quint32 streamID)
    self.uglySide.call(
        'ritual_ZN5Http211FrameWriter5startENS_9FrameTypeE6QFlagsINS_9Frame'
        'FlagEEj',
        type.value, flags.value, streamID,
    )

  @overload(Http2.FrameFlag)
  def addFlag(self, flag: Http2.FrameFlag) -> None:
    """
    Calls Qt's 'void Http2::FrameWriter::addFlag(FrameFlag flag)'.

    Qt's own words: https://doc.qt.io/qt-6/http2-framewriter.html#addFlag

    Parameters
    ----------

    flag : Http2.FrameFlag
      Passed on as its number.
    """
    #  void Http2::FrameWriter::addFlag(FrameFlag flag)
    self.uglySide.call(
        'ritual_ZN5Http211FrameWriter7addFlagENS_9FrameFlagE', flag.value,
    )

  @overload(int)
  def append(self, val: int) -> None:
    """
    Calls Qt's 'void Http2::FrameWriter::append(uchar val)'.

    Qt's own words: https://doc.qt.io/qt-6/http2-framewriter.html#append

    Parameters
    ----------

    val : int
      Passed on as it is.
    """
    #  void Http2::FrameWriter::append(uchar val)
    self.uglySide.call('ritual_ZN5Http211FrameWriter6appendEh', val)

  @overload(Http2.Settings)
  def append(self, identifier: Http2.Settings) -> None:
    """
    Calls Qt's 'void Http2::FrameWriter::append(Settings identifier)'.

    Qt's own words: https://doc.qt.io/qt-6/http2-framewriter.html#append

    Parameters
    ----------

    identifier : Http2.Settings
      Passed on as its number.
    """
    #  void Http2::FrameWriter::append(Settings identifier)
    self.uglySide.call(
        'ritual_ZN5Http211FrameWriter6appendENS_8SettingsE',
        identifier.value,
    )

  @overload(QByteArrayView)
  def append(self, payload: QByteArrayView) -> None:
    """
    Calls Qt's 'void Http2::FrameWriter::append(QByteArrayView payload)'.

    Qt's own words: https://doc.qt.io/qt-6/http2-framewriter.html#append

    Parameters
    ----------

    payload : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  void Http2::FrameWriter::append(QByteArrayView payload)
    self.uglySide.call(
        'ritual_ZN5Http211FrameWriter6appendE14QByteArrayView',
        self._valueOf(payload),
    )

  def updatePayloadSize(self) -> None:
    """
    Calls Qt's 'void Http2::FrameWriter::updatePayloadSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/http2-framewriter.html#updatePayloadSize
    """
    #  void Http2::FrameWriter::updatePayloadSize()
    self.uglySide.call('ritual_ZN5Http211FrameWriter17updatePayloadSizeEv')

  @staticmethod
  def outboundFrame(*__, **_) -> Never:
    """
    Qt's 'Frame &Http2::FrameWriter::outboundFrame()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'Http2.FrameWriter.outboundFrame' has no cute function yet. Qt's "
        "'Frame &Http2::FrameWriter::outboundFrame()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setOutboundFrame(*__, **_) -> Never:
    """
    Qt's 'void Http2::FrameWriter::setOutboundFrame(Frame &&newFrame)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Http2.FrameWriter.setOutboundFrame' has no cute function yet. "
        "Qt's 'void Http2::FrameWriter::setOutboundFrame(Frame "
        "&&newFrame)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'bool Http2::FrameWriter::write(QIODevice &socket) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Http2.FrameWriter.write' has no cute function yet. Qt's 'bool "
        "Http2::FrameWriter::write(QIODevice &socket) const': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def writeDATA(*__, **_) -> Never:
    """
    Qt's 'bool Http2::FrameWriter::writeDATA(QIODevice &socket, quint32
    sizeLimit, const uchar *src, quint32 size)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'Http2.FrameWriter.writeDATA' has no cute function yet. Qt's 'bool "
        "Http2::FrameWriter::writeDATA(QIODevice &socket, quint32 "
        "sizeLimit, const uchar *src, quint32 size)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def writeHEADERS(*__, **_) -> Never:
    """
    Qt's 'bool Http2::FrameWriter::writeHEADERS(QIODevice &socket, quint32
    sizeLimit)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Http2.FrameWriter.writeHEADERS' has no cute function yet. Qt's "
        "'bool Http2::FrameWriter::writeHEADERS(QIODevice &socket, quint32 "
        "sizeLimit)': takes a type Python has no way to hand over yet.")
