"""
QAnimationGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qanimationgroup.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from . import QAbstractAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAnimationGroup(QAbstractAnimation):
  """
  The cute side of Qt's QAnimationGroup: a plain Python object standing in
  front of one C++ QAnimationGroup.

  It is built on the cute 'QAbstractAnimation', as Qt's QAnimationGroup is
  built on Qt's QAbstractAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAnimationGroup that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'animationAt',
  'animationCount', 'indexOfAnimation', 'addAnimation', 'insertAnimation',
  'removeAnimation', 'takeAnimation', 'clear'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAnimationGroup::~QAnimationGroup()': the destructor: Python never
    removes a C++ QAnimationGroup.

  What has no ritual
  ------------------

  11 of the 22 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 protected; 2 forbidden; 1 a template; 1 the class
  is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QAnimationGroup is created at the first use, not by
    'QAnimationGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAnimationGroup.
  - Qt tells when it has removed the C++ QAnimationGroup. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QAnimationGroup::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationgroup.html#tr

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
    #  QString QAnimationGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QAnimationGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAnimationGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAnimationGroup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAnimationGroup::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QAnimationGroup10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def animationAt(self, index: int) -> Optional[QAbstractAnimation]:
    """
    Calls Qt's 'QAbstractAnimation *QAnimationGroup::animationAt(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationgroup.html#animationAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QAbstractAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimation *QAnimationGroup::animationAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK15QAnimationGroup11animationAtEi', index,
    )
    return QAbstractAnimation._cuteAt(address)

  def animationCount(self) -> int:
    """
    Calls Qt's 'int QAnimationGroup::animationCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroup.html#animationCount
    """
    #  int QAnimationGroup::animationCount() const
    return self.uglySide.call(
        'ritual_ZNK15QAnimationGroup14animationCountEv',
    )

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def indexOfAnimation(self, animation: Optional[QAbstractAnimation]) -> int:
    """
    Calls Qt's 'int QAnimationGroup::indexOfAnimation(QAbstractAnimation
    *animation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroup.html#indexOfAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAnimationGroup::indexOfAnimation(QAbstractAnimation *animation)
    #      const
    return self.uglySide.call(
        'ritual_ZNK15QAnimationGroup16indexOfAnimationEP18QAbstractAnimatio'
        'n',
        self._addressOf(animation),
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

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def addAnimation(self, animation: Optional[QAbstractAnimation]) -> None:
    """
    Calls Qt's 'void QAnimationGroup::addAnimation(QAbstractAnimation
    *animation)'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationgroup.html#addAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroup::addAnimation(QAbstractAnimation *animation)
    self.uglySide.call(
        'ritual_ZN15QAnimationGroup12addAnimationEP18QAbstractAnimation',
        self._addressOf(animation),
    )

  @overload(int, QAbstractAnimation)
  @overload(int, NoneType)
  def insertAnimation(
      self,
      index: int,
      animation: Optional[QAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void QAnimationGroup::insertAnimation(int index,
    QAbstractAnimation *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroup.html#insertAnimation

    Parameters
    ----------

    index : int
      Passed on as it is.

    animation : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroup::insertAnimation(int index, QAbstractAnimation
    #      *animation)
    self.uglySide.call(
        'ritual_ZN15QAnimationGroup15insertAnimationEiP18QAbstractAnimation',
        index, self._addressOf(animation),
    )

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def removeAnimation(self, animation: Optional[QAbstractAnimation]) -> None:
    """
    Calls Qt's 'void QAnimationGroup::removeAnimation(QAbstractAnimation
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroup.html#removeAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroup::removeAnimation(QAbstractAnimation *animation)
    self.uglySide.call(
        'ritual_ZN15QAnimationGroup15removeAnimationEP18QAbstractAnimation',
        self._addressOf(animation),
    )

  @overload(int)
  def takeAnimation(self, index: int) -> Optional[QAbstractAnimation]:
    """
    Calls Qt's 'QAbstractAnimation *QAnimationGroup::takeAnimation(int
    index)'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationgroup.html#takeAnimation

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QAbstractAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimation *QAnimationGroup::takeAnimation(int index)
    address = self.uglySide.call(
        'ritual_ZN15QAnimationGroup13takeAnimationEi', index,
    )
    return QAbstractAnimation._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QAnimationGroup::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationgroup.html#clear
    """
    #  void QAnimationGroup::clear()
    self.uglySide.call('ritual_ZN15QAnimationGroup5clearEv')
