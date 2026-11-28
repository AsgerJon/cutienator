"""
QQuickAnimatorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimator_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAnimatorPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QQuickAbstractAnimationPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickAnimator


class QQuickAnimatorPrivate(QQuickAbstractAnimationPrivate):
  """
  The cute side of Qt's QQuickAnimatorPrivate: a plain Python object standing
  in front of one C++ QQuickAnimatorPrivate.

  It is built on the cute 'QQuickAbstractAnimationPrivate', as Qt's
  QQuickAnimatorPrivate is built on Qt's QQuickAbstractAnimationPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnimatorPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickAnimator *QQuickAnimatorPrivate::q_func() const': takes
    in Python what 'QQuickAnimator *QQuickAnimatorPrivate::q_func()' takes.
  - Qt's 'void QQuickAnimatorPrivate::apply(QQuickAnimatorJob *job, const
    QString &propertyName, QQuickStateActions &actions, QQmlProperties
    &modified, QObject *defaultTarget)': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ QQuickAnimatorPrivate is created at the first use, not by
    'QQuickAnimatorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimatorPrivate.
  - Each name of Qt's QQuickAnimatorPrivate that has no cute function yet,
    'apply', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QQuickAnimatorPrivate'

  #  A C++ QQuickAnimatorPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnimatorPrivate'

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
    'QQuickAnimatorPrivate::QQuickAnimatorPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatorprivate.html#QQuickAnimatorPrivate
    """
    #  QQuickAnimatorPrivate::QQuickAnimatorPrivate()
    self._noteCreation(QQuickAnimatorPrivate, lambda: Rituals.call(
        'ritual_ZN21QQuickAnimatorPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickAnimator]:
    """
    Calls Qt's 'QQuickAnimator *QQuickAnimatorPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatorprivate.html#q_func

    Returns
    -------

    Optional[QQuickAnimator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimator *QQuickAnimatorPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QQuickAnimatorPrivate6q_funcEv')
    from . import QQuickAnimator
    return QQuickAnimator._cuteAt(address)

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnimatorPrivate::apply(QQuickAnimatorJob *job, const
    QString &propertyName, QQuickStateActions &actions, QQmlProperties
    &modified, QObject *defaultTarget)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuickAnimatorPrivate.apply' has no cute function yet. Qt's 'void "
        "QQuickAnimatorPrivate::apply(QQuickAnimatorJob *job, const QString "
        "&propertyName, QQuickStateActions &actions, QQmlProperties "
        "&modified, QObject *defaultTarget)': takes a type Python has no "
        "way to hand over yet.")
