"""
QModbusRtuSerialClient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbusrtuserialclient.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QModbusClient

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QModbusRtuSerialClientPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QModbusRtuSerialClient(QModbusClient):
  """
  The cute side of Qt's QModbusRtuSerialClient: a plain Python object
  standing in front of one C++ QModbusRtuSerialClient.

  It is built on the cute 'QModbusClient', as Qt's QModbusRtuSerialClient is
  built on Qt's QModbusClient, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusRtuSerialClient that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'd_func',
  'interFrameDelay', 'setInterFrameDelay', 'turnaroundDelay',
  'setTurnaroundDelay', 'close', 'open'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QModbusRtuSerialClient::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QModbusRtuSerialClient::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QModbusRtuSerialClientPrivate
    *QModbusRtuSerialClient::d_func() const': takes in Python what
    'QModbusRtuSerialClientPrivate *QModbusRtuSerialClient::d_func()' takes.
  - Qt's 'QModbusRtuSerialClient::~QModbusRtuSerialClient()': the destructor:
    Python never removes a C++ QModbusRtuSerialClient.
  - Qt's 'QModbusRtuSerialClient::QModbusRtuSerialClient(
    QModbusRtuSerialClientPrivate &dd, QObject *parent)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QModbusRtuSerialClient is created at the first use, not by
    'QModbusRtuSerialClient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusRtuSerialClient.
  - Qt tells when it has removed the C++ QModbusRtuSerialClient. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QModbusRtuSerialClient::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusrtuserialclient.html#tr

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
    #  QString QModbusRtuSerialClient::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QModbusRtuSerialClient2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusRtuSerialClient'

  #  A C++ QModbusRtuSerialClient Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusRtuSerialClient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QModbusRtuSerialClient::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclient.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QModbusRtuSerialClient::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QModbusRtuSerialClient10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def interFrameDelay(self) -> int:
    """
    Calls Qt's 'int QModbusRtuSerialClient::interFrameDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclient.html#interFrameDelay
    """
    #  int QModbusRtuSerialClient::interFrameDelay() const
    return self.uglySide.call(
        'ritual_ZNK22QModbusRtuSerialClient15interFrameDelayEv',
    )

  def turnaroundDelay(self) -> int:
    """
    Calls Qt's 'int QModbusRtuSerialClient::turnaroundDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclient.html#turnaroundDelay
    """
    #  int QModbusRtuSerialClient::turnaroundDelay() const
    return self.uglySide.call(
        'ritual_ZNK22QModbusRtuSerialClient15turnaroundDelayEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInterFrameDelay(self, microseconds: int) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialClient::setInterFrameDelay(int
    microseconds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclient.html#setInterFrameDelay

    Parameters
    ----------

    microseconds : int
      Passed on as it is.
    """
    #  void QModbusRtuSerialClient::setInterFrameDelay(int microseconds)
    self.uglySide.call(
        'ritual_ZN22QModbusRtuSerialClient18setInterFrameDelayEi',
        microseconds,
    )

  @overload(int)
  def setTurnaroundDelay(self, turnaroundDelay: int) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialClient::setTurnaroundDelay(int
    turnaroundDelay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclient.html#setTurnaroundDelay

    Parameters
    ----------

    turnaroundDelay : int
      Passed on as it is.
    """
    #  void QModbusRtuSerialClient::setTurnaroundDelay(int turnaroundDelay)
    self.uglySide.call(
        'ritual_ZN22QModbusRtuSerialClient18setTurnaroundDelayEi',
        turnaroundDelay,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QModbusRtuSerialClient::QModbusRtuSerialClient(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialclient.html#QModbusRtuSerialClient

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QModbusRtuSerialClient::QModbusRtuSerialClient(QObject *parent)
    self._noteCreation(QModbusRtuSerialClient, lambda: Rituals.call(
        'ritual_ZN22QModbusRtuSerialClientC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QModbusRtuSerialClientPrivate]:
    """
    Calls Qt's 'QModbusRtuSerialClientPrivate
    *QModbusRtuSerialClient::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusrtuserialclient.html#d_func

    Returns
    -------

    Optional[QModbusRtuSerialClientPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusRtuSerialClientPrivate *QModbusRtuSerialClient::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QModbusRtuSerialClient6d_funcEv',
    )
    from . import QModbusRtuSerialClientPrivate
    return QModbusRtuSerialClientPrivate._cuteAt(address)

  def close(self) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialClient::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusrtuserialclient.html#close
    """
    #  void QModbusRtuSerialClient::close()
    ritual = 'ritual_ZN22QModbusRtuSerialClient5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QModbusRtuSerialClient5closeEv'
    self.uglySide.call(ritual)

  def open(self) -> bool:
    """
    Calls Qt's 'bool QModbusRtuSerialClient::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusrtuserialclient.html#open
    """
    #  bool QModbusRtuSerialClient::open()
    ritual = 'ritual_ZN22QModbusRtuSerialClient4openEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QModbusRtuSerialClient4openEv'
    return self.uglySide.call(ritual)
