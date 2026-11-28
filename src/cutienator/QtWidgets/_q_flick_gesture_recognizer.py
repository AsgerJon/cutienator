"""
QFlickGestureRecognizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qflickgesture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFlickGestureRecognizer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QGestureRecognizer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QObject
  from . import QGesture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QGesture = WAIT['QGesture']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFlickGestureRecognizer(QGestureRecognizer):
  """
  The cute side of Qt's QFlickGestureRecognizer: a plain Python object
  standing in front of one C++ QFlickGestureRecognizer.

  It is built on the cute 'QGestureRecognizer', as Qt's
  QFlickGestureRecognizer is built on Qt's QGestureRecognizer, and has
  everything that class has.

  C++ hands a QFlickGestureRecognizer around as a copy, so every C++
  QFlickGestureRecognizer behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFlickGestureRecognizer that has a ritual and that
  Python can call so far, 3 names in all: 'create', 'recognize', 'reset'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFlickGestureRecognizer::~QFlickGestureRecognizer()': the
    destructor: Python removes its C++ QFlickGestureRecognizer by it, and has
    no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'QFlickGestureRecognizer.

  What to expect
  --------------

  - The C++ QFlickGestureRecognizer is created at the first use, not by
    'QFlickGestureRecognizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFlickGestureRecognizer back gives a copy the ritual
    made for Python, in a new cute QFlickGestureRecognizer.
  - Each name of Qt's QFlickGestureRecognizer that has no cute function yet,
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
  __qt_class__ = 'QFlickGestureRecognizer'

  #  Qt's '~QFlickGestureRecognizer()'. Naming it makes this a value class:
  #  Python owns every C++ QFlickGestureRecognizer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QFlickGestureRecognizerD1Ev'

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
    Qt's 'QFlickGestureRecognizer::QFlickGestureRecognizer(Qt::MouseButton
    button)': leans on 'QFlickGestureRecognizer::recognize(QGesture*,
    QObject*, QEvent*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QFlickGestureRecognizer.__init__' has no cute function yet. Qt's "
        "'QFlickGestureRecognizer::QFlickGestureRecognizer(Qt::MouseButton "
        "button)': leans on 'QFlickGestureRecognizer::recognize(QGesture*, "
        "QObject*, QEvent*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QObject)
  @overload(NoneType)
  def create(self, target: Optional[QObject]) -> Optional[QGesture]:
    """
    Calls Qt's 'QGesture *QFlickGestureRecognizer::create(QObject *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qflickgesturerecognizer.html#create

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGesture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGesture *QFlickGestureRecognizer::create(QObject *target)
    ritual = 'ritual_ZN23QFlickGestureRecognizer6createEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QFlickGestureRecognizer6createEP7QObject'
    address = self.uglySide.call(ritual, self._addressOf(target, 'QObject'))
    from . import QGesture
    return QGesture._cuteAt(address)

  @overload(QGesture, QObject, QEvent)
  @overload(QGesture, QObject, NoneType)
  @overload(QGesture, NoneType, QEvent)
  @overload(QGesture, NoneType, NoneType)
  @overload(NoneType, QObject, QEvent)
  @overload(NoneType, QObject, NoneType)
  @overload(NoneType, NoneType, QEvent)
  @overload(NoneType, NoneType, NoneType)
  def recognize(
      self,
      state: Optional[QGesture],
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> QGestureRecognizer.Result:
    """
    Calls Qt's 'QGestureRecognizer::Result
    QFlickGestureRecognizer::recognize(QGesture *state, QObject *watched,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qflickgesturerecognizer.html#recognize

    Parameters
    ----------

    state : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QGestureRecognizer.Result
      The value standing for the combination Qt gave back.
    """
    #  QGestureRecognizer::Result QFlickGestureRecognizer::recognize(QGesture
    #      *state, QObject *watched, QEvent *event)
    return QGestureRecognizer.Result(self.uglySide.call(
        'ritual_ZN23QFlickGestureRecognizer9recognizeEP8QGestureP7QObjectP6'
        'QEvent',
        self._addressOf(state), self._addressOf(watched, 'QObject'),
        self._addressOf(event),
    ))

  @overload(QGesture)
  @overload(NoneType)
  def reset(self, state: Optional[QGesture]) -> None:
    """
    Calls Qt's 'void QFlickGestureRecognizer::reset(QGesture *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qflickgesturerecognizer.html#reset

    Parameters
    ----------

    state : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFlickGestureRecognizer::reset(QGesture *state)
    ritual = 'ritual_ZN23QFlickGestureRecognizer5resetEP8QGesture'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QFlickGestureRecognizer5resetEP8QGesture'
    self.uglySide.call(ritual, self._addressOf(state))
