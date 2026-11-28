"""
QHttpServerRequestPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverrequest_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QHttpServerRequestPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtNetwork import QHostAddress, QSslConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostAddress = WAIT['QHostAddress']
  QSslConfiguration = WAIT['QSslConfiguration']


class QHttpServerRequestPrivate(QSharedData):
  """
  The cute side of Qt's QHttpServerRequestPrivate: a plain Python object
  standing in front of one C++ QHttpServerRequestPrivate.

  It is built on the cute 'QSharedData', as Qt's QHttpServerRequestPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QHttpServerRequestPrivate around as a copy, so every C++
  QHttpServerRequestPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QHttpServerRequestPrivate yet. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpServerRequestPrivate::~QHttpServerRequestPrivate()': the
    destructor: Python removes its C++ QHttpServerRequestPrivate by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QHttpServerRequestPrivate is created at the first use, not by
    'QHttpServerRequestPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpServerRequestPrivate back gives a copy the
    ritual made for Python, in a new cute QHttpServerRequestPrivate.
  - Each name of Qt's QHttpServerRequestPrivate that has no cute function
    yet, 'contentLength', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpServerRequestPrivate'

  #  Qt's '~QHttpServerRequestPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QHttpServerRequestPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QHttpServerRequestPrivateD1Ev'

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

  @overload(QHostAddress, int, QHostAddress, int)
  def __init__(
      self,
      remoteAddress: QHostAddress,
      remotePort: int,
      localAddress: QHostAddress,
      localPort: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRequestPrivate::QHttpServerRequestPrivate(const QHostAddress
    &remoteAddress, quint16 remotePort, const QHostAddress &localAddress,
    quint16 localPort)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestprivate.html

    Parameters
    ----------

    remoteAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    remotePort : int
      Passed on as it is.

    localAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    localPort : int
      Passed on as it is.
    """
    #  QHttpServerRequestPrivate::QHttpServerRequestPrivate(const
    #      QHostAddress &remoteAddress, quint16 remotePort, const
    #      QHostAddress &localAddress, quint16 localPort)
    self._noteCreation(QHttpServerRequestPrivate, lambda: Rituals.call(
        'ritual_ZN25QHttpServerRequestPrivateC1ERK12QHostAddresstS2_t',
        self._valueOf(remoteAddress), remotePort,
        self._valueOf(localAddress), localPort,
    ))

  @overload(QHostAddress, int, QHostAddress, int, QSslConfiguration)
  def __init__(
      self,
      remoteAddress: QHostAddress,
      remotePort: int,
      localAddress: QHostAddress,
      localPort: int,
      sslConfiguration: QSslConfiguration,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRequestPrivate::QHttpServerRequestPrivate(const QHostAddress
    &remoteAddress, quint16 remotePort, const QHostAddress &localAddress,
    quint16 localPort, const QSslConfiguration &sslConfiguration)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestprivate.html

    Parameters
    ----------

    remoteAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    remotePort : int
      Passed on as it is.

    localAddress : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    localPort : int
      Passed on as it is.

    sslConfiguration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  QHttpServerRequestPrivate::QHttpServerRequestPrivate(const
    #      QHostAddress &remoteAddress, quint16 remotePort, const
    #      QHostAddress &localAddress, quint16 localPort, const
    #      QSslConfiguration &sslConfiguration)
    self._noteCreation(QHttpServerRequestPrivate, lambda: Rituals.call(
        'ritual_ZN25QHttpServerRequestPrivateC1ERK12QHostAddresstS2_tRK17QS'
        'slConfiguration',
        self._valueOf(remoteAddress), remotePort,
        self._valueOf(localAddress), localPort,
        self._valueOf(sslConfiguration),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRequestPrivate::QHttpServerRequestPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestprivate.html
    """
    #  QHttpServerRequestPrivate::QHttpServerRequestPrivate()
    self._noteCreation(QHttpServerRequestPrivate, lambda: Rituals.call(
        'ritual_ZN25QHttpServerRequestPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHttpServerRequestPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QHttpServerRequestPrivate::QHttpServerRequestPrivate(const
    QHttpServerRequestPrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpserverrequestprivate.html

    Parameters
    ----------

    other : QHttpServerRequestPrivate
      Passed on as a value: Qt reads the C++ QHttpServerRequestPrivate, which
      stays Python's own.
    """
    #  QHttpServerRequestPrivate::QHttpServerRequestPrivate(const
    #      QHttpServerRequestPrivate &other)
    self._noteCreation(QHttpServerRequestPrivate, lambda: Rituals.call(
        'ritual_ZN25QHttpServerRequestPrivateC1ERKS_', self._valueOf(other),
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
  def contentLength(*__, **_) -> Never:
    """
    Qt's 'qint64 QHttpServerRequestPrivate::contentLength() const': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QHttpServerRequestPrivate.contentLength' has no cute function "
        "yet. Qt's 'qint64 QHttpServerRequestPrivate::contentLength() "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
