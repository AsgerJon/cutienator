"""
QAnimationGroupPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qanimationgroup_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QAnimationGroupPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstractAnimationPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractAnimation, QAnimationGroup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAnimation = WAIT['QAbstractAnimation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAnimationGroupPrivate(QAbstractAnimationPrivate):
  """
  The cute side of Qt's QAnimationGroupPrivate: a plain Python object
  standing in front of one C++ QAnimationGroupPrivate.

  It is built on the cute 'QAbstractAnimationPrivate', as Qt's
  QAnimationGroupPrivate is built on Qt's QAbstractAnimationPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAnimationGroupPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'animationInsertedAt',
  'animationRemoved', 'clear', 'disconnectUncontrolledAnimation',
  'connectUncontrolledAnimation'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAnimationGroup *QAnimationGroupPrivate::q_func() const':
    takes in Python what 'QAnimationGroup *QAnimationGroupPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QAnimationGroupPrivate is created at the first use, not by
    'QAnimationGroupPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAnimationGroupPrivate.
  - Each name of Qt's QAnimationGroupPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QAnimationGroupPrivate'

  #  The functions Qt calls itself that QAnimationGroupPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'animationInsertedAt': (
          ('_ZN22QAnimationGroupPrivate19animationInsertedAtEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'animationRemoved': (
          ('_ZN22QAnimationGroupPrivate16animationRemovedExP18QAbstractAnim'
           'ation',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
               ('address', 'address', 'QtCore:QAbstractAnimation'),
           )),
      ),
  }

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAnimationGroupPrivate::QAnimationGroupPrivate()': the compiler
    refuses its ritual as it would be written here: cannot initialize return
    object of type 'QAnimationGroupPrivate *' with an rvalue of type
    'CuteQAnimationGroupPrivate *'.
    """
    raise NotImplementedError(
        "'QAnimationGroupPrivate.__init__' has no cute function yet. Qt's "
        "'QAnimationGroupPrivate::QAnimationGroupPrivate()': the compiler "
        "refuses its ritual as it would be written here: cannot initialize "
        "return object of type 'QAnimationGroupPrivate *' with an rvalue of "
        "type 'CuteQAnimationGroupPrivate *'.")

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

  def q_func(self) -> Optional[QAnimationGroup]:
    """
    Calls Qt's 'QAnimationGroup *QAnimationGroupPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationgroupprivate.html#q_func

    Returns
    -------

    Optional[QAnimationGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationGroup *QAnimationGroupPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QAnimationGroupPrivate6q_funcEv',
    )
    from . import QAnimationGroup
    return QAnimationGroup._cuteAt(address)

  @overload(int)
  def animationInsertedAt(self, a0: int) -> None:
    """
    Calls Qt's 'void QAnimationGroupPrivate::animationInsertedAt(qsizetype
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupprivate.html#animationInsertedAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAnimationGroupPrivate::animationInsertedAt(qsizetype a0)
    ritual = 'ritual_ZN22QAnimationGroupPrivate19animationInsertedAtEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QAnimationGroupPrivate19animationInsertedAtEx'
    self.uglySide.call(ritual, a0)

  @overload(int, QAbstractAnimation)
  @overload(int, NoneType)
  def animationRemoved(
      self,
      a0: int,
      a1: Optional[QAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void QAnimationGroupPrivate::animationRemoved(qsizetype a0,
    QAbstractAnimation *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupprivate.html#animationRemoved

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupPrivate::animationRemoved(qsizetype a0,
    #      QAbstractAnimation *a1)
    ritual = (
        'ritual_ZN22QAnimationGroupPrivate16animationRemovedExP18QAbstractA'
        'nimation')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QAnimationGroupPrivate16animationRemovedExP18QAbs'
          'tractAnimation')
    self.uglySide.call(ritual, a0, self._addressOf(a1))

  @overload(bool)
  def clear(self, onDestruction: bool) -> None:
    """
    Calls Qt's 'void QAnimationGroupPrivate::clear(bool onDestruction)'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationgroupprivate.html#clear

    Parameters
    ----------

    onDestruction : bool
      Passed on as it is.
    """
    #  void QAnimationGroupPrivate::clear(bool onDestruction)
    self.uglySide.call(
        'ritual_ZN22QAnimationGroupPrivate5clearEb', onDestruction,
    )

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def disconnectUncontrolledAnimation(
      self,
      anim: Optional[QAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void QAnimationGroupPrivate::disconnectUncontrolledAnimation(
    QAbstractAnimation *anim)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupprivate.html

    Parameters
    ----------

    anim : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupPrivate::disconnectUncontrolledAnimation(
    #      QAbstractAnimation *anim)
    self.uglySide.call(
        'ritual_ZN22QAnimationGroupPrivate31disconnectUncontrolledAnimation'
        'EP18QAbstractAnimation',
        self._addressOf(anim),
    )

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def connectUncontrolledAnimation(
      self,
      anim: Optional[QAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationGroupPrivate::connectUncontrolledAnimation(QAbstractAnimation
    *anim)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationgroupprivate.html

    Parameters
    ----------

    anim : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationGroupPrivate::connectUncontrolledAnimation(
    #      QAbstractAnimation *anim)
    self.uglySide.call(
        'ritual_ZN22QAnimationGroupPrivate28connectUncontrolledAnimationEP1'
        '8QAbstractAnimation',
        self._addressOf(anim),
    )
