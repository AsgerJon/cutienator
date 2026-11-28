"""
QWaylandQuickShellSurfaceItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandquickshellsurfaceitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandQuickShellSurfaceItemPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QWaylandQuickItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QWaylandQuickShellSurfaceItem, QWaylandShellSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandQuickShellSurfaceItem = WAIT['QWaylandQuickShellSurfaceItem']
  QWaylandShellSurface = WAIT['QWaylandShellSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickShellSurfaceItemPrivate(QWaylandQuickItemPrivate):
  """
  The cute side of Qt's QWaylandQuickShellSurfaceItemPrivate: a plain Python
  object standing in front of one C++ QWaylandQuickShellSurfaceItemPrivate.

  It is built on the cute 'QWaylandQuickItemPrivate', as Qt's
  QWaylandQuickShellSurfaceItemPrivate is built on Qt's
  QWaylandQuickItemPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandQuickShellSurfaceItemPrivate that has a
  ritual and that Python can call so far, 6 names in all: 'q_func',
  'setShellSurface', 'maybeCreateAutoPopup', 'get', 'raise_', 'lower'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWaylandQuickShellSurfaceItem
    *QWaylandQuickShellSurfaceItemPrivate::q_func() const': takes in Python
    what 'QWaylandQuickShellSurfaceItem
    *QWaylandQuickShellSurfaceItemPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QWaylandQuickShellSurfaceItemPrivate is created at the first use,
    not by 'QWaylandQuickShellSurfaceItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQuickShellSurfaceItemPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QWaylandQuickShellSurfaceItem)
  @overload(NoneType)
  def get(
      item: Optional[QWaylandQuickShellSurfaceItem],
  ) -> Optional[QWaylandQuickShellSurfaceItemPrivate]:
    """
    Calls Qt's 'QWaylandQuickShellSurfaceItemPrivate
    *QWaylandQuickShellSurfaceItemPrivate::get(QWaylandQuickShellSurfaceItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitemprivate.html#get

    Parameters
    ----------

    item : Optional[QWaylandQuickShellSurfaceItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandQuickShellSurfaceItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQuickShellSurfaceItemPrivate
    #      *QWaylandQuickShellSurfaceItemPrivate::get(
    #      QWaylandQuickShellSurfaceItem *item)
    address = Rituals.call(
        'ritual_ZN36QWaylandQuickShellSurfaceItemPrivate3getEP29QWaylandQui'
        'ckShellSurfaceItem',
        CuteMixin._addressOf(item),
    )
    return QWaylandQuickShellSurfaceItemPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickShellSurfaceItemPrivate'

  #  A C++ QWaylandQuickShellSurfaceItemPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandQuickShellSurfaceItemPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandShellSurface)
  @overload(NoneType)
  def setShellSurface(
      self,
      shellSurface: Optional[QWaylandShellSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellSurfaceItemPrivate::setShellSurface(
    QWaylandShellSurface *shellSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitemprivate.html

    Parameters
    ----------

    shellSurface : Optional[QWaylandShellSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickShellSurfaceItemPrivate::setShellSurface(
    #      QWaylandShellSurface *shellSurface)
    self.uglySide.call(
        'ritual_ZN36QWaylandQuickShellSurfaceItemPrivate15setShellSurfaceEP'
        '20QWaylandShellSurface',
        self._addressOf(shellSurface),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QWaylandQuickShellSurfaceItemPrivate::
    QWaylandQuickShellSurfaceItemPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitemprivate.html
    """
    #  QWaylandQuickShellSurfaceItemPrivate::
    #      QWaylandQuickShellSurfaceItemPrivate()
    self._noteCreation(
        QWaylandQuickShellSurfaceItemPrivate, lambda: Rituals.call(
            'ritual_ZN36QWaylandQuickShellSurfaceItemPrivateC1Ev',
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

  def q_func(self) -> Optional[QWaylandQuickShellSurfaceItem]:
    """
    Calls Qt's 'QWaylandQuickShellSurfaceItem
    *QWaylandQuickShellSurfaceItemPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitemprivate.html#q_func

    Returns
    -------

    Optional[QWaylandQuickShellSurfaceItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQuickShellSurfaceItem
    #      *QWaylandQuickShellSurfaceItemPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN36QWaylandQuickShellSurfaceItemPrivate6q_funcEv',
    )
    from . import QWaylandQuickShellSurfaceItem
    return QWaylandQuickShellSurfaceItem._cuteAt(address)

  @overload(QWaylandShellSurface)
  @overload(NoneType)
  def maybeCreateAutoPopup(
      self,
      shellSurface: Optional[QWaylandShellSurface],
  ) -> Optional[QWaylandQuickShellSurfaceItem]:
    """
    Calls Qt's 'QWaylandQuickShellSurfaceItem
    *QWaylandQuickShellSurfaceItemPrivate::maybeCreateAutoPopup(
    QWaylandShellSurface *shellSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitemprivate.html

    Parameters
    ----------

    shellSurface : Optional[QWaylandShellSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandQuickShellSurfaceItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQuickShellSurfaceItem
    #      *QWaylandQuickShellSurfaceItemPrivate::maybeCreateAutoPopup(
    #      QWaylandShellSurface *shellSurface)
    address = self.uglySide.call(
        'ritual_ZN36QWaylandQuickShellSurfaceItemPrivate20maybeCreateAutoPo'
        'pupEP20QWaylandShellSurface',
        self._addressOf(shellSurface),
    )
    from . import QWaylandQuickShellSurfaceItem
    return QWaylandQuickShellSurfaceItem._cuteAt(address)

  def raise_(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellSurfaceItemPrivate::raise()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitemprivate.html#raise
    """
    #  void QWaylandQuickShellSurfaceItemPrivate::raise()
    ritual = 'ritual_ZN36QWaylandQuickShellSurfaceItemPrivate5raiseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN36QWaylandQuickShellSurfaceItemPrivate5raiseEv'
    self.uglySide.call(ritual)

  def lower(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellSurfaceItemPrivate::lower()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitemprivate.html#lower
    """
    #  void QWaylandQuickShellSurfaceItemPrivate::lower()
    ritual = 'ritual_ZN36QWaylandQuickShellSurfaceItemPrivate5lowerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN36QWaylandQuickShellSurfaceItemPrivate5lowerEv'
    self.uglySide.call(ritual)
