"""
QQuickGeoCoordinateAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioningQuick/6.12.0/QtPositioningQuick/private/qquickgeocoordinateanimation_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickGeoCoordinateAnimation to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick import QQuickPropertyAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtPositioning import QGeoCoordinate
  from . import QQuickGeoCoordinateAnimationPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGeoCoordinateAnimation(QQuickPropertyAnimation):
  """
  The cute side of Qt's QQuickGeoCoordinateAnimation: a plain Python object
  standing in front of one C++ QQuickGeoCoordinateAnimation.

  It is built on the cute 'QQuickPropertyAnimation', as Qt's
  QQuickGeoCoordinateAnimation is built on Qt's QQuickPropertyAnimation, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGeoCoordinateAnimation that has a ritual and
  that Python can call so far, 10 names in all: 'metaObject', 'tr', 'd_func',
  'from_', 'setFrom', 'to', 'setTo', 'direction', 'setDirection',
  'directionChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGeoCoordinateAnimation::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickGeoCoordinateAnimation::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickGeoCoordinateAnimationPrivate
    *QQuickGeoCoordinateAnimation::d_func() const': takes in Python what
    'QQuickGeoCoordinateAnimationPrivate
    *QQuickGeoCoordinateAnimation::d_func()' takes.
  - Qt's 'QQuickGeoCoordinateAnimation::~QQuickGeoCoordinateAnimation()': the
    destructor: Python never removes a C++ QQuickGeoCoordinateAnimation.
  - Qt's 'QBindable<Direction>
    QQuickGeoCoordinateAnimation::bindableDirection()': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickGeoCoordinateAnimation is created at the first use, not by
    'QQuickGeoCoordinateAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGeoCoordinateAnimation.
  - Qt tells when it has removed the C++ QQuickGeoCoordinateAnimation. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGeoCoordinateAnimation that has no cute function
    yet, 'bindableDirection', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickGeoCoordinateAnimation, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Direction(CuteNum):
    """
    The enum 'QQuickGeoCoordinateAnimation::Direction' of Qt, with the 3
    names Qt gives in it.
    """

    Shortest = Kee[int](0)
    West = Kee[int](1)
    East = Kee[int](2)

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
    Calls Qt's 'QString QQuickGeoCoordinateAnimation::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html#tr

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
    #  QString QQuickGeoCoordinateAnimation::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QQuickGeoCoordinateAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGeoCoordinateAnimation'

  #  A C++ QQuickGeoCoordinateAnimation Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGeoCoordinateAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGeoCoordinateAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGeoCoordinateAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickGeoCoordinateAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def from_(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QQuickGeoCoordinateAnimation::from() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html#from

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QQuickGeoCoordinateAnimation::from() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickGeoCoordinateAnimation4fromEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def to(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QQuickGeoCoordinateAnimation::to() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html#to

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QQuickGeoCoordinateAnimation::to() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickGeoCoordinateAnimation2toEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def direction(self) -> Direction:
    """
    Calls Qt's 'Direction QQuickGeoCoordinateAnimation::direction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html#direction

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  Direction QQuickGeoCoordinateAnimation::direction() const
    return QQuickGeoCoordinateAnimation.Direction(self.uglySide.call(
        'ritual_ZNK28QQuickGeoCoordinateAnimation9directionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoCoordinate)
  def setFrom(self, a0: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QQuickGeoCoordinateAnimation::setFrom(const
    QGeoCoordinate &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html#setFrom

    Parameters
    ----------

    a0 : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QQuickGeoCoordinateAnimation::setFrom(const QGeoCoordinate &a0)
    self.uglySide.call(
        'ritual_ZN28QQuickGeoCoordinateAnimation7setFromERK14QGeoCoordinate',
        self._valueOf(a0),
    )

  @overload(QGeoCoordinate)
  def setTo(self, a0: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QQuickGeoCoordinateAnimation::setTo(const QGeoCoordinate
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html#setTo

    Parameters
    ----------

    a0 : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QQuickGeoCoordinateAnimation::setTo(const QGeoCoordinate &a0)
    self.uglySide.call(
        'ritual_ZN28QQuickGeoCoordinateAnimation5setToERK14QGeoCoordinate',
        self._valueOf(a0),
    )

  @overload(Direction)
  def setDirection(self, direction: Direction) -> None:
    """
    Calls Qt's 'void QQuickGeoCoordinateAnimation::setDirection(Direction
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html#setDirection

    Parameters
    ----------

    direction : Direction
      Passed on as its number.
    """
    #  void QQuickGeoCoordinateAnimation::setDirection(Direction direction)
    self.uglySide.call(
        'ritual_ZN28QQuickGeoCoordinateAnimation12setDirectionENS_9Directio'
        'nE',
        direction.value,
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
    'QQuickGeoCoordinateAnimation::QQuickGeoCoordinateAnimation(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickGeoCoordinateAnimation::QQuickGeoCoordinateAnimation(QObject
    #      *parent)
    self._noteCreation(QQuickGeoCoordinateAnimation, lambda: Rituals.call(
        'ritual_ZN28QQuickGeoCoordinateAnimationC1EP7QObject',
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

  def d_func(self) -> Optional[QQuickGeoCoordinateAnimationPrivate]:
    """
    Calls Qt's 'QQuickGeoCoordinateAnimationPrivate
    *QQuickGeoCoordinateAnimation::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html#d_func

    Returns
    -------

    Optional[QQuickGeoCoordinateAnimationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGeoCoordinateAnimationPrivate
    #      *QQuickGeoCoordinateAnimation::d_func()
    address = self.uglySide.call(
        'ritual_ZN28QQuickGeoCoordinateAnimation6d_funcEv',
    )
    from . import QQuickGeoCoordinateAnimationPrivate
    return QQuickGeoCoordinateAnimationPrivate._cuteAt(address)

  def directionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickGeoCoordinateAnimation::directionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgeocoordinateanimation.html#directionChanged
    """
    #  void QQuickGeoCoordinateAnimation::directionChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickGeoCoordinateAnimation16directionChangedEv',
    )

  @staticmethod
  def bindableDirection(*__, **_) -> Never:
    """
    Qt's 'QBindable<Direction>
    QQuickGeoCoordinateAnimation::bindableDirection()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickGeoCoordinateAnimation.bindableDirection' has no cute "
        "function yet. Qt's 'QBindable<Direction> "
        "QQuickGeoCoordinateAnimation::bindableDirection()': gives a type "
        "Python has no way to take yet.")
