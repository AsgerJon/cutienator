"""
QPropertyChangeTrigger binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPropertyChangeTrigger to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QPropertyObserver

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaProperty, QUntypedPropertyData
  from . import QQmlJavaScriptExpression
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJavaScriptExpression = WAIT['QQmlJavaScriptExpression']
  QUntypedPropertyData = WAIT['QUntypedPropertyData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPropertyChangeTrigger(QPropertyObserver):
  """
  The cute side of Qt's QPropertyChangeTrigger: a plain Python object
  standing in front of one C++ QPropertyChangeTrigger.

  It is built on the cute 'QPropertyObserver', as Qt's QPropertyChangeTrigger
  is built on Qt's QPropertyObserver, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPropertyChangeTrigger that has a ritual and that
  Python can call so far, 2 names in all: 'trigger', 'property'. It can be
  made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  4 of the 7 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QPropertyChangeTrigger is created at the first use, not by
    'QPropertyChangeTrigger(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPropertyChangeTrigger.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPropertyObserver, QUntypedPropertyData)
  @overload(QPropertyObserver, NoneType)
  @overload(NoneType, QUntypedPropertyData)
  @overload(NoneType, NoneType)
  def trigger(
      a0: Optional[QPropertyObserver],
      a1: Optional[QUntypedPropertyData],
  ) -> None:
    """
    Calls Qt's 'void QPropertyChangeTrigger::trigger(QPropertyObserver *a0,
    QUntypedPropertyData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertychangetrigger.html#trigger

    Parameters
    ----------

    a0 : Optional[QPropertyObserver]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QUntypedPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPropertyChangeTrigger::trigger(QPropertyObserver *a0,
    #      QUntypedPropertyData *a1)
    Rituals.call(
        'ritual_ZN22QPropertyChangeTrigger7triggerEP17QPropertyObserverP20Q'
        'UntypedPropertyData',
        CuteMixin._addressOf(a0), CuteMixin._addressOf(a1),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPropertyChangeTrigger'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def property(self) -> QMetaProperty:
    """
    Calls Qt's 'QMetaProperty QPropertyChangeTrigger::property() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertychangetrigger.html#property

    Returns
    -------

    QMetaProperty
      A new cute QMetaProperty around the copy Qt gave back. Python owns it.
    """
    #  QMetaProperty QPropertyChangeTrigger::property() const
    address = self.uglySide.call(
        'ritual_ZNK22QPropertyChangeTrigger8propertyEv',
    )
    from ..QtCore import QMetaProperty
    return QMetaProperty._cuteOwning(address)

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

  @overload(QQmlJavaScriptExpression)
  @overload(NoneType)
  def __init__(self, expression: Optional[QQmlJavaScriptExpression]) -> None:
    """
    Notes what was given, for Qt's
    'QPropertyChangeTrigger::QPropertyChangeTrigger(QQmlJavaScriptExpression
    *expression)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpropertychangetrigger.html#QPropertyChangeTrigger

    Parameters
    ----------

    expression : Optional[QQmlJavaScriptExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPropertyChangeTrigger::QPropertyChangeTrigger(
    #      QQmlJavaScriptExpression *expression)
    self._noteCreation(QPropertyChangeTrigger, lambda: Rituals.call(
        'ritual_ZN22QPropertyChangeTriggerC1EP24QQmlJavaScriptExpression',
        self._addressOf(expression, 'QQmlJavaScriptExpression'),
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
