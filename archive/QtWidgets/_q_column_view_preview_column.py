"""
QColumnViewPreviewColumn binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcolumnview_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QColumnViewPreviewColumn to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QItemSelectionModel
from . import QAbstractItemView, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QItemSelection, QModelIndex, QPoint, QRect
  from ..QtGui import QRegion, QResizeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QItemSelection = WAIT['QItemSelection']
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QColumnViewPreviewColumn(QAbstractItemView):
  """
  The cute side of Qt's QColumnViewPreviewColumn: a plain Python object
  standing in front of one C++ QColumnViewPreviewColumn.

  It is built on the cute 'QAbstractItemView', as Qt's
  QColumnViewPreviewColumn is built on Qt's QAbstractItemView, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QColumnViewPreviewColumn that has a ritual and that
  Python can call so far, 11 names in all: 'setPreviewWidget', 'resizeEvent',
  'scrollContentsBy', 'visualRect', 'scrollTo', 'indexAt',
  'horizontalOffset', 'verticalOffset', 'visualRegionForSelection',
  'isIndexHidden', 'setSelection'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QModelIndex QColumnViewPreviewColumn::moveCursor(CursorAction a0,
    Qt::KeyboardModifiers a1)': names the enum
    'QAbstractItemView::CursorAction', whose class cannot be named here.

  What to expect
  --------------

  - The C++ QColumnViewPreviewColumn is created at the first use, not by
    'QColumnViewPreviewColumn(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QColumnViewPreviewColumn.
  - Qt tells when it has removed the C++ QColumnViewPreviewColumn. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColumnViewPreviewColumn'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex)
  def visualRect(self, a0: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QColumnViewPreviewColumn::visualRect(const QModelIndex
    &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html#visualRect

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QColumnViewPreviewColumn::visualRect(const QModelIndex &a0)
    #      const
    ritual = (
        'ritual_ZNK24QColumnViewPreviewColumn10visualRectERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QColumnViewPreviewColumn10visualRectERK11QModelI'
          'ndex')
    address = self.uglySide.call(ritual, self._valueOf(a0))
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def indexAt(self, a0: QPoint) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QColumnViewPreviewColumn::indexAt(const QPoint
    &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html#indexAt

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QColumnViewPreviewColumn::indexAt(const QPoint &a0) const
    ritual = 'ritual_ZNK24QColumnViewPreviewColumn7indexAtERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QColumnViewPreviewColumn7indexAtERK6QPoint'
    address = self.uglySide.call(ritual, self._valueOf(a0))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def horizontalOffset(self) -> int:
    """
    Calls Qt's 'int QColumnViewPreviewColumn::horizontalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html#horizontalOffset
    """
    #  int QColumnViewPreviewColumn::horizontalOffset() const
    ritual = 'ritual_ZNK24QColumnViewPreviewColumn16horizontalOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QColumnViewPreviewColumn16horizontalOffsetEv'
    return self.uglySide.call(ritual)

  def verticalOffset(self) -> int:
    """
    Calls Qt's 'int QColumnViewPreviewColumn::verticalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html#verticalOffset
    """
    #  int QColumnViewPreviewColumn::verticalOffset() const
    ritual = 'ritual_ZNK24QColumnViewPreviewColumn14verticalOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QColumnViewPreviewColumn14verticalOffsetEv'
    return self.uglySide.call(ritual)

  @overload(QItemSelection)
  def visualRegionForSelection(self, a0: QItemSelection) -> QRegion:
    """
    Calls Qt's 'QRegion
    QColumnViewPreviewColumn::visualRegionForSelection(const QItemSelection
    &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html

    Parameters
    ----------

    a0 : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QColumnViewPreviewColumn::visualRegionForSelection(const
    #      QItemSelection &a0) const
    ritual = (
        'ritual_ZNK24QColumnViewPreviewColumn24visualRegionForSelectionERK1'
        '4QItemSelection')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QColumnViewPreviewColumn24visualRegionForSelecti'
          'onERK14QItemSelection')
    address = self.uglySide.call(ritual, self._valueOf(a0))
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  @overload(QModelIndex)
  def isIndexHidden(self, a0: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QColumnViewPreviewColumn::isIndexHidden(const
    QModelIndex &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html#isIndexHidden

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QColumnViewPreviewColumn::isIndexHidden(const QModelIndex &a0)
    #      const
    ritual = (
        'ritual_ZNK24QColumnViewPreviewColumn13isIndexHiddenERK11QModelInde'
        'x')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QColumnViewPreviewColumn13isIndexHiddenERK11QMod'
          'elIndex')
    return self.uglySide.call(ritual, self._valueOf(a0))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setPreviewWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QColumnViewPreviewColumn::setPreviewWidget(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html#setPreviewWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnViewPreviewColumn::setPreviewWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN24QColumnViewPreviewColumn16setPreviewWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QRect, QItemSelectionModel.SelectionFlags)
  def setSelection(
      self,
      a0: QRect,
      a1: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QColumnViewPreviewColumn::setSelection(const QRect &a0,
    QItemSelectionModel::SelectionFlags a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html#setSelection

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    a1 : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QColumnViewPreviewColumn::setSelection(const QRect &a0,
    #      QItemSelectionModel::SelectionFlags a1)
    ritual = (
        'ritual_ZN24QColumnViewPreviewColumn12setSelectionERK5QRect6QFlagsI'
        'N19QItemSelectionModel13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QColumnViewPreviewColumn12setSelectionERK5QRect6Q'
          'FlagsIN19QItemSelectionModel13SelectionFlagEE')
    self.uglySide.call(ritual, self._valueOf(a0), a1.value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QColumnViewPreviewColumn::QColumnViewPreviewColumn(QWidget *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QColumnViewPreviewColumn::QColumnViewPreviewColumn(QWidget *parent)
    self._noteCreation(QColumnViewPreviewColumn, lambda: Rituals.call(
        'ritual_ZN24QColumnViewPreviewColumnC1EP7QWidget',
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

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QColumnViewPreviewColumn::resizeEvent(QResizeEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnViewPreviewColumn::resizeEvent(QResizeEvent *event)
    ritual = (
        'ritual_ZN24QColumnViewPreviewColumn11resizeEventEP12QResizeEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QColumnViewPreviewColumn11resizeEventEP12QResizeE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(int, int)
  def scrollContentsBy(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QColumnViewPreviewColumn::scrollContentsBy(int dx, int
    dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QColumnViewPreviewColumn::scrollContentsBy(int dx, int dy)
    ritual = 'ritual_ZN24QColumnViewPreviewColumn16scrollContentsByEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QColumnViewPreviewColumn16scrollContentsByEii'
    self.uglySide.call(ritual, dx, dy)

  @overload(QModelIndex, QAbstractItemView.ScrollHint)
  def scrollTo(
      self,
      a0: QModelIndex,
      a1: QAbstractItemView.ScrollHint,
  ) -> None:
    """
    Calls Qt's 'void QColumnViewPreviewColumn::scrollTo(const QModelIndex
    &a0, ScrollHint a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewpreviewcolumn.html#scrollTo

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : QAbstractItemView.ScrollHint
      Passed on as its number.
    """
    #  void QColumnViewPreviewColumn::scrollTo(const QModelIndex &a0,
    #      ScrollHint a1)
    ritual = (
        'ritual_ZN24QColumnViewPreviewColumn8scrollToERK11QModelIndexN17QAb'
        'stractItemView10ScrollHintE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QColumnViewPreviewColumn8scrollToERK11QModelIndex'
          'N17QAbstractItemView10ScrollHintE')
    self.uglySide.call(ritual, self._valueOf(a0), a1.value)
