"""
QQmlBoundSignalExpression binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlboundsignal_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlBoundSignalExpression to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQmlJavaScriptExpression

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject


class QQmlBoundSignalExpression(QQmlJavaScriptExpression):
  """
  The cute side of Qt's QQmlBoundSignalExpression: a plain Python object
  standing in front of one C++ QQmlBoundSignalExpression.

  It is built on the cute 'QQmlJavaScriptExpression', as Qt's
  QQmlBoundSignalExpression is built on Qt's QQmlJavaScriptExpression, and
  has everything that class has. Qt's QQmlBoundSignalExpression is built on
  Qt's QQmlRefCounted<QQmlBoundSignalExpression> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQmlBoundSignalExpression that has a ritual and that
  Python can call so far, 6 names in all: 'expressionIdentifier',
  'expressionChanged', 'mustCaptureBindableProperty', 'expression', 'target',
  'expressionFunctionValid'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlBoundSignalExpression::QQmlBoundSignalExpression(const QObject
    *target, int index, const QQmlRefPointer<QQmlContextData> &ctxt, QObject
    *scope, const QString &expression, const QString &fileName, quint16 line,
    quint16 column, const QString &handlerName, const QString
    &parameterString)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlBoundSignalExpression::QQmlBoundSignalExpression(const QObject
    *target, int index, const QQmlRefPointer<QQmlContextData> &ctxt, QObject
    *scopeObject, QV4::Function *function, QV4::ExecutionContext *scope)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlBoundSignalExpression::evaluate(void **a)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlBoundSignalExpression::~QQmlBoundSignalExpression()': the
    destructor: Python never removes a C++ QQmlBoundSignalExpression.
  - Qt's 'void QQmlBoundSignalExpression::init(const
    QQmlRefPointer<QQmlContextData> &ctxt, QObject *scope)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlBoundSignalExpression is created at the first use, not by
    'QQmlBoundSignalExpression(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlBoundSignalExpression.
  - Each name of Qt's QQmlBoundSignalExpression that has no cute function
    yet, '__init__', 'init', holds a function that raises
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
  __qt_class__ = 'QQmlBoundSignalExpression'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def expressionIdentifier(self) -> str:
    """
    Calls Qt's 'QString QQmlBoundSignalExpression::expressionIdentifier()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlboundsignalexpression.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlBoundSignalExpression::expressionIdentifier() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlBoundSignalExpression20expressionIdentifierEv',
    )

  def mustCaptureBindableProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlBoundSignalExpression::mustCaptureBindableProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlboundsignalexpression.html
    """
    #  bool QQmlBoundSignalExpression::mustCaptureBindableProperty() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlBoundSignalExpression27mustCaptureBindableProperty'
        'Ev',
    )

  def expression(self) -> str:
    """
    Calls Qt's 'QString QQmlBoundSignalExpression::expression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlboundsignalexpression.html#expression

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlBoundSignalExpression::expression() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlBoundSignalExpression10expressionEv',
    )

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'const QObject *QQmlBoundSignalExpression::target() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlboundsignalexpression.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QObject *QQmlBoundSignalExpression::target() const
    address = self.uglySide.call(
        'ritual_ZNK25QQmlBoundSignalExpression6targetEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def expressionFunctionValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlBoundSignalExpression::expressionFunctionValid()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlboundsignalexpression.html
    """
    #  bool QQmlBoundSignalExpression::expressionFunctionValid() const
    return self.uglySide.call(
        'ritual_ZNK25QQmlBoundSignalExpression23expressionFunctionValidEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QQmlBoundSignalExpression::QQmlBoundSignalExpression(const
      QObject *target, int index, const QQmlRefPointer<QQmlContextData>
      &ctxt, QObject *scope, const QString &expression, const QString
      &fileName, quint16 line, quint16 column, const QString &handlerName,
      const QString &parameterString)': takes a type Python has no way to
      hand over yet.
    - Qt's 'QQmlBoundSignalExpression::QQmlBoundSignalExpression(const
      QObject *target, int index, const QQmlRefPointer<QQmlContextData>
      &ctxt, QObject *scopeObject, QV4::Function *function,
      QV4::ExecutionContext *scope)': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QQmlBoundSignalExpression.__init__' has no cute function yet. "
        "Qt's 'QQmlBoundSignalExpression::QQmlBoundSignalExpression(const "
        "QObject *target, int index, const QQmlRefPointer<QQmlContextData> "
        "&ctxt, QObject *scope, const QString &expression, const QString "
        "&fileName, quint16 line, quint16 column, const QString "
        "&handlerName, const QString &parameterString)': takes a type "
        "Python has no way to hand over yet. Qt's "
        "'QQmlBoundSignalExpression::QQmlBoundSignalExpression(const "
        "QObject *target, int index, const QQmlRefPointer<QQmlContextData> "
        "&ctxt, QObject *scopeObject, QV4::Function *function, "
        "QV4::ExecutionContext *scope)': takes a type Python has no way to "
        "hand over yet.")

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
    Calls Qt's 'void QQmlBoundSignalExpression::expressionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlboundsignalexpression.html#expressionChanged
    """
    #  void QQmlBoundSignalExpression::expressionChanged()
    self.uglySide.call(
        'ritual_ZN25QQmlBoundSignalExpression17expressionChangedEv',
    )

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QQmlBoundSignalExpression::init(const
    QQmlRefPointer<QQmlContextData> &ctxt, QObject *scope)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlBoundSignalExpression.init' has no cute function yet. Qt's "
        "'void QQmlBoundSignalExpression::init(const "
        "QQmlRefPointer<QQmlContextData> &ctxt, QObject *scope)': takes a "
        "type Python has no way to hand over yet.")
