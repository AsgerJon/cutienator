"""
QHttpPart binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qhttpmultipart.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QNetworkRequest

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QDebug, QIODevice, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDebug = WAIT['QDebug']
  QIODevice = WAIT['QIODevice']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpPart(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttpPart: a plain Python object standing in front of
  one C++ QHttpPart.

  C++ hands a QHttpPart around as a copy, so every C++ QHttpPart behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpPart that has a ritual and that Python can call
  so far, 7 names in all: '__eq__', '__ne__', 'setHeader', 'setRawHeader',
  'setBody', 'setBodyDevice', '__rlshift__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpPart::~QHttpPart()': the destructor: Python removes its C++
    QHttpPart by it, and has no other use for it.
  - Qt's 'QHttpPart &QHttpPart::operator=(QHttpPart &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QHttpPart &QHttpPart::operator=(const QHttpPart &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QHttpPart::swap(QHttpPart &other)': takes a type Python has no
    way to hand over yet.

  What to expect
  --------------

  - The C++ QHttpPart is created at the first use, not by 'QHttpPart(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpPart back gives a copy the ritual made for
    Python, in a new cute QHttpPart.
  - Each name of Qt's QHttpPart that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpPart'

  #  Qt's '~QHttpPart()'. Naming it makes this a value class: Python owns
  #  every C++ QHttpPart behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QHttpPartD1Ev'

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

  @overload(QNetworkRequest.KnownHeaders, QVariant)
  def setHeader(
      self,
      header: QNetworkRequest.KnownHeaders,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QHttpPart::setHeader(QNetworkRequest::KnownHeaders
    header, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppart.html#setHeader

    Parameters
    ----------

    header : QNetworkRequest.KnownHeaders
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QHttpPart::setHeader(QNetworkRequest::KnownHeaders header, const
    #      QVariant &value)
    self.uglySide.call(
        'ritual_ZN9QHttpPart9setHeaderEN15QNetworkRequest12KnownHeadersERK8'
        'QVariant',
        header.value, self._valueOf(value),
    )

  @overload(QByteArray, QByteArray)
  def setRawHeader(
      self,
      headerName: QByteArray,
      headerValue: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QHttpPart::setRawHeader(const QByteArray &headerName,
    const QByteArray &headerValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppart.html#setRawHeader

    Parameters
    ----------

    headerName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    headerValue : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpPart::setRawHeader(const QByteArray &headerName, const
    #      QByteArray &headerValue)
    self.uglySide.call(
        'ritual_ZN9QHttpPart12setRawHeaderERK10QByteArrayS2_',
        self._valueOf(headerName), self._valueOf(headerValue),
    )

  @overload(QByteArray)
  def setBody(self, body: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpPart::setBody(const QByteArray &body)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppart.html#setBody

    Parameters
    ----------

    body : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpPart::setBody(const QByteArray &body)
    self.uglySide.call(
        'ritual_ZN9QHttpPart7setBodyERK10QByteArray', self._valueOf(body),
    )

  @overload(QIODevice)
  @overload(NoneType)
  def setBodyDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QHttpPart::setBodyDevice(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppart.html#setBodyDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpPart::setBodyDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN9QHttpPart13setBodyDeviceEP9QIODevice',
        self._addressOf(device),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QHttpPart) -> bool:
    """
    Calls Qt's 'bool QHttpPart::operator==(const QHttpPart &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppart.html#operator==

    Parameters
    ----------

    other : QHttpPart
      Passed on as a value: Qt reads the C++ QHttpPart, which stays Python's
      own.
    """
    #  bool QHttpPart::operator==(const QHttpPart &other) const
    return self.uglySide.call(
        'ritual_ZNK9QHttpParteqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QHttpPart) -> bool:
    """
    Calls Qt's 'bool QHttpPart::operator!=(const QHttpPart &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppart.html#operator!=

    Parameters
    ----------

    other : QHttpPart
      Passed on as a value: Qt reads the C++ QHttpPart, which stays Python's
      own.
    """
    #  bool QHttpPart::operator!=(const QHttpPart &other) const
    return self.uglySide.call(
        'ritual_ZNK9QHttpPartneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QHttpPart &httpPart)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppart.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QHttpPart &httpPart)
    address = Rituals.call(
        'ritual_Zls6QDebugRK9QHttpPart',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QHttpPart::QHttpPart()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhttppart.html#QHttpPart
    """
    #  QHttpPart::QHttpPart()
    self._noteCreation(QHttpPart, lambda: Rituals.call(
        'ritual_ZN9QHttpPartC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHttpPart) -> None:
    """
    Notes what was given, for Qt's 'QHttpPart::QHttpPart(const QHttpPart
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhttppart.html#QHttpPart

    Parameters
    ----------

    other : QHttpPart
      Passed on as a value: Qt reads the C++ QHttpPart, which stays Python's
      own.
    """
    #  QHttpPart::QHttpPart(const QHttpPart &other)
    self._noteCreation(QHttpPart, lambda: Rituals.call(
        'ritual_ZN9QHttpPartC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHttpPart::swap(QHttpPart &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttpPart.swap' has no cute function yet. Qt's 'void "
        "QHttpPart::swap(QHttpPart &other)': takes a type Python has no way "
        "to hand over yet.")
