"""
QAccessibleQuickFlickable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qaccessiblequickflickable_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAccessibleQuickFlickable to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleViewportInterface
from . import QAccessibleQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QSizeF
  from . import QQuickFlickable
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickFlickable = WAIT['QQuickFlickable']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickFlickable(QAccessibleQuickItem, QAccessibleViewportInterface):
  """
  The cute side of Qt's QAccessibleQuickFlickable: a plain Python object
  standing in front of one C++ QAccessibleQuickFlickable.

  It is built on the cute 'QAccessibleQuickItem', as Qt's
  QAccessibleQuickFlickable is built on Qt's QAccessibleQuickItem, and has
  everything that class has. It is built on the cute
  'QAccessibleViewportInterface' as well, as Qt's QAccessibleQuickFlickable
  is built on Qt's QAccessibleViewportInterface too, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickFlickable that has a ritual and that
  Python can call so far, 6 names in all: 'contentSize', 'position',
  'viewportSize', 'isIndexed', 'setPosition', 'flickable'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QAccessibleQuickFlickable::interface_cast(QAccessible::InterfaceType
    t)': gives 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QAccessibleQuickFlickable is created at the first use, not by
    'QAccessibleQuickFlickable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickFlickable.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickFlickable'

  #  Qt's QAccessibleQuickFlickable is built on more than one class. The part
  #  of a C++ QAccessibleQuickFlickable that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleViewportInterface':
          'ritual_cast_QAccessibleQuickFlickable_QAccessibleViewportInterface',
  }

  #  A C++ QAccessibleQuickFlickable Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAccessibleQuickFlickable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def contentSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QAccessibleQuickFlickable::contentSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickflickable.html#contentSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QAccessibleQuickFlickable::contentSize() const
    ritual = 'ritual_ZNK25QAccessibleQuickFlickable11contentSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleQuickFlickable11contentSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def position(self) -> QPointF:
    """
    Calls Qt's 'QPointF QAccessibleQuickFlickable::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickflickable.html#position

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QAccessibleQuickFlickable::position() const
    ritual = 'ritual_ZNK25QAccessibleQuickFlickable8positionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleQuickFlickable8positionEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def viewportSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QAccessibleQuickFlickable::viewportSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickflickable.html#viewportSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QAccessibleQuickFlickable::viewportSize() const
    ritual = 'ritual_ZNK25QAccessibleQuickFlickable12viewportSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleQuickFlickable12viewportSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def isIndexed(self) -> bool:
    """
    Calls Qt's 'bool QAccessibleQuickFlickable::isIndexed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickflickable.html#isIndexed
    """
    #  bool QAccessibleQuickFlickable::isIndexed() const
    ritual = 'ritual_ZNK25QAccessibleQuickFlickable9isIndexedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QAccessibleQuickFlickable9isIndexedEv'
    return self.uglySide.call(ritual)

  def flickable(self) -> Optional[QQuickFlickable]:
    """
    Calls Qt's 'QQuickFlickable *QAccessibleQuickFlickable::flickable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickflickable.html#flickable

    Returns
    -------

    Optional[QQuickFlickable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFlickable *QAccessibleQuickFlickable::flickable() const
    address = self.uglySide.call(
        'ritual_ZNK25QAccessibleQuickFlickable9flickableEv',
    )
    from . import QQuickFlickable
    return QQuickFlickable._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setPosition(self, position: QPointF) -> None:
    """
    Calls Qt's 'void QAccessibleQuickFlickable::setPosition(QPointF
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickflickable.html#setPosition

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QAccessibleQuickFlickable::setPosition(QPointF position)
    ritual = 'ritual_ZN25QAccessibleQuickFlickable11setPositionE7QPointF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QAccessibleQuickFlickable11setPositionE7QPointF')
    self.uglySide.call(ritual, self._valueOf(position, 'QPointF'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickFlickable)
  @overload(NoneType)
  def __init__(self, flickable: Optional[QQuickFlickable]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleQuickFlickable::QAccessibleQuickFlickable(QQuickFlickable
    *flickable)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickflickable.html

    Parameters
    ----------

    flickable : Optional[QQuickFlickable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleQuickFlickable::QAccessibleQuickFlickable(QQuickFlickable
    #      *flickable)
    self._noteCreation(QAccessibleQuickFlickable, lambda: Rituals.call(
        'ritual_ZN25QAccessibleQuickFlickableC1EP15QQuickFlickable',
        self._addressOf(flickable),
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
