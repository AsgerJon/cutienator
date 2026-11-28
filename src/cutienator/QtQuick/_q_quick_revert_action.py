"""
QQuickRevertAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickRevertAction to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtQml import QQmlProperty
  from . import QQuickStateActionEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlProperty = WAIT['QQmlProperty']
  QQuickStateActionEvent = WAIT['QQuickStateActionEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRevertAction(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickRevertAction: a plain Python object standing in
  front of one C++ QQuickRevertAction.

  C++ hands a QQuickRevertAction around as a copy, so every C++
  QQuickRevertAction behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQuickRevertAction yet. It can be made from Python, in
  3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickRevertAction::~QQuickRevertAction()': the destructor: Python
    removes its C++ QQuickRevertAction by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickRevertAction is created at the first use, not by
    'QQuickRevertAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickRevertAction back gives a copy the ritual made
    for Python, in a new cute QQuickRevertAction.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRevertAction'

  #  Qt's '~QQuickRevertAction()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickRevertAction behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQuickRevertActionD1Ev'

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
    'QQuickRevertAction::QQuickRevertAction()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrevertaction.html#QQuickRevertAction
    """
    #  QQuickRevertAction::QQuickRevertAction()
    self._noteCreation(QQuickRevertAction, lambda: Rituals.call(
        'ritual_ZN18QQuickRevertActionC1Ev',
    ))

  @overload(QQmlProperty)
  def __init__(self, prop: QQmlProperty) -> None:
    """
    Notes what was given, for Qt's
    'QQuickRevertAction::QQuickRevertAction(const QQmlProperty &prop)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrevertaction.html#QQuickRevertAction

    Parameters
    ----------

    prop : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  QQuickRevertAction::QQuickRevertAction(const QQmlProperty &prop)
    self._noteCreation(QQuickRevertAction, lambda: Rituals.call(
        'ritual_ZN18QQuickRevertActionC1ERK12QQmlProperty',
        self._valueOf(prop),
    ))

  @overload(QQuickStateActionEvent)
  @overload(NoneType)
  def __init__(self, e: Optional[QQuickStateActionEvent]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickRevertAction::QQuickRevertAction(QQuickStateActionEvent *e)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrevertaction.html#QQuickRevertAction

    Parameters
    ----------

    e : Optional[QQuickStateActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickRevertAction::QQuickRevertAction(QQuickStateActionEvent *e)
    self._noteCreation(QQuickRevertAction, lambda: Rituals.call(
        'ritual_ZN18QQuickRevertActionC1EP22QQuickStateActionEvent',
        self._addressOf(e, 'QQuickStateActionEvent'),
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
