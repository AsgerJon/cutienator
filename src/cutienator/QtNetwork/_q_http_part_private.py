"""
QHttpPartPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpmultipart_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QHttpPartPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QNetworkHeadersPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpPartPrivate(QSharedData, QNetworkHeadersPrivate):
  """
  The cute side of Qt's QHttpPartPrivate: a plain Python object standing in
  front of one C++ QHttpPartPrivate.

  It is built on the cute 'QSharedData', as Qt's QHttpPartPrivate is built on
  Qt's QSharedData, and has everything that class has. It is built on the
  cute 'QNetworkHeadersPrivate' as well, as Qt's QHttpPartPrivate is built on
  Qt's QNetworkHeadersPrivate too, and has everything that class has.

  C++ hands a QHttpPartPrivate around as a copy, so every C++
  QHttpPartPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpPartPrivate that has a ritual and that Python
  can call so far, 7 names in all: '__eq__', 'setBodyDevice', 'setBody',
  'bytesAvailable', 'size', 'reset', 'checkHeaderCreated'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpPartPrivate::~QHttpPartPrivate()': the destructor: Python
    removes its C++ QHttpPartPrivate by it, and has no other use for it.
  - Qt's 'qint64 QHttpPartPrivate::readData(char *data, qint64 maxSize)':
    names 'char', which has no cute class yet.

  What to expect
  --------------

  - The C++ QHttpPartPrivate is created at the first use, not by
    'QHttpPartPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpPartPrivate back gives a copy the ritual made
    for Python, in a new cute QHttpPartPrivate.
  - Each name of Qt's QHttpPartPrivate that has no cute function yet,
    'readData', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpPartPrivate'

  #  Qt's QHttpPartPrivate is built on more than one class. The part of a C++
  #  QHttpPartPrivate that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QNetworkHeadersPrivate':
          'ritual_cast_QHttpPartPrivate_QNetworkHeadersPrivate',
  }

  #  Qt's '~QHttpPartPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QHttpPartPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QHttpPartPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QHttpPartPrivate::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttppartprivate.html#bytesAvailable
    """
    #  qint64 QHttpPartPrivate::bytesAvailable() const
    return self.uglySide.call(
        'ritual_ZNK16QHttpPartPrivate14bytesAvailableEv',
    )

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QHttpPartPrivate::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppartprivate.html#size
    """
    #  qint64 QHttpPartPrivate::size() const
    return self.uglySide.call('ritual_ZNK16QHttpPartPrivate4sizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  def setBodyDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QHttpPartPrivate::setBodyDevice(QIODevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttppartprivate.html#setBodyDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHttpPartPrivate::setBodyDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN16QHttpPartPrivate13setBodyDeviceEP9QIODevice',
        self._addressOf(device),
    )

  @overload(QByteArray)
  def setBody(self, newBody: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpPartPrivate::setBody(const QByteArray &newBody)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppartprivate.html#setBody

    Parameters
    ----------

    newBody : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpPartPrivate::setBody(const QByteArray &newBody)
    self.uglySide.call(
        'ritual_ZN16QHttpPartPrivate7setBodyERK10QByteArray',
        self._valueOf(newBody),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QHttpPartPrivate) -> bool:
    """
    Calls Qt's 'bool QHttpPartPrivate::operator==(const QHttpPartPrivate
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppartprivate.html#operator==

    Parameters
    ----------

    other : QHttpPartPrivate
      Passed on as a value: Qt reads the C++ QHttpPartPrivate, which stays
      Python's own.
    """
    #  bool QHttpPartPrivate::operator==(const QHttpPartPrivate &other) const
    return self.uglySide.call(
        'ritual_ZNK16QHttpPartPrivateeqERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QHttpPartPrivate::QHttpPartPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttppartprivate.html#QHttpPartPrivate
    """
    #  QHttpPartPrivate::QHttpPartPrivate()
    self._noteCreation(QHttpPartPrivate, lambda: Rituals.call(
        'ritual_ZN16QHttpPartPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHttpPartPrivate) -> None:
    """
    Notes what was given, for Qt's 'QHttpPartPrivate::QHttpPartPrivate(const
    QHttpPartPrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttppartprivate.html#QHttpPartPrivate

    Parameters
    ----------

    other : QHttpPartPrivate
      Passed on as a value: Qt reads the C++ QHttpPartPrivate, which stays
      Python's own.
    """
    #  QHttpPartPrivate::QHttpPartPrivate(const QHttpPartPrivate &other)
    self._noteCreation(QHttpPartPrivate, lambda: Rituals.call(
        'ritual_ZN16QHttpPartPrivateC1ERKS_', self._valueOf(other),
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

  def reset(self) -> bool:
    """
    Calls Qt's 'bool QHttpPartPrivate::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttppartprivate.html#reset
    """
    #  bool QHttpPartPrivate::reset()
    return self.uglySide.call('ritual_ZN16QHttpPartPrivate5resetEv')

  def checkHeaderCreated(self) -> None:
    """
    Calls Qt's 'void QHttpPartPrivate::checkHeaderCreated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttppartprivate.html#checkHeaderCreated
    """
    #  void QHttpPartPrivate::checkHeaderCreated() const
    self.uglySide.call('ritual_ZNK16QHttpPartPrivate18checkHeaderCreatedEv')

  @staticmethod
  def readData(*__, **_) -> Never:
    """
    Qt's 'qint64 QHttpPartPrivate::readData(char *data, qint64 maxSize)':
    names 'char', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QHttpPartPrivate.readData' has no cute function yet. Qt's 'qint64 "
        "QHttpPartPrivate::readData(char *data, qint64 maxSize)': names "
        "'char', which has no cute class yet.")
