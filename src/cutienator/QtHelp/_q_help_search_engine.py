"""
QHelpSearchEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpsearchengine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QHelpEngineCore, QHelpSearchQuery, QHelpSearchQueryWidget
  from . import QHelpSearchResult, QHelpSearchResultWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHelpEngineCore = WAIT['QHelpEngineCore']
  QHelpSearchQuery = WAIT['QHelpSearchQuery']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpSearchEngine(QObject):
  """
  The cute side of Qt's QHelpSearchEngine: a plain Python object standing in
  front of one C++ QHelpSearchEngine.

  It is built on the cute 'QObject', as Qt's QHelpSearchEngine is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpSearchEngine that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'queryWidget',
  'resultWidget', 'hitsCount', 'hitCount', 'query', 'searchResultCount',
  'searchResults', 'searchInput', 'reindexDocumentation', 'cancelIndexing',
  'search', 'cancelSearching', 'scheduleIndexDocumentation',
  'indexingStarted', 'indexingFinished', 'searchingStarted',
  'searchingFinished', 'indexDocumentation'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpSearchEngine::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QHelpSearchEngine::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QHelpSearchEngine::~QHelpSearchEngine()': the destructor: Python
    never removes a C++ QHelpSearchEngine.
  - Qt's 'QList<SearchHit> QHelpSearchEngine::hits(int start, int end)
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpSearchEngine is created at the first use, not by
    'QHelpSearchEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpSearchEngine.
  - Qt tells when it has removed the C++ QHelpSearchEngine. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHelpSearchEngine that has no cute function yet,
    'hits', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QHelpSearchEngine::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchengine.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpSearchEngine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QHelpSearchEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpSearchEngine'

  #  A C++ QHelpSearchEngine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHelpSearchEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpSearchEngine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpSearchEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpSearchEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hitsCount(self) -> int:
    """
    Calls Qt's 'int QHelpSearchEngine::hitsCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchengine.html#hitsCount
    """
    #  int QHelpSearchEngine::hitsCount() const
    return self.uglySide.call('ritual_ZNK17QHelpSearchEngine9hitsCountEv')

  def hitCount(self) -> int:
    """
    Calls Qt's 'int QHelpSearchEngine::hitCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchengine.html#hitCount
    """
    #  int QHelpSearchEngine::hitCount() const
    return self.uglySide.call('ritual_ZNK17QHelpSearchEngine8hitCountEv')

  def query(self) -> QList[QHelpSearchQuery]:
    """
    Calls Qt's 'QList<QHelpSearchQuery> QHelpSearchEngine::query() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchengine.html#query

    Returns
    -------

    QList[QHelpSearchQuery]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHelpSearchQuery> QHelpSearchEngine::query() const
    address = self.uglySide.call('ritual_ZNK17QHelpSearchEngine5queryEv')
    from . import QHelpSearchQuery
    return QList[QHelpSearchQuery]._cuteOwning(address)

  def searchResultCount(self) -> int:
    """
    Calls Qt's 'int QHelpSearchEngine::searchResultCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#searchResultCount
    """
    #  int QHelpSearchEngine::searchResultCount() const
    return self.uglySide.call(
        'ritual_ZNK17QHelpSearchEngine17searchResultCountEv',
    )

  @overload(int, int)
  def searchResults(self, start: int, end: int) -> QList[QHelpSearchResult]:
    """
    Calls Qt's 'QList<QHelpSearchResult> QHelpSearchEngine::searchResults(int
    start, int end) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#searchResults

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.

    Returns
    -------

    QList[QHelpSearchResult]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHelpSearchResult> QHelpSearchEngine::searchResults(int start,
    #      int end) const
    address = self.uglySide.call(
        'ritual_ZNK17QHelpSearchEngine13searchResultsEii', start, end,
    )
    from . import QHelpSearchResult
    return QList[QHelpSearchResult]._cuteOwning(address)

  def searchInput(self) -> str:
    """
    Calls Qt's 'QString QHelpSearchEngine::searchInput() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchengine.html#searchInput

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpSearchEngine::searchInput() const
    return self.uglySide.call('ritual_ZNK17QHelpSearchEngine11searchInputEv')

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

  @overload(QHelpEngineCore)
  @overload(NoneType)
  @overload(QHelpEngineCore, QObject)
  @overload(QHelpEngineCore, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      helpEngine: Optional[QHelpEngineCore],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHelpSearchEngine::QHelpSearchEngine(QHelpEngineCore *helpEngine,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#QHelpSearchEngine

    Parameters
    ----------

    helpEngine : Optional[QHelpEngineCore]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHelpSearchEngine::QHelpSearchEngine(QHelpEngineCore *helpEngine,
    #      QObject *parent)
    self._noteCreation(QHelpSearchEngine, lambda: Rituals.call(
        'ritual_ZN17QHelpSearchEngineC1EP15QHelpEngineCoreP7QObject',
        self._addressOf(helpEngine), self._addressOf(parent, 'QObject'),
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

  def queryWidget(self) -> Optional[QHelpSearchQueryWidget]:
    """
    Calls Qt's 'QHelpSearchQueryWidget *QHelpSearchEngine::queryWidget()'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchengine.html#queryWidget

    Returns
    -------

    Optional[QHelpSearchQueryWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHelpSearchQueryWidget *QHelpSearchEngine::queryWidget()
    address = self.uglySide.call(
        'ritual_ZN17QHelpSearchEngine11queryWidgetEv',
    )
    from . import QHelpSearchQueryWidget
    return QHelpSearchQueryWidget._cuteAt(address)

  def resultWidget(self) -> Optional[QHelpSearchResultWidget]:
    """
    Calls Qt's 'QHelpSearchResultWidget *QHelpSearchEngine::resultWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#resultWidget

    Returns
    -------

    Optional[QHelpSearchResultWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHelpSearchResultWidget *QHelpSearchEngine::resultWidget()
    address = self.uglySide.call(
        'ritual_ZN17QHelpSearchEngine12resultWidgetEv',
    )
    from . import QHelpSearchResultWidget
    return QHelpSearchResultWidget._cuteAt(address)

  def reindexDocumentation(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::reindexDocumentation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#reindexDocumentation
    """
    #  void QHelpSearchEngine::reindexDocumentation()
    self.uglySide.call(
        'ritual_ZN17QHelpSearchEngine20reindexDocumentationEv',
    )

  def cancelIndexing(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::cancelIndexing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#cancelIndexing
    """
    #  void QHelpSearchEngine::cancelIndexing()
    self.uglySide.call('ritual_ZN17QHelpSearchEngine14cancelIndexingEv')

  @overload(QList[QHelpSearchQuery])
  def search(self, queryList: QList[QHelpSearchQuery]) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::search(const QList<QHelpSearchQuery>
    &queryList)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchengine.html#search

    Parameters
    ----------

    queryList : QList[QHelpSearchQuery]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHelpSearchEngine::search(const QList<QHelpSearchQuery>
    #      &queryList)
    self.uglySide.call(
        'ritual_ZN17QHelpSearchEngine6searchERK5QListI16QHelpSearchQueryE',
        self._valueOf(queryList),
    )

  @overload(str)
  def search(self, searchInput: str) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::search(const QString &searchInput)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchengine.html#search

    Parameters
    ----------

    searchInput : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpSearchEngine::search(const QString &searchInput)
    self.uglySide.call(
        'ritual_ZN17QHelpSearchEngine6searchERK7QString', searchInput,
    )

  def cancelSearching(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::cancelSearching()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#cancelSearching
    """
    #  void QHelpSearchEngine::cancelSearching()
    self.uglySide.call('ritual_ZN17QHelpSearchEngine15cancelSearchingEv')

  def scheduleIndexDocumentation(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::scheduleIndexDocumentation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#scheduleIndexDocumentation
    """
    #  void QHelpSearchEngine::scheduleIndexDocumentation()
    self.uglySide.call(
        'ritual_ZN17QHelpSearchEngine26scheduleIndexDocumentationEv',
    )

  def indexingStarted(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::indexingStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#indexingStarted
    """
    #  void QHelpSearchEngine::indexingStarted()
    self.uglySide.call('ritual_ZN17QHelpSearchEngine15indexingStartedEv')

  def indexingFinished(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::indexingFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#indexingFinished
    """
    #  void QHelpSearchEngine::indexingFinished()
    self.uglySide.call('ritual_ZN17QHelpSearchEngine16indexingFinishedEv')

  def searchingStarted(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::searchingStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#searchingStarted
    """
    #  void QHelpSearchEngine::searchingStarted()
    self.uglySide.call('ritual_ZN17QHelpSearchEngine16searchingStartedEv')

  @overload(int)
  def searchingFinished(self, searchResultCount: int) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::searchingFinished(int
    searchResultCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#searchingFinished

    Parameters
    ----------

    searchResultCount : int
      Passed on as it is.
    """
    #  void QHelpSearchEngine::searchingFinished(int searchResultCount)
    self.uglySide.call(
        'ritual_ZN17QHelpSearchEngine17searchingFinishedEi',
        searchResultCount,
    )

  def indexDocumentation(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngine::indexDocumentation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchengine.html#indexDocumentation
    """
    #  void QHelpSearchEngine::indexDocumentation()
    self.uglySide.call('ritual_ZN17QHelpSearchEngine18indexDocumentationEv')

  @staticmethod
  def hits(*__, **_) -> Never:
    """
    Qt's 'QList<SearchHit> QHelpSearchEngine::hits(int start, int end)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QHelpSearchEngine.hits' has no cute function yet. Qt's "
        "'QList<SearchHit> QHelpSearchEngine::hits(int start, int end) "
        "const': gives a type Python has no way to take yet.")
