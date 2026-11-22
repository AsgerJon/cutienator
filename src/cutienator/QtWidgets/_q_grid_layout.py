"""
QGridLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgridlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QLayout, QLayoutItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect, QSize
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGridLayout(QLayout):
  """
  The cute side of Qt's QGridLayout: a plain Python object standing in front
  of one C++ QGridLayout.

  It is built on the cute 'QLayout', as Qt's QGridLayout is built on Qt's
  QLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGridLayout that has a ritual and that Python can
  call so far, 38 names in all: 'metaObject', 'tr', 'sizeHint',
  'minimumSize', 'maximumSize', 'setHorizontalSpacing', 'horizontalSpacing',
  'setVerticalSpacing', 'verticalSpacing', 'setSpacing', 'spacing',
  'setRowStretch', 'setColumnStretch', 'rowStretch', 'columnStretch',
  'setRowMinimumHeight', 'setColumnMinimumWidth', 'rowMinimumHeight',
  'columnMinimumWidth', 'columnCount', 'rowCount', 'cellRect',
  'hasHeightForWidth', 'heightForWidth', 'minimumHeightForWidth',
  'expandingDirections', 'invalidate', 'addWidget', 'addLayout',
  'setOriginCorner', 'originCorner', 'itemAt', 'itemAtPosition', 'takeAt',
  'count', 'setGeometry', 'addItem', 'setDefaultPositioning'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGridLayout::~QGridLayout()': the destructor: Python never removes
    a C++ QGridLayout.
  - Qt's 'void QGridLayout::getItemPosition(int idx, int *row, int *column,
    int *rowSpan, int *columnSpan) const': takes a number to change where it
    is.

  What has no ritual
  ------------------

  8 of the 53 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QGridLayout is created at the first use, not by
    'QGridLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGridLayout.
  - Qt tells when it has removed the C++ QGridLayout. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QGridLayout::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#tr

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
    #  QString QGridLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QGridLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGridLayout'

  #  A C++ QGridLayout Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGridLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGridLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGridLayout::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QGridLayout10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QGridLayout::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGridLayout::sizeHint() const
    ritual = 'ritual_ZNK11QGridLayout8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGridLayout8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QGridLayout::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGridLayout::minimumSize() const
    ritual = 'ritual_ZNK11QGridLayout11minimumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGridLayout11minimumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QGridLayout::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGridLayout::maximumSize() const
    ritual = 'ritual_ZNK11QGridLayout11maximumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGridLayout11maximumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def horizontalSpacing(self) -> int:
    """
    Calls Qt's 'int QGridLayout::horizontalSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#horizontalSpacing
    """
    #  int QGridLayout::horizontalSpacing() const
    return self.uglySide.call('ritual_ZNK11QGridLayout17horizontalSpacingEv')

  def verticalSpacing(self) -> int:
    """
    Calls Qt's 'int QGridLayout::verticalSpacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#verticalSpacing
    """
    #  int QGridLayout::verticalSpacing() const
    return self.uglySide.call('ritual_ZNK11QGridLayout15verticalSpacingEv')

  def spacing(self) -> int:
    """
    Calls Qt's 'int QGridLayout::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#spacing
    """
    #  int QGridLayout::spacing() const
    ritual = 'ritual_ZNK11QGridLayout7spacingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGridLayout7spacingEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def rowStretch(self, row: int) -> int:
    """
    Calls Qt's 'int QGridLayout::rowStretch(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#rowStretch

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  int QGridLayout::rowStretch(int row) const
    return self.uglySide.call('ritual_ZNK11QGridLayout10rowStretchEi', row)

  @overload(int)
  def columnStretch(self, column: int) -> int:
    """
    Calls Qt's 'int QGridLayout::columnStretch(int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#columnStretch

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QGridLayout::columnStretch(int column) const
    return self.uglySide.call(
        'ritual_ZNK11QGridLayout13columnStretchEi', column,
    )

  @overload(int)
  def rowMinimumHeight(self, row: int) -> int:
    """
    Calls Qt's 'int QGridLayout::rowMinimumHeight(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#rowMinimumHeight

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  int QGridLayout::rowMinimumHeight(int row) const
    return self.uglySide.call(
        'ritual_ZNK11QGridLayout16rowMinimumHeightEi', row,
    )

  @overload(int)
  def columnMinimumWidth(self, column: int) -> int:
    """
    Calls Qt's 'int QGridLayout::columnMinimumWidth(int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayout.html#columnMinimumWidth

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QGridLayout::columnMinimumWidth(int column) const
    return self.uglySide.call(
        'ritual_ZNK11QGridLayout18columnMinimumWidthEi', column,
    )

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QGridLayout::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#columnCount
    """
    #  int QGridLayout::columnCount() const
    return self.uglySide.call('ritual_ZNK11QGridLayout11columnCountEv')

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QGridLayout::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#rowCount
    """
    #  int QGridLayout::rowCount() const
    return self.uglySide.call('ritual_ZNK11QGridLayout8rowCountEv')

  @overload(int, int)
  def cellRect(self, row: int, column: int) -> QRect:
    """
    Calls Qt's 'QRect QGridLayout::cellRect(int row, int column) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#cellRect

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QGridLayout::cellRect(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QGridLayout8cellRectEii', row, column,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QGridLayout::hasHeightForWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#hasHeightForWidth
    """
    #  bool QGridLayout::hasHeightForWidth() const
    ritual = 'ritual_ZNK11QGridLayout17hasHeightForWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGridLayout17hasHeightForWidthEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def heightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QGridLayout::heightForWidth(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#heightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QGridLayout::heightForWidth(int a0) const
    ritual = 'ritual_ZNK11QGridLayout14heightForWidthEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGridLayout14heightForWidthEi'
    return self.uglySide.call(ritual, a0)

  @overload(int)
  def minimumHeightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QGridLayout::minimumHeightForWidth(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayout.html#minimumHeightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QGridLayout::minimumHeightForWidth(int a0) const
    ritual = 'ritual_ZNK11QGridLayout21minimumHeightForWidthEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGridLayout21minimumHeightForWidthEi'
    return self.uglySide.call(ritual, a0)

  def expandingDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QGridLayout::expandingDirections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayout.html#expandingDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QGridLayout::expandingDirections() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK11QGridLayout19expandingDirectionsEv',
    ))

  def originCorner(self) -> Qt.Corner:
    """
    Calls Qt's 'Qt::Corner QGridLayout::originCorner() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#originCorner

    Returns
    -------

    Qt.Corner
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Corner(number)' gives.
    """
    #  Qt::Corner QGridLayout::originCorner() const
    return Qt.Corner(self.uglySide.call(
        'ritual_ZNK11QGridLayout12originCornerEv',
    ))

  @overload(int)
  def itemAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QGridLayout::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QGridLayout::itemAt(int index) const
    ritual = 'ritual_ZNK11QGridLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGridLayout6itemAtEi'
    address = self.uglySide.call(ritual, index)
    return QLayoutItem._cuteAt(address)

  @overload(int, int)
  def itemAtPosition(self, row: int, column: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QGridLayout::itemAtPosition(int row, int column)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#itemAtPosition

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QGridLayout::itemAtPosition(int row, int column) const
    address = self.uglySide.call(
        'ritual_ZNK11QGridLayout14itemAtPositionEii', row, column,
    )
    return QLayoutItem._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QGridLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#count
    """
    #  int QGridLayout::count() const
    ritual = 'ritual_ZNK11QGridLayout5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QGridLayout5countEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setHorizontalSpacing(self, spacing: int) -> None:
    """
    Calls Qt's 'void QGridLayout::setHorizontalSpacing(int spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayout.html#setHorizontalSpacing

    Parameters
    ----------

    spacing : int
      Passed on as it is.
    """
    #  void QGridLayout::setHorizontalSpacing(int spacing)
    self.uglySide.call(
        'ritual_ZN11QGridLayout20setHorizontalSpacingEi', spacing,
    )

  @overload(int)
  def setVerticalSpacing(self, spacing: int) -> None:
    """
    Calls Qt's 'void QGridLayout::setVerticalSpacing(int spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayout.html#setVerticalSpacing

    Parameters
    ----------

    spacing : int
      Passed on as it is.
    """
    #  void QGridLayout::setVerticalSpacing(int spacing)
    self.uglySide.call(
        'ritual_ZN11QGridLayout18setVerticalSpacingEi', spacing,
    )

  @overload(int)
  def setSpacing(self, spacing: int) -> None:
    """
    Calls Qt's 'void QGridLayout::setSpacing(int spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#setSpacing

    Parameters
    ----------

    spacing : int
      Passed on as it is.
    """
    #  void QGridLayout::setSpacing(int spacing)
    ritual = 'ritual_ZN11QGridLayout10setSpacingEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QGridLayout10setSpacingEi'
    self.uglySide.call(ritual, spacing)

  @overload(int, int)
  def setRowStretch(self, row: int, stretch: int) -> None:
    """
    Calls Qt's 'void QGridLayout::setRowStretch(int row, int stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#setRowStretch

    Parameters
    ----------

    row : int
      Passed on as it is.

    stretch : int
      Passed on as it is.
    """
    #  void QGridLayout::setRowStretch(int row, int stretch)
    self.uglySide.call(
        'ritual_ZN11QGridLayout13setRowStretchEii', row, stretch,
    )

  @overload(int, int)
  def setColumnStretch(self, column: int, stretch: int) -> None:
    """
    Calls Qt's 'void QGridLayout::setColumnStretch(int column, int stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#setColumnStretch

    Parameters
    ----------

    column : int
      Passed on as it is.

    stretch : int
      Passed on as it is.
    """
    #  void QGridLayout::setColumnStretch(int column, int stretch)
    self.uglySide.call(
        'ritual_ZN11QGridLayout16setColumnStretchEii', column, stretch,
    )

  @overload(int, int)
  def setRowMinimumHeight(self, row: int, minSize: int) -> None:
    """
    Calls Qt's 'void QGridLayout::setRowMinimumHeight(int row, int minSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayout.html#setRowMinimumHeight

    Parameters
    ----------

    row : int
      Passed on as it is.

    minSize : int
      Passed on as it is.
    """
    #  void QGridLayout::setRowMinimumHeight(int row, int minSize)
    self.uglySide.call(
        'ritual_ZN11QGridLayout19setRowMinimumHeightEii', row, minSize,
    )

  @overload(int, int)
  def setColumnMinimumWidth(self, column: int, minSize: int) -> None:
    """
    Calls Qt's 'void QGridLayout::setColumnMinimumWidth(int column, int
    minSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayout.html#setColumnMinimumWidth

    Parameters
    ----------

    column : int
      Passed on as it is.

    minSize : int
      Passed on as it is.
    """
    #  void QGridLayout::setColumnMinimumWidth(int column, int minSize)
    self.uglySide.call(
        'ritual_ZN11QGridLayout21setColumnMinimumWidthEii', column, minSize,
    )

  @overload(Qt.Corner)
  def setOriginCorner(self, a0: Qt.Corner) -> None:
    """
    Calls Qt's 'void QGridLayout::setOriginCorner(Qt::Corner a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#setOriginCorner

    Parameters
    ----------

    a0 : Qt.Corner
      Passed on as its number.
    """
    #  void QGridLayout::setOriginCorner(Qt::Corner a0)
    self.uglySide.call(
        'ritual_ZN11QGridLayout15setOriginCornerEN2Qt6CornerE', a0.value,
    )

  @overload(QRect)
  def setGeometry(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QGridLayout::setGeometry(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#setGeometry

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QGridLayout::setGeometry(const QRect &a0)
    ritual = 'ritual_ZN11QGridLayout11setGeometryERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QGridLayout11setGeometryERK5QRect'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(int, Qt.Orientation)
  def setDefaultPositioning(self, n: int, orient: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QGridLayout::setDefaultPositioning(int n,
    Qt::Orientation orient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayout.html#setDefaultPositioning

    Parameters
    ----------

    n : int
      Passed on as it is.

    orient : Qt.Orientation
      Passed on as its number.
    """
    #  void QGridLayout::setDefaultPositioning(int n, Qt::Orientation orient)
    self.uglySide.call(
        'ritual_ZN11QGridLayout21setDefaultPositioningEiN2Qt11OrientationE',
        n, orient.value,
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
    Notes what was given, for Qt's 'QGridLayout::QGridLayout(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#QGridLayout

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGridLayout::QGridLayout(QWidget *parent)
    self._noteCreation(QGridLayout, lambda: Rituals.call(
        'ritual_ZN11QGridLayoutC1EP7QWidget', self._addressOf(parent),
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QGridLayout::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#invalidate
    """
    #  void QGridLayout::invalidate()
    ritual = 'ritual_ZN11QGridLayout10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QGridLayout10invalidateEv'
    self.uglySide.call(ritual)

  @overload(QWidget)
  @overload(NoneType)
  def addWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QGridLayout::addWidget(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#addWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGridLayout::addWidget(QWidget *w)
    self.uglySide.call(
        'ritual_ZN11QGridLayout9addWidgetEP7QWidget', self._addressOf(w),
    )

  @overload(QWidget, int, int)
  @overload(NoneType, int, int)
  @overload(QWidget, int, int, Qt.Alignment)
  @overload(NoneType, int, int, Qt.Alignment)
  def addWidget(
      self,
      a0: Optional[QWidget],
      row: int,
      column: int,
      a3: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Calls Qt's 'void QGridLayout::addWidget(QWidget *a0, int row, int column,
    Qt::Alignment a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#addWidget

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    a3 : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  void QGridLayout::addWidget(QWidget *a0, int row, int column,
    #      Qt::Alignment a3)
    self.uglySide.call(
        'ritual_ZN11QGridLayout9addWidgetEP7QWidgetii6QFlagsIN2Qt13Alignmen'
        'tFlagEE',
        self._addressOf(a0), row, column, a3.value,
    )

  @overload(QWidget, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  @overload(QWidget, int, int, int, int, Qt.Alignment)
  @overload(NoneType, int, int, int, int, Qt.Alignment)
  def addWidget(
      self,
      a0: Optional[QWidget],
      row: int,
      column: int,
      rowSpan: int,
      columnSpan: int,
      a5: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Calls Qt's 'void QGridLayout::addWidget(QWidget *a0, int row, int column,
    int rowSpan, int columnSpan, Qt::Alignment a5)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#addWidget

    Parameters
    ----------

    a0 : Optional[QWidget]
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

    a5 : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  void QGridLayout::addWidget(QWidget *a0, int row, int column, int
    #      rowSpan, int columnSpan, Qt::Alignment a5)
    self.uglySide.call(
        'ritual_ZN11QGridLayout9addWidgetEP7QWidgetiiii6QFlagsIN2Qt13Alignm'
        'entFlagEE',
        self._addressOf(a0), row, column, rowSpan, columnSpan, a5.value,
    )

  @overload(QLayout, int, int)
  @overload(NoneType, int, int)
  @overload(QLayout, int, int, Qt.Alignment)
  @overload(NoneType, int, int, Qt.Alignment)
  def addLayout(
      self,
      a0: Optional[QLayout],
      row: int,
      column: int,
      a3: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Calls Qt's 'void QGridLayout::addLayout(QLayout *a0, int row, int column,
    Qt::Alignment a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#addLayout

    Parameters
    ----------

    a0 : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    a3 : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  void QGridLayout::addLayout(QLayout *a0, int row, int column,
    #      Qt::Alignment a3)
    self.uglySide.call(
        'ritual_ZN11QGridLayout9addLayoutEP7QLayoutii6QFlagsIN2Qt13Alignmen'
        'tFlagEE',
        self._addressOf(a0), row, column, a3.value,
    )

  @overload(QLayout, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  @overload(QLayout, int, int, int, int, Qt.Alignment)
  @overload(NoneType, int, int, int, int, Qt.Alignment)
  def addLayout(
      self,
      a0: Optional[QLayout],
      row: int,
      column: int,
      rowSpan: int,
      columnSpan: int,
      a5: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Calls Qt's 'void QGridLayout::addLayout(QLayout *a0, int row, int column,
    int rowSpan, int columnSpan, Qt::Alignment a5)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#addLayout

    Parameters
    ----------

    a0 : Optional[QLayout]
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

    a5 : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  void QGridLayout::addLayout(QLayout *a0, int row, int column, int
    #      rowSpan, int columnSpan, Qt::Alignment a5)
    self.uglySide.call(
        'ritual_ZN11QGridLayout9addLayoutEP7QLayoutiiii6QFlagsIN2Qt13Alignm'
        'entFlagEE',
        self._addressOf(a0), row, column, rowSpan, columnSpan, a5.value,
    )

  @overload(int)
  def takeAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QGridLayout::takeAt(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#takeAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QGridLayout::takeAt(int index)
    ritual = 'ritual_ZN11QGridLayout6takeAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QGridLayout6takeAtEi'
    address = self.uglySide.call(ritual, index)
    return QLayoutItem._cuteAt(address)

  @overload(QLayoutItem, int, int)
  @overload(NoneType, int, int)
  @overload(QLayoutItem, int, int, int)
  @overload(NoneType, int, int, int)
  @overload(QLayoutItem, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  @overload(QLayoutItem, int, int, int, int, Qt.Alignment)
  @overload(NoneType, int, int, int, int, Qt.Alignment)
  def addItem(
      self,
      item: Optional[QLayoutItem],
      row: int,
      column: int,
      rowSpan: int = 1,
      columnSpan: int = 1,
      a5: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Calls Qt's 'void QGridLayout::addItem(QLayoutItem *item, int row, int
    column, int rowSpan, int columnSpan, Qt::Alignment a5)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#addItem

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    rowSpan : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    columnSpan : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    a5 : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  void QGridLayout::addItem(QLayoutItem *item, int row, int column, int
    #      rowSpan, int columnSpan, Qt::Alignment a5)
    self.uglySide.call(
        'ritual_ZN11QGridLayout7addItemEP11QLayoutItemiiii6QFlagsIN2Qt13Ali'
        'gnmentFlagEE',
        self._addressOf(item, 'QLayoutItem'), row, column, rowSpan,
        columnSpan, a5.value,
    )

  @overload(QLayoutItem)
  @overload(NoneType)
  def addItem(self, a0: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QGridLayout::addItem(QLayoutItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayout.html#addItem

    Parameters
    ----------

    a0 : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGridLayout::addItem(QLayoutItem *a0)
    self.uglySide.call(
        'ritual_own_ZN11QGridLayout7addItemEP11QLayoutItem',
        self._addressOf(a0, 'QLayoutItem'),
    )
