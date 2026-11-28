"""
QGrpcBidiStream binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpcstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QGrpcOperation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGrpcBidiStream(QGrpcOperation):
  """
  The cute side of Qt's QGrpcBidiStream: a plain Python object standing in
  front of one C++ QGrpcBidiStream.

  It is built on the cute 'QGrpcOperation', as Qt's QGrpcBidiStream is built
  on Qt's QGrpcOperation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGrpcBidiStream that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'writesDone',
  'messageReceived', 'event'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGrpcBidiStream::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGrpcBidiStream::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QGrpcBidiStream::QGrpcBidiStream(QLatin1StringView service,
    QLatin1StringView method, const QGrpcCallOptions &options,
    std::weak_ptr<QAbstractGrpcChannel> channel, PrivateConstructor a4)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QGrpcBidiStream::~QGrpcBidiStream()': the destructor: Python never
    removes a C++ QGrpcBidiStream.
  - Qt's 'void QGrpcBidiStream::writeMessage(const QProtobufMessage
    &message)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 16 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QGrpcBidiStream is created at the first use, not by
    'QGrpcBidiStream(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGrpcBidiStream.
  - Qt tells when it has removed the C++ QGrpcBidiStream. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGrpcBidiStream that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QGrpcBidiStream::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcbidistream.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGrpcBidiStream::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QGrpcBidiStream2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcBidiStream'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGrpcBidiStream::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcbidistream.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGrpcBidiStream::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGrpcBidiStream10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGrpcBidiStream::QGrpcBidiStream(QLatin1StringView service,
    QLatin1StringView method, const QGrpcCallOptions &options,
    std::weak_ptr<QAbstractGrpcChannel> channel, PrivateConstructor a4)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcBidiStream.__init__' has no cute function yet. Qt's "
        "'QGrpcBidiStream::QGrpcBidiStream(QLatin1StringView service, "
        "QLatin1StringView method, const QGrpcCallOptions &options, "
        "std::weak_ptr<QAbstractGrpcChannel> channel, PrivateConstructor "
        "a4)': takes a type Python has no way to hand over yet.")

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

  def writesDone(self) -> None:
    """
    Calls Qt's 'void QGrpcBidiStream::writesDone()'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcbidistream.html#writesDone
    """
    #  void QGrpcBidiStream::writesDone()
    self.uglySide.call('ritual_ZN15QGrpcBidiStream10writesDoneEv')

  def messageReceived(self) -> None:
    """
    Calls Qt's 'void QGrpcBidiStream::messageReceived()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcbidistream.html#messageReceived
    """
    #  void QGrpcBidiStream::messageReceived()
    self.uglySide.call('ritual_ZN15QGrpcBidiStream15messageReceivedEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGrpcBidiStream::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcbidistream.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGrpcBidiStream::event(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN15QGrpcBidiStream5eventEP6QEvent', self._addressOf(event),
    )
