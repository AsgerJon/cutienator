"""
QQuickPropertyAnimationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPropertyAnimationPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickAbstractAnimationPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQml import QAbstractAnimationJob
  from . import QQuickPropertyAnimation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAnimationJob = WAIT['QAbstractAnimationJob']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPropertyAnimationPrivate(QQuickAbstractAnimationPrivate):
  """
  The cute side of Qt's QQuickPropertyAnimationPrivate: a plain Python object
  standing in front of one C++ QQuickPropertyAnimationPrivate.

  It is built on the cute 'QQuickAbstractAnimationPrivate', as Qt's
  QQuickPropertyAnimationPrivate is built on Qt's
  QQuickAbstractAnimationPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPropertyAnimationPrivate that has a ritual and
  that Python can call so far, 2 names in all: 'q_func',
  'animationCurrentLoopChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPropertyAnimation
    *QQuickPropertyAnimationPrivate::q_func() const': takes in Python what
    'QQuickPropertyAnimation *QQuickPropertyAnimationPrivate::q_func()'
    takes.
  - Qt's 'void QQuickPropertyAnimationPrivate::convertVariant(QVariant
    &variant, QMetaType type)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QQuickPropertyAnimationPrivate is created at the first use, not
    by 'QQuickPropertyAnimationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPropertyAnimationPrivate.
  - Each name of Qt's QQuickPropertyAnimationPrivate that has no cute
    function yet, 'convertVariant', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPropertyAnimationPrivate'

  #  A C++ QQuickPropertyAnimationPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPropertyAnimationPrivate'

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
    'QQuickPropertyAnimationPrivate::QQuickPropertyAnimationPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimationprivate.html
    """
    #  QQuickPropertyAnimationPrivate::QQuickPropertyAnimationPrivate()
    self._noteCreation(QQuickPropertyAnimationPrivate, lambda: Rituals.call(
        'ritual_ZN30QQuickPropertyAnimationPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickPropertyAnimation]:
    """
    Calls Qt's 'QQuickPropertyAnimation
    *QQuickPropertyAnimationPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimationprivate.html#q_func

    Returns
    -------

    Optional[QQuickPropertyAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPropertyAnimation *QQuickPropertyAnimationPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QQuickPropertyAnimationPrivate6q_funcEv',
    )
    from . import QQuickPropertyAnimation
    return QQuickPropertyAnimation._cuteAt(address)

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def animationCurrentLoopChanged(
      self,
      job: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickPropertyAnimationPrivate::animationCurrentLoopChanged(
    QAbstractAnimationJob *job)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertyanimationprivate.html

    Parameters
    ----------

    job : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPropertyAnimationPrivate::animationCurrentLoopChanged(
    #      QAbstractAnimationJob *job)
    ritual = (
        'ritual_ZN30QQuickPropertyAnimationPrivate27animationCurrentLoopCha'
        'ngedEP21QAbstractAnimationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickPropertyAnimationPrivate27animationCurrentL'
          'oopChangedEP21QAbstractAnimationJob')
    self.uglySide.call(ritual, self._addressOf(job, 'QAbstractAnimationJob'))

  @staticmethod
  def convertVariant(*__, **_) -> Never:
    """
    Qt's 'void QQuickPropertyAnimationPrivate::convertVariant(QVariant
    &variant, QMetaType type)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuickPropertyAnimationPrivate.convertVariant' has no cute "
        "function yet. Qt's 'void "
        "QQuickPropertyAnimationPrivate::convertVariant(QVariant &variant, "
        "QMetaType type)': takes a type Python has no way to hand over yet.")
