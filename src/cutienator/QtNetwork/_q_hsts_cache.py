"""
QHstsCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhsts_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QHstsCache to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl
  from . import QHstsPolicy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QHstsCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHstsCache: a plain Python object standing in front
  of one C++ QHstsCache.

  C++ hands a QHstsCache around as a copy, so every C++ QHstsCache behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHstsCache that has a ritual and that Python can
  call so far, 3 names in all: 'isKnownHost', 'clear', 'policies'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHstsCache::~QHstsCache()': the destructor: Python removes its C++
    QHstsCache by it, and has no other use for it.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 4 leans on 'QHstsCache; 1 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file.

  What to expect
  --------------

  - The C++ QHstsCache is created at the first use, not by 'QHstsCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHstsCache back gives a copy the ritual made for
    Python, in a new cute QHstsCache.
  - Each name of Qt's QHstsCache that has no cute function yet, 'setStore',
    'updateFromHeaders', 'updateFromPolicies', 'updateKnownHost', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHstsCache'

  #  Qt's '~QHstsCache()'. Naming it makes this a value class: Python owns
  #  every C++ QHstsCache behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QHstsCacheD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def isKnownHost(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QHstsCache::isKnownHost(const QUrl &url) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhstscache.html#isKnownHost

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QHstsCache::isKnownHost(const QUrl &url) const
    return self.uglySide.call(
        'ritual_ZNK10QHstsCache11isKnownHostERK4QUrl', self._valueOf(url),
    )

  def policies(self) -> QList[QHstsPolicy]:
    """
    Calls Qt's 'QList<QHstsPolicy> QHstsCache::policies() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhstscache.html#policies

    Returns
    -------

    QList[QHstsPolicy]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHstsPolicy> QHstsCache::policies() const
    address = self.uglySide.call('ritual_ZNK10QHstsCache8policiesEv')
    from . import QHstsPolicy
    return QList[QHstsPolicy]._cuteOwning(address)

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

  def clear(self) -> None:
    """
    Calls Qt's 'void QHstsCache::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qhstscache.html#clear
    """
    #  void QHstsCache::clear()
    self.uglySide.call('ritual_ZN10QHstsCache5clearEv')

  @staticmethod
  def setStore(*__, **_) -> Never:
    """
    Qt's 'void QHstsCache::setStore(class QHstsStore *store)': leans on
    'QHstsCache::updateKnownHost(QString const&, QDateTime const&, bool)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QHstsCache.setStore' has no cute function yet. Qt's 'void "
        "QHstsCache::setStore(class QHstsStore *store)': leans on "
        "'QHstsCache::updateKnownHost(QString const&, QDateTime const&, "
        "bool)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def updateFromHeaders(*__, **_) -> Never:
    """
    Qt's 'void QHstsCache::updateFromHeaders(const QHttpHeaders &headers,
    const QUrl &url)': leans on 'QHstsCache::updateKnownHost(QString const&,
    QDateTime const&, bool)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHstsCache.updateFromHeaders' has no cute function yet. Qt's "
        "'void QHstsCache::updateFromHeaders(const QHttpHeaders &headers, "
        "const QUrl &url)': leans on 'QHstsCache::updateKnownHost(QString "
        "const&, QDateTime const&, bool)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateFromPolicies(*__, **_) -> Never:
    """
    Qt's 'void QHstsCache::updateFromPolicies(const QList<QHstsPolicy>
    &hosts)': leans on 'QHstsCache::updateKnownHost(QString const&, QDateTime
    const&, bool)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QHstsCache.updateFromPolicies' has no cute function yet. Qt's "
        "'void QHstsCache::updateFromPolicies(const QList<QHstsPolicy> "
        "&hosts)': leans on 'QHstsCache::updateKnownHost(QString const&, "
        "QDateTime const&, bool)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def updateKnownHost(*__, **_) -> Never:
    """
    - Qt's 'void QHstsCache::updateKnownHost(const QString &hostName, const
      QDateTime &expires, bool includeSubDomains)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'is_valid_domain_name'.
    - Qt's 'void QHstsCache::updateKnownHost(const QUrl &url, const QDateTime
      &expires, bool includeSubDomains)': leans on
      'QHstsCache::updateKnownHost(QString const&, QDateTime const&, bool)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QHstsCache.updateKnownHost' has no cute function yet. Qt's 'void "
        "QHstsCache::updateKnownHost(const QString &hostName, const "
        "QDateTime &expires, bool includeSubDomains)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'is_valid_domain_name'. Qt's 'void "
        "QHstsCache::updateKnownHost(const QUrl &url, const QDateTime "
        "&expires, bool includeSubDomains)': leans on "
        "'QHstsCache::updateKnownHost(QString const&, QDateTime const&, "
        "bool)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
