"""
QScrollbarStyleAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QScrollbarStyleAnimation to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from . import QNumberStyleAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScrollbarStyleAnimation(QNumberStyleAnimation):
  """
  The cute side of Qt's QScrollbarStyleAnimation: a plain Python object
  standing in front of one C++ QScrollbarStyleAnimation.

  It is built on the cute 'QNumberStyleAnimation', as Qt's
  QScrollbarStyleAnimation is built on Qt's QNumberStyleAnimation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QScrollbarStyleAnimation that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'mode',
  'wasActive', 'setActive', 'updateCurrentTime'. It can be made from Python,
  in 1 way; see '__init__'.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QScrollbarStyleAnimation is created at the first use, not by
    'QScrollbarStyleAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScrollbarStyleAnimation.
  - Qt tells when it has removed the C++ QScrollbarStyleAnimation. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QScrollbarStyleAnimation, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Mode(CuteNum):
    """
    The enum 'QScrollbarStyleAnimation::Mode' of Qt, with the 2 names Qt
    gives in it.
    """

    Activating = Kee[int](0)
    Deactivating = Kee[int](1)

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
    Calls Qt's 'QString QScrollbarStyleAnimation::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbarstyleanimation.html#tr

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
    #  QString QScrollbarStyleAnimation::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QScrollbarStyleAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScrollbarStyleAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScrollbarStyleAnimation::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarstyleanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScrollbarStyleAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QScrollbarStyleAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mode(self) -> Mode:
    """
    Calls Qt's 'Mode QScrollbarStyleAnimation::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscrollbarstyleanimation.html#mode

    Returns
    -------

    Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mode(number)' gives.
    """
    #  Mode QScrollbarStyleAnimation::mode() const
    return QScrollbarStyleAnimation.Mode(self.uglySide.call(
        'ritual_ZNK24QScrollbarStyleAnimation4modeEv',
    ))

  def wasActive(self) -> bool:
    """
    Calls Qt's 'bool QScrollbarStyleAnimation::wasActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarstyleanimation.html#wasActive
    """
    #  bool QScrollbarStyleAnimation::wasActive() const
    return self.uglySide.call(
        'ritual_ZNK24QScrollbarStyleAnimation9wasActiveEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QScrollbarStyleAnimation::setActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarstyleanimation.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QScrollbarStyleAnimation::setActive(bool active)
    self.uglySide.call(
        'ritual_ZN24QScrollbarStyleAnimation9setActiveEb', active,
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

  @overload(Mode, QObject)
  @overload(Mode, NoneType)
  def __init__(self, mode: Mode, target: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QScrollbarStyleAnimation::QScrollbarStyleAnimation(Mode mode, QObject
    *target)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarstyleanimation.html

    Parameters
    ----------

    mode : Mode
      Passed on as its number.

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScrollbarStyleAnimation::QScrollbarStyleAnimation(Mode mode, QObject
    #      *target)
    self._noteCreation(QScrollbarStyleAnimation, lambda: Rituals.call(
        'ritual_ZN24QScrollbarStyleAnimationC1ENS_4ModeEP7QObject',
        mode.value, self._addressOf(target, 'QObject'),
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

  @overload(int)
  def updateCurrentTime(self, time: int) -> None:
    """
    Calls Qt's 'void QScrollbarStyleAnimation::updateCurrentTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollbarstyleanimation.html#updateCurrentTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QScrollbarStyleAnimation::updateCurrentTime(int time)
    ritual = 'ritual_ZN24QScrollbarStyleAnimation17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QScrollbarStyleAnimation17updateCurrentTimeEi'
    self.uglySide.call(ritual, time)
