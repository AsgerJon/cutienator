"""
QQmlIncubatorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlincubator_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlIncubatorPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QQmlIncubator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlComponent, QQmlContext, RequiredProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQmlContext = WAIT['QQmlContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlIncubatorPrivate(QSharedData):
  """
  The cute side of Qt's QQmlIncubatorPrivate: a plain Python object standing
  in front of one C++ QQmlIncubatorPrivate.

  What exists
  -----------

  Every function of Qt's QQmlIncubatorPrivate that has a ritual and that
  Python can call so far, 7 names in all: 'get', 'calculateStatus',
  'changeStatus', 'clear', 'incubateCppBasedComponent', 'requiredProperties',
  'hadTopLevelRequiredProperties'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlIncubatorPrivate::~QQmlIncubatorPrivate()': the destructor:
    Python never removes a C++ QQmlIncubatorPrivate.
  - Qt's 'void
    QQmlIncubatorPrivate::forceCompletion(QQmlInstantiationInterrupt &i)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlIncubatorPrivate::incubate(QQmlInstantiationInterrupt
    &i)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlIncubatorPrivate is created at the first use, not by
    'QQmlIncubatorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlIncubatorPrivate.
  - Each name of Qt's QQmlIncubatorPrivate that has no cute function yet,
    'forceCompletion', 'incubate', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlIncubatorPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class HadTopLevelRequired(CuteNum):
    """
    The enum 'QQmlIncubatorPrivate::HadTopLevelRequired' of Qt, with the 2
    names Qt gives in it.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  class Progress(CuteNum):
    """
    The enum 'QQmlIncubatorPrivate::Progress' of Qt, with the 3 names Qt
    gives in it.
    """

    Execute = Kee[int](0)
    Completing = Kee[int](1)
    Completed = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlIncubator)
  @overload(NoneType)
  def get(
      incubator: Optional[QQmlIncubator],
  ) -> Optional[QQmlIncubatorPrivate]:
    """
    Calls Qt's 'QQmlIncubatorPrivate *QQmlIncubatorPrivate::get(QQmlIncubator
    *incubator)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubatorprivate.html#get

    Parameters
    ----------

    incubator : Optional[QQmlIncubator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlIncubatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlIncubatorPrivate *QQmlIncubatorPrivate::get(QQmlIncubator
    #      *incubator)
    address = Rituals.call(
        'ritual_ZN20QQmlIncubatorPrivate3getEP13QQmlIncubator',
        CuteMixin._addressOf(incubator),
    )
    return QQmlIncubatorPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlIncubatorPrivate'

  #  Qt's QQmlIncubatorPrivate is built on more than one class. The part of a
  #  C++ QQmlIncubatorPrivate that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QSharedData': 'ritual_cast_QQmlIncubatorPrivate_QSharedData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def calculateStatus(self) -> QQmlIncubator.Status:
    """
    Calls Qt's 'QQmlIncubator::Status QQmlIncubatorPrivate::calculateStatus()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubatorprivate.html#calculateStatus

    Returns
    -------

    QQmlIncubator.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlIncubator.Status(number)' gives.
    """
    #  QQmlIncubator::Status QQmlIncubatorPrivate::calculateStatus() const
    return QQmlIncubator.Status(self.uglySide.call(
        'ritual_ZNK20QQmlIncubatorPrivate15calculateStatusEv',
    ))

  def hadTopLevelRequiredProperties(self) -> bool:
    """
    Calls Qt's 'bool QQmlIncubatorPrivate::hadTopLevelRequiredProperties()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubatorprivate.html
    """
    #  bool QQmlIncubatorPrivate::hadTopLevelRequiredProperties() const
    return self.uglySide.call(
        'ritual_ZNK20QQmlIncubatorPrivate29hadTopLevelRequiredPropertiesEv',
    )

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

  @overload(QQmlIncubator, QQmlIncubator.IncubationMode)
  @overload(NoneType, QQmlIncubator.IncubationMode)
  def __init__(
      self,
      q: Optional[QQmlIncubator],
      m: QQmlIncubator.IncubationMode,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlIncubatorPrivate::QQmlIncubatorPrivate(QQmlIncubator *q,
    QQmlIncubator::IncubationMode m)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubatorprivate.html#QQmlIncubatorPrivate

    Parameters
    ----------

    q : Optional[QQmlIncubator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    m : QQmlIncubator.IncubationMode
      Passed on as its number.
    """
    #  QQmlIncubatorPrivate::QQmlIncubatorPrivate(QQmlIncubator *q,
    #      QQmlIncubator::IncubationMode m)
    self._noteCreation(QQmlIncubatorPrivate, lambda: Rituals.call(
        'ritual_ZN20QQmlIncubatorPrivateC1EP13QQmlIncubatorNS0_14Incubation'
        'ModeE',
        self._addressOf(q), m.value,
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

  @overload(QQmlIncubator.Status)
  def changeStatus(self, a0: QQmlIncubator.Status) -> None:
    """
    Calls Qt's 'void QQmlIncubatorPrivate::changeStatus(QQmlIncubator::Status
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubatorprivate.html#changeStatus

    Parameters
    ----------

    a0 : QQmlIncubator.Status
      Passed on as its number.
    """
    #  void QQmlIncubatorPrivate::changeStatus(QQmlIncubator::Status a0)
    self.uglySide.call(
        'ritual_ZN20QQmlIncubatorPrivate12changeStatusEN13QQmlIncubator6Sta'
        'tusE',
        a0.value,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlIncubatorPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlincubatorprivate.html#clear
    """
    #  void QQmlIncubatorPrivate::clear()
    self.uglySide.call('ritual_ZN20QQmlIncubatorPrivate5clearEv')

  @overload(QQmlComponent, QQmlContext)
  @overload(QQmlComponent, NoneType)
  @overload(NoneType, QQmlContext)
  @overload(NoneType, NoneType)
  def incubateCppBasedComponent(
      self,
      component: Optional[QQmlComponent],
      context: Optional[QQmlContext],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlIncubatorPrivate::incubateCppBasedComponent(QQmlComponent *component,
    QQmlContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubatorprivate.html

    Parameters
    ----------

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlIncubatorPrivate::incubateCppBasedComponent(QQmlComponent
    #      *component, QQmlContext *context)
    self.uglySide.call(
        'ritual_ZN20QQmlIncubatorPrivate25incubateCppBasedComponentEP13QQml'
        'ComponentP11QQmlContext',
        self._addressOf(component), self._addressOf(context),
    )

  def requiredProperties(self) -> Optional[RequiredProperties]:
    """
    Calls Qt's 'RequiredProperties
    *QQmlIncubatorPrivate::requiredProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlincubatorprivate.html#requiredProperties

    Returns
    -------

    Optional[RequiredProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RequiredProperties *QQmlIncubatorPrivate::requiredProperties()
    address = self.uglySide.call(
        'ritual_ZN20QQmlIncubatorPrivate18requiredPropertiesEv',
    )
    from . import RequiredProperties
    return RequiredProperties._cuteAt(address)

  @staticmethod
  def forceCompletion(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlIncubatorPrivate::forceCompletion(QQmlInstantiationInterrupt &i)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlIncubatorPrivate.forceCompletion' has no cute function yet. "
        "Qt's 'void "
        "QQmlIncubatorPrivate::forceCompletion(QQmlInstantiationInterrupt "
        "&i)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def incubate(*__, **_) -> Never:
    """
    Qt's 'void QQmlIncubatorPrivate::incubate(QQmlInstantiationInterrupt
    &i)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlIncubatorPrivate.incubate' has no cute function yet. Qt's "
        "'void QQmlIncubatorPrivate::incubate(QQmlInstantiationInterrupt "
        "&i)': takes a type Python has no way to hand over yet.")
