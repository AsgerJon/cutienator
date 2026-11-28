"""
QQuickPinchAreaPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpincharea_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPinchAreaPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QQuickItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickPinchArea


class QQuickPinchAreaPrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickPinchAreaPrivate: a plain Python object
  standing in front of one C++ QQuickPinchAreaPrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's QQuickPinchAreaPrivate
  is built on Qt's QQuickItemPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPinchAreaPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'init'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPinchArea *QQuickPinchAreaPrivate::q_func() const':
    takes in Python what 'QQuickPinchArea *QQuickPinchAreaPrivate::q_func()'
    takes.
  - Qt's 'QQuickPinchAreaPrivate::~QQuickPinchAreaPrivate()': the destructor:
    Python never removes a C++ QQuickPinchAreaPrivate.

  What to expect
  --------------

  - The C++ QQuickPinchAreaPrivate is created at the first use, not by
    'QQuickPinchAreaPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPinchAreaPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPinchAreaPrivate'

  #  A C++ QQuickPinchAreaPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPinchAreaPrivate'

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
    'QQuickPinchAreaPrivate::QQuickPinchAreaPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpinchareaprivate.html#QQuickPinchAreaPrivate
    """
    #  QQuickPinchAreaPrivate::QQuickPinchAreaPrivate()
    self._noteCreation(QQuickPinchAreaPrivate, lambda: Rituals.call(
        'ritual_ZN22QQuickPinchAreaPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickPinchArea]:
    """
    Calls Qt's 'QQuickPinchArea *QQuickPinchAreaPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchareaprivate.html#q_func

    Returns
    -------

    Optional[QQuickPinchArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPinchArea *QQuickPinchAreaPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickPinchAreaPrivate6q_funcEv',
    )
    from . import QQuickPinchArea
    return QQuickPinchArea._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickPinchAreaPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpinchareaprivate.html#init
    """
    #  void QQuickPinchAreaPrivate::init()
    self.uglySide.call('ritual_ZN22QQuickPinchAreaPrivate4initEv')
