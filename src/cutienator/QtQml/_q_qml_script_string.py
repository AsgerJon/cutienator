"""
QQmlScriptString binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlscriptstring.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQmlContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlScriptString(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlScriptString: a plain Python object standing in
  front of one C++ QQmlScriptString.

  C++ hands a QQmlScriptString around as a copy, so every C++
  QQmlScriptString behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlScriptString that has a ritual and that Python
  can call so far, 6 names in all: '__eq__', '__ne__', 'isEmpty',
  'isUndefinedLiteral', 'isNullLiteral', 'stringLiteral'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlScriptString::~QQmlScriptString()': the destructor: Python
    removes its C++ QQmlScriptString by it, and has no other use for it.
  - Qt's 'QQmlScriptString &QQmlScriptString::operator=(const
    QQmlScriptString &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'qreal QQmlScriptString::numberLiteral(bool *ok) const': takes a
    number to change where it is.
  - Qt's 'bool QQmlScriptString::booleanLiteral(bool *ok) const': takes a
    number to change where it is.

  What has no ritual
  ------------------

  3 of the 16 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQmlScriptString is created at the first use, not by
    'QQmlScriptString(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlScriptString back gives a copy the ritual made
    for Python, in a new cute QQmlScriptString.
  - Each name of Qt's QQmlScriptString that has no cute function yet,
    'booleanLiteral', 'numberLiteral', holds a function that raises
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
  __qt_class__ = 'QQmlScriptString'

  #  Qt's '~QQmlScriptString()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlScriptString behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQmlScriptStringD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQmlScriptString::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlscriptstring.html#isEmpty
    """
    #  bool QQmlScriptString::isEmpty() const
    return self.uglySide.call('ritual_ZNK16QQmlScriptString7isEmptyEv')

  def isUndefinedLiteral(self) -> bool:
    """
    Calls Qt's 'bool QQmlScriptString::isUndefinedLiteral() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlscriptstring.html#isUndefinedLiteral
    """
    #  bool QQmlScriptString::isUndefinedLiteral() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlScriptString18isUndefinedLiteralEv',
    )

  def isNullLiteral(self) -> bool:
    """
    Calls Qt's 'bool QQmlScriptString::isNullLiteral() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlscriptstring.html#isNullLiteral
    """
    #  bool QQmlScriptString::isNullLiteral() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlScriptString13isNullLiteralEv',
    )

  def stringLiteral(self) -> str:
    """
    Calls Qt's 'QString QQmlScriptString::stringLiteral() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlscriptstring.html#stringLiteral

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlScriptString::stringLiteral() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlScriptString13stringLiteralEv',
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

  @overload(THIS)
  def __eq__(self, a0: QQmlScriptString) -> bool:
    """
    Calls Qt's 'bool QQmlScriptString::operator==(const QQmlScriptString &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlscriptstring.html#operator==

    Parameters
    ----------

    a0 : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  bool QQmlScriptString::operator==(const QQmlScriptString &a0) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlScriptStringeqERKS_', self._valueOf(a0),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, a0: QQmlScriptString) -> bool:
    """
    Calls Qt's 'bool QQmlScriptString::operator!=(const QQmlScriptString &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlscriptstring.html#operator!=

    Parameters
    ----------

    a0 : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  bool QQmlScriptString::operator!=(const QQmlScriptString &a0) const
    return self.uglySide.call(
        'ritual_ZNK16QQmlScriptStringneERKS_', self._valueOf(a0),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlScriptString::QQmlScriptString()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlscriptstring.html#QQmlScriptString
    """
    #  QQmlScriptString::QQmlScriptString()
    self._noteCreation(QQmlScriptString, lambda: Rituals.call(
        'ritual_ZN16QQmlScriptStringC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QQmlScriptString) -> None:
    """
    Notes what was given, for Qt's 'QQmlScriptString::QQmlScriptString(const
    QQmlScriptString &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlscriptstring.html#QQmlScriptString

    Parameters
    ----------

    a0 : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  QQmlScriptString::QQmlScriptString(const QQmlScriptString &a0)
    self._noteCreation(QQmlScriptString, lambda: Rituals.call(
        'ritual_ZN16QQmlScriptStringC1ERKS_', self._valueOf(a0),
    ))

  @overload(str, QQmlContext, QObject)
  @overload(str, QQmlContext, NoneType)
  @overload(str, NoneType, QObject)
  @overload(str, NoneType, NoneType)
  def __init__(
      self,
      script: str,
      context: Optional[QQmlContext],
      scope: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlScriptString::QQmlScriptString(const
    QString &script, QQmlContext *context, QObject *scope)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlscriptstring.html#QQmlScriptString

    Parameters
    ----------

    script : str
      Passed on as it is: a QString is made of it for the call.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scope : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlScriptString::QQmlScriptString(const QString &script, QQmlContext
    #      *context, QObject *scope)
    self._noteCreation(QQmlScriptString, lambda: Rituals.call(
        'ritual_ZN16QQmlScriptStringC1ERK7QStringP11QQmlContextP7QObject',
        script, self._addressOf(context), self._addressOf(scope, 'QObject'),
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

  @staticmethod
  def booleanLiteral(*__, **_) -> Never:
    """
    Qt's 'bool QQmlScriptString::booleanLiteral(bool *ok) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlScriptString.booleanLiteral' has no cute function yet. Qt's "
        "'bool QQmlScriptString::booleanLiteral(bool *ok) const': takes a "
        "number to change where it is.")

  @staticmethod
  def numberLiteral(*__, **_) -> Never:
    """
    Qt's 'qreal QQmlScriptString::numberLiteral(bool *ok) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlScriptString.numberLiteral' has no cute function yet. Qt's "
        "'qreal QQmlScriptString::numberLiteral(bool *ok) const': takes a "
        "number to change where it is.")
