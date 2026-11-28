"""
QTapGestureRecognizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qstandardgestures_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QTapGestureRecognizer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QGestureRecognizer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

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


class QTapGestureRecognizer(QGestureRecognizer):
  """
  The cute side of Qt's QTapGestureRecognizer: a plain Python object standing
  in front of one C++ QTapGestureRecognizer.

  It is built on the cute 'QGestureRecognizer', as Qt's QTapGestureRecognizer
  is built on Qt's QGestureRecognizer, and has everything that class has.

  C++ hands a QTapGestureRecognizer around as a copy, so every C++
  QTapGestureRecognizer behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTapGestureRecognizer that has a ritual and that
  Python can call so far, 3 names in all: 'create', 'recognize', 'reset'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTapGestureRecognizer::~QTapGestureRecognizer()': the destructor:
    Python removes its C++ QTapGestureRecognizer by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QTapGestureRecognizer is created at the first use, not by
    'QTapGestureRecognizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTapGestureRecognizer back gives a copy the ritual
    made for Python, in a new cute QTapGestureRecognizer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTapGestureRecognizer'

  #  A C++ QTapGestureRecognizer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTapGestureRecognizer'

  #  Qt's '~QTapGestureRecognizer()'. Naming it makes this a value class:
  #  Python owns every C++ QTapGestureRecognizer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QTapGestureRecognizerD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QTapGestureRecognizer::QTapGestureRecognizer()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtapgesturerecognizer.html#QTapGestureRecognizer
    """
    #  QTapGestureRecognizer::QTapGestureRecognizer()
    self._noteCreation(QTapGestureRecognizer, lambda: Rituals.call(
        'ritual_ZN21QTapGestureRecognizerC1Ev',
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

  @overload(QObject)
  @overload(NoneType)
  def create(self, target: Optional[QObject]) -> Optional[QGesture]:
    """
    Calls Qt's 'QGesture *QTapGestureRecognizer::create(QObject *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qtapgesturerecognizer.html#create

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
    #  QGesture *QTapGestureRecognizer::create(QObject *target)
    ritual = 'ritual_ZN21QTapGestureRecognizer6createEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QTapGestureRecognizer6createEP7QObject'
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
    QTapGestureRecognizer::recognize(QGesture *state, QObject *watched,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtapgesturerecognizer.html#recognize

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
    #  QGestureRecognizer::Result QTapGestureRecognizer::recognize(QGesture
    #      *state, QObject *watched, QEvent *event)
    ritual = (
        'ritual_ZN21QTapGestureRecognizer9recognizeEP8QGestureP7QObjectP6QE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QTapGestureRecognizer9recognizeEP8QGestureP7QObje'
          'ctP6QEvent')
    return QGestureRecognizer.Result(self.uglySide.call(
        ritual,
        self._addressOf(state), self._addressOf(watched, 'QObject'),
        self._addressOf(event),
    ))

  @overload(QGesture)
  @overload(NoneType)
  def reset(self, state: Optional[QGesture]) -> None:
    """
    Calls Qt's 'void QTapGestureRecognizer::reset(QGesture *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qtapgesturerecognizer.html#reset

    Parameters
    ----------

    state : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTapGestureRecognizer::reset(QGesture *state)
    ritual = 'ritual_ZN21QTapGestureRecognizer5resetEP8QGesture'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QTapGestureRecognizer5resetEP8QGesture'
    self.uglySide.call(ritual, self._addressOf(state))
