"""
QGraphicsLinearLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicslinearlayout.h, Qt 6.12.0. Changes made here are lost.
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


class QGraphicsLinearLayout(QGraphicsLayout):
  """
  The cute side of Qt's QGraphicsLinearLayout: a plain Python object standing
  in front of one C++ QGraphicsLinearLayout.

  It is built on the cute 'QGraphicsLayout', as Qt's QGraphicsLinearLayout is
  built on Qt's QGraphicsLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsLinearLayout that has a ritual and that
  Python can call so far, 22 names in all: 'setOrientation', 'orientation',
  'addItem', 'addStretch', 'insertItem', 'insertStretch', 'removeItem',
  'removeAt', 'setSpacing', 'spacing', 'setItemSpacing', 'itemSpacing',
  'setStretchFactor', 'stretchFactor', 'setAlignment', 'alignment',
  'setGeometry', 'count', 'itemAt', 'invalidate', 'sizeHint', 'dump'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsLinearLayout::~QGraphicsLinearLayout()': the destructor:
    Python never removes a C++ QGraphicsLinearLayout.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 forbidden; 2 private.

  What to expect
  --------------

  - The C++ QGraphicsLinearLayout is created at the first use, not by
    'QGraphicsLinearLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsLinearLayout.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsLinearLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QGraphicsLinearLayout::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QGraphicsLinearLayout::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK21QGraphicsLinearLayout11orientationEv',
    ))

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsLinearLayout::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslinearlayout.html#spacing
    """
    #  qreal QGraphicsLinearLayout::spacing() const
    return self.uglySide.call('ritual_ZNK21QGraphicsLinearLayout7spacingEv')

  @overload(int)
  def itemSpacing(self, index: int) -> float:
    """
    Calls Qt's 'qreal QGraphicsLinearLayout::itemSpacing(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#itemSpacing

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  qreal QGraphicsLinearLayout::itemSpacing(int index) const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsLinearLayout11itemSpacingEi', index,
    )

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def stretchFactor(self, item: Optional[QGraphicsLayoutItem]) -> int:
    """
    Calls Qt's 'int QGraphicsLinearLayout::stretchFactor(QGraphicsLayoutItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#stretchFactor

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QGraphicsLinearLayout::stretchFactor(QGraphicsLayoutItem *item)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QGraphicsLinearLayout13stretchFactorEP19QGraphicsLayou'
        'tItem',
        self._addressOf(item, 'QGraphicsLayoutItem'),
    )

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def alignment(self, item: Optional[QGraphicsLayoutItem]) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment
    QGraphicsLinearLayout::alignment(QGraphicsLayoutItem *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#alignment

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
    #  Qt::Alignment QGraphicsLinearLayout::alignment(QGraphicsLayoutItem
    #      *item) const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK21QGraphicsLinearLayout9alignmentEP19QGraphicsLayoutItem',
        self._addressOf(item, 'QGraphicsLayoutItem'),
    ))

  def count(self) -> int:
    """
    Calls Qt's 'int QGraphicsLinearLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslinearlayout.html#count
    """
    #  int QGraphicsLinearLayout::count() const
    return self.uglySide.call('ritual_ZNK21QGraphicsLinearLayout5countEv')

  @overload(int)
  def itemAt(self, index: int) -> Optional[QGraphicsLayoutItem]:
    """
    Calls Qt's 'QGraphicsLayoutItem *QGraphicsLinearLayout::itemAt(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslinearlayout.html#itemAt

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
    #  QGraphicsLayoutItem *QGraphicsLinearLayout::itemAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK21QGraphicsLinearLayout6itemAtEi', index,
    )
    return QGraphicsLayoutItem._cuteAt(address)

  @overload(Qt.SizeHint)
  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(
      self,
      which: Qt.SizeHint,
      constraint: Optional[QSizeF] = None,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsLinearLayout::sizeHint(Qt::SizeHint which,
    const QSizeF &constraint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#sizeHint

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
    #  QSizeF QGraphicsLinearLayout::sizeHint(Qt::SizeHint which, const
    #      QSizeF &constraint) const
    if constraint is None:
      from ..QtCore import QSizeF
      constraint = QSizeF()
    address = self.uglySide.call(
        'ritual_ZNK21QGraphicsLinearLayout8sizeHintEN2Qt8SizeHintERK6QSizeF',
        which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGraphicsLinearLayout::setOrientation(Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout14setOrientationEN2Qt11Orientation'
        'E',
        orientation.value,
    )

  @overload(float)
  def setSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::setSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsLinearLayout::setSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout10setSpacingEd', spacing,
    )

  @overload(int, float)
  def setItemSpacing(self, index: int, spacing: float) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::setItemSpacing(int index, qreal
    spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#setItemSpacing

    Parameters
    ----------

    index : int
      Passed on as it is.

    spacing : float
      Passed on as it is.
    """
    #  void QGraphicsLinearLayout::setItemSpacing(int index, qreal spacing)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout14setItemSpacingEid',
        index, spacing,
    )

  @overload(QGraphicsLayoutItem, int)
  @overload(NoneType, int)
  def setStretchFactor(
      self,
      item: Optional[QGraphicsLayoutItem],
      stretch: int,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsLinearLayout::setStretchFactor(QGraphicsLayoutItem *item, int
    stretch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#setStretchFactor

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is.
    """
    #  void QGraphicsLinearLayout::setStretchFactor(QGraphicsLayoutItem
    #      *item, int stretch)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout16setStretchFactorEP19QGraphicsLay'
        'outItemi',
        self._addressOf(item, 'QGraphicsLayoutItem'), stretch,
    )

  @overload(QGraphicsLayoutItem, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def setAlignment(
      self,
      item: Optional[QGraphicsLayoutItem],
      alignment: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::setAlignment(QGraphicsLayoutItem
    *item, Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#setAlignment

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QGraphicsLinearLayout::setAlignment(QGraphicsLayoutItem *item,
    #      Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout12setAlignmentEP19QGraphicsLayoutI'
        'tem6QFlagsIN2Qt13AlignmentFlagEE',
        self._addressOf(item, 'QGraphicsLayoutItem'), alignment.value,
    )

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::setGeometry(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsLinearLayout::setGeometry(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout11setGeometryERK6QRectF',
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

  @overload()
  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsLayoutItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsLinearLayout::QGraphicsLinearLayout(QGraphicsLayoutItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#QGraphicsLinearLayout

    Parameters
    ----------

    parent : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsLinearLayout::QGraphicsLinearLayout(QGraphicsLayoutItem
    #      *parent)
    self._noteCreation(QGraphicsLinearLayout, lambda: Rituals.call(
        'ritual_ZN21QGraphicsLinearLayoutC1EP19QGraphicsLayoutItem',
        self._addressOf(parent, 'QGraphicsLayoutItem'),
    ))

  @overload(Qt.Orientation)
  @overload(Qt.Orientation, QGraphicsLayoutItem)
  @overload(Qt.Orientation, NoneType)
  def __init__(
      self,
      orientation: Qt.Orientation,
      parent: Optional[QGraphicsLayoutItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsLinearLayout::QGraphicsLinearLayout(Qt::Orientation
    orientation, QGraphicsLayoutItem *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#QGraphicsLinearLayout

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    parent : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsLinearLayout::QGraphicsLinearLayout(Qt::Orientation
    #      orientation, QGraphicsLayoutItem *parent)
    self._noteCreation(QGraphicsLinearLayout, lambda: Rituals.call(
        'ritual_ZN21QGraphicsLinearLayoutC1EN2Qt11OrientationEP19QGraphicsL'
        'ayoutItem',
        orientation.value, self._addressOf(parent, 'QGraphicsLayoutItem'),
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

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QGraphicsLayoutItem]) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::addItem(QGraphicsLayoutItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslinearlayout.html#addItem

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsLinearLayout::addItem(QGraphicsLayoutItem *item)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout7addItemEP19QGraphicsLayoutItem',
        self._addressOf(item, 'QGraphicsLayoutItem'),
    )

  @overload()
  @overload(int)
  def addStretch(self, stretch: int = 1) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::addStretch(int stretch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#addStretch

    Parameters
    ----------

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QGraphicsLinearLayout::addStretch(int stretch)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout10addStretchEi', stretch,
    )

  @overload(int, QGraphicsLayoutItem)
  @overload(int, NoneType)
  def insertItem(
      self,
      index: int,
      item: Optional[QGraphicsLayoutItem],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::insertItem(int index,
    QGraphicsLayoutItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsLinearLayout::insertItem(int index, QGraphicsLayoutItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout10insertItemEiP19QGraphicsLayoutIt'
        'em',
        index, self._addressOf(item, 'QGraphicsLayoutItem'),
    )

  @overload(int)
  @overload(int, int)
  def insertStretch(self, index: int, stretch: int = 1) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::insertStretch(int index, int
    stretch)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#insertStretch

    Parameters
    ----------

    index : int
      Passed on as it is.

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QGraphicsLinearLayout::insertStretch(int index, int stretch)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout13insertStretchEii', index, stretch,
    )

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QGraphicsLayoutItem]) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::removeItem(QGraphicsLayoutItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#removeItem

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsLinearLayout::removeItem(QGraphicsLayoutItem *item)
    self.uglySide.call(
        'ritual_ZN21QGraphicsLinearLayout10removeItemEP19QGraphicsLayoutIte'
        'm',
        self._addressOf(item, 'QGraphicsLayoutItem'),
    )

  @overload(int)
  def removeAt(self, index: int) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::removeAt(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#removeAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QGraphicsLinearLayout::removeAt(int index)
    self.uglySide.call('ritual_ZN21QGraphicsLinearLayout8removeAtEi', index)

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslinearlayout.html#invalidate
    """
    #  void QGraphicsLinearLayout::invalidate()
    self.uglySide.call('ritual_ZN21QGraphicsLinearLayout10invalidateEv')

  @overload()
  @overload(int)
  def dump(self, indent: int = 0) -> None:
    """
    Calls Qt's 'void QGraphicsLinearLayout::dump(int indent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslinearlayout.html#dump

    Parameters
    ----------

    indent : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QGraphicsLinearLayout::dump(int indent) const
    self.uglySide.call('ritual_ZNK21QGraphicsLinearLayout4dumpEi', indent)
