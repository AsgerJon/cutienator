"""
QtGraphicsAnchorLayout::AnchorVertexPair binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsanchorlayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtGraphicsAnchorLayout::AnchorVertexPair to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QtGraphicsAnchorLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AnchorVertexPair(QtGraphicsAnchorLayout.AnchorVertex):
  """
  The cute side of Qt's QtGraphicsAnchorLayout::AnchorVertexPair: a plain
  Python object standing in front of one C++
  QtGraphicsAnchorLayout::AnchorVertexPair.

  It is built on the cute 'QtGraphicsAnchorLayout::AnchorVertex', as Qt's
  QtGraphicsAnchorLayout::AnchorVertexPair is built on Qt's
  QtGraphicsAnchorLayout::AnchorVertex, and has everything that class has.

  C++ hands a QtGraphicsAnchorLayout::AnchorVertexPair around as a copy, so
  every C++ QtGraphicsAnchorLayout::AnchorVertexPair behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtGraphicsAnchorLayout::AnchorVertexPair that has a
  ritual and that Python can call so far, 1 name in all: 'toString'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtGraphicsAnchorLayout::AnchorVertexPair::~AnchorVertexPair()': the
    destructor: Python removes its C++
    QtGraphicsAnchorLayout::AnchorVertexPair by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QtGraphicsAnchorLayout::AnchorVertexPair is created at the first
    use, not by 'QtGraphicsAnchorLayout::AnchorVertexPair(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtGraphicsAnchorLayout::AnchorVertexPair back gives a
    copy the ritual made for Python, in a new cute
    QtGraphicsAnchorLayout::AnchorVertexPair.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtGraphicsAnchorLayout::AnchorVertexPair'

  #  A C++ QtGraphicsAnchorLayout::AnchorVertexPair Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtGraphicsAnchorLayout_AnchorVertexPair'

  #  Qt's '~QtGraphicsAnchorLayout::AnchorVertexPair()'. Naming it makes this
  #  a value class: Python owns every C++
  #  QtGraphicsAnchorLayout::AnchorVertexPair behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN22QtGraphicsAnchorLayout16AnchorVertexPairD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QtGraphicsAnchorLayout::AnchorVertexPair::toString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgraphicsanchorlayout-anchorvertexpair.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtGraphicsAnchorLayout::AnchorVertexPair::toString() const
    ritual = (
        'ritual_ZNK22QtGraphicsAnchorLayout16AnchorVertexPair8toStringEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QtGraphicsAnchorLayout16AnchorVertexPair8toStrin'
          'gEv')
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

  @overload(
      QtGraphicsAnchorLayout.AnchorVertex,
      QtGraphicsAnchorLayout.AnchorVertex,
      WAIT['QtGraphicsAnchorLayout.AnchorData'],
  )
  @overload(
      QtGraphicsAnchorLayout.AnchorVertex,
      QtGraphicsAnchorLayout.AnchorVertex, NoneType,
  )
  @overload(
      QtGraphicsAnchorLayout.AnchorVertex, NoneType,
      WAIT['QtGraphicsAnchorLayout.AnchorData'],
  )
  @overload(QtGraphicsAnchorLayout.AnchorVertex, NoneType, NoneType)
  @overload(
      NoneType, QtGraphicsAnchorLayout.AnchorVertex,
      WAIT['QtGraphicsAnchorLayout.AnchorData'],
  )
  @overload(NoneType, QtGraphicsAnchorLayout.AnchorVertex, NoneType)
  @overload(NoneType, NoneType, WAIT['QtGraphicsAnchorLayout.AnchorData'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      v1: Optional[QtGraphicsAnchorLayout.AnchorVertex],
      v2: Optional[QtGraphicsAnchorLayout.AnchorVertex],
      data: Optional[QtGraphicsAnchorLayout.AnchorData],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QtGraphicsAnchorLayout::AnchorVertexPair::AnchorVertexPair(AnchorVertex
    *v1, AnchorVertex *v2, AnchorData *data)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtgraphicsanchorlayout-anchorvertexpair.html

    Parameters
    ----------

    v1 : Optional[QtGraphicsAnchorLayout.AnchorVertex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    v2 : Optional[QtGraphicsAnchorLayout.AnchorVertex]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[QtGraphicsAnchorLayout.AnchorData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtGraphicsAnchorLayout::AnchorVertexPair::AnchorVertexPair(
    #      AnchorVertex *v1, AnchorVertex *v2, AnchorData *data)
    self._noteCreation(AnchorVertexPair, lambda: Rituals.call(
        'ritual_ZN22QtGraphicsAnchorLayout16AnchorVertexPairC1EPNS_12Anchor'
        'VertexES2_PNS_10AnchorDataE',
        self._addressOf(v1), self._addressOf(v2), self._addressOf(data),
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
