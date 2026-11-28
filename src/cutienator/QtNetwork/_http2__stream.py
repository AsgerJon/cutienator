"""
Http2::Stream binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/http2streams_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Http2::Stream to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QHttpNetworkRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QNonContiguousByteDevice
  from . import QHttpNetworkReply


class Stream(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Http2::Stream: a plain Python object standing in
  front of one C++ Http2::Stream.

  C++ hands a Http2::Stream around as a copy, so every C++ Http2::Stream
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Http2::Stream that has a ritual and that Python can
  call so far, 5 names in all: 'reply', 'request', 'priority', 'weight',
  'data'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Http2::Stream::Stream(const HttpMessagePair &message, quint32
    streamID, qint32 sendSize, qint32 recvSize)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QHttpNetworkRequest &Http2::Stream::request()': gives a type Python
    has no way to take yet.
  - Qt's 'Http2::Stream::~Stream()': the destructor: Python removes its C++
    Http2::Stream by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Http2::Stream is created at the first use, not by
    'Http2::Stream(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Http2::Stream back gives a copy the ritual made for
    Python, in a new cute Http2::Stream.
  """

  #  The enums Qt writes inside Http2::Stream, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class StreamState(CuteNum):
    """
    The enum 'Http2::Stream::StreamState' of Qt, with the 6 names Qt gives in
    it.
    """

    idle = Kee[int](0)
    open = Kee[int](1)
    halfClosedLocal = Kee[int](2)
    halfClosedRemote = Kee[int](3)
    remoteReserved = Kee[int](4)
    closed = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Http2::Stream'

  #  Qt's '~Http2::Stream()'. Naming it makes this a value class: Python owns
  #  every C++ Http2::Stream behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN5Http26StreamD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def reply(self) -> Optional[QHttpNetworkReply]:
    """
    Calls Qt's 'QHttpNetworkReply *Http2::Stream::reply() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-stream.html#reply

    Returns
    -------

    Optional[QHttpNetworkReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpNetworkReply *Http2::Stream::reply() const
    address = self.uglySide.call('ritual_ZNK5Http26Stream5replyEv')
    from . import QHttpNetworkReply
    return QHttpNetworkReply._cuteAt(address)

  def request(self) -> QHttpNetworkRequest:
    """
    Calls Qt's 'const QHttpNetworkRequest &Http2::Stream::request() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-stream.html#request

    Returns
    -------

    QHttpNetworkRequest
      A new cute QHttpNetworkRequest around the copy Qt gave back. Python
      owns it.
    """
    #  const QHttpNetworkRequest &Http2::Stream::request() const
    address = self.uglySide.call('ritual_ZNK5Http26Stream7requestEv')
    return QHttpNetworkRequest._cuteOwning(address)

  def priority(self) -> QHttpNetworkRequest.Priority:
    """
    Calls Qt's 'QHttpNetworkRequest::Priority Http2::Stream::priority()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-stream.html#priority

    Returns
    -------

    QHttpNetworkRequest.Priority
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QHttpNetworkRequest.Priority(number)' gives.
    """
    #  QHttpNetworkRequest::Priority Http2::Stream::priority() const
    return QHttpNetworkRequest.Priority(self.uglySide.call(
        'ritual_ZNK5Http26Stream8priorityEv',
    ))

  def weight(self) -> int:
    """
    Calls Qt's 'uchar Http2::Stream::weight() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-stream.html#weight
    """
    #  uchar Http2::Stream::weight() const
    return self.uglySide.call('ritual_ZNK5Http26Stream6weightEv')

  def data(self) -> Optional[QNonContiguousByteDevice]:
    """
    Calls Qt's 'QNonContiguousByteDevice *Http2::Stream::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/http2-stream.html#data

    Returns
    -------

    Optional[QNonContiguousByteDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNonContiguousByteDevice *Http2::Stream::data() const
    address = self.uglySide.call('ritual_ZNK5Http26Stream4dataEv')
    from ..QtCore import QNonContiguousByteDevice
    return QNonContiguousByteDevice._cuteAt(address)

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
    Notes what was given, for Qt's 'Http2::Stream::Stream()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/http2-stream.html#Stream
    """
    #  Http2::Stream::Stream()
    self._noteCreation(Stream, lambda: Rituals.call(
        'ritual_ZN5Http26StreamC1Ev',
    ))

  @overload(str, int, int)
  def __init__(self, key: str, streamID: int, recvSize: int) -> None:
    """
    Notes what was given, for Qt's 'Http2::Stream::Stream(const QString &key,
    quint32 streamID, qint32 recvSize)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/http2-stream.html#Stream

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    streamID : int
      Passed on as it is.

    recvSize : int
      Passed on as it is.
    """
    #  Http2::Stream::Stream(const QString &key, quint32 streamID, qint32
    #      recvSize)
    self._noteCreation(Stream, lambda: Rituals.call(
        'ritual_ZN5Http26StreamC1ERK7QStringji', key, streamID, recvSize,
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
