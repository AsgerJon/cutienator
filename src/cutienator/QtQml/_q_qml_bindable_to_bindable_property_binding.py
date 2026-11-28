"""
QQmlBindableToBindablePropertyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlBindableToBindablePropertyBinding to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQmlPropertyToBindablePropertyBinding

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMetaProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QMetaProperty = WAIT['QMetaProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlBindableToBindablePropertyBinding(QQmlPropertyToBindablePropertyBinding):
  """
  The cute side of Qt's QQmlBindableToBindablePropertyBinding: a plain Python
  object standing in front of one C++ QQmlBindableToBindablePropertyBinding.

  It is built on the cute 'QQmlPropertyToBindablePropertyBinding', as Qt's
  QQmlBindableToBindablePropertyBinding is built on Qt's
  QQmlPropertyToBindablePropertyBinding, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlBindableToBindablePropertyBinding that has a
  ritual and that Python can call so far, 1 name in all: 'captureProperty'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has no ritual
  ------------------

  1 of the 2 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQmlBindableToBindablePropertyBinding is created at the first
    use, not by 'QQmlBindableToBindablePropertyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlBindableToBindablePropertyBinding.
  - Each name of Qt's QQmlBindableToBindablePropertyBinding that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlBindableToBindablePropertyBinding'

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
    Qt's 'QQmlBindableToBindablePropertyBinding::
    QQmlBindableToBindablePropertyBinding(QQmlEngine *engine, const
    QQmlProperty &source, const QQmlProperty &target)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: template argument for non-type template parameter must be an
    expression.
    """
    raise NotImplementedError(
        "'QQmlBindableToBindablePropertyBinding.__init__' has no cute "
        "function yet. Qt's "
        "'QQmlBindableToBindablePropertyBinding::QQmlBindableToBindablePrope"
        "rtyBinding(QQmlEngine *engine, const QQmlProperty &source, const "
        "QQmlProperty &target)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: template "
        "argument for non-type template parameter must be an expression.")

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

  @overload(QMetaObject, QMetaProperty)
  @overload(NoneType, QMetaProperty)
  def captureProperty(
      self,
      a0: Optional[QMetaObject],
      a1: QMetaProperty,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlBindableToBindablePropertyBinding::captureProperty(const QMetaObject
    *a0, const QMetaProperty &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbindabletobindablepropertybinding.html

    Parameters
    ----------

    a0 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.
    """
    #  void QQmlBindableToBindablePropertyBinding::captureProperty(const
    #      QMetaObject *a0, const QMetaProperty &a1)
    self.uglySide.call(
        'ritual_ZN37QQmlBindableToBindablePropertyBinding15capturePropertyE'
        'PK11QMetaObjectRK13QMetaProperty',
        self._addressOf(a0, 'QMetaObject'), self._valueOf(a1),
    )
