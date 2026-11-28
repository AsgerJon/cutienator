"""
QNetmask binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhostaddress_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QNetmask to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QAbstractSocket

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QHostAddress
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']


class QNetmask(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetmask: a plain Python object standing in front of
  one C++ QNetmask.

  C++ hands a QNetmask around as a copy, so every C++ QNetmask behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetmask that has a ritual and that Python can call
  so far, 5 names in all: 'setAddress', 'address', 'prefixLength',
  'setPrefixLength', '__eq__'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetmask::~QNetmask()': the destructor: Python removes its C++
    QNetmask by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QNetmask is created at the first use, not by 'QNetmask(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetmask back gives a copy the ritual made for
    Python, in a new cute QNetmask.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetmask'

  #  Qt's '~QNetmask()'. Naming it makes this a value class: Python owns
  #  every C++ QNetmask behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QNetmaskD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractSocket.NetworkLayerProtocol)
  def address(
      self,
      protocol: QAbstractSocket.NetworkLayerProtocol,
  ) -> QHostAddress:
    """
    Calls Qt's 'QHostAddress
    QNetmask::address(QAbstractSocket::NetworkLayerProtocol protocol) const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetmask.html#address

    Parameters
    ----------

    protocol : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number.

    Returns
    -------

    QHostAddress
      A new cute QHostAddress around the copy Qt gave back. Python owns it.
    """
    #  QHostAddress QNetmask::address(QAbstractSocket::NetworkLayerProtocol
    #      protocol) const
    address = self.uglySide.call(
        'ritual_ZNK8QNetmask7addressEN15QAbstractSocket20NetworkLayerProtoc'
        'olE',
        protocol.value,
    )
    from . import QHostAddress
    return QHostAddress._cuteOwning(address)

  def prefixLength(self) -> int:
    """
    Calls Qt's 'int QNetmask::prefixLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetmask.html#prefixLength
    """
    #  int QNetmask::prefixLength() const
    return self.uglySide.call('ritual_ZNK8QNetmask12prefixLengthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QHostAddress)
  def setAddress(self, address: QHostAddress) -> bool:
    """
    Calls Qt's 'bool QNetmask::setAddress(const QHostAddress &address)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetmask.html#setAddress

    Parameters
    ----------

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.
    """
    #  bool QNetmask::setAddress(const QHostAddress &address)
    return self.uglySide.call(
        'ritual_ZN8QNetmask10setAddressERK12QHostAddress',
        self._valueOf(address),
    )

  @overload(QAbstractSocket.NetworkLayerProtocol, int)
  def setPrefixLength(
      self,
      proto: QAbstractSocket.NetworkLayerProtocol,
      len: int,
  ) -> None:
    """
    Calls Qt's 'void
    QNetmask::setPrefixLength(QAbstractSocket::NetworkLayerProtocol proto,
    int len)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetmask.html#setPrefixLength

    Parameters
    ----------

    proto : QAbstractSocket.NetworkLayerProtocol
      Passed on as its number.

    len : int
      Passed on as it is.
    """
    #  void QNetmask::setPrefixLength(QAbstractSocket::NetworkLayerProtocol
    #      proto, int len)
    self.uglySide.call(
        'ritual_ZN8QNetmask15setPrefixLengthEN15QAbstractSocket20NetworkLay'
        'erProtocolEi',
        proto.value, len,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, n2: QNetmask) -> bool:
    """
    Calls Qt's 'bool operator==(QNetmask n1, QNetmask n2)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetmask.html#operator==

    Parameters
    ----------

    n2 : QNetmask
      Passed on as a value: Qt reads the C++ QNetmask, which stays Python's
      own.
    """
    #  bool operator==(QNetmask n1, QNetmask n2)
    return Rituals.call(
        'ritual_Zeq8QNetmaskS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(n2),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QNetmask::QNetmask()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qnetmask.html#QNetmask
    """
    #  QNetmask::QNetmask()
    self._noteCreation(QNetmask, lambda: Rituals.call(
        'ritual_ZN8QNetmaskC1Ev',
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
