"""
QQmlObjectCreator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlobjectcreator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlObjectCreator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlData, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQmlInstantiationInterrupt, QQmlProperty, QQmlPropertyData
  from . import QQmlPropertyPrivate, RequiredProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlInstantiationInterrupt = WAIT['QQmlInstantiationInterrupt']
  QQmlProperty = WAIT['QQmlProperty']
  QQmlPropertyData = WAIT['QQmlPropertyData']
  QQmlPropertyPrivate = WAIT['QQmlPropertyPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlObjectCreator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlObjectCreator: a plain Python object standing in
  front of one C++ QQmlObjectCreator.

  What exists
  -----------

  Every function of Qt's QQmlObjectCreator that has a ritual and that Python
  can call so far, 29 names in all: 'tr', 'create',
  'populateDeferredProperties', 'populateDeferredBinding',
  'populateDeferredInstance', 'finalizePopulateDeferred', 'clear',
  'requiredProperties', 'componentHadTopLevelRequiredProperties',
  'removePendingBinding', 'initializeDData', 'initializePropertyCache',
  'initializeParent', 'populateInstanceAndAliasBindings', 'createInstance',
  'initializeComponent', 'initializeComposite', 'initializeNonComposite',
  'populateInstance', 'populateDeferred', 'setPropertyBinding',
  'setPropertyValue', 'setupFunctions', 'stringAt', 'recordError',
  'registerObjectWithContextById', 'currentQmlContext', 'resolvedType',
  'registerPostHocRequiredProperties'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlObjectCreator::QQmlObjectCreator(const
    QQmlRefPointer<QQmlContextData> &parentContext, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
    QQmlRefPointer<QQmlContextData> &creationContext, const QString
    &inlineComponentName, QQmlIncubatorPrivate *incubator)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlObjectCreator::~QQmlObjectCreator()': the destructor: Python
    never removes a C++ QQmlObjectCreator.
  - Qt's 'void QQmlObjectCreator::beginPopulateDeferred(const
    QQmlRefPointer<QQmlContextData> &context)': takes a type Python has no
    way to hand over yet.
  - Qt's 'bool QQmlObjectCreator::finalize(QQmlInstantiationInterrupt
    &interrupt)': takes a type Python has no way to hand over yet.
  - Qt's 'QObject *QQmlObjectCreator::createObjectInContext(int objectIndex,
    QObject *parent, const QQmlRefPointer<QQmlContextData>
    &existingContext)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData> QQmlObjectCreator::rootContext()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlComponentAttached **QQmlObjectCreator::componentAttachment()':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlObjectCreator::parentContextData() const': gives a type Python has no
    way to take yet.
  - Qt's 'std::vector<QQmlGuard<QObject>>
    &QQmlObjectCreator::allCreatedObjects()': gives a type Python has no way
    to take yet.
  - Qt's 'QQmlComponent *QQmlObjectCreator::createComponent(QQmlEngine
    *engine, QV4::ExecutableCompilationUnit *compilationUnit, int index,
    QObject *parent, const QQmlRefPointer<QQmlContextData> &context)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QQmlObjectCreator::repopulateBindings(int index, QObject
    *instance, const QQmlRefPointer<QQmlContextData> &instanceContext,
    InitFlags flags)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlObjectCreator::QQmlObjectCreator(const
    QQmlRefPointer<QQmlContextData> &contextData, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
    QString inlineComponentName, QQmlObjectCreatorSharedState
    *inheritedSharedState, bool isContextObject)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQmlObjectCreator::init(const QQmlRefPointer<QQmlContextData>
    &parentContext)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlObjectCreator::setupBindings(BindingSetupFlags mode)':
    names the enum 'QQmlObjectCreator::BindingMode', whose class cannot be
    named here.

  What has no ritual
  ------------------

  1 of the 45 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlObjectCreator is created at the first use, not by
    'QQmlObjectCreator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlObjectCreator.
  - Each name of Qt's QQmlObjectCreator that has no cute function yet,
    '__init__', 'allCreatedObjects', 'beginPopulateDeferred',
    'componentAttachment', 'createComponent', 'createObjectInContext',
    'doPopulateDeferred', 'finalize', 'init', 'parentContextData',
    'repopulateBindings', 'rootContext', 'setupBindings', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlObjectCreator, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CreationFlags(CuteNum):
    """
    The enum 'QQmlObjectCreator::CreationFlags' of Qt, with the 2 names Qt
    gives in it.
    """

    NormalObject = Kee[int](1)
    InlineComponent = Kee[int](2)

  class InitFlag(CuteFlags, number='unsigned char', scoped=True):
    """
    The flags enum 'QQmlObjectCreator::InitFlag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QQmlObjectCreator::InitFlags'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    NULL = 0x0
    IsDocumentRoot = 0x1
    IsContextObject = 0x2
    IsImplicitComponent = 0x4

  InitFlags = InitFlag

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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QQmlObjectCreator::tr(const char *sourceText, const
    char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectcreator.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlObjectCreator::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN17QQmlObjectCreator2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlObjectCreator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def componentHadTopLevelRequiredProperties(self) -> bool:
    """
    Calls Qt's 'bool
    QQmlObjectCreator::componentHadTopLevelRequiredProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html
    """
    #  bool QQmlObjectCreator::componentHadTopLevelRequiredProperties() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlObjectCreator38componentHadTopLevelRequiredPropert'
        'iesEv',
    )

  @overload(int)
  def stringAt(self, idx: int) -> str:
    """
    Calls Qt's 'QString QQmlObjectCreator::stringAt(int idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectcreator.html#stringAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlObjectCreator::stringAt(int idx) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlObjectCreator8stringAtEi', idx,
    )

  @overload(int)
  def resolvedType(self, id: int) -> Optional[QV4.ResolvedTypeReference]:
    """
    Calls Qt's 'QV4::ResolvedTypeReference
    *QQmlObjectCreator::resolvedType(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#resolvedType

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.ResolvedTypeReference]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ResolvedTypeReference *QQmlObjectCreator::resolvedType(int id)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlObjectCreator12resolvedTypeEi', id,
    )
    return QV4.ResolvedTypeReference._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlPropertyData, WAIT['QV4.CompiledData.Binding'])
  @overload(QQmlPropertyData, NoneType)
  @overload(NoneType, WAIT['QV4.CompiledData.Binding'])
  @overload(NoneType, NoneType)
  def setPropertyBinding(
      self,
      property: Optional[QQmlPropertyData],
      binding: Optional[QV4.CompiledData.Binding],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlObjectCreator::setPropertyBinding(const
    QQmlPropertyData *property, const QV4::CompiledData::Binding *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#setPropertyBinding

    Parameters
    ----------

    property : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlObjectCreator::setPropertyBinding(const QQmlPropertyData
    #      *property, const QV4::CompiledData::Binding *binding)
    return self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator18setPropertyBindingEPK16QQmlPropertyD'
        'ataPKN3QV412CompiledData7BindingE',
        self._addressOf(property), self._addressOf(binding),
    )

  @overload(QQmlPropertyData, WAIT['QV4.CompiledData.Binding'])
  @overload(QQmlPropertyData, NoneType)
  @overload(NoneType, WAIT['QV4.CompiledData.Binding'])
  @overload(NoneType, NoneType)
  def setPropertyValue(
      self,
      property: Optional[QQmlPropertyData],
      binding: Optional[QV4.CompiledData.Binding],
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::setPropertyValue(const
    QQmlPropertyData *property, const QV4::CompiledData::Binding *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#setPropertyValue

    Parameters
    ----------

    property : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlObjectCreator::setPropertyValue(const QQmlPropertyData
    #      *property, const QV4::CompiledData::Binding *binding)
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator16setPropertyValueEPK16QQmlPropertyDat'
        'aPKN3QV412CompiledData7BindingE',
        self._addressOf(property), self._addressOf(binding),
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
    - Qt's 'QQmlObjectCreator::QQmlObjectCreator(const
      QQmlRefPointer<QQmlContextData> &parentContext, const
      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
      QQmlRefPointer<QQmlContextData> &creationContext, const QString
      &inlineComponentName, QQmlIncubatorPrivate *incubator)': takes a type
      Python has no way to hand over yet.
    - Qt's 'QQmlObjectCreator::QQmlObjectCreator(const
      QQmlRefPointer<QQmlContextData> &contextData, const
      QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, const
      QString inlineComponentName, QQmlObjectCreatorSharedState
      *inheritedSharedState, bool isContextObject)': takes a type Python has
      no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.__init__' has no cute function yet. Qt's "
        "'QQmlObjectCreator::QQmlObjectCreator(const "
        "QQmlRefPointer<QQmlContextData> &parentContext, const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, "
        "const QQmlRefPointer<QQmlContextData> &creationContext, const "
        "QString &inlineComponentName, QQmlIncubatorPrivate *incubator)': "
        "takes a type Python has no way to hand over yet. Qt's "
        "'QQmlObjectCreator::QQmlObjectCreator(const "
        "QQmlRefPointer<QQmlContextData> &contextData, const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit, "
        "const QString inlineComponentName, QQmlObjectCreatorSharedState "
        "*inheritedSharedState, bool isContextObject)': takes a type Python "
        "has no way to hand over yet.")

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

  @overload()
  @overload(int)
  @overload(int, QObject)
  @overload(int, NoneType)
  @overload(int, QObject, QQmlInstantiationInterrupt)
  @overload(int, QObject, NoneType)
  @overload(int, NoneType, QQmlInstantiationInterrupt)
  @overload(int, NoneType, NoneType)
  @overload(int, QObject, QQmlInstantiationInterrupt, int)
  @overload(int, QObject, NoneType, int)
  @overload(int, NoneType, QQmlInstantiationInterrupt, int)
  @overload(int, NoneType, NoneType, int)
  def create(
      self,
      subComponentIndex: int = -1,
      parent: Optional[QObject] = None,
      interrupt: Optional[QQmlInstantiationInterrupt] = None,
      flags: int = 1,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlObjectCreator::create(int subComponentIndex,
    QObject *parent, QQmlInstantiationInterrupt *interrupt, int flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectcreator.html#create

    Parameters
    ----------

    subComponentIndex : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    interrupt : Optional[QQmlInstantiationInterrupt]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 1.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlObjectCreator::create(int subComponentIndex, QObject
    #      *parent, QQmlInstantiationInterrupt *interrupt, int flags)
    address = self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator6createEiP7QObjectP26QQmlInstantiation'
        'Interrupti',
        subComponentIndex, self._addressOf(parent, 'QObject'),
        self._addressOf(interrupt), flags,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(QObject, QQmlData.DeferredData)
  @overload(QObject, NoneType)
  @overload(NoneType, QQmlData.DeferredData)
  @overload(NoneType, NoneType)
  def populateDeferredProperties(
      self,
      instance: Optional[QObject],
      deferredData: Optional[QQmlData.DeferredData],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlObjectCreator::populateDeferredProperties(QObject
    *instance, const QQmlData::DeferredData *deferredData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#populateDeferredProperties

    Parameters
    ----------

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    deferredData : Optional[QQmlData.DeferredData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlObjectCreator::populateDeferredProperties(QObject *instance,
    #      const QQmlData::DeferredData *deferredData)
    return self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator26populateDeferredPropertiesEP7QObject'
        'PKN8QQmlData12DeferredDataE',
        self._addressOf(instance, 'QObject'), self._addressOf(deferredData),
    )

  @overload(QQmlProperty, int, WAIT['QV4.CompiledData.Binding'])
  @overload(QQmlProperty, int, NoneType)
  def populateDeferredBinding(
      self,
      qmlProperty: QQmlProperty,
      deferredIndex: int,
      binding: Optional[QV4.CompiledData.Binding],
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::populateDeferredBinding(const
    QQmlProperty &qmlProperty, int deferredIndex, const
    QV4::CompiledData::Binding *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#populateDeferredBinding

    Parameters
    ----------

    qmlProperty : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    deferredIndex : int
      Passed on as it is.

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlObjectCreator::populateDeferredBinding(const QQmlProperty
    #      &qmlProperty, int deferredIndex, const QV4::CompiledData::Binding
    #      *binding)
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator23populateDeferredBindingERK12QQmlProp'
        'ertyiPKN3QV412CompiledData7BindingE',
        self._valueOf(qmlProperty), deferredIndex, self._addressOf(binding),
    )

  @overload(QObject, int, int, QObject, QObject, QQmlPropertyData)
  @overload(QObject, int, int, QObject, QObject, NoneType)
  @overload(QObject, int, int, QObject, NoneType, QQmlPropertyData)
  @overload(QObject, int, int, QObject, NoneType, NoneType)
  @overload(QObject, int, int, NoneType, QObject, QQmlPropertyData)
  @overload(QObject, int, int, NoneType, QObject, NoneType)
  @overload(QObject, int, int, NoneType, NoneType, QQmlPropertyData)
  @overload(QObject, int, int, NoneType, NoneType, NoneType)
  @overload(NoneType, int, int, QObject, QObject, QQmlPropertyData)
  @overload(NoneType, int, int, QObject, QObject, NoneType)
  @overload(NoneType, int, int, QObject, NoneType, QQmlPropertyData)
  @overload(NoneType, int, int, QObject, NoneType, NoneType)
  @overload(NoneType, int, int, NoneType, QObject, QQmlPropertyData)
  @overload(NoneType, int, int, NoneType, QObject, NoneType)
  @overload(NoneType, int, int, NoneType, NoneType, QQmlPropertyData)
  @overload(NoneType, int, int, NoneType, NoneType, NoneType)
  @overload(
      QObject, int, int, QObject, QObject, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(QObject, int, int, QObject, QObject, QQmlPropertyData, NoneType)
  @overload(
      QObject, int, int, QObject, QObject, NoneType,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(QObject, int, int, QObject, QObject, NoneType, NoneType)
  @overload(
      QObject, int, int, QObject, NoneType, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(QObject, int, int, QObject, NoneType, QQmlPropertyData, NoneType)
  @overload(
      QObject, int, int, QObject, NoneType, NoneType,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(QObject, int, int, QObject, NoneType, NoneType, NoneType)
  @overload(
      QObject, int, int, NoneType, QObject, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(QObject, int, int, NoneType, QObject, QQmlPropertyData, NoneType)
  @overload(
      QObject, int, int, NoneType, QObject, NoneType,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(QObject, int, int, NoneType, QObject, NoneType, NoneType)
  @overload(
      QObject, int, int, NoneType, NoneType, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(
      QObject, int, int, NoneType, NoneType, QQmlPropertyData, NoneType,
  )
  @overload(
      QObject, int, int, NoneType, NoneType, NoneType,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(QObject, int, int, NoneType, NoneType, NoneType, NoneType)
  @overload(
      NoneType, int, int, QObject, QObject, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(NoneType, int, int, QObject, QObject, QQmlPropertyData, NoneType)
  @overload(
      NoneType, int, int, QObject, QObject, NoneType,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(NoneType, int, int, QObject, QObject, NoneType, NoneType)
  @overload(
      NoneType, int, int, QObject, NoneType, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(
      NoneType, int, int, QObject, NoneType, QQmlPropertyData, NoneType,
  )
  @overload(
      NoneType, int, int, QObject, NoneType, NoneType,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(NoneType, int, int, QObject, NoneType, NoneType, NoneType)
  @overload(
      NoneType, int, int, NoneType, QObject, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(
      NoneType, int, int, NoneType, QObject, QQmlPropertyData, NoneType,
  )
  @overload(
      NoneType, int, int, NoneType, QObject, NoneType,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(NoneType, int, int, NoneType, QObject, NoneType, NoneType)
  @overload(
      NoneType, int, int, NoneType, NoneType, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(
      NoneType, int, int, NoneType, NoneType, QQmlPropertyData, NoneType,
  )
  @overload(
      NoneType, int, int, NoneType, NoneType, NoneType,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(NoneType, int, int, NoneType, NoneType, NoneType, NoneType)
  def populateDeferredInstance(
      self,
      outerObject: Optional[QObject],
      deferredIndex: int,
      index: int,
      instance: Optional[QObject],
      bindingTarget: Optional[QObject],
      valueTypeProperty: Optional[QQmlPropertyData],
      binding: Optional[QV4.CompiledData.Binding] = None,
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::populateDeferredInstance(QObject
    *outerObject, int deferredIndex, int index, QObject *instance, QObject
    *bindingTarget, const QQmlPropertyData *valueTypeProperty, const
    QV4::CompiledData::Binding *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#populateDeferredInstance

    Parameters
    ----------

    outerObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    deferredIndex : int
      Passed on as it is.

    index : int
      Passed on as it is.

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bindingTarget : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    valueTypeProperty : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQmlObjectCreator::populateDeferredInstance(QObject *outerObject,
    #      int deferredIndex, int index, QObject *instance, QObject
    #      *bindingTarget, const QQmlPropertyData *valueTypeProperty, const
    #      QV4::CompiledData::Binding *binding)
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator24populateDeferredInstanceEP7QObjectii'
        'S1_S1_PK16QQmlPropertyDataPKN3QV412CompiledData7BindingE',
        self._addressOf(outerObject, 'QObject'), deferredIndex, index,
        self._addressOf(instance, 'QObject'), self._addressOf(bindingTarget,
        'QObject'), self._addressOf(valueTypeProperty),
        self._addressOf(binding),
    )

  def finalizePopulateDeferred(self) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::finalizePopulateDeferred()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#finalizePopulateDeferred
    """
    #  void QQmlObjectCreator::finalizePopulateDeferred()
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator24finalizePopulateDeferredEv',
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectcreator.html#clear
    """
    #  void QQmlObjectCreator::clear()
    self.uglySide.call('ritual_ZN17QQmlObjectCreator5clearEv')

  def requiredProperties(self) -> Optional[RequiredProperties]:
    """
    Calls Qt's 'RequiredProperties *QQmlObjectCreator::requiredProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#requiredProperties

    Returns
    -------

    Optional[RequiredProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RequiredProperties *QQmlObjectCreator::requiredProperties()
    address = self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator18requiredPropertiesEv',
    )
    from . import RequiredProperties
    return RequiredProperties._cuteAt(address)

  @overload(QObject, int)
  @overload(NoneType, int)
  def removePendingBinding(
      self,
      target: Optional[QObject],
      propertyIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::removePendingBinding(QObject *target,
    int propertyIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#removePendingBinding

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyIndex : int
      Passed on as it is.
    """
    #  void QQmlObjectCreator::removePendingBinding(QObject *target, int
    #      propertyIndex) const
    self.uglySide.call(
        'ritual_ZNK17QQmlObjectCreator20removePendingBindingEP7QObjecti',
        self._addressOf(target, 'QObject'), propertyIndex,
    )

  @overload(WAIT['QV4.CompiledData.Object'], QObject, QQmlData, InitFlags)
  @overload(WAIT['QV4.CompiledData.Object'], QObject, NoneType, InitFlags)
  @overload(WAIT['QV4.CompiledData.Object'], NoneType, QQmlData, InitFlags)
  @overload(WAIT['QV4.CompiledData.Object'], NoneType, NoneType, InitFlags)
  @overload(NoneType, QObject, QQmlData, InitFlags)
  @overload(NoneType, QObject, NoneType, InitFlags)
  @overload(NoneType, NoneType, QQmlData, InitFlags)
  @overload(NoneType, NoneType, NoneType, InitFlags)
  def initializeDData(
      self,
      obj: Optional[QV4.CompiledData.Object],
      instance: Optional[QObject],
      ddata: Optional[QQmlData],
      flags: InitFlags,
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::initializeDData(const
    QV4::CompiledData::Object *obj, QObject *instance, QQmlData *ddata,
    InitFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#initializeDData

    Parameters
    ----------

    obj : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ddata : Optional[QQmlData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : InitFlags
      Passed on as its number.
    """
    #  void QQmlObjectCreator::initializeDData(const
    #      QV4::CompiledData::Object *obj, QObject *instance, QQmlData
    #      *ddata, InitFlags flags)
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator15initializeDDataEPKN3QV412CompiledDat'
        'a6ObjectEP7QObjectP8QQmlData6QFlagsINS_8InitFlagEE',
        self._addressOf(obj), self._addressOf(instance, 'QObject'),
        self._addressOf(ddata), flags.value,
    )

  @overload(int, QQmlData, WAIT['QV4.ResolvedTypeReference'])
  @overload(int, QQmlData, NoneType)
  @overload(int, NoneType, WAIT['QV4.ResolvedTypeReference'])
  @overload(int, NoneType, NoneType)
  def initializePropertyCache(
      self,
      index: int,
      ddata: Optional[QQmlData],
      typeRef: Optional[QV4.ResolvedTypeReference],
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::initializePropertyCache(int index,
    QQmlData *ddata, const QV4::ResolvedTypeReference *typeRef)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#initializePropertyCache

    Parameters
    ----------

    index : int
      Passed on as it is.

    ddata : Optional[QQmlData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeRef : Optional[QV4.ResolvedTypeReference]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlObjectCreator::initializePropertyCache(int index, QQmlData
    #      *ddata, const QV4::ResolvedTypeReference *typeRef)
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator23initializePropertyCacheEiP8QQmlDataP'
        'KN3QV421ResolvedTypeReferenceE',
        index, self._addressOf(ddata), self._addressOf(typeRef),
    )

  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def initializeParent(
      self,
      instance: Optional[QObject],
      parent: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::initializeParent(QObject *instance,
    QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#initializeParent

    Parameters
    ----------

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlObjectCreator::initializeParent(QObject *instance, QObject
    #      *parent)
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator16initializeParentEP7QObjectS1_',
        self._addressOf(instance, 'QObject'), self._addressOf(parent,
        'QObject'),
    )

  @overload(int, QObject, InitFlags)
  @overload(int, NoneType, InitFlags)
  def populateInstanceAndAliasBindings(
      self,
      index: int,
      instance: Optional[QObject],
      flags: InitFlags,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *QQmlObjectCreator::populateInstanceAndAliasBindings(int index, QObject
    *instance, InitFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : InitFlags
      Passed on as its number.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlObjectCreator::populateInstanceAndAliasBindings(int
    #      index, QObject *instance, InitFlags flags)
    address = self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator32populateInstanceAndAliasBindingsEiP7'
        'QObject6QFlagsINS_8InitFlagEE',
        index, self._addressOf(instance, 'QObject'), flags.value,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(int)
  @overload(int, QObject)
  @overload(int, NoneType)
  @overload(int, QObject, bool)
  @overload(int, NoneType, bool)
  def createInstance(
      self,
      index: int,
      parent: Optional[QObject] = None,
      isContextObject: bool = False,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlObjectCreator::createInstance(int index, QObject
    *parent, bool isContextObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#createInstance

    Parameters
    ----------

    index : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    isContextObject : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlObjectCreator::createInstance(int index, QObject *parent,
    #      bool isContextObject)
    address = self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator14createInstanceEiP7QObjectb',
        index, self._addressOf(parent, 'QObject'), isContextObject,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(WAIT['QV4.CompiledData.Object'], QObject, InitFlags)
  @overload(WAIT['QV4.CompiledData.Object'], NoneType, InitFlags)
  @overload(NoneType, QObject, InitFlags)
  @overload(NoneType, NoneType, InitFlags)
  def initializeComponent(
      self,
      obj: Optional[QV4.CompiledData.Object],
      instance: Optional[QObject],
      flags: InitFlags,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlObjectCreator::initializeComponent(const
    QV4::CompiledData::Object *obj, QObject *instance, InitFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#initializeComponent

    Parameters
    ----------

    obj : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : InitFlags
      Passed on as its number.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlObjectCreator::initializeComponent(const
    #      QV4::CompiledData::Object *obj, QObject *instance, InitFlags
    #      flags)
    address = self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator19initializeComponentEPKN3QV412Compile'
        'dData6ObjectEP7QObject6QFlagsINS_8InitFlagEE',
        self._addressOf(obj), self._addressOf(instance, 'QObject'),
        flags.value,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(
      int, WAIT['QV4.CompiledData.Object'],
      WAIT['QV4.ResolvedTypeReference'], QObject, QObject, InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'],
      WAIT['QV4.ResolvedTypeReference'], QObject, NoneType, InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'],
      WAIT['QV4.ResolvedTypeReference'], NoneType, QObject, InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'],
      WAIT['QV4.ResolvedTypeReference'], NoneType, NoneType, InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'], NoneType, QObject, QObject,
      InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'], NoneType, QObject, NoneType,
      InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'], NoneType, NoneType, QObject,
      InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'], NoneType, NoneType, NoneType,
      InitFlags,
  )
  @overload(
      int, NoneType, WAIT['QV4.ResolvedTypeReference'], QObject, QObject,
      InitFlags,
  )
  @overload(
      int, NoneType, WAIT['QV4.ResolvedTypeReference'], QObject, NoneType,
      InitFlags,
  )
  @overload(
      int, NoneType, WAIT['QV4.ResolvedTypeReference'], NoneType, QObject,
      InitFlags,
  )
  @overload(
      int, NoneType, WAIT['QV4.ResolvedTypeReference'], NoneType, NoneType,
      InitFlags,
  )
  @overload(int, NoneType, NoneType, QObject, QObject, InitFlags)
  @overload(int, NoneType, NoneType, QObject, NoneType, InitFlags)
  @overload(int, NoneType, NoneType, NoneType, QObject, InitFlags)
  @overload(int, NoneType, NoneType, NoneType, NoneType, InitFlags)
  def initializeComposite(
      self,
      index: int,
      obj: Optional[QV4.CompiledData.Object],
      typeRef: Optional[QV4.ResolvedTypeReference],
      instance: Optional[QObject],
      parent: Optional[QObject],
      flags: InitFlags,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlObjectCreator::initializeComposite(int index,
    const QV4::CompiledData::Object *obj, const QV4::ResolvedTypeReference
    *typeRef, QObject *instance, QObject *parent, InitFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#initializeComposite

    Parameters
    ----------

    index : int
      Passed on as it is.

    obj : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeRef : Optional[QV4.ResolvedTypeReference]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : InitFlags
      Passed on as its number.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlObjectCreator::initializeComposite(int index, const
    #      QV4::CompiledData::Object *obj, const QV4::ResolvedTypeReference
    #      *typeRef, QObject *instance, QObject *parent, InitFlags flags)
    address = self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator19initializeCompositeEiPKN3QV412Compil'
        'edData6ObjectEPKNS0_21ResolvedTypeReferenceEP7QObjectS9_6QFlagsINS'
        '_8InitFlagEE',
        index, self._addressOf(obj), self._addressOf(typeRef),
        self._addressOf(instance, 'QObject'), self._addressOf(parent,
        'QObject'), flags.value,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(
      int, WAIT['QV4.CompiledData.Object'],
      WAIT['QV4.ResolvedTypeReference'], QObject, QObject, InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'],
      WAIT['QV4.ResolvedTypeReference'], QObject, NoneType, InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'],
      WAIT['QV4.ResolvedTypeReference'], NoneType, QObject, InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'],
      WAIT['QV4.ResolvedTypeReference'], NoneType, NoneType, InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'], NoneType, QObject, QObject,
      InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'], NoneType, QObject, NoneType,
      InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'], NoneType, NoneType, QObject,
      InitFlags,
  )
  @overload(
      int, WAIT['QV4.CompiledData.Object'], NoneType, NoneType, NoneType,
      InitFlags,
  )
  @overload(
      int, NoneType, WAIT['QV4.ResolvedTypeReference'], QObject, QObject,
      InitFlags,
  )
  @overload(
      int, NoneType, WAIT['QV4.ResolvedTypeReference'], QObject, NoneType,
      InitFlags,
  )
  @overload(
      int, NoneType, WAIT['QV4.ResolvedTypeReference'], NoneType, QObject,
      InitFlags,
  )
  @overload(
      int, NoneType, WAIT['QV4.ResolvedTypeReference'], NoneType, NoneType,
      InitFlags,
  )
  @overload(int, NoneType, NoneType, QObject, QObject, InitFlags)
  @overload(int, NoneType, NoneType, QObject, NoneType, InitFlags)
  @overload(int, NoneType, NoneType, NoneType, QObject, InitFlags)
  @overload(int, NoneType, NoneType, NoneType, NoneType, InitFlags)
  def initializeNonComposite(
      self,
      index: int,
      obj: Optional[QV4.CompiledData.Object],
      typeRef: Optional[QV4.ResolvedTypeReference],
      instance: Optional[QObject],
      parent: Optional[QObject],
      flags: InitFlags,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlObjectCreator::initializeNonComposite(int index,
    const QV4::CompiledData::Object *obj, const QV4::ResolvedTypeReference
    *typeRef, QObject *instance, QObject *parent, InitFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#initializeNonComposite

    Parameters
    ----------

    index : int
      Passed on as it is.

    obj : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeRef : Optional[QV4.ResolvedTypeReference]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : InitFlags
      Passed on as its number.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlObjectCreator::initializeNonComposite(int index, const
    #      QV4::CompiledData::Object *obj, const QV4::ResolvedTypeReference
    #      *typeRef, QObject *instance, QObject *parent, InitFlags flags)
    address = self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator22initializeNonCompositeEiPKN3QV412Com'
        'piledData6ObjectEPKNS0_21ResolvedTypeReferenceEP7QObjectS9_6QFlags'
        'INS_8InitFlagEE',
        index, self._addressOf(obj), self._addressOf(typeRef),
        self._addressOf(instance, 'QObject'), self._addressOf(parent,
        'QObject'), flags.value,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(int, QObject, QObject, QQmlPropertyData)
  @overload(int, QObject, QObject, NoneType)
  @overload(int, QObject, NoneType, QQmlPropertyData)
  @overload(int, QObject, NoneType, NoneType)
  @overload(int, NoneType, QObject, QQmlPropertyData)
  @overload(int, NoneType, QObject, NoneType)
  @overload(int, NoneType, NoneType, QQmlPropertyData)
  @overload(int, NoneType, NoneType, NoneType)
  @overload(
      int, QObject, QObject, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(int, QObject, QObject, QQmlPropertyData, NoneType)
  @overload(
      int, QObject, QObject, NoneType, WAIT['QV4.CompiledData.Binding'],
  )
  @overload(int, QObject, QObject, NoneType, NoneType)
  @overload(
      int, QObject, NoneType, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(int, QObject, NoneType, QQmlPropertyData, NoneType)
  @overload(
      int, QObject, NoneType, NoneType, WAIT['QV4.CompiledData.Binding'],
  )
  @overload(int, QObject, NoneType, NoneType, NoneType)
  @overload(
      int, NoneType, QObject, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(int, NoneType, QObject, QQmlPropertyData, NoneType)
  @overload(
      int, NoneType, QObject, NoneType, WAIT['QV4.CompiledData.Binding'],
  )
  @overload(int, NoneType, QObject, NoneType, NoneType)
  @overload(
      int, NoneType, NoneType, QQmlPropertyData,
      WAIT['QV4.CompiledData.Binding'],
  )
  @overload(int, NoneType, NoneType, QQmlPropertyData, NoneType)
  @overload(
      int, NoneType, NoneType, NoneType, WAIT['QV4.CompiledData.Binding'],
  )
  @overload(int, NoneType, NoneType, NoneType, NoneType)
  def populateInstance(
      self,
      index: int,
      instance: Optional[QObject],
      bindingTarget: Optional[QObject],
      valueTypeProperty: Optional[QQmlPropertyData],
      binding: Optional[QV4.CompiledData.Binding] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlObjectCreator::populateInstance(int index, QObject
    *instance, QObject *bindingTarget, const QQmlPropertyData
    *valueTypeProperty, const QV4::CompiledData::Binding *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#populateInstance

    Parameters
    ----------

    index : int
      Passed on as it is.

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    bindingTarget : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    valueTypeProperty : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QQmlObjectCreator::populateInstance(int index, QObject *instance,
    #      QObject *bindingTarget, const QQmlPropertyData *valueTypeProperty,
    #      const QV4::CompiledData::Binding *binding)
    return self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator16populateInstanceEiP7QObjectS1_PK16QQ'
        'mlPropertyDataPKN3QV412CompiledData7BindingE',
        index, self._addressOf(instance, 'QObject'),
        self._addressOf(bindingTarget, 'QObject'),
        self._addressOf(valueTypeProperty), self._addressOf(binding),
    )

  @overload(QObject, int)
  @overload(NoneType, int)
  def populateDeferred(
      self,
      instance: Optional[QObject],
      deferredIndex: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::populateDeferred(QObject *instance,
    int deferredIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#populateDeferred

    Parameters
    ----------

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    deferredIndex : int
      Passed on as it is.
    """
    #  void QQmlObjectCreator::populateDeferred(QObject *instance, int
    #      deferredIndex)
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator16populateDeferredEP7QObjecti',
        self._addressOf(instance, 'QObject'), deferredIndex,
    )

  @overload(
      QObject, int, QQmlPropertyPrivate, WAIT['QV4.CompiledData.Binding'],
  )
  @overload(QObject, int, QQmlPropertyPrivate, NoneType)
  @overload(QObject, int, NoneType, WAIT['QV4.CompiledData.Binding'])
  @overload(QObject, int, NoneType, NoneType)
  @overload(
      NoneType, int, QQmlPropertyPrivate, WAIT['QV4.CompiledData.Binding'],
  )
  @overload(NoneType, int, QQmlPropertyPrivate, NoneType)
  @overload(NoneType, int, NoneType, WAIT['QV4.CompiledData.Binding'])
  @overload(NoneType, int, NoneType, NoneType)
  def populateDeferred(
      self,
      instance: Optional[QObject],
      deferredIndex: int,
      qmlProperty: Optional[QQmlPropertyPrivate],
      binding: Optional[QV4.CompiledData.Binding],
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::populateDeferred(QObject *instance,
    int deferredIndex, const QQmlPropertyPrivate *qmlProperty, const
    QV4::CompiledData::Binding *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#populateDeferred

    Parameters
    ----------

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    deferredIndex : int
      Passed on as it is.

    qmlProperty : Optional[QQmlPropertyPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlObjectCreator::populateDeferred(QObject *instance, int
    #      deferredIndex, const QQmlPropertyPrivate *qmlProperty, const
    #      QV4::CompiledData::Binding *binding)
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator16populateDeferredEP7QObjectiPK19QQmlP'
        'ropertyPrivatePKN3QV412CompiledData7BindingE',
        self._addressOf(instance, 'QObject'), deferredIndex,
        self._addressOf(qmlProperty), self._addressOf(binding),
    )

  def setupFunctions(self) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::setupFunctions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#setupFunctions
    """
    #  void QQmlObjectCreator::setupFunctions()
    self.uglySide.call('ritual_ZN17QQmlObjectCreator14setupFunctionsEv')

  @overload(WAIT['QV4.CompiledData.Location'], str)
  def recordError(
      self,
      location: QV4.CompiledData.Location,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::recordError(const
    QV4::CompiledData::Location &location, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectcreator.html#recordError

    Parameters
    ----------

    location : QV4.CompiledData.Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlObjectCreator::recordError(const QV4::CompiledData::Location
    #      &location, const QString &description)
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator11recordErrorERKN3QV412CompiledData8Lo'
        'cationERK7QString',
        self._valueOf(location), description,
    )

  @overload(WAIT['QV4.CompiledData.Object'], QObject)
  @overload(WAIT['QV4.CompiledData.Object'], NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def registerObjectWithContextById(
      self,
      object: Optional[QV4.CompiledData.Object],
      instance: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQmlObjectCreator::registerObjectWithContextById(const
    QV4::CompiledData::Object *object, QObject *instance) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html

    Parameters
    ----------

    object : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlObjectCreator::registerObjectWithContextById(const
    #      QV4::CompiledData::Object *object, QObject *instance) const
    self.uglySide.call(
        'ritual_ZNK17QQmlObjectCreator29registerObjectWithContextByIdEPKN3Q'
        'V412CompiledData6ObjectEP7QObject',
        self._addressOf(object), self._addressOf(instance, 'QObject'),
    )

  def currentQmlContext(self) -> Optional[QV4.QmlContext]:
    """
    Calls Qt's 'QV4::QmlContext *QQmlObjectCreator::currentQmlContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html#currentQmlContext

    Returns
    -------

    Optional[QV4.QmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::QmlContext *QQmlObjectCreator::currentQmlContext()
    address = self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator17currentQmlContextEv',
    )
    return QV4.QmlContext._cuteAt(address)

  @overload(WAIT['QV4.CompiledData.Binding'])
  @overload(NoneType)
  def registerPostHocRequiredProperties(
      self,
      binding: Optional[QV4.CompiledData.Binding],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlObjectCreator::registerPostHocRequiredProperties(const
    QV4::CompiledData::Binding *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectcreator.html

    Parameters
    ----------

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlObjectCreator::registerPostHocRequiredProperties(const
    #      QV4::CompiledData::Binding *binding)
    self.uglySide.call(
        'ritual_ZN17QQmlObjectCreator33registerPostHocRequiredPropertiesEPK'
        'N3QV412CompiledData7BindingE',
        self._addressOf(binding),
    )

  @staticmethod
  def allCreatedObjects(*__, **_) -> Never:
    """
    Qt's 'std::vector<QQmlGuard<QObject>>
    &QQmlObjectCreator::allCreatedObjects()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.allCreatedObjects' has no cute function yet. "
        "Qt's 'std::vector<QQmlGuard<QObject>> "
        "&QQmlObjectCreator::allCreatedObjects()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def beginPopulateDeferred(*__, **_) -> Never:
    """
    Qt's 'void QQmlObjectCreator::beginPopulateDeferred(const
    QQmlRefPointer<QQmlContextData> &context)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.beginPopulateDeferred' has no cute function "
        "yet. Qt's 'void QQmlObjectCreator::beginPopulateDeferred(const "
        "QQmlRefPointer<QQmlContextData> &context)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def componentAttachment(*__, **_) -> Never:
    """
    Qt's 'QQmlComponentAttached **QQmlObjectCreator::componentAttachment()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.componentAttachment' has no cute function yet. "
        "Qt's 'QQmlComponentAttached "
        "**QQmlObjectCreator::componentAttachment()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def createComponent(*__, **_) -> Never:
    """
    Qt's 'QQmlComponent *QQmlObjectCreator::createComponent(QQmlEngine
    *engine, QV4::ExecutableCompilationUnit *compilationUnit, int index,
    QObject *parent, const QQmlRefPointer<QQmlContextData> &context)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.createComponent' has no cute function yet. Qt's "
        "'QQmlComponent *QQmlObjectCreator::createComponent(QQmlEngine "
        "*engine, QV4::ExecutableCompilationUnit *compilationUnit, int "
        "index, QObject *parent, const QQmlRefPointer<QQmlContextData> "
        "&context)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def createObjectInContext(*__, **_) -> Never:
    """
    Qt's 'QObject *QQmlObjectCreator::createObjectInContext(int objectIndex,
    QObject *parent, const QQmlRefPointer<QQmlContextData>
    &existingContext)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.createObjectInContext' has no cute function "
        "yet. Qt's 'QObject *QQmlObjectCreator::createObjectInContext(int "
        "objectIndex, QObject *parent, const "
        "QQmlRefPointer<QQmlContextData> &existingContext)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def doPopulateDeferred(*__, **_) -> Never:
    """
    Qt's 'QQmlObjectCreator::doPopulateDeferred': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.doPopulateDeferred' has no cute function yet. "
        "Qt's 'QQmlObjectCreator::doPopulateDeferred': a template: a "
        "pattern and no single function.")

  @staticmethod
  def finalize(*__, **_) -> Never:
    """
    Qt's 'bool QQmlObjectCreator::finalize(QQmlInstantiationInterrupt
    &interrupt)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.finalize' has no cute function yet. Qt's 'bool "
        "QQmlObjectCreator::finalize(QQmlInstantiationInterrupt "
        "&interrupt)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QQmlObjectCreator::init(const QQmlRefPointer<QQmlContextData>
    &parentContext)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.init' has no cute function yet. Qt's 'void "
        "QQmlObjectCreator::init(const QQmlRefPointer<QQmlContextData> "
        "&parentContext)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def parentContextData(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlObjectCreator::parentContextData() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.parentContextData' has no cute function yet. "
        "Qt's 'QQmlRefPointer<QQmlContextData> "
        "QQmlObjectCreator::parentContextData() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def repopulateBindings(*__, **_) -> Never:
    """
    Qt's 'void QQmlObjectCreator::repopulateBindings(int index, QObject
    *instance, const QQmlRefPointer<QQmlContextData> &instanceContext,
    InitFlags flags)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.repopulateBindings' has no cute function yet. "
        "Qt's 'void QQmlObjectCreator::repopulateBindings(int index, "
        "QObject *instance, const QQmlRefPointer<QQmlContextData> "
        "&instanceContext, InitFlags flags)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def rootContext(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData> QQmlObjectCreator::rootContext()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.rootContext' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> QQmlObjectCreator::rootContext() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setupBindings(*__, **_) -> Never:
    """
    Qt's 'void QQmlObjectCreator::setupBindings(BindingSetupFlags mode)':
    names the enum 'QQmlObjectCreator::BindingMode', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QQmlObjectCreator.setupBindings' has no cute function yet. Qt's "
        "'void QQmlObjectCreator::setupBindings(BindingSetupFlags mode)': "
        "names the enum 'QQmlObjectCreator::BindingMode', whose class "
        "cannot be named here.")
