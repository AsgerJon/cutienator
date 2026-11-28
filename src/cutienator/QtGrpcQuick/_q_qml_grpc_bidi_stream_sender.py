"""
QQmlGrpcBidiStreamSender binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpcQuick/qtqmlgrpcstreamsender.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGrpc import QGrpcBidiStream
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGrpcBidiStream = WAIT['QGrpcBidiStream']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlGrpcBidiStreamSender(QObject):
  """
  The cute side of Qt's QQmlGrpcBidiStreamSender: a plain Python object
  standing in front of one C++ QQmlGrpcBidiStreamSender.

  It is built on the cute 'QObject', as Qt's QQmlGrpcBidiStreamSender is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlGrpcBidiStreamSender that has a ritual and that
  Python can call so far, 2 names in all: 'metaObject', 'tr'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlGrpcBidiStreamSender::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQmlGrpcBidiStreamSender::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlGrpcBidiStreamSender::~QQmlGrpcBidiStreamSender()': the
    destructor: Python never removes a C++ QQmlGrpcBidiStreamSender.
  - Qt's 'void QQmlGrpcBidiStreamSender::writeMessageImpl(const
    QProtobufMessage &message) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQmlGrpcBidiStreamSenderPrivate
    *QQmlGrpcBidiStreamSender::d_func()': gives
    'QQmlGrpcBidiStreamSenderPrivate', which has no cute class yet.
  - Qt's 'const QQmlGrpcBidiStreamSenderPrivate
    *QQmlGrpcBidiStreamSender::d_func() const': gives
    'QQmlGrpcBidiStreamSenderPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 15 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlGrpcBidiStreamSender is created at the first use, not by
    'QQmlGrpcBidiStreamSender(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlGrpcBidiStreamSender.
  - Qt tells when it has removed the C++ QQmlGrpcBidiStreamSender. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlGrpcBidiStreamSender that has no cute function yet,
    'writeMessageImpl', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQmlGrpcBidiStreamSender::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgrpcbidistreamsender.html#tr

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
    #  QString QQmlGrpcBidiStreamSender::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQmlGrpcBidiStreamSender2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlGrpcBidiStreamSender'

  #  A C++ QQmlGrpcBidiStreamSender Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlGrpcBidiStreamSender'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlGrpcBidiStreamSender::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcbidistreamsender.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlGrpcBidiStreamSender::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlGrpcBidiStreamSender10metaObjectEv',
    )
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

  @overload(QGrpcBidiStream)
  @overload(NoneType)
  @overload(QGrpcBidiStream, QObject)
  @overload(QGrpcBidiStream, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      stream: Optional[QGrpcBidiStream],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlGrpcBidiStreamSender::QQmlGrpcBidiStreamSender(QGrpcBidiStream
    *stream, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcbidistreamsender.html

    Parameters
    ----------

    stream : Optional[QGrpcBidiStream]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlGrpcBidiStreamSender::QQmlGrpcBidiStreamSender(QGrpcBidiStream
    #      *stream, QObject *parent)
    self._noteCreation(QQmlGrpcBidiStreamSender, lambda: Rituals.call(
        'ritual_ZN24QQmlGrpcBidiStreamSenderC1EP15QGrpcBidiStreamP7QObject',
        self._addressOf(stream), self._addressOf(parent, 'QObject'),
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
  def writeMessageImpl(*__, **_) -> Never:
    """
    Qt's 'void QQmlGrpcBidiStreamSender::writeMessageImpl(const
    QProtobufMessage &message) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlGrpcBidiStreamSender.writeMessageImpl' has no cute function "
        "yet. Qt's 'void QQmlGrpcBidiStreamSender::writeMessageImpl(const "
        "QProtobufMessage &message) const': takes a type Python has no way "
        "to hand over yet.")
