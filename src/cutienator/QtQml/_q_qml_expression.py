"""
QQmlExpression binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlexpression.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQmlContext, QQmlEngine, QQmlError, QQmlExpressionPrivate
  from . import QQmlScriptString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlContext = WAIT['QQmlContext']
  QQmlScriptString = WAIT['QQmlScriptString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlExpression(QObject):
  """
  The cute side of Qt's QQmlExpression: a plain Python object standing in
  front of one C++ QQmlExpression.

  It is built on the cute 'QObject', as Qt's QQmlExpression is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlExpression that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'engine', 'context',
  'expression', 'setExpression', 'notifyOnValueChanged',
  'setNotifyOnValueChanged', 'sourceFile', 'lineNumber', 'columnNumber',
  'setSourceLocation', 'scopeObject', 'hasError', 'clearError', 'error',
  'valueChanged', 'd_func'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlExpression::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlExpression::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlExpression::~QQmlExpression()': the destructor: Python never
    removes a C++ QQmlExpression.
  - Qt's 'QVariant QQmlExpression::evaluate(bool *valueIsUndefined)': takes a
    number to change where it is.
  - Qt's 'QQmlExpression::QQmlExpression(QQmlExpressionPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQmlExpressionPrivate *QQmlExpression::d_func() const': takes
    in Python what 'QQmlExpressionPrivate *QQmlExpression::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 31 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQmlExpression is created at the first use, not by
    'QQmlExpression(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlExpression.
  - Qt tells when it has removed the C++ QQmlExpression. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlExpression that has no cute function yet,
    'evaluate', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQmlExpression::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlExpression::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQmlExpression2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlExpression'

  #  A C++ QQmlExpression Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlExpression'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlExpression::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlExpression::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQmlExpression10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def engine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQmlExpression::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#engine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQmlExpression::engine() const
    address = self.uglySide.call('ritual_ZNK14QQmlExpression6engineEv')
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def context(self) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQmlExpression::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#context

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQmlExpression::context() const
    address = self.uglySide.call('ritual_ZNK14QQmlExpression7contextEv')
    from . import QQmlContext
    return QQmlContext._cuteAt(address)

  def expression(self) -> str:
    """
    Calls Qt's 'QString QQmlExpression::expression() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#expression

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlExpression::expression() const
    return self.uglySide.call('ritual_ZNK14QQmlExpression10expressionEv')

  def notifyOnValueChanged(self) -> bool:
    """
    Calls Qt's 'bool QQmlExpression::notifyOnValueChanged() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlexpression.html#notifyOnValueChanged
    """
    #  bool QQmlExpression::notifyOnValueChanged() const
    return self.uglySide.call(
        'ritual_ZNK14QQmlExpression20notifyOnValueChangedEv',
    )

  def sourceFile(self) -> str:
    """
    Calls Qt's 'QString QQmlExpression::sourceFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#sourceFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlExpression::sourceFile() const
    return self.uglySide.call('ritual_ZNK14QQmlExpression10sourceFileEv')

  def lineNumber(self) -> int:
    """
    Calls Qt's 'int QQmlExpression::lineNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#lineNumber
    """
    #  int QQmlExpression::lineNumber() const
    return self.uglySide.call('ritual_ZNK14QQmlExpression10lineNumberEv')

  def columnNumber(self) -> int:
    """
    Calls Qt's 'int QQmlExpression::columnNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#columnNumber
    """
    #  int QQmlExpression::columnNumber() const
    return self.uglySide.call('ritual_ZNK14QQmlExpression12columnNumberEv')

  def scopeObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlExpression::scopeObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#scopeObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlExpression::scopeObject() const
    address = self.uglySide.call('ritual_ZNK14QQmlExpression11scopeObjectEv')
    return QObject._cuteAt(address)

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QQmlExpression::hasError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#hasError
    """
    #  bool QQmlExpression::hasError() const
    return self.uglySide.call('ritual_ZNK14QQmlExpression8hasErrorEv')

  def error(self) -> QQmlError:
    """
    Calls Qt's 'QQmlError QQmlExpression::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#error

    Returns
    -------

    QQmlError
      A new cute QQmlError around the copy Qt gave back. Python owns it.
    """
    #  QQmlError QQmlExpression::error() const
    address = self.uglySide.call('ritual_ZNK14QQmlExpression5errorEv')
    from . import QQmlError
    return QQmlError._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setExpression(self, a0: str) -> None:
    """
    Calls Qt's 'void QQmlExpression::setExpression(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#setExpression

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlExpression::setExpression(const QString &a0)
    self.uglySide.call(
        'ritual_ZN14QQmlExpression13setExpressionERK7QString', a0,
    )

  @overload(bool)
  def setNotifyOnValueChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQmlExpression::setNotifyOnValueChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlexpression.html#setNotifyOnValueChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQmlExpression::setNotifyOnValueChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN14QQmlExpression23setNotifyOnValueChangedEb', a0,
    )

  @overload(str, int)
  @overload(str, int, int)
  def setSourceLocation(
      self,
      fileName: str,
      line: int,
      column: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QQmlExpression::setSourceLocation(const QString
    &fileName, int line, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlexpression.html#setSourceLocation

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    line : int
      Passed on as it is.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QQmlExpression::setSourceLocation(const QString &fileName, int
    #      line, int column)
    self.uglySide.call(
        'ritual_ZN14QQmlExpression17setSourceLocationERK7QStringii',
        fileName, line, column,
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
    Notes what was given, for Qt's 'QQmlExpression::QQmlExpression()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#QQmlExpression
    """
    #  QQmlExpression::QQmlExpression()
    self._noteCreation(QQmlExpression, lambda: Rituals.call(
        'ritual_ZN14QQmlExpressionC1Ev',
    ))

  @overload(QQmlContext, QObject, str)
  @overload(QQmlContext, NoneType, str)
  @overload(NoneType, QObject, str)
  @overload(NoneType, NoneType, str)
  @overload(QQmlContext, QObject, str, QObject)
  @overload(QQmlContext, QObject, str, NoneType)
  @overload(QQmlContext, NoneType, str, QObject)
  @overload(QQmlContext, NoneType, str, NoneType)
  @overload(NoneType, QObject, str, QObject)
  @overload(NoneType, QObject, str, NoneType)
  @overload(NoneType, NoneType, str, QObject)
  @overload(NoneType, NoneType, str, NoneType)
  def __init__(
      self,
      a0: Optional[QQmlContext],
      a1: Optional[QObject],
      a2: str,
      a3: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlExpression::QQmlExpression(QQmlContext *a0, QObject *a1, const
    QString &a2, QObject *a3)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#QQmlExpression

    Parameters
    ----------

    a0 : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : str
      Passed on as it is: a QString is made of it for the call.

    a3 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlExpression::QQmlExpression(QQmlContext *a0, QObject *a1, const
    #      QString &a2, QObject *a3)
    self._noteCreation(QQmlExpression, lambda: Rituals.call(
        'ritual_ZN14QQmlExpressionC1EP11QQmlContextP7QObjectRK7QStringS3_',
        self._addressOf(a0), self._addressOf(a1, 'QObject'), a2,
        self._addressOf(a3, 'QObject'),
    ))

  @overload(QQmlScriptString)
  @overload(QQmlScriptString, QQmlContext)
  @overload(QQmlScriptString, NoneType)
  @overload(QQmlScriptString, QQmlContext, QObject)
  @overload(QQmlScriptString, QQmlContext, NoneType)
  @overload(QQmlScriptString, NoneType, QObject)
  @overload(QQmlScriptString, NoneType, NoneType)
  @overload(QQmlScriptString, QQmlContext, QObject, QObject)
  @overload(QQmlScriptString, QQmlContext, QObject, NoneType)
  @overload(QQmlScriptString, QQmlContext, NoneType, QObject)
  @overload(QQmlScriptString, QQmlContext, NoneType, NoneType)
  @overload(QQmlScriptString, NoneType, QObject, QObject)
  @overload(QQmlScriptString, NoneType, QObject, NoneType)
  @overload(QQmlScriptString, NoneType, NoneType, QObject)
  @overload(QQmlScriptString, NoneType, NoneType, NoneType)
  def __init__(
      self,
      a0: QQmlScriptString,
      a1: Optional[QQmlContext] = None,
      a2: Optional[QObject] = None,
      a3: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlExpression::QQmlExpression(const
    QQmlScriptString &a0, QQmlContext *a1, QObject *a2, QObject *a3)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#QQmlExpression

    Parameters
    ----------

    a0 : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.

    a1 : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    a2 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    a3 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlExpression::QQmlExpression(const QQmlScriptString &a0, QQmlContext
    #      *a1, QObject *a2, QObject *a3)
    self._noteCreation(QQmlExpression, lambda: Rituals.call(
        'ritual_ZN14QQmlExpressionC1ERK16QQmlScriptStringP11QQmlContextP7QO'
        'bjectS6_',
        self._valueOf(a0), self._addressOf(a1), self._addressOf(a2,
        'QObject'), self._addressOf(a3, 'QObject'),
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

  def clearError(self) -> None:
    """
    Calls Qt's 'void QQmlExpression::clearError()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#clearError
    """
    #  void QQmlExpression::clearError()
    self.uglySide.call('ritual_ZN14QQmlExpression10clearErrorEv')

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQmlExpression::valueChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#valueChanged
    """
    #  void QQmlExpression::valueChanged()
    self.uglySide.call('ritual_ZN14QQmlExpression12valueChangedEv')

  def d_func(self) -> Optional[QQmlExpressionPrivate]:
    """
    Calls Qt's 'QQmlExpressionPrivate *QQmlExpression::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlexpression.html#d_func

    Returns
    -------

    Optional[QQmlExpressionPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlExpressionPrivate *QQmlExpression::d_func()
    address = self.uglySide.call('ritual_ZN14QQmlExpression6d_funcEv')
    from . import QQmlExpressionPrivate
    return QQmlExpressionPrivate._cuteAt(address)

  @staticmethod
  def evaluate(*__, **_) -> Never:
    """
    Qt's 'QVariant QQmlExpression::evaluate(bool *valueIsUndefined)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlExpression.evaluate' has no cute function yet. Qt's 'QVariant "
        "QQmlExpression::evaluate(bool *valueIsUndefined)': takes a number "
        "to change where it is.")
