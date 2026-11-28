"""
QHelpSearchEngineCore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpsearchenginecore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QHelpEngineCore, QHelpSearchResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHelpEngineCore = WAIT['QHelpEngineCore']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpSearchEngineCore(QObject):
  """
  The cute side of Qt's QHelpSearchEngineCore: a plain Python object standing
  in front of one C++ QHelpSearchEngineCore.

  It is built on the cute 'QObject', as Qt's QHelpSearchEngineCore is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpSearchEngineCore that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr',
  'searchResultCount', 'searchResults', 'searchInput',
  'reindexDocumentation', 'cancelIndexing', 'search', 'cancelSearching',
  'scheduleIndexDocumentation', 'indexingStarted', 'indexingFinished',
  'searchingStarted', 'searchingFinished'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpSearchEngineCore::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QHelpSearchEngineCore::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QHelpSearchEngineCorePrivate *QHelpSearchEngineCore::d_func()':
    gives 'QHelpSearchEngineCorePrivate', which has no cute class yet.
  - Qt's 'const QHelpSearchEngineCorePrivate *QHelpSearchEngineCore::d_func()
    const': gives 'QHelpSearchEngineCorePrivate', which has no cute class
    yet.
  - Qt's 'QHelpSearchEngineCore::~QHelpSearchEngineCore()': the destructor:
    Python never removes a C++ QHelpSearchEngineCore.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpSearchEngineCore is created at the first use, not by
    'QHelpSearchEngineCore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpSearchEngineCore.
  - Qt tells when it has removed the C++ QHelpSearchEngineCore. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QHelpSearchEngineCore::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchenginecore.html#tr

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
    #  QString QHelpSearchEngineCore::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QHelpSearchEngineCore2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpSearchEngineCore'

  #  A C++ QHelpSearchEngineCore Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHelpSearchEngineCore'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpSearchEngineCore::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpSearchEngineCore::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QHelpSearchEngineCore10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def searchResultCount(self) -> int:
    """
    Calls Qt's 'int QHelpSearchEngineCore::searchResultCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#searchResultCount
    """
    #  int QHelpSearchEngineCore::searchResultCount() const
    return self.uglySide.call(
        'ritual_ZNK21QHelpSearchEngineCore17searchResultCountEv',
    )

  @overload(int, int)
  def searchResults(self, start: int, end: int) -> QList[QHelpSearchResult]:
    """
    Calls Qt's 'QList<QHelpSearchResult>
    QHelpSearchEngineCore::searchResults(int start, int end) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#searchResults

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
    #  QList<QHelpSearchResult> QHelpSearchEngineCore::searchResults(int
    #      start, int end) const
    address = self.uglySide.call(
        'ritual_ZNK21QHelpSearchEngineCore13searchResultsEii', start, end,
    )
    from . import QHelpSearchResult
    return QList[QHelpSearchResult]._cuteOwning(address)

  def searchInput(self) -> str:
    """
    Calls Qt's 'QString QHelpSearchEngineCore::searchInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#searchInput

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpSearchEngineCore::searchInput() const
    return self.uglySide.call(
        'ritual_ZNK21QHelpSearchEngineCore11searchInputEv',
    )

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
    'QHelpSearchEngineCore::QHelpSearchEngineCore(QHelpEngineCore
    *helpEngine, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#QHelpSearchEngineCore

    Parameters
    ----------

    helpEngine : Optional[QHelpEngineCore]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHelpSearchEngineCore::QHelpSearchEngineCore(QHelpEngineCore
    #      *helpEngine, QObject *parent)
    self._noteCreation(QHelpSearchEngineCore, lambda: Rituals.call(
        'ritual_ZN21QHelpSearchEngineCoreC1EP15QHelpEngineCoreP7QObject',
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

  def reindexDocumentation(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngineCore::reindexDocumentation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#reindexDocumentation
    """
    #  void QHelpSearchEngineCore::reindexDocumentation()
    self.uglySide.call(
        'ritual_ZN21QHelpSearchEngineCore20reindexDocumentationEv',
    )

  def cancelIndexing(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngineCore::cancelIndexing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#cancelIndexing
    """
    #  void QHelpSearchEngineCore::cancelIndexing()
    self.uglySide.call('ritual_ZN21QHelpSearchEngineCore14cancelIndexingEv')

  @overload(str)
  def search(self, searchInput: str) -> None:
    """
    Calls Qt's 'void QHelpSearchEngineCore::search(const QString
    &searchInput)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchenginecore.html#search

    Parameters
    ----------

    searchInput : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpSearchEngineCore::search(const QString &searchInput)
    self.uglySide.call(
        'ritual_ZN21QHelpSearchEngineCore6searchERK7QString', searchInput,
    )

  def cancelSearching(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngineCore::cancelSearching()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#cancelSearching
    """
    #  void QHelpSearchEngineCore::cancelSearching()
    self.uglySide.call('ritual_ZN21QHelpSearchEngineCore15cancelSearchingEv')

  def scheduleIndexDocumentation(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngineCore::scheduleIndexDocumentation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html
    """
    #  void QHelpSearchEngineCore::scheduleIndexDocumentation()
    self.uglySide.call(
        'ritual_ZN21QHelpSearchEngineCore26scheduleIndexDocumentationEv',
    )

  def indexingStarted(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngineCore::indexingStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#indexingStarted
    """
    #  void QHelpSearchEngineCore::indexingStarted()
    self.uglySide.call('ritual_ZN21QHelpSearchEngineCore15indexingStartedEv')

  def indexingFinished(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngineCore::indexingFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#indexingFinished
    """
    #  void QHelpSearchEngineCore::indexingFinished()
    self.uglySide.call(
        'ritual_ZN21QHelpSearchEngineCore16indexingFinishedEv',
    )

  def searchingStarted(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngineCore::searchingStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#searchingStarted
    """
    #  void QHelpSearchEngineCore::searchingStarted()
    self.uglySide.call(
        'ritual_ZN21QHelpSearchEngineCore16searchingStartedEv',
    )

  def searchingFinished(self) -> None:
    """
    Calls Qt's 'void QHelpSearchEngineCore::searchingFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchenginecore.html#searchingFinished
    """
    #  void QHelpSearchEngineCore::searchingFinished()
    self.uglySide.call(
        'ritual_ZN21QHelpSearchEngineCore17searchingFinishedEv',
    )
