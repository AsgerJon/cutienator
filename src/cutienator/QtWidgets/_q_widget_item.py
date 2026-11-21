"""
QWidgetItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QLayoutItem, QSizePolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect, QSize
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


class QWidgetItem(QLayoutItem):
  """
  The cute side of Qt's QWidgetItem: a plain Python object standing in front
  of one C++ QWidgetItem.

  It is built on the cute 'QLayoutItem', as Qt's QWidgetItem is built on Qt's
  QLayoutItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetItem that has a ritual and that Python can
  call so far, 12 names in all: 'sizeHint', 'minimumSize', 'maximumSize',
  'expandingDirections', 'isEmpty', 'setGeometry', 'geometry', 'widget',
  'hasHeightForWidth', 'heightForWidth', 'minimumHeightForWidth',
  'controlTypes'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidgetItem::~QWidgetItem()': the destructor: Python never removes
    a C++ QWidgetItem.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QWidgetItem is created at the first use, not by
    'QWidgetItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QWidgetItem::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidgetItem::sizeHint() const
    address = self.uglySide.call('ritual_ZNK11QWidgetItem8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWidgetItem::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidgetItem::minimumSize() const
    address = self.uglySide.call('ritual_ZNK11QWidgetItem11minimumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWidgetItem::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidgetItem::maximumSize() const
    address = self.uglySide.call('ritual_ZNK11QWidgetItem11maximumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def expandingDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QWidgetItem::expandingDirections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetitem.html#expandingDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QWidgetItem::expandingDirections() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK11QWidgetItem19expandingDirectionsEv',
    ))

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QWidgetItem::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#isEmpty
    """
    #  bool QWidgetItem::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QWidgetItem7isEmptyEv')

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWidgetItem::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetItem::geometry() const
    address = self.uglySide.call('ritual_ZNK11QWidgetItem8geometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetItem::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetItem::widget() const
    address = self.uglySide.call('ritual_ZNK11QWidgetItem6widgetEv')
    from . import QWidget
    return QWidget._cuteAt(address)

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QWidgetItem::hasHeightForWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#hasHeightForWidth
    """
    #  bool QWidgetItem::hasHeightForWidth() const
    return self.uglySide.call('ritual_ZNK11QWidgetItem17hasHeightForWidthEv')

  @overload(int)
  def heightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QWidgetItem::heightForWidth(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#heightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QWidgetItem::heightForWidth(int a0) const
    return self.uglySide.call(
        'ritual_ZNK11QWidgetItem14heightForWidthEi', a0,
    )

  @overload(int)
  def minimumHeightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QWidgetItem::minimumHeightForWidth(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetitem.html#minimumHeightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QWidgetItem::minimumHeightForWidth(int a0) const
    return self.uglySide.call(
        'ritual_ZNK11QWidgetItem21minimumHeightForWidthEi', a0,
    )

  def controlTypes(self) -> QSizePolicy.ControlTypes:
    """
    Calls Qt's 'QSizePolicy::ControlTypes QWidgetItem::controlTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#controlTypes

    Returns
    -------

    QSizePolicy.ControlTypes
      The value standing for the combination Qt gave back.
    """
    #  QSizePolicy::ControlTypes QWidgetItem::controlTypes() const
    return QSizePolicy.ControlTypes(self.uglySide.call(
        'ritual_ZNK11QWidgetItem12controlTypesEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setGeometry(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QWidgetItem::setGeometry(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#setGeometry

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QWidgetItem::setGeometry(const QRect &a0)
    self.uglySide.call(
        'ritual_ZN11QWidgetItem11setGeometryERK5QRect', self._valueOf(a0),
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

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, w: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's 'QWidgetItem::QWidgetItem(QWidget *w)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitem.html#QWidgetItem

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWidgetItem::QWidgetItem(QWidget *w)
    self._noteCreation(QWidgetItem, lambda: Rituals.call(
        'ritual_ZN11QWidgetItemC1EP7QWidget', self._addressOf(w),
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
