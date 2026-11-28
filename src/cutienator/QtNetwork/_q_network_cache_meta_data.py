"""
QNetworkCacheMetaData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qabstractnetworkcache.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDateTime, QUrl
  from . import QHttpHeaders
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QHttpHeaders = WAIT['QHttpHeaders']
  QUrl = WAIT['QUrl']


class QNetworkCacheMetaData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkCacheMetaData: a plain Python object standing
  in front of one C++ QNetworkCacheMetaData.

  C++ hands a QNetworkCacheMetaData around as a copy, so every C++
  QNetworkCacheMetaData behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetworkCacheMetaData that has a ritual and that
  Python can call so far, 13 names in all: '__eq__', '__ne__', 'isValid',
  'url', 'setUrl', 'headers', 'setHeaders', 'lastModified',
  'setLastModified', 'expirationDate', 'setExpirationDate', 'saveToDisk',
  'setSaveToDisk'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNetworkCacheMetaData::~QNetworkCacheMetaData()': the destructor:
    Python removes its C++ QNetworkCacheMetaData by it, and has no other use
    for it.
  - Qt's 'QNetworkCacheMetaData
    &QNetworkCacheMetaData::operator=(QNetworkCacheMetaData &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QNetworkCacheMetaData &QNetworkCacheMetaData::operator=(const
    QNetworkCacheMetaData &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'void QNetworkCacheMetaData::swap(QNetworkCacheMetaData &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'RawHeaderList QNetworkCacheMetaData::rawHeaders() const': gives a
    type Python has no way to take yet.
  - Qt's 'void QNetworkCacheMetaData::setRawHeaders(const RawHeaderList
    &headers)': takes a type Python has no way to hand over yet.
  - Qt's 'AttributesMap QNetworkCacheMetaData::attributes() const': gives a
    type Python has no way to take yet.
  - Qt's 'void QNetworkCacheMetaData::setAttributes(const AttributesMap
    &attributes)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QNetworkCacheMetaData is created at the first use, not by
    'QNetworkCacheMetaData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkCacheMetaData back gives a copy the ritual
    made for Python, in a new cute QNetworkCacheMetaData.
  - Each name of Qt's QNetworkCacheMetaData that has no cute function yet,
    'attributes', 'rawHeaders', 'setAttributes', 'setRawHeaders', 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkCacheMetaData'

  #  Qt's '~QNetworkCacheMetaData()'. Naming it makes this a value class:
  #  Python owns every C++ QNetworkCacheMetaData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QNetworkCacheMetaDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QNetworkCacheMetaData::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcachemetadata.html#isValid
    """
    #  bool QNetworkCacheMetaData::isValid() const
    return self.uglySide.call('ritual_ZNK21QNetworkCacheMetaData7isValidEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QNetworkCacheMetaData::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcachemetadata.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QNetworkCacheMetaData::url() const
    address = self.uglySide.call('ritual_ZNK21QNetworkCacheMetaData3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QNetworkCacheMetaData::headers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcachemetadata.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QNetworkCacheMetaData::headers() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkCacheMetaData7headersEv',
    )
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

  def lastModified(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QNetworkCacheMetaData::lastModified() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#lastModified

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QNetworkCacheMetaData::lastModified() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkCacheMetaData12lastModifiedEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def expirationDate(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QNetworkCacheMetaData::expirationDate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#expirationDate

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QNetworkCacheMetaData::expirationDate() const
    address = self.uglySide.call(
        'ritual_ZNK21QNetworkCacheMetaData14expirationDateEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def saveToDisk(self) -> bool:
    """
    Calls Qt's 'bool QNetworkCacheMetaData::saveToDisk() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#saveToDisk
    """
    #  bool QNetworkCacheMetaData::saveToDisk() const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkCacheMetaData10saveToDiskEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QNetworkCacheMetaData::setUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QNetworkCacheMetaData::setUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN21QNetworkCacheMetaData6setUrlERK4QUrl',
        self._valueOf(url),
    )

  @overload(QHttpHeaders)
  def setHeaders(self, headers: QHttpHeaders) -> None:
    """
    Calls Qt's 'void QNetworkCacheMetaData::setHeaders(const QHttpHeaders
    &headers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setHeaders

    Parameters
    ----------

    headers : QHttpHeaders
      Passed on as a value: Qt reads the C++ QHttpHeaders, which stays
      Python's own.
    """
    #  void QNetworkCacheMetaData::setHeaders(const QHttpHeaders &headers)
    self.uglySide.call(
        'ritual_ZN21QNetworkCacheMetaData10setHeadersERK12QHttpHeaders',
        self._valueOf(headers),
    )

  @overload(QDateTime)
  def setLastModified(self, dateTime: QDateTime) -> None:
    """
    Calls Qt's 'void QNetworkCacheMetaData::setLastModified(const QDateTime
    &dateTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setLastModified

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QNetworkCacheMetaData::setLastModified(const QDateTime &dateTime)
    self.uglySide.call(
        'ritual_ZN21QNetworkCacheMetaData15setLastModifiedERK9QDateTime',
        self._valueOf(dateTime),
    )

  @overload(QDateTime)
  def setExpirationDate(self, dateTime: QDateTime) -> None:
    """
    Calls Qt's 'void QNetworkCacheMetaData::setExpirationDate(const QDateTime
    &dateTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setExpirationDate

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QNetworkCacheMetaData::setExpirationDate(const QDateTime
    #      &dateTime)
    self.uglySide.call(
        'ritual_ZN21QNetworkCacheMetaData17setExpirationDateERK9QDateTime',
        self._valueOf(dateTime),
    )

  @overload(bool)
  def setSaveToDisk(self, allow: bool) -> None:
    """
    Calls Qt's 'void QNetworkCacheMetaData::setSaveToDisk(bool allow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#setSaveToDisk

    Parameters
    ----------

    allow : bool
      Passed on as it is.
    """
    #  void QNetworkCacheMetaData::setSaveToDisk(bool allow)
    self.uglySide.call(
        'ritual_ZN21QNetworkCacheMetaData13setSaveToDiskEb', allow,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QNetworkCacheMetaData) -> bool:
    """
    Calls Qt's 'bool QNetworkCacheMetaData::operator==(const
    QNetworkCacheMetaData &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#operator==

    Parameters
    ----------

    other : QNetworkCacheMetaData
      Passed on as a value: Qt reads the C++ QNetworkCacheMetaData, which
      stays Python's own.
    """
    #  bool QNetworkCacheMetaData::operator==(const QNetworkCacheMetaData
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkCacheMetaDataeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QNetworkCacheMetaData) -> bool:
    """
    Calls Qt's 'bool QNetworkCacheMetaData::operator!=(const
    QNetworkCacheMetaData &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#operator!=

    Parameters
    ----------

    other : QNetworkCacheMetaData
      Passed on as a value: Qt reads the C++ QNetworkCacheMetaData, which
      stays Python's own.
    """
    #  bool QNetworkCacheMetaData::operator!=(const QNetworkCacheMetaData
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK21QNetworkCacheMetaDataneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
    Notes what was given, for Qt's
    'QNetworkCacheMetaData::QNetworkCacheMetaData()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#QNetworkCacheMetaData
    """
    #  QNetworkCacheMetaData::QNetworkCacheMetaData()
    self._noteCreation(QNetworkCacheMetaData, lambda: Rituals.call(
        'ritual_ZN21QNetworkCacheMetaDataC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QNetworkCacheMetaData) -> None:
    """
    Notes what was given, for Qt's
    'QNetworkCacheMetaData::QNetworkCacheMetaData(const QNetworkCacheMetaData
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkcachemetadata.html#QNetworkCacheMetaData

    Parameters
    ----------

    other : QNetworkCacheMetaData
      Passed on as a value: Qt reads the C++ QNetworkCacheMetaData, which
      stays Python's own.
    """
    #  QNetworkCacheMetaData::QNetworkCacheMetaData(const
    #      QNetworkCacheMetaData &other)
    self._noteCreation(QNetworkCacheMetaData, lambda: Rituals.call(
        'ritual_ZN21QNetworkCacheMetaDataC1ERKS_', self._valueOf(other),
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
  def attributes(*__, **_) -> Never:
    """
    Qt's 'AttributesMap QNetworkCacheMetaData::attributes() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkCacheMetaData.attributes' has no cute function yet. Qt's "
        "'AttributesMap QNetworkCacheMetaData::attributes() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def rawHeaders(*__, **_) -> Never:
    """
    Qt's 'RawHeaderList QNetworkCacheMetaData::rawHeaders() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkCacheMetaData.rawHeaders' has no cute function yet. Qt's "
        "'RawHeaderList QNetworkCacheMetaData::rawHeaders() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setAttributes(*__, **_) -> Never:
    """
    Qt's 'void QNetworkCacheMetaData::setAttributes(const AttributesMap
    &attributes)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkCacheMetaData.setAttributes' has no cute function yet. "
        "Qt's 'void QNetworkCacheMetaData::setAttributes(const "
        "AttributesMap &attributes)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setRawHeaders(*__, **_) -> Never:
    """
    Qt's 'void QNetworkCacheMetaData::setRawHeaders(const RawHeaderList
    &headers)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkCacheMetaData.setRawHeaders' has no cute function yet. "
        "Qt's 'void QNetworkCacheMetaData::setRawHeaders(const "
        "RawHeaderList &headers)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QNetworkCacheMetaData::swap(QNetworkCacheMetaData &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkCacheMetaData.swap' has no cute function yet. Qt's 'void "
        "QNetworkCacheMetaData::swap(QNetworkCacheMetaData &other)': takes "
        "a type Python has no way to hand over yet.")
