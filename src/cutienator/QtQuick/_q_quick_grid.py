"""
QQuickGrid binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickGrid to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickBasePositioner, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGrid(QQuickBasePositioner):
  """
  The cute side of Qt's QQuickGrid: a plain Python object standing in front
  of one C++ QQuickGrid.

  It is built on the cute 'QQuickBasePositioner', as Qt's QQuickGrid is built
  on Qt's QQuickBasePositioner, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGrid that has a ritual and that Python can
  call so far, 34 names in all: 'metaObject', 'tr', 'rows', 'setRows',
  'columns', 'setColumns', 'rowSpacing', 'setRowSpacing', 'resetRowSpacing',
  'columnSpacing', 'setColumnSpacing', 'resetColumnSpacing', 'flow',
  'setFlow', 'layoutDirection', 'setLayoutDirection',
  'effectiveLayoutDirection', 'hItemAlign', 'setHItemAlign',
  'effectiveHAlign', 'vItemAlign', 'setVItemAlign', 'rowsChanged',
  'columnsChanged', 'flowChanged', 'layoutDirectionChanged',
  'effectiveLayoutDirectionChanged', 'rowSpacingChanged',
  'columnSpacingChanged', 'horizontalAlignmentChanged',
  'effectiveHorizontalAlignmentChanged', 'verticalAlignmentChanged',
  'doPositioning', 'reportConflictingAnchors'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGrid::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickGrid::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGridPrivate *QQuickGrid::d_func()': gives
    'QQuickGridPrivate', which has no cute class yet.
  - Qt's 'const QQuickGridPrivate *QQuickGrid::d_func() const': gives
    'QQuickGridPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 41 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGrid is created at the first use, not by 'QQuickGrid(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGrid.
  - Qt tells when it has removed the C++ QQuickGrid. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickGrid, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Flow(CuteNum):
    """The enum 'QQuickGrid::Flow' of Qt, with the 2 names Qt gives in it."""

    LeftToRight = Kee[int](0)
    TopToBottom = Kee[int](1)

  class HAlignment(CuteNum):
    """
    The enum 'QQuickGrid::HAlignment' of Qt, with the 3 names Qt gives in it.
    """

    AlignLeft = Kee[int](1)
    AlignRight = Kee[int](2)
    AlignHCenter = Kee[int](4)

  class VAlignment(CuteNum):
    """
    The enum 'QQuickGrid::VAlignment' of Qt, with the 3 names Qt gives in it.
    """

    AlignTop = Kee[int](32)
    AlignBottom = Kee[int](64)
    AlignVCenter = Kee[int](128)

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
    Calls Qt's 'QString QQuickGrid::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#tr

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
    #  QString QQuickGrid::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQuickGrid2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGrid'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGrid::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGrid::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickGrid10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rows(self) -> int:
    """
    Calls Qt's 'int QQuickGrid::rows() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#rows
    """
    #  int QQuickGrid::rows() const
    return self.uglySide.call('ritual_ZNK10QQuickGrid4rowsEv')

  def columns(self) -> int:
    """
    Calls Qt's 'int QQuickGrid::columns() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#columns
    """
    #  int QQuickGrid::columns() const
    return self.uglySide.call('ritual_ZNK10QQuickGrid7columnsEv')

  def rowSpacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickGrid::rowSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#rowSpacing
    """
    #  qreal QQuickGrid::rowSpacing() const
    return self.uglySide.call('ritual_ZNK10QQuickGrid10rowSpacingEv')

  def columnSpacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickGrid::columnSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#columnSpacing
    """
    #  qreal QQuickGrid::columnSpacing() const
    return self.uglySide.call('ritual_ZNK10QQuickGrid13columnSpacingEv')

  def flow(self) -> Flow:
    """
    Calls Qt's 'Flow QQuickGrid::flow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#flow

    Returns
    -------

    Flow
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Flow(number)' gives.
    """
    #  Flow QQuickGrid::flow() const
    return QQuickGrid.Flow(self.uglySide.call(
        'ritual_ZNK10QQuickGrid4flowEv',
    ))

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQuickGrid::layoutDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickGrid::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK10QQuickGrid15layoutDirectionEv',
    ))

  def effectiveLayoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QQuickGrid::effectiveLayoutDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrid.html#effectiveLayoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QQuickGrid::effectiveLayoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK10QQuickGrid24effectiveLayoutDirectionEv',
    ))

  def hItemAlign(self) -> HAlignment:
    """
    Calls Qt's 'HAlignment QQuickGrid::hItemAlign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#hItemAlign

    Returns
    -------

    HAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HAlignment(number)'
      gives.
    """
    #  HAlignment QQuickGrid::hItemAlign() const
    return QQuickGrid.HAlignment(self.uglySide.call(
        'ritual_ZNK10QQuickGrid10hItemAlignEv',
    ))

  def effectiveHAlign(self) -> HAlignment:
    """
    Calls Qt's 'HAlignment QQuickGrid::effectiveHAlign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#effectiveHAlign

    Returns
    -------

    HAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HAlignment(number)'
      gives.
    """
    #  HAlignment QQuickGrid::effectiveHAlign() const
    return QQuickGrid.HAlignment(self.uglySide.call(
        'ritual_ZNK10QQuickGrid15effectiveHAlignEv',
    ))

  def vItemAlign(self) -> VAlignment:
    """
    Calls Qt's 'VAlignment QQuickGrid::vItemAlign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#vItemAlign

    Returns
    -------

    VAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'VAlignment(number)'
      gives.
    """
    #  VAlignment QQuickGrid::vItemAlign() const
    return QQuickGrid.VAlignment(self.uglySide.call(
        'ritual_ZNK10QQuickGrid10vItemAlignEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRows(self, rows: int) -> None:
    """
    Calls Qt's 'void QQuickGrid::setRows(const int rows)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#setRows

    Parameters
    ----------

    rows : int
      Passed on as it is.
    """
    #  void QQuickGrid::setRows(const int rows)
    self.uglySide.call('ritual_ZN10QQuickGrid7setRowsEi', rows)

  @overload(int)
  def setColumns(self, columns: int) -> None:
    """
    Calls Qt's 'void QQuickGrid::setColumns(const int columns)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#setColumns

    Parameters
    ----------

    columns : int
      Passed on as it is.
    """
    #  void QQuickGrid::setColumns(const int columns)
    self.uglySide.call('ritual_ZN10QQuickGrid10setColumnsEi', columns)

  @overload(float)
  def setRowSpacing(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickGrid::setRowSpacing(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#setRowSpacing

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickGrid::setRowSpacing(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickGrid13setRowSpacingEd', a0)

  @overload(float)
  def setColumnSpacing(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickGrid::setColumnSpacing(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#setColumnSpacing

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickGrid::setColumnSpacing(qreal a0)
    self.uglySide.call('ritual_ZN10QQuickGrid16setColumnSpacingEd', a0)

  @overload(Flow)
  def setFlow(self, a0: Flow) -> None:
    """
    Calls Qt's 'void QQuickGrid::setFlow(Flow a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#setFlow

    Parameters
    ----------

    a0 : Flow
      Passed on as its number.
    """
    #  void QQuickGrid::setFlow(Flow a0)
    self.uglySide.call('ritual_ZN10QQuickGrid7setFlowENS_4FlowE', a0.value)

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, a0: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void QQuickGrid::setLayoutDirection(Qt::LayoutDirection a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#setLayoutDirection

    Parameters
    ----------

    a0 : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QQuickGrid::setLayoutDirection(Qt::LayoutDirection a0)
    self.uglySide.call(
        'ritual_ZN10QQuickGrid18setLayoutDirectionEN2Qt15LayoutDirectionE',
        a0.value,
    )

  @overload(HAlignment)
  def setHItemAlign(self, align: HAlignment) -> None:
    """
    Calls Qt's 'void QQuickGrid::setHItemAlign(HAlignment align)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#setHItemAlign

    Parameters
    ----------

    align : HAlignment
      Passed on as its number.
    """
    #  void QQuickGrid::setHItemAlign(HAlignment align)
    self.uglySide.call(
        'ritual_ZN10QQuickGrid13setHItemAlignENS_10HAlignmentE', align.value,
    )

  @overload(VAlignment)
  def setVItemAlign(self, align: VAlignment) -> None:
    """
    Calls Qt's 'void QQuickGrid::setVItemAlign(VAlignment align)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#setVItemAlign

    Parameters
    ----------

    align : VAlignment
      Passed on as its number.
    """
    #  void QQuickGrid::setVItemAlign(VAlignment align)
    self.uglySide.call(
        'ritual_ZN10QQuickGrid13setVItemAlignENS_10VAlignmentE', align.value,
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
    Notes what was given, for Qt's 'QQuickGrid::QQuickGrid(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#QQuickGrid

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGrid::QQuickGrid(QQuickItem *parent)
    self._noteCreation(QQuickGrid, lambda: Rituals.call(
        'ritual_ZN10QQuickGridC1EP10QQuickItem', self._addressOf(parent),
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

  def resetRowSpacing(self) -> None:
    """
    Calls Qt's 'void QQuickGrid::resetRowSpacing()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#resetRowSpacing
    """
    #  void QQuickGrid::resetRowSpacing()
    self.uglySide.call('ritual_ZN10QQuickGrid15resetRowSpacingEv')

  def resetColumnSpacing(self) -> None:
    """
    Calls Qt's 'void QQuickGrid::resetColumnSpacing()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#resetColumnSpacing
    """
    #  void QQuickGrid::resetColumnSpacing()
    self.uglySide.call('ritual_ZN10QQuickGrid18resetColumnSpacingEv')

  def rowsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGrid::rowsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#rowsChanged
    """
    #  void QQuickGrid::rowsChanged()
    self.uglySide.call('ritual_ZN10QQuickGrid11rowsChangedEv')

  def columnsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGrid::columnsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#columnsChanged
    """
    #  void QQuickGrid::columnsChanged()
    self.uglySide.call('ritual_ZN10QQuickGrid14columnsChangedEv')

  def flowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGrid::flowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#flowChanged
    """
    #  void QQuickGrid::flowChanged()
    self.uglySide.call('ritual_ZN10QQuickGrid11flowChangedEv')

  def layoutDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGrid::layoutDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrid.html#layoutDirectionChanged
    """
    #  void QQuickGrid::layoutDirectionChanged()
    self.uglySide.call('ritual_ZN10QQuickGrid22layoutDirectionChangedEv')

  def effectiveLayoutDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGrid::effectiveLayoutDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrid.html#effectiveLayoutDirectionChanged
    """
    #  void QQuickGrid::effectiveLayoutDirectionChanged()
    self.uglySide.call(
        'ritual_ZN10QQuickGrid31effectiveLayoutDirectionChangedEv',
    )

  def rowSpacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGrid::rowSpacingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#rowSpacingChanged
    """
    #  void QQuickGrid::rowSpacingChanged()
    self.uglySide.call('ritual_ZN10QQuickGrid17rowSpacingChangedEv')

  def columnSpacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGrid::columnSpacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrid.html#columnSpacingChanged
    """
    #  void QQuickGrid::columnSpacingChanged()
    self.uglySide.call('ritual_ZN10QQuickGrid20columnSpacingChangedEv')

  @overload(HAlignment)
  def horizontalAlignmentChanged(self, alignment: HAlignment) -> None:
    """
    Calls Qt's 'void
    QQuickGrid::horizontalAlignmentChanged(QQuickGrid::HAlignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrid.html#horizontalAlignmentChanged

    Parameters
    ----------

    alignment : HAlignment
      Passed on as its number.
    """
    #  void QQuickGrid::horizontalAlignmentChanged(QQuickGrid::HAlignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN10QQuickGrid26horizontalAlignmentChangedENS_10HAlignmentE',
        alignment.value,
    )

  @overload(HAlignment)
  def effectiveHorizontalAlignmentChanged(
      self,
      alignment: HAlignment,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickGrid::effectiveHorizontalAlignmentChanged(QQuickGrid::HAlignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrid.html

    Parameters
    ----------

    alignment : HAlignment
      Passed on as its number.
    """
    #  void QQuickGrid::effectiveHorizontalAlignmentChanged(QQuickGrid::
    #      HAlignment alignment)
    self.uglySide.call(
        'ritual_ZN10QQuickGrid35effectiveHorizontalAlignmentChangedENS_10HA'
        'lignmentE',
        alignment.value,
    )

  @overload(VAlignment)
  def verticalAlignmentChanged(self, alignment: VAlignment) -> None:
    """
    Calls Qt's 'void
    QQuickGrid::verticalAlignmentChanged(QQuickGrid::VAlignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrid.html#verticalAlignmentChanged

    Parameters
    ----------

    alignment : VAlignment
      Passed on as its number.
    """
    #  void QQuickGrid::verticalAlignmentChanged(QQuickGrid::VAlignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN10QQuickGrid24verticalAlignmentChangedENS_10VAlignmentE',
        alignment.value,
    )

  @overload(QSizeF)
  @overload(NoneType)
  def doPositioning(self, contentSize: Optional[QSizeF]) -> None:
    """
    Calls Qt's 'void QQuickGrid::doPositioning(QSizeF *contentSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrid.html#doPositioning

    Parameters
    ----------

    contentSize : Optional[QSizeF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGrid::doPositioning(QSizeF *contentSize)
    ritual = 'ritual_ZN10QQuickGrid13doPositioningEP6QSizeF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickGrid13doPositioningEP6QSizeF'
    self.uglySide.call(ritual, self._addressOf(contentSize))

  def reportConflictingAnchors(self) -> None:
    """
    Calls Qt's 'void QQuickGrid::reportConflictingAnchors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrid.html#reportConflictingAnchors
    """
    #  void QQuickGrid::reportConflictingAnchors()
    ritual = 'ritual_ZN10QQuickGrid24reportConflictingAnchorsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickGrid24reportConflictingAnchorsEv'
    self.uglySide.call(ritual)
