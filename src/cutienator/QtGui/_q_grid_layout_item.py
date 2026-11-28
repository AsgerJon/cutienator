"""
QGridLayoutItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QGridLayoutItem to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QLayoutPolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRectF, QSizeF
  from . import QGridLayoutBox
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']


class QGridLayoutItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGridLayoutItem: a plain Python object standing in
  front of one C++ QGridLayoutItem.

  What exists
  -----------

  Every function of Qt's QGridLayoutItem that has a ritual and that Python
  can call so far, 24 names in all: 'firstRow', 'firstColumn', 'rowSpan',
  'columnSpan', 'lastRow', 'lastColumn', 'setFirstRow', 'setRowSpan',
  'stretchFactor', 'setStretchFactor', 'alignment', 'setAlignment',
  'sizePolicy', 'sizeHint', 'isEmpty', 'setGeometry', 'hasDynamicConstraint',
  'dynamicConstraintOrientation', 'toString', 'geometryWithin', 'box',
  'transpose', 'insertOrRemoveRows', 'effectiveMaxSize'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGridLayoutItem::~QGridLayoutItem()': the destructor: Python never
    removes a C++ QGridLayoutItem.
  - Qt's 'QLayoutPolicy::ControlTypes
    QGridLayoutItem::controlTypes(LayoutSide side) const': names the enum
    'LayoutSide', whose class cannot be named here.

  What to expect
  --------------

  - The C++ QGridLayoutItem is created at the first use, not by
    'QGridLayoutItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGridLayoutItem.
  - Each name of Qt's QGridLayoutItem that has no cute function yet,
    'controlTypes', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGridLayoutItem'

  #  A C++ QGridLayoutItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGridLayoutItem'

  #  The functions Qt calls itself that QGridLayoutItem is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'controlTypes': (
          'QLayoutPolicy::ControlTypes '
          'QGridLayoutItem::controlTypes(LayoutSide) const',
      ),
  }

  #  The functions Qt calls itself that QGridLayoutItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'sizePolicy': (
          ('_ZNK15QGridLayoutItem10sizePolicyEN2Qt11OrientationE',
           ('int', 'flags', 'QtGui:QLayoutPolicy.PolicyFlag'),
           (
               ('int', 'enum', 'QtCore:Qt.Orientation'),
           )),
      ),
      'sizeHint': (
          ('_ZNK15QGridLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF',
           ('address', 'value', 'QtCore:QSizeF'),
           (
               ('int', 'enum', 'QtCore:Qt.SizeHint'),
               ('address', 'value', 'QtCore:QSizeF'),
           )),
      ),
      'isEmpty': (
          ('_ZNK15QGridLayoutItem7isEmptyEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setGeometry': (
          ('_ZN15QGridLayoutItem11setGeometryERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'hasDynamicConstraint': (
          ('_ZNK15QGridLayoutItem20hasDynamicConstraintEv',
           ('bool', 'number', ''),
           ()),
      ),
      'dynamicConstraintOrientation': (
          ('_ZNK15QGridLayoutItem28dynamicConstraintOrientationEv',
           ('int', 'enum', 'QtCore:Qt.Orientation'),
           ()),
      ),
      'toString': (
          ('_ZNK15QGridLayoutItem8toStringEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def firstRow(self) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::firstRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#firstRow
    """
    #  int QGridLayoutItem::firstRow() const
    return self.uglySide.call('ritual_ZNK15QGridLayoutItem8firstRowEv')

  @overload(Qt.Orientation)
  def firstRow(self, orientation: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::firstRow(Qt::Orientation orientation)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#firstRow

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  int QGridLayoutItem::firstRow(Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem8firstRowEN2Qt11OrientationE',
        orientation.value,
    )

  @overload()
  def firstColumn(self) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::firstColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#firstColumn
    """
    #  int QGridLayoutItem::firstColumn() const
    return self.uglySide.call('ritual_ZNK15QGridLayoutItem11firstColumnEv')

  @overload(Qt.Orientation)
  def firstColumn(self, orientation: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::firstColumn(Qt::Orientation orientation)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#firstColumn

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  int QGridLayoutItem::firstColumn(Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem11firstColumnEN2Qt11OrientationE',
        orientation.value,
    )

  @overload()
  def rowSpan(self) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::rowSpan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#rowSpan
    """
    #  int QGridLayoutItem::rowSpan() const
    return self.uglySide.call('ritual_ZNK15QGridLayoutItem7rowSpanEv')

  @overload(Qt.Orientation)
  def rowSpan(self, orientation: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::rowSpan(Qt::Orientation orientation)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#rowSpan

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  int QGridLayoutItem::rowSpan(Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem7rowSpanEN2Qt11OrientationE',
        orientation.value,
    )

  @overload()
  def columnSpan(self) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::columnSpan() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#columnSpan
    """
    #  int QGridLayoutItem::columnSpan() const
    return self.uglySide.call('ritual_ZNK15QGridLayoutItem10columnSpanEv')

  @overload(Qt.Orientation)
  def columnSpan(self, orientation: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::columnSpan(Qt::Orientation orientation)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#columnSpan

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  int QGridLayoutItem::columnSpan(Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem10columnSpanEN2Qt11OrientationE',
        orientation.value,
    )

  @overload()
  def lastRow(self) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::lastRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#lastRow
    """
    #  int QGridLayoutItem::lastRow() const
    return self.uglySide.call('ritual_ZNK15QGridLayoutItem7lastRowEv')

  @overload(Qt.Orientation)
  def lastRow(self, orientation: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::lastRow(Qt::Orientation orientation)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#lastRow

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  int QGridLayoutItem::lastRow(Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem7lastRowEN2Qt11OrientationE',
        orientation.value,
    )

  @overload()
  def lastColumn(self) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::lastColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#lastColumn
    """
    #  int QGridLayoutItem::lastColumn() const
    return self.uglySide.call('ritual_ZNK15QGridLayoutItem10lastColumnEv')

  @overload(Qt.Orientation)
  def lastColumn(self, orientation: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::lastColumn(Qt::Orientation orientation)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#lastColumn

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  int QGridLayoutItem::lastColumn(Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem10lastColumnEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(Qt.Orientation)
  def stretchFactor(self, orientation: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QGridLayoutItem::stretchFactor(Qt::Orientation
    orientation) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#stretchFactor

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  int QGridLayoutItem::stretchFactor(Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem13stretchFactorEN2Qt11OrientationE',
        orientation.value,
    )

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QGridLayoutItem::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QGridLayoutItem::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem9alignmentEv',
    ))

  @overload(Qt.Orientation)
  def sizePolicy(self, orientation: Qt.Orientation) -> QLayoutPolicy.Policy:
    """
    Calls Qt's 'QLayoutPolicy::Policy
    QGridLayoutItem::sizePolicy(Qt::Orientation orientation) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#sizePolicy

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    QLayoutPolicy.Policy
      The value standing for the combination Qt gave back.
    """
    #  QLayoutPolicy::Policy QGridLayoutItem::sizePolicy(Qt::Orientation
    #      orientation) const
    return QLayoutPolicy.Policy(self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem10sizePolicyEN2Qt11OrientationE',
        orientation.value,
    ))

  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(self, which: Qt.SizeHint, constraint: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGridLayoutItem::sizeHint(Qt::SizeHint which, const
    QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGridLayoutItem::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    address = self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF',
        which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGridLayoutItem::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#isEmpty
    """
    #  bool QGridLayoutItem::isEmpty() const
    ritual = 'ritual_ZNK15QGridLayoutItem7isEmptyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGridLayoutItem7isEmptyEv'
    return self.uglySide.call(ritual)

  def hasDynamicConstraint(self) -> bool:
    """
    Calls Qt's 'bool QGridLayoutItem::hasDynamicConstraint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutitem.html#hasDynamicConstraint
    """
    #  bool QGridLayoutItem::hasDynamicConstraint() const
    ritual = 'ritual_ZNK15QGridLayoutItem20hasDynamicConstraintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGridLayoutItem20hasDynamicConstraintEv'
    return self.uglySide.call(ritual)

  def dynamicConstraintOrientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation
    QGridLayoutItem::dynamicConstraintOrientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutitem.html#dynamicConstraintOrientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QGridLayoutItem::dynamicConstraintOrientation() const
    ritual = 'ritual_ZNK15QGridLayoutItem28dynamicConstraintOrientationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QGridLayoutItem28dynamicConstraintOrientationEv')
    return Qt.Orientation(self.uglySide.call(ritual))

  def toString(self) -> str:
    """
    Calls Qt's 'QString QGridLayoutItem::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGridLayoutItem::toString() const
    ritual = 'ritual_ZNK15QGridLayoutItem8toStringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGridLayoutItem8toStringEv'
    return self.uglySide.call(ritual)

  @overload(float, float, float, float, float, Qt.Alignment, bool)
  def geometryWithin(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
      rowDescent: float,
      align: Qt.Alignment,
      snapToPixelGrid: bool,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF QGridLayoutItem::geometryWithin(qreal x, qreal y,
    qreal width, qreal height, qreal rowDescent, Qt::Alignment align, bool
    snapToPixelGrid) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutitem.html#geometryWithin

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    rowDescent : float
      Passed on as it is.

    align : Qt.Alignment
      Passed on as its number.

    snapToPixelGrid : bool
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGridLayoutItem::geometryWithin(qreal x, qreal y, qreal width,
    #      qreal height, qreal rowDescent, Qt::Alignment align, bool
    #      snapToPixelGrid) const
    address = self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem14geometryWithinEddddd6QFlagsIN2Qt13Ali'
        'gnmentFlagEEb',
        x, y, width, height, rowDescent, align.value, snapToPixelGrid,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Qt.Orientation, bool)
  @overload(Qt.Orientation, bool, float)
  def box(
      self,
      orientation: Qt.Orientation,
      snapToPixelGrid: bool,
      constraint: float = -1.0,
  ) -> QGridLayoutBox:
    """
    Calls Qt's 'QGridLayoutBox QGridLayoutItem::box(Qt::Orientation
    orientation, bool snapToPixelGrid, qreal constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#box

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    snapToPixelGrid : bool
      Passed on as it is.

    constraint : float
      Passed on as it is. May be left out, as in Qt: it is then -1.0.

    Returns
    -------

    QGridLayoutBox
      A new cute QGridLayoutBox around the copy Qt gave back. Python owns it.
    """
    #  QGridLayoutBox QGridLayoutItem::box(Qt::Orientation orientation, bool
    #      snapToPixelGrid, qreal constraint) const
    address = self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem3boxEN2Qt11OrientationEbd',
        orientation.value, snapToPixelGrid, constraint,
    )
    from . import QGridLayoutBox
    return QGridLayoutBox._cuteOwning(address)

  @overload(QSizeF)
  def effectiveMaxSize(self, constraint: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGridLayoutItem::effectiveMaxSize(const QSizeF
    &constraint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutitem.html#effectiveMaxSize

    Parameters
    ----------

    constraint : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QGridLayoutItem::effectiveMaxSize(const QSizeF &constraint)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QGridLayoutItem16effectiveMaxSizeERK6QSizeF',
        self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  @overload(int, Qt.Orientation)
  def setFirstRow(
      self,
      row: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutItem::setFirstRow(int row, Qt::Orientation
    orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#setFirstRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  void QGridLayoutItem::setFirstRow(int row, Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN15QGridLayoutItem11setFirstRowEiN2Qt11OrientationE',
        row, orientation.value,
    )

  @overload(int)
  @overload(int, Qt.Orientation)
  def setRowSpan(
      self,
      rowSpan: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutItem::setRowSpan(int rowSpan, Qt::Orientation
    orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#setRowSpan

    Parameters
    ----------

    rowSpan : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Orientation.Vertical.
    """
    #  void QGridLayoutItem::setRowSpan(int rowSpan, Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN15QGridLayoutItem10setRowSpanEiN2Qt11OrientationE',
        rowSpan, orientation.value,
    )

  @overload(int, Qt.Orientation)
  def setStretchFactor(
      self,
      stretch: int,
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutItem::setStretchFactor(int stretch,
    Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutitem.html#setStretchFactor

    Parameters
    ----------

    stretch : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGridLayoutItem::setStretchFactor(int stretch, Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN15QGridLayoutItem16setStretchFactorEiN2Qt11OrientationE',
        stretch, orientation.value,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QGridLayoutItem::setAlignment(Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QGridLayoutItem::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN15QGridLayoutItem12setAlignmentE6QFlagsIN2Qt13AlignmentFl'
        'agEE',
        alignment.value,
    )

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGridLayoutItem::setGeometry(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGridLayoutItem::setGeometry(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN15QGridLayoutItem11setGeometryERK6QRectF',
        self._valueOf(rect),
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

  @overload(int, int)
  @overload(int, int, int)
  @overload(int, int, int, int)
  @overload(int, int, int, int, Qt.Alignment)
  def __init__(
      self,
      row: int,
      column: int,
      rowSpan: int = 1,
      columnSpan: int = 1,
      alignment: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QGridLayoutItem::QGridLayoutItem(int row,
    int column, int rowSpan, int columnSpan, Qt::Alignment alignment)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutitem.html#QGridLayoutItem

    Parameters
    ----------

    row : int
      Passed on as it is.

    column : int
      Passed on as it is.

    rowSpan : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    columnSpan : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    alignment : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  QGridLayoutItem::QGridLayoutItem(int row, int column, int rowSpan, int
    #      columnSpan, Qt::Alignment alignment)
    self._noteCreation(QGridLayoutItem, lambda: Rituals.call(
        'ritual_ZN15QGridLayoutItemC1Eiiii6QFlagsIN2Qt13AlignmentFlagEE',
        row, column, rowSpan, columnSpan, alignment.value,
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

  def transpose(self) -> None:
    """
    Calls Qt's 'void QGridLayoutItem::transpose()'.

    Qt's own words: https://doc.qt.io/qt-6/qgridlayoutitem.html#transpose
    """
    #  void QGridLayoutItem::transpose()
    self.uglySide.call('ritual_ZN15QGridLayoutItem9transposeEv')

  @overload(int, int)
  @overload(int, int, Qt.Orientation)
  def insertOrRemoveRows(
      self,
      row: int,
      delta: int,
      orientation: Qt.Orientation = Qt.Orientation.Vertical,
  ) -> None:
    """
    Calls Qt's 'void QGridLayoutItem::insertOrRemoveRows(int row, int delta,
    Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgridlayoutitem.html#insertOrRemoveRows

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
    #  void QGridLayoutItem::insertOrRemoveRows(int row, int delta,
    #      Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN15QGridLayoutItem18insertOrRemoveRowsEiiN2Qt11Orientation'
        'E',
        row, delta, orientation.value,
    )

  @staticmethod
  def controlTypes(*__, **_) -> Never:
    """
    Qt's 'QLayoutPolicy::ControlTypes
    QGridLayoutItem::controlTypes(LayoutSide side) const': names the enum
    'LayoutSide', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QGridLayoutItem.controlTypes' has no cute function yet. Qt's "
        "'QLayoutPolicy::ControlTypes "
        "QGridLayoutItem::controlTypes(LayoutSide side) const': names the "
        "enum 'LayoutSide', whose class cannot be named here.")
