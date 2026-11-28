"""
QTouch3DInputHandlerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qtouch3dinputhandler_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QTouch3DInputHandlerPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import Q3DInputHandlerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class QTouch3DInputHandlerPrivate(Q3DInputHandlerPrivate):
  """
  The cute side of Qt's QTouch3DInputHandlerPrivate: a plain Python object
  standing in front of one C++ QTouch3DInputHandlerPrivate.

  It is built on the cute 'Q3DInputHandlerPrivate', as Qt's
  QTouch3DInputHandlerPrivate is built on Qt's Q3DInputHandlerPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QTouch3DInputHandlerPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'metaObject',
  'handlePinchZoom', 'handleTapAndHold'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTouch3DInputHandlerPrivate::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QTouch3DInputHandlerPrivate::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QTouch3DInputHandlerPrivate::~QTouch3DInputHandlerPrivate()': the
    destructor: Python never removes a C++ QTouch3DInputHandlerPrivate.

  What has no ritual
  ------------------

  6 of the 12 functions Qt declares: 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 2
  leans on 'QTouch3DInputHandlerPrivate.

  What to expect
  --------------

  - The C++ QTouch3DInputHandlerPrivate is created at the first use, not by
    'QTouch3DInputHandlerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTouch3DInputHandlerPrivate.
  - Qt tells when it has removed the C++ QTouch3DInputHandlerPrivate. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QTouch3DInputHandlerPrivate that has no cute function
    yet, '__init__', 'handleRotation', 'handleSelection', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTouch3DInputHandlerPrivate'

  #  A C++ QTouch3DInputHandlerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTouch3DInputHandlerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTouch3DInputHandlerPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtouch3dinputhandlerprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTouch3DInputHandlerPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QTouch3DInputHandlerPrivate10metaObjectEv',
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
    Qt's 'QTouch3DInputHandlerPrivate::QTouch3DInputHandlerPrivate(
    QTouch3DInputHandler *q)': leans on
    'QTouch3DInputHandlerPrivate::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTouch3DInputHandlerPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QTouch3DInputHandlerPrivate::QTouch3DInputHandlerPrivate(QTouch3DI"
        "nputHandler *q)': leans on "
        "'QTouch3DInputHandlerPrivate::qt_metacall(QMetaObject::Call, int, "
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

  @overload(float, QPoint)
  def handlePinchZoom(self, distance: float, pos: QPoint) -> None:
    """
    Calls Qt's 'void QTouch3DInputHandlerPrivate::handlePinchZoom(float
    distance, const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtouch3dinputhandlerprivate.html#handlePinchZoom

    Parameters
    ----------

    distance : float
      Passed on as it is.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QTouch3DInputHandlerPrivate::handlePinchZoom(float distance,
    #      const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN27QTouch3DInputHandlerPrivate15handlePinchZoomEfRK6QPoint',
        distance, self._valueOf(pos),
    )

  def handleTapAndHold(self) -> None:
    """
    Calls Qt's 'void QTouch3DInputHandlerPrivate::handleTapAndHold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtouch3dinputhandlerprivate.html#handleTapAndHold
    """
    #  void QTouch3DInputHandlerPrivate::handleTapAndHold()
    self.uglySide.call(
        'ritual_ZN27QTouch3DInputHandlerPrivate16handleTapAndHoldEv',
    )

  @staticmethod
  def handleRotation(*__, **_) -> Never:
    """
    Qt's 'void QTouch3DInputHandlerPrivate::handleRotation(const QPointF
    &position)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    't3ihRotationSpeed'.
    """
    raise NotImplementedError(
        "'QTouch3DInputHandlerPrivate.handleRotation' has no cute function "
        "yet. Qt's 'void QTouch3DInputHandlerPrivate::handleRotation(const "
        "QPointF &position)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 't3ihRotationSpeed'.")

  @staticmethod
  def handleSelection(*__, **_) -> Never:
    """
    Qt's 'void QTouch3DInputHandlerPrivate::handleSelection(const QPointF
    &position)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'maxSelectionJitter'.
    """
    raise NotImplementedError(
        "'QTouch3DInputHandlerPrivate.handleSelection' has no cute function "
        "yet. Qt's 'void QTouch3DInputHandlerPrivate::handleSelection(const "
        "QPointF &position)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'maxSelectionJitter'.")
