"""
QLayoutItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import Qt
from . import QSizePolicyControlType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
  from . import QLayout, QSizePolicy, QSpacerItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']


class QLayoutItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLayoutItem: a plain Python object standing in front
  of one C++ QLayoutItem.

  What exists
  -----------

  Every function of Qt's QLayoutItem that has a ritual and that Python can
  call so far, 17 names in all: 'sizeHint', 'minimumSize', 'maximumSize',
  'expandingDirections', 'setGeometry', 'geometry', 'isEmpty',
  'hasHeightForWidth', 'heightForWidth', 'minimumHeightForWidth',
  'invalidate', 'widget', 'layout', 'spacerItem', 'alignment',
  'setAlignment', 'controlTypes'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLayoutItem::~QLayoutItem()': the destructor: Python never removes
    a C++ QLayoutItem.

  What has no ritual
  ------------------

  1 of the 19 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one.

  What to expect
  --------------

  - The C++ QLayoutItem is created at the first use, not by
    'QLayoutItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLayoutItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLayoutItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QLayoutItem::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLayoutItem::sizeHint() const
    address = self.uglySide.call('ritual_ZNK11QLayoutItem8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QLayoutItem::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLayoutItem::minimumSize() const
    address = self.uglySide.call('ritual_ZNK11QLayoutItem11minimumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QLayoutItem::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLayoutItem::maximumSize() const
    address = self.uglySide.call('ritual_ZNK11QLayoutItem11maximumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def expandingDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QLayoutItem::expandingDirections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutitem.html#expandingDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QLayoutItem::expandingDirections() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK11QLayoutItem19expandingDirectionsEv',
    ))

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QLayoutItem::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QLayoutItem::geometry() const
    address = self.uglySide.call('ritual_ZNK11QLayoutItem8geometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QLayoutItem::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#isEmpty
    """
    #  bool QLayoutItem::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QLayoutItem7isEmptyEv')

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QLayoutItem::hasHeightForWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#hasHeightForWidth
    """
    #  bool QLayoutItem::hasHeightForWidth() const
    return self.uglySide.call('ritual_ZNK11QLayoutItem17hasHeightForWidthEv')

  @overload(int)
  def heightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QLayoutItem::heightForWidth(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#heightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QLayoutItem::heightForWidth(int a0) const
    return self.uglySide.call(
        'ritual_ZNK11QLayoutItem14heightForWidthEi', a0,
    )

  @overload(int)
  def minimumHeightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QLayoutItem::minimumHeightForWidth(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutitem.html#minimumHeightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QLayoutItem::minimumHeightForWidth(int a0) const
    return self.uglySide.call(
        'ritual_ZNK11QLayoutItem21minimumHeightForWidthEi', a0,
    )

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QLayoutItem::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QLayoutItem::widget() const
    address = self.uglySide.call('ritual_ZNK11QLayoutItem6widgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QLayoutItem::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QLayoutItem::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK11QLayoutItem9alignmentEv',
    ))

  def controlTypes(self) -> QSizePolicy.ControlTypes:
    """
    Calls Qt's 'QSizePolicy::ControlTypes QLayoutItem::controlTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#controlTypes

    Returns
    -------

    QSizePolicy.ControlTypes
      The value standing for the combination Qt gave back.
    """
    #  QSizePolicy::ControlTypes QLayoutItem::controlTypes() const
    return QSizePolicyControlType(self.uglySide.call(
        'ritual_ZNK11QLayoutItem12controlTypesEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setGeometry(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QLayoutItem::setGeometry(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#setGeometry

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QLayoutItem::setGeometry(const QRect &a0)
    self.uglySide.call(
        'ritual_ZN11QLayoutItem11setGeometryERK5QRect', self._valueOf(a0),
    )

  @overload(Qt.Alignment)
  def setAlignment(self, a: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QLayoutItem::setAlignment(Qt::Alignment a)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#setAlignment

    Parameters
    ----------

    a : Qt.Alignment
      Passed on as its number.
    """
    #  void QLayoutItem::setAlignment(Qt::Alignment a)
    self.uglySide.call(
        'ritual_ZN11QLayoutItem12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE',
        a.value,
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
    Calls Qt's 'void QLayoutItem::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#invalidate
    """
    #  void QLayoutItem::invalidate()
    self.uglySide.call('ritual_ZN11QLayoutItem10invalidateEv')

  def layout(self) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *QLayoutItem::layout()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#layout

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *QLayoutItem::layout()
    address = self.uglySide.call('ritual_ZN11QLayoutItem6layoutEv')
    from . import QLayout
    return QLayout._cuteAt(address)

  def spacerItem(self) -> Optional[QSpacerItem]:
    """
    Calls Qt's 'QSpacerItem *QLayoutItem::spacerItem()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutitem.html#spacerItem

    Returns
    -------

    Optional[QSpacerItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSpacerItem *QLayoutItem::spacerItem()
    address = self.uglySide.call('ritual_ZN11QLayoutItem10spacerItemEv')
    from . import QSpacerItem
    return QSpacerItem._cuteAt(address)
