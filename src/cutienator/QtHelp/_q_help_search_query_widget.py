"""
QHelpSearchQueryWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpsearchquerywidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QFocusEvent
  from . import QHelpSearchQuery
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QHelpSearchQuery = WAIT['QHelpSearchQuery']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpSearchQueryWidget(QWidget):
  """
  The cute side of Qt's QHelpSearchQueryWidget: a plain Python object
  standing in front of one C++ QHelpSearchQueryWidget.

  It is built on the cute 'QWidget', as Qt's QHelpSearchQueryWidget is built
  on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHelpSearchQueryWidget that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr',
  'expandExtendedSearch', 'collapseExtendedSearch', 'query', 'setQuery',
  'searchInput', 'setSearchInput', 'isCompactMode', 'setCompactMode',
  'search', 'focusInEvent', 'changeEvent'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHelpSearchQueryWidget::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QHelpSearchQueryWidget::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QHelpSearchQueryWidget::~QHelpSearchQueryWidget()': the destructor:
    Python never removes a C++ QHelpSearchQueryWidget.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QHelpSearchQueryWidget is created at the first use, not by
    'QHelpSearchQueryWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpSearchQueryWidget.
  - Qt tells when it has removed the C++ QHelpSearchQueryWidget. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QHelpSearchQueryWidget::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#tr

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
    #  QString QHelpSearchQueryWidget::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QHelpSearchQueryWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpSearchQueryWidget'

  #  A C++ QHelpSearchQueryWidget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHelpSearchQueryWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHelpSearchQueryWidget::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHelpSearchQueryWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpSearchQueryWidget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def query(self) -> QList[QHelpSearchQuery]:
    """
    Calls Qt's 'QList<QHelpSearchQuery> QHelpSearchQueryWidget::query()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#query

    Returns
    -------

    QList[QHelpSearchQuery]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QHelpSearchQuery> QHelpSearchQueryWidget::query() const
    address = self.uglySide.call(
        'ritual_ZNK22QHelpSearchQueryWidget5queryEv',
    )
    from . import QHelpSearchQuery
    return QList[QHelpSearchQuery]._cuteOwning(address)

  def searchInput(self) -> str:
    """
    Calls Qt's 'QString QHelpSearchQueryWidget::searchInput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#searchInput

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpSearchQueryWidget::searchInput() const
    return self.uglySide.call(
        'ritual_ZNK22QHelpSearchQueryWidget11searchInputEv',
    )

  def isCompactMode(self) -> bool:
    """
    Calls Qt's 'bool QHelpSearchQueryWidget::isCompactMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#isCompactMode
    """
    #  bool QHelpSearchQueryWidget::isCompactMode() const
    return self.uglySide.call(
        'ritual_ZNK22QHelpSearchQueryWidget13isCompactModeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QHelpSearchQuery])
  def setQuery(self, queryList: QList[QHelpSearchQuery]) -> None:
    """
    Calls Qt's 'void QHelpSearchQueryWidget::setQuery(const
    QList<QHelpSearchQuery> &queryList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#setQuery

    Parameters
    ----------

    queryList : QList[QHelpSearchQuery]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHelpSearchQueryWidget::setQuery(const QList<QHelpSearchQuery>
    #      &queryList)
    self.uglySide.call(
        'ritual_ZN22QHelpSearchQueryWidget8setQueryERK5QListI16QHelpSearchQ'
        'ueryE',
        self._valueOf(queryList),
    )

  @overload(str)
  def setSearchInput(self, searchInput: str) -> None:
    """
    Calls Qt's 'void QHelpSearchQueryWidget::setSearchInput(const QString
    &searchInput)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#setSearchInput

    Parameters
    ----------

    searchInput : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHelpSearchQueryWidget::setSearchInput(const QString
    #      &searchInput)
    self.uglySide.call(
        'ritual_ZN22QHelpSearchQueryWidget14setSearchInputERK7QString',
        searchInput,
    )

  @overload(bool)
  def setCompactMode(self, on: bool) -> None:
    """
    Calls Qt's 'void QHelpSearchQueryWidget::setCompactMode(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#setCompactMode

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QHelpSearchQueryWidget::setCompactMode(bool on)
    self.uglySide.call(
        'ritual_ZN22QHelpSearchQueryWidget14setCompactModeEb', on,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QHelpSearchQueryWidget::QHelpSearchQueryWidget(QWidget *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#QHelpSearchQueryWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHelpSearchQueryWidget::QHelpSearchQueryWidget(QWidget *parent)
    self._noteCreation(QHelpSearchQueryWidget, lambda: Rituals.call(
        'ritual_ZN22QHelpSearchQueryWidgetC1EP7QWidget',
        self._addressOf(parent),
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

  def expandExtendedSearch(self) -> None:
    """
    Calls Qt's 'void QHelpSearchQueryWidget::expandExtendedSearch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#expandExtendedSearch
    """
    #  void QHelpSearchQueryWidget::expandExtendedSearch()
    self.uglySide.call(
        'ritual_ZN22QHelpSearchQueryWidget20expandExtendedSearchEv',
    )

  def collapseExtendedSearch(self) -> None:
    """
    Calls Qt's 'void QHelpSearchQueryWidget::collapseExtendedSearch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#collapseExtendedSearch
    """
    #  void QHelpSearchQueryWidget::collapseExtendedSearch()
    self.uglySide.call(
        'ritual_ZN22QHelpSearchQueryWidget22collapseExtendedSearchEv',
    )

  def search(self) -> None:
    """
    Calls Qt's 'void QHelpSearchQueryWidget::search()'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#search
    """
    #  void QHelpSearchQueryWidget::search()
    self.uglySide.call('ritual_ZN22QHelpSearchQueryWidget6searchEv')

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, focusEvent: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QHelpSearchQueryWidget::focusInEvent(QFocusEvent
    *focusEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#focusInEvent

    Parameters
    ----------

    focusEvent : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHelpSearchQueryWidget::focusInEvent(QFocusEvent *focusEvent)
    ritual = 'ritual_ZN22QHelpSearchQueryWidget12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QHelpSearchQueryWidget12focusInEventEP11QFocusEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(focusEvent))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QHelpSearchQueryWidget::changeEvent(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpsearchquerywidget.html#changeEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHelpSearchQueryWidget::changeEvent(QEvent *event)
    ritual = 'ritual_ZN22QHelpSearchQueryWidget11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QHelpSearchQueryWidget11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))
