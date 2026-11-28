"""
QQmlBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlbinding_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlBinding to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQmlAbstractBinding, QQmlJavaScriptExpression, QQmlPropertyData
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QObject, QVariant
  from . import QQmlContext, QQmlProperty, QQmlScriptString
  from . import QQmlSourceLocation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QQmlProperty = WAIT['QQmlProperty']
  QQmlScriptString = WAIT['QQmlScriptString']
  QQmlSourceLocation = WAIT['QQmlSourceLocation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlBinding(QQmlJavaScriptExpression, QQmlAbstractBinding):
  """
  The cute side of Qt's QQmlBinding: a plain Python object standing in front
  of one C++ QQmlBinding.

  It is built on the cute 'QQmlJavaScriptExpression', as Qt's QQmlBinding is
  built on Qt's QQmlJavaScriptExpression, and has everything that class has.
  It is built on the cute 'QQmlAbstractBinding' as well, as Qt's QQmlBinding
  is built on Qt's QQmlAbstractBinding too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QQmlBinding that has a ritual and that Python can
  call so far, 19 names in all: 'create', 'kind',
  'mustCaptureBindableProperty', 'refresh', 'setEnabled', 'expression',
  'update', 'printBindingLoopError', 'evaluate', 'expressionChanged',
  'sourceLocation', 'setSourceLocation', 'setBoundFunction',
  'hasBoundFunction', 'dependencies', 'hasDependencies', 'write',
  'slowWrite', 'newBinding'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlBinding *QQmlBinding::create(const QQmlPropertyData *a0, const
    QString &a1, QObject *a2, const QQmlRefPointer<QQmlContextData> &a3,
    const QString &url, quint16 lineNumber)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QQmlBinding *QQmlBinding::create(const QQmlPropertyData *property,
    QV4::Function *function, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlBinding *QQmlBinding::create(QMetaType propertyType,
    QV4::Function *function, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt, QV4::ExecutionContext *scope)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlBinding *QQmlBinding::createTranslationBinding(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
    QV4::CompiledData::Binding *binding, QObject *obj, const
    QQmlRefPointer<QQmlContextData> &ctxt)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QQmlBinding *QQmlBinding::createTranslationBinding(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
    QQmlRefPointer<QQmlContextData> &ctxt, const QString &propertyName, const
    QQmlTranslation &translationData, const QQmlSourceLocation &location,
    QObject *obj)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlBinding::~QQmlBinding()': the destructor: Python never removes
    a C++ QQmlBinding.
  - Qt's 'bool QQmlBinding::evaluate(void *result, QMetaType type)': names
    'void', which has no cute class yet.
  - Qt's 'void QQmlBinding::doUpdate(const DeleteWatcher &watcher,
    QQmlPropertyData::WriteFlags flags, QV4::Scope &scope)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QQmlBinding::write(void *result, QMetaType type, bool
    isUndefined, QQmlPropertyData::WriteFlags flags)': names 'void', which
    has no cute class yet.
  - Qt's 'bool QQmlBinding::slowWrite(const QQmlPropertyData &core, const
    QQmlPropertyData &valueTypeData, const void *result, QMetaType
    resultType, bool isUndefined, QQmlPropertyData::WriteFlags flags)': names
    'void', which has no cute class yet.
  - Qt's 'QV4::ReturnedValue QQmlBinding::evaluate(bool *isUndefined)': takes
    a number to change where it is.
  - Qt's 'void QQmlBinding::handleWriteError(const void *result, QMetaType
    resultType, QMetaType metaType)': names 'void', which has no cute class
    yet.

  What has no ritual
  ------------------

  1 of the 33 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQmlBinding is created at the first use, not by
    'QQmlBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlBinding.
  - Each name of Qt's QQmlBinding that has no cute function yet,
    'createTranslationBinding', 'doUpdate', 'getPropertyType',
    'handleWriteError', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlPropertyData, QQmlScriptString, QObject, QQmlContext)
  @overload(QQmlPropertyData, QQmlScriptString, QObject, NoneType)
  @overload(QQmlPropertyData, QQmlScriptString, NoneType, QQmlContext)
  @overload(QQmlPropertyData, QQmlScriptString, NoneType, NoneType)
  @overload(NoneType, QQmlScriptString, QObject, QQmlContext)
  @overload(NoneType, QQmlScriptString, QObject, NoneType)
  @overload(NoneType, QQmlScriptString, NoneType, QQmlContext)
  @overload(NoneType, QQmlScriptString, NoneType, NoneType)
  def create(
      a0: Optional[QQmlPropertyData],
      a1: QQmlScriptString,
      a2: Optional[QObject],
      a3: Optional[QQmlContext],
  ) -> Optional[QQmlBinding]:
    """
    Calls Qt's 'QQmlBinding *QQmlBinding::create(const QQmlPropertyData *a0,
    const QQmlScriptString &a1, QObject *a2, QQmlContext *a3)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#create

    Parameters
    ----------

    a0 : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.

    a2 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a3 : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlBinding *QQmlBinding::create(const QQmlPropertyData *a0, const
    #      QQmlScriptString &a1, QObject *a2, QQmlContext *a3)
    address = Rituals.call(
        'ritual_ZN11QQmlBinding6createEPK16QQmlPropertyDataRK16QQmlScriptSt'
        'ringP7QObjectP11QQmlContext',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
        CuteMixin._addressOf(a2, 'QObject'), CuteMixin._addressOf(a3),
    )
    return QQmlBinding._cuteAt(address)

  @staticmethod
  @overload(QQmlPropertyData)
  @overload(NoneType)
  def newBinding(
      property: Optional[QQmlPropertyData],
  ) -> Optional[QQmlBinding]:
    """
    Calls Qt's 'QQmlBinding *QQmlBinding::newBinding(const QQmlPropertyData
    *property)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#newBinding

    Parameters
    ----------

    property : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlBinding *QQmlBinding::newBinding(const QQmlPropertyData *property)
    address = Rituals.call(
        'ritual_ZN11QQmlBinding10newBindingEPK16QQmlPropertyData',
        CuteMixin._addressOf(property),
    )
    return QQmlBinding._cuteAt(address)

  @staticmethod
  @overload(QMetaType)
  def newBinding(propertyType: QMetaType) -> Optional[QQmlBinding]:
    """
    Calls Qt's 'QQmlBinding *QQmlBinding::newBinding(QMetaType
    propertyType)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#newBinding

    Parameters
    ----------

    propertyType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    Optional[QQmlBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlBinding *QQmlBinding::newBinding(QMetaType propertyType)
    address = Rituals.call(
        'ritual_ZN11QQmlBinding10newBindingE9QMetaType',
        CuteMixin._valueOf(propertyType),
    )
    return QQmlBinding._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlBinding'

  #  Qt's QQmlBinding is built on more than one class. The part of a C++
  #  QQmlBinding that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlAbstractBinding': 'ritual_cast_QQmlBinding_QQmlAbstractBinding',
  }

  #  A C++ QQmlBinding Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlBinding'

  #  The functions Qt calls itself that QQmlBinding is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'doUpdate': (
          'void QQmlBinding::doUpdate(const DeleteWatcher &, '
          'QQmlPropertyData::WriteFlags, QV4::Scope &)',
      ),
  }

  #  The functions Qt calls itself that QQmlBinding is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'hasDependencies': (
          ('_ZNK11QQmlBinding15hasDependenciesEv',
           ('bool', 'number', ''),
           ()),
      ),
      'write': (
          ('_ZN11QQmlBinding5writeERKN3QV45ValueEb6QFlagsIN16QQmlPropertyDa'
           'ta9WriteFlagEE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtQml:QV4.Value'),
               ('bool', 'number', ''),
               ('int', 'flags', 'QtQml:QQmlPropertyData.WriteFlag'),
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

  def kind(self) -> QQmlAbstractBinding.Kind:
    """
    Calls Qt's 'Kind QQmlBinding::kind() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#kind

    Returns
    -------

    QQmlAbstractBinding.Kind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlAbstractBinding.Kind(number)' gives.
    """
    #  Kind QQmlBinding::kind() const
    return QQmlAbstractBinding.Kind(self.uglySide.call(
        'ritual_ZNK11QQmlBinding4kindEv',
    ))

  def mustCaptureBindableProperty(self) -> bool:
    """
    Calls Qt's 'bool QQmlBinding::mustCaptureBindableProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbinding.html#mustCaptureBindableProperty
    """
    #  bool QQmlBinding::mustCaptureBindableProperty() const
    return self.uglySide.call(
        'ritual_ZNK11QQmlBinding27mustCaptureBindablePropertyEv',
    )

  def expression(self) -> str:
    """
    Calls Qt's 'QString QQmlBinding::expression() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#expression

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlBinding::expression() const
    ritual = 'ritual_ZNK11QQmlBinding10expressionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQmlBinding10expressionEv'
    return self.uglySide.call(ritual)

  def sourceLocation(self) -> QQmlSourceLocation:
    """
    Calls Qt's 'QQmlSourceLocation QQmlBinding::sourceLocation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#sourceLocation

    Returns
    -------

    QQmlSourceLocation
      A new cute QQmlSourceLocation around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlSourceLocation QQmlBinding::sourceLocation() const
    ritual = 'ritual_ZNK11QQmlBinding14sourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQmlBinding14sourceLocationEv'
    address = self.uglySide.call(ritual)
    from . import QQmlSourceLocation
    return QQmlSourceLocation._cuteOwning(address)

  def hasBoundFunction(self) -> bool:
    """
    Calls Qt's 'bool QQmlBinding::hasBoundFunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#hasBoundFunction
    """
    #  bool QQmlBinding::hasBoundFunction() const
    return self.uglySide.call('ritual_ZNK11QQmlBinding16hasBoundFunctionEv')

  def dependencies(self) -> QList[QQmlProperty]:
    """
    Calls Qt's 'QList<QQmlProperty> QQmlBinding::dependencies() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#dependencies

    Returns
    -------

    QList[QQmlProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlProperty> QQmlBinding::dependencies() const
    address = self.uglySide.call('ritual_ZNK11QQmlBinding12dependenciesEv')
    from . import QQmlProperty
    return QList[QQmlProperty]._cuteOwning(address)

  def hasDependencies(self) -> bool:
    """
    Calls Qt's 'bool QQmlBinding::hasDependencies() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#hasDependencies
    """
    #  bool QQmlBinding::hasDependencies() const
    ritual = 'ritual_ZNK11QQmlBinding15hasDependenciesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQmlBinding15hasDependenciesEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  @overload(bool, QQmlPropertyData.WriteFlags)
  def setEnabled(
      self,
      a0: bool,
      flags: QQmlPropertyData.WriteFlags = (
          QQmlPropertyData.WriteFlags.DontRemoveBinding),
  ) -> None:
    """
    Calls Qt's 'void QQmlBinding::setEnabled(bool a0,
    QQmlPropertyData::WriteFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.

    flags : QQmlPropertyData.WriteFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlPropertyData.WriteFlags.DontRemoveBinding.
    """
    #  void QQmlBinding::setEnabled(bool a0, QQmlPropertyData::WriteFlags
    #      flags)
    ritual = (
        'ritual_ZN11QQmlBinding10setEnabledEb6QFlagsIN16QQmlPropertyData9Wr'
        'iteFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQmlBinding10setEnabledEb6QFlagsIN16QQmlPropertyD'
          'ata9WriteFlagEE')
    self.uglySide.call(ritual, a0, flags.value)

  @overload(QQmlSourceLocation)
  def setSourceLocation(self, location: QQmlSourceLocation) -> None:
    """
    Calls Qt's 'void QQmlBinding::setSourceLocation(const QQmlSourceLocation
    &location)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#setSourceLocation

    Parameters
    ----------

    location : QQmlSourceLocation
      Passed on as a value: Qt reads the C++ QQmlSourceLocation, which stays
      Python's own.
    """
    #  void QQmlBinding::setSourceLocation(const QQmlSourceLocation
    #      &location)
    self.uglySide.call(
        'ritual_ZN11QQmlBinding17setSourceLocationERK18QQmlSourceLocation',
        self._valueOf(location),
    )

  @overload(WAIT['QV4.BoundFunction'])
  @overload(NoneType)
  def setBoundFunction(
      self,
      boundFunction: Optional[QV4.BoundFunction],
  ) -> None:
    """
    Calls Qt's 'void QQmlBinding::setBoundFunction(QV4::BoundFunction
    *boundFunction)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#setBoundFunction

    Parameters
    ----------

    boundFunction : Optional[QV4.BoundFunction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlBinding::setBoundFunction(QV4::BoundFunction *boundFunction)
    self.uglySide.call(
        'ritual_ZN11QQmlBinding16setBoundFunctionEPN3QV413BoundFunctionE',
        self._addressOf(boundFunction),
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

  def refresh(self) -> None:
    """
    Calls Qt's 'void QQmlBinding::refresh()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#refresh
    """
    #  void QQmlBinding::refresh()
    ritual = 'ritual_ZN11QQmlBinding7refreshEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQmlBinding7refreshEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(QQmlPropertyData.WriteFlags)
  def update(
      self,
      flags: QQmlPropertyData.WriteFlags = (
          QQmlPropertyData.WriteFlags.DontRemoveBinding),
  ) -> None:
    """
    Calls Qt's 'void QQmlBinding::update(QQmlPropertyData::WriteFlags
    flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#update

    Parameters
    ----------

    flags : QQmlPropertyData.WriteFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlPropertyData.WriteFlags.DontRemoveBinding.
    """
    #  void QQmlBinding::update(QQmlPropertyData::WriteFlags flags)
    self.uglySide.call(
        'ritual_ZN11QQmlBinding6updateE6QFlagsIN16QQmlPropertyData9WriteFla'
        'gEE',
        flags.value,
    )

  @overload(QQmlProperty)
  def printBindingLoopError(self, prop: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQmlBinding::printBindingLoopError(const QQmlProperty
    &prop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlbinding.html#printBindingLoopError

    Parameters
    ----------

    prop : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQmlBinding::printBindingLoopError(const QQmlProperty &prop)
    ritual = 'ritual_ZN11QQmlBinding21printBindingLoopErrorERK12QQmlProperty'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQmlBinding21printBindingLoopErrorERK12QQmlProper'
          'ty')
    self.uglySide.call(ritual, self._valueOf(prop))

  def evaluate(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlBinding::evaluate()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#evaluate

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlBinding::evaluate()
    address = self.uglySide.call('ritual_ZN11QQmlBinding8evaluateEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def expressionChanged(self) -> None:
    """
    Calls Qt's 'void QQmlBinding::expressionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#expressionChanged
    """
    #  void QQmlBinding::expressionChanged()
    ritual = 'ritual_ZN11QQmlBinding17expressionChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQmlBinding17expressionChangedEv'
    self.uglySide.call(ritual)

  @overload(WAIT['QV4.Value'], bool, QQmlPropertyData.WriteFlags)
  def write(
      self,
      result: QV4.Value,
      isUndefined: bool,
      flags: QQmlPropertyData.WriteFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlBinding::write(const QV4::Value &result, bool
    isUndefined, QQmlPropertyData::WriteFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#write

    Parameters
    ----------

    result : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    isUndefined : bool
      Passed on as it is.

    flags : QQmlPropertyData.WriteFlags
      Passed on as its number.
    """
    #  bool QQmlBinding::write(const QV4::Value &result, bool isUndefined,
    #      QQmlPropertyData::WriteFlags flags)
    return self.uglySide.call(
        'ritual_ZN11QQmlBinding5writeERKN3QV45ValueEb6QFlagsIN16QQmlPropert'
        'yData9WriteFlagEE',
        self._valueOf(result), isUndefined, flags.value,
    )

  @overload(
      QQmlPropertyData, QQmlPropertyData, WAIT['QV4.Value'], bool,
      QQmlPropertyData.WriteFlags,
  )
  def slowWrite(
      self,
      core: QQmlPropertyData,
      valueTypeData: QQmlPropertyData,
      result: QV4.Value,
      isUndefined: bool,
      flags: QQmlPropertyData.WriteFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlBinding::slowWrite(const QQmlPropertyData &core,
    const QQmlPropertyData &valueTypeData, const QV4::Value &result, bool
    isUndefined, QQmlPropertyData::WriteFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlbinding.html#slowWrite

    Parameters
    ----------

    core : QQmlPropertyData
      Passed on as a value: Qt reads the C++ QQmlPropertyData, which stays
      Python's own.

    valueTypeData : QQmlPropertyData
      Passed on as a value: Qt reads the C++ QQmlPropertyData, which stays
      Python's own.

    result : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    isUndefined : bool
      Passed on as it is.

    flags : QQmlPropertyData.WriteFlags
      Passed on as its number.
    """
    #  bool QQmlBinding::slowWrite(const QQmlPropertyData &core, const
    #      QQmlPropertyData &valueTypeData, const QV4::Value &result, bool
    #      isUndefined, QQmlPropertyData::WriteFlags flags)
    return self.uglySide.call(
        'ritual_ZN11QQmlBinding9slowWriteERK16QQmlPropertyDataS2_RKN3QV45Va'
        'lueEb6QFlagsINS0_9WriteFlagEE',
        self._valueOf(core), self._valueOf(valueTypeData),
        self._valueOf(result), isUndefined, flags.value,
    )

  @staticmethod
  def createTranslationBinding(*__, **_) -> Never:
    """
    - Qt's 'QQmlBinding *QQmlBinding::createTranslationBinding(const
      QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
      QV4::CompiledData::Binding *binding, QObject *obj, const
      QQmlRefPointer<QQmlContextData> &ctxt)': takes a type Python has no way
      to hand over yet.
    - Qt's 'QQmlBinding *QQmlBinding::createTranslationBinding(const
      QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const
      QQmlRefPointer<QQmlContextData> &ctxt, const QString &propertyName,
      const QQmlTranslation &translationData, const QQmlSourceLocation
      &location, QObject *obj)': takes a type Python has no way to hand over
      yet.
    """
    raise NotImplementedError(
        "'QQmlBinding.createTranslationBinding' has no cute function yet. "
        "Qt's 'QQmlBinding *QQmlBinding::createTranslationBinding(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const "
        "QV4::CompiledData::Binding *binding, QObject *obj, const "
        "QQmlRefPointer<QQmlContextData> &ctxt)': takes a type Python has "
        "no way to hand over yet. Qt's 'QQmlBinding "
        "*QQmlBinding::createTranslationBinding(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, const "
        "QQmlRefPointer<QQmlContextData> &ctxt, const QString "
        "&propertyName, const QQmlTranslation &translationData, const "
        "QQmlSourceLocation &location, QObject *obj)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def doUpdate(*__, **_) -> Never:
    """
    Qt's 'void QQmlBinding::doUpdate(const DeleteWatcher &watcher,
    QQmlPropertyData::WriteFlags flags, QV4::Scope &scope)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlBinding.doUpdate' has no cute function yet. Qt's 'void "
        "QQmlBinding::doUpdate(const DeleteWatcher &watcher, "
        "QQmlPropertyData::WriteFlags flags, QV4::Scope &scope)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def getPropertyType(*__, **_) -> Never:
    """
    Qt's 'int QQmlBinding::getPropertyType() const': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQmlBinding.getPropertyType' has no cute function yet. Qt's 'int "
        "QQmlBinding::getPropertyType() const': cannot be called and cannot "
        "be called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def handleWriteError(*__, **_) -> Never:
    """
    Qt's 'void QQmlBinding::handleWriteError(const void *result, QMetaType
    resultType, QMetaType metaType)': names 'void', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlBinding.handleWriteError' has no cute function yet. Qt's "
        "'void QQmlBinding::handleWriteError(const void *result, QMetaType "
        "resultType, QMetaType metaType)': names 'void', which has no cute "
        "class yet.")
