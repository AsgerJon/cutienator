"""
QQuickRotationAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickRotationAnimator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickAnimator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickAnimatorJob, QQuickRotationAnimatorPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRotationAnimator(QQuickAnimator):
  """
  The cute side of Qt's QQuickRotationAnimator: a plain Python object
  standing in front of one C++ QQuickRotationAnimator.

  It is built on the cute 'QQuickAnimator', as Qt's QQuickRotationAnimator is
  built on Qt's QQuickAnimator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRotationAnimator that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'd_func',
  'setDirection', 'direction', 'directionChanged', 'createJob',
  'propertyName'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRotationAnimator::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickRotationAnimator::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickRotationAnimatorPrivate
    *QQuickRotationAnimator::d_func() const': takes in Python what
    'QQuickRotationAnimatorPrivate *QQuickRotationAnimator::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickRotationAnimator is created at the first use, not by
    'QQuickRotationAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRotationAnimator.
  - Qt tells when it has removed the C++ QQuickRotationAnimator. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickRotationAnimator, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class RotationDirection(CuteNum):
    """
    The enum 'QQuickRotationAnimator::RotationDirection' of Qt, with the 4
    names Qt gives in it.
    """

    Numerical = Kee[int](0)
    Shortest = Kee[int](1)
    Clockwise = Kee[int](2)
    Counterclockwise = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickRotationAnimator::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotationanimator.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickRotationAnimator::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuickRotationAnimator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRotationAnimator'

  #  A C++ QQuickRotationAnimator Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRotationAnimator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRotationAnimator::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRotationAnimator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickRotationAnimator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def direction(self) -> RotationDirection:
    """
    Calls Qt's 'RotationDirection QQuickRotationAnimator::direction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimator.html#direction

    Returns
    -------

    RotationDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'RotationDirection(number)' gives.
    """
    #  RotationDirection QQuickRotationAnimator::direction() const
    return QQuickRotationAnimator.RotationDirection(self.uglySide.call(
        'ritual_ZNK22QQuickRotationAnimator9directionEv',
    ))

  def createJob(self) -> Optional[QQuickAnimatorJob]:
    """
    Calls Qt's 'QQuickAnimatorJob *QQuickRotationAnimator::createJob()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimator.html#createJob

    Returns
    -------

    Optional[QQuickAnimatorJob]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimatorJob *QQuickRotationAnimator::createJob() const
    ritual = 'ritual_ZNK22QQuickRotationAnimator9createJobEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickRotationAnimator9createJobEv'
    address = self.uglySide.call(ritual)
    from . import QQuickAnimatorJob
    return QQuickAnimatorJob._cuteAt(address)

  def propertyName(self) -> str:
    """
    Calls Qt's 'QString QQuickRotationAnimator::propertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimator.html#propertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickRotationAnimator::propertyName() const
    ritual = 'ritual_ZNK22QQuickRotationAnimator12propertyNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QQuickRotationAnimator12propertyNameEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(RotationDirection)
  def setDirection(self, dir: RotationDirection) -> None:
    """
    Calls Qt's 'void QQuickRotationAnimator::setDirection(RotationDirection
    dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimator.html#setDirection

    Parameters
    ----------

    dir : RotationDirection
      Passed on as its number.
    """
    #  void QQuickRotationAnimator::setDirection(RotationDirection dir)
    self.uglySide.call(
        'ritual_ZN22QQuickRotationAnimator12setDirectionENS_17RotationDirec'
        'tionE',
        dir.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickRotationAnimator::QQuickRotationAnimator(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimator.html#QQuickRotationAnimator

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRotationAnimator::QQuickRotationAnimator(QObject *parent)
    self._noteCreation(QQuickRotationAnimator, lambda: Rituals.call(
        'ritual_ZN22QQuickRotationAnimatorC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QQuickRotationAnimatorPrivate]:
    """
    Calls Qt's 'QQuickRotationAnimatorPrivate
    *QQuickRotationAnimator::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrotationanimator.html#d_func

    Returns
    -------

    Optional[QQuickRotationAnimatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRotationAnimatorPrivate *QQuickRotationAnimator::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QQuickRotationAnimator6d_funcEv',
    )
    from . import QQuickRotationAnimatorPrivate
    return QQuickRotationAnimatorPrivate._cuteAt(address)

  @overload(RotationDirection)
  def directionChanged(self, dir: RotationDirection) -> None:
    """
    Calls Qt's 'void
    QQuickRotationAnimator::directionChanged(QQuickRotationAnimator::
    RotationDirection dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimator.html#directionChanged

    Parameters
    ----------

    dir : RotationDirection
      Passed on as its number.
    """
    #  void QQuickRotationAnimator::directionChanged(QQuickRotationAnimator::
    #      RotationDirection dir)
    self.uglySide.call(
        'ritual_ZN22QQuickRotationAnimator16directionChangedENS_17RotationD'
        'irectionE',
        dir.value,
    )
