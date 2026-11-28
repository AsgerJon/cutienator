"""
QtGraphicsAnchorLayout::AnchorVertex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtGraphicsAnchorLayout::AnchorVertex to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGraphicsLayoutItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsLayoutItem = WAIT['QGraphicsLayoutItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AnchorVertex(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtGraphicsAnchorLayout::AnchorVertex: a plain Python
  object standing in front of one C++ QtGraphicsAnchorLayout::AnchorVertex.

  C++ hands a QtGraphicsAnchorLayout::AnchorVertex around as a copy, so every
  C++ QtGraphicsAnchorLayout::AnchorVertex behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QtGraphicsAnchorLayout::AnchorVertex that has a
  ritual and that Python can call so far, 1 name in all: 'toString'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtGraphicsAnchorLayout::AnchorVertex::~AnchorVertex()': the
    destructor: Python removes its C++ QtGraphicsAnchorLayout::AnchorVertex
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtGraphicsAnchorLayout::AnchorVertex is created at the first use,
    not by 'QtGraphicsAnchorLayout::AnchorVertex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtGraphicsAnchorLayout::AnchorVertex back gives a
    copy the ritual made for Python, in a new cute
    QtGraphicsAnchorLayout::AnchorVertex.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtGraphicsAnchorLayout::AnchorVertex'

  #  A C++ QtGraphicsAnchorLayout::AnchorVertex Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtGraphicsAnchorLayout_AnchorVertex'

  #  The functions Qt calls itself that QtGraphicsAnchorLayout::AnchorVertex
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'toString': (
          ('_ZNK22QtGraphicsAnchorLayout12AnchorVertex8toStringEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Qt's '~QtGraphicsAnchorLayout::AnchorVertex()'. Naming it makes this a
  #  value class: Python owns every C++ QtGraphicsAnchorLayout::AnchorVertex
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QtGraphicsAnchorLayout12AnchorVertexD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QtGraphicsAnchorLayout::AnchorVertex::toString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgraphicsanchorlayout-anchorvertex.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtGraphicsAnchorLayout::AnchorVertex::toString() const
    ritual = 'ritual_ZNK22QtGraphicsAnchorLayout12AnchorVertex8toStringEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QtGraphicsAnchorLayout12AnchorVertex8toStringEv')
    return self.uglySide.call(ritual)

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

  @overload(QGraphicsLayoutItem, Qt.AnchorPoint)
  @overload(NoneType, Qt.AnchorPoint)
  def __init__(
      self,
      item: Optional[QGraphicsLayoutItem],
      edge: Qt.AnchorPoint,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtGraphicsAnchorLayout::AnchorVertex::AnchorVertex(QGraphicsLayoutItem
    *item, Qt::AnchorPoint edge)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgraphicsanchorlayout-anchorvertex.html

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    edge : Qt.AnchorPoint
      Passed on as its number.
    """
    #  QtGraphicsAnchorLayout::AnchorVertex::AnchorVertex(QGraphicsLayoutItem
    #      *item, Qt::AnchorPoint edge)
    self._noteCreation(AnchorVertex, lambda: Rituals.call(
        'ritual_ZN22QtGraphicsAnchorLayout12AnchorVertexC1EP19QGraphicsLayo'
        'utItemN2Qt11AnchorPointE',
        self._addressOf(item, 'QGraphicsLayoutItem'), edge.value,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QtGraphicsAnchorLayout::AnchorVertex::AnchorVertex()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgraphicsanchorlayout-anchorvertex.html
    """
    #  QtGraphicsAnchorLayout::AnchorVertex::AnchorVertex()
    self._noteCreation(AnchorVertex, lambda: Rituals.call(
        'ritual_ZN22QtGraphicsAnchorLayout12AnchorVertexC1Ev',
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
