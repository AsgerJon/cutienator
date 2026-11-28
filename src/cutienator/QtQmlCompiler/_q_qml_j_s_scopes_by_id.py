"""
QQmlJSScopesById binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscopesbyid_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSScopesById to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QQmlJSScope

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlJSScopesById(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSScopesById: a plain Python object standing in
  front of one C++ QQmlJSScopesById.

  C++ hands a QQmlJSScopesById around as a copy, so every C++
  QQmlJSScopesById behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSScopesById that has a ritual and that Python
  can call so far, 11 names in all: 'componentsAreBound',
  'setComponentsAreBound', 'setSignaturesAreEnforced',
  'signaturesAreEnforced', 'setValueTypesAreAddressable',
  'valueTypesAreAddressable', 'setValueTypesAreAssertable',
  'valueTypesAreAssertable', 'clear', 'existsAnywhereInDocument',
  'confidence'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QString QQmlJSScopesById::id(const QQmlJSScope::ConstPtr &scope,
    const QQmlJSScope::ConstPtr &referrer, QQmlJSScopesByIdOptions options)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSScopesById::scope(const QString &id,
    const QQmlJSScope::ConstPtr &referrer, QQmlJSScopesByIdOptions options)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlJSScopesById::insert(const QString &id, const
    QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to hand
    over yet.
  - Qt's 'std::multimap<QQmlJSScope::ConstPtr, IdWithScope>
    QQmlJSScopesById::computeComponentRootsToIds()': gives a type Python has
    no way to take yet.
  - Qt's 'bool QQmlJSScopesById::isComponentVisible(const
    QQmlJSScope::ConstPtr &observed, const QQmlJSScope::ConstPtr &observer,
    QQmlJSScopesByIdOptions options) const': takes a type Python has no way
    to hand over yet.
  - Qt's 'QQmlJSScopesById::~QQmlJSScopesById()': the destructor: Python
    removes its C++ QQmlJSScopesById by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 3 a template.

  What to expect
  --------------

  - The C++ QQmlJSScopesById is created at the first use, not by
    'QQmlJSScopesById(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSScopesById back gives a copy the ritual made
    for Python, in a new cute QQmlJSScopesById.
  - Each name of Qt's QQmlJSScopesById that has no cute function yet,
    'computeComponentRootsToIds', 'id', 'insert', 'isComponentVisible',
    'possibleComponentRoots', 'possibleIds', 'possibleScopes', 'scope', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJSScopesById, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CallbackResult(CuteNum, scoped=True):
    """
    The enum 'QQmlJSScopesById::CallbackResult' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    StopSearch = Kee[int](0)
    ContinueSearch = Kee[int](1)

  class Confidence(CuteNum, scoped=True):
    """
    The enum 'QQmlJSScopesById::Confidence' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Certain = Kee[int](0)
    Possible = Kee[int](1)

  class Success(CuteNum, scoped=True):
    """
    The enum 'QQmlJSScopesById::Success' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  #  The classes Qt writes inside QQmlJSScopesById, each a class in here as
  #  in C++.

  class IdWithScope(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSScopesById::IdWithScope: a plain Python
    object standing in front of one C++ QQmlJSScopesById::IdWithScope.

    C++ hands a QQmlJSScopesById::IdWithScope around as a copy, so every C++
    QQmlJSScopesById::IdWithScope behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlJSScopesById::IdWithScope yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSScopesById::IdWithScope::~IdWithScope()': the destructor:
      Python removes its C++ QQmlJSScopesById::IdWithScope by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlJSScopesById::IdWithScope is created at the first use, not
      by 'QQmlJSScopesById::IdWithScope(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSScopesById::IdWithScope back gives a copy the
      ritual made for Python, in a new cute QQmlJSScopesById::IdWithScope.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSScopesById::IdWithScope'

    #  Qt's '~QQmlJSScopesById::IdWithScope()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlJSScopesById::IdWithScope behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QQmlJSScopesById11IdWithScopeD1Ev'

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

  @staticmethod
  @overload(QQmlJSScope.IsComponentRoot, QQmlJSScope.IsComponentRoot)
  def confidence(
      a: QQmlJSScope.IsComponentRoot,
      b: QQmlJSScope.IsComponentRoot,
  ) -> Confidence:
    """
    Calls Qt's 'Confidence
    QQmlJSScopesById::confidence(QQmlJSScope::IsComponentRoot a,
    QQmlJSScope::IsComponentRoot b)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscopesbyid.html#confidence

    Parameters
    ----------

    a : QQmlJSScope.IsComponentRoot
      Passed on as its number.

    b : QQmlJSScope.IsComponentRoot
      Passed on as its number.

    Returns
    -------

    Confidence
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Confidence(number)'
      gives.
    """
    #  Confidence QQmlJSScopesById::confidence(QQmlJSScope::IsComponentRoot
    #      a, QQmlJSScope::IsComponentRoot b)
    return QQmlJSScopesById.Confidence(Rituals.call(
        'ritual_ZN16QQmlJSScopesById10confidenceEN11QQmlJSScope15IsComponen'
        'tRootES1_',
        a.value, b.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSScopesById'

  #  Qt's '~QQmlJSScopesById()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJSScopesById behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QQmlJSScopesByIdD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def componentsAreBound(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScopesById::componentsAreBound() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscopesbyid.html#componentsAreBound
    """
    #  bool QQmlJSScopesById::componentsAreBound() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlJSScopesById18componentsAreBoundEv',
    )

  def signaturesAreEnforced(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScopesById::signaturesAreEnforced() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscopesbyid.html#signaturesAreEnforced
    """
    #  bool QQmlJSScopesById::signaturesAreEnforced() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlJSScopesById21signaturesAreEnforcedEv',
    )

  def valueTypesAreAddressable(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScopesById::valueTypesAreAddressable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscopesbyid.html#valueTypesAreAddressable
    """
    #  bool QQmlJSScopesById::valueTypesAreAddressable() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlJSScopesById24valueTypesAreAddressableEv',
    )

  def valueTypesAreAssertable(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSScopesById::valueTypesAreAssertable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscopesbyid.html#valueTypesAreAssertable
    """
    #  bool QQmlJSScopesById::valueTypesAreAssertable() const
    return self.uglySide.call(
        'ritual_ZNK16QQmlJSScopesById23valueTypesAreAssertableEv',
    )

  @overload(str)
  def existsAnywhereInDocument(self, id: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSScopesById::existsAnywhereInDocument(const QString
    &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscopesbyid.html#existsAnywhereInDocument

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSScopesById::existsAnywhereInDocument(const QString &id)
    #      const
    return self.uglySide.call(
        'ritual_ZNK16QQmlJSScopesById24existsAnywhereInDocumentERK7QString',
        id,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setComponentsAreBound(self, bound: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScopesById::setComponentsAreBound(bool bound)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscopesbyid.html#setComponentsAreBound

    Parameters
    ----------

    bound : bool
      Passed on as it is.
    """
    #  void QQmlJSScopesById::setComponentsAreBound(bool bound)
    self.uglySide.call(
        'ritual_ZN16QQmlJSScopesById21setComponentsAreBoundEb', bound,
    )

  @overload(bool)
  def setSignaturesAreEnforced(self, enforced: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScopesById::setSignaturesAreEnforced(bool
    enforced)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscopesbyid.html#setSignaturesAreEnforced

    Parameters
    ----------

    enforced : bool
      Passed on as it is.
    """
    #  void QQmlJSScopesById::setSignaturesAreEnforced(bool enforced)
    self.uglySide.call(
        'ritual_ZN16QQmlJSScopesById24setSignaturesAreEnforcedEb', enforced,
    )

  @overload(bool)
  def setValueTypesAreAddressable(self, addressable: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScopesById::setValueTypesAreAddressable(bool
    addressable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscopesbyid.html#setValueTypesAreAddressable

    Parameters
    ----------

    addressable : bool
      Passed on as it is.
    """
    #  void QQmlJSScopesById::setValueTypesAreAddressable(bool addressable)
    self.uglySide.call(
        'ritual_ZN16QQmlJSScopesById27setValueTypesAreAddressableEb',
        addressable,
    )

  @overload(bool)
  def setValueTypesAreAssertable(self, assertable: bool) -> None:
    """
    Calls Qt's 'void QQmlJSScopesById::setValueTypesAreAssertable(bool
    assertable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsscopesbyid.html#setValueTypesAreAssertable

    Parameters
    ----------

    assertable : bool
      Passed on as it is.
    """
    #  void QQmlJSScopesById::setValueTypesAreAssertable(bool assertable)
    self.uglySide.call(
        'ritual_ZN16QQmlJSScopesById26setValueTypesAreAssertableEb',
        assertable,
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QQmlJSScopesById::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsscopesbyid.html#clear
    """
    #  void QQmlJSScopesById::clear()
    self.uglySide.call('ritual_ZN16QQmlJSScopesById5clearEv')

  @staticmethod
  def computeComponentRootsToIds(*__, **_) -> Never:
    """
    Qt's 'std::multimap<QQmlJSScope::ConstPtr, IdWithScope>
    QQmlJSScopesById::computeComponentRootsToIds()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSScopesById.computeComponentRootsToIds' has no cute function "
        "yet. Qt's 'std::multimap<QQmlJSScope::ConstPtr, IdWithScope> "
        "QQmlJSScopesById::computeComponentRootsToIds()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def id(*__, **_) -> Never:
    """
    Qt's 'QString QQmlJSScopesById::id(const QQmlJSScope::ConstPtr &scope,
    const QQmlJSScope::ConstPtr &referrer, QQmlJSScopesByIdOptions options)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScopesById.id' has no cute function yet. Qt's 'QString "
        "QQmlJSScopesById::id(const QQmlJSScope::ConstPtr &scope, const "
        "QQmlJSScope::ConstPtr &referrer, QQmlJSScopesByIdOptions options) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def insert(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSScopesById::insert(const QString &id, const
    QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScopesById.insert' has no cute function yet. Qt's 'void "
        "QQmlJSScopesById::insert(const QString &id, const "
        "QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def isComponentVisible(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSScopesById::isComponentVisible(const
    QQmlJSScope::ConstPtr &observed, const QQmlJSScope::ConstPtr &observer,
    QQmlJSScopesByIdOptions options) const': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScopesById.isComponentVisible' has no cute function yet. "
        "Qt's 'bool QQmlJSScopesById::isComponentVisible(const "
        "QQmlJSScope::ConstPtr &observed, const QQmlJSScope::ConstPtr "
        "&observer, QQmlJSScopesByIdOptions options) const': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def possibleComponentRoots(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScopesById::possibleComponentRoots': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQmlJSScopesById.possibleComponentRoots' has no cute function "
        "yet. Qt's 'QQmlJSScopesById::possibleComponentRoots': a template: "
        "a pattern and no single function.")

  @staticmethod
  def possibleIds(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScopesById::possibleIds': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlJSScopesById.possibleIds' has no cute function yet. Qt's "
        "'QQmlJSScopesById::possibleIds': a template: a pattern and no "
        "single function.")

  @staticmethod
  def possibleScopes(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScopesById::possibleScopes': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlJSScopesById.possibleScopes' has no cute function yet. Qt's "
        "'QQmlJSScopesById::possibleScopes': a template: a pattern and no "
        "single function.")

  @staticmethod
  def scope(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSScopesById::scope(const QString &id,
    const QQmlJSScope::ConstPtr &referrer, QQmlJSScopesByIdOptions options)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSScopesById.scope' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSScopesById::scope(const QString &id, "
        "const QQmlJSScope::ConstPtr &referrer, QQmlJSScopesByIdOptions "
        "options) const': takes a type Python has no way to hand over yet.")
