"""
QQuickGridLayoutItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickgridlayoutengine_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickGridLayoutItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QLayoutPolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QSizeF
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGridLayoutItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickGridLayoutItem: a plain Python object standing
  in front of one C++ QQuickGridLayoutItem.

  C++ hands a QQuickGridLayoutItem around as a copy, so every C++
  QQuickGridLayoutItem behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickGridLayoutItem that has a ritual and that
  Python can call so far, 8 names in all: 'sizeHint', 'effectiveSizeHints',
  'setCachedSizeHints', 'invalidate', 'sizePolicy', 'setGeometry',
  'toString', 'layoutItem'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickGridLayoutItem::~QQuickGridLayoutItem()': the destructor:
    Python removes its C++ QQuickGridLayoutItem by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickGridLayoutItem is created at the first use, not by
    'QQuickGridLayoutItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickGridLayoutItem back gives a copy the ritual
    made for Python, in a new cute QQuickGridLayoutItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGridLayoutItem'

  #  Qt's '~QQuickGridLayoutItem()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickGridLayoutItem behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQuickGridLayoutItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(self, which: Qt.SizeHint, constraint: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickGridLayoutItem::sizeHint(Qt::SizeHint which,
    const QSizeF &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayoutitem.html#sizeHint

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
    #  QSizeF QQuickGridLayoutItem::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    ritual = (
        'ritual_ZNK20QQuickGridLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QQuickGridLayoutItem8sizeHintEN2Qt8SizeHintERK6Q'
          'SizeF')
    address = self.uglySide.call(
        ritual, which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def effectiveSizeHints(self) -> Optional[QSizeF]:
    """
    Calls Qt's 'QSizeF *QQuickGridLayoutItem::effectiveSizeHints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutitem.html#effectiveSizeHints

    Returns
    -------

    Optional[QSizeF]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSizeF *QQuickGridLayoutItem::effectiveSizeHints() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGridLayoutItem18effectiveSizeHintsEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteAt(address)

  @overload(Qt.Orientation)
  def sizePolicy(self, orientation: Qt.Orientation) -> QLayoutPolicy.Policy:
    """
    Calls Qt's 'QLayoutPolicy::Policy
    QQuickGridLayoutItem::sizePolicy(Qt::Orientation orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutitem.html#sizePolicy

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    Returns
    -------

    QLayoutPolicy.Policy
      The value standing for the combination Qt gave back.
    """
    #  QLayoutPolicy::Policy QQuickGridLayoutItem::sizePolicy(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK20QQuickGridLayoutItem10sizePolicyEN2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QQuickGridLayoutItem10sizePolicyEN2Qt11Orientati'
          'onE')
    return QLayoutPolicy.Policy(self.uglySide.call(
        ritual, orientation.value,
    ))

  def toString(self) -> str:
    """
    Calls Qt's 'QString QQuickGridLayoutItem::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridlayoutitem.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickGridLayoutItem::toString() const
    ritual = 'ritual_ZNK20QQuickGridLayoutItem8toStringEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickGridLayoutItem8toStringEv'
    return self.uglySide.call(ritual)

  def layoutItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickGridLayoutItem::layoutItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutitem.html#layoutItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickGridLayoutItem::layoutItem() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickGridLayoutItem10layoutItemEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSizeF)
  @overload(NoneType)
  def setCachedSizeHints(self, sizeHints: Optional[QSizeF]) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutItem::setCachedSizeHints(QSizeF
    *sizeHints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutitem.html#setCachedSizeHints

    Parameters
    ----------

    sizeHints : Optional[QSizeF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGridLayoutItem::setCachedSizeHints(QSizeF *sizeHints)
    self.uglySide.call(
        'ritual_ZN20QQuickGridLayoutItem18setCachedSizeHintsEP6QSizeF',
        self._addressOf(sizeHints),
    )

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutItem::setGeometry(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutitem.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickGridLayoutItem::setGeometry(const QRectF &rect)
    ritual = 'ritual_ZN20QQuickGridLayoutItem11setGeometryERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickGridLayoutItem11setGeometryERK6QRectF'
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

  @overload(QQuickItem, int, int)
  @overload(NoneType, int, int)
  @overload(QQuickItem, int, int, int)
  @overload(NoneType, int, int, int)
  @overload(QQuickItem, int, int, int, int)
  @overload(NoneType, int, int, int, int)
  @overload(QQuickItem, int, int, int, int, Qt.Alignment)
  @overload(NoneType, int, int, int, int, Qt.Alignment)
  def __init__(
      self,
      item: Optional[QQuickItem],
      row: int,
      column: int,
      rowSpan: int = 1,
      columnSpan: int = 1,
      alignment: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickGridLayoutItem::QQuickGridLayoutItem(QQuickItem *item, int row,
    int column, int rowSpan, int columnSpan, Qt::Alignment alignment)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutitem.html#QQuickGridLayoutItem

    Parameters
    ----------

    item : Optional[QQuickItem]
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

    alignment : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  QQuickGridLayoutItem::QQuickGridLayoutItem(QQuickItem *item, int row,
    #      int column, int rowSpan, int columnSpan, Qt::Alignment alignment)
    self._noteCreation(QQuickGridLayoutItem, lambda: Rituals.call(
        'ritual_ZN20QQuickGridLayoutItemC1EP10QQuickItemiiii6QFlagsIN2Qt13A'
        'lignmentFlagEE',
        self._addressOf(item), row, column, rowSpan, columnSpan,
        alignment.value,
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
    Calls Qt's 'void QQuickGridLayoutItem::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutitem.html#invalidate
    """
    #  void QQuickGridLayoutItem::invalidate()
    self.uglySide.call('ritual_ZN20QQuickGridLayoutItem10invalidateEv')
