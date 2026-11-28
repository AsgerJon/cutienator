"""
QQuickTableView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktableview_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTableView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtQml import QQmlFinalizerHook
from . import QQuickFlickable, QQuickItem
from ..QtQmlModels import QQmlDelegateModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QItemSelectionModel, QMetaObject, QModelIndex
  from ..QtCore import QPoint, QPointF, QRectF, QVariant
  from ..QtGui import QKeyEvent
  from ..QtQml import QJSValue, QQmlComponent
  from . import QQuickTableViewAttached, QQuickTableViewPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QItemSelectionModel = WAIT['QItemSelectionModel']
  QJSValue = WAIT['QJSValue']
  QKeyEvent = WAIT['QKeyEvent']
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QQmlComponent = WAIT['QQmlComponent']
  QRectF = WAIT['QRectF']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTableView(QQuickFlickable, QQmlFinalizerHook):
  """
  The cute side of Qt's QQuickTableView: a plain Python object standing in
  front of one C++ QQuickTableView.

  It is built on the cute 'QQuickFlickable', as Qt's QQuickTableView is built
  on Qt's QQuickFlickable, and has everything that class has. It is built on
  the cute 'QQmlFinalizerHook' as well, as Qt's QQuickTableView is built on
  Qt's QQmlFinalizerHook too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTableView that has a ritual and that Python
  can call so far, 126 names in all: 'metaObject', 'tr', 'rows', 'columns',
  'rowSpacing', 'setRowSpacing', 'columnSpacing', 'setColumnSpacing',
  'rowHeightProvider', 'setRowHeightProvider', 'columnWidthProvider',
  'setColumnWidthProvider', 'model', 'setModel', 'delegate', 'setDelegate',
  'reuseItems', 'setReuseItems', 'setContentWidth', 'setContentHeight',
  'syncView', 'setSyncView', 'syncDirection', 'setSyncDirection',
  'selectionModel', 'setSelectionModel', 'animate', 'setAnimate',
  'keyNavigationEnabled', 'setKeyNavigationEnabled',
  'pointerNavigationEnabled', 'setPointerNavigationEnabled', 'leftColumn',
  'rightColumn', 'topRow', 'bottomRow', 'currentRow', 'currentColumn',
  'alternatingRows', 'setAlternatingRows', 'selectionBehavior',
  'setSelectionBehavior', 'selectionMode', 'setSelectionMode',
  'resizableColumns', 'setResizableColumns', 'resizableRows',
  'setResizableRows', 'editTriggers', 'setEditTriggers',
  'delegateModelAccess', 'setDelegateModelAccess', 'forceLayout',
  'positionViewAtCell', 'positionViewAtIndex', 'positionViewAtRow',
  'positionViewAtColumn', 'itemAtCell', 'cellAtPosition', 'modelIndex',
  'cellAtPos', 'isColumnLoaded', 'isRowLoaded', 'columnWidth', 'rowHeight',
  'implicitColumnWidth', 'implicitRowHeight', 'index', 'cellAtIndex',
  'rowAtIndex', 'columnAtIndex', 'setColumnWidth', 'clearColumnWidths',
  'explicitColumnWidth', 'setRowHeight', 'clearRowHeights',
  'explicitRowHeight', 'edit', 'closeEditor', 'itemAtIndex', 'moveColumn',
  'moveRow', 'clearColumnReordering', 'clearRowReordering',
  'qmlAttachedProperties', 'rowsChanged', 'columnsChanged',
  'rowSpacingChanged', 'columnSpacingChanged', 'rowHeightProviderChanged',
  'columnWidthProviderChanged', 'modelChanged', 'delegateChanged',
  'reuseItemsChanged', 'syncViewChanged', 'syncDirectionChanged',
  'leftColumnChanged', 'rightColumnChanged', 'topRowChanged',
  'bottomRowChanged', 'selectionModelChanged', 'animateChanged',
  'keyNavigationEnabledChanged', 'pointerNavigationEnabledChanged',
  'currentRowChanged', 'currentColumnChanged', 'alternatingRowsChanged',
  'selectionBehaviorChanged', 'resizableColumnsChanged',
  'resizableRowsChanged', 'editTriggersChanged', 'layoutChanged',
  'selectionModeChanged', 'rowMoved', 'columnMoved',
  'delegateModelAccessChanged', 'geometryChange', 'viewportMoved',
  'keyPressEvent', 'eventFilter', 'componentFinalized', 'd_func',
  'minXExtent', 'maxXExtent', 'minYExtent', 'maxYExtent'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTableView::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTableView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickTableView::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickTableView::~QQuickTableView()': the destructor: Python never
    removes a C++ QQuickTableView.
  - Qt's 'QQuickTableView::QQuickTableView(QQuickTableViewPrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickTableViewPrivate *QQuickTableView::d_func() const':
    takes in Python what 'QQuickTableViewPrivate *QQuickTableView::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 142 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTableView is created at the first use, not by
    'QQuickTableView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTableView.
  - Qt tells when it has removed the C++ QQuickTableView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickTableView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class EditTrigger(CuteFlags):
    """
    The flags enum 'QQuickTableView::EditTrigger' of Qt, with the 6 names Qt
    gives in it. Qt names the type of its combinations
    'QQuickTableView::EditTriggers'.
    """

    NoEditTriggers = 0x0
    SingleTapped = 0x1
    DoubleTapped = 0x2
    SelectedTapped = 0x4
    EditKeyPressed = 0x8
    AnyKeyPressed = 0x10

  EditTriggers = EditTrigger

  class SelectionBehavior(CuteNum):
    """
    The enum 'QQuickTableView::SelectionBehavior' of Qt, with the 4 names Qt
    gives in it.
    """

    SelectionDisabled = Kee[int](0)
    SelectCells = Kee[int](1)
    SelectRows = Kee[int](2)
    SelectColumns = Kee[int](3)

  class SelectionMode(CuteNum):
    """
    The enum 'QQuickTableView::SelectionMode' of Qt, with the 3 names Qt
    gives in it.
    """

    SingleSelection = Kee[int](0)
    ContiguousSelection = Kee[int](1)
    ExtendedSelection = Kee[int](2)

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
    Calls Qt's 'QString QQuickTableView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#tr

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
    #  QString QQuickTableView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickTableView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      a0: Optional[QObject],
  ) -> Optional[QQuickTableViewAttached]:
    """
    Calls Qt's 'QQuickTableViewAttached
    *QQuickTableView::qmlAttachedProperties(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#qmlAttachedProperties

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTableViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableViewAttached
    #      *QQuickTableView::qmlAttachedProperties(QObject *a0)
    address = Rituals.call(
        'ritual_ZN15QQuickTableView21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    from . import QQuickTableViewAttached
    return QQuickTableViewAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTableView'

  #  Qt's QQuickTableView is built on more than one class. The part of a C++
  #  QQuickTableView that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlFinalizerHook': 'ritual_cast_QQuickTableView_QQmlFinalizerHook',
  }

  #  A C++ QQuickTableView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTableView'

  #  The functions Qt calls itself that QQuickTableView is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'modelIndex': (
          ('_ZNK15QQuickTableView10modelIndexEii',
           ('address', 'value', 'QtCore:QModelIndex'),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
          ('_ZNK15QQuickTableView10modelIndexERK6QPoint',
           ('address', 'value', 'QtCore:QModelIndex'),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'cellAtIndex': (
          ('_ZNK15QQuickTableView11cellAtIndexERK11QModelIndex',
           ('address', 'value', 'QtCore:QPoint'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTableView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTableView::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickTableView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rows(self) -> int:
    """
    Calls Qt's 'int QQuickTableView::rows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#rows
    """
    #  int QQuickTableView::rows() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView4rowsEv')

  def columns(self) -> int:
    """
    Calls Qt's 'int QQuickTableView::columns() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#columns
    """
    #  int QQuickTableView::columns() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView7columnsEv')

  def rowSpacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::rowSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#rowSpacing
    """
    #  qreal QQuickTableView::rowSpacing() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView10rowSpacingEv')

  def columnSpacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::columnSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#columnSpacing
    """
    #  qreal QQuickTableView::columnSpacing() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView13columnSpacingEv')

  def rowHeightProvider(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQuickTableView::rowHeightProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#rowHeightProvider

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQuickTableView::rowHeightProvider() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView17rowHeightProviderEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def columnWidthProvider(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQuickTableView::columnWidthProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#columnWidthProvider

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQuickTableView::columnWidthProvider() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView19columnWidthProviderEv',
    )
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickTableView::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTableView::model() const
    address = self.uglySide.call('ritual_ZNK15QQuickTableView5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickTableView::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickTableView::delegate() const
    address = self.uglySide.call('ritual_ZNK15QQuickTableView8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def reuseItems(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableView::reuseItems() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#reuseItems
    """
    #  bool QQuickTableView::reuseItems() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView10reuseItemsEv')

  def syncView(self) -> Optional[QQuickTableView]:
    """
    Calls Qt's 'QQuickTableView *QQuickTableView::syncView() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#syncView

    Returns
    -------

    Optional[QQuickTableView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableView *QQuickTableView::syncView() const
    address = self.uglySide.call('ritual_ZNK15QQuickTableView8syncViewEv')
    return QQuickTableView._cuteAt(address)

  def syncDirection(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QQuickTableView::syncDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#syncDirection

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QQuickTableView::syncDirection() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK15QQuickTableView13syncDirectionEv',
    ))

  def selectionModel(self) -> Optional[QItemSelectionModel]:
    """
    Calls Qt's 'QItemSelectionModel *QQuickTableView::selectionModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#selectionModel

    Returns
    -------

    Optional[QItemSelectionModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemSelectionModel *QQuickTableView::selectionModel() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView14selectionModelEv',
    )
    from ..QtCore import QItemSelectionModel
    return QItemSelectionModel._cuteAt(address)

  def animate(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableView::animate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#animate
    """
    #  bool QQuickTableView::animate() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView7animateEv')

  def keyNavigationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableView::keyNavigationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#keyNavigationEnabled
    """
    #  bool QQuickTableView::keyNavigationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView20keyNavigationEnabledEv',
    )

  def pointerNavigationEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableView::pointerNavigationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#pointerNavigationEnabled
    """
    #  bool QQuickTableView::pointerNavigationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView24pointerNavigationEnabledEv',
    )

  def leftColumn(self) -> int:
    """
    Calls Qt's 'int QQuickTableView::leftColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#leftColumn
    """
    #  int QQuickTableView::leftColumn() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView10leftColumnEv')

  def rightColumn(self) -> int:
    """
    Calls Qt's 'int QQuickTableView::rightColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#rightColumn
    """
    #  int QQuickTableView::rightColumn() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView11rightColumnEv')

  def topRow(self) -> int:
    """
    Calls Qt's 'int QQuickTableView::topRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#topRow
    """
    #  int QQuickTableView::topRow() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView6topRowEv')

  def bottomRow(self) -> int:
    """
    Calls Qt's 'int QQuickTableView::bottomRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#bottomRow
    """
    #  int QQuickTableView::bottomRow() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView9bottomRowEv')

  def currentRow(self) -> int:
    """
    Calls Qt's 'int QQuickTableView::currentRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#currentRow
    """
    #  int QQuickTableView::currentRow() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView10currentRowEv')

  def currentColumn(self) -> int:
    """
    Calls Qt's 'int QQuickTableView::currentColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#currentColumn
    """
    #  int QQuickTableView::currentColumn() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView13currentColumnEv')

  def alternatingRows(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableView::alternatingRows() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#alternatingRows
    """
    #  bool QQuickTableView::alternatingRows() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView15alternatingRowsEv',
    )

  def selectionBehavior(self) -> SelectionBehavior:
    """
    Calls Qt's 'SelectionBehavior QQuickTableView::selectionBehavior()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#selectionBehavior

    Returns
    -------

    SelectionBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'SelectionBehavior(number)' gives.
    """
    #  SelectionBehavior QQuickTableView::selectionBehavior() const
    return QQuickTableView.SelectionBehavior(self.uglySide.call(
        'ritual_ZNK15QQuickTableView17selectionBehaviorEv',
    ))

  def selectionMode(self) -> SelectionMode:
    """
    Calls Qt's 'SelectionMode QQuickTableView::selectionMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#selectionMode

    Returns
    -------

    SelectionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SelectionMode(number)'
      gives.
    """
    #  SelectionMode QQuickTableView::selectionMode() const
    return QQuickTableView.SelectionMode(self.uglySide.call(
        'ritual_ZNK15QQuickTableView13selectionModeEv',
    ))

  def resizableColumns(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableView::resizableColumns() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#resizableColumns
    """
    #  bool QQuickTableView::resizableColumns() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView16resizableColumnsEv',
    )

  def resizableRows(self) -> bool:
    """
    Calls Qt's 'bool QQuickTableView::resizableRows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#resizableRows
    """
    #  bool QQuickTableView::resizableRows() const
    return self.uglySide.call('ritual_ZNK15QQuickTableView13resizableRowsEv')

  def editTriggers(self) -> EditTriggers:
    """
    Calls Qt's 'EditTriggers QQuickTableView::editTriggers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#editTriggers

    Returns
    -------

    EditTriggers
      The value standing for the combination Qt gave back.
    """
    #  EditTriggers QQuickTableView::editTriggers() const
    return QQuickTableView.EditTriggers(self.uglySide.call(
        'ritual_ZNK15QQuickTableView12editTriggersEv',
    ))

  def delegateModelAccess(self) -> QQmlDelegateModel.DelegateModelAccess:
    """
    Calls Qt's 'QQmlDelegateModel::DelegateModelAccess
    QQuickTableView::delegateModelAccess() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#delegateModelAccess

    Returns
    -------

    QQmlDelegateModel.DelegateModelAccess
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlDelegateModel.DelegateModelAccess(number)' gives.
    """
    #  QQmlDelegateModel::DelegateModelAccess
    #      QQuickTableView::delegateModelAccess() const
    return QQmlDelegateModel.DelegateModelAccess(self.uglySide.call(
        'ritual_ZNK15QQuickTableView19delegateModelAccessEv',
    ))

  @overload(QPoint)
  def itemAtCell(self, cell: QPoint) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickTableView::itemAtCell(const QPoint &cell)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#itemAtCell

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickTableView::itemAtCell(const QPoint &cell) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView10itemAtCellERK6QPoint',
        self._valueOf(cell),
    )
    return QQuickItem._cuteAt(address)

  @overload(int, int)
  def itemAtCell(self, column: int, row: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickTableView::itemAtCell(int column, int row)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#itemAtCell

    Parameters
    ----------

    column : int
      Passed on as it is.

    row : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickTableView::itemAtCell(int column, int row) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView10itemAtCellEii', column, row,
    )
    return QQuickItem._cuteAt(address)

  @overload(QPointF)
  @overload(QPointF, bool)
  def cellAtPosition(
      self,
      position: QPointF,
      includeSpacing: bool = False,
  ) -> QPoint:
    """
    Calls Qt's 'QPoint QQuickTableView::cellAtPosition(const QPointF
    &position, bool includeSpacing) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#cellAtPosition

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    includeSpacing : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickTableView::cellAtPosition(const QPointF &position, bool
    #      includeSpacing) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView14cellAtPositionERK7QPointFb',
        self._valueOf(position, 'QPointF'), includeSpacing,
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(float, float)
  @overload(float, float, bool)
  def cellAtPosition(
      self,
      x: float,
      y: float,
      includeSpacing: bool = False,
  ) -> QPoint:
    """
    Calls Qt's 'QPoint QQuickTableView::cellAtPosition(qreal x, qreal y, bool
    includeSpacing) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#cellAtPosition

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    includeSpacing : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickTableView::cellAtPosition(qreal x, qreal y, bool
    #      includeSpacing) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView14cellAtPositionEddb',
        x, y, includeSpacing,
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(int, int)
  def modelIndex(self, row: int, column: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQuickTableView::modelIndex(int row, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#modelIndex

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
    #  QModelIndex QQuickTableView::modelIndex(int row, int column) const
    ritual = 'ritual_ZNK15QQuickTableView10modelIndexEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickTableView10modelIndexEii'
    address = self.uglySide.call(ritual, row, column)
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QPoint)
  def modelIndex(self, cell: QPoint) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQuickTableView::modelIndex(const QPoint &cell)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#modelIndex

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
    #  QModelIndex QQuickTableView::modelIndex(const QPoint &cell) const
    ritual = 'ritual_ZNK15QQuickTableView10modelIndexERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickTableView10modelIndexERK6QPoint'
    address = self.uglySide.call(ritual, self._valueOf(cell))
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QPointF)
  @overload(QPointF, bool)
  def cellAtPos(
      self,
      position: QPointF,
      includeSpacing: bool = False,
  ) -> QPoint:
    """
    Calls Qt's 'QPoint QQuickTableView::cellAtPos(const QPointF &position,
    bool includeSpacing) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#cellAtPos

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    includeSpacing : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickTableView::cellAtPos(const QPointF &position, bool
    #      includeSpacing) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView9cellAtPosERK7QPointFb',
        self._valueOf(position, 'QPointF'), includeSpacing,
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(float, float)
  @overload(float, float, bool)
  def cellAtPos(
      self,
      x: float,
      y: float,
      includeSpacing: bool = False,
  ) -> QPoint:
    """
    Calls Qt's 'QPoint QQuickTableView::cellAtPos(qreal x, qreal y, bool
    includeSpacing) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#cellAtPos

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    includeSpacing : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QQuickTableView::cellAtPos(qreal x, qreal y, bool
    #      includeSpacing) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView9cellAtPosEddb', x, y, includeSpacing,
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(int)
  def isColumnLoaded(self, column: int) -> bool:
    """
    Calls Qt's 'bool QQuickTableView::isColumnLoaded(int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#isColumnLoaded

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  bool QQuickTableView::isColumnLoaded(int column) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView14isColumnLoadedEi', column,
    )

  @overload(int)
  def isRowLoaded(self, row: int) -> bool:
    """
    Calls Qt's 'bool QQuickTableView::isRowLoaded(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#isRowLoaded

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QQuickTableView::isRowLoaded(int row) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView11isRowLoadedEi', row,
    )

  @overload(int)
  def columnWidth(self, column: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::columnWidth(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#columnWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QQuickTableView::columnWidth(int column) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView11columnWidthEi', column,
    )

  @overload(int)
  def rowHeight(self, row: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::rowHeight(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#rowHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QQuickTableView::rowHeight(int row) const
    return self.uglySide.call('ritual_ZNK15QQuickTableView9rowHeightEi', row)

  @overload(int)
  def implicitColumnWidth(self, column: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::implicitColumnWidth(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#implicitColumnWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QQuickTableView::implicitColumnWidth(int column) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView19implicitColumnWidthEi', column,
    )

  @overload(int)
  def implicitRowHeight(self, row: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::implicitRowHeight(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#implicitRowHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QQuickTableView::implicitRowHeight(int row) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView17implicitRowHeightEi', row,
    )

  @overload(int, int)
  def index(self, row: int, column: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QQuickTableView::index(int row, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#index

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
    #  QModelIndex QQuickTableView::index(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView5indexEii', row, column,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def cellAtIndex(self, index: QModelIndex) -> QPoint:
    """
    Calls Qt's 'QPoint QQuickTableView::cellAtIndex(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#cellAtIndex

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
    #  QPoint QQuickTableView::cellAtIndex(const QModelIndex &index) const
    ritual = 'ritual_ZNK15QQuickTableView11cellAtIndexERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickTableView11cellAtIndexERK11QModelIndex'
    address = self.uglySide.call(ritual, self._valueOf(index))
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QModelIndex)
  def rowAtIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QQuickTableView::rowAtIndex(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#rowAtIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QQuickTableView::rowAtIndex(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView10rowAtIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def columnAtIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QQuickTableView::columnAtIndex(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#columnAtIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QQuickTableView::columnAtIndex(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView13columnAtIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(int)
  def explicitColumnWidth(self, column: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::explicitColumnWidth(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#explicitColumnWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QQuickTableView::explicitColumnWidth(int column) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView19explicitColumnWidthEi', column,
    )

  @overload(int)
  def explicitRowHeight(self, row: int) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::explicitRowHeight(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#explicitRowHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QQuickTableView::explicitRowHeight(int row) const
    return self.uglySide.call(
        'ritual_ZNK15QQuickTableView17explicitRowHeightEi', row,
    )

  @overload(QModelIndex)
  def itemAtIndex(self, index: QModelIndex) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickTableView::itemAtIndex(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#itemAtIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickTableView::itemAtIndex(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickTableView11itemAtIndexERK11QModelIndex',
        self._valueOf(index),
    )
    return QQuickItem._cuteAt(address)

  def minXExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::minXExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#minXExtent
    """
    #  qreal QQuickTableView::minXExtent() const
    ritual = 'ritual_ZNK15QQuickTableView10minXExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickTableView10minXExtentEv'
    return self.uglySide.call(ritual)

  def maxXExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::maxXExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#maxXExtent
    """
    #  qreal QQuickTableView::maxXExtent() const
    ritual = 'ritual_ZNK15QQuickTableView10maxXExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickTableView10maxXExtentEv'
    return self.uglySide.call(ritual)

  def minYExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::minYExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#minYExtent
    """
    #  qreal QQuickTableView::minYExtent() const
    ritual = 'ritual_ZNK15QQuickTableView10minYExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickTableView10minYExtentEv'
    return self.uglySide.call(ritual)

  def maxYExtent(self) -> float:
    """
    Calls Qt's 'qreal QQuickTableView::maxYExtent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#maxYExtent
    """
    #  qreal QQuickTableView::maxYExtent() const
    ritual = 'ritual_ZNK15QQuickTableView10maxYExtentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickTableView10maxYExtentEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setRowSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickTableView::setRowSpacing(qreal spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#setRowSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickTableView::setRowSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView13setRowSpacingEd', spacing,
    )

  @overload(float)
  def setColumnSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickTableView::setColumnSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setColumnSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickTableView::setColumnSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView16setColumnSpacingEd', spacing,
    )

  @overload(QJSValue)
  def setRowHeightProvider(self, provider: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickTableView::setRowHeightProvider(const QJSValue
    &provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setRowHeightProvider

    Parameters
    ----------

    provider : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickTableView::setRowHeightProvider(const QJSValue &provider)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView20setRowHeightProviderERK8QJSValue',
        self._valueOf(provider),
    )

  @overload(QJSValue)
  def setColumnWidthProvider(self, provider: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickTableView::setColumnWidthProvider(const QJSValue
    &provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setColumnWidthProvider

    Parameters
    ----------

    provider : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickTableView::setColumnWidthProvider(const QJSValue &provider)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView22setColumnWidthProviderERK8QJSValue',
        self._valueOf(provider),
    )

  @overload(QVariant)
  def setModel(self, newModel: QVariant) -> None:
    """
    Calls Qt's 'void QQuickTableView::setModel(const QVariant &newModel)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#setModel

    Parameters
    ----------

    newModel : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickTableView::setModel(const QVariant &newModel)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView8setModelERK8QVariant',
        self._valueOf(newModel),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, a0: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickTableView::setDelegate(QQmlComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#setDelegate

    Parameters
    ----------

    a0 : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableView::setDelegate(QQmlComponent *a0)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView11setDelegateEP13QQmlComponent',
        self._addressOf(a0),
    )

  @overload(bool)
  def setReuseItems(self, reuseItems: bool) -> None:
    """
    Calls Qt's 'void QQuickTableView::setReuseItems(bool reuseItems)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#setReuseItems

    Parameters
    ----------

    reuseItems : bool
      Passed on as it is.
    """
    #  void QQuickTableView::setReuseItems(bool reuseItems)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView13setReuseItemsEb', reuseItems,
    )

  @overload(float)
  def setContentWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickTableView::setContentWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setContentWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickTableView::setContentWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView15setContentWidthEd', width,
    )

  @overload(float)
  def setContentHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickTableView::setContentHeight(qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setContentHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickTableView::setContentHeight(qreal height)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView16setContentHeightEd', height,
    )

  @overload(THIS)
  @overload(NoneType)
  def setSyncView(self, view: Optional[QQuickTableView]) -> None:
    """
    Calls Qt's 'void QQuickTableView::setSyncView(QQuickTableView *view)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#setSyncView

    Parameters
    ----------

    view : Optional[QQuickTableView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableView::setSyncView(QQuickTableView *view)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView11setSyncViewEPS_', self._addressOf(view),
    )

  @overload(Qt.Orientations)
  def setSyncDirection(self, direction: Qt.Orientations) -> None:
    """
    Calls Qt's 'void QQuickTableView::setSyncDirection(Qt::Orientations
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setSyncDirection

    Parameters
    ----------

    direction : Qt.Orientations
      Passed on as its number.
    """
    #  void QQuickTableView::setSyncDirection(Qt::Orientations direction)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView16setSyncDirectionE6QFlagsIN2Qt11Orienta'
        'tionEE',
        direction.value,
    )

  @overload(QItemSelectionModel)
  @overload(NoneType)
  def setSelectionModel(
      self,
      selectionModel: Optional[QItemSelectionModel],
  ) -> None:
    """
    Calls Qt's 'void QQuickTableView::setSelectionModel(QItemSelectionModel
    *selectionModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setSelectionModel

    Parameters
    ----------

    selectionModel : Optional[QItemSelectionModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableView::setSelectionModel(QItemSelectionModel
    #      *selectionModel)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView17setSelectionModelEP19QItemSelectionMod'
        'el',
        self._addressOf(selectionModel),
    )

  @overload(bool)
  def setAnimate(self, animate: bool) -> None:
    """
    Calls Qt's 'void QQuickTableView::setAnimate(bool animate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#setAnimate

    Parameters
    ----------

    animate : bool
      Passed on as it is.
    """
    #  void QQuickTableView::setAnimate(bool animate)
    self.uglySide.call('ritual_ZN15QQuickTableView10setAnimateEb', animate)

  @overload(bool)
  def setKeyNavigationEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTableView::setKeyNavigationEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setKeyNavigationEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTableView::setKeyNavigationEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView23setKeyNavigationEnabledEb', enabled,
    )

  @overload(bool)
  def setPointerNavigationEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTableView::setPointerNavigationEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setPointerNavigationEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTableView::setPointerNavigationEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView27setPointerNavigationEnabledEb', enabled,
    )

  @overload(bool)
  def setAlternatingRows(self, alternatingRows: bool) -> None:
    """
    Calls Qt's 'void QQuickTableView::setAlternatingRows(bool
    alternatingRows)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setAlternatingRows

    Parameters
    ----------

    alternatingRows : bool
      Passed on as it is.
    """
    #  void QQuickTableView::setAlternatingRows(bool alternatingRows)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView18setAlternatingRowsEb', alternatingRows,
    )

  @overload(SelectionBehavior)
  def setSelectionBehavior(
      self,
      selectionBehavior: SelectionBehavior,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableView::setSelectionBehavior(SelectionBehavior
    selectionBehavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setSelectionBehavior

    Parameters
    ----------

    selectionBehavior : SelectionBehavior
      Passed on as its number.
    """
    #  void QQuickTableView::setSelectionBehavior(SelectionBehavior
    #      selectionBehavior)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView20setSelectionBehaviorENS_17SelectionBeh'
        'aviorE',
        selectionBehavior.value,
    )

  @overload(SelectionMode)
  def setSelectionMode(self, selectionMode: SelectionMode) -> None:
    """
    Calls Qt's 'void QQuickTableView::setSelectionMode(SelectionMode
    selectionMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setSelectionMode

    Parameters
    ----------

    selectionMode : SelectionMode
      Passed on as its number.
    """
    #  void QQuickTableView::setSelectionMode(SelectionMode selectionMode)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView16setSelectionModeENS_13SelectionModeE',
        selectionMode.value,
    )

  @overload(bool)
  def setResizableColumns(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTableView::setResizableColumns(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setResizableColumns

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTableView::setResizableColumns(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView19setResizableColumnsEb', enabled,
    )

  @overload(bool)
  def setResizableRows(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTableView::setResizableRows(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setResizableRows

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTableView::setResizableRows(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView16setResizableRowsEb', enabled,
    )

  @overload(EditTriggers)
  def setEditTriggers(self, editTriggers: EditTriggers) -> None:
    """
    Calls Qt's 'void QQuickTableView::setEditTriggers(EditTriggers
    editTriggers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setEditTriggers

    Parameters
    ----------

    editTriggers : EditTriggers
      Passed on as its number.
    """
    #  void QQuickTableView::setEditTriggers(EditTriggers editTriggers)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView15setEditTriggersE6QFlagsINS_11EditTrigg'
        'erEE',
        editTriggers.value,
    )

  @overload(QQmlDelegateModel.DelegateModelAccess)
  def setDelegateModelAccess(
      self,
      delegateModelAccess: QQmlDelegateModel.DelegateModelAccess,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTableView::setDelegateModelAccess(QQmlDelegateModel::
    DelegateModelAccess delegateModelAccess)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setDelegateModelAccess

    Parameters
    ----------

    delegateModelAccess : QQmlDelegateModel.DelegateModelAccess
      Passed on as its number.
    """
    #  void QQuickTableView::setDelegateModelAccess(QQmlDelegateModel::
    #      DelegateModelAccess delegateModelAccess)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView22setDelegateModelAccessEN17QQmlDelegate'
        'Model19DelegateModelAccessE',
        delegateModelAccess.value,
    )

  @overload(int, float)
  def setColumnWidth(self, column: int, size: float) -> None:
    """
    Calls Qt's 'void QQuickTableView::setColumnWidth(int column, qreal
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#setColumnWidth

    Parameters
    ----------

    column : int
      Passed on as it is.

    size : float
      Passed on as it is.
    """
    #  void QQuickTableView::setColumnWidth(int column, qreal size)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView14setColumnWidthEid', column, size,
    )

  @overload(int, float)
  def setRowHeight(self, row: int, size: float) -> None:
    """
    Calls Qt's 'void QQuickTableView::setRowHeight(int row, qreal size)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#setRowHeight

    Parameters
    ----------

    row : int
      Passed on as it is.

    size : float
      Passed on as it is.
    """
    #  void QQuickTableView::setRowHeight(int row, qreal size)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView12setRowHeightEid', row, size,
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
    Notes what was given, for Qt's
    'QQuickTableView::QQuickTableView(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#QQuickTableView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTableView::QQuickTableView(QQuickItem *parent)
    self._noteCreation(QQuickTableView, lambda: Rituals.call(
        'ritual_ZN15QQuickTableViewC1EP10QQuickItem',
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

  def forceLayout(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::forceLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#forceLayout
    """
    #  void QQuickTableView::forceLayout()
    self.uglySide.call('ritual_ZN15QQuickTableView11forceLayoutEv')

  @overload(QPoint, QQuickFlickable.PositionMode)
  @overload(QPoint, QQuickFlickable.PositionMode, QPointF)
  @overload(QPoint, QQuickFlickable.PositionMode, QPointF, QRectF)
  def positionViewAtCell(
      self,
      cell: QPoint,
      mode: QQuickFlickable.PositionMode,
      offset: Optional[QPointF] = None,
      subRect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableView::positionViewAtCell(const QPoint &cell,
    QQuickFlickable::PositionMode mode, const QPointF &offset, const QRectF
    &subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#positionViewAtCell

    Parameters
    ----------

    cell : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    mode : QQuickFlickable.PositionMode
      Passed on as its number.

    offset : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    subRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickTableView::positionViewAtCell(const QPoint &cell,
    #      QQuickFlickable::PositionMode mode, const QPointF &offset, const
    #      QRectF &subRect)
    if offset is None:
      from ..QtCore import QPointF
      offset = QPointF()
    if subRect is None:
      from ..QtCore import QRectF
      subRect = QRectF()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView18positionViewAtCellERK6QPoint6QFlagsIN1'
        '5QQuickFlickable16PositionModeFlagEERK7QPointFRK6QRectF',
        self._valueOf(cell), mode.value, self._valueOf(offset, 'QPointF'),
        self._valueOf(subRect),
    )

  @overload(int, int, QQuickFlickable.PositionMode)
  @overload(int, int, QQuickFlickable.PositionMode, QPointF)
  @overload(int, int, QQuickFlickable.PositionMode, QPointF, QRectF)
  def positionViewAtCell(
      self,
      column: int,
      row: int,
      mode: QQuickFlickable.PositionMode,
      offset: Optional[QPointF] = None,
      subRect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableView::positionViewAtCell(int column, int row,
    QQuickFlickable::PositionMode mode, const QPointF &offset, const QRectF
    &subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#positionViewAtCell

    Parameters
    ----------

    column : int
      Passed on as it is.

    row : int
      Passed on as it is.

    mode : QQuickFlickable.PositionMode
      Passed on as its number.

    offset : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    subRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickTableView::positionViewAtCell(int column, int row,
    #      QQuickFlickable::PositionMode mode, const QPointF &offset, const
    #      QRectF &subRect)
    if offset is None:
      from ..QtCore import QPointF
      offset = QPointF()
    if subRect is None:
      from ..QtCore import QRectF
      subRect = QRectF()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView18positionViewAtCellEii6QFlagsIN15QQuick'
        'Flickable16PositionModeFlagEERK7QPointFRK6QRectF',
        column, row, mode.value, self._valueOf(offset, 'QPointF'),
        self._valueOf(subRect),
    )

  @overload(QModelIndex, QQuickFlickable.PositionMode)
  @overload(QModelIndex, QQuickFlickable.PositionMode, QPointF)
  @overload(QModelIndex, QQuickFlickable.PositionMode, QPointF, QRectF)
  def positionViewAtIndex(
      self,
      index: QModelIndex,
      mode: QQuickFlickable.PositionMode,
      offset: Optional[QPointF] = None,
      subRect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableView::positionViewAtIndex(const QModelIndex
    &index, QQuickFlickable::PositionMode mode, const QPointF &offset, const
    QRectF &subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#positionViewAtIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    mode : QQuickFlickable.PositionMode
      Passed on as its number.

    offset : Optional[QPointF]
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own. May be left out, as in Qt: a new 'QPointF()' is then passed on.

    subRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickTableView::positionViewAtIndex(const QModelIndex &index,
    #      QQuickFlickable::PositionMode mode, const QPointF &offset, const
    #      QRectF &subRect)
    if offset is None:
      from ..QtCore import QPointF
      offset = QPointF()
    if subRect is None:
      from ..QtCore import QRectF
      subRect = QRectF()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView19positionViewAtIndexERK11QModelIndex6QF'
        'lagsIN15QQuickFlickable16PositionModeFlagEERK7QPointFRK6QRectF',
        self._valueOf(index), mode.value, self._valueOf(offset, 'QPointF'),
        self._valueOf(subRect),
    )

  @overload(int, QQuickFlickable.PositionMode)
  @overload(int, QQuickFlickable.PositionMode, float)
  @overload(int, QQuickFlickable.PositionMode, float, QRectF)
  def positionViewAtRow(
      self,
      row: int,
      mode: QQuickFlickable.PositionMode,
      offset: float = 0.0,
      subRect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableView::positionViewAtRow(int row,
    QQuickFlickable::PositionMode mode, qreal offset, const QRectF
    &subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#positionViewAtRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    mode : QQuickFlickable.PositionMode
      Passed on as its number.

    offset : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    subRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickTableView::positionViewAtRow(int row,
    #      QQuickFlickable::PositionMode mode, qreal offset, const QRectF
    #      &subRect)
    if subRect is None:
      from ..QtCore import QRectF
      subRect = QRectF()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView17positionViewAtRowEi6QFlagsIN15QQuickFl'
        'ickable16PositionModeFlagEEdRK6QRectF',
        row, mode.value, offset, self._valueOf(subRect),
    )

  @overload(int, QQuickFlickable.PositionMode)
  @overload(int, QQuickFlickable.PositionMode, float)
  @overload(int, QQuickFlickable.PositionMode, float, QRectF)
  def positionViewAtColumn(
      self,
      column: int,
      mode: QQuickFlickable.PositionMode,
      offset: float = 0.0,
      subRect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableView::positionViewAtColumn(int column,
    QQuickFlickable::PositionMode mode, qreal offset, const QRectF
    &subRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#positionViewAtColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    mode : QQuickFlickable.PositionMode
      Passed on as its number.

    offset : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    subRect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QQuickTableView::positionViewAtColumn(int column,
    #      QQuickFlickable::PositionMode mode, qreal offset, const QRectF
    #      &subRect)
    if subRect is None:
      from ..QtCore import QRectF
      subRect = QRectF()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView20positionViewAtColumnEi6QFlagsIN15QQuic'
        'kFlickable16PositionModeFlagEEdRK6QRectF',
        column, mode.value, offset, self._valueOf(subRect),
    )

  def clearColumnWidths(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::clearColumnWidths()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#clearColumnWidths
    """
    #  void QQuickTableView::clearColumnWidths()
    self.uglySide.call('ritual_ZN15QQuickTableView17clearColumnWidthsEv')

  def clearRowHeights(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::clearRowHeights()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#clearRowHeights
    """
    #  void QQuickTableView::clearRowHeights()
    self.uglySide.call('ritual_ZN15QQuickTableView15clearRowHeightsEv')

  @overload(QModelIndex)
  def edit(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QQuickTableView::edit(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#edit

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QQuickTableView::edit(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView4editERK11QModelIndex',
        self._valueOf(index),
    )

  def closeEditor(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::closeEditor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#closeEditor
    """
    #  void QQuickTableView::closeEditor()
    self.uglySide.call('ritual_ZN15QQuickTableView11closeEditorEv')

  @overload(int, int)
  def moveColumn(self, source: int, destination: int) -> None:
    """
    Calls Qt's 'void QQuickTableView::moveColumn(int source, int
    destination)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#moveColumn

    Parameters
    ----------

    source : int
      Passed on as it is.

    destination : int
      Passed on as it is.
    """
    #  void QQuickTableView::moveColumn(int source, int destination)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView10moveColumnEii', source, destination,
    )

  @overload(int, int)
  def moveRow(self, source: int, destination: int) -> None:
    """
    Calls Qt's 'void QQuickTableView::moveRow(int source, int destination)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#moveRow

    Parameters
    ----------

    source : int
      Passed on as it is.

    destination : int
      Passed on as it is.
    """
    #  void QQuickTableView::moveRow(int source, int destination)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView7moveRowEii', source, destination,
    )

  def clearColumnReordering(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::clearColumnReordering()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#clearColumnReordering
    """
    #  void QQuickTableView::clearColumnReordering()
    self.uglySide.call('ritual_ZN15QQuickTableView21clearColumnReorderingEv')

  def clearRowReordering(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::clearRowReordering()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#clearRowReordering
    """
    #  void QQuickTableView::clearRowReordering()
    self.uglySide.call('ritual_ZN15QQuickTableView18clearRowReorderingEv')

  def rowsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::rowsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#rowsChanged
    """
    #  void QQuickTableView::rowsChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView11rowsChangedEv')

  def columnsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::columnsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#columnsChanged
    """
    #  void QQuickTableView::columnsChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView14columnsChangedEv')

  def rowSpacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::rowSpacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#rowSpacingChanged
    """
    #  void QQuickTableView::rowSpacingChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView17rowSpacingChangedEv')

  def columnSpacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::columnSpacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#columnSpacingChanged
    """
    #  void QQuickTableView::columnSpacingChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView20columnSpacingChangedEv')

  def rowHeightProviderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::rowHeightProviderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#rowHeightProviderChanged
    """
    #  void QQuickTableView::rowHeightProviderChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView24rowHeightProviderChangedEv',
    )

  def columnWidthProviderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::columnWidthProviderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#columnWidthProviderChanged
    """
    #  void QQuickTableView::columnWidthProviderChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView26columnWidthProviderChangedEv',
    )

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#modelChanged
    """
    #  void QQuickTableView::modelChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView12modelChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#delegateChanged
    """
    #  void QQuickTableView::delegateChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView15delegateChangedEv')

  def reuseItemsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::reuseItemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#reuseItemsChanged
    """
    #  void QQuickTableView::reuseItemsChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView17reuseItemsChangedEv')

  def syncViewChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::syncViewChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#syncViewChanged
    """
    #  void QQuickTableView::syncViewChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView15syncViewChangedEv')

  def syncDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::syncDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#syncDirectionChanged
    """
    #  void QQuickTableView::syncDirectionChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView20syncDirectionChangedEv')

  def leftColumnChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::leftColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#leftColumnChanged
    """
    #  void QQuickTableView::leftColumnChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView17leftColumnChangedEv')

  def rightColumnChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::rightColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#rightColumnChanged
    """
    #  void QQuickTableView::rightColumnChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView18rightColumnChangedEv')

  def topRowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::topRowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#topRowChanged
    """
    #  void QQuickTableView::topRowChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView13topRowChangedEv')

  def bottomRowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::bottomRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#bottomRowChanged
    """
    #  void QQuickTableView::bottomRowChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView16bottomRowChangedEv')

  def selectionModelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::selectionModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#selectionModelChanged
    """
    #  void QQuickTableView::selectionModelChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView21selectionModelChangedEv')

  def animateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::animateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#animateChanged
    """
    #  void QQuickTableView::animateChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView14animateChangedEv')

  def keyNavigationEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::keyNavigationEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#keyNavigationEnabledChanged
    """
    #  void QQuickTableView::keyNavigationEnabledChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView27keyNavigationEnabledChangedEv',
    )

  def pointerNavigationEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::pointerNavigationEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html
    """
    #  void QQuickTableView::pointerNavigationEnabledChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView31pointerNavigationEnabledChangedEv',
    )

  def currentRowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::currentRowChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#currentRowChanged
    """
    #  void QQuickTableView::currentRowChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView17currentRowChangedEv')

  def currentColumnChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::currentColumnChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#currentColumnChanged
    """
    #  void QQuickTableView::currentColumnChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView20currentColumnChangedEv')

  def alternatingRowsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::alternatingRowsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#alternatingRowsChanged
    """
    #  void QQuickTableView::alternatingRowsChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView22alternatingRowsChangedEv',
    )

  def selectionBehaviorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::selectionBehaviorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#selectionBehaviorChanged
    """
    #  void QQuickTableView::selectionBehaviorChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView24selectionBehaviorChangedEv',
    )

  def resizableColumnsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::resizableColumnsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#resizableColumnsChanged
    """
    #  void QQuickTableView::resizableColumnsChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView23resizableColumnsChangedEv',
    )

  def resizableRowsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::resizableRowsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#resizableRowsChanged
    """
    #  void QQuickTableView::resizableRowsChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView20resizableRowsChangedEv')

  def editTriggersChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::editTriggersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#editTriggersChanged
    """
    #  void QQuickTableView::editTriggersChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView19editTriggersChangedEv')

  def layoutChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::layoutChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#layoutChanged
    """
    #  void QQuickTableView::layoutChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView13layoutChangedEv')

  def selectionModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::selectionModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#selectionModeChanged
    """
    #  void QQuickTableView::selectionModeChanged()
    self.uglySide.call('ritual_ZN15QQuickTableView20selectionModeChangedEv')

  @overload(int, int, int)
  def rowMoved(
      self,
      logicalIndex: int,
      oldVisualIndex: int,
      newVisualIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableView::rowMoved(int logicalIndex, int
    oldVisualIndex, int newVisualIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#rowMoved

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.

    oldVisualIndex : int
      Passed on as it is.

    newVisualIndex : int
      Passed on as it is.
    """
    #  void QQuickTableView::rowMoved(int logicalIndex, int oldVisualIndex,
    #      int newVisualIndex)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView8rowMovedEiii',
        logicalIndex, oldVisualIndex, newVisualIndex,
    )

  @overload(int, int, int)
  def columnMoved(
      self,
      logicalIndex: int,
      oldVisualIndex: int,
      newVisualIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickTableView::columnMoved(int logicalIndex, int
    oldVisualIndex, int newVisualIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#columnMoved

    Parameters
    ----------

    logicalIndex : int
      Passed on as it is.

    oldVisualIndex : int
      Passed on as it is.

    newVisualIndex : int
      Passed on as it is.
    """
    #  void QQuickTableView::columnMoved(int logicalIndex, int
    #      oldVisualIndex, int newVisualIndex)
    self.uglySide.call(
        'ritual_ZN15QQuickTableView11columnMovedEiii',
        logicalIndex, oldVisualIndex, newVisualIndex,
    )

  def delegateModelAccessChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::delegateModelAccessChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#delegateModelAccessChanged
    """
    #  void QQuickTableView::delegateModelAccessChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickTableView26delegateModelAccessChangedEv',
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTableView::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTableView::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickTableView14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTableView14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(Qt.Orientations)
  def viewportMoved(self, orientation: Qt.Orientations) -> None:
    """
    Calls Qt's 'void QQuickTableView::viewportMoved(Qt::Orientations
    orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#viewportMoved

    Parameters
    ----------

    orientation : Qt.Orientations
      Passed on as its number.
    """
    #  void QQuickTableView::viewportMoved(Qt::Orientations orientation)
    ritual = (
        'ritual_ZN15QQuickTableView13viewportMovedE6QFlagsIN2Qt11Orientatio'
        'nEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTableView13viewportMovedE6QFlagsIN2Qt11Orie'
          'ntationEE')
    self.uglySide.call(ritual, orientation.value)

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickTableView::keyPressEvent(QKeyEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#keyPressEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTableView::keyPressEvent(QKeyEvent *e)
    ritual = 'ritual_ZN15QQuickTableView13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTableView13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      obj: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickTableView::eventFilter(QObject *obj, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#eventFilter

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTableView::eventFilter(QObject *obj, QEvent *event)
    ritual = 'ritual_ZN15QQuickTableView11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickTableView11eventFilterEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(obj, 'QObject'), self._addressOf(event),
    )

  def componentFinalized(self) -> None:
    """
    Calls Qt's 'void QQuickTableView::componentFinalized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableview.html#componentFinalized
    """
    #  void QQuickTableView::componentFinalized()
    ritual = 'ritual_ZN15QQuickTableView18componentFinalizedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickTableView18componentFinalizedEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickTableViewPrivate]:
    """
    Calls Qt's 'QQuickTableViewPrivate *QQuickTableView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktableview.html#d_func

    Returns
    -------

    Optional[QQuickTableViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTableViewPrivate *QQuickTableView::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickTableView6d_funcEv')
    from . import QQuickTableViewPrivate
    return QQuickTableViewPrivate._cuteAt(address)
