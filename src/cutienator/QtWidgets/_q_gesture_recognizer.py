"""
QGestureRecognizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgesturerecognizer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

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


class QGestureRecognizer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGestureRecognizer: a plain Python object standing in
  front of one C++ QGestureRecognizer.

  What exists
  -----------

  Every function of Qt's QGestureRecognizer that has a ritual and that Python
  can call so far, 5 names in all: 'create', 'recognize', 'reset',
  'registerRecognizer', 'unregisterRecognizer'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGestureRecognizer::~QGestureRecognizer()': the destructor: Python
    never removes a C++ QGestureRecognizer.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one.

  What to expect
  --------------

  - The C++ QGestureRecognizer is created at the first use, not by
    'QGestureRecognizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGestureRecognizer.
  """

  #  The enums Qt writes inside QGestureRecognizer, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ResultFlag(CuteFlags):
    """
    The flags enum 'QGestureRecognizer::ResultFlag' of Qt, with the 8 names
    Qt gives in it. Qt names the type of its combinations
    'QGestureRecognizer::Result'.
    """

    Ignore = 0x1
    MayBeGesture = 0x2
    TriggerGesture = 0x4
    FinishGesture = 0x8
    CancelGesture = 0x10
    ResultState_Mask = 0xff
    ConsumeEventHint = 0x100
    ResultHint_Mask = 0xff00

  Result = ResultFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS)
  @overload(NoneType)
  def registerRecognizer(
      recognizer: Optional[QGestureRecognizer],
  ) -> Qt.GestureType:
    """
    Calls Qt's 'Qt::GestureType
    QGestureRecognizer::registerRecognizer(QGestureRecognizer *recognizer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgesturerecognizer.html#registerRecognizer

    Parameters
    ----------

    recognizer : Optional[QGestureRecognizer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.GestureType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.GestureType(number)'
      gives.
    """
    #  Qt::GestureType
    #      QGestureRecognizer::registerRecognizer(QGestureRecognizer
    #      *recognizer)
    return Qt.GestureType(Rituals.call(
        'ritual_ZN18QGestureRecognizer18registerRecognizerEPS_',
        CuteMixin._addressOf(recognizer),
    ))

  @staticmethod
  @overload(Qt.GestureType)
  def unregisterRecognizer(type: Qt.GestureType) -> None:
    """
    Calls Qt's 'void QGestureRecognizer::unregisterRecognizer(Qt::GestureType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgesturerecognizer.html#unregisterRecognizer

    Parameters
    ----------

    type : Qt.GestureType
      Passed on as its number.
    """
    #  void QGestureRecognizer::unregisterRecognizer(Qt::GestureType type)
    Rituals.call(
        'ritual_ZN18QGestureRecognizer20unregisterRecognizerEN2Qt11GestureT'
        'ypeE',
        type.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGestureRecognizer'

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
    Calls Qt's 'QGesture *QGestureRecognizer::create(QObject *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qgesturerecognizer.html#create

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
    #  QGesture *QGestureRecognizer::create(QObject *target)
    address = self.uglySide.call(
        'ritual_ZN18QGestureRecognizer6createEP7QObject',
        self._addressOf(target),
    )
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
  ) -> Result:
    """
    Calls Qt's 'Result QGestureRecognizer::recognize(QGesture *state, QObject
    *watched, QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgesturerecognizer.html#recognize

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

    Result
      The value standing for the combination Qt gave back.
    """
    #  Result QGestureRecognizer::recognize(QGesture *state, QObject
    #      *watched, QEvent *event)
    return QGestureRecognizer.Result(self.uglySide.call(
        'ritual_ZN18QGestureRecognizer9recognizeEP8QGestureP7QObjectP6QEven'
        't',
        self._addressOf(state), self._addressOf(watched),
        self._addressOf(event),
    ))

  @overload(QGesture)
  @overload(NoneType)
  def reset(self, state: Optional[QGesture]) -> None:
    """
    Calls Qt's 'void QGestureRecognizer::reset(QGesture *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qgesturerecognizer.html#reset

    Parameters
    ----------

    state : Optional[QGesture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGestureRecognizer::reset(QGesture *state)
    self.uglySide.call(
        'ritual_ZN18QGestureRecognizer5resetEP8QGesture',
        self._addressOf(state),
    )
