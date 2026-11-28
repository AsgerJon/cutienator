"""
Q3DGraphsWidgetItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphsWidgets/6.12.0/QtGraphsWidgets/private/q3dgraphswidgetitem_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Q3DGraphsWidgetItemPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtQuick import QQuickWheelEvent
  from . import Q3DGraphsWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWheelEvent = WAIT['QQuickWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DGraphsWidgetItemPrivate(QObjectPrivate):
  """
  The cute side of Qt's Q3DGraphsWidgetItemPrivate: a plain Python object
  standing in front of one C++ Q3DGraphsWidgetItemPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  Q3DGraphsWidgetItemPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DGraphsWidgetItemPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'createGraph', 'onWheel',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const Q3DGraphsWidgetItem *Q3DGraphsWidgetItemPrivate::q_func()
    const': takes in Python what 'Q3DGraphsWidgetItem
    *Q3DGraphsWidgetItemPrivate::q_func()' takes.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ Q3DGraphsWidgetItemPrivate is created at the first use, not by
    'Q3DGraphsWidgetItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DGraphsWidgetItemPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DGraphsWidgetItemPrivate'

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
    'Q3DGraphsWidgetItemPrivate::Q3DGraphsWidgetItemPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitemprivate.html
    """
    #  Q3DGraphsWidgetItemPrivate::Q3DGraphsWidgetItemPrivate()
    self._noteCreation(Q3DGraphsWidgetItemPrivate, lambda: Rituals.call(
        'ritual_ZN26Q3DGraphsWidgetItemPrivateC1Ev',
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

  def createGraph(self) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItemPrivate::createGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitemprivate.html#createGraph
    """
    #  void Q3DGraphsWidgetItemPrivate::createGraph()
    self.uglySide.call(
        'ritual_ZN26Q3DGraphsWidgetItemPrivate11createGraphEv',
    )

  @overload(QQuickWheelEvent)
  @overload(NoneType)
  def onWheel(self, event: Optional[QQuickWheelEvent]) -> None:
    """
    Calls Qt's 'void Q3DGraphsWidgetItemPrivate::onWheel(QQuickWheelEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitemprivate.html#onWheel

    Parameters
    ----------

    event : Optional[QQuickWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DGraphsWidgetItemPrivate::onWheel(QQuickWheelEvent *event)
    self.uglySide.call(
        'ritual_ZN26Q3DGraphsWidgetItemPrivate7onWheelEP16QQuickWheelEvent',
        self._addressOf(event),
    )

  def q_func(self) -> Optional[Q3DGraphsWidgetItem]:
    """
    Calls Qt's 'Q3DGraphsWidgetItem *Q3DGraphsWidgetItemPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dgraphswidgetitemprivate.html#q_func

    Returns
    -------

    Optional[Q3DGraphsWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DGraphsWidgetItem *Q3DGraphsWidgetItemPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26Q3DGraphsWidgetItemPrivate6q_funcEv',
    )
    from . import Q3DGraphsWidgetItem
    return Q3DGraphsWidgetItem._cuteAt(address)
