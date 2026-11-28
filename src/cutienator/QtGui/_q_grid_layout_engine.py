"""
QGridLayoutEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QGridLayoutEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF, QSizeF
  from . import QAbstractLayoutStyleInfo, QGridLayoutItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractLayoutStyleInfo = WAIT['QAbstractLayoutStyleInfo']
  QGridLayoutItem = WAIT['QGridLayoutItem']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGridLayoutEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGridLayoutEngine: a plain Python object standing in
  front of one C++ QGridLayoutEngine.

  C++ hands a QGridLayoutEngine around as a copy, so every C++
  QGridLayoutEngine behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGridLayoutEngine that has a ritual and that Python
  can call so far, 46 names in all: 'rowCount', 'columnCount', 'itemCount',
  'itemAt', 'effectiveFirstRow', 'effectiveLastRow', 'setSpacing', 'spacing',
  'setRowSpacing', 'rowSpacing', 'setRowStretchFactor', 'rowStretchFactor',
  'setRowSizeHint', 'rowSizeHint', 'uniformCellWidths',
  'setUniformCellWidths', 'uniformCellHeights', 'setUniformCellHeights',
  'setRowAlignment', 'rowAlignment', 'effectiveAlignment', 'insertItem',
  'addItem', 'removeItem', 'deleteItems', 'insertRow', 'removeRows',
  'invalidate', 'setGeometries', 'cellRect', 'sizeHint',
  'ensureDynamicConstraint', 'hasDynamicConstraint', 'constraintOrientation',
  'transpose', 'setVisualDirection', 'visualDirection', 'grossRoundUp',
  'maybeExpandGrid', 'regenerateGrid', 'internalGridRowCount',
  'internalGridColumnCount', 'setItemAt', 'insertOrRemoveRows',
  'ensureEffectiveFirstAndLastRows', 'ensureGeometries'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGridLayoutEngine::~QGridLayoutEngine()': the destructor: Python
    removes its C++ QGridLayoutEngine by it, and has no other use for it.
  - Qt's 'QLayoutPolicy::ControlTypes
    QGridLayoutEngine::controlTypes(LayoutSide side) const': names the enum
    'LayoutSide', whose class cannot be named here.
  - Qt's 'void QGridLayoutEngine::fillRowData(QGridLayoutRowData *rowData,
    const qreal *colPositions, const qreal *colSizes, Qt::Orientation
    orientation, const QAbstractLayoutStyleInfo *styleInfo) const': names
    'qreal', which has no cute class yet.
  - Qt's 'void QGridLayoutEngine::ensureColumnAndRowData(QGridLayoutRowData
    *rowData, QGridLayoutBox *totalBox, const qreal *colPositions, const
    qreal *colSizes, Qt::Orientation orientation, const
    QAbstractLayoutStyleInfo *styleInfo) const': names 'qreal', which has no
    cute class yet.

  What has no ritual
  ------------------

  1 of the 55 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QGridLayoutEngine is created at the first use, not by
    'QGridLayoutEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGridLayoutEngine back gives a copy the ritual made
    for Python, in a new cute QGridLayoutEngine.
  - Each name of Qt's QGridLayoutEngine that has no cute function yet,
    'controlTypes', 'dynamicallyConstrainedSizeHint',
    'ensureColumnAndRowData', 'fillRowData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def grossRoundUp(n: int) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::grossRoundUp(int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#grossRoundUp

    Parameters
    ----------

    n : int
      Passed on as it is.
    """
    #  int QGridLayoutEngine::grossRoundUp(int n)
    return Rituals.call('ritual_ZN17QGridLayoutEngine12grossRoundUpEi', n)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGridLayoutEngine'

  #  Qt's '~QGridLayoutEngine()'. Naming it makes this a value class: Python
  #  owns every C++ QGridLayoutEngine behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QGridLayoutEngineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def rowCount(self, orientation: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::rowCount(Qt::Orientation orientation)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#rowCount

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  int QGridLayoutEngine::rowCount(Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine8rowCountEN2Qt11OrientationE',
        orientation.value,
    )

  @overload()
  def rowCount(self) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#rowCount
    """
    #  int QGridLayoutEngine::rowCount() const
    return self.uglySide.call('ritual_ZNK17QGridLayoutEngine8rowCountEv')

  @overload(Qt.Orientation)
  def columnCount(self, orientation: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::columnCount(Qt::Orientation
    orientation) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#columnCount

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  int QGridLayoutEngine::columnCount(Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine11columnCountEN2Qt11OrientationE',
        orientation.value,
    )

  @overload()
  def columnCount(self) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#columnCount
    """
    #  int QGridLayoutEngine::columnCount() const
    return self.uglySide.call('ritual_ZNK17QGridLayoutEngine11columnCountEv')

  def itemCount(self) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::itemCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#itemCount
    """
    #  int QGridLayoutEngine::itemCount() const
    return self.uglySide.call('ritual_ZNK17QGridLayoutEngine9itemCountEv')

  @overload(int)
  def itemAt(self, index: int) -> Optional[QGridLayoutItem]:
    """
    Calls Qt's 'QGridLayoutItem *QGridLayoutEngine::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QGridLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGridLayoutItem *QGridLayoutEngine::itemAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine6itemAtEi', index,
    )
    from . import QGridLayoutItem
    return QGridLayoutItem._cuteAt(address)

  @overload(int, int)
  @overload(int, int, Qt.Orientation)
  def itemAt(
      self,
      row: int,
      column: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> Optional[QGridLayoutItem]:
    """
    Calls Qt's 'QGridLayoutItem *QGridLayoutEngine::itemAt(int row, int
    column, Qt::Orientation orientation) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#itemAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.

    Returns
    -------

    Optional[QGridLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGridLayoutItem *QGridLayoutEngine::itemAt(int row, int column,
    #      Qt::Orientation orientation) const
    address = self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine6itemAtEiiN2Qt11OrientationE',
        row, column, orientation.value,
    )
    from . import QGridLayoutItem
    return QGridLayoutItem._cuteAt(address)

  @overload()
  @overload(Qt.Orientation)
  def effectiveFirstRow(
      self,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::effectiveFirstRow(Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#effectiveFirstRow

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  int QGridLayoutEngine::effectiveFirstRow(Qt::Orientation orientation)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine17effectiveFirstRowEN2Qt11Orientation'
        'E',
        orientation.value,
    )

  @overload()
  @overload(Qt.Orientation)
  def effectiveLastRow(
      self,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::effectiveLastRow(Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#effectiveLastRow

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  int QGridLayoutEngine::effectiveLastRow(Qt::Orientation orientation)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine16effectiveLastRowEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(Qt.Orientation, QAbstractLayoutStyleInfo)
  @overload(Qt.Orientation, NoneType)
  def spacing(
      self,
      orientation: Qt.Orientation,
      styleInfo: Optional[QAbstractLayoutStyleInfo],
  ) -> float:
    """
    Calls Qt's 'qreal QGridLayoutEngine::spacing(Qt::Orientation orientation,
    const QAbstractLayoutStyleInfo *styleInfo) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#spacing

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    styleInfo : Optional[QAbstractLayoutStyleInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qreal QGridLayoutEngine::spacing(Qt::Orientation orientation, const
    #      QAbstractLayoutStyleInfo *styleInfo) const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine7spacingEN2Qt11OrientationEPK24QAbstr'
        'actLayoutStyleInfo',
        orientation.value, self._addressOf(styleInfo),
    )

  @overload(int)
  @overload(int, Qt.Orientation)
  def rowSpacing(
      self,
      row: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> float:
    """
    Calls Qt's 'qreal QGridLayoutEngine::rowSpacing(int row, Qt::Orientation
    orientation) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#rowSpacing

    Parameters
    ----------

    row : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  qreal QGridLayoutEngine::rowSpacing(int row, Qt::Orientation
    #      orientation) const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine10rowSpacingEiN2Qt11OrientationE',
        row, orientation.value,
    )

  @overload(int)
  @overload(int, Qt.Orientation)
  def rowStretchFactor(
      self,
      row: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::rowStretchFactor(int row,
    Qt::Orientation orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#rowStretchFactor

    Parameters
    ----------

    row : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  int QGridLayoutEngine::rowStretchFactor(int row, Qt::Orientation
    #      orientation) const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine16rowStretchFactorEiN2Qt11Orientation'
        'E',
        row, orientation.value,
    )

  @overload(Qt.SizeHint, int)
  @overload(Qt.SizeHint, int, Qt.Orientation)
  def rowSizeHint(
      self,
      which: Qt.SizeHint,
      row: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> float:
    """
    Calls Qt's 'qreal QGridLayoutEngine::rowSizeHint(Qt::SizeHint which, int
    row, Qt::Orientation orientation) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#rowSizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    row : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  qreal QGridLayoutEngine::rowSizeHint(Qt::SizeHint which, int row,
    #      Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine11rowSizeHintEN2Qt8SizeHintEiNS0_11Or'
        'ientationE',
        which.value, row, orientation.value,
    )

  def uniformCellWidths(self) -> bool:
    """
    Calls Qt's 'bool QGridLayoutEngine::uniformCellWidths() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#uniformCellWidths
    """
    #  bool QGridLayoutEngine::uniformCellWidths() const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine17uniformCellWidthsEv',
    )

  def uniformCellHeights(self) -> bool:
    """
    Calls Qt's 'bool QGridLayoutEngine::uniformCellHeights() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#uniformCellHeights
    """
    #  bool QGridLayoutEngine::uniformCellHeights() const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine18uniformCellHeightsEv',
    )

  @overload(int, Qt.Orientation)
  def rowAlignment(
      self,
      row: int,
      orientation: Qt.Orientation,
  ) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QGridLayoutEngine::rowAlignment(int row,
    Qt::Orientation orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#rowAlignment

    Parameters
    ----------

    row : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QGridLayoutEngine::rowAlignment(int row, Qt::Orientation
    #      orientation) const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine12rowAlignmentEiN2Qt11OrientationE',
        row, orientation.value,
    ))

  @overload(QGridLayoutItem)
  @overload(NoneType)
  def effectiveAlignment(
      self,
      layoutItem: Optional[QGridLayoutItem],
  ) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QGridLayoutEngine::effectiveAlignment(const
    QGridLayoutItem *layoutItem) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#effectiveAlignment

    Parameters
    ----------

    layoutItem : Optional[QGridLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QGridLayoutEngine::effectiveAlignment(const
    #      QGridLayoutItem *layoutItem) const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine18effectiveAlignmentEPK15QGridLayoutI'
        'tem',
        self._addressOf(layoutItem),
    ))

  @overload(QRectF, int, int, int, int, QAbstractLayoutStyleInfo)
  @overload(QRectF, int, int, int, int, NoneType)
  def cellRect(
      self,
      contentsGeometry: QRectF,
      row: int,
      column: int,
      rowSpan: int,
      columnSpan: int,
      styleInfo: Optional[QAbstractLayoutStyleInfo],
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QGridLayoutEngine::cellRect(const QRectF
    &contentsGeometry, int row, int column, int rowSpan, int columnSpan,
    const QAbstractLayoutStyleInfo *styleInfo) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#cellRect

    Parameters
    ----------

    contentsGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    rowSpan : int
      Passed on as it is.

    columnSpan : int
      Passed on as it is.

    styleInfo : Optional[QAbstractLayoutStyleInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGridLayoutEngine::cellRect(const QRectF &contentsGeometry, int
    #      row, int column, int rowSpan, int columnSpan, const
    #      QAbstractLayoutStyleInfo *styleInfo) const
    address = self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine8cellRectERK6QRectFiiiiPK24QAbstractL'
        'ayoutStyleInfo',
        self._valueOf(contentsGeometry), row, column, rowSpan, columnSpan,
        self._addressOf(styleInfo),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Qt.SizeHint, QSizeF, QAbstractLayoutStyleInfo)
  @overload(Qt.SizeHint, QSizeF, NoneType)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: QSizeF,
      styleInfo: Optional[QAbstractLayoutStyleInfo],
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGridLayoutEngine::sizeHint(Qt::SizeHint which, const
    QSizeF &constraint, const QAbstractLayoutStyleInfo *styleInfo) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    styleInfo : Optional[QAbstractLayoutStyleInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGridLayoutEngine::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint, const QAbstractLayoutStyleInfo *styleInfo) const
    address = self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine8sizeHintEN2Qt8SizeHintERK6QSizeFPK24'
        'QAbstractLayoutStyleInfo',
        which.value, self._valueOf(constraint), self._addressOf(styleInfo),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def ensureDynamicConstraint(self) -> bool:
    """
    Calls Qt's 'bool QGridLayoutEngine::ensureDynamicConstraint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#ensureDynamicConstraint
    """
    #  bool QGridLayoutEngine::ensureDynamicConstraint() const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine23ensureDynamicConstraintEv',
    )

  def hasDynamicConstraint(self) -> bool:
    """
    Calls Qt's 'bool QGridLayoutEngine::hasDynamicConstraint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#hasDynamicConstraint
    """
    #  bool QGridLayoutEngine::hasDynamicConstraint() const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine20hasDynamicConstraintEv',
    )

  def constraintOrientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QGridLayoutEngine::constraintOrientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#constraintOrientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QGridLayoutEngine::constraintOrientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine21constraintOrientationEv',
    ))

  def visualDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QGridLayoutEngine::visualDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#visualDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QGridLayoutEngine::visualDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine15visualDirectionEv',
    ))

  def internalGridRowCount(self) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::internalGridRowCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#internalGridRowCount
    """
    #  int QGridLayoutEngine::internalGridRowCount() const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine20internalGridRowCountEv',
    )

  def internalGridColumnCount(self) -> int:
    """
    Calls Qt's 'int QGridLayoutEngine::internalGridColumnCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#internalGridColumnCount
    """
    #  int QGridLayoutEngine::internalGridColumnCount() const
    return self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine23internalGridColumnCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, Qt.Orientations)
  def setSpacing(
      self,
      spacing: float,
      orientations: Qt.Orientations,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::setSpacing(qreal spacing,
    Qt::Orientations orientations)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.

    orientations : Qt.Orientations
      Passed on as its number.
    """
    #  void QGridLayoutEngine::setSpacing(qreal spacing, Qt::Orientations
    #      orientations)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine10setSpacingEd6QFlagsIN2Qt11Orientatio'
        'nEE',
        spacing, orientations.value,
    )

  @overload(int, float)
  @overload(int, float, Qt.Orientation)
  def setRowSpacing(
      self,
      row: int,
      spacing: float,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::setRowSpacing(int row, qreal spacing,
    Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#setRowSpacing

    Parameters
    ----------

    row : int
      Passed on as it is.

    spacing : float
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  void QGridLayoutEngine::setRowSpacing(int row, qreal spacing,
    #      Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine13setRowSpacingEidN2Qt11OrientationE',
        row, spacing, orientation.value,
    )

  @overload(int, int)
  @overload(int, int, Qt.Orientation)
  def setRowStretchFactor(
      self,
      row: int,
      stretch: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::setRowStretchFactor(int row, int
    stretch, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#setRowStretchFactor

    Parameters
    ----------

    row : int
      Passed on as it is.

    stretch : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  void QGridLayoutEngine::setRowStretchFactor(int row, int stretch,
    #      Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine19setRowStretchFactorEiiN2Qt11Orientat'
        'ionE',
        row, stretch, orientation.value,
    )

  @overload(Qt.SizeHint, int, float)
  @overload(Qt.SizeHint, int, float, Qt.Orientation)
  def setRowSizeHint(
      self,
      which: Qt.SizeHint,
      row: int,
      size: float,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::setRowSizeHint(Qt::SizeHint which,
    int row, qreal size, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#setRowSizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    row : int
      Passed on as it is.

    size : float
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  void QGridLayoutEngine::setRowSizeHint(Qt::SizeHint which, int row,
    #      qreal size, Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine14setRowSizeHintEN2Qt8SizeHintEidNS0_1'
        '1OrientationE',
        which.value, row, size, orientation.value,
    )

  @overload(bool)
  def setUniformCellWidths(self, uniformCellWidths: bool) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::setUniformCellWidths(bool
    uniformCellWidths)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#setUniformCellWidths

    Parameters
    ----------

    uniformCellWidths : bool
      Passed on as it is.
    """
    #  void QGridLayoutEngine::setUniformCellWidths(bool uniformCellWidths)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine20setUniformCellWidthsEb',
        uniformCellWidths,
    )

  @overload(bool)
  def setUniformCellHeights(self, uniformCellHeights: bool) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::setUniformCellHeights(bool
    uniformCellHeights)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#setUniformCellHeights

    Parameters
    ----------

    uniformCellHeights : bool
      Passed on as it is.
    """
    #  void QGridLayoutEngine::setUniformCellHeights(bool uniformCellHeights)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine21setUniformCellHeightsEb',
        uniformCellHeights,
    )

  @overload(int, Qt.Alignment, Qt.Orientation)
  def setRowAlignment(
      self,
      row: int,
      alignment: Qt.Alignment,
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::setRowAlignment(int row,
    Qt::Alignment alignment, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#setRowAlignment

    Parameters
    ----------

    row : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGridLayoutEngine::setRowAlignment(int row, Qt::Alignment
    #      alignment, Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine15setRowAlignmentEi6QFlagsIN2Qt13Align'
        'mentFlagEENS1_11OrientationE',
        row, alignment.value, orientation.value,
    )

  @overload(QRectF, QAbstractLayoutStyleInfo)
  @overload(QRectF, NoneType)
  def setGeometries(
      self,
      contentsGeometry: QRectF,
      styleInfo: Optional[QAbstractLayoutStyleInfo],
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::setGeometries(const QRectF
    &contentsGeometry, const QAbstractLayoutStyleInfo *styleInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#setGeometries

    Parameters
    ----------

    contentsGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    styleInfo : Optional[QAbstractLayoutStyleInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGridLayoutEngine::setGeometries(const QRectF &contentsGeometry,
    #      const QAbstractLayoutStyleInfo *styleInfo)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine13setGeometriesERK6QRectFPK24QAbstract'
        'LayoutStyleInfo',
        self._valueOf(contentsGeometry), self._addressOf(styleInfo),
    )

  @overload(Qt.LayoutDirection)
  def setVisualDirection(self, direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void
    QGridLayoutEngine::setVisualDirection(Qt::LayoutDirection direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#setVisualDirection

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QGridLayoutEngine::setVisualDirection(Qt::LayoutDirection
    #      direction)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine18setVisualDirectionEN2Qt15LayoutDirec'
        'tionE',
        direction.value,
    )

  @overload(int, int, QGridLayoutItem)
  @overload(int, int, NoneType)
  def setItemAt(
      self,
      row: int,
      column: int,
      item: Optional[QGridLayoutItem],
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::setItemAt(int row, int column,
    QGridLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#setItemAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    item : Optional[QGridLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGridLayoutEngine::setItemAt(int row, int column, QGridLayoutItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine9setItemAtEiiP15QGridLayoutItem',
        row, column, self._addressOf(item),
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
  @overload(Qt.Alignment)
  @overload(Qt.Alignment, bool)
  def __init__(
      self,
      defaultAlignment: Qt.Alignment = Qt.Alignment(),
      snapToPixelGrid: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGridLayoutEngine::QGridLayoutEngine(Qt::Alignment defaultAlignment,
    bool snapToPixelGrid)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#QGridLayoutEngine

    Parameters
    ----------

    defaultAlignment : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().

    snapToPixelGrid : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QGridLayoutEngine::QGridLayoutEngine(Qt::Alignment defaultAlignment,
    #      bool snapToPixelGrid)
    self._noteCreation(QGridLayoutEngine, lambda: Rituals.call(
        'ritual_ZN17QGridLayoutEngineC1E6QFlagsIN2Qt13AlignmentFlagEEb',
        defaultAlignment.value, snapToPixelGrid,
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

  @overload(QGridLayoutItem, int)
  @overload(NoneType, int)
  def insertItem(self, item: Optional[QGridLayoutItem], index: int) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::insertItem(QGridLayoutItem *item, int
    index)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#insertItem

    Parameters
    ----------

    item : Optional[QGridLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  void QGridLayoutEngine::insertItem(QGridLayoutItem *item, int index)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine10insertItemEP15QGridLayoutItemi',
        self._addressOf(item), index,
    )

  @overload(QGridLayoutItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QGridLayoutItem]) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::addItem(QGridLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#addItem

    Parameters
    ----------

    item : Optional[QGridLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGridLayoutEngine::addItem(QGridLayoutItem *item)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine7addItemEP15QGridLayoutItem',
        self._addressOf(item),
    )

  @overload(QGridLayoutItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QGridLayoutItem]) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::removeItem(QGridLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#removeItem

    Parameters
    ----------

    item : Optional[QGridLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGridLayoutEngine::removeItem(QGridLayoutItem *item)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine10removeItemEP15QGridLayoutItem',
        self._addressOf(item),
    )

  def deleteItems(self) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::deleteItems()'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#deleteItems
    """
    #  void QGridLayoutEngine::deleteItems()
    self.uglySide.call('ritual_ZN17QGridLayoutEngine11deleteItemsEv')

  @overload(int)
  @overload(int, Qt.Orientation)
  def insertRow(
      self,
      row: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::insertRow(int row, Qt::Orientation
    orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#insertRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  void QGridLayoutEngine::insertRow(int row, Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine9insertRowEiN2Qt11OrientationE',
        row, orientation.value,
    )

  @overload(int, int, Qt.Orientation)
  def removeRows(
      self,
      row: int,
      count: int,
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::removeRows(int row, int count,
    Qt::Orientation orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#removeRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    count : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGridLayoutEngine::removeRows(int row, int count, Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine10removeRowsEiiN2Qt11OrientationE',
        row, count, orientation.value,
    )

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#invalidate
    """
    #  void QGridLayoutEngine::invalidate()
    self.uglySide.call('ritual_ZN17QGridLayoutEngine10invalidateEv')

  def transpose(self) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::transpose()'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutengine.html#transpose
    """
    #  void QGridLayoutEngine::transpose()
    self.uglySide.call('ritual_ZN17QGridLayoutEngine9transposeEv')

  @overload(int, int)
  @overload(int, int, Qt.Orientation)
  def maybeExpandGrid(
      self,
      row: int,
      column: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::maybeExpandGrid(int row, int column,
    Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#maybeExpandGrid

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  void QGridLayoutEngine::maybeExpandGrid(int row, int column,
    #      Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine15maybeExpandGridEiiN2Qt11OrientationE',
        row, column, orientation.value,
    )

  def regenerateGrid(self) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::regenerateGrid()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#regenerateGrid
    """
    #  void QGridLayoutEngine::regenerateGrid()
    self.uglySide.call('ritual_ZN17QGridLayoutEngine14regenerateGridEv')

  @overload(int, int)
  @overload(int, int, Qt.Orientation)
  def insertOrRemoveRows(
      self,
      row: int,
      delta: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::insertOrRemoveRows(int row, int
    delta, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#insertOrRemoveRows

    Parameters
    ----------

    row : int
      Passed on as it is.

    delta : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  void QGridLayoutEngine::insertOrRemoveRows(int row, int delta,
    #      Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN17QGridLayoutEngine18insertOrRemoveRowsEiiN2Qt11Orientati'
        'onE',
        row, delta, orientation.value,
    )

  def ensureEffectiveFirstAndLastRows(self) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::ensureEffectiveFirstAndLastRows()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html
    """
    #  void QGridLayoutEngine::ensureEffectiveFirstAndLastRows() const
    self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine31ensureEffectiveFirstAndLastRowsEv',
    )

  @overload(QSizeF, QAbstractLayoutStyleInfo)
  @overload(QSizeF, NoneType)
  def ensureGeometries(
      self,
      size: QSizeF,
      styleInfo: Optional[QAbstractLayoutStyleInfo],
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutEngine::ensureGeometries(const QSizeF &size,
    const QAbstractLayoutStyleInfo *styleInfo) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutengine.html#ensureGeometries

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    styleInfo : Optional[QAbstractLayoutStyleInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGridLayoutEngine::ensureGeometries(const QSizeF &size, const
    #      QAbstractLayoutStyleInfo *styleInfo) const
    self.uglySide.call(
        'ritual_ZNK17QGridLayoutEngine16ensureGeometriesERK6QSizeFPK24QAbst'
        'ractLayoutStyleInfo',
        self._valueOf(size), self._addressOf(styleInfo),
    )

  @staticmethod
  def controlTypes(*__, **_) -> Never:
    """
    Qt's 'QLayoutPolicy::ControlTypes
    QGridLayoutEngine::controlTypes(LayoutSide side) const': names the enum
    'LayoutSide', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QGridLayoutEngine.controlTypes' has no cute function yet. Qt's "
        "'QLayoutPolicy::ControlTypes "
        "QGridLayoutEngine::controlTypes(LayoutSide side) const': names the "
        "enum 'LayoutSide', whose class cannot be named here.")

  @staticmethod
  def dynamicallyConstrainedSizeHint(*__, **_) -> Never:
    """
    Qt's 'QSizeF
    QGridLayoutEngine::dynamicallyConstrainedSizeHint(Qt::SizeHint which,
    const QSizeF &constraint) const': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QGridLayoutEngine.dynamicallyConstrainedSizeHint' has no cute "
        "function yet. Qt's 'QSizeF "
        "QGridLayoutEngine::dynamicallyConstrainedSizeHint(Qt::SizeHint "
        "which, const QSizeF &constraint) const': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def ensureColumnAndRowData(*__, **_) -> Never:
    """
    Qt's 'void QGridLayoutEngine::ensureColumnAndRowData(QGridLayoutRowData
    *rowData, QGridLayoutBox *totalBox, const qreal *colPositions, const
    qreal *colSizes, Qt::Orientation orientation, const
    QAbstractLayoutStyleInfo *styleInfo) const': names 'qreal', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QGridLayoutEngine.ensureColumnAndRowData' has no cute function "
        "yet. Qt's 'void "
        "QGridLayoutEngine::ensureColumnAndRowData(QGridLayoutRowData "
        "*rowData, QGridLayoutBox *totalBox, const qreal *colPositions, "
        "const qreal *colSizes, Qt::Orientation orientation, const "
        "QAbstractLayoutStyleInfo *styleInfo) const': names 'qreal', which "
        "has no cute class yet.")

  @staticmethod
  def fillRowData(*__, **_) -> Never:
    """
    Qt's 'void QGridLayoutEngine::fillRowData(QGridLayoutRowData *rowData,
    const qreal *colPositions, const qreal *colSizes, Qt::Orientation
    orientation, const QAbstractLayoutStyleInfo *styleInfo) const': names
    'qreal', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGridLayoutEngine.fillRowData' has no cute function yet. Qt's "
        "'void QGridLayoutEngine::fillRowData(QGridLayoutRowData *rowData, "
        "const qreal *colPositions, const qreal *colSizes, Qt::Orientation "
        "orientation, const QAbstractLayoutStyleInfo *styleInfo) const': "
        "names 'qreal', which has no cute class yet.")
