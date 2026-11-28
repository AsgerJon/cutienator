"""
QQmlDebugStatesDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldebugstatesdelegate_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlDebugStatesDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDebugStatesDelegate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlDebugStatesDelegate: a plain Python object
  standing in front of one C++ QQmlDebugStatesDelegate.

  What exists
  -----------

  Every function of Qt's QQmlDebugStatesDelegate that has a ritual and that
  Python can call so far, 2 names in all: 'setBindingForInvalidProperty',
  'resetBindingForInvalidProperty'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDebugStatesDelegate::~QQmlDebugStatesDelegate()': the
    destructor: Python never removes a C++ QQmlDebugStatesDelegate.
  - Qt's 'void QQmlDebugStatesDelegate::buildStatesList(bool cleanList, const
    QList<QPointer<QObject>> &instances)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlDebugStatesDelegate::updateBinding(QQmlContext *context,
    const QQmlProperty &property, const QVariant &expression, bool
    isLiteralValue, const QString &fileName, int line, int column, bool
    *inBaseState)': takes a number to change where it is.

  What has no ritual
  ------------------

  3 of the 8 functions Qt declares: 2 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QQmlDebugStatesDelegate is created at the first use, not by
    'QQmlDebugStatesDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDebugStatesDelegate.
  - Each name of Qt's QQmlDebugStatesDelegate that has no cute function yet,
    '__init__', 'buildStatesList', 'updateBinding', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDebugStatesDelegate'

  #  A C++ QQmlDebugStatesDelegate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDebugStatesDelegate'

  #  The functions Qt calls itself that QQmlDebugStatesDelegate is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'buildStatesList': (
          'void QQmlDebugStatesDelegate::buildStatesList(bool, const '
          'QList<QPointer<QObject>> &)',
      ),
      'updateBinding': (
          'void QQmlDebugStatesDelegate::updateBinding(QQmlContext *, '
          'const QQmlProperty &, const QVariant &, bool, const QString &, '
          'int, int, bool *)',
      ),
  }

  #  The functions Qt calls itself that QQmlDebugStatesDelegate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setBindingForInvalidProperty': (
          ('_ZN23QQmlDebugStatesDelegate28setBindingForInvalidPropertyEP7QO'
           'bjectRK7QStringRK8QVariantb',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
               ('bool', 'number', ''),
           )),
      ),
      'resetBindingForInvalidProperty': (
          ('_ZN23QQmlDebugStatesDelegate30resetBindingForInvalidPropertyEP7'
           'QObjectRK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
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

  @overload(QObject, str, QVariant, bool)
  @overload(NoneType, str, QVariant, bool)
  def setBindingForInvalidProperty(
      self,
      object: Optional[QObject],
      propertyName: str,
      expression: QVariant,
      isLiteralValue: bool,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlDebugStatesDelegate::setBindingForInvalidProperty(QObject *object,
    const QString &propertyName, const QVariant &expression, bool
    isLiteralValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugstatesdelegate.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    expression : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    isLiteralValue : bool
      Passed on as it is.
    """
    #  bool QQmlDebugStatesDelegate::setBindingForInvalidProperty(QObject
    #      *object, const QString &propertyName, const QVariant &expression,
    #      bool isLiteralValue)
    return self.uglySide.call(
        'ritual_ZN23QQmlDebugStatesDelegate28setBindingForInvalidPropertyEP'
        '7QObjectRK7QStringRK8QVariantb',
        self._addressOf(object, 'QObject'), propertyName,
        self._valueOf(expression), isLiteralValue,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlDebugStatesDelegate::QQmlDebugStatesDelegate()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QQmlDebugStatesDelegate.__init__' has no cute function yet. Qt's "
        "'QQmlDebugStatesDelegate::QQmlDebugStatesDelegate()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  @overload(QObject, str)
  @overload(NoneType, str)
  def resetBindingForInvalidProperty(
      self,
      object: Optional[QObject],
      propertyName: str,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlDebugStatesDelegate::resetBindingForInvalidProperty(QObject *object,
    const QString &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugstatesdelegate.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDebugStatesDelegate::resetBindingForInvalidProperty(QObject
    #      *object, const QString &propertyName)
    self.uglySide.call(
        'ritual_ZN23QQmlDebugStatesDelegate30resetBindingForInvalidProperty'
        'EP7QObjectRK7QString',
        self._addressOf(object, 'QObject'), propertyName,
    )

  @staticmethod
  def buildStatesList(*__, **_) -> Never:
    """
    Qt's 'void QQmlDebugStatesDelegate::buildStatesList(bool cleanList, const
    QList<QPointer<QObject>> &instances)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDebugStatesDelegate.buildStatesList' has no cute function "
        "yet. Qt's 'void QQmlDebugStatesDelegate::buildStatesList(bool "
        "cleanList, const QList<QPointer<QObject>> &instances)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def updateBinding(*__, **_) -> Never:
    """
    Qt's 'void QQmlDebugStatesDelegate::updateBinding(QQmlContext *context,
    const QQmlProperty &property, const QVariant &expression, bool
    isLiteralValue, const QString &fileName, int line, int column, bool
    *inBaseState)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlDebugStatesDelegate.updateBinding' has no cute function yet. "
        "Qt's 'void QQmlDebugStatesDelegate::updateBinding(QQmlContext "
        "*context, const QQmlProperty &property, const QVariant "
        "&expression, bool isLiteralValue, const QString &fileName, int "
        "line, int column, bool *inBaseState)': takes a number to change "
        "where it is.")
