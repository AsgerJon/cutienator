"""
Http2::Frame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/http2frames_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Http2::Frame to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import Http2

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Frame(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Http2::Frame: a plain Python object standing in front
  of one C++ Http2::Frame.

  C++ hands a Http2::Frame around as a copy, so every C++ Http2::Frame behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Http2::Frame that has a ritual and that Python can
  call so far, 11 names in all: 'type', 'streamID', 'flags', 'payloadSize',
  'padding', 'supportsPaddedFlag', 'isPadded', 'validateHeader',
  'validatePayload', 'dataSize', 'hpackBlockSize'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool Http2::Frame::priority(quint32 *streamID, uchar *weight)
    const': takes a number to change where it is.
  - Qt's 'const uchar *Http2::Frame::dataBegin() const': gives 'unsigned
    char', which has no cute class yet.
  - Qt's 'const uchar *Http2::Frame::hpackBlockBegin() const': gives
    'unsigned char', which has no cute class yet.
  - Qt's 'Http2::Frame::~Frame()': the destructor: Python removes its C++
    Http2::Frame by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Http2::Frame is created at the first use, not by
    'Http2::Frame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Http2::Frame back gives a copy the ritual made for
    Python, in a new cute Http2::Frame.
  - Each name of Qt's Http2::Frame that has no cute function yet,
    'dataBegin', 'hpackBlockBegin', 'priority', holds a function that raises
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
  __qt_class__ = 'Http2::Frame'

  #  Qt's '~Http2::Frame()'. Naming it makes this a value class: Python owns
  #  every C++ Http2::Frame behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5Http25FrameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Http2.FrameType:
    """
    Calls Qt's 'FrameType Http2::Frame::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#type

    Returns
    -------

    Http2.FrameType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Http2.FrameType(number)'
      gives.
    """
    #  FrameType Http2::Frame::type() const
    return Http2.FrameType(self.uglySide.call(
        'ritual_ZNK5Http25Frame4typeEv',
    ))

  def streamID(self) -> int:
    """
    Calls Qt's 'quint32 Http2::Frame::streamID() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#streamID
    """
    #  quint32 Http2::Frame::streamID() const
    return self.uglySide.call('ritual_ZNK5Http25Frame8streamIDEv')

  def flags(self) -> Http2.FrameFlags:
    """
    Calls Qt's 'FrameFlags Http2::Frame::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#flags

    Returns
    -------

    Http2.FrameFlags
      The value standing for the combination Qt gave back.
    """
    #  FrameFlags Http2::Frame::flags() const
    return Http2.FrameFlags(self.uglySide.call(
        'ritual_ZNK5Http25Frame5flagsEv',
    ))

  def payloadSize(self) -> int:
    """
    Calls Qt's 'quint32 Http2::Frame::payloadSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#payloadSize
    """
    #  quint32 Http2::Frame::payloadSize() const
    return self.uglySide.call('ritual_ZNK5Http25Frame11payloadSizeEv')

  def padding(self) -> int:
    """
    Calls Qt's 'uchar Http2::Frame::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#padding
    """
    #  uchar Http2::Frame::padding() const
    return self.uglySide.call('ritual_ZNK5Http25Frame7paddingEv')

  def supportsPaddedFlag(self) -> bool:
    """
    Calls Qt's 'bool Http2::Frame::supportsPaddedFlag() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/http2-frame.html#supportsPaddedFlag
    """
    #  bool Http2::Frame::supportsPaddedFlag() const
    return self.uglySide.call('ritual_ZNK5Http25Frame18supportsPaddedFlagEv')

  def isPadded(self) -> bool:
    """
    Calls Qt's 'bool Http2::Frame::isPadded() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#isPadded
    """
    #  bool Http2::Frame::isPadded() const
    return self.uglySide.call('ritual_ZNK5Http25Frame8isPaddedEv')

  def validateHeader(self) -> Http2.FrameStatus:
    """
    Calls Qt's 'FrameStatus Http2::Frame::validateHeader() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#validateHeader

    Returns
    -------

    Http2.FrameStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Http2.FrameStatus(number)' gives.
    """
    #  FrameStatus Http2::Frame::validateHeader() const
    return Http2.FrameStatus(self.uglySide.call(
        'ritual_ZNK5Http25Frame14validateHeaderEv',
    ))

  def validatePayload(self) -> Http2.FrameStatus:
    """
    Calls Qt's 'FrameStatus Http2::Frame::validatePayload() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#validatePayload

    Returns
    -------

    Http2.FrameStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Http2.FrameStatus(number)' gives.
    """
    #  FrameStatus Http2::Frame::validatePayload() const
    return Http2.FrameStatus(self.uglySide.call(
        'ritual_ZNK5Http25Frame15validatePayloadEv',
    ))

  def dataSize(self) -> int:
    """
    Calls Qt's 'quint32 Http2::Frame::dataSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#dataSize
    """
    #  quint32 Http2::Frame::dataSize() const
    return self.uglySide.call('ritual_ZNK5Http25Frame8dataSizeEv')

  def hpackBlockSize(self) -> int:
    """
    Calls Qt's 'quint32 Http2::Frame::hpackBlockSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#hpackBlockSize
    """
    #  quint32 Http2::Frame::hpackBlockSize() const
    return self.uglySide.call('ritual_ZNK5Http25Frame14hpackBlockSizeEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'Http2::Frame::Frame()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/http2-frame.html#Frame
    """
    #  Http2::Frame::Frame()
    self._noteCreation(Frame, lambda: Rituals.call(
        'ritual_ZN5Http25FrameC1Ev',
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

  @staticmethod
  def dataBegin(*__, **_) -> Never:
    """
    Qt's 'const uchar *Http2::Frame::dataBegin() const': gives 'unsigned
    char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Http2.Frame.dataBegin' has no cute function yet. Qt's 'const "
        "uchar *Http2::Frame::dataBegin() const': gives 'unsigned char', "
        "which has no cute class yet.")

  @staticmethod
  def hpackBlockBegin(*__, **_) -> Never:
    """
    Qt's 'const uchar *Http2::Frame::hpackBlockBegin() const': gives
    'unsigned char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'Http2.Frame.hpackBlockBegin' has no cute function yet. Qt's "
        "'const uchar *Http2::Frame::hpackBlockBegin() const': gives "
        "'unsigned char', which has no cute class yet.")

  @staticmethod
  def priority(*__, **_) -> Never:
    """
    Qt's 'bool Http2::Frame::priority(quint32 *streamID, uchar *weight)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'Http2.Frame.priority' has no cute function yet. Qt's 'bool "
        "Http2::Frame::priority(quint32 *streamID, uchar *weight) const': "
        "takes a number to change where it is.")
