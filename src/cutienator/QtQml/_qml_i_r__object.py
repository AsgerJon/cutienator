"""
QmlIR::Object binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::Object to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS, QV4, QmlIR

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Object(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QmlIR::Object: a plain Python object standing in
  front of one C++ QmlIR::Object.

  C++ hands a QmlIR::Object around as a copy, so every C++ QmlIR::Object
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QmlIR::Object that has a ritual and that Python can
  call so far, 35 names in all: 'tr', 'firstProperty', 'propertyCount',
  'firstAlias', 'aliasCount', 'firstEnum', 'enumCount', 'firstSignal',
  'signalCount', 'firstBinding', 'bindingCount', 'firstFunction',
  'functionCount', 'inlineComponent', 'inlineComponentCount',
  'requiredPropertyExtraData', 'requiredPropertyExtraDataCount',
  'simplifyRequiredProperties', 'init', 'appendEnum', 'appendSignal',
  'appendProperty', 'appendAlias', 'setFirstAlias', 'appendFunction',
  'appendInlineComponent', 'appendRequiredPropertyExtraData',
  'appendBinding', 'findBinding', 'unlinkBinding', 'bindingAsString',
  'namedObjectsInComponentCount', 'hasFlag', 'objectId',
  'hasAliasAsDefaultProperty'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QmlIR::Object::sortAliasDependencies(const Document *doc,
    QList<QQmlJS::DiagnosticMessage> *errors)': names
    'QList<QQmlJS::DiagnosticMessage>', which has no cute class yet.
  - Qt's 'const quint32 *QmlIR::Object::namedObjectsInComponentTable()
    const': gives 'unsigned int', which has no cute class yet.
  - Qt's 'QmlIR::Object::~Object()': the destructor: Python removes its C++
    QmlIR::Object by it, and has no other use for it.

  What has no ritual
  ------------------

  16 of the 54 functions Qt declares: 16 the compiler refuses its ritual as
  it would be written here.

  What to expect
  --------------

  - The C++ QmlIR::Object is created at the first use, not by
    'QmlIR::Object(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QmlIR::Object back gives a copy the ritual made for
    Python, in a new cute QmlIR::Object.
  - Each name of Qt's QmlIR::Object that has no cute function yet,
    'aliasesBegin', 'aliasesEnd', 'bindingsBegin', 'bindingsEnd',
    'enumsBegin', 'enumsEnd', 'functionsBegin', 'functionsEnd',
    'inlineComponentsBegin', 'inlineComponentsEnd',
    'namedObjectsInComponentTable', 'propertiesBegin', 'propertiesEnd',
    'requiredPropertyExtraDataBegin', 'requiredPropertyExtraDataEnd',
    'signalsBegin', 'signalsEnd', 'sortAliasDependencies', holds a function
    that raises 'NotImplementedError', and its docstring says why.
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
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QmlIR::Object::tr(const char *sourceText, const char
    *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#tr

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
    #  QString QmlIR::Object::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN5QmlIR6Object2trEPKcS2_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlIR::Object'

  #  Qt's '~QmlIR::Object()'. Naming it makes this a value class: Python owns
  #  every C++ QmlIR::Object behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN5QmlIR6ObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def firstProperty(self) -> Optional[QmlIR.Property]:
    """
    Calls Qt's 'const Property *QmlIR::Object::firstProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#firstProperty

    Returns
    -------

    Optional[QmlIR.Property]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Property *QmlIR::Object::firstProperty() const
    address = self.uglySide.call('ritual_ZNK5QmlIR6Object13firstPropertyEv')
    return QmlIR.Property._cuteAt(address)

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Object::propertyCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#propertyCount
    """
    #  int QmlIR::Object::propertyCount() const
    return self.uglySide.call('ritual_ZNK5QmlIR6Object13propertyCountEv')

  def firstAlias(self) -> Optional[QmlIR.Alias]:
    """
    Calls Qt's 'Alias *QmlIR::Object::firstAlias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#firstAlias

    Returns
    -------

    Optional[QmlIR.Alias]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Alias *QmlIR::Object::firstAlias() const
    address = self.uglySide.call('ritual_ZNK5QmlIR6Object10firstAliasEv')
    return QmlIR.Alias._cuteAt(address)

  def aliasCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Object::aliasCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#aliasCount
    """
    #  int QmlIR::Object::aliasCount() const
    return self.uglySide.call('ritual_ZNK5QmlIR6Object10aliasCountEv')

  def firstEnum(self) -> Optional[QmlIR.Enum]:
    """
    Calls Qt's 'const Enum *QmlIR::Object::firstEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#firstEnum

    Returns
    -------

    Optional[QmlIR.Enum]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Enum *QmlIR::Object::firstEnum() const
    address = self.uglySide.call('ritual_ZNK5QmlIR6Object9firstEnumEv')
    return QmlIR.Enum._cuteAt(address)

  def enumCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Object::enumCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#enumCount
    """
    #  int QmlIR::Object::enumCount() const
    return self.uglySide.call('ritual_ZNK5QmlIR6Object9enumCountEv')

  def firstSignal(self) -> Optional[QmlIR.Signal]:
    """
    Calls Qt's 'const Signal *QmlIR::Object::firstSignal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#firstSignal

    Returns
    -------

    Optional[QmlIR.Signal]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Signal *QmlIR::Object::firstSignal() const
    address = self.uglySide.call('ritual_ZNK5QmlIR6Object11firstSignalEv')
    return QmlIR.Signal._cuteAt(address)

  def signalCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Object::signalCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#signalCount
    """
    #  int QmlIR::Object::signalCount() const
    return self.uglySide.call('ritual_ZNK5QmlIR6Object11signalCountEv')

  def firstBinding(self) -> Optional[QmlIR.Binding]:
    """
    Calls Qt's 'Binding *QmlIR::Object::firstBinding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#firstBinding

    Returns
    -------

    Optional[QmlIR.Binding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Binding *QmlIR::Object::firstBinding() const
    address = self.uglySide.call('ritual_ZNK5QmlIR6Object12firstBindingEv')
    return QmlIR.Binding._cuteAt(address)

  def bindingCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Object::bindingCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#bindingCount
    """
    #  int QmlIR::Object::bindingCount() const
    return self.uglySide.call('ritual_ZNK5QmlIR6Object12bindingCountEv')

  def firstFunction(self) -> Optional[QmlIR.Function]:
    """
    Calls Qt's 'const Function *QmlIR::Object::firstFunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#firstFunction

    Returns
    -------

    Optional[QmlIR.Function]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Function *QmlIR::Object::firstFunction() const
    address = self.uglySide.call('ritual_ZNK5QmlIR6Object13firstFunctionEv')
    return QmlIR.Function._cuteAt(address)

  def functionCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Object::functionCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#functionCount
    """
    #  int QmlIR::Object::functionCount() const
    return self.uglySide.call('ritual_ZNK5QmlIR6Object13functionCountEv')

  def inlineComponent(self) -> Optional[QmlIR.InlineComponent]:
    """
    Calls Qt's 'const InlineComponent *QmlIR::Object::inlineComponent()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#inlineComponent

    Returns
    -------

    Optional[QmlIR.InlineComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const InlineComponent *QmlIR::Object::inlineComponent() const
    address = self.uglySide.call(
        'ritual_ZNK5QmlIR6Object15inlineComponentEv',
    )
    return QmlIR.InlineComponent._cuteAt(address)

  def inlineComponentCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Object::inlineComponentCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-object.html#inlineComponentCount
    """
    #  int QmlIR::Object::inlineComponentCount() const
    return self.uglySide.call(
        'ritual_ZNK5QmlIR6Object20inlineComponentCountEv',
    )

  def requiredPropertyExtraData(
      self,
  ) -> Optional[QmlIR.RequiredPropertyExtraData]:
    """
    Calls Qt's 'const RequiredPropertyExtraData
    *QmlIR::Object::requiredPropertyExtraData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-object.html#requiredPropertyExtraData

    Returns
    -------

    Optional[QmlIR.RequiredPropertyExtraData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const RequiredPropertyExtraData
    #      *QmlIR::Object::requiredPropertyExtraData() const
    address = self.uglySide.call(
        'ritual_ZNK5QmlIR6Object25requiredPropertyExtraDataEv',
    )
    return QmlIR.RequiredPropertyExtraData._cuteAt(address)

  def requiredPropertyExtraDataCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Object::requiredPropertyExtraDataCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-object.html#requiredPropertyExtraDataCount
    """
    #  int QmlIR::Object::requiredPropertyExtraDataCount() const
    return self.uglySide.call(
        'ritual_ZNK5QmlIR6Object30requiredPropertyExtraDataCountEv',
    )

  @overload(int)
  def findBinding(self, nameIndex: int) -> Optional[QmlIR.Binding]:
    """
    Calls Qt's 'Binding *QmlIR::Object::findBinding(quint32 nameIndex)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#findBinding

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QmlIR.Binding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Binding *QmlIR::Object::findBinding(quint32 nameIndex) const
    address = self.uglySide.call(
        'ritual_ZNK5QmlIR6Object11findBindingEj', nameIndex,
    )
    return QmlIR.Binding._cuteAt(address)

  @overload(WAIT['QmlIR.Document'], int)
  @overload(NoneType, int)
  def bindingAsString(
      self,
      doc: Optional[QmlIR.Document],
      scriptIndex: int,
  ) -> str:
    """
    Calls Qt's 'QString QmlIR::Object::bindingAsString(Document *doc, int
    scriptIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#bindingAsString

    Parameters
    ----------

    doc : Optional[QmlIR.Document]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scriptIndex : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlIR::Object::bindingAsString(Document *doc, int scriptIndex)
    #      const
    return self.uglySide.call(
        'ritual_ZNK5QmlIR6Object15bindingAsStringEPNS_8DocumentEi',
        self._addressOf(doc), scriptIndex,
    )

  def namedObjectsInComponentCount(self) -> int:
    """
    Calls Qt's 'int QmlIR::Object::namedObjectsInComponentCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-object.html#namedObjectsInComponentCount
    """
    #  int QmlIR::Object::namedObjectsInComponentCount() const
    return self.uglySide.call(
        'ritual_ZNK5QmlIR6Object28namedObjectsInComponentCountEv',
    )

  @overload(QV4.CompiledData.Object.Flag)
  def hasFlag(self, flag: QV4.CompiledData.Object.Flag) -> bool:
    """
    Calls Qt's 'bool QmlIR::Object::hasFlag(QV4::CompiledData::Object::Flag
    flag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#hasFlag

    Parameters
    ----------

    flag : QV4.CompiledData.Object.Flag
      Passed on as its number.
    """
    #  bool QmlIR::Object::hasFlag(QV4::CompiledData::Object::Flag flag)
    #      const
    return self.uglySide.call(
        'ritual_ZNK5QmlIR6Object7hasFlagEN3QV412CompiledData6Object4FlagE',
        flag.value,
    )

  def objectId(self) -> int:
    """
    Calls Qt's 'qint32 QmlIR::Object::objectId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#objectId
    """
    #  qint32 QmlIR::Object::objectId() const
    return self.uglySide.call('ritual_ZNK5QmlIR6Object8objectIdEv')

  def hasAliasAsDefaultProperty(self) -> bool:
    """
    Calls Qt's 'bool QmlIR::Object::hasAliasAsDefaultProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-object.html#hasAliasAsDefaultProperty
    """
    #  bool QmlIR::Object::hasAliasAsDefaultProperty() const
    return self.uglySide.call(
        'ritual_ZNK5QmlIR6Object25hasAliasAsDefaultPropertyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QmlIR.Alias'])
  @overload(NoneType)
  def setFirstAlias(self, alias: Optional[QmlIR.Alias]) -> None:
    """
    Calls Qt's 'void QmlIR::Object::setFirstAlias(Alias *alias)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#setFirstAlias

    Parameters
    ----------

    alias : Optional[QmlIR.Alias]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QmlIR::Object::setFirstAlias(Alias *alias)
    self.uglySide.call(
        'ritual_ZN5QmlIR6Object13setFirstAliasEPNS_5AliasE',
        self._addressOf(alias),
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

  def simplifyRequiredProperties(self) -> None:
    """
    Calls Qt's 'void QmlIR::Object::simplifyRequiredProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-object.html#simplifyRequiredProperties
    """
    #  void QmlIR::Object::simplifyRequiredProperties()
    self.uglySide.call(
        'ritual_ZN5QmlIR6Object26simplifyRequiredPropertiesEv',
    )

  @overload(
      WAIT['QQmlJS.MemoryPool'], int, int, WAIT['QV4.CompiledData.Location'],
  )
  @overload(NoneType, int, int, WAIT['QV4.CompiledData.Location'])
  def init(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      typeNameIndex: int,
      idIndex: int,
      location: QV4.CompiledData.Location,
  ) -> None:
    """
    Calls Qt's 'void QmlIR::Object::init(QQmlJS::MemoryPool *pool, int
    typeNameIndex, int idIndex, const QV4::CompiledData::Location
    &location)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#init

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeNameIndex : int
      Passed on as it is.

    idIndex : int
      Passed on as it is.

    location : QV4.CompiledData.Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.
    """
    #  void QmlIR::Object::init(QQmlJS::MemoryPool *pool, int typeNameIndex,
    #      int idIndex, const QV4::CompiledData::Location &location)
    self.uglySide.call(
        'ritual_ZN5QmlIR6Object4initEPN6QQmlJS10MemoryPoolEiiRKN3QV412Compi'
        'ledData8LocationE',
        self._addressOf(pool), typeNameIndex, idIndex,
        self._valueOf(location),
    )

  @overload(WAIT['QmlIR.Enum'])
  @overload(NoneType)
  def appendEnum(self, enumeration: Optional[QmlIR.Enum]) -> str:
    """
    Calls Qt's 'QString QmlIR::Object::appendEnum(Enum *enumeration)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#appendEnum

    Parameters
    ----------

    enumeration : Optional[QmlIR.Enum]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlIR::Object::appendEnum(Enum *enumeration)
    return self.uglySide.call(
        'ritual_ZN5QmlIR6Object10appendEnumEPNS_4EnumE',
        self._addressOf(enumeration),
    )

  @overload(WAIT['QmlIR.Signal'])
  @overload(NoneType)
  def appendSignal(self, signal: Optional[QmlIR.Signal]) -> str:
    """
    Calls Qt's 'QString QmlIR::Object::appendSignal(Signal *signal)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#appendSignal

    Parameters
    ----------

    signal : Optional[QmlIR.Signal]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlIR::Object::appendSignal(Signal *signal)
    return self.uglySide.call(
        'ritual_ZN5QmlIR6Object12appendSignalEPNS_6SignalE',
        self._addressOf(signal),
    )

  @overload(
      WAIT['QmlIR.Property'], str, bool, WAIT['QQmlJS.SourceLocation'],
      WAIT['QQmlJS.SourceLocation'],
  )
  @overload(
      WAIT['QmlIR.Property'], str, bool, WAIT['QQmlJS.SourceLocation'],
      NoneType,
  )
  @overload(
      NoneType, str, bool, WAIT['QQmlJS.SourceLocation'],
      WAIT['QQmlJS.SourceLocation'],
  )
  @overload(NoneType, str, bool, WAIT['QQmlJS.SourceLocation'], NoneType)
  def appendProperty(
      self,
      prop: Optional[QmlIR.Property],
      propertyName: str,
      isDefaultProperty: bool,
      defaultToken: QQmlJS.SourceLocation,
      errorLocation: Optional[QQmlJS.SourceLocation],
  ) -> str:
    """
    Calls Qt's 'QString QmlIR::Object::appendProperty(Property *prop, const
    QString &propertyName, bool isDefaultProperty, const
    QQmlJS::SourceLocation &defaultToken, QQmlJS::SourceLocation
    *errorLocation)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#appendProperty

    Parameters
    ----------

    prop : Optional[QmlIR.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    isDefaultProperty : bool
      Passed on as it is.

    defaultToken : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    errorLocation : Optional[QQmlJS.SourceLocation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlIR::Object::appendProperty(Property *prop, const QString
    #      &propertyName, bool isDefaultProperty, const
    #      QQmlJS::SourceLocation &defaultToken, QQmlJS::SourceLocation
    #      *errorLocation)
    return self.uglySide.call(
        'ritual_ZN5QmlIR6Object14appendPropertyEPNS_8PropertyERK7QStringbRK'
        'N6QQmlJS14SourceLocationEPS7_',
        self._addressOf(prop), propertyName, isDefaultProperty,
        self._valueOf(defaultToken), self._addressOf(errorLocation),
    )

  @overload(
      WAIT['QmlIR.Alias'], str, bool, WAIT['QQmlJS.SourceLocation'],
      WAIT['QQmlJS.SourceLocation'],
  )
  @overload(
      WAIT['QmlIR.Alias'], str, bool, WAIT['QQmlJS.SourceLocation'],
      NoneType,
  )
  @overload(
      NoneType, str, bool, WAIT['QQmlJS.SourceLocation'],
      WAIT['QQmlJS.SourceLocation'],
  )
  @overload(NoneType, str, bool, WAIT['QQmlJS.SourceLocation'], NoneType)
  def appendAlias(
      self,
      prop: Optional[QmlIR.Alias],
      aliasName: str,
      isDefaultProperty: bool,
      defaultToken: QQmlJS.SourceLocation,
      errorLocation: Optional[QQmlJS.SourceLocation],
  ) -> str:
    """
    Calls Qt's 'QString QmlIR::Object::appendAlias(Alias *prop, const QString
    &aliasName, bool isDefaultProperty, const QQmlJS::SourceLocation
    &defaultToken, QQmlJS::SourceLocation *errorLocation)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#appendAlias

    Parameters
    ----------

    prop : Optional[QmlIR.Alias]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    aliasName : str
      Passed on as it is: a QString is made of it for the call.

    isDefaultProperty : bool
      Passed on as it is.

    defaultToken : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    errorLocation : Optional[QQmlJS.SourceLocation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlIR::Object::appendAlias(Alias *prop, const QString
    #      &aliasName, bool isDefaultProperty, const QQmlJS::SourceLocation
    #      &defaultToken, QQmlJS::SourceLocation *errorLocation)
    return self.uglySide.call(
        'ritual_ZN5QmlIR6Object11appendAliasEPNS_5AliasERK7QStringbRKN6QQml'
        'JS14SourceLocationEPS7_',
        self._addressOf(prop), aliasName, isDefaultProperty,
        self._valueOf(defaultToken), self._addressOf(errorLocation),
    )

  @overload(WAIT['QmlIR.Function'])
  @overload(NoneType)
  def appendFunction(self, f: Optional[QmlIR.Function]) -> None:
    """
    Calls Qt's 'void QmlIR::Object::appendFunction(QmlIR::Function *f)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#appendFunction

    Parameters
    ----------

    f : Optional[QmlIR.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QmlIR::Object::appendFunction(QmlIR::Function *f)
    self.uglySide.call(
        'ritual_ZN5QmlIR6Object14appendFunctionEPNS_8FunctionE',
        self._addressOf(f),
    )

  @overload(WAIT['QmlIR.InlineComponent'])
  @overload(NoneType)
  def appendInlineComponent(
      self,
      ic: Optional[QmlIR.InlineComponent],
  ) -> None:
    """
    Calls Qt's 'void QmlIR::Object::appendInlineComponent(InlineComponent
    *ic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-object.html#appendInlineComponent

    Parameters
    ----------

    ic : Optional[QmlIR.InlineComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QmlIR::Object::appendInlineComponent(InlineComponent *ic)
    self.uglySide.call(
        'ritual_ZN5QmlIR6Object21appendInlineComponentEPNS_15InlineComponen'
        'tE',
        self._addressOf(ic),
    )

  @overload(WAIT['QmlIR.RequiredPropertyExtraData'])
  @overload(NoneType)
  def appendRequiredPropertyExtraData(
      self,
      extraData: Optional[QmlIR.RequiredPropertyExtraData],
  ) -> None:
    """
    Calls Qt's 'void
    QmlIR::Object::appendRequiredPropertyExtraData(RequiredPropertyExtraData
    *extraData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-object.html#appendRequiredPropertyExtraData

    Parameters
    ----------

    extraData : Optional[QmlIR.RequiredPropertyExtraData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QmlIR::Object::appendRequiredPropertyExtraData(
    #      RequiredPropertyExtraData *extraData)
    self.uglySide.call(
        'ritual_ZN5QmlIR6Object31appendRequiredPropertyExtraDataEPNS_25Requ'
        'iredPropertyExtraDataE',
        self._addressOf(extraData),
    )

  @overload(WAIT['QmlIR.Binding'], bool)
  @overload(NoneType, bool)
  def appendBinding(
      self,
      b: Optional[QmlIR.Binding],
      isListBinding: bool,
  ) -> str:
    """
    Calls Qt's 'QString QmlIR::Object::appendBinding(Binding *b, bool
    isListBinding)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#appendBinding

    Parameters
    ----------

    b : Optional[QmlIR.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isListBinding : bool
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlIR::Object::appendBinding(Binding *b, bool isListBinding)
    return self.uglySide.call(
        'ritual_ZN5QmlIR6Object13appendBindingEPNS_7BindingEb',
        self._addressOf(b), isListBinding,
    )

  @overload(WAIT['QmlIR.Binding'], WAIT['QmlIR.Binding'])
  @overload(WAIT['QmlIR.Binding'], NoneType)
  @overload(NoneType, WAIT['QmlIR.Binding'])
  @overload(NoneType, NoneType)
  def unlinkBinding(
      self,
      before: Optional[QmlIR.Binding],
      binding: Optional[QmlIR.Binding],
  ) -> Optional[QmlIR.Binding]:
    """
    Calls Qt's 'Binding *QmlIR::Object::unlinkBinding(Binding *before,
    Binding *binding)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-object.html#unlinkBinding

    Parameters
    ----------

    before : Optional[QmlIR.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    binding : Optional[QmlIR.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QmlIR.Binding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Binding *QmlIR::Object::unlinkBinding(Binding *before, Binding
    #      *binding)
    address = self.uglySide.call(
        'ritual_ZN5QmlIR6Object13unlinkBindingEPNS_7BindingES2_',
        self._addressOf(before), self._addressOf(binding),
    )
    return QmlIR.Binding._cuteAt(address)

  @staticmethod
  def aliasesBegin(*__, **_) -> Never:
    """
    Qt's 'PoolList<Alias>::Iterator QmlIR::Object::aliasesBegin() const': the
    compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.aliasesBegin' has no cute function yet. Qt's "
        "'PoolList<Alias>::Iterator QmlIR::Object::aliasesBegin() const': "
        "the compiler refuses its ritual as it would be written here: no "
        "template named 'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def aliasesEnd(*__, **_) -> Never:
    """
    Qt's 'PoolList<Alias>::Iterator QmlIR::Object::aliasesEnd() const': the
    compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.aliasesEnd' has no cute function yet. Qt's "
        "'PoolList<Alias>::Iterator QmlIR::Object::aliasesEnd() const': the "
        "compiler refuses its ritual as it would be written here: no "
        "template named 'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def bindingsBegin(*__, **_) -> Never:
    """
    Qt's 'PoolList<Binding>::Iterator QmlIR::Object::bindingsBegin() const':
    the compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.bindingsBegin' has no cute function yet. Qt's "
        "'PoolList<Binding>::Iterator QmlIR::Object::bindingsBegin() "
        "const': the compiler refuses its ritual as it would be written "
        "here: no template named 'PoolList'; did you mean "
        "'QmlIR::PoolList'?.")

  @staticmethod
  def bindingsEnd(*__, **_) -> Never:
    """
    Qt's 'PoolList<Binding>::Iterator QmlIR::Object::bindingsEnd() const':
    the compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.bindingsEnd' has no cute function yet. Qt's "
        "'PoolList<Binding>::Iterator QmlIR::Object::bindingsEnd() const': "
        "the compiler refuses its ritual as it would be written here: no "
        "template named 'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def enumsBegin(*__, **_) -> Never:
    """
    Qt's 'PoolList<Enum>::Iterator QmlIR::Object::enumsBegin() const': the
    compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.enumsBegin' has no cute function yet. Qt's "
        "'PoolList<Enum>::Iterator QmlIR::Object::enumsBegin() const': the "
        "compiler refuses its ritual as it would be written here: no "
        "template named 'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def enumsEnd(*__, **_) -> Never:
    """
    Qt's 'PoolList<Enum>::Iterator QmlIR::Object::enumsEnd() const': the
    compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.enumsEnd' has no cute function yet. Qt's "
        "'PoolList<Enum>::Iterator QmlIR::Object::enumsEnd() const': the "
        "compiler refuses its ritual as it would be written here: no "
        "template named 'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def functionsBegin(*__, **_) -> Never:
    """
    Qt's 'PoolList<Function>::Iterator QmlIR::Object::functionsBegin()
    const': the compiler refuses its ritual as it would be written here: no
    template named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.functionsBegin' has no cute function yet. Qt's "
        "'PoolList<Function>::Iterator QmlIR::Object::functionsBegin() "
        "const': the compiler refuses its ritual as it would be written "
        "here: no template named 'PoolList'; did you mean "
        "'QmlIR::PoolList'?.")

  @staticmethod
  def functionsEnd(*__, **_) -> Never:
    """
    Qt's 'PoolList<Function>::Iterator QmlIR::Object::functionsEnd() const':
    the compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.functionsEnd' has no cute function yet. Qt's "
        "'PoolList<Function>::Iterator QmlIR::Object::functionsEnd() "
        "const': the compiler refuses its ritual as it would be written "
        "here: no template named 'PoolList'; did you mean "
        "'QmlIR::PoolList'?.")

  @staticmethod
  def inlineComponentsBegin(*__, **_) -> Never:
    """
    Qt's 'PoolList<InlineComponent>::Iterator
    QmlIR::Object::inlineComponentsBegin() const': the compiler refuses its
    ritual as it would be written here: no template named 'PoolList'; did you
    mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.inlineComponentsBegin' has no cute function yet. "
        "Qt's 'PoolList<InlineComponent>::Iterator "
        "QmlIR::Object::inlineComponentsBegin() const': the compiler "
        "refuses its ritual as it would be written here: no template named "
        "'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def inlineComponentsEnd(*__, **_) -> Never:
    """
    Qt's 'PoolList<InlineComponent>::Iterator
    QmlIR::Object::inlineComponentsEnd() const': the compiler refuses its
    ritual as it would be written here: no template named 'PoolList'; did you
    mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.inlineComponentsEnd' has no cute function yet. Qt's "
        "'PoolList<InlineComponent>::Iterator "
        "QmlIR::Object::inlineComponentsEnd() const': the compiler refuses "
        "its ritual as it would be written here: no template named "
        "'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def namedObjectsInComponentTable(*__, **_) -> Never:
    """
    Qt's 'const quint32 *QmlIR::Object::namedObjectsInComponentTable()
    const': gives 'unsigned int', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QmlIR.Object.namedObjectsInComponentTable' has no cute function "
        "yet. Qt's 'const quint32 "
        "*QmlIR::Object::namedObjectsInComponentTable() const': gives "
        "'unsigned int', which has no cute class yet.")

  @staticmethod
  def propertiesBegin(*__, **_) -> Never:
    """
    Qt's 'PoolList<Property>::Iterator QmlIR::Object::propertiesBegin()
    const': the compiler refuses its ritual as it would be written here: no
    template named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.propertiesBegin' has no cute function yet. Qt's "
        "'PoolList<Property>::Iterator QmlIR::Object::propertiesBegin() "
        "const': the compiler refuses its ritual as it would be written "
        "here: no template named 'PoolList'; did you mean "
        "'QmlIR::PoolList'?.")

  @staticmethod
  def propertiesEnd(*__, **_) -> Never:
    """
    Qt's 'PoolList<Property>::Iterator QmlIR::Object::propertiesEnd() const':
    the compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.propertiesEnd' has no cute function yet. Qt's "
        "'PoolList<Property>::Iterator QmlIR::Object::propertiesEnd() "
        "const': the compiler refuses its ritual as it would be written "
        "here: no template named 'PoolList'; did you mean "
        "'QmlIR::PoolList'?.")

  @staticmethod
  def requiredPropertyExtraDataBegin(*__, **_) -> Never:
    """
    Qt's 'PoolList<RequiredPropertyExtraData>::Iterator
    QmlIR::Object::requiredPropertyExtraDataBegin() const': the compiler
    refuses its ritual as it would be written here: no template named
    'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.requiredPropertyExtraDataBegin' has no cute function "
        "yet. Qt's 'PoolList<RequiredPropertyExtraData>::Iterator "
        "QmlIR::Object::requiredPropertyExtraDataBegin() const': the "
        "compiler refuses its ritual as it would be written here: no "
        "template named 'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def requiredPropertyExtraDataEnd(*__, **_) -> Never:
    """
    Qt's 'PoolList<RequiredPropertyExtraData>::Iterator
    QmlIR::Object::requiredPropertyExtraDataEnd() const': the compiler
    refuses its ritual as it would be written here: no template named
    'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.requiredPropertyExtraDataEnd' has no cute function "
        "yet. Qt's 'PoolList<RequiredPropertyExtraData>::Iterator "
        "QmlIR::Object::requiredPropertyExtraDataEnd() const': the compiler "
        "refuses its ritual as it would be written here: no template named "
        "'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def signalsBegin(*__, **_) -> Never:
    """
    Qt's 'PoolList<Signal>::Iterator QmlIR::Object::signalsBegin() const':
    the compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.signalsBegin' has no cute function yet. Qt's "
        "'PoolList<Signal>::Iterator QmlIR::Object::signalsBegin() const': "
        "the compiler refuses its ritual as it would be written here: no "
        "template named 'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def signalsEnd(*__, **_) -> Never:
    """
    Qt's 'PoolList<Signal>::Iterator QmlIR::Object::signalsEnd() const': the
    compiler refuses its ritual as it would be written here: no template
    named 'PoolList'; did you mean 'QmlIR::PoolList'?.
    """
    raise NotImplementedError(
        "'QmlIR.Object.signalsEnd' has no cute function yet. Qt's "
        "'PoolList<Signal>::Iterator QmlIR::Object::signalsEnd() const': "
        "the compiler refuses its ritual as it would be written here: no "
        "template named 'PoolList'; did you mean 'QmlIR::PoolList'?.")

  @staticmethod
  def sortAliasDependencies(*__, **_) -> Never:
    """
    Qt's 'void QmlIR::Object::sortAliasDependencies(const Document *doc,
    QList<QQmlJS::DiagnosticMessage> *errors)': names
    'QList<QQmlJS::DiagnosticMessage>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QmlIR.Object.sortAliasDependencies' has no cute function yet. "
        "Qt's 'void QmlIR::Object::sortAliasDependencies(const Document "
        "*doc, QList<QQmlJS::DiagnosticMessage> *errors)': names "
        "'QList<QQmlJS::DiagnosticMessage>', which has no cute class yet.")
