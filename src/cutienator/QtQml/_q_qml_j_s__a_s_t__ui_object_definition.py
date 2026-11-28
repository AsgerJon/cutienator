"""
QQmlJS::AST::UiObjectDefinition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::UiObjectDefinition to be private: it declares the
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


class UiObjectDefinition(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::UiObjectDefinition: a plain Python
  object standing in front of one C++ QQmlJS::AST::UiObjectDefinition.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::UiObjectDefinition that has a ritual
  and that Python can call so far, 2 names in all: 'firstSourceLocation',
  'lastSourceLocation'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::UiObjectDefinition::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::UiObjectDefinition is created at the first use, not
    by 'QQmlJS::AST::UiObjectDefinition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::UiObjectDefinition.
  - Each name of Qt's QQmlJS::AST::UiObjectDefinition that has no cute
    function yet, 'accept0', holds a function that raises
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
  __qt_class__ = 'QQmlJS::AST::UiObjectDefinition'

  #  A C++ QQmlJS::AST::UiObjectDefinition Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_UiObjectDefinition'

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
    QQmlJS::AST::UiObjectDefinition::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiobjectdefinition.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiObjectDefinition::firstSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST18UiObjectDefinition19firstSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST18UiObjectDefinition19firstSourceLocati'
          'onEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiObjectDefinition::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiobjectdefinition.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiObjectDefinition::lastSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST18UiObjectDefinition18lastSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST18UiObjectDefinition18lastSourceLocatio'
          'nEv')
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

  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.UiQualifiedId'],
      WAIT['QQmlJS.AST.UiObjectInitializer'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.UiQualifiedId'], NoneType,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], NoneType,
      WAIT['QQmlJS.AST.UiObjectInitializer'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType)
  @overload(
      NoneType, WAIT['QQmlJS.AST.UiQualifiedId'],
      WAIT['QQmlJS.AST.UiObjectInitializer'],
  )
  @overload(NoneType, WAIT['QQmlJS.AST.UiQualifiedId'], NoneType)
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.UiObjectInitializer'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      qualifiedTypeNameId: Optional[QQmlJS.AST.UiQualifiedId],
      initializer: Optional[QQmlJS.AST.UiObjectInitializer],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiObjectDefinition::UiObjectDefinition(UiQualifiedId
    *qualifiedTypeNameId, UiObjectInitializer *initializer)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiobjectdefinition.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    qualifiedTypeNameId : Optional[QQmlJS.AST.UiQualifiedId]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    initializer : Optional[QQmlJS.AST.UiObjectInitializer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::UiObjectDefinition::UiObjectDefinition(UiQualifiedId
    #      *qualifiedTypeNameId, UiObjectInitializer *initializer)
    self._noteCreation(UiObjectDefinition, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST18UiObjectDefinitionC1EPNS0_13UiQualifiedIdEPN'
        'S0_19UiObjectInitializerE',
        self._addressOf(pool), self._addressOf(qualifiedTypeNameId),
        self._addressOf(initializer),
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
    Qt's 'void QQmlJS::AST::UiObjectDefinition::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.UiObjectDefinition.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::UiObjectDefinition::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
