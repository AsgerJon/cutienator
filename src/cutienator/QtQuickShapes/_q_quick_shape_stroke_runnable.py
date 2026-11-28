"""
QQuickShapeStrokeRunnable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickShapeStrokeRunnable to be private: it declares the class in
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


class QQuickShapeStrokeRunnable(QObject, QRunnable):
  """
  The cute side of Qt's QQuickShapeStrokeRunnable: a plain Python object
  standing in front of one C++ QQuickShapeStrokeRunnable.

  It is built on the cute 'QObject', as Qt's QQuickShapeStrokeRunnable is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QRunnable' as well, as Qt's QQuickShapeStrokeRunnable is built on
  Qt's QRunnable too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickShapeStrokeRunnable that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'run', 'done'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShapeStrokeRunnable::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickShapeStrokeRunnable::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickShapeStrokeRunnable.

  What to expect
  --------------

  - The C++ QQuickShapeStrokeRunnable is created at the first use, not by
    'QQuickShapeStrokeRunnable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapeStrokeRunnable.
  - Qt tells when it has removed the C++ QQuickShapeStrokeRunnable. Every
    call on the cute object, and every use of it as an argument, then raises
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
  __qt_class__ = 'QQuickShapeStrokeRunnable'

  #  Qt's QQuickShapeStrokeRunnable is built on more than one class. The part
  #  of a C++ QQuickShapeStrokeRunnable that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QRunnable': 'ritual_cast_QQuickShapeStrokeRunnable_QRunnable',
  }

  #  A C++ QQuickShapeStrokeRunnable Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShapeStrokeRunnable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickShapeStrokeRunnable::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapestrokerunnable.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShapeStrokeRunnable::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickShapeStrokeRunnable10metaObjectEv',
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
    Calls Qt's 'void QQuickShapeStrokeRunnable::run()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapestrokerunnable.html#run
    """
    #  void QQuickShapeStrokeRunnable::run()
    self.uglySide.call('ritual_ZN25QQuickShapeStrokeRunnable3runEv')

  @overload(THIS)
  @overload(NoneType)
  def done(self, self_: Optional[QQuickShapeStrokeRunnable]) -> None:
    """
    Calls Qt's 'void
    QQuickShapeStrokeRunnable::done(QQuickShapeStrokeRunnable *self_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapestrokerunnable.html#done

    Parameters
    ----------

    self_ : Optional[QQuickShapeStrokeRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapeStrokeRunnable::done(QQuickShapeStrokeRunnable *self_)
    self.uglySide.call(
        'ritual_ZN25QQuickShapeStrokeRunnable4doneEPS_',
        self._addressOf(self_),
    )
