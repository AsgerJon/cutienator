"""
QGraphicsGridLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicsgridlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGraphicsLayout, QGraphicsLayoutItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsGridLayout(QGraphicsLayout):
  """
  The cute side of Qt's QGraphicsGridLayout: a plain Python object standing
  in front of one C++ QGraphicsGridLayout.

  It is built on the cute 'QGraphicsLayout', as Qt's QGraphicsGridLayout is
  built on Qt's QGraphicsLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsGridLayout that has a ritual and that
  Python can call so far, 43 names in all: 'addItem', 'setHorizontalSpacing',
  'horizontalSpacing', 'setVerticalSpacing', 'verticalSpacing', 'setSpacing',
  'setRowSpacing', 'rowSpacing', 'setColumnSpacing', 'columnSpacing',
  'setRowStretchFactor', 'rowStretchFactor', 'setColumnStretchFactor',
  'columnStretchFactor', 'setRowMinimumHeight', 'rowMinimumHeight',
  'setRowPreferredHeight', 'rowPreferredHeight', 'setRowMaximumHeight',
  'rowMaximumHeight', 'setRowFixedHeight', 'setColumnMinimumWidth',
  'columnMinimumWidth', 'setColumnPreferredWidth', 'columnPreferredWidth',
  'setColumnMaximumWidth', 'columnMaximumWidth', 'setColumnFixedWidth',
  'setRowAlignment', 'rowAlignment', 'setColumnAlignment', 'columnAlignment',
  'setAlignment', 'alignment', 'rowCount', 'columnCount', 'itemAt', 'count',
  'removeAt', 'removeItem', 'invalidate', 'setGeometry', 'sizeHint'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsGridLayout::~QGraphicsGridLayout()': the destructor:
    Python never removes a C++ QGraphicsGridLayout.

  What has no ritual
  ------------------

  4 of the 51 functions Qt declares: 2 forbidden; 2 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QGraphicsGridLayout is created at the first use, not by
    'QGraphicsGridLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsGridLayout.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsGridLayout'

  #  A C++ QGraphicsGridLayout Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsGridLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def horizontalSpacing(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsGridLayout::horizontalSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#horizontalSpacing
    """
    #  qreal QGraphicsGridLayout::horizontalSpacing() const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout17horizontalSpacingEv',
    )

  def verticalSpacing(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsGridLayout::verticalSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#verticalSpacing
    """
    #  qreal QGraphicsGridLayout::verticalSpacing() const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout15verticalSpacingEv',
    )

  @overload(int)
  def rowSpacing(self, row: int) -> float:
    """
    Calls Qt's 'qreal QGraphicsGridLayout::rowSpacing(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowSpacing

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QGraphicsGridLayout::rowSpacing(int row) const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout10rowSpacingEi', row,
    )

  @overload(int)
  def columnSpacing(self, column: int) -> float:
    """
    Calls Qt's 'qreal QGraphicsGridLayout::columnSpacing(int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnSpacing

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QGraphicsGridLayout::columnSpacing(int column) const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout13columnSpacingEi', column,
    )

  @overload(int)
  def rowStretchFactor(self, row: int) -> int:
    """
    Calls Qt's 'int QGraphicsGridLayout::rowStretchFactor(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowStretchFactor

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  int QGraphicsGridLayout::rowStretchFactor(int row) const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout16rowStretchFactorEi', row,
    )

  @overload(int)
  def columnStretchFactor(self, column: int) -> int:
    """
    Calls Qt's 'int QGraphicsGridLayout::columnStretchFactor(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnStretchFactor

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QGraphicsGridLayout::columnStretchFactor(int column) const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout19columnStretchFactorEi', column,
    )

  @overload(int)
  def rowMinimumHeight(self, row: int) -> float:
    """
    Calls Qt's 'qreal QGraphicsGridLayout::rowMinimumHeight(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowMinimumHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QGraphicsGridLayout::rowMinimumHeight(int row) const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout16rowMinimumHeightEi', row,
    )

  @overload(int)
  def rowPreferredHeight(self, row: int) -> float:
    """
    Calls Qt's 'qreal QGraphicsGridLayout::rowPreferredHeight(int row)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowPreferredHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QGraphicsGridLayout::rowPreferredHeight(int row) const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout18rowPreferredHeightEi', row,
    )

  @overload(int)
  def rowMaximumHeight(self, row: int) -> float:
    """
    Calls Qt's 'qreal QGraphicsGridLayout::rowMaximumHeight(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowMaximumHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  qreal QGraphicsGridLayout::rowMaximumHeight(int row) const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout16rowMaximumHeightEi', row,
    )

  @overload(int)
  def columnMinimumWidth(self, column: int) -> float:
    """
    Calls Qt's 'qreal QGraphicsGridLayout::columnMinimumWidth(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnMinimumWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QGraphicsGridLayout::columnMinimumWidth(int column) const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout18columnMinimumWidthEi', column,
    )

  @overload(int)
  def columnPreferredWidth(self, column: int) -> float:
    """
    Calls Qt's 'qreal QGraphicsGridLayout::columnPreferredWidth(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnPreferredWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QGraphicsGridLayout::columnPreferredWidth(int column) const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout20columnPreferredWidthEi', column,
    )

  @overload(int)
  def columnMaximumWidth(self, column: int) -> float:
    """
    Calls Qt's 'qreal QGraphicsGridLayout::columnMaximumWidth(int column)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnMaximumWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  qreal QGraphicsGridLayout::columnMaximumWidth(int column) const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout18columnMaximumWidthEi', column,
    )

  @overload(int)
  def rowAlignment(self, row: int) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QGraphicsGridLayout::rowAlignment(int row)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowAlignment

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QGraphicsGridLayout::rowAlignment(int row) const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout12rowAlignmentEi', row,
    ))

  @overload(int)
  def columnAlignment(self, column: int) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QGraphicsGridLayout::columnAlignment(int
    column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnAlignment

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QGraphicsGridLayout::columnAlignment(int column) const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout15columnAlignmentEi', column,
    ))

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def alignment(self, item: Optional[QGraphicsLayoutItem]) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment
    QGraphicsGridLayout::alignment(QGraphicsLayoutItem *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsgridlayout.html#alignment

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QGraphicsGridLayout::alignment(QGraphicsLayoutItem
    #      *item) const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout9alignmentEP19QGraphicsLayoutItem',
        self._addressOf(item, 'QGraphicsLayoutItem'),
    ))

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QGraphicsGridLayout::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsgridlayout.html#rowCount
    """
    #  int QGraphicsGridLayout::rowCount() const
    return self.uglySide.call('ritual_ZNK19QGraphicsGridLayout8rowCountEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QGraphicsGridLayout::columnCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#columnCount
    """
    #  int QGraphicsGridLayout::columnCount() const
    return self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout11columnCountEv',
    )

  @overload(int, int)
  def itemAt(self, row: int, column: int) -> Optional[QGraphicsLayoutItem]:
    """
    Calls Qt's 'QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int row, int
    column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsgridlayout.html#itemAt

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QGraphicsLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int row, int column)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QGraphicsGridLayout6itemAtEii', row, column,
    )
    return QGraphicsLayoutItem._cuteAt(address)

  @overload(int)
  def itemAt(self, index: int) -> Optional[QGraphicsLayoutItem]:
    """
    Calls Qt's 'QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsgridlayout.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QGraphicsLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayoutItem *QGraphicsGridLayout::itemAt(int index) const
    ritual = 'ritual_ZNK19QGraphicsGridLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGraphicsGridLayout6itemAtEi'
    address = self.uglySide.call(ritual, index)
    return QGraphicsLayoutItem._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QGraphicsGridLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsgridlayout.html#count
    """
    #  int QGraphicsGridLayout::count() const
    ritual = 'ritual_ZNK19QGraphicsGridLayout5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QGraphicsGridLayout5countEv'
    return self.uglySide.call(ritual)

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsGridLayout::sizeHint(Qt::SizeHint which,
    const QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsgridlayout.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : Optional[QSizeF]
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own. May be left out, as in Qt: a new 'QSizeF()' is then passed on.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGraphicsGridLayout::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    ritual = (
        'ritual_ZNK19QGraphicsGridLayout8sizeHintEN2Qt8SizeHintERK6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK19QGraphicsGridLayout8sizeHintEN2Qt8SizeHintERK6QS'
          'izeF')
    address = self.uglySide.call(
        ritual, which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setHorizontalSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setHorizontalSpacing(qreal
    spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setHorizontalSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setHorizontalSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout20setHorizontalSpacingEd', spacing,
    )

  @overload(float)
  def setVerticalSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setVerticalSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setVerticalSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setVerticalSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout18setVerticalSpacingEd', spacing,
    )

  @overload(float)
  def setSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout10setSpacingEd', spacing,
    )

  @overload(int, float)
  def setRowSpacing(self, row: int, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setRowSpacing(int row, qreal
    spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowSpacing

    Parameters
    ----------

    row : int
      Passed on as it is.

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setRowSpacing(int row, qreal spacing)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout13setRowSpacingEid', row, spacing,
    )

  @overload(int, float)
  def setColumnSpacing(self, column: int, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setColumnSpacing(int column, qreal
    spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnSpacing

    Parameters
    ----------

    column : int
      Passed on as it is.

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setColumnSpacing(int column, qreal spacing)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout16setColumnSpacingEid',
        column, spacing,
    )

  @overload(int, int)
  def setRowStretchFactor(self, row: int, stretch: int) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setRowStretchFactor(int row, int
    stretch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowStretchFactor

    Parameters
    ----------

    row : int
      Passed on as it is.

    stretch : int
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setRowStretchFactor(int row, int stretch)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout19setRowStretchFactorEii',
        row, stretch,
    )

  @overload(int, int)
  def setColumnStretchFactor(self, column: int, stretch: int) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setColumnStretchFactor(int column,
    int stretch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnStretchFactor

    Parameters
    ----------

    column : int
      Passed on as it is.

    stretch : int
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setColumnStretchFactor(int column, int
    #      stretch)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout22setColumnStretchFactorEii',
        column, stretch,
    )

  @overload(int, float)
  def setRowMinimumHeight(self, row: int, height: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setRowMinimumHeight(int row, qreal
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowMinimumHeight

    Parameters
    ----------

    row : int
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setRowMinimumHeight(int row, qreal height)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout19setRowMinimumHeightEid',
        row, height,
    )

  @overload(int, float)
  def setRowPreferredHeight(self, row: int, height: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setRowPreferredHeight(int row,
    qreal height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowPreferredHeight

    Parameters
    ----------

    row : int
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setRowPreferredHeight(int row, qreal height)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout21setRowPreferredHeightEid',
        row, height,
    )

  @overload(int, float)
  def setRowMaximumHeight(self, row: int, height: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setRowMaximumHeight(int row, qreal
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowMaximumHeight

    Parameters
    ----------

    row : int
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setRowMaximumHeight(int row, qreal height)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout19setRowMaximumHeightEid',
        row, height,
    )

  @overload(int, float)
  def setRowFixedHeight(self, row: int, height: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setRowFixedHeight(int row, qreal
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowFixedHeight

    Parameters
    ----------

    row : int
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setRowFixedHeight(int row, qreal height)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout17setRowFixedHeightEid', row, height,
    )

  @overload(int, float)
  def setColumnMinimumWidth(self, column: int, width: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setColumnMinimumWidth(int column,
    qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnMinimumWidth

    Parameters
    ----------

    column : int
      Passed on as it is.

    width : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setColumnMinimumWidth(int column, qreal
    #      width)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout21setColumnMinimumWidthEid',
        column, width,
    )

  @overload(int, float)
  def setColumnPreferredWidth(self, column: int, width: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setColumnPreferredWidth(int column,
    qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnPreferredWidth

    Parameters
    ----------

    column : int
      Passed on as it is.

    width : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setColumnPreferredWidth(int column, qreal
    #      width)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout23setColumnPreferredWidthEid',
        column, width,
    )

  @overload(int, float)
  def setColumnMaximumWidth(self, column: int, width: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setColumnMaximumWidth(int column,
    qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnMaximumWidth

    Parameters
    ----------

    column : int
      Passed on as it is.

    width : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setColumnMaximumWidth(int column, qreal
    #      width)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout21setColumnMaximumWidthEid',
        column, width,
    )

  @overload(int, float)
  def setColumnFixedWidth(self, column: int, width: float) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setColumnFixedWidth(int column,
    qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnFixedWidth

    Parameters
    ----------

    column : int
      Passed on as it is.

    width : float
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::setColumnFixedWidth(int column, qreal width)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout19setColumnFixedWidthEid',
        column, width,
    )

  @overload(int, Qt.Alignment)
  def setRowAlignment(self, row: int, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setRowAlignment(int row,
    Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setRowAlignment

    Parameters
    ----------

    row : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QGraphicsGridLayout::setRowAlignment(int row, Qt::Alignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout15setRowAlignmentEi6QFlagsIN2Qt13Ali'
        'gnmentFlagEE',
        row, alignment.value,
    )

  @overload(int, Qt.Alignment)
  def setColumnAlignment(self, column: int, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setColumnAlignment(int column,
    Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setColumnAlignment

    Parameters
    ----------

    column : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QGraphicsGridLayout::setColumnAlignment(int column, Qt::Alignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout18setColumnAlignmentEi6QFlagsIN2Qt13'
        'AlignmentFlagEE',
        column, alignment.value,
    )

  @overload(QGraphicsLayoutItem, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def setAlignment(
      self,
      item: Optional[QGraphicsLayoutItem],
      alignment: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setAlignment(QGraphicsLayoutItem
    *item, Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setAlignment

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QGraphicsGridLayout::setAlignment(QGraphicsLayoutItem *item,
    #      Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout12setAlignmentEP19QGraphicsLayoutIte'
        'm6QFlagsIN2Qt13AlignmentFlagEE',
        self._addressOf(item, 'QGraphicsLayoutItem'), alignment.value,
    )

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::setGeometry(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsGridLayout::setGeometry(const QRectF &rect)
    ritual = 'ritual_ZN19QGraphicsGridLayout11setGeometryERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGraphicsGridLayout11setGeometryERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

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
  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsLayoutItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsGridLayout::QGraphicsGridLayout(QGraphicsLayoutItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#QGraphicsGridLayout

    Parameters
    ----------

    parent : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsGridLayout::QGraphicsGridLayout(QGraphicsLayoutItem *parent)
    self._noteCreation(QGraphicsGridLayout, lambda: Rituals.call(
        'ritual_ZN19QGraphicsGridLayoutC1EP19QGraphicsLayoutItem',
        self._addressOf(parent, 'QGraphicsLayoutItem'),
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

  @overload(QGraphicsLayoutItem, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  @overload(QGraphicsLayoutItem, int, int, int, int, Qt.Alignment)
  @overload(NoneType, int, int, int, int, Qt.Alignment)
  def addItem(
      self,
      item: Optional[QGraphicsLayoutItem],
      row: int,
      column: int,
      rowSpan: int,
      columnSpan: int,
      alignment: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::addItem(QGraphicsLayoutItem *item,
    int row, int column, int rowSpan, int columnSpan, Qt::Alignment
    alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsgridlayout.html#addItem

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    rowSpan : int
      Passed on as it is.

    columnSpan : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  void QGraphicsGridLayout::addItem(QGraphicsLayoutItem *item, int row,
    #      int column, int rowSpan, int columnSpan, Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout7addItemEP19QGraphicsLayoutItemiiii6'
        'QFlagsIN2Qt13AlignmentFlagEE',
        self._addressOf(item, 'QGraphicsLayoutItem'), row, column, rowSpan,
        columnSpan, alignment.value,
    )

  @overload(QGraphicsLayoutItem, int, int)
  @overload(NoneType, int, int)
  @overload(QGraphicsLayoutItem, int, int, Qt.Alignment)
  @overload(NoneType, int, int, Qt.Alignment)
  def addItem(
      self,
      item: Optional[QGraphicsLayoutItem],
      row: int,
      column: int,
      alignment: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::addItem(QGraphicsLayoutItem *item,
    int row, int column, Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsgridlayout.html#addItem

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    alignment : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  void QGraphicsGridLayout::addItem(QGraphicsLayoutItem *item, int row,
    #      int column, Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout7addItemEP19QGraphicsLayoutItemii6QF'
        'lagsIN2Qt13AlignmentFlagEE',
        self._addressOf(item, 'QGraphicsLayoutItem'), row, column,
        alignment.value,
    )

  @overload(int)
  def removeAt(self, index: int) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::removeAt(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsgridlayout.html#removeAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QGraphicsGridLayout::removeAt(int index)
    ritual = 'ritual_ZN19QGraphicsGridLayout8removeAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGraphicsGridLayout8removeAtEi'
    self.uglySide.call(ritual, index)

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QGraphicsLayoutItem]) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::removeItem(QGraphicsLayoutItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#removeItem

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsGridLayout::removeItem(QGraphicsLayoutItem *item)
    self.uglySide.call(
        'ritual_ZN19QGraphicsGridLayout10removeItemEP19QGraphicsLayoutItem',
        self._addressOf(item, 'QGraphicsLayoutItem'),
    )

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayout::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayout.html#invalidate
    """
    #  void QGraphicsGridLayout::invalidate()
    ritual = 'ritual_ZN19QGraphicsGridLayout10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QGraphicsGridLayout10invalidateEv'
    self.uglySide.call(ritual)
