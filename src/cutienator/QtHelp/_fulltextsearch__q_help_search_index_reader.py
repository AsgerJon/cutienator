"""
fulltextsearch::QHelpSearchIndexReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/6.12.0/QtHelp/private/qhelpsearchindexreader_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means fulltextsearch::QHelpSearchIndexReader to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QList, QThread

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QHelpSearchResult


class QHelpSearchIndexReader(QThread):
  """
  The cute side of Qt's fulltextsearch::QHelpSearchIndexReader: a plain
  Python object standing in front of one C++
  fulltextsearch::QHelpSearchIndexReader.

  It is built on the cute 'QThread', as Qt's
  fulltextsearch::QHelpSearchIndexReader is built on Qt's QThread, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's fulltextsearch::QHelpSearchIndexReader that has a
  ritual and that Python can call so far, 8 names in all: 'metaObject',
  'cancelSearching', 'search', 'searchResultCount', 'searchResults',
  'searchingStarted', 'searchingFinished', 'run'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *fulltextsearch::QHelpSearchIndexReader::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    fulltextsearch::QHelpSearchIndexReader::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'fulltextsearch::QHelpSearchIndexReader::~QHelpSearchIndexReader()':
    the destructor: Python never removes a C++
    fulltextsearch::QHelpSearchIndexReader.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 2 not a gap; 1 leans on 'fulltextsearch.

  What to expect
  --------------

  - The C++ fulltextsearch::QHelpSearchIndexReader is created at the first
    use, not by 'fulltextsearch::QHelpSearchIndexReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ fulltextsearch::QHelpSearchIndexReader.
  - Qt tells when it has removed the C++
    fulltextsearch::QHelpSearchIndexReader. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'fulltextsearch::QHelpSearchIndexReader'

  #  A C++ fulltextsearch::QHelpSearchIndexReader Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_fulltextsearch_QHelpSearchIndexReader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *fulltextsearch::QHelpSearchIndexReader::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/fulltextsearch-qhelpsearchindexreader.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *fulltextsearch::QHelpSearchIndexReader::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK14fulltextsearch22QHelpSearchIndexReader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def searchResultCount(self) -> int:
    """
    Calls Qt's 'int
    fulltextsearch::QHelpSearchIndexReader::searchResultCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/fulltextsearch-qhelpsearchindexreader.html
    """
    #  int fulltextsearch::QHelpSearchIndexReader::searchResultCount() const
    return self.uglySide.call(
        'ritual_ZNK14fulltextsearch22QHelpSearchIndexReader17searchResultCo'
        'untEv',
    )

  @overload(int, int)
  def searchResults(self, start: int, end: int) -> QList[QHelpSearchResult]:
    """
    Calls Qt's 'QList<QHelpSearchResult>
    fulltextsearch::QHelpSearchIndexReader::searchResults(int start, int end)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/fulltextsearch-qhelpsearchindexreader.html

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
    #  QList<QHelpSearchResult>
    #      fulltextsearch::QHelpSearchIndexReader::searchResults(int start,
    #      int end) const
    address = self.uglySide.call(
        'ritual_ZNK14fulltextsearch22QHelpSearchIndexReader13searchResultsE'
        'ii',
        start, end,
    )
    from . import QHelpSearchResult
    return QList[QHelpSearchResult]._cuteOwning(address)

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

  def cancelSearching(self) -> None:
    """
    Calls Qt's 'void
    fulltextsearch::QHelpSearchIndexReader::cancelSearching()'.

    Qt's own words:
    https://doc.qt.io/qt-6/fulltextsearch-qhelpsearchindexreader.html
    """
    #  void fulltextsearch::QHelpSearchIndexReader::cancelSearching()
    self.uglySide.call(
        'ritual_ZN14fulltextsearch22QHelpSearchIndexReader15cancelSearching'
        'Ev',
    )

  @overload(str, str, str)
  @overload(str, str, str, bool)
  def search(
      self,
      collectionFile: str,
      indexFilesFolder: str,
      searchInput: str,
      usesFilterEngine: bool = False,
  ) -> None:
    """
    Calls Qt's 'void fulltextsearch::QHelpSearchIndexReader::search(const
    QString &collectionFile, const QString &indexFilesFolder, const QString
    &searchInput, bool usesFilterEngine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/fulltextsearch-qhelpsearchindexreader.html#search

    Parameters
    ----------

    collectionFile : str
      Passed on as it is: a QString is made of it for the call.

    indexFilesFolder : str
      Passed on as it is: a QString is made of it for the call.

    searchInput : str
      Passed on as it is: a QString is made of it for the call.

    usesFilterEngine : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void fulltextsearch::QHelpSearchIndexReader::search(const QString
    #      &collectionFile, const QString &indexFilesFolder, const QString
    #      &searchInput, bool usesFilterEngine)
    self.uglySide.call(
        'ritual_ZN14fulltextsearch22QHelpSearchIndexReader6searchERK7QStrin'
        'gS3_S3_b',
        collectionFile, indexFilesFolder, searchInput, usesFilterEngine,
    )

  def searchingStarted(self) -> None:
    """
    Calls Qt's 'void
    fulltextsearch::QHelpSearchIndexReader::searchingStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/fulltextsearch-qhelpsearchindexreader.html
    """
    #  void fulltextsearch::QHelpSearchIndexReader::searchingStarted()
    self.uglySide.call(
        'ritual_ZN14fulltextsearch22QHelpSearchIndexReader16searchingStarte'
        'dEv',
    )

  def searchingFinished(self) -> None:
    """
    Calls Qt's 'void
    fulltextsearch::QHelpSearchIndexReader::searchingFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/fulltextsearch-qhelpsearchindexreader.html
    """
    #  void fulltextsearch::QHelpSearchIndexReader::searchingFinished()
    self.uglySide.call(
        'ritual_ZN14fulltextsearch22QHelpSearchIndexReader17searchingFinish'
        'edEv',
    )

  def run(self) -> None:
    """
    Calls Qt's 'void fulltextsearch::QHelpSearchIndexReader::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/fulltextsearch-qhelpsearchindexreader.html#run
    """
    #  void fulltextsearch::QHelpSearchIndexReader::run()
    self.uglySide.call(
        'ritual_ZN14fulltextsearch22QHelpSearchIndexReader3runEv',
    )
