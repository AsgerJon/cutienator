"""
QGraphicsLayoutPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicslayout_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsLayoutPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGraphicsLayoutItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGraphicsItem, QGraphicsLayout, QGraphicsLayoutItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsItem = WAIT['QGraphicsItem']
  QGraphicsLayoutItem = WAIT['QGraphicsLayoutItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsLayoutPrivate(QGraphicsLayoutItemPrivate):
  """
  The cute side of Qt's QGraphicsLayoutPrivate: a plain Python object
  standing in front of one C++ QGraphicsLayoutPrivate.

  It is built on the cute 'QGraphicsLayoutItemPrivate', as Qt's
  QGraphicsLayoutPrivate is built on Qt's QGraphicsLayoutItemPrivate, and has
  everything that class has.

  C++ hands a QGraphicsLayoutPrivate around as a copy, so every C++
  QGraphicsLayoutPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGraphicsLayoutPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func', 'reparentChildItems',
  'visualDirection', 'addChildLayoutItem', 'activateRecursive'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsLayout *QGraphicsLayoutPrivate::q_func() const':
    takes in Python what 'QGraphicsLayout *QGraphicsLayoutPrivate::q_func()'
    takes.
  - Qt's 'void QGraphicsLayoutPrivate::getMargin(qreal *result, qreal
    userMargin, QStyle::PixelMetric pm) const': takes a number to change
    where it is.
  - Qt's 'QGraphicsLayoutPrivate::~QGraphicsLayoutPrivate()': the destructor:
    Python removes its C++ QGraphicsLayoutPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QGraphicsLayoutPrivate is created at the first use, not by
    'QGraphicsLayoutPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGraphicsLayoutPrivate back gives a copy the ritual
    made for Python, in a new cute QGraphicsLayoutPrivate.
  - Each name of Qt's QGraphicsLayoutPrivate that has no cute function yet,
    'getMargin', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsLayoutPrivate'

  #  Qt's '~QGraphicsLayoutPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QGraphicsLayoutPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QGraphicsLayoutPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def visualDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QGraphicsLayoutPrivate::visualDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutprivate.html#visualDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QGraphicsLayoutPrivate::visualDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK22QGraphicsLayoutPrivate15visualDirectionEv',
    ))

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsLayoutPrivate::QGraphicsLayoutPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutprivate.html#QGraphicsLayoutPrivate
    """
    #  QGraphicsLayoutPrivate::QGraphicsLayoutPrivate()
    self._noteCreation(QGraphicsLayoutPrivate, lambda: Rituals.call(
        'ritual_ZN22QGraphicsLayoutPrivateC1Ev',
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

  def q_func(self) -> Optional[QGraphicsLayout]:
    """
    Calls Qt's 'QGraphicsLayout *QGraphicsLayoutPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicslayoutprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsLayout *QGraphicsLayoutPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QGraphicsLayoutPrivate6q_funcEv',
    )
    from . import QGraphicsLayout
    return QGraphicsLayout._cuteAt(address)

  @overload(QGraphicsItem)
  @overload(NoneType)
  def reparentChildItems(self, newParent: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutPrivate::reparentChildItems(QGraphicsItem
    *newParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutprivate.html#reparentChildItems

    Parameters
    ----------

    newParent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsLayoutPrivate::reparentChildItems(QGraphicsItem
    #      *newParent)
    self.uglySide.call(
        'ritual_ZN22QGraphicsLayoutPrivate18reparentChildItemsEP13QGraphics'
        'Item',
        self._addressOf(newParent, 'QGraphicsItem'),
    )

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def addChildLayoutItem(self, item: Optional[QGraphicsLayoutItem]) -> None:
    """
    Calls Qt's 'void
    QGraphicsLayoutPrivate::addChildLayoutItem(QGraphicsLayoutItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutprivate.html#addChildLayoutItem

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsLayoutPrivate::addChildLayoutItem(QGraphicsLayoutItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN22QGraphicsLayoutPrivate18addChildLayoutItemEP19QGraphics'
        'LayoutItem',
        self._addressOf(item, 'QGraphicsLayoutItem'),
    )

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def activateRecursive(self, item: Optional[QGraphicsLayoutItem]) -> None:
    """
    Calls Qt's 'void
    QGraphicsLayoutPrivate::activateRecursive(QGraphicsLayoutItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutprivate.html#activateRecursive

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsLayoutPrivate::activateRecursive(QGraphicsLayoutItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN22QGraphicsLayoutPrivate17activateRecursiveEP19QGraphicsL'
        'ayoutItem',
        self._addressOf(item, 'QGraphicsLayoutItem'),
    )

  @staticmethod
  def getMargin(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsLayoutPrivate::getMargin(qreal *result, qreal
    userMargin, QStyle::PixelMetric pm) const': takes a number to change
    where it is.
    """
    raise NotImplementedError(
        "'QGraphicsLayoutPrivate.getMargin' has no cute function yet. Qt's "
        "'void QGraphicsLayoutPrivate::getMargin(qreal *result, qreal "
        "userMargin, QStyle::PixelMetric pm) const': takes a number to "
        "change where it is.")
