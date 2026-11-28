"""
QQuickScriptActionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickScriptActionPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickAbstractAnimationPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDebug
  from . import QAbstractAnimationAction, QQuickScriptAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QQuickScriptActionPrivate(QQuickAbstractAnimationPrivate):
  """
  The cute side of Qt's QQuickScriptActionPrivate: a plain Python object
  standing in front of one C++ QQuickScriptActionPrivate.

  It is built on the cute 'QQuickAbstractAnimationPrivate', as Qt's
  QQuickScriptActionPrivate is built on Qt's QQuickAbstractAnimationPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScriptActionPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'q_func', 'execute',
  'createAction', 'debugAction'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickScriptAction *QQuickScriptActionPrivate::q_func()
    const': takes in Python what 'QQuickScriptAction
    *QQuickScriptActionPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickScriptActionPrivate is created at the first use, not by
    'QQuickScriptActionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScriptActionPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScriptActionPrivate'

  #  A C++ QQuickScriptActionPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickScriptActionPrivate'

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
    'QQuickScriptActionPrivate::QQuickScriptActionPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscriptactionprivate.html
    """
    #  QQuickScriptActionPrivate::QQuickScriptActionPrivate()
    self._noteCreation(QQuickScriptActionPrivate, lambda: Rituals.call(
        'ritual_ZN25QQuickScriptActionPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickScriptAction]:
    """
    Calls Qt's 'QQuickScriptAction *QQuickScriptActionPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscriptactionprivate.html#q_func

    Returns
    -------

    Optional[QQuickScriptAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScriptAction *QQuickScriptActionPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QQuickScriptActionPrivate6q_funcEv',
    )
    from . import QQuickScriptAction
    return QQuickScriptAction._cuteAt(address)

  def execute(self) -> None:
    """
    Calls Qt's 'void QQuickScriptActionPrivate::execute()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscriptactionprivate.html#execute
    """
    #  void QQuickScriptActionPrivate::execute()
    self.uglySide.call('ritual_ZN25QQuickScriptActionPrivate7executeEv')

  def createAction(self) -> Optional[QAbstractAnimationAction]:
    """
    Calls Qt's 'QAbstractAnimationAction
    *QQuickScriptActionPrivate::createAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscriptactionprivate.html#createAction

    Returns
    -------

    Optional[QAbstractAnimationAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimationAction *QQuickScriptActionPrivate::createAction()
    address = self.uglySide.call(
        'ritual_ZN25QQuickScriptActionPrivate12createActionEv',
    )
    from . import QAbstractAnimationAction
    return QAbstractAnimationAction._cuteAt(address)

  @overload(QDebug, int)
  def debugAction(self, d: QDebug, indentLevel: int) -> None:
    """
    Calls Qt's 'void QQuickScriptActionPrivate::debugAction(QDebug d, int
    indentLevel) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscriptactionprivate.html#debugAction

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    indentLevel : int
      Passed on as it is.
    """
    #  void QQuickScriptActionPrivate::debugAction(QDebug d, int indentLevel)
    #      const
    self.uglySide.call(
        'ritual_ZNK25QQuickScriptActionPrivate11debugActionE6QDebugi',
        self._valueOf(d), indentLevel,
    )
