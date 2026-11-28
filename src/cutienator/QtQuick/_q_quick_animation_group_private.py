"""
QQuickAnimationGroupPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAnimationGroupPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickAbstractAnimationPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQml import QAbstractAnimationJob
  from . import QQuickAnimationGroup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAnimationJob = WAIT['QAbstractAnimationJob']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnimationGroupPrivate(QQuickAbstractAnimationPrivate):
  """
  The cute side of Qt's QQuickAnimationGroupPrivate: a plain Python object
  standing in front of one C++ QQuickAnimationGroupPrivate.

  It is built on the cute 'QQuickAbstractAnimationPrivate', as Qt's
  QQuickAnimationGroupPrivate is built on Qt's
  QQuickAbstractAnimationPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnimationGroupPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'q_func',
  'restartFromCurrentLoop', 'animationCurrentLoopChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickAnimationGroup *QQuickAnimationGroupPrivate::q_func()
    const': takes in Python what 'QQuickAnimationGroup
    *QQuickAnimationGroupPrivate::q_func()' takes.
  - Qt's 'void QQuickAnimationGroupPrivate::append_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list, QQuickAbstractAnimation
    *role)': names 'QQmlListProperty<QQuickAbstractAnimation>', which has no
    cute class yet.
  - Qt's 'QQuickAbstractAnimation *QQuickAnimationGroupPrivate::at_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list, qsizetype index)': names
    'QQmlListProperty<QQuickAbstractAnimation>', which has no cute class yet.
  - Qt's 'qsizetype QQuickAnimationGroupPrivate::count_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list)': names
    'QQmlListProperty<QQuickAbstractAnimation>', which has no cute class yet.
  - Qt's 'void QQuickAnimationGroupPrivate::clear_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list)': names
    'QQmlListProperty<QQuickAbstractAnimation>', which has no cute class yet.
  - Qt's 'void QQuickAnimationGroupPrivate::replace_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list, qsizetype index,
    QQuickAbstractAnimation *role)': names
    'QQmlListProperty<QQuickAbstractAnimation>', which has no cute class yet.
  - Qt's 'void QQuickAnimationGroupPrivate::removeLast_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list)': names
    'QQmlListProperty<QQuickAbstractAnimation>', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQuickAnimationGroupPrivate is created at the first use, not by
    'QQuickAnimationGroupPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimationGroupPrivate.
  - Each name of Qt's QQuickAnimationGroupPrivate that has no cute function
    yet, 'append_animation', 'at_animation', 'clear_animation',
    'count_animation', 'removeLast_animation', 'replace_animation', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimationGroupPrivate'

  #  A C++ QQuickAnimationGroupPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnimationGroupPrivate'

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
    'QQuickAnimationGroupPrivate::QQuickAnimationGroupPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationgroupprivate.html
    """
    #  QQuickAnimationGroupPrivate::QQuickAnimationGroupPrivate()
    self._noteCreation(QQuickAnimationGroupPrivate, lambda: Rituals.call(
        'ritual_ZN27QQuickAnimationGroupPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickAnimationGroup]:
    """
    Calls Qt's 'QQuickAnimationGroup *QQuickAnimationGroupPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationgroupprivate.html#q_func

    Returns
    -------

    Optional[QQuickAnimationGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimationGroup *QQuickAnimationGroupPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QQuickAnimationGroupPrivate6q_funcEv',
    )
    from . import QQuickAnimationGroup
    return QQuickAnimationGroup._cuteAt(address)

  def restartFromCurrentLoop(self) -> None:
    """
    Calls Qt's 'void QQuickAnimationGroupPrivate::restartFromCurrentLoop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationgroupprivate.html
    """
    #  void QQuickAnimationGroupPrivate::restartFromCurrentLoop()
    self.uglySide.call(
        'ritual_ZN27QQuickAnimationGroupPrivate22restartFromCurrentLoopEv',
    )

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def animationCurrentLoopChanged(
      self,
      job: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickAnimationGroupPrivate::animationCurrentLoopChanged(
    QAbstractAnimationJob *job)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimationgroupprivate.html

    Parameters
    ----------

    job : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimationGroupPrivate::animationCurrentLoopChanged(
    #      QAbstractAnimationJob *job)
    ritual = (
        'ritual_ZN27QQuickAnimationGroupPrivate27animationCurrentLoopChange'
        'dEP21QAbstractAnimationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickAnimationGroupPrivate27animationCurrentLoop'
          'ChangedEP21QAbstractAnimationJob')
    self.uglySide.call(ritual, self._addressOf(job, 'QAbstractAnimationJob'))

  @staticmethod
  def append_animation(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnimationGroupPrivate::append_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list, QQuickAbstractAnimation
    *role)': names 'QQmlListProperty<QQuickAbstractAnimation>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickAnimationGroupPrivate.append_animation' has no cute "
        "function yet. Qt's 'void "
        "QQuickAnimationGroupPrivate::append_animation(QQmlListProperty<QQui"
        "ckAbstractAnimation> *list, QQuickAbstractAnimation *role)': names "
        "'QQmlListProperty<QQuickAbstractAnimation>', which has no cute "
        "class yet.")

  @staticmethod
  def at_animation(*__, **_) -> Never:
    """
    Qt's 'QQuickAbstractAnimation *QQuickAnimationGroupPrivate::at_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list, qsizetype index)': names
    'QQmlListProperty<QQuickAbstractAnimation>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickAnimationGroupPrivate.at_animation' has no cute function "
        "yet. Qt's 'QQuickAbstractAnimation "
        "*QQuickAnimationGroupPrivate::at_animation(QQmlListProperty<QQuickA"
        "bstractAnimation> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuickAbstractAnimation>', which has no cute "
        "class yet.")

  @staticmethod
  def clear_animation(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnimationGroupPrivate::clear_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list)': names
    'QQmlListProperty<QQuickAbstractAnimation>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickAnimationGroupPrivate.clear_animation' has no cute function "
        "yet. Qt's 'void "
        "QQuickAnimationGroupPrivate::clear_animation(QQmlListProperty<QQuic"
        "kAbstractAnimation> *list)': names "
        "'QQmlListProperty<QQuickAbstractAnimation>', which has no cute "
        "class yet.")

  @staticmethod
  def count_animation(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickAnimationGroupPrivate::count_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list)': names
    'QQmlListProperty<QQuickAbstractAnimation>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickAnimationGroupPrivate.count_animation' has no cute function "
        "yet. Qt's 'qsizetype "
        "QQuickAnimationGroupPrivate::count_animation(QQmlListProperty<QQuic"
        "kAbstractAnimation> *list)': names "
        "'QQmlListProperty<QQuickAbstractAnimation>', which has no cute "
        "class yet.")

  @staticmethod
  def removeLast_animation(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnimationGroupPrivate::removeLast_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list)': names
    'QQmlListProperty<QQuickAbstractAnimation>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickAnimationGroupPrivate.removeLast_animation' has no cute "
        "function yet. Qt's 'void "
        "QQuickAnimationGroupPrivate::removeLast_animation(QQmlListProperty<"
        "QQuickAbstractAnimation> *list)': names "
        "'QQmlListProperty<QQuickAbstractAnimation>', which has no cute "
        "class yet.")

  @staticmethod
  def replace_animation(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnimationGroupPrivate::replace_animation(
    QQmlListProperty<QQuickAbstractAnimation> *list, qsizetype index,
    QQuickAbstractAnimation *role)': names
    'QQmlListProperty<QQuickAbstractAnimation>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickAnimationGroupPrivate.replace_animation' has no cute "
        "function yet. Qt's 'void "
        "QQuickAnimationGroupPrivate::replace_animation(QQmlListProperty<QQu"
        "ickAbstractAnimation> *list, qsizetype index, "
        "QQuickAbstractAnimation *role)': names "
        "'QQmlListProperty<QQuickAbstractAnimation>', which has no cute "
        "class yet.")
