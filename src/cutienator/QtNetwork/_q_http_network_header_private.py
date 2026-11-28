"""
QHttpNetworkHeaderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkheader_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QHttpNetworkHeaderPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QByteArrayView, QUrl
  from . import QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QByteArrayView = WAIT['QByteArrayView']
  QUrl = WAIT['QUrl']


class QHttpNetworkHeaderPrivate(QSharedData):
  """
  The cute side of Qt's QHttpNetworkHeaderPrivate: a plain Python object
  standing in front of one C++ QHttpNetworkHeaderPrivate.

  It is built on the cute 'QSharedData', as Qt's QHttpNetworkHeaderPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QHttpNetworkHeaderPrivate around as a copy, so every C++
  QHttpNetworkHeaderPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttpNetworkHeaderPrivate that has a ritual and that
  Python can call so far, 9 names in all: 'contentLength',
  'setContentLength', 'headerField', 'headerFieldValues', 'setHeaderField',
  'prependHeaderField', 'clearHeaders', 'headers', '__eq__'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttpNetworkHeaderPrivate::~QHttpNetworkHeaderPrivate()': the
    destructor: Python removes its C++ QHttpNetworkHeaderPrivate by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QHttpNetworkHeaderPrivate is created at the first use, not by
    'QHttpNetworkHeaderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttpNetworkHeaderPrivate back gives a copy the
    ritual made for Python, in a new cute QHttpNetworkHeaderPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpNetworkHeaderPrivate'

  #  Qt's '~QHttpNetworkHeaderPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QHttpNetworkHeaderPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QHttpNetworkHeaderPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def contentLength(self) -> int:
    """
    Calls Qt's 'qint64 QHttpNetworkHeaderPrivate::contentLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html#contentLength
    """
    #  qint64 QHttpNetworkHeaderPrivate::contentLength() const
    return self._callAs(
        'QHttpNetworkHeaderPrivate',
        'ritual_ZNK25QHttpNetworkHeaderPrivate13contentLengthEv',
    )

  @overload(QByteArrayView)
  @overload(QByteArrayView, QByteArray)
  def headerField(
      self,
      name: QByteArrayView,
      defaultValue: Optional[QByteArray] = None,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QHttpNetworkHeaderPrivate::headerField(QByteArrayView name, const
    QByteArray &defaultValue) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html#headerField

    Parameters
    ----------

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    defaultValue : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpNetworkHeaderPrivate::headerField(QByteArrayView name,
    #      const QByteArray &defaultValue) const
    if defaultValue is None:
      from ..QtCore import QByteArray
      defaultValue = QByteArray()
    address = self._callAs(
        'QHttpNetworkHeaderPrivate',
        'ritual_ZNK25QHttpNetworkHeaderPrivate11headerFieldE14QByteArrayVie'
        'wRK10QByteArray',
        self._valueOf(name), self._valueOf(defaultValue),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArrayView)
  def headerFieldValues(self, name: QByteArrayView) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray>
    QHttpNetworkHeaderPrivate::headerFieldValues(QByteArrayView name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html#headerFieldValues

    Parameters
    ----------

    name : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray>
    #      QHttpNetworkHeaderPrivate::headerFieldValues(QByteArrayView name)
    #      const
    address = self._callAs(
        'QHttpNetworkHeaderPrivate',
        'ritual_ZNK25QHttpNetworkHeaderPrivate17headerFieldValuesE14QByteAr'
        'rayView',
        self._valueOf(name),
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QHttpNetworkHeaderPrivate::headers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QHttpNetworkHeaderPrivate::headers() const
    address = self._callAs(
        'QHttpNetworkHeaderPrivate',
        'ritual_ZNK25QHttpNetworkHeaderPrivate7headersEv',
    )
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setContentLength(self, length: int) -> None:
    """
    Calls Qt's 'void QHttpNetworkHeaderPrivate::setContentLength(qint64
    length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html#setContentLength

    Parameters
    ----------

    length : int
      Passed on as it is.
    """
    #  void QHttpNetworkHeaderPrivate::setContentLength(qint64 length)
    self._callAs(
        'QHttpNetworkHeaderPrivate',
        'ritual_ZN25QHttpNetworkHeaderPrivate16setContentLengthEx',
        length,
    )

  @overload(QByteArray, QByteArray)
  def setHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpNetworkHeaderPrivate::setHeaderField(const
    QByteArray &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html#setHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpNetworkHeaderPrivate::setHeaderField(const QByteArray &name,
    #      const QByteArray &data)
    self._callAs(
        'QHttpNetworkHeaderPrivate',
        'ritual_ZN25QHttpNetworkHeaderPrivate14setHeaderFieldERK10QByteArra'
        'yS2_',
        self._valueOf(name), self._valueOf(data),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QHttpNetworkHeaderPrivate) -> bool:
    """
    Calls Qt's 'bool QHttpNetworkHeaderPrivate::operator==(const
    QHttpNetworkHeaderPrivate &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html#operator==

    Parameters
    ----------

    other : QHttpNetworkHeaderPrivate
      Passed on as a value: Qt reads the C++ QHttpNetworkHeaderPrivate, which
      stays Python's own.
    """
    #  bool QHttpNetworkHeaderPrivate::operator==(const
    #      QHttpNetworkHeaderPrivate &other) const
    return self._callAs(
        'QHttpNetworkHeaderPrivate',
        'ritual_ZNK25QHttpNetworkHeaderPrivateeqERKS_',
        self._valueOf(other, 'QHttpNetworkHeaderPrivate'),
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
  @overload(QUrl)
  def __init__(self, newUrl: Optional[QUrl] = None) -> None:
    """
    Notes what was given, for Qt's
    'QHttpNetworkHeaderPrivate::QHttpNetworkHeaderPrivate(const QUrl
    &newUrl)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html

    Parameters
    ----------

    newUrl : Optional[QUrl]
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
      May be left out, as in Qt: a new 'QUrl()' is then passed on.
    """
    #  QHttpNetworkHeaderPrivate::QHttpNetworkHeaderPrivate(const QUrl
    #      &newUrl)
    if newUrl is None:
      from ..QtCore import QUrl
      newUrl = QUrl()
    self._noteCreation(QHttpNetworkHeaderPrivate, lambda: Rituals.call(
        'ritual_ZN25QHttpNetworkHeaderPrivateC1ERK4QUrl',
        self._valueOf(newUrl),
    ))

  @overload(THIS)
  def __init__(self, other: QHttpNetworkHeaderPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QHttpNetworkHeaderPrivate::QHttpNetworkHeaderPrivate(const
    QHttpNetworkHeaderPrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html

    Parameters
    ----------

    other : QHttpNetworkHeaderPrivate
      Passed on as a value: Qt reads the C++ QHttpNetworkHeaderPrivate, which
      stays Python's own.
    """
    #  QHttpNetworkHeaderPrivate::QHttpNetworkHeaderPrivate(const
    #      QHttpNetworkHeaderPrivate &other)
    self._noteCreation(QHttpNetworkHeaderPrivate, lambda: Rituals.call(
        'ritual_ZN25QHttpNetworkHeaderPrivateC1ERKS_',
        self._valueOf(other, 'QHttpNetworkHeaderPrivate'),
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
  def prependHeaderField(self, name: QByteArray, data: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpNetworkHeaderPrivate::prependHeaderField(const
    QByteArray &name, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html#prependHeaderField

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpNetworkHeaderPrivate::prependHeaderField(const QByteArray
    #      &name, const QByteArray &data)
    self._callAs(
        'QHttpNetworkHeaderPrivate',
        'ritual_ZN25QHttpNetworkHeaderPrivate18prependHeaderFieldERK10QByte'
        'ArrayS2_',
        self._valueOf(name), self._valueOf(data),
    )

  def clearHeaders(self) -> None:
    """
    Calls Qt's 'void QHttpNetworkHeaderPrivate::clearHeaders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttpnetworkheaderprivate.html#clearHeaders
    """
    #  void QHttpNetworkHeaderPrivate::clearHeaders()
    self._callAs(
        'QHttpNetworkHeaderPrivate',
        'ritual_ZN25QHttpNetworkHeaderPrivate12clearHeadersEv',
    )
