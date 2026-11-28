"""
QQuickTreeView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktreeview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickTreeView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickItem, QQuickTableView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QModelIndex, QPoint
  from ..QtGui import QKeyEvent
  from . import QQuickTreeViewPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTreeView(QQuickTableView):
  """
  The cute side of Qt's QQuickTreeView: a plain Python object standing in
  front of one C++ QQuickTreeView.

  It is built on the cute 'QQuickTableView', as Qt's QQuickTreeView is built
  on Qt's QQuickTableView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTreeView that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'rootIndex',
  'setRootIndex', 'resetRootIndex', 'depth', 'isExpanded', 'expand',
  'collapse', 'toggleExpanded', 'expandRecursively', 'collapseRecursively',
  'expandToIndex', 'modelIndex', 'cellAtIndex', 'expanded', 'collapsed',
  'rootIndexChanged', 'keyPressEvent', 'd_func'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTreeView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickTreeView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTreeView::~QQuickTreeView()': the destructor: Python never
    removes a C++ QQuickTreeView.
  - Qt's 'const QQuickTreeViewPrivate *QQuickTreeView::d_func() const': takes
    in Python what 'QQuickTreeViewPrivate *QQuickTreeView::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 30 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTreeView is created at the first use, not by
    'QQuickTreeView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTreeView.
  - Qt tells when it has removed the C++ QQuickTreeView. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickTreeView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#tr

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
    #  QString QQuickTreeView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickTreeView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTreeView'

  #  A C++ QQuickTreeView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTreeView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTreeView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTreeView::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickTreeView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rootIndex(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQuickTreeView::rootIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#rootIndex

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQuickTreeView::rootIndex() const
    address = self.uglySide.call('ritual_ZNK14QQuickTreeView9rootIndexEv')
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int)
  def depth(self, row: int) -> int:
    """
    Calls Qt's 'int QQuickTreeView::depth(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#depth

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  int QQuickTreeView::depth(int row) const
    return self.uglySide.call('ritual_ZNK14QQuickTreeView5depthEi', row)

  @overload(int)
  def isExpanded(self, row: int) -> bool:
    """
    Calls Qt's 'bool QQuickTreeView::isExpanded(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#isExpanded

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QQuickTreeView::isExpanded(int row) const
    return self.uglySide.call(
        'ritual_ZNK14QQuickTreeView10isExpandedEi', row,
    )

  @overload(QPoint)
  def modelIndex(self, cell: QPoint) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQuickTreeView::modelIndex(const QPoint &cell)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#modelIndex

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQuickTreeView::modelIndex(const QPoint &cell) const
    ritual = 'ritual_ZNK14QQuickTreeView10modelIndexERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickTreeView10modelIndexERK6QPoint'
    address = self.uglySide.call(ritual, self._valueOf(cell))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(int, int)
  def modelIndex(self, row: int, column: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQuickTreeView::modelIndex(int row, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#modelIndex

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QQuickTreeView::modelIndex(int row, int column) const
    ritual = 'ritual_ZNK14QQuickTreeView10modelIndexEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickTreeView10modelIndexEii'
    address = self.uglySide.call(ritual, row, column)
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def cellAtIndex(self, index: QModelIndex) -> QPoint:
    """
    Calls Qt's 'QPoint QQuickTreeView::cellAtIndex(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#cellAtIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickTreeView::cellAtIndex(const QModelIndex &index) const
    ritual = 'ritual_ZNK14QQuickTreeView11cellAtIndexERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QQuickTreeView11cellAtIndexERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex)
  def setRootIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QQuickTreeView::setRootIndex(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#setRootIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QQuickTreeView::setRootIndex(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN14QQuickTreeView12setRootIndexERK11QModelIndex',
        self._valueOf(index),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickTreeView::QQuickTreeView(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#QQuickTreeView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTreeView::QQuickTreeView(QQuickItem *parent)
    self._noteCreation(QQuickTreeView, lambda: Rituals.call(
        'ritual_ZN14QQuickTreeViewC1EP10QQuickItem', self._addressOf(parent),
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

  def resetRootIndex(self) -> None:
    """
    Calls Qt's 'void QQuickTreeView::resetRootIndex()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#resetRootIndex
    """
    #  void QQuickTreeView::resetRootIndex()
    self.uglySide.call('ritual_ZN14QQuickTreeView14resetRootIndexEv')

  @overload(int)
  def expand(self, row: int) -> None:
    """
    Calls Qt's 'void QQuickTreeView::expand(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#expand

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QQuickTreeView::expand(int row)
    self.uglySide.call('ritual_ZN14QQuickTreeView6expandEi', row)

  @overload(int)
  def collapse(self, row: int) -> None:
    """
    Calls Qt's 'void QQuickTreeView::collapse(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#collapse

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QQuickTreeView::collapse(int row)
    self.uglySide.call('ritual_ZN14QQuickTreeView8collapseEi', row)

  @overload(int)
  def toggleExpanded(self, row: int) -> None:
    """
    Calls Qt's 'void QQuickTreeView::toggleExpanded(int row)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#toggleExpanded

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QQuickTreeView::toggleExpanded(int row)
    self.uglySide.call('ritual_ZN14QQuickTreeView14toggleExpandedEi', row)

  @overload()
  @overload(int)
  @overload(int, int)
  def expandRecursively(self, row: int = -1, depth: int = -1) -> None:
    """
    Calls Qt's 'void QQuickTreeView::expandRecursively(int row, int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeview.html#expandRecursively

    Parameters
    ----------

    row : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    depth : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QQuickTreeView::expandRecursively(int row, int depth)
    self.uglySide.call(
        'ritual_ZN14QQuickTreeView17expandRecursivelyEii', row, depth,
    )

  @overload()
  @overload(int)
  def collapseRecursively(self, row: int = -1) -> None:
    """
    Calls Qt's 'void QQuickTreeView::collapseRecursively(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeview.html#collapseRecursively

    Parameters
    ----------

    row : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QQuickTreeView::collapseRecursively(int row)
    self.uglySide.call(
        'ritual_ZN14QQuickTreeView19collapseRecursivelyEi', row,
    )

  @overload(QModelIndex)
  def expandToIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QQuickTreeView::expandToIndex(const QModelIndex
    &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#expandToIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QQuickTreeView::expandToIndex(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN14QQuickTreeView13expandToIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(int, int)
  def expanded(self, row: int, depth: int) -> None:
    """
    Calls Qt's 'void QQuickTreeView::expanded(int row, int depth)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#expanded

    Parameters
    ----------

    row : int
      Passed on as it is.

    depth : int
      Passed on as it is.
    """
    #  void QQuickTreeView::expanded(int row, int depth)
    self.uglySide.call('ritual_ZN14QQuickTreeView8expandedEii', row, depth)

  @overload(int, bool)
  def collapsed(self, row: int, recursively: bool) -> None:
    """
    Calls Qt's 'void QQuickTreeView::collapsed(int row, bool recursively)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#collapsed

    Parameters
    ----------

    row : int
      Passed on as it is.

    recursively : bool
      Passed on as it is.
    """
    #  void QQuickTreeView::collapsed(int row, bool recursively)
    self.uglySide.call(
        'ritual_ZN14QQuickTreeView9collapsedEib', row, recursively,
    )

  def rootIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTreeView::rootIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktreeview.html#rootIndexChanged
    """
    #  void QQuickTreeView::rootIndexChanged()
    self.uglySide.call('ritual_ZN14QQuickTreeView16rootIndexChangedEv')

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickTreeView::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTreeView::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN14QQuickTreeView13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickTreeView13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickTreeViewPrivate]:
    """
    Calls Qt's 'QQuickTreeViewPrivate *QQuickTreeView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktreeview.html#d_func

    Returns
    -------

    Optional[QQuickTreeViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTreeViewPrivate *QQuickTreeView::d_func()
    address = self.uglySide.call('ritual_ZN14QQuickTreeView6d_funcEv')
    from . import QQuickTreeViewPrivate
    return QQuickTreeViewPrivate._cuteAt(address)
