"""
QQuickParticleSystemAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickParticleSystemAnimation to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QAbstractAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickParticleSystemAnimation(QAbstractAnimation):
  """
  The cute side of Qt's QQuickParticleSystemAnimation: a plain Python object
  standing in front of one C++ QQuickParticleSystemAnimation.

  It is built on the cute 'QAbstractAnimation', as Qt's
  QQuickParticleSystemAnimation is built on Qt's QAbstractAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickParticleSystemAnimation that has a ritual and
  that Python can call so far, 3 names in all: 'metaObject',
  'updateCurrentTime', 'duration'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickParticleSystemAnimation::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickParticleSystemAnimation::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickParticleSystemAnimation; 1 leans on 'vtable for
  QQuickParticleSystemAnimation', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickParticleSystemAnimation is created at the first use, not by
    'QQuickParticleSystemAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickParticleSystemAnimation.
  - Qt tells when it has removed the C++ QQuickParticleSystemAnimation. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickParticleSystemAnimation that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickParticleSystemAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickParticleSystemAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystemanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickParticleSystemAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickParticleSystemAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickParticleSystemAnimation::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystemanimation.html#duration
    """
    #  int QQuickParticleSystemAnimation::duration() const
    ritual = 'ritual_ZNK29QQuickParticleSystemAnimation8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QQuickParticleSystemAnimation8durationEv'
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickParticleSystemAnimation::QQuickParticleSystemAnimation(
    QQuickParticleSystem *system)': leans on 'vtable for
    QQuickParticleSystemAnimation', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickParticleSystemAnimation.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickParticleSystemAnimation::QQuickParticleSystemAnimation(QQuic"
        "kParticleSystem *system)': leans on 'vtable for "
        "QQuickParticleSystemAnimation', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  @overload(int)
  def updateCurrentTime(self, t: int) -> None:
    """
    Calls Qt's 'void QQuickParticleSystemAnimation::updateCurrentTime(int
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystemanimation.html

    Parameters
    ----------

    t : int
      Passed on as it is.
    """
    #  void QQuickParticleSystemAnimation::updateCurrentTime(int t)
    ritual = 'ritual_ZN29QQuickParticleSystemAnimation17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuickParticleSystemAnimation17updateCurrentTimeE'
          'i')
    self.uglySide.call(ritual, t)
