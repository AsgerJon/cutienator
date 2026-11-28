"""
QQuickGridLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklinearlayout_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickGridLayout to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from . import QQuickGridLayoutBase
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickGridLayoutPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGridLayout(QQuickGridLayoutBase):
  """
  The cute side of Qt's QQuickGridLayout: a plain Python object standing in
  front of one C++ QQuickGridLayout.

  It is built on the cute 'QQuickGridLayoutBase', as Qt's QQuickGridLayout is
  built on Qt's QQuickGridLayoutBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGridLayout that has a ritual and that Python
  can call so far, 25 names in all: 'metaObject', 'tr', 'columnSpacing',
  'setColumnSpacing', 'rowSpacing', 'setRowSpacing', 'columns', 'setColumns',
  'rows', 'setRows', 'flow', 'setFlow', 'uniformCellWidths',
  'setUniformCellWidths', 'uniformCellHeights', 'setUniformCellHeights',
  'insertLayoutItems', 'columnSpacingChanged', 'rowSpacingChanged',
  'columnsChanged', 'rowsChanged', 'flowChanged', 'uniformCellWidthsChanged',
  'uniformCellHeightsChanged', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGridLayout::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickGridLayout::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickGridLayoutPrivate *QQuickGridLayout::d_func() const':
    takes in Python what 'QQuickGridLayoutPrivate
    *QQuickGridLayout::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGridLayout is created at the first use, not by
    'QQuickGridLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGridLayout.
  - Qt tells when it has removed the C++ QQuickGridLayout. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickGridLayout, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flow(CuteNum):
    """
    The enum 'QQuickGridLayout::Flow' of Qt, with the 2 names Qt gives in it.
    """

    LeftToRight = Kee[int](0)
    TopToBottom = Kee[int](1)

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
    Calls Qt's 'QString QQuickGridLayout::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#tr

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
    #  QString QQuickGridLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickGridLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGridLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGridLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGridLayout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickGridLayout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def columnSpacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickGridLayout::columnSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#columnSpacing
    """
    #  qreal QQuickGridLayout::columnSpacing() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGridLayout13columnSpacingEv',
    )

  def rowSpacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickGridLayout::rowSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#rowSpacing
    """
    #  qreal QQuickGridLayout::rowSpacing() const
    return self.uglySide.call('ritual_ZNK16QQuickGridLayout10rowSpacingEv')

  def columns(self) -> int:
    """
    Calls Qt's 'int QQuickGridLayout::columns() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#columns
    """
    #  int QQuickGridLayout::columns() const
    return self.uglySide.call('ritual_ZNK16QQuickGridLayout7columnsEv')

  def rows(self) -> int:
    """
    Calls Qt's 'int QQuickGridLayout::rows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#rows
    """
    #  int QQuickGridLayout::rows() const
    return self.uglySide.call('ritual_ZNK16QQuickGridLayout4rowsEv')

  def flow(self) -> Flow:
    """
    Calls Qt's 'Flow QQuickGridLayout::flow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#flow

    Returns
    -------

    Flow
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Flow(number)' gives.
    """
    #  Flow QQuickGridLayout::flow() const
    return QQuickGridLayout.Flow(self.uglySide.call(
        'ritual_ZNK16QQuickGridLayout4flowEv',
    ))

  def uniformCellWidths(self) -> bool:
    """
    Calls Qt's 'bool QQuickGridLayout::uniformCellWidths() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#uniformCellWidths
    """
    #  bool QQuickGridLayout::uniformCellWidths() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGridLayout17uniformCellWidthsEv',
    )

  def uniformCellHeights(self) -> bool:
    """
    Calls Qt's 'bool QQuickGridLayout::uniformCellHeights() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#uniformCellHeights
    """
    #  bool QQuickGridLayout::uniformCellHeights() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickGridLayout18uniformCellHeightsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setColumnSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::setColumnSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#setColumnSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickGridLayout::setColumnSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN16QQuickGridLayout16setColumnSpacingEd', spacing,
    )

  @overload(float)
  def setRowSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::setRowSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#setRowSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickGridLayout::setRowSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN16QQuickGridLayout13setRowSpacingEd', spacing,
    )

  @overload(int)
  def setColumns(self, columns: int) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::setColumns(int columns)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#setColumns

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QQuickGridLayout::setColumns(int columns)
    self.uglySide.call('ritual_ZN16QQuickGridLayout10setColumnsEi', columns)

  @overload(int)
  def setRows(self, rows: int) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::setRows(int rows)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#setRows

    Parameters
    ----------

    rows : int
      Passed on as it is.
    """
    #  void QQuickGridLayout::setRows(int rows)
    self.uglySide.call('ritual_ZN16QQuickGridLayout7setRowsEi', rows)

  @overload(Flow)
  def setFlow(self, flow: Flow) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::setFlow(Flow flow)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#setFlow

    Parameters
    ----------

    flow : Flow
      Passed on as its number.
    """
    #  void QQuickGridLayout::setFlow(Flow flow)
    self.uglySide.call(
        'ritual_ZN16QQuickGridLayout7setFlowENS_4FlowE', flow.value,
    )

  @overload(bool)
  def setUniformCellWidths(self, uniformCellWidths: bool) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::setUniformCellWidths(bool
    uniformCellWidths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#setUniformCellWidths

    Parameters
    ----------

    uniformCellWidths : bool
      Passed on as it is.
    """
    #  void QQuickGridLayout::setUniformCellWidths(bool uniformCellWidths)
    self.uglySide.call(
        'ritual_ZN16QQuickGridLayout20setUniformCellWidthsEb',
        uniformCellWidths,
    )

  @overload(bool)
  def setUniformCellHeights(self, uniformCellHeights: bool) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::setUniformCellHeights(bool
    uniformCellHeights)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#setUniformCellHeights

    Parameters
    ----------

    uniformCellHeights : bool
      Passed on as it is.
    """
    #  void QQuickGridLayout::setUniformCellHeights(bool uniformCellHeights)
    self.uglySide.call(
        'ritual_ZN16QQuickGridLayout21setUniformCellHeightsEb',
        uniformCellHeights,
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
    'QQuickGridLayout::QQuickGridLayout(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#QQuickGridLayout

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGridLayout::QQuickGridLayout(QQuickItem *parent)
    self._noteCreation(QQuickGridLayout, lambda: Rituals.call(
        'ritual_ZN16QQuickGridLayoutC1EP10QQuickItem',
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

  def insertLayoutItems(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::insertLayoutItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#insertLayoutItems
    """
    #  void QQuickGridLayout::insertLayoutItems()
    ritual = 'ritual_ZN16QQuickGridLayout17insertLayoutItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QQuickGridLayout17insertLayoutItemsEv'
    self.uglySide.call(ritual)

  def columnSpacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::columnSpacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#columnSpacingChanged
    """
    #  void QQuickGridLayout::columnSpacingChanged()
    self.uglySide.call('ritual_ZN16QQuickGridLayout20columnSpacingChangedEv')

  def rowSpacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::rowSpacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#rowSpacingChanged
    """
    #  void QQuickGridLayout::rowSpacingChanged()
    self.uglySide.call('ritual_ZN16QQuickGridLayout17rowSpacingChangedEv')

  def columnsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::columnsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#columnsChanged
    """
    #  void QQuickGridLayout::columnsChanged()
    self.uglySide.call('ritual_ZN16QQuickGridLayout14columnsChangedEv')

  def rowsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::rowsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#rowsChanged
    """
    #  void QQuickGridLayout::rowsChanged()
    self.uglySide.call('ritual_ZN16QQuickGridLayout11rowsChangedEv')

  def flowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::flowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#flowChanged
    """
    #  void QQuickGridLayout::flowChanged()
    self.uglySide.call('ritual_ZN16QQuickGridLayout11flowChangedEv')

  def uniformCellWidthsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::uniformCellWidthsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#uniformCellWidthsChanged
    """
    #  void QQuickGridLayout::uniformCellWidthsChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGridLayout24uniformCellWidthsChangedEv',
    )

  def uniformCellHeightsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGridLayout::uniformCellHeightsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayout.html#uniformCellHeightsChanged
    """
    #  void QQuickGridLayout::uniformCellHeightsChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickGridLayout25uniformCellHeightsChangedEv',
    )

  def d_func(self) -> Optional[QQuickGridLayoutPrivate]:
    """
    Calls Qt's 'QQuickGridLayoutPrivate *QQuickGridLayout::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayout.html#d_func

    Returns
    -------

    Optional[QQuickGridLayoutPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGridLayoutPrivate *QQuickGridLayout::d_func()
    address = self.uglySide.call('ritual_ZN16QQuickGridLayout6d_funcEv')
    from . import QQuickGridLayoutPrivate
    return QQuickGridLayoutPrivate._cuteAt(address)
