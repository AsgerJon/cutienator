"""
QQuickDesignerSupportStates binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdesignersupportstates_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickDesignerSupportStates to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QObject, QVariant
  from ..QtQml import QQmlContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDesignerSupportStates(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickDesignerSupportStates: a plain Python object
  standing in front of one C++ QQuickDesignerSupportStates.

  C++ hands a QQuickDesignerSupportStates around as a copy, so every C++
  QQuickDesignerSupportStates behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickDesignerSupportStates that has a ritual and
  that Python can call so far, 6 names in all: 'isStateActive',
  'activateState', 'deactivateState', 'changeValueInRevertList',
  'updateStateBinding', 'resetStateProperty'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickDesignerSupportStates::~QQuickDesignerSupportStates()': the
    destructor: Python removes its C++ QQuickDesignerSupportStates by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQuickDesignerSupportStates is created at the first use, not by
    'QQuickDesignerSupportStates(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDesignerSupportStates back gives a copy the
    ritual made for Python, in a new cute QQuickDesignerSupportStates.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject, QQmlContext)
  @overload(QObject, NoneType)
  @overload(NoneType, QQmlContext)
  @overload(NoneType, NoneType)
  def isStateActive(
      object: Optional[QObject],
      context: Optional[QQmlContext],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupportStates::isStateActive(QObject
    *object, QQmlContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportstates.html#isStateActive

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDesignerSupportStates::isStateActive(QObject *object,
    #      QQmlContext *context)
    return Rituals.call(
        'ritual_ZN27QQuickDesignerSupportStates13isStateActiveEP7QObjectP11'
        'QQmlContext',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(context),
    )

  @staticmethod
  @overload(QObject, QQmlContext)
  @overload(QObject, NoneType)
  @overload(NoneType, QQmlContext)
  @overload(NoneType, NoneType)
  def activateState(
      object: Optional[QObject],
      context: Optional[QQmlContext],
  ) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupportStates::activateState(QObject
    *object, QQmlContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportstates.html#activateState

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportStates::activateState(QObject *object,
    #      QQmlContext *context)
    Rituals.call(
        'ritual_ZN27QQuickDesignerSupportStates13activateStateEP7QObjectP11'
        'QQmlContext',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(context),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def deactivateState(object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupportStates::deactivateState(QObject
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportstates.html#deactivateState

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportStates::deactivateState(QObject *object)
    Rituals.call(
        'ritual_ZN27QQuickDesignerSupportStates15deactivateStateEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(QObject, QObject, QByteArray, QVariant)
  @overload(QObject, NoneType, QByteArray, QVariant)
  @overload(NoneType, QObject, QByteArray, QVariant)
  @overload(NoneType, NoneType, QByteArray, QVariant)
  def changeValueInRevertList(
      state: Optional[QObject],
      target: Optional[QObject],
      propertyName: QByteArray,
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickDesignerSupportStates::changeValueInRevertList(QObject *state,
    QObject *target, const QQuickDesignerSupport::PropertyName &propertyName,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportstates.html

    Parameters
    ----------

    state : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQuickDesignerSupportStates::changeValueInRevertList(QObject
    #      *state, QObject *target, const QQuickDesignerSupport::PropertyName
    #      &propertyName, const QVariant &value)
    return Rituals.call(
        'ritual_ZN27QQuickDesignerSupportStates23changeValueInRevertListEP7'
        'QObjectS1_RK10QByteArrayRK8QVariant',
        CuteMixin._addressOf(state, 'QObject'), CuteMixin._addressOf(target,
        'QObject'), CuteMixin._valueOf(propertyName),
        CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(QObject, QObject, QByteArray, str)
  @overload(QObject, NoneType, QByteArray, str)
  @overload(NoneType, QObject, QByteArray, str)
  @overload(NoneType, NoneType, QByteArray, str)
  def updateStateBinding(
      state: Optional[QObject],
      target: Optional[QObject],
      propertyName: QByteArray,
      expression: str,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupportStates::updateStateBinding(QObject
    *state, QObject *target, const QQuickDesignerSupport::PropertyName
    &propertyName, const QString &expression)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportstates.html

    Parameters
    ----------

    state : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    expression : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickDesignerSupportStates::updateStateBinding(QObject *state,
    #      QObject *target, const QQuickDesignerSupport::PropertyName
    #      &propertyName, const QString &expression)
    return Rituals.call(
        'ritual_ZN27QQuickDesignerSupportStates18updateStateBindingEP7QObje'
        'ctS1_RK10QByteArrayRK7QString',
        CuteMixin._addressOf(state, 'QObject'), CuteMixin._addressOf(target,
        'QObject'), CuteMixin._valueOf(propertyName), expression,
    )

  @staticmethod
  @overload(QObject, QObject, QByteArray, QVariant)
  @overload(QObject, NoneType, QByteArray, QVariant)
  @overload(NoneType, QObject, QByteArray, QVariant)
  @overload(NoneType, NoneType, QByteArray, QVariant)
  def resetStateProperty(
      state: Optional[QObject],
      target: Optional[QObject],
      propertyName: QByteArray,
      a3: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupportStates::resetStateProperty(QObject
    *state, QObject *target, const QQuickDesignerSupport::PropertyName
    &propertyName, const QVariant &a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportstates.html

    Parameters
    ----------

    state : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    a3 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQuickDesignerSupportStates::resetStateProperty(QObject *state,
    #      QObject *target, const QQuickDesignerSupport::PropertyName
    #      &propertyName, const QVariant &a3)
    return Rituals.call(
        'ritual_ZN27QQuickDesignerSupportStates18resetStatePropertyEP7QObje'
        'ctS1_RK10QByteArrayRK8QVariant',
        CuteMixin._addressOf(state, 'QObject'), CuteMixin._addressOf(target,
        'QObject'), CuteMixin._valueOf(propertyName), CuteMixin._valueOf(a3),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDesignerSupportStates'

  #  Qt's '~QQuickDesignerSupportStates()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickDesignerSupportStates behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QQuickDesignerSupportStatesD1Ev'

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
