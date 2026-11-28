"""
QQmlSA::Binding binding of the Qt C++
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
  from typing import Never, Optional


class Binding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::Binding: a plain Python object standing in
  front of one C++ QQmlSA::Binding.

  C++ hands a QQmlSA::Binding around as a copy, so every C++ QQmlSA::Binding
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::Binding that has a ritual and that Python
  can call so far, 19 names in all: 'd_func', 'groupType', 'bindingScope',
  'bindingType', 'stringValue', 'propertyName', 'isAttached', 'attachedType',
  'attachingType', 'sourceLocation', 'numberValue', 'scriptKind',
  'hasObject', 'objectType', 'hasUndefinedScriptValue',
  'hasFunctionScriptValue', '__eq__', '__ne__', 'isLiteralBinding'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const BindingPrivate *QQmlSA::Binding::d_func() const': takes in
    Python what 'BindingPrivate *QQmlSA::Binding::d_func()' takes.
  - Qt's 'QQmlSA::Binding::Binding(Binding &&a0)': takes a type Python has no
    way to hand over yet.
  - Qt's 'Binding &QQmlSA::Binding::operator=(const Binding &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'Binding &QQmlSA::Binding::operator=(Binding &&a0)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QQmlSA::Binding::~Binding()': the destructor: Python removes its
    C++ QQmlSA::Binding by it, and has no other use for it.
  - Qt's 'bool QQmlSA::Binding::operatorEqualsImpl(const Binding &a0, const
    Binding &a1)': an operator Python has no name for.

  What to expect
  --------------

  - The C++ QQmlSA::Binding is created at the first use, not by
    'QQmlSA::Binding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::Binding back gives a copy the ritual made for
    Python, in a new cute QQmlSA::Binding.
  """

  #  The classes Qt writes inside QQmlSA::Binding, each a class in here as in
  #  C++.

  class Bindings(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlSA::Binding::Bindings: a plain Python object
    standing in front of one C++ QQmlSA::Binding::Bindings.

    C++ hands a QQmlSA::Binding::Bindings around as a copy, so every C++
    QQmlSA::Binding::Bindings behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlSA::Binding::Bindings that has a ritual and
    that Python can call so far, 1 name in all: 'd_func'. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'const BindingsPrivate *QQmlSA::Binding::Bindings::d_func()
      const': takes in Python what 'BindingsPrivate
      *QQmlSA::Binding::Bindings::d_func()' takes.
    - Qt's 'QQmlSA::Binding::Bindings::~Bindings()': the destructor: Python
      removes its C++ QQmlSA::Binding::Bindings by it, and has no other use
      for it.
    - Qt's 'QMultiHash<QString, Binding>::const_iterator
      QQmlSA::Binding::Bindings::begin() const': gives a type Python has no
      way to take yet.
    - Qt's 'QMultiHash<QString, Binding>::const_iterator
      QQmlSA::Binding::Bindings::end() const': gives a type Python has no way
      to take yet.
    - Qt's 'QMultiHash<QString, Binding>::const_iterator
      QQmlSA::Binding::Bindings::constBegin() const': gives a type Python has
      no way to take yet.
    - Qt's 'QMultiHash<QString, Binding>::const_iterator
      QQmlSA::Binding::Bindings::constEnd() const': gives a type Python has
      no way to take yet.

    What to expect
    --------------

    - The C++ QQmlSA::Binding::Bindings is created at the first use, not by
      'QQmlSA::Binding::Bindings(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlSA::Binding::Bindings back gives a copy the
      ritual made for Python, in a new cute QQmlSA::Binding::Bindings.
    - Each name of Qt's QQmlSA::Binding::Bindings that has no cute function
      yet, 'begin', 'constBegin', 'constEnd', 'end', holds a function that
      raises 'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlSA::Binding::Bindings'

    #  Qt's '~QQmlSA::Binding::Bindings()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlSA::Binding::Bindings behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN6QQmlSA7Binding8BindingsD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QQmlSA::Binding::Bindings::Bindings()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlsa-binding-bindings.html#Bindings
      """
      #  QQmlSA::Binding::Bindings::Bindings()
      self._noteCreation(Binding.Bindings, lambda: Rituals.call(
          'ritual_ZN6QQmlSA7Binding8BindingsC1Ev',
      ))

    @overload(THIS)
    def __init__(self, a0: Binding.Bindings) -> None:
      """
      Notes what was given, for Qt's
      'QQmlSA::Binding::Bindings::Bindings(const Bindings &a0)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlsa-binding-bindings.html#Bindings

      Parameters
      ----------

      a0 : Binding.Bindings
        Passed on as a value: Qt reads the C++ QQmlSA::Binding::Bindings,
        which stays Python's own.
      """
      #  QQmlSA::Binding::Bindings::Bindings(const Bindings &a0)
      self._noteCreation(Binding.Bindings, lambda: Rituals.call(
          'ritual_ZN6QQmlSA7Binding8BindingsC1ERKS1_', self._valueOf(a0),
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

    def d_func(self) -> Optional[QQmlSA.BindingsPrivate]:
      """
      Calls Qt's 'BindingsPrivate *QQmlSA::Binding::Bindings::d_func()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlsa-binding-bindings.html#d_func

      Returns
      -------

      Optional[QQmlSA.BindingsPrivate]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  BindingsPrivate *QQmlSA::Binding::Bindings::d_func()
      address = self.uglySide.call(
          'ritual_ZN6QQmlSA7Binding8Bindings6d_funcEv',
      )
      return QQmlSA.BindingsPrivate._cuteAt(address)

    @staticmethod
    def begin(*__, **_) -> Never:
      """
      Qt's 'QMultiHash<QString, Binding>::const_iterator
      QQmlSA::Binding::Bindings::begin() const': gives a type Python has no
      way to take yet.
      """
      raise NotImplementedError(
          "'QQmlSA.Binding.Bindings.begin' has no cute function yet. Qt's "
          "'QMultiHash<QString, Binding>::const_iterator "
          "QQmlSA::Binding::Bindings::begin() const': gives a type Python "
          "has no way to take yet.")

    @staticmethod
    def constBegin(*__, **_) -> Never:
      """
      Qt's 'QMultiHash<QString, Binding>::const_iterator
      QQmlSA::Binding::Bindings::constBegin() const': gives a type Python has
      no way to take yet.
      """
      raise NotImplementedError(
          "'QQmlSA.Binding.Bindings.constBegin' has no cute function yet. "
          "Qt's 'QMultiHash<QString, Binding>::const_iterator "
          "QQmlSA::Binding::Bindings::constBegin() const': gives a type "
          "Python has no way to take yet.")

    @staticmethod
    def constEnd(*__, **_) -> Never:
      """
      Qt's 'QMultiHash<QString, Binding>::const_iterator
      QQmlSA::Binding::Bindings::constEnd() const': gives a type Python has
      no way to take yet.
      """
      raise NotImplementedError(
          "'QQmlSA.Binding.Bindings.constEnd' has no cute function yet. "
          "Qt's 'QMultiHash<QString, Binding>::const_iterator "
          "QQmlSA::Binding::Bindings::constEnd() const': gives a type "
          "Python has no way to take yet.")

    @staticmethod
    def end(*__, **_) -> Never:
      """
      Qt's 'QMultiHash<QString, Binding>::const_iterator
      QQmlSA::Binding::Bindings::end() const': gives a type Python has no way
      to take yet.
      """
      raise NotImplementedError(
          "'QQmlSA.Binding.Bindings.end' has no cute function yet. Qt's "
          "'QMultiHash<QString, Binding>::const_iterator "
          "QQmlSA::Binding::Bindings::end() const': gives a type Python has "
          "no way to take yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlSA.BindingType)
  def isLiteralBinding(a0: QQmlSA.BindingType) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Binding::isLiteralBinding(BindingType a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-binding.html#isLiteralBinding

    Parameters
    ----------

    a0 : QQmlSA.BindingType
      Passed on as its number.
    """
    #  bool QQmlSA::Binding::isLiteralBinding(BindingType a0)
    return Rituals.call(
        'ritual_ZN6QQmlSA7Binding16isLiteralBindingENS_11BindingTypeE',
        a0.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::Binding'

  #  Qt's '~QQmlSA::Binding()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlSA::Binding behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA7BindingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def groupType(self) -> QQmlSA.Element:
    """
    Calls Qt's 'Element QQmlSA::Binding::groupType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#groupType

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::Binding::groupType() const
    address = self.uglySide.call('ritual_ZNK6QQmlSA7Binding9groupTypeEv')
    return QQmlSA.Element._cuteOwning(address)

  def bindingScope(self) -> QQmlSA.Element:
    """
    Calls Qt's 'Element QQmlSA::Binding::bindingScope() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#bindingScope

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::Binding::bindingScope() const
    address = self.uglySide.call('ritual_ZNK6QQmlSA7Binding12bindingScopeEv')
    return QQmlSA.Element._cuteOwning(address)

  def bindingType(self) -> QQmlSA.BindingType:
    """
    Calls Qt's 'BindingType QQmlSA::Binding::bindingType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#bindingType

    Returns
    -------

    QQmlSA.BindingType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.BindingType(number)' gives.
    """
    #  BindingType QQmlSA::Binding::bindingType() const
    return QQmlSA.BindingType(self.uglySide.call(
        'ritual_ZNK6QQmlSA7Binding11bindingTypeEv',
    ))

  def stringValue(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::Binding::stringValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#stringValue

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::Binding::stringValue() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Binding11stringValueEv')

  def propertyName(self) -> str:
    """
    Calls Qt's 'QString QQmlSA::Binding::propertyName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#propertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::Binding::propertyName() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Binding12propertyNameEv')

  def isAttached(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Binding::isAttached() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#isAttached
    """
    #  bool QQmlSA::Binding::isAttached() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Binding10isAttachedEv')

  def attachedType(self) -> QQmlSA.Element:
    """
    Calls Qt's 'Element QQmlSA::Binding::attachedType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#attachedType

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::Binding::attachedType() const
    address = self.uglySide.call('ritual_ZNK6QQmlSA7Binding12attachedTypeEv')
    return QQmlSA.Element._cuteOwning(address)

  def attachingType(self) -> QQmlSA.Element:
    """
    Calls Qt's 'Element QQmlSA::Binding::attachingType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#attachingType

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::Binding::attachingType() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA7Binding13attachingTypeEv',
    )
    return QQmlSA.Element._cuteOwning(address)

  def sourceLocation(self) -> QQmlSA.SourceLocation:
    """
    Calls Qt's 'QQmlSA::SourceLocation QQmlSA::Binding::sourceLocation()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#sourceLocation

    Returns
    -------

    QQmlSA.SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlSA::SourceLocation QQmlSA::Binding::sourceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA7Binding14sourceLocationEv',
    )
    return QQmlSA.SourceLocation._cuteOwning(address)

  def numberValue(self) -> float:
    """
    Calls Qt's 'double QQmlSA::Binding::numberValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#numberValue
    """
    #  double QQmlSA::Binding::numberValue() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Binding11numberValueEv')

  def scriptKind(self) -> QQmlSA.ScriptBindingKind:
    """
    Calls Qt's 'ScriptBindingKind QQmlSA::Binding::scriptKind() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#scriptKind

    Returns
    -------

    QQmlSA.ScriptBindingKind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.ScriptBindingKind(number)' gives.
    """
    #  ScriptBindingKind QQmlSA::Binding::scriptKind() const
    return QQmlSA.ScriptBindingKind(self.uglySide.call(
        'ritual_ZNK6QQmlSA7Binding10scriptKindEv',
    ))

  def hasObject(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Binding::hasObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#hasObject
    """
    #  bool QQmlSA::Binding::hasObject() const
    return self.uglySide.call('ritual_ZNK6QQmlSA7Binding9hasObjectEv')

  def objectType(self) -> QQmlSA.Element:
    """
    Calls Qt's 'Element QQmlSA::Binding::objectType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#objectType

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::Binding::objectType() const
    address = self.uglySide.call('ritual_ZNK6QQmlSA7Binding10objectTypeEv')
    return QQmlSA.Element._cuteOwning(address)

  def hasUndefinedScriptValue(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Binding::hasUndefinedScriptValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-binding.html#hasUndefinedScriptValue
    """
    #  bool QQmlSA::Binding::hasUndefinedScriptValue() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Binding23hasUndefinedScriptValueEv',
    )

  def hasFunctionScriptValue(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::Binding::hasFunctionScriptValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-binding.html#hasFunctionScriptValue
    """
    #  bool QQmlSA::Binding::hasFunctionScriptValue() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA7Binding22hasFunctionScriptValueEv',
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
  def __eq__(self, rhs: Binding) -> bool:
    """
    Calls Qt's 'bool operator==(const Binding &lhs, const Binding &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#operator==

    Parameters
    ----------

    rhs : Binding
      Passed on as a value: Qt reads the C++ QQmlSA::Binding, which stays
      Python's own.
    """
    #  bool operator==(const Binding &lhs, const Binding &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAeqERKNS_7BindingES2_',
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
  def __ne__(self, rhs: Binding) -> bool:
    """
    Calls Qt's 'bool operator!=(const Binding &lhs, const Binding &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#operator!=

    Parameters
    ----------

    rhs : Binding
      Passed on as a value: Qt reads the C++ QQmlSA::Binding, which stays
      Python's own.
    """
    #  bool operator!=(const Binding &lhs, const Binding &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAneERKNS_7BindingES2_',
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
    Notes what was given, for Qt's 'QQmlSA::Binding::Binding()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#Binding
    """
    #  QQmlSA::Binding::Binding()
    self._noteCreation(Binding, lambda: Rituals.call(
        'ritual_ZN6QQmlSA7BindingC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: Binding) -> None:
    """
    Notes what was given, for Qt's 'QQmlSA::Binding::Binding(const Binding
    &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#Binding

    Parameters
    ----------

    a0 : Binding
      Passed on as a value: Qt reads the C++ QQmlSA::Binding, which stays
      Python's own.
    """
    #  QQmlSA::Binding::Binding(const Binding &a0)
    self._noteCreation(Binding, lambda: Rituals.call(
        'ritual_ZN6QQmlSA7BindingC1ERKS0_', self._valueOf(a0),
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

  def d_func(self) -> Optional[QQmlSA.BindingPrivate]:
    """
    Calls Qt's 'BindingPrivate *QQmlSA::Binding::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-binding.html#d_func

    Returns
    -------

    Optional[QQmlSA.BindingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  BindingPrivate *QQmlSA::Binding::d_func()
    address = self.uglySide.call('ritual_ZN6QQmlSA7Binding6d_funcEv')
    return QQmlSA.BindingPrivate._cuteAt(address)
