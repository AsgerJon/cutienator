"""
QQmlExpressionPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlexpression_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlExpressionPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QQmlJavaScriptExpression

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlExpression
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlExpression = WAIT['QQmlExpression']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlExpressionPrivate(QObjectPrivate, QQmlJavaScriptExpression):
  """
  The cute side of Qt's QQmlExpressionPrivate: a plain Python object standing
  in front of one C++ QQmlExpressionPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQmlExpressionPrivate is
  built on Qt's QObjectPrivate, and has everything that class has. It is
  built on the cute 'QQmlJavaScriptExpression' as well, as Qt's
  QQmlExpressionPrivate is built on Qt's QQmlJavaScriptExpression too, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlExpressionPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func',
  'mustCaptureBindableProperty', 'get', 'expressionIdentifier',
  'expressionChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlExpression *QQmlExpressionPrivate::q_func() const': takes
    in Python what 'QQmlExpression *QQmlExpressionPrivate::q_func()' takes.
  - Qt's 'QQmlExpressionPrivate::~QQmlExpressionPrivate()': the destructor:
    Python never removes a C++ QQmlExpressionPrivate.
  - Qt's 'void QQmlExpressionPrivate::init(const
    QQmlRefPointer<QQmlContextData> &a0, const QString &a1, QObject *a2)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlExpressionPrivate::init(const
    QQmlRefPointer<QQmlContextData> &a0, QV4::Function *runtimeFunction,
    QObject *a2)': takes a type Python has no way to hand over yet.
  - Qt's 'QVariant QQmlExpressionPrivate::value(bool *isUndefined)': takes a
    number to change where it is.
  - Qt's 'QV4::ReturnedValue QQmlExpressionPrivate::v4value(bool
    *isUndefined)': takes a number to change where it is.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQmlExpressionPrivate is created at the first use, not by
    'QQmlExpressionPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlExpressionPrivate.
  - Each name of Qt's QQmlExpressionPrivate that has no cute function yet,
    '_q_notify', 'init', 'v4value', 'value', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlExpression)
  @overload(NoneType)
  def get(expr: Optional[QQmlExpression]) -> Optional[QQmlExpressionPrivate]:
    """
    Calls Qt's 'QQmlExpressionPrivate
    *QQmlExpressionPrivate::get(QQmlExpression *expr)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpressionprivate.html#get

    Parameters
    ----------

    expr : Optional[QQmlExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlExpressionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlExpressionPrivate *QQmlExpressionPrivate::get(QQmlExpression
    #      *expr)
    address = Rituals.call(
        'ritual_ZN21QQmlExpressionPrivate3getEP14QQmlExpression',
        CuteMixin._addressOf(expr),
    )
    return QQmlExpressionPrivate._cuteAt(address)

  @staticmethod
  @overload(THIS)
  def get(expr: Optional[QQmlExpressionPrivate]) -> Optional[QQmlExpression]:
    """
    Calls Qt's 'QQmlExpression
    *QQmlExpressionPrivate::get(QQmlExpressionPrivate *expr)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpressionprivate.html#get

    Parameters
    ----------

    expr : Optional[QQmlExpressionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlExpression]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlExpression *QQmlExpressionPrivate::get(QQmlExpressionPrivate
    #      *expr)
    address = Rituals.call(
        'ritual_ZN21QQmlExpressionPrivate3getEPS_',
        CuteMixin._addressOf(expr),
    )
    from . import QQmlExpression
    return QQmlExpression._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlExpressionPrivate'

  #  Qt's QQmlExpressionPrivate is built on more than one class. The part of
  #  a C++ QQmlExpressionPrivate that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlJavaScriptExpression':
          'ritual_cast_QQmlExpressionPrivate_QQmlJavaScriptExpression',
  }

  #  A C++ QQmlExpressionPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlExpressionPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def mustCaptureBindableProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlExpressionPrivate::mustCaptureBindableProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlexpressionprivate.html
    """
    #  bool QQmlExpressionPrivate::mustCaptureBindableProperty() const
    return self.uglySide.call(
        'ritual_ZNK21QQmlExpressionPrivate27mustCaptureBindablePropertyEv',
    )

  def expressionIdentifier(self) -> str:
    """
    Calls Qt's 'QString QQmlExpressionPrivate::expressionIdentifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlexpressionprivate.html#expressionIdentifier

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlExpressionPrivate::expressionIdentifier() const
    ritual = 'ritual_ZNK21QQmlExpressionPrivate20expressionIdentifierEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQmlExpressionPrivate20expressionIdentifierEv')
    return self.uglySide.call(ritual)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlExpressionPrivate::QQmlExpressionPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlexpressionprivate.html#QQmlExpressionPrivate
    """
    #  QQmlExpressionPrivate::QQmlExpressionPrivate()
    self._noteCreation(QQmlExpressionPrivate, lambda: Rituals.call(
        'ritual_ZN21QQmlExpressionPrivateC1Ev',
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

  def q_func(self) -> Optional[QQmlExpression]:
    """
    Calls Qt's 'QQmlExpression *QQmlExpressionPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpressionprivate.html#q_func

    Returns
    -------

    Optional[QQmlExpression]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlExpression *QQmlExpressionPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QQmlExpressionPrivate6q_funcEv')
    from . import QQmlExpression
    return QQmlExpression._cuteAt(address)

  def expressionChanged(self) -> None:
    """
    Calls Qt's 'void QQmlExpressionPrivate::expressionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlexpressionprivate.html#expressionChanged
    """
    #  void QQmlExpressionPrivate::expressionChanged()
    ritual = 'ritual_ZN21QQmlExpressionPrivate17expressionChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQmlExpressionPrivate17expressionChangedEv'
    self.uglySide.call(ritual)

  @staticmethod
  def _q_notify(*__, **_) -> Never:
    """
    Qt's 'void QQmlExpressionPrivate::_q_notify()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQmlExpressionPrivate._q_notify' has no cute function yet. Qt's "
        "'void QQmlExpressionPrivate::_q_notify()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    - Qt's 'void QQmlExpressionPrivate::init(const
      QQmlRefPointer<QQmlContextData> &a0, const QString &a1, QObject *a2)':
      takes a type Python has no way to hand over yet.
    - Qt's 'void QQmlExpressionPrivate::init(const
      QQmlRefPointer<QQmlContextData> &a0, QV4::Function *runtimeFunction,
      QObject *a2)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlExpressionPrivate.init' has no cute function yet. Qt's 'void "
        "QQmlExpressionPrivate::init(const QQmlRefPointer<QQmlContextData> "
        "&a0, const QString &a1, QObject *a2)': takes a type Python has no "
        "way to hand over yet. Qt's 'void QQmlExpressionPrivate::init(const "
        "QQmlRefPointer<QQmlContextData> &a0, QV4::Function "
        "*runtimeFunction, QObject *a2)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def v4value(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlExpressionPrivate::v4value(bool
    *isUndefined)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlExpressionPrivate.v4value' has no cute function yet. Qt's "
        "'QV4::ReturnedValue QQmlExpressionPrivate::v4value(bool "
        "*isUndefined)': takes a number to change where it is.")

  @staticmethod
  def value(*__, **_) -> Never:
    """
    Qt's 'QVariant QQmlExpressionPrivate::value(bool *isUndefined)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlExpressionPrivate.value' has no cute function yet. Qt's "
        "'QVariant QQmlExpressionPrivate::value(bool *isUndefined)': takes "
        "a number to change where it is.")
