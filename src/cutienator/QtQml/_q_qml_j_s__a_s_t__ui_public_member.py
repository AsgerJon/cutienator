"""
QQmlJS::AST::UiPublicMember binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::UiPublicMember to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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


class UiPublicMember(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::UiPublicMember: a plain Python object
  standing in front of one C++ QQmlJS::AST::UiPublicMember.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::UiPublicMember that has a ritual and
  that Python can call so far, 17 names in all: 'firstSourceLocation',
  'lastSourceLocation', 'defaultToken', 'isDefaultMember', 'requiredToken',
  'isRequired', 'readonlyToken', 'isReadonly', 'finalToken', 'isFinal',
  'overrideToken', 'isOverride', 'virtualToken', 'isVirtual',
  'setAttributes', 'propertyToken', 'setPropertyToken'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::AST::UiPublicMember::UiPublicMember(UiQualifiedId
    *memberType, QStringView name, Statement *statement)': names
    'QQmlJS::AST::Statement', which has no cute class yet.
  - Qt's 'void QQmlJS::AST::UiPublicMember::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::UiPublicMember is created at the first use, not by
    'QQmlJS::AST::UiPublicMember(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::UiPublicMember.
  - Each name of Qt's QQmlJS::AST::UiPublicMember that has no cute function
    yet, 'accept0', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::AST::UiPublicMember'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def firstSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPublicMember::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#firstSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPublicMember::firstSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST14UiPublicMember19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST14UiPublicMember19firstSourceLocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPublicMember::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPublicMember::lastSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST14UiPublicMember18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST14UiPublicMember18lastSourceLocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def defaultToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::UiPublicMember::defaultToken()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#defaultToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPublicMember::defaultToken() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember12defaultTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isDefaultMember(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPublicMember::isDefaultMember() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#isDefaultMember
    """
    #  bool QQmlJS::AST::UiPublicMember::isDefaultMember() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember15isDefaultMemberEv',
    )

  def requiredToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::UiPublicMember::requiredToken()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#requiredToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPublicMember::requiredToken() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember13requiredTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPublicMember::isRequired() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#isRequired
    """
    #  bool QQmlJS::AST::UiPublicMember::isRequired() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember10isRequiredEv',
    )

  def readonlyToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::UiPublicMember::readonlyToken()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#readonlyToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPublicMember::readonlyToken() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember13readonlyTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isReadonly(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPublicMember::isReadonly() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#isReadonly
    """
    #  bool QQmlJS::AST::UiPublicMember::isReadonly() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember10isReadonlyEv',
    )

  def finalToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::UiPublicMember::finalToken()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#finalToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPublicMember::finalToken() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember10finalTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isFinal(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPublicMember::isFinal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#isFinal
    """
    #  bool QQmlJS::AST::UiPublicMember::isFinal() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember7isFinalEv',
    )

  def overrideToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::UiPublicMember::overrideToken()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#overrideToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPublicMember::overrideToken() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember13overrideTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isOverride(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPublicMember::isOverride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#isOverride
    """
    #  bool QQmlJS::AST::UiPublicMember::isOverride() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember10isOverrideEv',
    )

  def virtualToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::UiPublicMember::virtualToken()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#virtualToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPublicMember::virtualToken() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember12virtualTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  def isVirtual(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::UiPublicMember::isVirtual() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#isVirtual
    """
    #  bool QQmlJS::AST::UiPublicMember::isVirtual() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember9isVirtualEv',
    )

  def propertyToken(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::UiPublicMember::propertyToken()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#propertyToken

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPublicMember::propertyToken() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14UiPublicMember13propertyTokenEv',
    )
    return QQmlJS.SourceLocation._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QQmlJS.AST.UiPropertyAttributes'])
  @overload(NoneType)
  def setAttributes(
      self,
      attributes: Optional[QQmlJS.AST.UiPropertyAttributes],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJS::AST::UiPublicMember::setAttributes(UiPropertyAttributes
    *attributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#setAttributes

    Parameters
    ----------

    attributes : Optional[QQmlJS.AST.UiPropertyAttributes]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::UiPublicMember::setAttributes(UiPropertyAttributes
    #      *attributes)
    self.uglySide.call(
        'ritual_ZN6QQmlJS3AST14UiPublicMember13setAttributesEPNS0_20UiPrope'
        'rtyAttributesE',
        self._addressOf(attributes),
    )

  @overload(WAIT['QQmlJS.SourceLocation'])
  def setPropertyToken(self, token: QQmlJS.SourceLocation) -> None:
    """
    Calls Qt's 'void
    QQmlJS::AST::UiPublicMember::setPropertyToken(SourceLocation token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#setPropertyToken

    Parameters
    ----------

    token : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJS::AST::UiPublicMember::setPropertyToken(SourceLocation
    #      token)
    self.uglySide.call(
        'ritual_ZN6QQmlJS3AST14UiPublicMember16setPropertyTokenENS_14Source'
        'LocationE',
        self._valueOf(token),
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

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.UiQualifiedId'], str)
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, str)
  @overload(NoneType, WAIT['QQmlJS.AST.UiQualifiedId'], str)
  @overload(NoneType, NoneType, str)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      memberType: Optional[QQmlJS.AST.UiQualifiedId],
      name: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiPublicMember::UiPublicMember(UiQualifiedId *memberType,
    QStringView name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipublicmember.html#UiPublicMember

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    memberType : Optional[QQmlJS.AST.UiQualifiedId]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJS::AST::UiPublicMember::UiPublicMember(UiQualifiedId *memberType,
    #      QStringView name)
    self._noteCreation(UiPublicMember, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST14UiPublicMemberC1EPNS0_13UiQualifiedIdE11QStr'
        'ingView',
        self._addressOf(pool), self._addressOf(memberType), name,
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
    Qt's 'void QQmlJS::AST::UiPublicMember::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.UiPublicMember.accept0' has no cute function yet. Qt's "
        "'void QQmlJS::AST::UiPublicMember::accept0(BaseVisitor *visitor)': "
        "names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.")
