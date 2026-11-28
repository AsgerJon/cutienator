"""
QQuickPropertyChanges binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpropertychanges_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickPropertyChanges to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuickStateOperation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QQuickStateAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPropertyChanges(QQuickStateOperation):
  """
  The cute side of Qt's QQuickPropertyChanges: a plain Python object standing
  in front of one C++ QQuickPropertyChanges.

  It is built on the cute 'QQuickStateOperation', as Qt's
  QQuickPropertyChanges is built on Qt's QQuickStateOperation, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPropertyChanges that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr', 'object',
  'setObject', 'restoreEntryValues', 'setRestoreEntryValues', 'isExplicit',
  'setIsExplicit', 'actions', 'containsProperty', 'containsValue',
  'containsExpression', 'changeValue', 'changeExpression', 'removeProperty',
  'value', 'expression', 'detachFromState', 'attachToState', 'property',
  'objectChanged', 'restoreEntryValuesChanged', 'isExplicitChanged'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPropertyChanges::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPropertyChanges::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPropertyChangesPrivate *QQuickPropertyChanges::d_func()':
    gives 'QQuickPropertyChangesPrivate', which has no cute class yet.
  - Qt's 'const QQuickPropertyChangesPrivate *QQuickPropertyChanges::d_func()
    const': gives 'QQuickPropertyChangesPrivate', which has no cute class
    yet.
  - Qt's 'QQuickPropertyChanges::~QQuickPropertyChanges()': the destructor:
    Python never removes a C++ QQuickPropertyChanges.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPropertyChanges is created at the first use, not by
    'QQuickPropertyChanges(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPropertyChanges.
  - Qt tells when it has removed the C++ QQuickPropertyChanges. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickPropertyChanges::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertychanges.html#tr

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
    #  QString QQuickPropertyChanges::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickPropertyChanges2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPropertyChanges'

  #  A C++ QQuickPropertyChanges Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPropertyChanges'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPropertyChanges::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPropertyChanges::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickPropertyChanges10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickPropertyChanges::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertychanges.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickPropertyChanges::object() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickPropertyChanges6objectEv',
    )
    return QObject._cuteAt(address)

  def restoreEntryValues(self) -> bool:
    """
    Calls Qt's 'bool QQuickPropertyChanges::restoreEntryValues() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#restoreEntryValues
    """
    #  bool QQuickPropertyChanges::restoreEntryValues() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPropertyChanges18restoreEntryValuesEv',
    )

  def isExplicit(self) -> bool:
    """
    Calls Qt's 'bool QQuickPropertyChanges::isExplicit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#isExplicit
    """
    #  bool QQuickPropertyChanges::isExplicit() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPropertyChanges10isExplicitEv',
    )

  @overload(str)
  def containsProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQuickPropertyChanges::containsProperty(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#containsProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickPropertyChanges::containsProperty(const QString &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPropertyChanges16containsPropertyERK7QString',
        name,
    )

  @overload(str)
  def containsValue(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQuickPropertyChanges::containsValue(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#containsValue

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickPropertyChanges::containsValue(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPropertyChanges13containsValueERK7QString', name,
    )

  @overload(str)
  def containsExpression(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQuickPropertyChanges::containsExpression(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#containsExpression

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickPropertyChanges::containsExpression(const QString &name)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPropertyChanges18containsExpressionERK7QString',
        name,
    )

  @overload(str)
  def value(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickPropertyChanges::value(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertychanges.html#value

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickPropertyChanges::value(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickPropertyChanges5valueERK7QString', name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def expression(self, name: str) -> str:
    """
    Calls Qt's 'QString QQuickPropertyChanges::expression(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#expression

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickPropertyChanges::expression(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPropertyChanges10expressionERK7QString', name,
    )

  @overload(str)
  def property(self, name: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickPropertyChanges::property(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#property

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickPropertyChanges::property(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickPropertyChanges8propertyERK7QString', name,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setObject(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::setObject(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#setObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPropertyChanges::setObject(QObject *a0)
    self.uglySide.call(
        'ritual_ZN21QQuickPropertyChanges9setObjectEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(bool)
  def setRestoreEntryValues(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::setRestoreEntryValues(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#setRestoreEntryValues

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickPropertyChanges::setRestoreEntryValues(bool a0)
    self.uglySide.call(
        'ritual_ZN21QQuickPropertyChanges21setRestoreEntryValuesEb', a0,
    )

  @overload(bool)
  def setIsExplicit(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::setIsExplicit(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#setIsExplicit

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickPropertyChanges::setIsExplicit(bool a0)
    self.uglySide.call(
        'ritual_ZN21QQuickPropertyChanges13setIsExplicitEb', a0,
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
    'QQuickPropertyChanges::QQuickPropertyChanges()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#QQuickPropertyChanges
    """
    #  QQuickPropertyChanges::QQuickPropertyChanges()
    self._noteCreation(QQuickPropertyChanges, lambda: Rituals.call(
        'ritual_ZN21QQuickPropertyChangesC1Ev',
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

  def actions(self) -> QList[QQuickStateAction]:
    """
    Calls Qt's 'ActionList QQuickPropertyChanges::actions()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpropertychanges.html#actions

    Returns
    -------

    QList[QQuickStateAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  ActionList QQuickPropertyChanges::actions()
    address = self.uglySide.call(
        'ritual_ZN21QQuickPropertyChanges7actionsEv',
    )
    from . import QQuickStateAction
    return QList[QQuickStateAction]._cuteOwning(address)

  @overload(str, QVariant)
  def changeValue(self, name: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::changeValue(const QString &name,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#changeValue

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickPropertyChanges::changeValue(const QString &name, const
    #      QVariant &value)
    self.uglySide.call(
        'ritual_ZN21QQuickPropertyChanges11changeValueERK7QStringRK8QVarian'
        't',
        name, self._valueOf(value),
    )

  @overload(str, str)
  def changeExpression(self, name: str, expression: str) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::changeExpression(const QString
    &name, const QString &expression)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#changeExpression

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    expression : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPropertyChanges::changeExpression(const QString &name,
    #      const QString &expression)
    self.uglySide.call(
        'ritual_ZN21QQuickPropertyChanges16changeExpressionERK7QStringS2_',
        name, expression,
    )

  @overload(str)
  def removeProperty(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::removeProperty(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#removeProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickPropertyChanges::removeProperty(const QString &name)
    self.uglySide.call(
        'ritual_ZN21QQuickPropertyChanges14removePropertyERK7QString', name,
    )

  def detachFromState(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::detachFromState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#detachFromState
    """
    #  void QQuickPropertyChanges::detachFromState()
    self.uglySide.call('ritual_ZN21QQuickPropertyChanges15detachFromStateEv')

  def attachToState(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::attachToState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#attachToState
    """
    #  void QQuickPropertyChanges::attachToState()
    self.uglySide.call('ritual_ZN21QQuickPropertyChanges13attachToStateEv')

  def objectChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::objectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#objectChanged
    """
    #  void QQuickPropertyChanges::objectChanged()
    self.uglySide.call('ritual_ZN21QQuickPropertyChanges13objectChangedEv')

  def restoreEntryValuesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::restoreEntryValuesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html
    """
    #  void QQuickPropertyChanges::restoreEntryValuesChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickPropertyChanges25restoreEntryValuesChangedEv',
    )

  def isExplicitChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPropertyChanges::isExplicitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpropertychanges.html#isExplicitChanged
    """
    #  void QQuickPropertyChanges::isExplicitChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickPropertyChanges17isExplicitChangedEv',
    )
