"""
QQmlPropertyValueInterceptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertyvalueinterceptor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlPropertyValueInterceptor to be private: it declares the class
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

  from ..QtCore import QUntypedBindable, QVariant
  from . import QQmlProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlProperty = WAIT['QQmlProperty']
  QUntypedBindable = WAIT['QUntypedBindable']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyValueInterceptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyValueInterceptor: a plain Python object
  standing in front of one C++ QQmlPropertyValueInterceptor.

  What exists
  -----------

  Every function of Qt's QQmlPropertyValueInterceptor that has a ritual and
  that Python can call so far, 3 names in all: 'setTarget', 'write',
  'bindable'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlPropertyValueInterceptor::~QQmlPropertyValueInterceptor()': the
    destructor: Python never removes a C++ QQmlPropertyValueInterceptor.

  What to expect
  --------------

  - The C++ QQmlPropertyValueInterceptor is created at the first use, not by
    'QQmlPropertyValueInterceptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPropertyValueInterceptor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyValueInterceptor'

  #  A C++ QQmlPropertyValueInterceptor Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlPropertyValueInterceptor'

  #  The functions Qt calls itself that QQmlPropertyValueInterceptor is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setTarget': (
          ('_ZN28QQmlPropertyValueInterceptor9setTargetERK12QQmlProperty',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtQml:QQmlProperty'),
           )),
      ),
      'write': (
          ('_ZN28QQmlPropertyValueInterceptor5writeERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'bindable': (
          ('_ZN28QQmlPropertyValueInterceptor8bindableEP16QUntypedBindableS'
           '0_',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QUntypedBindable'),
               ('address', 'value', 'QtCore:QUntypedBindable'),
           )),
      ),
  }

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

  @overload(QQmlProperty)
  def setTarget(self, property: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQmlPropertyValueInterceptor::setTarget(const
    QQmlProperty &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalueinterceptor.html#setTarget

    Parameters
    ----------

    property : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQmlPropertyValueInterceptor::setTarget(const QQmlProperty
    #      &property)
    self._callAs(
        'QQmlPropertyValueInterceptor',
        'ritual_ZN28QQmlPropertyValueInterceptor9setTargetERK12QQmlProperty',
        self._valueOf(property),
    )

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
    'QQmlPropertyValueInterceptor::QQmlPropertyValueInterceptor()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalueinterceptor.html
    """
    #  QQmlPropertyValueInterceptor::QQmlPropertyValueInterceptor()
    self._noteCreation(QQmlPropertyValueInterceptor, lambda: Rituals.call(
        'ritual_ZN28QQmlPropertyValueInterceptorC1Ev',
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

  @overload(QVariant)
  def write(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlPropertyValueInterceptor::write(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalueinterceptor.html#write

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlPropertyValueInterceptor::write(const QVariant &value)
    self._callAs(
        'QQmlPropertyValueInterceptor',
        'ritual_ZN28QQmlPropertyValueInterceptor5writeERK8QVariant',
        self._valueOf(value),
    )

  @overload(QUntypedBindable, QUntypedBindable)
  @overload(NoneType, QUntypedBindable)
  def bindable(
      self,
      bindable: Optional[QUntypedBindable],
      target: QUntypedBindable,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyValueInterceptor::bindable(QUntypedBindable
    *bindable, QUntypedBindable target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyvalueinterceptor.html#bindable

    Parameters
    ----------

    bindable : Optional[QUntypedBindable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : QUntypedBindable
      Passed on as a value: Qt reads the C++ QUntypedBindable, which stays
      Python's own.
    """
    #  bool QQmlPropertyValueInterceptor::bindable(QUntypedBindable
    #      *bindable, QUntypedBindable target)
    ritual = (
        'ritual_ZN28QQmlPropertyValueInterceptor8bindableEP16QUntypedBindab'
        'leS0_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQmlPropertyValueInterceptor8bindableEP16QUntyped'
          'BindableS0_')
    return self._callAs(
        'QQmlPropertyValueInterceptor', ritual,
        self._addressOf(bindable), self._valueOf(target),
    )
