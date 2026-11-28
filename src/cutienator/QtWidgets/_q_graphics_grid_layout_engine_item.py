"""
QGraphicsGridLayoutEngineItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsgridlayoutengine_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGraphicsGridLayoutEngineItem to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QGridLayoutItem, QLayoutPolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QSizeF
  from . import QGraphicsLayoutItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsLayoutItem = WAIT['QGraphicsLayoutItem']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsGridLayoutEngineItem(QGridLayoutItem):
  """
  The cute side of Qt's QGraphicsGridLayoutEngineItem: a plain Python object
  standing in front of one C++ QGraphicsGridLayoutEngineItem.

  It is built on the cute 'QGridLayoutItem', as Qt's
  QGraphicsGridLayoutEngineItem is built on Qt's QGridLayoutItem, and has
  everything that class has.

  C++ hands a QGraphicsGridLayoutEngineItem around as a copy, so every C++
  QGraphicsGridLayoutEngineItem behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QGraphicsGridLayoutEngineItem that has a ritual and
  that Python can call so far, 7 names in all: 'sizePolicy', 'sizeHint',
  'setGeometry', 'hasDynamicConstraint', 'dynamicConstraintOrientation',
  'isEmpty', 'layoutItem'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLayoutPolicy::ControlTypes
    QGraphicsGridLayoutEngineItem::controlTypes(LayoutSide a0) const': names
    the enum 'LayoutSide', whose class cannot be named here.
  - Qt's 'QGraphicsGridLayoutEngineItem::~QGraphicsGridLayoutEngineItem()':
    the destructor: Python removes its C++ QGraphicsGridLayoutEngineItem by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QGraphicsGridLayoutEngineItem is created at the first use, not by
    'QGraphicsGridLayoutEngineItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGraphicsGridLayoutEngineItem back gives a copy the
    ritual made for Python, in a new cute QGraphicsGridLayoutEngineItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsGridLayoutEngineItem'

  #  A C++ QGraphicsGridLayoutEngineItem Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsGridLayoutEngineItem'

  #  Qt's '~QGraphicsGridLayoutEngineItem()'. Naming it makes this a value
  #  class: Python owns every C++ QGraphicsGridLayoutEngineItem behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QGraphicsGridLayoutEngineItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def sizePolicy(self, orientation: Qt.Orientation) -> QLayoutPolicy.Policy:
    """
    Calls Qt's 'QLayoutPolicy::Policy
    QGraphicsGridLayoutEngineItem::sizePolicy(Qt::Orientation orientation)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengineitem.html#sizePolicy

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    QLayoutPolicy.Policy
      The value standing for the combination Qt gave back.
    """
    #  QLayoutPolicy::Policy
    #      QGraphicsGridLayoutEngineItem::sizePolicy(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK29QGraphicsGridLayoutEngineItem10sizePolicyEN2Qt11Orient'
        'ationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QGraphicsGridLayoutEngineItem10sizePolicyEN2Qt11'
          'OrientationE')
    return QLayoutPolicy.Policy(self.uglySide.call(
        ritual, orientation.value,
    ))

  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(self, which: Qt.SizeHint, constraint: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF QGraphicsGridLayoutEngineItem::sizeHint(Qt::SizeHint
    which, const QSizeF &constraint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengineitem.html#sizeHint

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
    #  QSizeF QGraphicsGridLayoutEngineItem::sizeHint(Qt::SizeHint which,
    #      const QSizeF &constraint) const
    ritual = (
        'ritual_ZNK29QGraphicsGridLayoutEngineItem8sizeHintEN2Qt8SizeHintER'
        'K6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QGraphicsGridLayoutEngineItem8sizeHintEN2Qt8Size'
          'HintERK6QSizeF')
    address = self.uglySide.call(
        ritual, which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def hasDynamicConstraint(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsGridLayoutEngineItem::hasDynamicConstraint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengineitem.html
    """
    #  bool QGraphicsGridLayoutEngineItem::hasDynamicConstraint() const
    ritual = (
        'ritual_ZNK29QGraphicsGridLayoutEngineItem20hasDynamicConstraintEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QGraphicsGridLayoutEngineItem20hasDynamicConstra'
          'intEv')
    return self.uglySide.call(ritual)

  def dynamicConstraintOrientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation
    QGraphicsGridLayoutEngineItem::dynamicConstraintOrientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengineitem.html

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation
    #      QGraphicsGridLayoutEngineItem::dynamicConstraintOrientation()
    #      const
    ritual = (
        'ritual_ZNK29QGraphicsGridLayoutEngineItem28dynamicConstraintOrient'
        'ationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QGraphicsGridLayoutEngineItem28dynamicConstraint'
          'OrientationEv')
    return Qt.Orientation(self.uglySide.call(ritual))

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsGridLayoutEngineItem::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengineitem.html#isEmpty
    """
    #  bool QGraphicsGridLayoutEngineItem::isEmpty() const
    ritual = 'ritual_ZNK29QGraphicsGridLayoutEngineItem7isEmptyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QGraphicsGridLayoutEngineItem7isEmptyEv'
    return self.uglySide.call(ritual)

  def layoutItem(self) -> Optional[QGraphicsLayoutItem]:
    """
    Calls Qt's 'QGraphicsLayoutItem
    *QGraphicsGridLayoutEngineItem::layoutItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengineitem.html#layoutItem

    Returns
    -------

    Optional[QGraphicsLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayoutItem *QGraphicsGridLayoutEngineItem::layoutItem() const
    address = self.uglySide.call(
        'ritual_ZNK29QGraphicsGridLayoutEngineItem10layoutItemEv',
    )
    from . import QGraphicsLayoutItem
    return QGraphicsLayoutItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QGraphicsGridLayoutEngineItem::setGeometry(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengineitem.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGraphicsGridLayoutEngineItem::setGeometry(const QRectF &rect)
    ritual = (
        'ritual_ZN29QGraphicsGridLayoutEngineItem11setGeometryERK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QGraphicsGridLayoutEngineItem11setGeometryERK6QRe'
          'ctF')
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

  @overload(QGraphicsLayoutItem, int, int)
  @overload(NoneType, int, int)
  @overload(QGraphicsLayoutItem, int, int, int)
  @overload(NoneType, int, int, int)
  @overload(QGraphicsLayoutItem, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  @overload(QGraphicsLayoutItem, int, int, int, int, Qt.Alignment)
  @overload(NoneType, int, int, int, int, Qt.Alignment)
  def __init__(
      self,
      item: Optional[QGraphicsLayoutItem],
      row: int,
      columns: int,
      rowSpan: int = 1,
      columnSpan: int = 1,
      alignment: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsGridLayoutEngineItem::QGraphicsGridLayoutEngineItem(
    QGraphicsLayoutItem *item, int row, int columns, int rowSpan, int
    columnSpan, Qt::Alignment alignment)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengineitem.html

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    row : int
      Passed on as it is.

    columns : int
      Passed on as it is.

    rowSpan : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    columnSpan : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    alignment : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  QGraphicsGridLayoutEngineItem::QGraphicsGridLayoutEngineItem(
    #      QGraphicsLayoutItem *item, int row, int columns, int rowSpan, int
    #      columnSpan, Qt::Alignment alignment)
    self._noteCreation(QGraphicsGridLayoutEngineItem, lambda: Rituals.call(
        'ritual_ZN29QGraphicsGridLayoutEngineItemC1EP19QGraphicsLayoutItemi'
        'iii6QFlagsIN2Qt13AlignmentFlagEE',
        self._addressOf(item, 'QGraphicsLayoutItem'), row, columns, rowSpan,
        columnSpan, alignment.value,
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
