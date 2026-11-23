"""
QSwipeGesture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QGesture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSwipeGesture(QGesture):
  """
  The cute side of Qt's QSwipeGesture: a plain Python object standing in
  front of one C++ QSwipeGesture.

  It is built on the cute 'QGesture', as Qt's QSwipeGesture is built on Qt's
  QGesture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSwipeGesture that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'horizontalDirection',
  'verticalDirection', 'swipeAngle', 'setSwipeAngle'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSwipeGesture::~QSwipeGesture()': the destructor: Python never
    removes a C++ QSwipeGesture.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QSwipeGesture is created at the first use, not by
    'QSwipeGesture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSwipeGesture.
  - Qt tells when it has removed the C++ QSwipeGesture. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QSwipeGesture, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class SwipeDirection(CuteNum):
    """
    The enum 'QSwipeGesture::SwipeDirection' of Qt, with the 5 names Qt gives
    in it.
    """

    NoDirection = Kee[int](0)
    Left = Kee[int](1)
    Right = Kee[int](2)
    Up = Kee[int](3)
    Down = Kee[int](4)

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
    Calls Qt's 'QString QSwipeGesture::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qswipegesture.html#tr

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
    #  QString QSwipeGesture::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QSwipeGesture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSwipeGesture'

  #  A C++ QSwipeGesture Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSwipeGesture'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSwipeGesture::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qswipegesture.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSwipeGesture::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QSwipeGesture10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def horizontalDirection(self) -> SwipeDirection:
    """
    Calls Qt's 'SwipeDirection QSwipeGesture::horizontalDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qswipegesture.html#horizontalDirection

    Returns
    -------

    SwipeDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SwipeDirection(number)'
      gives.
    """
    #  SwipeDirection QSwipeGesture::horizontalDirection() const
    return QSwipeGesture.SwipeDirection(self.uglySide.call(
        'ritual_ZNK13QSwipeGesture19horizontalDirectionEv',
    ))

  def verticalDirection(self) -> SwipeDirection:
    """
    Calls Qt's 'SwipeDirection QSwipeGesture::verticalDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qswipegesture.html#verticalDirection

    Returns
    -------

    SwipeDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SwipeDirection(number)'
      gives.
    """
    #  SwipeDirection QSwipeGesture::verticalDirection() const
    return QSwipeGesture.SwipeDirection(self.uglySide.call(
        'ritual_ZNK13QSwipeGesture17verticalDirectionEv',
    ))

  def swipeAngle(self) -> float:
    """
    Calls Qt's 'qreal QSwipeGesture::swipeAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qswipegesture.html#swipeAngle
    """
    #  qreal QSwipeGesture::swipeAngle() const
    return self.uglySide.call('ritual_ZNK13QSwipeGesture10swipeAngleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSwipeAngle(self, value: float) -> None:
    """
    Calls Qt's 'void QSwipeGesture::setSwipeAngle(qreal value)'.

    Qt's own words: https://doc.qt.io/qt-6/qswipegesture.html#setSwipeAngle

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QSwipeGesture::setSwipeAngle(qreal value)
    self.uglySide.call('ritual_ZN13QSwipeGesture13setSwipeAngleEd', value)

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
    Notes what was given, for Qt's 'QSwipeGesture::QSwipeGesture(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qswipegesture.html#QSwipeGesture

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSwipeGesture::QSwipeGesture(QObject *parent)
    self._noteCreation(QSwipeGesture, lambda: Rituals.call(
        'ritual_ZN13QSwipeGestureC1EP7QObject', self._addressOf(parent),
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
