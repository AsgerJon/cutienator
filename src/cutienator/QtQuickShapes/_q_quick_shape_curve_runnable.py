"""
QQuickShapeCurveRunnable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapecurverenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickShapeCurveRunnable to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..QtCore import QObject, QRunnable

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapeCurveRunnable(QObject, QRunnable):
  """
  The cute side of Qt's QQuickShapeCurveRunnable: a plain Python object
  standing in front of one C++ QQuickShapeCurveRunnable.

  It is built on the cute 'QObject', as Qt's QQuickShapeCurveRunnable is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QRunnable' as well, as Qt's QQuickShapeCurveRunnable is built on
  Qt's QRunnable too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickShapeCurveRunnable that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'run', 'done'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShapeCurveRunnable::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickShapeCurveRunnable::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickShapeCurveRunnable::~QQuickShapeCurveRunnable()': the
    destructor: Python never removes a C++ QQuickShapeCurveRunnable.

  What has no ritual
  ------------------

  3 of the 9 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickShapeCurveRunnable.

  What to expect
  --------------

  - The C++ QQuickShapeCurveRunnable is created at the first use, not by
    'QQuickShapeCurveRunnable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapeCurveRunnable.
  - Qt tells when it has removed the C++ QQuickShapeCurveRunnable. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapeCurveRunnable'

  #  Qt's QQuickShapeCurveRunnable is built on more than one class. The part
  #  of a C++ QQuickShapeCurveRunnable that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QRunnable': 'ritual_cast_QQuickShapeCurveRunnable_QRunnable',
  }

  #  A C++ QQuickShapeCurveRunnable Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShapeCurveRunnable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickShapeCurveRunnable::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapecurverunnable.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShapeCurveRunnable::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickShapeCurveRunnable10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  def run(self) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRunnable::run()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapecurverunnable.html#run
    """
    #  void QQuickShapeCurveRunnable::run()
    self.uglySide.call('ritual_ZN24QQuickShapeCurveRunnable3runEv')

  @overload(THIS)
  @overload(NoneType)
  def done(self, self_: Optional[QQuickShapeCurveRunnable]) -> None:
    """
    Calls Qt's 'void QQuickShapeCurveRunnable::done(QQuickShapeCurveRunnable
    *self_)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapecurverunnable.html#done

    Parameters
    ----------

    self_ : Optional[QQuickShapeCurveRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeCurveRunnable::done(QQuickShapeCurveRunnable *self_)
    self.uglySide.call(
        'ritual_ZN24QQuickShapeCurveRunnable4doneEPS_',
        self._addressOf(self_),
    )
