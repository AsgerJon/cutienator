"""
QQmlJS::AST::UiPropertyAttributes binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::UiPropertyAttributes to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class UiPropertyAttributes(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::UiPropertyAttributes: a plain Python
  object standing in front of one C++ QQmlJS::AST::UiPropertyAttributes.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::UiPropertyAttributes that has a ritual
  and that Python can call so far, 15 names in all: 'defaultToken',
  'isDefaultMember', 'requiredToken', 'isRequired', 'readonlyToken',
  'isReadonly', 'finalToken', 'isFinal', 'virtualToken', 'isVirtual',
  'overrideToken', 'isOverride', 'propertyToken', 'firstSourceLocation',
  'lastSourceLocation'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::UiPropertyAttributes::accept0(BaseVisitor *a0)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 18 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlJS::AST::UiPropertyAttributes is created at the first use,
    not by 'QQmlJS::AST::UiPropertyAttributes(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::UiPropertyAttributes.
  - Each name of Qt's QQmlJS::AST::UiPropertyAttributes that has no cute
    function yet, 'accept0', 'compareLocationsByBegin', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::AST::UiPropertyAttributes'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def defaultToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPropertyAttributes::defaultToken() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#defaultToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPropertyAttributes::defaultToken() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes12defaultTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isDefaultMember(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPropertyAttributes::isDefaultMember()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html
    """
    #  bool QQmlJS::AST::UiPropertyAttributes::isDefaultMember() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes15isDefaultMemberEv',
    )

  def requiredToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPropertyAttributes::requiredToken() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#requiredToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPropertyAttributes::requiredToken()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes13requiredTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPropertyAttributes::isRequired() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#isRequired
    """
    #  bool QQmlJS::AST::UiPropertyAttributes::isRequired() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes10isRequiredEv',
    )

  def readonlyToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPropertyAttributes::readonlyToken() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#readonlyToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPropertyAttributes::readonlyToken()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes13readonlyTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isReadonly(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPropertyAttributes::isReadonly() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#isReadonly
    """
    #  bool QQmlJS::AST::UiPropertyAttributes::isReadonly() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes10isReadonlyEv',
    )

  def finalToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPropertyAttributes::finalToken() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#finalToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPropertyAttributes::finalToken() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes10finalTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isFinal(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPropertyAttributes::isFinal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#isFinal
    """
    #  bool QQmlJS::AST::UiPropertyAttributes::isFinal() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes7isFinalEv',
    )

  def virtualToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPropertyAttributes::virtualToken() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#virtualToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPropertyAttributes::virtualToken() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes12virtualTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isVirtual(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPropertyAttributes::isVirtual() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#isVirtual
    """
    #  bool QQmlJS::AST::UiPropertyAttributes::isVirtual() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes9isVirtualEv',
    )

  def overrideToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPropertyAttributes::overrideToken() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#overrideToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPropertyAttributes::overrideToken()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes13overrideTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isOverride(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPropertyAttributes::isOverride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#isOverride
    """
    #  bool QQmlJS::AST::UiPropertyAttributes::isOverride() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes10isOverrideEv',
    )

  def propertyToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPropertyAttributes::propertyToken() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html#propertyToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPropertyAttributes::propertyToken()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes13propertyTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def firstSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPropertyAttributes::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation
    #      QQmlJS::AST::UiPropertyAttributes::firstSourceLocation() const
    ritual = (
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes19firstSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST20UiPropertyAttributes19firstSourceLoca'
          'tionEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPropertyAttributes::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPropertyAttributes::lastSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST20UiPropertyAttributes18lastSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST20UiPropertyAttributes18lastSourceLocat'
          'ionEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QQmlJS.MemoryPool'])
  @overload(NoneType)
  def __init__(self, pool: Optional[QQmlJS.MemoryPool]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiPropertyAttributes::UiPropertyAttributes()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipropertyattributes.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::UiPropertyAttributes::UiPropertyAttributes()
    self._noteCreation(UiPropertyAttributes, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST20UiPropertyAttributesC1Ev',
        self._addressOf(pool),
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
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::UiPropertyAttributes::accept0(BaseVisitor *a0)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.UiPropertyAttributes.accept0' has no cute function "
        "yet. Qt's 'void "
        "QQmlJS::AST::UiPropertyAttributes::accept0(BaseVisitor *a0)': "
        "names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.")

  @staticmethod
  def compareLocationsByBegin(*__, **_) -> Never:
    """
    Qt's 'QQmlJS::AST::UiPropertyAttributes::compareLocationsByBegin': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.UiPropertyAttributes.compareLocationsByBegin' has no "
        "cute function yet. Qt's "
        "'QQmlJS::AST::UiPropertyAttributes::compareLocationsByBegin': a "
        "template: a pattern and no single function.")
