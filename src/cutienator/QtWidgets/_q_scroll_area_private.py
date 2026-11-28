"""
QScrollAreaPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qscrollarea_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QScrollAreaPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QAbstractScrollAreaPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QScrollArea


class QScrollAreaPrivate(QAbstractScrollAreaPrivate):
  """
  The cute side of Qt's QScrollAreaPrivate: a plain Python object standing in
  front of one C++ QScrollAreaPrivate.

  It is built on the cute 'QAbstractScrollAreaPrivate', as Qt's
  QScrollAreaPrivate is built on Qt's QAbstractScrollAreaPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QScrollAreaPrivate that has a ritual and that Python
  can call so far, 3 names in all: 'q_func', 'updateScrollBars',
  'updateWidgetPosition'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QScrollArea *QScrollAreaPrivate::q_func() const': takes in
    Python what 'QScrollArea *QScrollAreaPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QScrollAreaPrivate is created at the first use, not by
    'QScrollAreaPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScrollAreaPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScrollAreaPrivate'

  #  A C++ QScrollAreaPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScrollAreaPrivate'

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
    'QScrollAreaPrivate::QScrollAreaPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollareaprivate.html#QScrollAreaPrivate
    """
    #  QScrollAreaPrivate::QScrollAreaPrivate()
    self._noteCreation(QScrollAreaPrivate, lambda: Rituals.call(
        'ritual_ZN18QScrollAreaPrivateC1Ev',
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

  def q_func(self) -> Optional[QScrollArea]:
    """
    Calls Qt's 'QScrollArea *QScrollAreaPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollareaprivate.html#q_func

    Returns
    -------

    Optional[QScrollArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollArea *QScrollAreaPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QScrollAreaPrivate6q_funcEv')
    from . import QScrollArea
    return QScrollArea._cuteAt(address)

  def updateScrollBars(self) -> None:
    """
    Calls Qt's 'void QScrollAreaPrivate::updateScrollBars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollareaprivate.html#updateScrollBars
    """
    #  void QScrollAreaPrivate::updateScrollBars()
    self.uglySide.call('ritual_ZN18QScrollAreaPrivate16updateScrollBarsEv')

  def updateWidgetPosition(self) -> None:
    """
    Calls Qt's 'void QScrollAreaPrivate::updateWidgetPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollareaprivate.html#updateWidgetPosition
    """
    #  void QScrollAreaPrivate::updateWidgetPosition()
    self.uglySide.call(
        'ritual_ZN18QScrollAreaPrivate20updateWidgetPositionEv',
    )
