"""
FxTableItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means FxTableItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickItemViewFxItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickItem, QQuickTableView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QQuickTableView = WAIT['QQuickTableView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FxTableItem(QQuickItemViewFxItem):
  """
  The cute side of Qt's FxTableItem: a plain Python object standing in front
  of one C++ FxTableItem.

  It is built on the cute 'QQuickItemViewFxItem', as Qt's FxTableItem is
  built on Qt's QQuickItemViewFxItem, and has everything that class has.

  C++ hands a FxTableItem around as a copy, so every C++ FxTableItem behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's FxTableItem that has a ritual and that Python can
  call so far, 5 names in all: 'position', 'endPosition', 'size',
  'sectionSize', 'contains'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'FxTableItem::~FxTableItem()': the destructor: Python removes its
    C++ FxTableItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ FxTableItem is created at the first use, not by
    'FxTableItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a FxTableItem back gives a copy the ritual made for
    Python, in a new cute FxTableItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'FxTableItem'

  #  A C++ FxTableItem Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_FxTableItem'

  #  Qt's '~FxTableItem()'. Naming it makes this a value class: Python owns
  #  every C++ FxTableItem behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11FxTableItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def position(self) -> float:
    """
    Calls Qt's 'qreal FxTableItem::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/fxtableitem.html#position
    """
    #  qreal FxTableItem::position() const
    ritual = 'ritual_ZNK11FxTableItem8positionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11FxTableItem8positionEv'
    return self.uglySide.call(ritual)

  def endPosition(self) -> float:
    """
    Calls Qt's 'qreal FxTableItem::endPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/fxtableitem.html#endPosition
    """
    #  qreal FxTableItem::endPosition() const
    ritual = 'ritual_ZNK11FxTableItem11endPositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11FxTableItem11endPositionEv'
    return self.uglySide.call(ritual)

  def size(self) -> float:
    """
    Calls Qt's 'qreal FxTableItem::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/fxtableitem.html#size
    """
    #  qreal FxTableItem::size() const
    ritual = 'ritual_ZNK11FxTableItem4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11FxTableItem4sizeEv'
    return self.uglySide.call(ritual)

  def sectionSize(self) -> float:
    """
    Calls Qt's 'qreal FxTableItem::sectionSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/fxtableitem.html#sectionSize
    """
    #  qreal FxTableItem::sectionSize() const
    ritual = 'ritual_ZNK11FxTableItem11sectionSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11FxTableItem11sectionSizeEv'
    return self.uglySide.call(ritual)

  @overload(float, float)
  def contains(self, a0: float, a1: float) -> bool:
    """
    Calls Qt's 'bool FxTableItem::contains(qreal a0, qreal a1) const'.

    Qt's own words: https://doc.qt.io/qt-6/fxtableitem.html#contains

    Parameters
    ----------

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.
    """
    #  bool FxTableItem::contains(qreal a0, qreal a1) const
    ritual = 'ritual_ZNK11FxTableItem8containsEdd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11FxTableItem8containsEdd'
    return self.uglySide.call(ritual, a0, a1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem, QQuickTableView, bool)
  @overload(QQuickItem, NoneType, bool)
  @overload(NoneType, QQuickTableView, bool)
  @overload(NoneType, NoneType, bool)
  def __init__(
      self,
      item: Optional[QQuickItem],
      table: Optional[QQuickTableView],
      own: bool,
  ) -> None:
    """
    Notes what was given, for Qt's 'FxTableItem::FxTableItem(QQuickItem
    *item, QQuickTableView *table, bool own)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/fxtableitem.html#FxTableItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    table : Optional[QQuickTableView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    own : bool
      Passed on as it is.
    """
    #  FxTableItem::FxTableItem(QQuickItem *item, QQuickTableView *table,
    #      bool own)
    self._noteCreation(FxTableItem, lambda: Rituals.call(
        'ritual_ZN11FxTableItemC1EP10QQuickItemP15QQuickTableViewb',
        self._addressOf(item), self._addressOf(table), own,
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
