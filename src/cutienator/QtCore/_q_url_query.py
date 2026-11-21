"""
QUrlQuery binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qurlquery.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QUrl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']


class QUrlQuery(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUrlQuery: a plain Python object standing in front of
  one C++ QUrlQuery.

  C++ hands a QUrlQuery around as a copy, so every C++ QUrlQuery behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QUrlQuery that has a ritual and that Python can call
  so far, 14 names in all: 'isEmpty', 'isDetached', 'clear', 'query',
  'setQuery', 'toString', 'setQueryDelimiters', 'queryValueDelimiter',
  'queryPairDelimiter', 'hasQueryItem', 'addQueryItem', 'removeQueryItem',
  'queryItemValue', 'removeAllQueryItems'. It can be made from Python, in 4
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUrlQuery::~QUrlQuery()': the destructor: Python removes its C++
    QUrlQuery by it, and has no other use for it.

  What has no ritual
  ------------------

  11 of the 30 functions Qt declares: 11 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QUrlQuery is created at the first use, not by 'QUrlQuery(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUrlQuery back gives a copy the ritual made for
    Python, in a new cute QUrlQuery.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUrlQuery'

  #  Qt's '~QUrlQuery()'. Naming it makes this a value class: Python owns
  #  every C++ QUrlQuery behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QUrlQueryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QUrlQuery::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#isEmpty
    """
    #  bool QUrlQuery::isEmpty() const
    return self.uglySide.call('ritual_ZNK9QUrlQuery7isEmptyEv')

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QUrlQuery::isDetached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#isDetached
    """
    #  bool QUrlQuery::isDetached() const
    return self.uglySide.call('ritual_ZNK9QUrlQuery10isDetachedEv')

  @overload()
  @overload(QUrl.ComponentFormattingOptions)
  def query(
      self,
      encoding: QUrl.ComponentFormattingOptions = (
          QUrl.ComponentFormattingOptions.PrettyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrlQuery::query(QUrl::ComponentFormattingOptions
    encoding) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#query

    Parameters
    ----------

    encoding : QUrl.ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QUrl.ComponentFormattingOptions.PrettyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrlQuery::query(QUrl::ComponentFormattingOptions encoding)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9QUrlQuery5queryE6QFlagsIN4QUrl25ComponentFormattingOpti'
        'onEE',
        encoding.value,
    )

  @overload()
  @overload(QUrl.ComponentFormattingOptions)
  def toString(
      self,
      encoding: QUrl.ComponentFormattingOptions = (
          QUrl.ComponentFormattingOptions.PrettyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrlQuery::toString(QUrl::ComponentFormattingOptions
    encoding) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#toString

    Parameters
    ----------

    encoding : QUrl.ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QUrl.ComponentFormattingOptions.PrettyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrlQuery::toString(QUrl::ComponentFormattingOptions encoding)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9QUrlQuery8toStringE6QFlagsIN4QUrl25ComponentFormattingO'
        'ptionEE',
        encoding.value,
    )

  def queryValueDelimiter(self) -> QChar:
    """
    Calls Qt's 'QChar QUrlQuery::queryValueDelimiter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#queryValueDelimiter

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QUrlQuery::queryValueDelimiter() const
    address = self.uglySide.call(
        'ritual_ZNK9QUrlQuery19queryValueDelimiterEv',
    )
    from . import QChar
    return QChar._cuteOwning(address)

  def queryPairDelimiter(self) -> QChar:
    """
    Calls Qt's 'QChar QUrlQuery::queryPairDelimiter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#queryPairDelimiter

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QUrlQuery::queryPairDelimiter() const
    address = self.uglySide.call(
        'ritual_ZNK9QUrlQuery18queryPairDelimiterEv',
    )
    from . import QChar
    return QChar._cuteOwning(address)

  @overload(str)
  def hasQueryItem(self, key: str) -> bool:
    """
    Calls Qt's 'bool QUrlQuery::hasQueryItem(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#hasQueryItem

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QUrlQuery::hasQueryItem(const QString &key) const
    return self.uglySide.call(
        'ritual_ZNK9QUrlQuery12hasQueryItemERK7QString', key,
    )

  @overload(str)
  @overload(str, QUrl.ComponentFormattingOptions)
  def queryItemValue(
      self,
      key: str,
      encoding: QUrl.ComponentFormattingOptions = (
          QUrl.ComponentFormattingOptions.PrettyDecoded),
  ) -> str:
    """
    Calls Qt's 'QString QUrlQuery::queryItemValue(const QString &key,
    QUrl::ComponentFormattingOptions encoding) const'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#queryItemValue

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    encoding : QUrl.ComponentFormattingOptions
      Passed on as its number. May be left out, as in Qt: it is then
      QUrl.ComponentFormattingOptions.PrettyDecoded.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUrlQuery::queryItemValue(const QString &key,
    #      QUrl::ComponentFormattingOptions encoding) const
    return self.uglySide.call(
        'ritual_ZNK9QUrlQuery14queryItemValueERK7QString6QFlagsIN4QUrl25Com'
        'ponentFormattingOptionEE',
        key, encoding.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setQuery(self, queryString: str) -> None:
    """
    Calls Qt's 'void QUrlQuery::setQuery(const QString &queryString)'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#setQuery

    Parameters
    ----------

    queryString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUrlQuery::setQuery(const QString &queryString)
    self.uglySide.call(
        'ritual_ZN9QUrlQuery8setQueryERK7QString', queryString,
    )

  @overload(QChar, QChar)
  def setQueryDelimiters(
      self,
      valueDelimiter: QChar,
      pairDelimiter: QChar,
  ) -> None:
    """
    Calls Qt's 'void QUrlQuery::setQueryDelimiters(QChar valueDelimiter,
    QChar pairDelimiter)'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#setQueryDelimiters

    Parameters
    ----------

    valueDelimiter : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    pairDelimiter : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  void QUrlQuery::setQueryDelimiters(QChar valueDelimiter, QChar
    #      pairDelimiter)
    self.uglySide.call(
        'ritual_ZN9QUrlQuery18setQueryDelimitersE5QCharS0_',
        self._valueOf(valueDelimiter), self._valueOf(pairDelimiter),
    )

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
    Notes what was given, for Qt's 'QUrlQuery::QUrlQuery()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#QUrlQuery
    """
    #  QUrlQuery::QUrlQuery()
    self._noteCreation(QUrlQuery, lambda: Rituals.call(
        'ritual_ZN9QUrlQueryC1Ev',
    ))

  @overload(QUrl)
  def __init__(self, url: QUrl) -> None:
    """
    Notes what was given, for Qt's 'QUrlQuery::QUrlQuery(const QUrl &url)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#QUrlQuery

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QUrlQuery::QUrlQuery(const QUrl &url)
    self._noteCreation(QUrlQuery, lambda: Rituals.call(
        'ritual_ZN9QUrlQueryC1ERK4QUrl', self._valueOf(url),
    ))

  @overload(str)
  def __init__(self, queryString: str) -> None:
    """
    Notes what was given, for Qt's 'QUrlQuery::QUrlQuery(const QString
    &queryString)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#QUrlQuery

    Parameters
    ----------

    queryString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QUrlQuery::QUrlQuery(const QString &queryString)
    self._noteCreation(QUrlQuery, lambda: Rituals.call(
        'ritual_ZN9QUrlQueryC1ERK7QString', queryString,
    ))

  @overload(THIS)
  def __init__(self, other: QUrlQuery) -> None:
    """
    Notes what was given, for Qt's 'QUrlQuery::QUrlQuery(const QUrlQuery
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#QUrlQuery

    Parameters
    ----------

    other : QUrlQuery
      Passed on as a value: Qt reads the C++ QUrlQuery, which stays Python's
      own.
    """
    #  QUrlQuery::QUrlQuery(const QUrlQuery &other)
    self._noteCreation(QUrlQuery, lambda: Rituals.call(
        'ritual_ZN9QUrlQueryC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QUrlQuery::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#clear
    """
    #  void QUrlQuery::clear()
    self.uglySide.call('ritual_ZN9QUrlQuery5clearEv')

  @overload(str, str)
  def addQueryItem(self, key: str, value: str) -> None:
    """
    Calls Qt's 'void QUrlQuery::addQueryItem(const QString &key, const
    QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#addQueryItem

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUrlQuery::addQueryItem(const QString &key, const QString &value)
    self.uglySide.call(
        'ritual_ZN9QUrlQuery12addQueryItemERK7QStringS2_', key, value,
    )

  @overload(str)
  def removeQueryItem(self, key: str) -> None:
    """
    Calls Qt's 'void QUrlQuery::removeQueryItem(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#removeQueryItem

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUrlQuery::removeQueryItem(const QString &key)
    self.uglySide.call(
        'ritual_ZN9QUrlQuery15removeQueryItemERK7QString', key,
    )

  @overload(str)
  def removeAllQueryItems(self, key: str) -> None:
    """
    Calls Qt's 'void QUrlQuery::removeAllQueryItems(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qurlquery.html#removeAllQueryItems

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUrlQuery::removeAllQueryItems(const QString &key)
    self.uglySide.call(
        'ritual_ZN9QUrlQuery19removeAllQueryItemsERK7QString', key,
    )
