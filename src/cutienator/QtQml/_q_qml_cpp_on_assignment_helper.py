"""
QQmlCppOnAssignmentHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlcpponassignment_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlCppOnAssignmentHelper to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlProperty, QQmlPropertyValueInterceptor
  from . import QQmlPropertyValueSource
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlProperty = WAIT['QQmlProperty']
  QQmlPropertyValueInterceptor = WAIT['QQmlPropertyValueInterceptor']
  QQmlPropertyValueSource = WAIT['QQmlPropertyValueSource']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlCppOnAssignmentHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlCppOnAssignmentHelper: a plain Python object
  standing in front of one C++ QQmlCppOnAssignmentHelper.

  C++ hands a QQmlCppOnAssignmentHelper around as a copy, so every C++
  QQmlCppOnAssignmentHelper behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlCppOnAssignmentHelper that has a ritual and that
  Python can call so far, 1 name in all: 'set'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlCppOnAssignmentHelper::~QQmlCppOnAssignmentHelper()': the
    destructor: Python removes its C++ QQmlCppOnAssignmentHelper by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlCppOnAssignmentHelper is created at the first use, not by
    'QQmlCppOnAssignmentHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlCppOnAssignmentHelper back gives a copy the
    ritual made for Python, in a new cute QQmlCppOnAssignmentHelper.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlPropertyValueInterceptor, QQmlProperty)
  @overload(NoneType, QQmlProperty)
  def set(
      interceptor: Optional[QQmlPropertyValueInterceptor],
      property: QQmlProperty,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlCppOnAssignmentHelper::set(QQmlPropertyValueInterceptor *interceptor,
    const QQmlProperty &property)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcpponassignmenthelper.html#set

    Parameters
    ----------

    interceptor : Optional[QQmlPropertyValueInterceptor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQmlCppOnAssignmentHelper::set(QQmlPropertyValueInterceptor
    #      *interceptor, const QQmlProperty &property)
    Rituals.call(
        'ritual_ZN25QQmlCppOnAssignmentHelper3setEP28QQmlPropertyValueInter'
        'ceptorRK12QQmlProperty',
        CuteMixin._addressOf(interceptor, 'QQmlPropertyValueInterceptor'),
        CuteMixin._valueOf(property),
    )

  @staticmethod
  @overload(QQmlPropertyValueSource, QQmlProperty)
  def set(
      valueSource: Optional[QQmlPropertyValueSource],
      property: QQmlProperty,
  ) -> None:
    """
    Calls Qt's 'void QQmlCppOnAssignmentHelper::set(QQmlPropertyValueSource
    *valueSource, const QQmlProperty &property)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcpponassignmenthelper.html#set

    Parameters
    ----------

    valueSource : Optional[QQmlPropertyValueSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQmlCppOnAssignmentHelper::set(QQmlPropertyValueSource
    #      *valueSource, const QQmlProperty &property)
    Rituals.call(
        'ritual_ZN25QQmlCppOnAssignmentHelper3setEP23QQmlPropertyValueSourc'
        'eRK12QQmlProperty',
        CuteMixin._addressOf(valueSource, 'QQmlPropertyValueSource'),
        CuteMixin._valueOf(property),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlCppOnAssignmentHelper'

  #  Qt's '~QQmlCppOnAssignmentHelper()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlCppOnAssignmentHelper behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QQmlCppOnAssignmentHelperD1Ev'

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
