"""
QListViewItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QListViewItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPoint, QRect, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']


class QListViewItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QListViewItem: a plain Python object standing in
  front of one C++ QListViewItem.

  C++ hands a QListViewItem around as a copy, so every C++ QListViewItem
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QListViewItem that has a ritual and that Python can
  call so far, 9 names in all: '__eq__', '__ne__', 'isValid', 'invalidate',
  'resize', 'move', 'width', 'height', 'rect'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QListViewItem::~QListViewItem()': the destructor: Python removes
    its C++ QListViewItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QListViewItem is created at the first use, not by
    'QListViewItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QListViewItem back gives a copy the ritual made for
    Python, in a new cute QListViewItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QListViewItem'

  #  Qt's '~QListViewItem()'. Naming it makes this a value class: Python owns
  #  every C++ QListViewItem behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QListViewItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QListViewItem::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#isValid
    """
    #  bool QListViewItem::isValid() const
    return self.uglySide.call('ritual_ZNK13QListViewItem7isValidEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QListViewItem::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#width
    """
    #  int QListViewItem::width() const
    return self.uglySide.call('ritual_ZNK13QListViewItem5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QListViewItem::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#height
    """
    #  int QListViewItem::height() const
    return self.uglySide.call('ritual_ZNK13QListViewItem6heightEv')

  def rect(self) -> QRect:
    """
    Calls Qt's 'QRect QListViewItem::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#rect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QListViewItem::rect() const
    address = self.uglySide.call('ritual_ZNK13QListViewItem4rectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QListViewItem) -> bool:
    """
    Calls Qt's 'bool QListViewItem::operator==(const QListViewItem &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#operator==

    Parameters
    ----------

    other : QListViewItem
      Passed on as a value: Qt reads the C++ QListViewItem, which stays
      Python's own.
    """
    #  bool QListViewItem::operator==(const QListViewItem &other) const
    return self.uglySide.call(
        'ritual_ZNK13QListViewItemeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QListViewItem) -> bool:
    """
    Calls Qt's 'bool QListViewItem::operator!=(const QListViewItem &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#operator!=

    Parameters
    ----------

    other : QListViewItem
      Passed on as a value: Qt reads the C++ QListViewItem, which stays
      Python's own.
    """
    #  bool QListViewItem::operator!=(const QListViewItem &other) const
    return self.uglySide.call(
        'ritual_ZNK13QListViewItemneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QListViewItem::QListViewItem()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#QListViewItem
    """
    #  QListViewItem::QListViewItem()
    self._noteCreation(QListViewItem, lambda: Rituals.call(
        'ritual_ZN13QListViewItemC1Ev',
    ))

  @overload(QRect, int)
  def __init__(self, r: QRect, i: int) -> None:
    """
    Notes what was given, for Qt's 'QListViewItem::QListViewItem(QRect r, int
    i)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#QListViewItem

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    i : int
      Passed on as it is.
    """
    #  QListViewItem::QListViewItem(QRect r, int i)
    self._noteCreation(QListViewItem, lambda: Rituals.call(
        'ritual_ZN13QListViewItemC1E5QRecti', self._valueOf(r), i,
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
    Calls Qt's 'void QListViewItem::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#invalidate
    """
    #  void QListViewItem::invalidate()
    self.uglySide.call('ritual_ZN13QListViewItem10invalidateEv')

  @overload(QSize)
  def resize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QListViewItem::resize(QSize size)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#resize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QListViewItem::resize(QSize size)
    self.uglySide.call(
        'ritual_ZN13QListViewItem6resizeE5QSize', self._valueOf(size),
    )

  @overload(QPoint)
  def move(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QListViewItem::move(QPoint position)'.

    Qt's own words: https://doc.qt.io/qt-6/qlistviewitem.html#move

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QListViewItem::move(QPoint position)
    self.uglySide.call(
        'ritual_ZN13QListViewItem4moveE6QPoint', self._valueOf(position),
    )
