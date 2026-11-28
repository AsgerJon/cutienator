"""
QNetworkDatagramPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkdatagram_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkDatagramPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QHostAddress, QIpPacketHeader
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHostAddress = WAIT['QHostAddress']
  QIpPacketHeader = WAIT['QIpPacketHeader']


class QNetworkDatagramPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkDatagramPrivate: a plain Python object
  standing in front of one C++ QNetworkDatagramPrivate.

  C++ hands a QNetworkDatagramPrivate around as a copy, so every C++
  QNetworkDatagramPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QNetworkDatagramPrivate yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkDatagramPrivate::~QNetworkDatagramPrivate()': the
    destructor: Python removes its C++ QNetworkDatagramPrivate by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QNetworkDatagramPrivate is created at the first use, not by
    'QNetworkDatagramPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkDatagramPrivate back gives a copy the ritual
    made for Python, in a new cute QNetworkDatagramPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkDatagramPrivate'

  #  Qt's '~QNetworkDatagramPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QNetworkDatagramPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QNetworkDatagramPrivateD1Ev'

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

  @overload()
  @overload(QByteArray)
  @overload(QByteArray, QHostAddress)
  @overload(QByteArray, QHostAddress, int)
  def __init__(
      self,
      data: Optional[QByteArray] = None,
      dstAddr: Optional[QHostAddress] = None,
      port: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkDatagramPrivate::QNetworkDatagramPrivate(const QByteArray &data,
    const QHostAddress &dstAddr, quint16 port)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagramprivate.html

    Parameters
    ----------

    data : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    dstAddr : Optional[QHostAddress]
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own. May be left out, as in Qt: a new 'QHostAddress()' is then
      passed on.

    port : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QNetworkDatagramPrivate::QNetworkDatagramPrivate(const QByteArray
    #      &data, const QHostAddress &dstAddr, quint16 port)
    if data is None:
      from ..QtCore import QByteArray
      data = QByteArray()
    if dstAddr is None:
      from . import QHostAddress
      dstAddr = QHostAddress()
    self._noteCreation(QNetworkDatagramPrivate, lambda: Rituals.call(
        'ritual_ZN23QNetworkDatagramPrivateC1ERK10QByteArrayRK12QHostAddres'
        'st',
        self._valueOf(data), self._valueOf(dstAddr), port,
    ))

  @overload(QByteArray, QIpPacketHeader)
  def __init__(self, data: QByteArray, header: QIpPacketHeader) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkDatagramPrivate::QNetworkDatagramPrivate(const QByteArray &data,
    const QIpPacketHeader &header)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkdatagramprivate.html

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    header : QIpPacketHeader
      Passed on as a value: Qt reads the C++ QIpPacketHeader, which stays
      Python's own.
    """
    #  QNetworkDatagramPrivate::QNetworkDatagramPrivate(const QByteArray
    #      &data, const QIpPacketHeader &header)
    self._noteCreation(QNetworkDatagramPrivate, lambda: Rituals.call(
        'ritual_ZN23QNetworkDatagramPrivateC1ERK10QByteArrayRK15QIpPacketHe'
        'ader',
        self._valueOf(data), self._valueOf(header),
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
