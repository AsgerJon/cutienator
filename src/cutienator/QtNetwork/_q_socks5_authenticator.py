"""
QSocks5Authenticator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qsocks5socketengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSocks5Authenticator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QTcpSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QTcpSocket = WAIT['QTcpSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSocks5Authenticator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSocks5Authenticator: a plain Python object standing
  in front of one C++ QSocks5Authenticator.

  C++ hands a QSocks5Authenticator around as a copy, so every C++
  QSocks5Authenticator behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSocks5Authenticator that has a ritual and that
  Python can call so far, 3 names in all: 'seal', 'unSeal', 'errorString'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSocks5Authenticator::~QSocks5Authenticator()': the destructor:
    Python removes its C++ QSocks5Authenticator by it, and has no other use
    for it.
  - Qt's 'char QSocks5Authenticator::methodId()': gives a single letter as C
    has it.
  - Qt's 'bool QSocks5Authenticator::beginAuthenticate(QTcpSocket *socket,
    bool *completed)': takes a number to change where it is.
  - Qt's 'bool QSocks5Authenticator::continueAuthenticate(QTcpSocket *socket,
    bool *completed)': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QSocks5Authenticator is created at the first use, not by
    'QSocks5Authenticator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSocks5Authenticator back gives a copy the ritual
    made for Python, in a new cute QSocks5Authenticator.
  - Each name of Qt's QSocks5Authenticator that has no cute function yet,
    'beginAuthenticate', 'continueAuthenticate', 'methodId', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSocks5Authenticator'

  #  A C++ QSocks5Authenticator Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSocks5Authenticator'

  #  The functions Qt calls itself that QSocks5Authenticator is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'beginAuthenticate': (
          'bool QSocks5Authenticator::beginAuthenticate(QTcpSocket *, bool '
          '*)',
      ),
      'continueAuthenticate': (
          'bool QSocks5Authenticator::continueAuthenticate(QTcpSocket *, '
          'bool *)',
      ),
  }

  #  The functions Qt calls itself that QSocks5Authenticator is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'methodId': (
          ('_ZN20QSocks5Authenticator8methodIdEv',
           ('char', 'number', ''),
           ()),
      ),
      'errorString': (
          ('_ZN20QSocks5Authenticator11errorStringEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Qt's '~QSocks5Authenticator()'. Naming it makes this a value class:
  #  Python owns every C++ QSocks5Authenticator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QSocks5AuthenticatorD1Ev'

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSocks5Authenticator::QSocks5Authenticator()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5authenticator.html#QSocks5Authenticator
    """
    #  QSocks5Authenticator::QSocks5Authenticator()
    self._noteCreation(QSocks5Authenticator, lambda: Rituals.call(
        'ritual_ZN20QSocks5AuthenticatorC1Ev',
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

  @overload(QByteArray, QByteArray)
  @overload(QByteArray, NoneType)
  def seal(self, buf: QByteArray, sealedBuf: Optional[QByteArray]) -> bool:
    """
    Calls Qt's 'bool QSocks5Authenticator::seal(const QByteArray &buf,
    QByteArray *sealedBuf)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5authenticator.html#seal

    Parameters
    ----------

    buf : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    sealedBuf : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSocks5Authenticator::seal(const QByteArray &buf, QByteArray
    #      *sealedBuf)
    return self.uglySide.call(
        'ritual_ZN20QSocks5Authenticator4sealERK10QByteArrayPS0_',
        self._valueOf(buf), self._addressOf(sealedBuf),
    )

  @overload(QByteArray, QByteArray)
  @overload(QByteArray, NoneType)
  def unSeal(self, sealedBuf: QByteArray, buf: Optional[QByteArray]) -> bool:
    """
    Calls Qt's 'bool QSocks5Authenticator::unSeal(const QByteArray
    &sealedBuf, QByteArray *buf)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5authenticator.html#unSeal

    Parameters
    ----------

    sealedBuf : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    buf : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSocks5Authenticator::unSeal(const QByteArray &sealedBuf,
    #      QByteArray *buf)
    return self.uglySide.call(
        'ritual_ZN20QSocks5Authenticator6unSealERK10QByteArrayPS0_',
        self._valueOf(sealedBuf), self._addressOf(buf),
    )

  @overload(QTcpSocket, QByteArray)
  @overload(QTcpSocket, NoneType)
  @overload(NoneType, QByteArray)
  @overload(NoneType, NoneType)
  def unSeal(
      self,
      sealedSocket: Optional[QTcpSocket],
      buf: Optional[QByteArray],
  ) -> bool:
    """
    Calls Qt's 'bool QSocks5Authenticator::unSeal(QTcpSocket *sealedSocket,
    QByteArray *buf)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocks5authenticator.html#unSeal

    Parameters
    ----------

    sealedSocket : Optional[QTcpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    buf : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSocks5Authenticator::unSeal(QTcpSocket *sealedSocket, QByteArray
    #      *buf)
    return self.uglySide.call(
        'ritual_ZN20QSocks5Authenticator6unSealEP10QTcpSocketP10QByteArray',
        self._addressOf(sealedSocket), self._addressOf(buf),
    )

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QSocks5Authenticator::errorString()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocks5authenticator.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSocks5Authenticator::errorString()
    ritual = 'ritual_ZN20QSocks5Authenticator11errorStringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSocks5Authenticator11errorStringEv'
    return self.uglySide.call(ritual)

  @staticmethod
  def beginAuthenticate(*__, **_) -> Never:
    """
    Qt's 'bool QSocks5Authenticator::beginAuthenticate(QTcpSocket *socket,
    bool *completed)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QSocks5Authenticator.beginAuthenticate' has no cute function yet. "
        "Qt's 'bool QSocks5Authenticator::beginAuthenticate(QTcpSocket "
        "*socket, bool *completed)': takes a number to change where it is.")

  @staticmethod
  def continueAuthenticate(*__, **_) -> Never:
    """
    Qt's 'bool QSocks5Authenticator::continueAuthenticate(QTcpSocket *socket,
    bool *completed)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QSocks5Authenticator.continueAuthenticate' has no cute function "
        "yet. Qt's 'bool "
        "QSocks5Authenticator::continueAuthenticate(QTcpSocket *socket, "
        "bool *completed)': takes a number to change where it is.")

  @staticmethod
  def methodId(*__, **_) -> Never:
    """
    Qt's 'char QSocks5Authenticator::methodId()': gives a single letter as C
    has it.
    """
    raise NotImplementedError(
        "'QSocks5Authenticator.methodId' has no cute function yet. Qt's "
        "'char QSocks5Authenticator::methodId()': gives a single letter as "
        "C has it.")
