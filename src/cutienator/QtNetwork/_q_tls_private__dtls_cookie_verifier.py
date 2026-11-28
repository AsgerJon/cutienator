"""
QTlsPrivate::DtlsCookieVerifier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTlsPrivate::DtlsCookieVerifier to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QTlsPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QHostAddress, QUdpSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHostAddress = WAIT['QHostAddress']
  QUdpSocket = WAIT['QUdpSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DtlsCookieVerifier(QTlsPrivate.DtlsBase):
  """
  The cute side of Qt's QTlsPrivate::DtlsCookieVerifier: a plain Python
  object standing in front of one C++ QTlsPrivate::DtlsCookieVerifier.

  It is built on the cute 'QTlsPrivate::DtlsBase', as Qt's
  QTlsPrivate::DtlsCookieVerifier is built on Qt's QTlsPrivate::DtlsBase, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QTlsPrivate::DtlsCookieVerifier that has a ritual
  and that Python can call so far, 2 names in all: 'verifyClient',
  'verifiedHello'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What to expect
  --------------

  - The C++ QTlsPrivate::DtlsCookieVerifier is created at the first use, not
    by 'QTlsPrivate::DtlsCookieVerifier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTlsPrivate::DtlsCookieVerifier.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTlsPrivate::DtlsCookieVerifier'

  #  A C++ QTlsPrivate::DtlsCookieVerifier Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTlsPrivate_DtlsCookieVerifier'

  #  The functions Qt calls itself that QTlsPrivate::DtlsCookieVerifier is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'verifyClient': (
          ('_ZN11QTlsPrivate18DtlsCookieVerifier12verifyClientEP10QUdpSocke'
           'tRK10QByteArrayRK12QHostAddresst',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtNetwork:QUdpSocket'),
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value', 'QtNetwork:QHostAddress'),
               ('unsigned short', 'number', ''),
           )),
      ),
      'verifiedHello': (
          ('_ZNK11QTlsPrivate18DtlsCookieVerifier13verifiedHelloEv',
           ('address', 'value', 'QtCore:QByteArray'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def verifiedHello(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QTlsPrivate::DtlsCookieVerifier::verifiedHello()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscookieverifier.html#verifiedHello

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QTlsPrivate::DtlsCookieVerifier::verifiedHello() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate18DtlsCookieVerifier13verifiedHelloEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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

  @overload(QUdpSocket, QByteArray, QHostAddress, int)
  @overload(NoneType, QByteArray, QHostAddress, int)
  def verifyClient(
      self,
      socket: Optional[QUdpSocket],
      dgram: QByteArray,
      address: QHostAddress,
      port: int,
  ) -> bool:
    """
    Calls Qt's 'bool QTlsPrivate::DtlsCookieVerifier::verifyClient(QUdpSocket
    *socket, const QByteArray &dgram, const QHostAddress &address, quint16
    port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlscookieverifier.html#verifyClient

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dgram : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  bool QTlsPrivate::DtlsCookieVerifier::verifyClient(QUdpSocket *socket,
    #      const QByteArray &dgram, const QHostAddress &address, quint16
    #      port)
    return self.uglySide.call(
        'ritual_ZN11QTlsPrivate18DtlsCookieVerifier12verifyClientEP10QUdpSo'
        'cketRK10QByteArrayRK12QHostAddresst',
        self._addressOf(socket), self._valueOf(dgram),
        self._valueOf(address), port,
    )
