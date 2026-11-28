"""
QWidgetAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidgetanimator_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QWidgetAnimator to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteNum
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QWidgetAnimator(QObject):
  """
  The cute side of Qt's QWidgetAnimator: a plain Python object standing in
  front of one C++ QWidgetAnimator.

  It is built on the cute 'QObject', as Qt's QWidgetAnimator is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetAnimator that has a ritual and that Python
  can call so far, 2 names in all: 'metaObject', 'animating'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWidgetAnimator::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWidgetAnimator::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 10 functions Qt declares: 2 not a gap; 2 leans on 'QToolBarLayout;
  1 leans on 'QWidgetAnimator; 1 leans on 'vtable for QWidgetAnimator', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QWidgetAnimator is created at the first use, not by
    'QWidgetAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetAnimator.
  - Qt tells when it has removed the C++ QWidgetAnimator. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWidgetAnimator that has no cute function yet,
    '__init__', 'abort', 'animate', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWidgetAnimator, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AnimationRule(CuteNum, scoped=True):
    """
    The enum 'QWidgetAnimator::AnimationRule' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Run = Kee[int](0)
    Stop = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetAnimator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWidgetAnimator::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetanimator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWidgetAnimator::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QWidgetAnimator10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def animating(self) -> bool:
    """
    Calls Qt's 'bool QWidgetAnimator::animating() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetanimator.html#animating
    """
    #  bool QWidgetAnimator::animating() const
    return self.uglySide.call('ritual_ZNK15QWidgetAnimator9animatingEv')

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
    Qt's 'QWidgetAnimator::QWidgetAnimator(QMainWindowLayout *layout)': leans
    on 'vtable for QWidgetAnimator', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWidgetAnimator.__init__' has no cute function yet. Qt's "
        "'QWidgetAnimator::QWidgetAnimator(QMainWindowLayout *layout)': "
        "leans on 'vtable for QWidgetAnimator', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @staticmethod
  def abort(*__, **_) -> Never:
    """
    Qt's 'void QWidgetAnimator::abort(QWidget *widget)': leans on
    'QToolBarLayout::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWidgetAnimator.abort' has no cute function yet. Qt's 'void "
        "QWidgetAnimator::abort(QWidget *widget)': leans on "
        "'QToolBarLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def animate(*__, **_) -> Never:
    """
    Qt's 'void QWidgetAnimator::animate(QWidget *widget, const QRect
    &final_geometry, AnimationRule rule)': leans on
    'QToolBarLayout::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QWidgetAnimator.animate' has no cute function yet. Qt's 'void "
        "QWidgetAnimator::animate(QWidget *widget, const QRect "
        "&final_geometry, AnimationRule rule)': leans on "
        "'QToolBarLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
