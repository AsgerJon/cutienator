"""
QSequentialAnimationGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsequentialanimationgroup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QAbstractAnimation, QAnimationGroup, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject, QPauseAnimation

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSequentialAnimationGroup(QAnimationGroup):
  """
  The cute side of Qt's QSequentialAnimationGroup: a plain Python object
  standing in front of one C++ QSequentialAnimationGroup.

  It is built on the cute 'QAnimationGroup', as Qt's
  QSequentialAnimationGroup is built on Qt's QAnimationGroup, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSequentialAnimationGroup that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'addPause',
  'insertPause', 'currentAnimation', 'duration'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSequentialAnimationGroup::~QSequentialAnimationGroup()': the
    destructor: Python never removes a C++ QSequentialAnimationGroup.

  What has no ritual
  ------------------

  15 of the 23 functions Qt declares: 5 protected; 3 takes or gives a type
  that cannot be passed yet; 3 private; 2 forbidden; 1 a template; 1 a
  signal.

  What to expect
  --------------

  - The C++ QSequentialAnimationGroup is created at the first use, not by
    'QSequentialAnimationGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSequentialAnimationGroup.
  - Qt tells when it has removed the C++ QSequentialAnimationGroup. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QSequentialAnimationGroup::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsequentialanimationgroup.html#tr

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
    #  QString QSequentialAnimationGroup::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QSequentialAnimationGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSequentialAnimationGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSequentialAnimationGroup::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSequentialAnimationGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QSequentialAnimationGroup10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentAnimation(self) -> Optional[QAbstractAnimation]:
    """
    Calls Qt's 'QAbstractAnimation
    *QSequentialAnimationGroup::currentAnimation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#currentAnimation

    Returns
    -------

    Optional[QAbstractAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimation *QSequentialAnimationGroup::currentAnimation()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QSequentialAnimationGroup16currentAnimationEv',
    )
    return QAbstractAnimation._cuteAt(address)

  def duration(self) -> int:
    """
    Calls Qt's 'int QSequentialAnimationGroup::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#duration
    """
    #  int QSequentialAnimationGroup::duration() const
    return self.uglySide.call(
        'ritual_ZNK25QSequentialAnimationGroup8durationEv',
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QSequentialAnimationGroup::QSequentialAnimationGroup(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSequentialAnimationGroup::QSequentialAnimationGroup(QObject *parent)
    self._noteCreation(QSequentialAnimationGroup, lambda: Rituals.call(
        'ritual_ZN25QSequentialAnimationGroupC1EP7QObject',
        self._addressOf(parent),
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
  def addPause(self, msecs: int) -> Optional[QPauseAnimation]:
    """
    Calls Qt's 'QPauseAnimation *QSequentialAnimationGroup::addPause(int
    msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#addPause

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    Returns
    -------

    Optional[QPauseAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPauseAnimation *QSequentialAnimationGroup::addPause(int msecs)
    address = self.uglySide.call(
        'ritual_ZN25QSequentialAnimationGroup8addPauseEi', msecs,
    )
    from . import QPauseAnimation
    return QPauseAnimation._cuteAt(address)

  @overload(int, int)
  def insertPause(self, index: int, msecs: int) -> Optional[QPauseAnimation]:
    """
    Calls Qt's 'QPauseAnimation *QSequentialAnimationGroup::insertPause(int
    index, int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroup.html#insertPause

    Parameters
    ----------

    index : int
      Passed on as it is.

    msecs : int
      Passed on as it is.

    Returns
    -------

    Optional[QPauseAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPauseAnimation *QSequentialAnimationGroup::insertPause(int index, int
    #      msecs)
    address = self.uglySide.call(
        'ritual_ZN25QSequentialAnimationGroup11insertPauseEii', index, msecs,
    )
    from . import QPauseAnimation
    return QPauseAnimation._cuteAt(address)
