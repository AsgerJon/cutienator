"""
QQuickSmoothedAnimationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickSmoothedAnimationPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQuickPropertyAnimationPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickSmoothedAnimation


class QQuickSmoothedAnimationPrivate(QQuickPropertyAnimationPrivate):
  """
  The cute side of Qt's QQuickSmoothedAnimationPrivate: a plain Python object
  standing in front of one C++ QQuickSmoothedAnimationPrivate.

  It is built on the cute 'QQuickPropertyAnimationPrivate', as Qt's
  QQuickSmoothedAnimationPrivate is built on Qt's
  QQuickPropertyAnimationPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSmoothedAnimationPrivate that has a ritual and
  that Python can call so far, 2 names in all: 'q_func',
  'updateRunningAnimations'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickSmoothedAnimation
    *QQuickSmoothedAnimationPrivate::q_func() const': takes in Python what
    'QQuickSmoothedAnimation *QQuickSmoothedAnimationPrivate::q_func()'
    takes.
  - Qt's 'QQuickSmoothedAnimationPrivate::~QQuickSmoothedAnimationPrivate()':
    the destructor: Python never removes a C++
    QQuickSmoothedAnimationPrivate.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'vtable for
  QSmoothedAnimationTimer', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickSmoothedAnimationPrivate is created at the first use, not
    by 'QQuickSmoothedAnimationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSmoothedAnimationPrivate.
  - Each name of Qt's QQuickSmoothedAnimationPrivate that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSmoothedAnimationPrivate'

  #  A C++ QQuickSmoothedAnimationPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSmoothedAnimationPrivate'

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
    Qt's 'QQuickSmoothedAnimationPrivate::QQuickSmoothedAnimationPrivate()':
    leans on 'vtable for QSmoothedAnimationTimer', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickSmoothedAnimationPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickSmoothedAnimationPrivate::QQuickSmoothedAnimationPrivate()':"
        " leans on 'vtable for QSmoothedAnimationTimer', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  def q_func(self) -> Optional[QQuickSmoothedAnimation]:
    """
    Calls Qt's 'QQuickSmoothedAnimation
    *QQuickSmoothedAnimationPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimationprivate.html#q_func

    Returns
    -------

    Optional[QQuickSmoothedAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSmoothedAnimation *QQuickSmoothedAnimationPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QQuickSmoothedAnimationPrivate6q_funcEv',
    )
    from . import QQuickSmoothedAnimation
    return QQuickSmoothedAnimation._cuteAt(address)

  def updateRunningAnimations(self) -> None:
    """
    Calls Qt's 'void
    QQuickSmoothedAnimationPrivate::updateRunningAnimations()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksmoothedanimationprivate.html
    """
    #  void QQuickSmoothedAnimationPrivate::updateRunningAnimations()
    self.uglySide.call(
        'ritual_ZN30QQuickSmoothedAnimationPrivate23updateRunningAnimations'
        'Ev',
    )
