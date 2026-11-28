"""
QNetworkHeadersPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkrequest_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QNetworkHeadersPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QByteArrayView, QDateTime
  from . import QHttpHeaders, QNetworkCookie
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QDateTime = WAIT['QDateTime']
  QNetworkCookie = WAIT['QNetworkCookie']


class QNetworkHeadersPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNetworkHeadersPrivate: a plain Python object
  standing in front of one C++ QNetworkHeadersPrivate.

  C++ hands a QNetworkHeadersPrivate around as a copy, so every C++
  QNetworkHeadersPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QNetworkHeadersPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'rawHeadersKeys', 'rawHeader',
  'headers', 'clearHeaders', 'fromHttpDate', 'toHttpDate', 'fromCookieList',
  'invalidateHeaderCache'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const RawHeadersList &QNetworkHeadersPrivate::allRawHeaders()
    const': gives a type Python has no way to take yet.
  - Qt's 'std::optional<qint64> QNetworkHeadersPrivate::toInt(QByteArrayView
    value)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<NetworkCookieList>
    QNetworkHeadersPrivate::toSetCookieList(const QList<QByteArray>
    &values)': gives a type Python has no way to take yet.
  - Qt's 'std::optional<NetworkCookieList>
    QNetworkHeadersPrivate::toCookieList(const QList<QByteArray> &values)':
    gives a type Python has no way to take yet.
  - Qt's 'RawHeadersList QNetworkHeadersPrivate::fromHttpToRaw(const
    QHttpHeaders &headers)': gives a type Python has no way to take yet.
  - Qt's 'QHttpHeaders QNetworkHeadersPrivate::fromRawToHttp(const
    RawHeadersList &raw)': takes a type Python has no way to hand over yet.
  - Qt's 'QNetworkHeadersPrivate::~QNetworkHeadersPrivate()': the destructor:
    Python removes its C++ QNetworkHeadersPrivate by it, and has no other use
    for it.

  What has no ritual
  ------------------

  8 of the 23 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QNetworkHeadersPrivate.

  What to expect
  --------------

  - The C++ QNetworkHeadersPrivate is created at the first use, not by
    'QNetworkHeadersPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QNetworkHeadersPrivate back gives a copy the ritual
    made for Python, in a new cute QNetworkHeadersPrivate.
  - Each name of Qt's QNetworkHeadersPrivate that has no cute function yet,
    'allRawHeaders', 'fromHttpToRaw', 'fromRawToHttp', 'parseAndSetHeader',
    'setCookedFromHttp', 'setCookedHeader', 'setHeader', 'setHeaders',
    'setRawHeader', 'toCookieList', 'toInt', 'toSetCookieList', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArrayView)
  def fromHttpDate(value: QByteArrayView) -> QDateTime:
    """
    Calls Qt's 'QDateTime QNetworkHeadersPrivate::fromHttpDate(QByteArrayView
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkheadersprivate.html#fromHttpDate

    Parameters
    ----------

    value : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QNetworkHeadersPrivate::fromHttpDate(QByteArrayView value)
    address = Rituals.call(
        'ritual_ZN22QNetworkHeadersPrivate12fromHttpDateE14QByteArrayView',
        CuteMixin._valueOf(value),
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @staticmethod
  @overload(QDateTime)
  def toHttpDate(dt: QDateTime) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkHeadersPrivate::toHttpDate(const QDateTime
    &dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkheadersprivate.html#toHttpDate

    Parameters
    ----------

    dt : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkHeadersPrivate::toHttpDate(const QDateTime &dt)
    address = Rituals.call(
        'ritual_ZN22QNetworkHeadersPrivate10toHttpDateERK9QDateTime',
        CuteMixin._valueOf(dt),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QList[QNetworkCookie])
  def fromCookieList(cookies: QList[QNetworkCookie]) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkHeadersPrivate::fromCookieList(const
    NetworkCookieList &cookies)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkheadersprivate.html#fromCookieList

    Parameters
    ----------

    cookies : QList[QNetworkCookie]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkHeadersPrivate::fromCookieList(const
    #      NetworkCookieList &cookies)
    address = Rituals.call(
        'ritual_ZN22QNetworkHeadersPrivate14fromCookieListERK5QListI14QNetw'
        'orkCookieE',
        CuteMixin._valueOf(cookies),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkHeadersPrivate'

  #  Qt's '~QNetworkHeadersPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QNetworkHeadersPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QNetworkHeadersPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rawHeadersKeys(self) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QNetworkHeadersPrivate::rawHeadersKeys()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkheadersprivate.html#rawHeadersKeys

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QNetworkHeadersPrivate::rawHeadersKeys() const
    address = self._callAs(
        'QNetworkHeadersPrivate',
        'ritual_ZNK22QNetworkHeadersPrivate14rawHeadersKeysEv',
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(str)
  def rawHeader(self, headerName: str) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNetworkHeadersPrivate::rawHeader(QAnyStringView
    headerName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkheadersprivate.html#rawHeader

    Parameters
    ----------

    headerName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNetworkHeadersPrivate::rawHeader(QAnyStringView
    #      headerName) const
    address = self._callAs(
        'QNetworkHeadersPrivate',
        'ritual_ZNK22QNetworkHeadersPrivate9rawHeaderE14QAnyStringView',
        headerName,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def headers(self) -> QHttpHeaders:
    """
    Calls Qt's 'QHttpHeaders QNetworkHeadersPrivate::headers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkheadersprivate.html#headers

    Returns
    -------

    QHttpHeaders
      A new cute QHttpHeaders around the copy Qt gave back. Python owns it.
    """
    #  QHttpHeaders QNetworkHeadersPrivate::headers() const
    address = self._callAs(
        'QNetworkHeadersPrivate',
        'ritual_ZNK22QNetworkHeadersPrivate7headersEv',
    )
    from . import QHttpHeaders
    return QHttpHeaders._cuteOwning(address)

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

  def clearHeaders(self) -> None:
    """
    Calls Qt's 'void QNetworkHeadersPrivate::clearHeaders()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkheadersprivate.html#clearHeaders
    """
    #  void QNetworkHeadersPrivate::clearHeaders()
    self._callAs(
        'QNetworkHeadersPrivate',
        'ritual_ZN22QNetworkHeadersPrivate12clearHeadersEv',
    )

  def invalidateHeaderCache(self) -> None:
    """
    Calls Qt's 'void QNetworkHeadersPrivate::invalidateHeaderCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkheadersprivate.html#invalidateHeaderCache
    """
    #  void QNetworkHeadersPrivate::invalidateHeaderCache()
    self._callAs(
        'QNetworkHeadersPrivate',
        'ritual_ZN22QNetworkHeadersPrivate21invalidateHeaderCacheEv',
    )

  @staticmethod
  def allRawHeaders(*__, **_) -> Never:
    """
    Qt's 'const RawHeadersList &QNetworkHeadersPrivate::allRawHeaders()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.allRawHeaders' has no cute function yet. "
        "Qt's 'const RawHeadersList "
        "&QNetworkHeadersPrivate::allRawHeaders() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def fromHttpToRaw(*__, **_) -> Never:
    """
    Qt's 'RawHeadersList QNetworkHeadersPrivate::fromHttpToRaw(const
    QHttpHeaders &headers)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.fromHttpToRaw' has no cute function yet. "
        "Qt's 'RawHeadersList QNetworkHeadersPrivate::fromHttpToRaw(const "
        "QHttpHeaders &headers)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def fromRawToHttp(*__, **_) -> Never:
    """
    Qt's 'QHttpHeaders QNetworkHeadersPrivate::fromRawToHttp(const
    RawHeadersList &raw)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.fromRawToHttp' has no cute function yet. "
        "Qt's 'QHttpHeaders QNetworkHeadersPrivate::fromRawToHttp(const "
        "RawHeadersList &raw)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def parseAndSetHeader(*__, **_) -> Never:
    """
    - Qt's 'void QNetworkHeadersPrivate::parseAndSetHeader(QByteArrayView
      key, QByteArrayView value)': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'parseHeaderName'.
    - Qt's 'void
      QNetworkHeadersPrivate::parseAndSetHeader(QNetworkRequest::KnownHeaders
      key, QByteArrayView value)': Qt's library has no name for it, and its
      code in Qt's source does not compile apart from its file: use of
      undeclared identifier 'parseHeaderValue'.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.parseAndSetHeader' has no cute function "
        "yet. Qt's 'void "
        "QNetworkHeadersPrivate::parseAndSetHeader(QByteArrayView key, "
        "QByteArrayView value)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'parseHeaderName'. Qt's 'void "
        "QNetworkHeadersPrivate::parseAndSetHeader(QNetworkRequest::KnownHea"
        "ders key, QByteArrayView value)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'parseHeaderValue'.")

  @staticmethod
  def setCookedFromHttp(*__, **_) -> Never:
    """
    Qt's 'void QNetworkHeadersPrivate::setCookedFromHttp(const QHttpHeaders
    &newHeaders)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: no matching function for
    call to 'parseHeaderValue'.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.setCookedFromHttp' has no cute function "
        "yet. Qt's 'void QNetworkHeadersPrivate::setCookedFromHttp(const "
        "QHttpHeaders &newHeaders)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: no "
        "matching function for call to 'parseHeaderValue'.")

  @staticmethod
  def setCookedHeader(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkHeadersPrivate::setCookedHeader(QNetworkRequest::KnownHeaders
    header, const QVariant &value)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'toWellKnownHeader'; did you mean
    'QHttpHeaders::WellKnownHeader'?.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.setCookedHeader' has no cute function yet. "
        "Qt's 'void "
        "QNetworkHeadersPrivate::setCookedHeader(QNetworkRequest::KnownHeade"
        "rs header, const QVariant &value)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'toWellKnownHeader'; did you "
        "mean 'QHttpHeaders::WellKnownHeader'?.")

  @staticmethod
  def setHeader(*__, **_) -> Never:
    """
    Qt's 'void
    QNetworkHeadersPrivate::setHeader(QHttpHeaders::WellKnownHeader name,
    QByteArrayView value)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'toKnownHeader'; did you mean
    'QNetworkRequest::KnownHeaders'?.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.setHeader' has no cute function yet. Qt's "
        "'void "
        "QNetworkHeadersPrivate::setHeader(QHttpHeaders::WellKnownHeader "
        "name, QByteArrayView value)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'toKnownHeader'; did you mean "
        "'QNetworkRequest::KnownHeaders'?.")

  @staticmethod
  def setHeaders(*__, **_) -> Never:
    """
    - Qt's 'void QNetworkHeadersPrivate::setHeaders(const QHttpHeaders
      &newHeaders)': leans on
      'QNetworkHeadersPrivate::setCookedFromHttp(QHttpHeaders const&)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    - Qt's 'void QNetworkHeadersPrivate::setHeaders(QHttpHeaders
      &&newHeaders)': leans on
      'QNetworkHeadersPrivate::setCookedFromHttp(QHttpHeaders const&)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.setHeaders' has no cute function yet. Qt's "
        "'void QNetworkHeadersPrivate::setHeaders(const QHttpHeaders "
        "&newHeaders)': leans on "
        "'QNetworkHeadersPrivate::setCookedFromHttp(QHttpHeaders const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken. Qt's 'void "
        "QNetworkHeadersPrivate::setHeaders(QHttpHeaders &&newHeaders)': "
        "leans on 'QNetworkHeadersPrivate::setCookedFromHttp(QHttpHeaders "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setRawHeader(*__, **_) -> Never:
    """
    Qt's 'void QNetworkHeadersPrivate::setRawHeader(const QByteArray &key,
    const QByteArray &value)': leans on
    'QNetworkHeadersPrivate::parseAndSetHeader(QByteArrayView,
    QByteArrayView)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.setRawHeader' has no cute function yet. "
        "Qt's 'void QNetworkHeadersPrivate::setRawHeader(const QByteArray "
        "&key, const QByteArray &value)': leans on "
        "'QNetworkHeadersPrivate::parseAndSetHeader(QByteArrayView, "
        "QByteArrayView)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def toCookieList(*__, **_) -> Never:
    """
    Qt's 'std::optional<NetworkCookieList>
    QNetworkHeadersPrivate::toCookieList(const QList<QByteArray> &values)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.toCookieList' has no cute function yet. "
        "Qt's 'std::optional<NetworkCookieList> "
        "QNetworkHeadersPrivate::toCookieList(const QList<QByteArray> "
        "&values)': gives a type Python has no way to take yet.")

  @staticmethod
  def toInt(*__, **_) -> Never:
    """
    Qt's 'std::optional<qint64> QNetworkHeadersPrivate::toInt(QByteArrayView
    value)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.toInt' has no cute function yet. Qt's "
        "'std::optional<qint64> "
        "QNetworkHeadersPrivate::toInt(QByteArrayView value)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def toSetCookieList(*__, **_) -> Never:
    """
    Qt's 'std::optional<NetworkCookieList>
    QNetworkHeadersPrivate::toSetCookieList(const QList<QByteArray>
    &values)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNetworkHeadersPrivate.toSetCookieList' has no cute function yet. "
        "Qt's 'std::optional<NetworkCookieList> "
        "QNetworkHeadersPrivate::toSetCookieList(const QList<QByteArray> "
        "&values)': gives a type Python has no way to take yet.")
