"""
QQmlJavaScriptExpression binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljavascriptexpression_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJavaScriptExpression to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QPropertyChangeTrigger, QQmlContext, QQmlDelayedError
  from . import QQmlEngine, QQmlError, QQmlSourceLocation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJavaScriptExpression(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJavaScriptExpression: a plain Python object
  standing in front of one C++ QQmlJavaScriptExpression.

  What exists
  -----------

  Every function of Qt's QQmlJavaScriptExpression that has a ritual and that
  Python can call so far, 28 names in all: 'expressionIdentifier',
  'expressionChanged', 'notifyOnValueChanged', 'setNotifyOnValueChanged',
  'resetNotifyOnValueChanged', 'scopeObject', 'setScopeObject',
  'sourceLocation', 'hasContext', 'hasValidContext', 'publicContext',
  'function', 'setFunction', 'compilationUnit', 'nextExpression', 'refresh',
  'hasError', 'hasDelayedError', 'error', 'clearError', 'clearActiveGuards',
  'delayedError', 'mustCaptureBindableProperty', 'engine',
  'hasUnresolvedNames', 'needsPropertyChangeTrigger',
  'allocatePropertyChangeTrigger', 'setupFunction'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJavaScriptExpression::~QQmlJavaScriptExpression()': the
    destructor: Python never removes a C++ QQmlJavaScriptExpression.
  - Qt's 'QV4::ReturnedValue QQmlJavaScriptExpression::evaluate(bool
    *isUndefined)': takes a number to change where it is.
  - Qt's 'QV4::ReturnedValue QQmlJavaScriptExpression::evaluate(QV4::CallData
    *callData, bool *isUndefined)': takes a number to change where it is.
  - Qt's 'bool QQmlJavaScriptExpression::evaluate(void **a, const QMetaType
    *types, int argc)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData> QQmlJavaScriptExpression::context()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQmlJavaScriptExpression::setContext(const
    QQmlRefPointer<QQmlContextData> &context)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void
    QQmlJavaScriptExpression::insertIntoList(QQmlJavaScriptExpression
    **listHead)': takes a type Python has no way to hand over yet.
  - Qt's 'QV4::ReturnedValue QQmlJavaScriptExpression::evalFunction(const
    QQmlRefPointer<QQmlContextData> &ctxt, QObject *scope, const QString
    &code, const QString &filename, quint16 line)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QQmlJavaScriptExpression::createQmlBinding(const
    QQmlRefPointer<QQmlContextData> &ctxt, QObject *scope, const QString
    &code, const QString &filename, quint16 line)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QQmlJavaScriptExpression::setCompilationUnit(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 43 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QQmlJavaScriptExpression is created at the first use, not by
    'QQmlJavaScriptExpression(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJavaScriptExpression.
  - Each name of Qt's QQmlJavaScriptExpression that has no cute function yet,
    'context', 'createQmlBinding', 'evalFunction', 'evaluate',
    'insertIntoList', 'setCompilationUnit', 'setContext', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlJavaScriptExpression, each a class in
  #  here as in C++.

  class DeleteWatcher(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJavaScriptExpression::DeleteWatcher: a plain
    Python object standing in front of one C++
    QQmlJavaScriptExpression::DeleteWatcher.

    C++ hands a QQmlJavaScriptExpression::DeleteWatcher around as a copy, so
    every C++ QQmlJavaScriptExpression::DeleteWatcher behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQmlJavaScriptExpression::DeleteWatcher that has a
    ritual and that Python can call so far, 1 name in all: 'wasDeleted'. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJavaScriptExpression::DeleteWatcher::~DeleteWatcher()': the
      destructor: Python removes its C++
      QQmlJavaScriptExpression::DeleteWatcher by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQmlJavaScriptExpression::DeleteWatcher is created at the first
      use, not by 'QQmlJavaScriptExpression::DeleteWatcher(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJavaScriptExpression::DeleteWatcher back gives
      a copy the ritual made for Python, in a new cute
      QQmlJavaScriptExpression::DeleteWatcher.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQmlJavaScriptExpression = WAIT['QQmlJavaScriptExpression']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJavaScriptExpression::DeleteWatcher'

    #  Qt's '~QQmlJavaScriptExpression::DeleteWatcher()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQmlJavaScriptExpression::DeleteWatcher behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN24QQmlJavaScriptExpression13DeleteWatcherD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def wasDeleted(self) -> bool:
      """
      Calls Qt's 'bool QQmlJavaScriptExpression::DeleteWatcher::wasDeleted()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljavascriptexpression-deletewatcher.html
      """
      #  bool QQmlJavaScriptExpression::DeleteWatcher::wasDeleted() const
      return self.uglySide.call(
          'ritual_ZNK24QQmlJavaScriptExpression13DeleteWatcher10wasDeletedE'
          'v',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QQmlJavaScriptExpression)
    @overload(NoneType)
    def __init__(self, a0: Optional[QQmlJavaScriptExpression]) -> None:
      """
      Notes what was given, for Qt's
      'QQmlJavaScriptExpression::DeleteWatcher::DeleteWatcher(
      QQmlJavaScriptExpression *a0)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljavascriptexpression-deletewatcher.html

      Parameters
      ----------

      a0 : Optional[QQmlJavaScriptExpression]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQmlJavaScriptExpression::DeleteWatcher::DeleteWatcher(
      #      QQmlJavaScriptExpression *a0)
      self._noteCreation(
          QQmlJavaScriptExpression.DeleteWatcher, lambda: Rituals.call(
              'ritual_ZN24QQmlJavaScriptExpression13DeleteWatcherC1EPS_',
              self._addressOf(a0, 'QQmlJavaScriptExpression'),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJavaScriptExpression'

  #  A C++ QQmlJavaScriptExpression Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJavaScriptExpression'

  #  The functions Qt calls itself that QQmlJavaScriptExpression is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'expressionIdentifier': (
          ('_ZNK24QQmlJavaScriptExpression20expressionIdentifierEv',
           ('address', 'text', ''),
           ()),
      ),
      'expressionChanged': (
          ('_ZN24QQmlJavaScriptExpression17expressionChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'sourceLocation': (
          ('_ZNK24QQmlJavaScriptExpression14sourceLocationEv',
           ('address', 'value', 'QtQml:QQmlSourceLocation'),
           ()),
      ),
      'refresh': (
          ('_ZN24QQmlJavaScriptExpression7refreshEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'mustCaptureBindableProperty': (
          ('_ZNK24QQmlJavaScriptExpression27mustCaptureBindablePropertyEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def expressionIdentifier(self) -> str:
    """
    Calls Qt's 'QString QQmlJavaScriptExpression::expressionIdentifier()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#expressionIdentifier

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJavaScriptExpression::expressionIdentifier() const
    ritual = 'ritual_ZNK24QQmlJavaScriptExpression20expressionIdentifierEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlJavaScriptExpression20expressionIdentifierEv')
    return self._callAs('QQmlJavaScriptExpression', ritual)

  def notifyOnValueChanged(self) -> bool:
    """
    Calls Qt's 'bool QQmlJavaScriptExpression::notifyOnValueChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#notifyOnValueChanged
    """
    #  bool QQmlJavaScriptExpression::notifyOnValueChanged() const
    return self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression20notifyOnValueChangedEv',
    )

  def scopeObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlJavaScriptExpression::scopeObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#scopeObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlJavaScriptExpression::scopeObject() const
    address = self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression11scopeObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def sourceLocation(self) -> QQmlSourceLocation:
    """
    Calls Qt's 'QQmlSourceLocation QQmlJavaScriptExpression::sourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#sourceLocation

    Returns
    -------

    QQmlSourceLocation
      A new cute QQmlSourceLocation around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlSourceLocation QQmlJavaScriptExpression::sourceLocation() const
    ritual = 'ritual_ZNK24QQmlJavaScriptExpression14sourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QQmlJavaScriptExpression14sourceLocationEv'
    address = self._callAs('QQmlJavaScriptExpression', ritual)
    from . import QQmlSourceLocation
    return QQmlSourceLocation._cuteOwning(address)

  def hasContext(self) -> bool:
    """
    Calls Qt's 'bool QQmlJavaScriptExpression::hasContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#hasContext
    """
    #  bool QQmlJavaScriptExpression::hasContext() const
    return self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression10hasContextEv',
    )

  def hasValidContext(self) -> bool:
    """
    Calls Qt's 'bool QQmlJavaScriptExpression::hasValidContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#hasValidContext
    """
    #  bool QQmlJavaScriptExpression::hasValidContext() const
    return self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression15hasValidContextEv',
    )

  def publicContext(self) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQmlJavaScriptExpression::publicContext()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#publicContext

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQmlJavaScriptExpression::publicContext() const
    address = self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression13publicContextEv',
    )
    from . import QQmlContext
    return QQmlContext._cuteAt(address)

  def function(self) -> Optional[QV4.Function]:
    """
    Calls Qt's 'QV4::Function *QQmlJavaScriptExpression::function() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#function

    Returns
    -------

    Optional[QV4.Function]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Function *QQmlJavaScriptExpression::function() const
    address = self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression8functionEv',
    )
    return QV4.Function._cuteAt(address)

  def compilationUnit(self) -> Optional[QV4.ExecutableCompilationUnit]:
    """
    Calls Qt's 'QV4::ExecutableCompilationUnit
    *QQmlJavaScriptExpression::compilationUnit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#compilationUnit

    Returns
    -------

    Optional[QV4.ExecutableCompilationUnit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutableCompilationUnit
    #      *QQmlJavaScriptExpression::compilationUnit() const
    address = self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression15compilationUnitEv',
    )
    return QV4.ExecutableCompilationUnit._cuteAt(address)

  def nextExpression(self) -> Optional[QQmlJavaScriptExpression]:
    """
    Calls Qt's 'QQmlJavaScriptExpression
    *QQmlJavaScriptExpression::nextExpression() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#nextExpression

    Returns
    -------

    Optional[QQmlJavaScriptExpression]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJavaScriptExpression *QQmlJavaScriptExpression::nextExpression()
    #      const
    address = self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression14nextExpressionEv',
    )
    return QQmlJavaScriptExpression._cuteAt(address)

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QQmlJavaScriptExpression::hasError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#hasError
    """
    #  bool QQmlJavaScriptExpression::hasError() const
    return self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression8hasErrorEv',
    )

  def hasDelayedError(self) -> bool:
    """
    Calls Qt's 'bool QQmlJavaScriptExpression::hasDelayedError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#hasDelayedError
    """
    #  bool QQmlJavaScriptExpression::hasDelayedError() const
    return self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression15hasDelayedErrorEv',
    )

  @overload(QQmlEngine)
  @overload(NoneType)
  def error(self, a0: Optional[QQmlEngine]) -> QQmlError:
    """
    Calls Qt's 'QQmlError QQmlJavaScriptExpression::error(QQmlEngine *a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#error

    Parameters
    ----------

    a0 : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlError
      A new cute QQmlError around the copy Qt gave back. Python owns it.
    """
    #  QQmlError QQmlJavaScriptExpression::error(QQmlEngine *a0) const
    address = self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression5errorEP10QQmlEngine',
        self._addressOf(a0),
    )
    from . import QQmlError
    return QQmlError._cuteOwning(address)

  def mustCaptureBindableProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlJavaScriptExpression::mustCaptureBindableProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html
    """
    #  bool QQmlJavaScriptExpression::mustCaptureBindableProperty() const
    ritual = (
        'ritual_ZNK24QQmlJavaScriptExpression27mustCaptureBindablePropertyE'
        'v')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QQmlJavaScriptExpression27mustCaptureBindablePro'
          'pertyEv')
    return self._callAs('QQmlJavaScriptExpression', ritual)

  def engine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQmlJavaScriptExpression::engine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#engine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQmlJavaScriptExpression::engine() const
    address = self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression6engineEv',
    )
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def hasUnresolvedNames(self) -> bool:
    """
    Calls Qt's 'bool QQmlJavaScriptExpression::hasUnresolvedNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#hasUnresolvedNames
    """
    #  bool QQmlJavaScriptExpression::hasUnresolvedNames() const
    return self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZNK24QQmlJavaScriptExpression18hasUnresolvedNamesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setNotifyOnValueChanged(self, v: bool) -> None:
    """
    Calls Qt's 'void QQmlJavaScriptExpression::setNotifyOnValueChanged(bool
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void QQmlJavaScriptExpression::setNotifyOnValueChanged(bool v)
    self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression23setNotifyOnValueChangedEb',
        v,
    )

  @overload(QObject)
  @overload(NoneType)
  def setScopeObject(self, v: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlJavaScriptExpression::setScopeObject(QObject *v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#setScopeObject

    Parameters
    ----------

    v : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJavaScriptExpression::setScopeObject(QObject *v)
    self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression14setScopeObjectEP7QObject',
        self._addressOf(v, 'QObject'),
    )

  @overload(WAIT['QV4.Function'])
  @overload(NoneType)
  def setFunction(self, f: Optional[QV4.Function]) -> None:
    """
    Calls Qt's 'void QQmlJavaScriptExpression::setFunction(QV4::Function
    *f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#setFunction

    Parameters
    ----------

    f : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJavaScriptExpression::setFunction(QV4::Function *f)
    self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression11setFunctionEPN3QV48FunctionE',
        self._addressOf(f),
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
    'QQmlJavaScriptExpression::QQmlJavaScriptExpression()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html
    """
    #  QQmlJavaScriptExpression::QQmlJavaScriptExpression()
    self._noteCreation(QQmlJavaScriptExpression, lambda: Rituals.call(
        'ritual_ZN24QQmlJavaScriptExpressionC1Ev',
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

  def expressionChanged(self) -> None:
    """
    Calls Qt's 'void QQmlJavaScriptExpression::expressionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#expressionChanged
    """
    #  void QQmlJavaScriptExpression::expressionChanged()
    self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression17expressionChangedEv',
    )

  def resetNotifyOnValueChanged(self) -> None:
    """
    Calls Qt's 'void QQmlJavaScriptExpression::resetNotifyOnValueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html
    """
    #  void QQmlJavaScriptExpression::resetNotifyOnValueChanged()
    self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression25resetNotifyOnValueChangedEv',
    )

  def refresh(self) -> None:
    """
    Calls Qt's 'void QQmlJavaScriptExpression::refresh()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#refresh
    """
    #  void QQmlJavaScriptExpression::refresh()
    ritual = 'ritual_ZN24QQmlJavaScriptExpression7refreshEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQmlJavaScriptExpression7refreshEv'
    self._callAs('QQmlJavaScriptExpression', ritual)

  def clearError(self) -> None:
    """
    Calls Qt's 'void QQmlJavaScriptExpression::clearError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#clearError
    """
    #  void QQmlJavaScriptExpression::clearError()
    self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression10clearErrorEv',
    )

  def clearActiveGuards(self) -> None:
    """
    Calls Qt's 'void QQmlJavaScriptExpression::clearActiveGuards()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#clearActiveGuards
    """
    #  void QQmlJavaScriptExpression::clearActiveGuards()
    self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression17clearActiveGuardsEv',
    )

  def delayedError(self) -> Optional[QQmlDelayedError]:
    """
    Calls Qt's 'QQmlDelayedError *QQmlJavaScriptExpression::delayedError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#delayedError

    Returns
    -------

    Optional[QQmlDelayedError]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlDelayedError *QQmlJavaScriptExpression::delayedError()
    address = self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression12delayedErrorEv',
    )
    from . import QQmlDelayedError
    return QQmlDelayedError._cuteAt(address)

  @overload(QObject, int)
  @overload(NoneType, int)
  def needsPropertyChangeTrigger(
      self,
      target: Optional[QObject],
      propertyIndex: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlJavaScriptExpression::needsPropertyChangeTrigger(QObject *target, int
    propertyIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyIndex : int
      Passed on as it is.
    """
    #  bool QQmlJavaScriptExpression::needsPropertyChangeTrigger(QObject
    #      *target, int propertyIndex)
    return self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression26needsPropertyChangeTriggerEP7'
        'QObjecti',
        self._addressOf(target, 'QObject'), propertyIndex,
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def allocatePropertyChangeTrigger(
      self,
      target: Optional[QObject],
      propertyIndex: int,
  ) -> Optional[QPropertyChangeTrigger]:
    """
    Calls Qt's 'QPropertyChangeTrigger
    *QQmlJavaScriptExpression::allocatePropertyChangeTrigger(QObject *target,
    int propertyIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QPropertyChangeTrigger]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPropertyChangeTrigger
    #      *QQmlJavaScriptExpression::allocatePropertyChangeTrigger(QObject
    #      *target, int propertyIndex)
    address = self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression29allocatePropertyChangeTrigger'
        'EP7QObjecti',
        self._addressOf(target, 'QObject'), propertyIndex,
    )
    from . import QPropertyChangeTrigger
    return QPropertyChangeTrigger._cuteAt(address)

  @overload(WAIT['QV4.ExecutionContext'], WAIT['QV4.Function'])
  @overload(WAIT['QV4.ExecutionContext'], NoneType)
  @overload(NoneType, WAIT['QV4.Function'])
  @overload(NoneType, NoneType)
  def setupFunction(
      self,
      qmlContext: Optional[QV4.ExecutionContext],
      f: Optional[QV4.Function],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJavaScriptExpression::setupFunction(QV4::ExecutionContext
    *qmlContext, QV4::Function *f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljavascriptexpression.html#setupFunction

    Parameters
    ----------

    qmlContext : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    f : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJavaScriptExpression::setupFunction(QV4::ExecutionContext
    #      *qmlContext, QV4::Function *f)
    self._callAs(
        'QQmlJavaScriptExpression',
        'ritual_ZN24QQmlJavaScriptExpression13setupFunctionEPN3QV416Executi'
        'onContextEPNS0_8FunctionE',
        self._addressOf(qmlContext), self._addressOf(f),
    )

  @staticmethod
  def context(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData> QQmlJavaScriptExpression::context()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJavaScriptExpression.context' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> "
        "QQmlJavaScriptExpression::context() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def createQmlBinding(*__, **_) -> Never:
    """
    Qt's 'void QQmlJavaScriptExpression::createQmlBinding(const
    QQmlRefPointer<QQmlContextData> &ctxt, QObject *scope, const QString
    &code, const QString &filename, quint16 line)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJavaScriptExpression.createQmlBinding' has no cute function "
        "yet. Qt's 'void QQmlJavaScriptExpression::createQmlBinding(const "
        "QQmlRefPointer<QQmlContextData> &ctxt, QObject *scope, const "
        "QString &code, const QString &filename, quint16 line)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def evalFunction(*__, **_) -> Never:
    """
    Qt's 'QV4::ReturnedValue QQmlJavaScriptExpression::evalFunction(const
    QQmlRefPointer<QQmlContextData> &ctxt, QObject *scope, const QString
    &code, const QString &filename, quint16 line)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJavaScriptExpression.evalFunction' has no cute function yet. "
        "Qt's 'QV4::ReturnedValue "
        "QQmlJavaScriptExpression::evalFunction(const "
        "QQmlRefPointer<QQmlContextData> &ctxt, QObject *scope, const "
        "QString &code, const QString &filename, quint16 line)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def evaluate(*__, **_) -> Never:
    """
    - Qt's 'QV4::ReturnedValue QQmlJavaScriptExpression::evaluate(bool
      *isUndefined)': takes a number to change where it is.
    - Qt's 'QV4::ReturnedValue
      QQmlJavaScriptExpression::evaluate(QV4::CallData *callData, bool
      *isUndefined)': takes a number to change where it is.
    - Qt's 'bool QQmlJavaScriptExpression::evaluate(void **a, const QMetaType
      *types, int argc)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJavaScriptExpression.evaluate' has no cute function yet. Qt's "
        "'QV4::ReturnedValue QQmlJavaScriptExpression::evaluate(bool "
        "*isUndefined)': takes a number to change where it is. Qt's "
        "'QV4::ReturnedValue "
        "QQmlJavaScriptExpression::evaluate(QV4::CallData *callData, bool "
        "*isUndefined)': takes a number to change where it is. Qt's 'bool "
        "QQmlJavaScriptExpression::evaluate(void **a, const QMetaType "
        "*types, int argc)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def insertIntoList(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlJavaScriptExpression::insertIntoList(QQmlJavaScriptExpression
    **listHead)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJavaScriptExpression.insertIntoList' has no cute function "
        "yet. Qt's 'void "
        "QQmlJavaScriptExpression::insertIntoList(QQmlJavaScriptExpression "
        "**listHead)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'void QQmlJavaScriptExpression::setCompilationUnit(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJavaScriptExpression.setCompilationUnit' has no cute function "
        "yet. Qt's 'void QQmlJavaScriptExpression::setCompilationUnit(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setContext(*__, **_) -> Never:
    """
    Qt's 'void QQmlJavaScriptExpression::setContext(const
    QQmlRefPointer<QQmlContextData> &context)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJavaScriptExpression.setContext' has no cute function yet. "
        "Qt's 'void QQmlJavaScriptExpression::setContext(const "
        "QQmlRefPointer<QQmlContextData> &context)': takes a type Python "
        "has no way to hand over yet.")
