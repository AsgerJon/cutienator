"""
QQmlPropertyBindingJS binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertybinding_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlPropertyBindingJS to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQmlJavaScriptExpression

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQmlPropertyBinding


class QQmlPropertyBindingJS(QQmlJavaScriptExpression):
  """
  The cute side of Qt's QQmlPropertyBindingJS: a plain Python object standing
  in front of one C++ QQmlPropertyBindingJS.

  It is built on the cute 'QQmlJavaScriptExpression', as Qt's
  QQmlPropertyBindingJS is built on Qt's QQmlJavaScriptExpression, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlPropertyBindingJS that has a ritual and that
  Python can call so far, 3 names in all: 'mustCaptureBindableProperty',
  'expressionChanged', 'asBinding'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlPropertyBinding *QQmlPropertyBindingJS::asBinding()
    const': takes in Python what 'QQmlPropertyBinding
    *QQmlPropertyBindingJS::asBinding()' takes.

  What to expect
  --------------

  - The C++ QQmlPropertyBindingJS is created at the first use, not by
    'QQmlPropertyBindingJS(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPropertyBindingJS.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyBindingJS'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def mustCaptureBindableProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyBindingJS::mustCaptureBindableProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingjs.html
    """
    #  bool QQmlPropertyBindingJS::mustCaptureBindableProperty() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlPropertyBindingJS27mustCaptureBindablePropertyEv',
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

  def expressionChanged(self) -> None:
    """
    Calls Qt's 'void QQmlPropertyBindingJS::expressionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingjs.html#expressionChanged
    """
    #  void QQmlPropertyBindingJS::expressionChanged()
    ritual = 'ritual_ZN21QQmlPropertyBindingJS17expressionChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQmlPropertyBindingJS17expressionChangedEv'
    self.uglySide.call(ritual)

  def asBinding(self) -> Optional[QQmlPropertyBinding]:
    """
    Calls Qt's 'QQmlPropertyBinding *QQmlPropertyBindingJS::asBinding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertybindingjs.html#asBinding

    Returns
    -------

    Optional[QQmlPropertyBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlPropertyBinding *QQmlPropertyBindingJS::asBinding()
    address = self.uglySide.call(
        'ritual_ZN21QQmlPropertyBindingJS9asBindingEv',
    )
    from . import QQmlPropertyBinding
    return QQmlPropertyBinding._cuteAt(address)
