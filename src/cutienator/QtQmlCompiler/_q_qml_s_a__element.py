"""
QQmlSA::Element binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Element(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::Element: a plain Python object standing in
  front of one C++ QQmlSA::Element.

  C++ hands a QQmlSA::Element around as a copy, so every C++ QQmlSA::Element
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::Element that has a ritual and that Python
  can call so far, 28 names in all: 'scopeType', 'baseType', 'baseTypeName',
  'parentScope', 'inherits', 'isFileRootComponent', 'isNull', 'internalId',
  'accessSemantics', 'isComposite', 'hasProperty', 'hasOwnProperty',
  'property', 'isPropertyRequired', 'defaultPropertyName', 'hasMethod',
  'ownMethods', 'sourceLocation', 'idSourceLocation', 'filePath',
  'hasPropertyBindings', 'hasOwnPropertyBindings', 'ownPropertyBindings',
  '__bool__', 'name', '__eq__', '__ne__', 'hash'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlSA::Element::Element(Element &&other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'Element &QQmlSA::Element::operator=(const Element &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'Element &QQmlSA::Element::operator=(Element &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QQmlSA::Element::~Element()': the destructor: Python removes its
    C++ QQmlSA::Element by it, and has no other use for it.
  - Qt's 'QList<Binding> QQmlSA::Element::propertyBindings(const QString
    &propertyName) const': gives a type Python has no way to take yet.
  - Qt's 'bool QQmlSA::Element::operator!() const': an operator Python has no
    name for.
  - Qt's 'bool QQmlSA::Element::operatorEqualsImpl(const Element &a0, const
    Element &a1)': an operator Python has no name for.
  - Qt's 'void QQmlSA::Element::swap(Element &other)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlSA::Element is created at the first use, not by
    'QQmlSA::Element(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::Element back gives a copy the ritual made for
    Python, in a new cute QQmlSA::Element.
  - Each name of Qt's QQmlSA::Element that has no cute function yet,
    'propertyBindings', 'swap', holds a function that raises
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
  __qt_class__ = 'QQmlSA::Element'

  #  Qt's '~QQmlSA::Element()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlSA::Element behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA7ElementD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scopeType(self) -> QQmlSA.ScopeType:
    """
    Calls Qt's 'ScopeType QQmlSA::Element::scopeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#scopeType

    Returns
    -------

    QQmlSA.ScopeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QQmlSA.ScopeType(number)'
      gives.
    """
    #  ScopeType QQmlSA::Element::scopeType() const
    return QQmlSA.ScopeType(self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element9scopeTypeEv',
    ))

  def baseType(self) -> Element:
    """
    Calls Qt's 'Element QQmlSA::Element::baseType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#baseType

    Returns
    -------

    Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::Element::baseType() const
    address = self.uglySide.call('ritual_ZNK6QQmlSA7Element8baseTypeEv')
    return Element._cuteOwning(address)

  def baseTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::Element::baseTypeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#baseTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::Element::baseTypeName() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Element12baseTypeNameEv')

  def parentScope(self) -> Element:
    """
    Calls Qt's 'Element QQmlSA::Element::parentScope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#parentScope

    Returns
    -------

    Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::Element::parentScope() const
    address = self.uglySide.call('ritual_ZNK6QQmlSA7Element11parentScopeEv')
    return Element._cuteOwning(address)

  @overload(THIS)
  def inherits(self, a0: Element) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::inherits(const Element &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#inherits

    Parameters
    ----------

    a0 : Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  bool QQmlSA::Element::inherits(const Element &a0) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element8inheritsERKS0_', self._valueOf(a0),
    )

  def isFileRootComponent(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::isFileRootComponent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-element.html#isFileRootComponent
    """
    #  bool QQmlSA::Element::isFileRootComponent() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element19isFileRootComponentEv',
    )

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#isNull
    """
    #  bool QQmlSA::Element::isNull() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Element6isNullEv')

  def internalId(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::Element::internalId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#internalId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::Element::internalId() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Element10internalIdEv')

  def accessSemantics(self) -> QQmlSA.AccessSemantics:
    """
    Calls Qt's 'AccessSemantics QQmlSA::Element::accessSemantics() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-element.html#accessSemantics

    Returns
    -------

    QQmlSA.AccessSemantics
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.AccessSemantics(number)' gives.
    """
    #  AccessSemantics QQmlSA::Element::accessSemantics() const
    return QQmlSA.AccessSemantics(self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element15accessSemanticsEv',
    ))

  def isComposite(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::isComposite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#isComposite
    """
    #  bool QQmlSA::Element::isComposite() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Element11isCompositeEv')

  @overload(str)
  def hasProperty(self, propertyName: str) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::hasProperty(const QString
    &propertyName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#hasProperty

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlSA::Element::hasProperty(const QString &propertyName) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element11hasPropertyERK7QString', propertyName,
    )

  @overload(str)
  def hasOwnProperty(self, propertyName: str) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::hasOwnProperty(const QString
    &propertyName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#hasOwnProperty

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlSA::Element::hasOwnProperty(const QString &propertyName)
    #      const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element14hasOwnPropertyERK7QString', propertyName,
    )

  @overload(str)
  def property(self, propertyName: str) -> QQmlSA.Property:
    """
    Calls Qt's 'Property QQmlSA::Element::property(const QString
    &propertyName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#property

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlSA.Property
      A new cute QQmlSA::Property around the copy Qt gave back. Python owns
      it.
    """
    #  Property QQmlSA::Element::property(const QString &propertyName) const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element8propertyERK7QString', propertyName,
    )
    return QQmlSA.Property._cuteOwning(address)

  @overload(str)
  def isPropertyRequired(self, propertyName: str) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::isPropertyRequired(const QString
    &propertyName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-element.html#isPropertyRequired

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlSA::Element::isPropertyRequired(const QString &propertyName)
    #      const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element18isPropertyRequiredERK7QString',
        propertyName,
    )

  def defaultPropertyName(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::Element::defaultPropertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-element.html#defaultPropertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::Element::defaultPropertyName() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element19defaultPropertyNameEv',
    )

  @overload(str)
  def hasMethod(self, methodName: str) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::hasMethod(const QString &methodName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#hasMethod

    Parameters
    ----------

    methodName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlSA::Element::hasMethod(const QString &methodName) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element9hasMethodERK7QString', methodName,
    )

  def ownMethods(self) -> QQmlSA.Method.Methods:
    """
    Calls Qt's 'Method::Methods QQmlSA::Element::ownMethods() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#ownMethods

    Returns
    -------

    QQmlSA.Method.Methods
      A new cute QQmlSA::Method::Methods around the copy Qt gave back. Python
      owns it.
    """
    #  Method::Methods QQmlSA::Element::ownMethods() const
    address = self.uglySide.call('ritual_ZNK6QQmlSA7Element10ownMethodsEv')
    return QQmlSA.Method.Methods._cuteOwning(address)

  def sourceLocation(self) -> QQmlSA.SourceLocation:
    """
    Calls Qt's 'QQmlSA::SourceLocation QQmlSA::Element::sourceLocation()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#sourceLocation

    Returns
    -------

    QQmlSA.SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlSA::SourceLocation QQmlSA::Element::sourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element14sourceLocationEv',
    )
    return QQmlSA.SourceLocation._cuteOwning(address)

  def idSourceLocation(self) -> QQmlSA.SourceLocation:
    """
    Calls Qt's 'QQmlSA::SourceLocation QQmlSA::Element::idSourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-element.html#idSourceLocation

    Returns
    -------

    QQmlSA.SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlSA::SourceLocation QQmlSA::Element::idSourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element16idSourceLocationEv',
    )
    return QQmlSA.SourceLocation._cuteOwning(address)

  def filePath(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::Element::filePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#filePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::Element::filePath() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Element8filePathEv')

  @overload(str)
  def hasPropertyBindings(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::hasPropertyBindings(const QString
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-element.html#hasPropertyBindings

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlSA::Element::hasPropertyBindings(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element19hasPropertyBindingsERK7QString', name,
    )

  @overload(str)
  def hasOwnPropertyBindings(self, propertyName: str) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::hasOwnPropertyBindings(const QString
    &propertyName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-element.html#hasOwnPropertyBindings

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlSA::Element::hasOwnPropertyBindings(const QString
    #      &propertyName) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element22hasOwnPropertyBindingsERK7QString',
        propertyName,
    )

  @overload()
  def ownPropertyBindings(self) -> QQmlSA.Binding.Bindings:
    """
    Calls Qt's 'Binding::Bindings QQmlSA::Element::ownPropertyBindings()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-element.html#ownPropertyBindings

    Returns
    -------

    QQmlSA.Binding.Bindings
      A new cute QQmlSA::Binding::Bindings around the copy Qt gave back.
      Python owns it.
    """
    #  Binding::Bindings QQmlSA::Element::ownPropertyBindings() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element19ownPropertyBindingsEv',
    )
    return QQmlSA.Binding.Bindings._cuteOwning(address)

  @overload(str)
  def ownPropertyBindings(
      self,
      propertyName: str,
  ) -> QQmlSA.Binding.Bindings:
    """
    Calls Qt's 'Binding::Bindings QQmlSA::Element::ownPropertyBindings(const
    QString &propertyName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-element.html#ownPropertyBindings

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlSA.Binding.Bindings
      A new cute QQmlSA::Binding::Bindings around the copy Qt gave back.
      Python owns it.
    """
    #  Binding::Bindings QQmlSA::Element::ownPropertyBindings(const QString
    #      &propertyName) const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA7Element19ownPropertyBindingsERK7QString',
        propertyName,
    )
    return QQmlSA.Binding.Bindings._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::Element::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::Element::name() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Element4nameEv')

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QQmlSA::Element::hash(size_t seed) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QQmlSA::Element::hash(size_t seed) const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Element4hashEm', seed)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Element::operator bool() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#operator bool
    """
    #  bool QQmlSA::Element::operator bool() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7ElementcvbEv')

  @overload(THIS)
  def __eq__(self, rhs: Element) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlSA::Element &lhs, const
    QQmlSA::Element &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#operator==

    Parameters
    ----------

    rhs : Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  bool operator==(const QQmlSA::Element &lhs, const QQmlSA::Element
    #      &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAeqERKNS_7ElementES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: Element) -> bool:
    """
    Calls Qt's 'bool operator!=(const Element &lhs, const Element &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#operator!=

    Parameters
    ----------

    rhs : Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  bool operator!=(const Element &lhs, const Element &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAneERKNS_7ElementES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    Notes what was given, for Qt's 'QQmlSA::Element::Element()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#Element
    """
    #  QQmlSA::Element::Element()
    self._noteCreation(Element, lambda: Rituals.call(
        'ritual_ZN6QQmlSA7ElementC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: Element) -> None:
    """
    Notes what was given, for Qt's 'QQmlSA::Element::Element(const Element
    &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-element.html#Element

    Parameters
    ----------

    a0 : Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  QQmlSA::Element::Element(const Element &a0)
    self._noteCreation(Element, lambda: Rituals.call(
        'ritual_ZN6QQmlSA7ElementC1ERKS0_', self._valueOf(a0),
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
  def propertyBindings(*__, **_) -> Never:
    """
    Qt's 'QList<Binding> QQmlSA::Element::propertyBindings(const QString
    &propertyName) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSA.Element.propertyBindings' has no cute function yet. Qt's "
        "'QList<Binding> QQmlSA::Element::propertyBindings(const QString "
        "&propertyName) const': gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QQmlSA::Element::swap(Element &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.Element.swap' has no cute function yet. Qt's 'void "
        "QQmlSA::Element::swap(Element &other)': takes a type Python has no "
        "way to hand over yet.")
