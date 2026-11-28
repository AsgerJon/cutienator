"""
QQuickContext2DRenderThread binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcanvasitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickContext2DRenderThread to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QThread

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickContext2DRenderThread(QThread):
  """
  The cute side of Qt's QQuickContext2DRenderThread: a plain Python object
  standing in front of one C++ QQuickContext2DRenderThread.

  It is built on the cute 'QThread', as Qt's QQuickContext2DRenderThread is
  built on Qt's QThread, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickContext2DRenderThread that has a ritual and
  that Python can call so far, 1 name in all: 'metaObject'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickContext2DRenderThread::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickContext2DRenderThread::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickContext2DRenderThread::~QQuickContext2DRenderThread()': the
    destructor: Python never removes a C++ QQuickContext2DRenderThread.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 3 leans on 'QQuickContext2DRenderThread;
  2 not a gap.

  What to expect
  --------------

  - The C++ QQuickContext2DRenderThread is created at the first use, not by
    'QQuickContext2DRenderThread(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickContext2DRenderThread.
  - Qt tells when it has removed the C++ QQuickContext2DRenderThread. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickContext2DRenderThread that has no cute function
    yet, '__init__', 'instance', holds a function that raises
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
  __qt_class__ = 'QQuickContext2DRenderThread'

  #  A C++ QQuickContext2DRenderThread Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickContext2DRenderThread'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickContext2DRenderThread::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2drenderthread.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickContext2DRenderThread::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickContext2DRenderThread10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickContext2DRenderThread::QQuickContext2DRenderThread(QQmlEngine
    *eng)': leans on
    'QQuickContext2DRenderThread::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickContext2DRenderThread.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickContext2DRenderThread::QQuickContext2DRenderThread(QQmlEngin"
        "e *eng)': leans on "
        "'QQuickContext2DRenderThread::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
  def instance(*__, **_) -> Never:
    """
    Qt's 'QQuickContext2DRenderThread
    *QQuickContext2DRenderThread::instance(QQmlEngine *engine)': leans on
    'QQuickContext2DRenderThread::renderThreads', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickContext2DRenderThread.instance' has no cute function yet. "
        "Qt's 'QQuickContext2DRenderThread "
        "*QQuickContext2DRenderThread::instance(QQmlEngine *engine)': leans "
        "on 'QQuickContext2DRenderThread::renderThreads', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
