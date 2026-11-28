"""
QQmlJS::AST::Visitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsastvisitor_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlJS::AST::Visitor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class Visitor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::Visitor: a plain Python object standing
  in front of one C++ QQmlJS::AST::Visitor.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::Visitor that has a ritual and that
  Python can call so far, 2 names in all: 'visit', 'endVisit'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QQmlJS::AST::Visitor::preVisit(Node *a0)': names
    'QQmlJS::AST::Node', which has no cute class yet.
  - Qt's 'void QQmlJS::AST::Visitor::postVisit(Node *a0)': names
    'QQmlJS::AST::Node', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::Visitor is created at the first use, not by
    'QQmlJS::AST::Visitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::Visitor.
  - Each name of Qt's QQmlJS::AST::Visitor that has no cute function yet,
    'postVisit', 'preVisit', holds a function that raises
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
  __qt_class__ = 'QQmlJS::AST::Visitor'

  #  A C++ QQmlJS::AST::Visitor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_Visitor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  @overload(int)
  def __init__(self, parentRecursionDepth: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QQmlJS::AST::Visitor::Visitor(quint16
    parentRecursionDepth)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#Visitor

    Parameters
    ----------

    parentRecursionDepth : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QQmlJS::AST::Visitor::Visitor(quint16 parentRecursionDepth)
    self._noteCreation(Visitor, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST7VisitorC1Et', parentRecursionDepth,
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

  @overload(WAIT['QQmlJS.AST.UiProgram'])
  @overload(NoneType)
  def visit(self, a0: Optional[QQmlJS.AST.UiProgram]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiProgram *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiProgram *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_9UiProgramE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_9UiProgramE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiHeaderItemList'])
  def visit(self, a0: Optional[QQmlJS.AST.UiHeaderItemList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiHeaderItemList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiHeaderItemList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiHeaderItemList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiHeaderItemListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiHeaderItemListE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiPragmaValueList'])
  def visit(self, a0: Optional[QQmlJS.AST.UiPragmaValueList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiPragmaValueList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiPragmaValueList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiPragmaValueList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiPragmaValueListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiPragmaValueListE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiPragma'])
  def visit(self, a0: Optional[QQmlJS.AST.UiPragma]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiPragma *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiPragma]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiPragma *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_8UiPragmaE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_8UiPragmaE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiImport'])
  def visit(self, a0: Optional[QQmlJS.AST.UiImport]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiImport *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiImport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiImport *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_8UiImportE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_8UiImportE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiPublicMember'])
  def visit(self, a0: Optional[QQmlJS.AST.UiPublicMember]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiPublicMember *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiPublicMember]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiPublicMember *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14UiPublicMemberE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14UiPublicMemberE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiSourceElement'])
  def visit(self, a0: Optional[QQmlJS.AST.UiSourceElement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiSourceElement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiSourceElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiSourceElement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiSourceElementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiSourceElementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiObjectDefinition'])
  def visit(self, a0: Optional[QQmlJS.AST.UiObjectDefinition]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiObjectDefinition *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiObjectDefinition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiObjectDefinition *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiObjectDefinitionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiObjectDefinition'
          'E')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiObjectInitializer'])
  def visit(self, a0: Optional[QQmlJS.AST.UiObjectInitializer]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiObjectInitializer *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiObjectInitializer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiObjectInitializer *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19UiObjectInitializerE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19UiObjectInitialize'
          'rE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiObjectBinding'])
  def visit(self, a0: Optional[QQmlJS.AST.UiObjectBinding]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiObjectBinding *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiObjectBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiObjectBinding *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiObjectBindingE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiObjectBindingE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  def visit(self, a0: Optional[QQmlJS.AST.UiScriptBinding]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiScriptBinding *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiScriptBinding *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiScriptBindingE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiScriptBindingE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiArrayBinding'])
  def visit(self, a0: Optional[QQmlJS.AST.UiArrayBinding]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiArrayBinding *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiArrayBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiArrayBinding *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14UiArrayBindingE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14UiArrayBindingE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiParameterList'])
  def visit(self, a0: Optional[QQmlJS.AST.UiParameterList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiParameterList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiParameterList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiParameterList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiParameterListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiParameterListE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiObjectMemberList'])
  def visit(self, a0: Optional[QQmlJS.AST.UiObjectMemberList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiObjectMemberList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiObjectMemberList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiObjectMemberList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiObjectMemberListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiObjectMemberList'
          'E')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiArrayMemberList'])
  def visit(self, a0: Optional[QQmlJS.AST.UiArrayMemberList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiArrayMemberList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiArrayMemberList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiArrayMemberList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiArrayMemberListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiArrayMemberListE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiQualifiedId'])
  def visit(self, a0: Optional[QQmlJS.AST.UiQualifiedId]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiQualifiedId *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiQualifiedId]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiQualifiedId *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13UiQualifiedIdE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13UiQualifiedIdE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiEnumDeclaration'])
  def visit(self, a0: Optional[QQmlJS.AST.UiEnumDeclaration]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiEnumDeclaration *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiEnumDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiEnumDeclaration *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiEnumDeclarationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiEnumDeclarationE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiEnumMemberList'])
  def visit(self, a0: Optional[QQmlJS.AST.UiEnumMemberList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiEnumMemberList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiEnumMemberList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiEnumMemberList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiEnumMemberListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiEnumMemberListE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiVersionSpecifier'])
  def visit(self, a0: Optional[QQmlJS.AST.UiVersionSpecifier]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiVersionSpecifier *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiVersionSpecifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiVersionSpecifier *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiVersionSpecifierE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiVersionSpecifier'
          'E')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiInlineComponent'])
  def visit(self, a0: Optional[QQmlJS.AST.UiInlineComponent]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiInlineComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiInlineComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiInlineComponent *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiInlineComponentE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiInlineComponentE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiAnnotation'])
  def visit(self, a0: Optional[QQmlJS.AST.UiAnnotation]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiAnnotation *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiAnnotation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiAnnotation *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12UiAnnotationE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12UiAnnotationE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiAnnotationList'])
  def visit(self, a0: Optional[QQmlJS.AST.UiAnnotationList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiAnnotationList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiAnnotationList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiAnnotationList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiAnnotationListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiAnnotationListE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiRequired'])
  def visit(self, a0: Optional[QQmlJS.AST.UiRequired]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UiRequired *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiRequired]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UiRequired *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_10UiRequiredE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_10UiRequiredE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TypeExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.TypeExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(TypeExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TypeExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(TypeExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TypeExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TypeExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ThisExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.ThisExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ThisExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ThisExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ThisExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14ThisExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14ThisExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.IdentifierExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.IdentifierExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(IdentifierExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.IdentifierExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(IdentifierExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_20IdentifierExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_20IdentifierExpressi'
          'onE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NullExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.NullExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(NullExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NullExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(NullExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14NullExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14NullExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TrueLiteral'])
  def visit(self, a0: Optional[QQmlJS.AST.TrueLiteral]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(TrueLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TrueLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(TrueLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_11TrueLiteralE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_11TrueLiteralE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FalseLiteral'])
  def visit(self, a0: Optional[QQmlJS.AST.FalseLiteral]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(FalseLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FalseLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(FalseLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12FalseLiteralE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12FalseLiteralE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.SuperLiteral'])
  def visit(self, a0: Optional[QQmlJS.AST.SuperLiteral]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(SuperLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.SuperLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(SuperLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12SuperLiteralE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12SuperLiteralE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.StringLiteral'])
  def visit(self, a0: Optional[QQmlJS.AST.StringLiteral]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(StringLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.StringLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(StringLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13StringLiteralE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13StringLiteralE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TemplateLiteral'])
  def visit(self, a0: Optional[QQmlJS.AST.TemplateLiteral]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(TemplateLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TemplateLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(TemplateLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15TemplateLiteralE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15TemplateLiteralE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NumericLiteral'])
  def visit(self, a0: Optional[QQmlJS.AST.NumericLiteral]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(NumericLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NumericLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(NumericLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14NumericLiteralE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14NumericLiteralE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.RegExpLiteral'])
  def visit(self, a0: Optional[QQmlJS.AST.RegExpLiteral]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(RegExpLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.RegExpLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(RegExpLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13RegExpLiteralE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13RegExpLiteralE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ArrayPattern'])
  def visit(self, a0: Optional[QQmlJS.AST.ArrayPattern]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ArrayPattern *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ArrayPattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ArrayPattern *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ArrayPatternE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ArrayPatternE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ObjectPattern'])
  def visit(self, a0: Optional[QQmlJS.AST.ObjectPattern]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ObjectPattern *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ObjectPattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ObjectPattern *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13ObjectPatternE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13ObjectPatternE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PatternElementList'])
  def visit(self, a0: Optional[QQmlJS.AST.PatternElementList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(PatternElementList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PatternElementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(PatternElementList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_18PatternElementListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_18PatternElementList'
          'E')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PatternPropertyList'])
  def visit(self, a0: Optional[QQmlJS.AST.PatternPropertyList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(PatternPropertyList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PatternPropertyList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(PatternPropertyList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19PatternPropertyListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19PatternPropertyLis'
          'tE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PatternElement'])
  def visit(self, a0: Optional[QQmlJS.AST.PatternElement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(PatternElement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PatternElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(PatternElement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14PatternElementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14PatternElementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PatternProperty'])
  def visit(self, a0: Optional[QQmlJS.AST.PatternProperty]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(PatternProperty *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PatternProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(PatternProperty *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15PatternPropertyE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15PatternPropertyE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Elision'])
  def visit(self, a0: Optional[QQmlJS.AST.Elision]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(Elision *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Elision]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(Elision *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_7ElisionE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_7ElisionE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NestedExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.NestedExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(NestedExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NestedExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(NestedExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16NestedExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16NestedExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.IdentifierPropertyName'])
  def visit(self, a0: Optional[QQmlJS.AST.IdentifierPropertyName]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(IdentifierPropertyName
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.IdentifierPropertyName]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(IdentifierPropertyName *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_22IdentifierPropertyNameE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_22IdentifierProperty'
          'NameE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.StringLiteralPropertyName'])
  def visit(
      self,
      a0: Optional[QQmlJS.AST.StringLiteralPropertyName],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(StringLiteralPropertyName
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.StringLiteralPropertyName]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(StringLiteralPropertyName *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_25StringLiteralPropertyNam'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_25StringLiteralPrope'
          'rtyNameE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NumericLiteralPropertyName'])
  def visit(
      self,
      a0: Optional[QQmlJS.AST.NumericLiteralPropertyName],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(NumericLiteralPropertyName
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NumericLiteralPropertyName]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(NumericLiteralPropertyName *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_26NumericLiteralPropertyNa'
        'meE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_26NumericLiteralProp'
          'ertyNameE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ComputedPropertyName'])
  def visit(self, a0: Optional[QQmlJS.AST.ComputedPropertyName]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ComputedPropertyName *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ComputedPropertyName]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ComputedPropertyName *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_20ComputedPropertyNameE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_20ComputedPropertyNa'
          'meE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ArrayMemberExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.ArrayMemberExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ArrayMemberExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ArrayMemberExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ArrayMemberExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_21ArrayMemberExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_21ArrayMemberExpress'
          'ionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FieldMemberExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.FieldMemberExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(FieldMemberExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FieldMemberExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(FieldMemberExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_21FieldMemberExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_21FieldMemberExpress'
          'ionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TaggedTemplate'])
  def visit(self, a0: Optional[QQmlJS.AST.TaggedTemplate]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(TaggedTemplate *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TaggedTemplate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(TaggedTemplate *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TaggedTemplateE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TaggedTemplateE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NewMemberExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.NewMemberExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(NewMemberExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NewMemberExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(NewMemberExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19NewMemberExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19NewMemberExpressio'
          'nE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NewExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.NewExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(NewExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NewExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(NewExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13NewExpressionE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13NewExpressionE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.CallExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.CallExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(CallExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.CallExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(CallExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14CallExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14CallExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ArgumentList'])
  def visit(self, a0: Optional[QQmlJS.AST.ArgumentList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ArgumentList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ArgumentList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ArgumentList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ArgumentListE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ArgumentListE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PostIncrementExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.PostIncrementExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(PostIncrementExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PostIncrementExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(PostIncrementExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_23PostIncrementExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_23PostIncrementExpre'
          'ssionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PostDecrementExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.PostDecrementExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(PostDecrementExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PostDecrementExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(PostDecrementExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_23PostDecrementExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_23PostDecrementExpre'
          'ssionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.DeleteExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.DeleteExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(DeleteExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.DeleteExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(DeleteExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16DeleteExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16DeleteExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.VoidExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.VoidExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(VoidExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.VoidExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(VoidExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14VoidExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14VoidExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TypeOfExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.TypeOfExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(TypeOfExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TypeOfExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(TypeOfExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16TypeOfExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16TypeOfExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PreIncrementExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.PreIncrementExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(PreIncrementExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PreIncrementExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(PreIncrementExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_22PreIncrementExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_22PreIncrementExpres'
          'sionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PreDecrementExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.PreDecrementExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(PreDecrementExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PreDecrementExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(PreDecrementExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_22PreDecrementExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_22PreDecrementExpres'
          'sionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UnaryPlusExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.UnaryPlusExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UnaryPlusExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UnaryPlusExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UnaryPlusExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19UnaryPlusExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19UnaryPlusExpressio'
          'nE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UnaryMinusExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.UnaryMinusExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(UnaryMinusExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UnaryMinusExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(UnaryMinusExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_20UnaryMinusExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_20UnaryMinusExpressi'
          'onE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TildeExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.TildeExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(TildeExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TildeExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(TildeExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15TildeExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15TildeExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NotExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.NotExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(NotExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NotExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(NotExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13NotExpressionE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13NotExpressionE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.BinaryExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.BinaryExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(BinaryExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.BinaryExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(BinaryExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16BinaryExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16BinaryExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ConditionalExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.ConditionalExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ConditionalExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ConditionalExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ConditionalExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_21ConditionalExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_21ConditionalExpress'
          'ionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.CommaExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.CommaExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(CommaExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.CommaExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(CommaExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15CommaExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15CommaExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Block'])
  def visit(self, a0: Optional[QQmlJS.AST.Block]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(Block *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Block]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(Block *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_5BlockE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_5BlockE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.StatementList'])
  def visit(self, a0: Optional[QQmlJS.AST.StatementList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(StatementList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.StatementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(StatementList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13StatementListE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13StatementListE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.VariableStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.VariableStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(VariableStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.VariableStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(VariableStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17VariableStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17VariableStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.VariableDeclarationList'])
  def visit(self, a0: Optional[QQmlJS.AST.VariableDeclarationList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(VariableDeclarationList
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.VariableDeclarationList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(VariableDeclarationList *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_23VariableDeclarationListE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_23VariableDeclaratio'
          'nListE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.EmptyStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.EmptyStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(EmptyStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.EmptyStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(EmptyStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14EmptyStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14EmptyStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExpressionStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.ExpressionStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ExpressionStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ExpressionStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ExpressionStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19ExpressionStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19ExpressionStatemen'
          'tE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.IfStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.IfStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(IfStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.IfStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(IfStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_11IfStatementE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_11IfStatementE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.DoWhileStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.DoWhileStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(DoWhileStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.DoWhileStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(DoWhileStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16DoWhileStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16DoWhileStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.WhileStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.WhileStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(WhileStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.WhileStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(WhileStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14WhileStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14WhileStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ForStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.ForStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ForStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ForStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ForStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ForStatementE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ForStatementE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ForEachStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.ForEachStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ForEachStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ForEachStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ForEachStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ForEachStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ForEachStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ContinueStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.ContinueStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ContinueStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ContinueStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ContinueStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ContinueStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ContinueStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.BreakStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.BreakStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(BreakStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.BreakStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(BreakStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14BreakStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14BreakStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ReturnStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.ReturnStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ReturnStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ReturnStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ReturnStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ReturnStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ReturnStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.YieldExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.YieldExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(YieldExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.YieldExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(YieldExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15YieldExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15YieldExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.WithStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.WithStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(WithStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.WithStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(WithStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13WithStatementE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13WithStatementE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.SwitchStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.SwitchStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(SwitchStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.SwitchStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(SwitchStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15SwitchStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15SwitchStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.CaseBlock'])
  def visit(self, a0: Optional[QQmlJS.AST.CaseBlock]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(CaseBlock *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.CaseBlock]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(CaseBlock *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_9CaseBlockE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_9CaseBlockE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.CaseClauses'])
  def visit(self, a0: Optional[QQmlJS.AST.CaseClauses]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(CaseClauses *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.CaseClauses]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(CaseClauses *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_11CaseClausesE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_11CaseClausesE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.CaseClause'])
  def visit(self, a0: Optional[QQmlJS.AST.CaseClause]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(CaseClause *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.CaseClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(CaseClause *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_10CaseClauseE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_10CaseClauseE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.DefaultClause'])
  def visit(self, a0: Optional[QQmlJS.AST.DefaultClause]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(DefaultClause *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.DefaultClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(DefaultClause *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13DefaultClauseE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13DefaultClauseE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.LabelledStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.LabelledStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(LabelledStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.LabelledStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(LabelledStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17LabelledStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17LabelledStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ThrowStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.ThrowStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ThrowStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ThrowStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ThrowStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14ThrowStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14ThrowStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TryStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.TryStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(TryStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TryStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(TryStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12TryStatementE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12TryStatementE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Catch'])
  def visit(self, a0: Optional[QQmlJS.AST.Catch]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(Catch *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Catch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(Catch *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_5CatchE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_5CatchE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Finally'])
  def visit(self, a0: Optional[QQmlJS.AST.Finally]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(Finally *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Finally]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(Finally *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_7FinallyE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_7FinallyE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FunctionDeclaration'])
  def visit(self, a0: Optional[QQmlJS.AST.FunctionDeclaration]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(FunctionDeclaration *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FunctionDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(FunctionDeclaration *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19FunctionDeclarationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19FunctionDeclaratio'
          'nE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FunctionExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.FunctionExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(FunctionExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(FunctionExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_18FunctionExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_18FunctionExpression'
          'E')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FormalParameterList'])
  def visit(self, a0: Optional[QQmlJS.AST.FormalParameterList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(FormalParameterList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FormalParameterList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(FormalParameterList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19FormalParameterListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19FormalParameterLis'
          'tE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ClassExpression'])
  def visit(self, a0: Optional[QQmlJS.AST.ClassExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ClassExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ClassExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ClassExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ClassExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ClassExpressionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ClassDeclaration'])
  def visit(self, a0: Optional[QQmlJS.AST.ClassDeclaration]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ClassDeclaration *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ClassDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ClassDeclaration *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ClassDeclarationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ClassDeclarationE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ClassElementList'])
  def visit(self, a0: Optional[QQmlJS.AST.ClassElementList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ClassElementList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ClassElementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ClassElementList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ClassElementListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ClassElementListE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Program'])
  def visit(self, a0: Optional[QQmlJS.AST.Program]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(Program *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Program]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(Program *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_7ProgramE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_7ProgramE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NameSpaceImport'])
  def visit(self, a0: Optional[QQmlJS.AST.NameSpaceImport]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(NameSpaceImport *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NameSpaceImport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(NameSpaceImport *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15NameSpaceImportE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15NameSpaceImportE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ImportSpecifier'])
  def visit(self, a0: Optional[QQmlJS.AST.ImportSpecifier]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ImportSpecifier *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ImportSpecifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ImportSpecifier *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ImportSpecifierE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ImportSpecifierE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ImportsList'])
  def visit(self, a0: Optional[QQmlJS.AST.ImportsList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ImportsList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ImportsList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ImportsList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_11ImportsListE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_11ImportsListE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NamedImports'])
  def visit(self, a0: Optional[QQmlJS.AST.NamedImports]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(NamedImports *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NamedImports]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(NamedImports *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12NamedImportsE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12NamedImportsE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FromClause'])
  def visit(self, a0: Optional[QQmlJS.AST.FromClause]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(FromClause *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FromClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(FromClause *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_10FromClauseE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_10FromClauseE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ImportClause'])
  def visit(self, a0: Optional[QQmlJS.AST.ImportClause]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ImportClause *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ImportClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ImportClause *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ImportClauseE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ImportClauseE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ImportDeclaration'])
  def visit(self, a0: Optional[QQmlJS.AST.ImportDeclaration]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ImportDeclaration *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ImportDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ImportDeclaration *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ImportDeclarationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ImportDeclarationE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExportSpecifier'])
  def visit(self, a0: Optional[QQmlJS.AST.ExportSpecifier]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ExportSpecifier *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ExportSpecifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ExportSpecifier *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ExportSpecifierE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ExportSpecifierE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExportsList'])
  def visit(self, a0: Optional[QQmlJS.AST.ExportsList]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ExportsList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ExportsList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ExportsList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_11ExportsListE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_11ExportsListE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExportClause'])
  def visit(self, a0: Optional[QQmlJS.AST.ExportClause]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ExportClause *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ExportClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ExportClause *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ExportClauseE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ExportClauseE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExportDeclaration'])
  def visit(self, a0: Optional[QQmlJS.AST.ExportDeclaration]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ExportDeclaration *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ExportDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ExportDeclaration *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ExportDeclarationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ExportDeclarationE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ESModule'])
  def visit(self, a0: Optional[QQmlJS.AST.ESModule]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(ESModule *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ESModule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(ESModule *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_8ESModuleE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_8ESModuleE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.DebuggerStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.DebuggerStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(DebuggerStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.DebuggerStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(DebuggerStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17DebuggerStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17DebuggerStatementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Type'])
  def visit(self, a0: Optional[QQmlJS.AST.Type]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(Type *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Type]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(Type *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_4TypeE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_4TypeE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TypeAnnotation'])
  def visit(self, a0: Optional[QQmlJS.AST.TypeAnnotation]) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::Visitor::visit(TypeAnnotation *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TypeAnnotation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::Visitor::visit(TypeAnnotation *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TypeAnnotationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TypeAnnotationE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiProgram'])
  @overload(NoneType)
  def endVisit(self, a0: Optional[QQmlJS.AST.UiProgram]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiProgram *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiProgram *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_9UiProgramE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_9UiProgramE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiHeaderItemList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiHeaderItemList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiHeaderItemList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiHeaderItemList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiHeaderItemList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiHeaderItemListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiHeaderItemLis'
          'tE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiPragmaValueList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiPragmaValueList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiPragmaValueList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiPragmaValueList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiPragmaValueList *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiPragmaValueListE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiPragmaValueLi'
          'stE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiPragma'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiPragma]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiPragma *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiPragma]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiPragma *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8UiPragmaE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8UiPragmaE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiImport'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiImport]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiImport *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiImport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiImport *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8UiImportE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8UiImportE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiPublicMember'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiPublicMember]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiPublicMember *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiPublicMember]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiPublicMember *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14UiPublicMemberE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14UiPublicMemberE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiSourceElement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiSourceElement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiSourceElement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiSourceElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiSourceElement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiSourceElementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiSourceElement'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiObjectDefinition'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiObjectDefinition]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiObjectDefinition *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiObjectDefinition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiObjectDefinition *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiObjectDefinitionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiObjectDefinit'
          'ionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiObjectInitializer'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiObjectInitializer]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiObjectInitializer
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiObjectInitializer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiObjectInitializer *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19UiObjectInitializerE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19UiObjectInitial'
          'izerE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiObjectBinding'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiObjectBinding]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiObjectBinding *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiObjectBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiObjectBinding *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiObjectBindingE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiObjectBinding'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiScriptBinding]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiScriptBinding *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiScriptBinding *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiScriptBindingE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiScriptBinding'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiArrayBinding'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiArrayBinding]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiArrayBinding *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiArrayBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiArrayBinding *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14UiArrayBindingE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14UiArrayBindingE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiParameterList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiParameterList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiParameterList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiParameterList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiParameterList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiParameterListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiParameterList'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiObjectMemberList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiObjectMemberList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiObjectMemberList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiObjectMemberList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiObjectMemberList *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiObjectMemberListE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiObjectMemberL'
          'istE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiArrayMemberList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiArrayMemberList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiArrayMemberList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiArrayMemberList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiArrayMemberList *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiArrayMemberListE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiArrayMemberLi'
          'stE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiQualifiedId'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiQualifiedId]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiQualifiedId *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiQualifiedId]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiQualifiedId *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13UiQualifiedIdE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13UiQualifiedIdE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiEnumDeclaration'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiEnumDeclaration]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiEnumDeclaration *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiEnumDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiEnumDeclaration *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiEnumDeclarationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiEnumDeclarati'
          'onE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiEnumMemberList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiEnumMemberList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiEnumMemberList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiEnumMemberList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiEnumMemberList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiEnumMemberListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiEnumMemberLis'
          'tE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiVersionSpecifier'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiVersionSpecifier]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiVersionSpecifier *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiVersionSpecifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiVersionSpecifier *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiVersionSpecifierE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiVersionSpecif'
          'ierE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiInlineComponent'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiInlineComponent]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiInlineComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiInlineComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiInlineComponent *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiInlineComponentE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiInlineCompone'
          'ntE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiAnnotation'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiAnnotation]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiAnnotation *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiAnnotation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiAnnotation *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12UiAnnotationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12UiAnnotationE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiAnnotationList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiAnnotationList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiAnnotationList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiAnnotationList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiAnnotationList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiAnnotationListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiAnnotationLis'
          'tE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiRequired'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiRequired]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UiRequired *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiRequired]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UiRequired *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10UiRequiredE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10UiRequiredE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TypeExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.TypeExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(TypeExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TypeExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(TypeExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TypeExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TypeExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ThisExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ThisExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ThisExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ThisExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ThisExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14ThisExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14ThisExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.IdentifierExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.IdentifierExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(IdentifierExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.IdentifierExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(IdentifierExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20IdentifierExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20IdentifierExpre'
          'ssionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NullExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.NullExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(NullExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NullExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(NullExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14NullExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14NullExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TrueLiteral'])
  def endVisit(self, a0: Optional[QQmlJS.AST.TrueLiteral]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(TrueLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TrueLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(TrueLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11TrueLiteralE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11TrueLiteralE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FalseLiteral'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FalseLiteral]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(FalseLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FalseLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(FalseLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12FalseLiteralE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12FalseLiteralE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.SuperLiteral'])
  def endVisit(self, a0: Optional[QQmlJS.AST.SuperLiteral]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(SuperLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.SuperLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(SuperLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12SuperLiteralE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12SuperLiteralE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.StringLiteral'])
  def endVisit(self, a0: Optional[QQmlJS.AST.StringLiteral]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(StringLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.StringLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(StringLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13StringLiteralE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13StringLiteralE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TemplateLiteral'])
  def endVisit(self, a0: Optional[QQmlJS.AST.TemplateLiteral]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(TemplateLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TemplateLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(TemplateLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15TemplateLiteralE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15TemplateLiteral'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NumericLiteral'])
  def endVisit(self, a0: Optional[QQmlJS.AST.NumericLiteral]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(NumericLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NumericLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(NumericLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14NumericLiteralE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14NumericLiteralE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.RegExpLiteral'])
  def endVisit(self, a0: Optional[QQmlJS.AST.RegExpLiteral]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(RegExpLiteral *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.RegExpLiteral]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(RegExpLiteral *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13RegExpLiteralE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13RegExpLiteralE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ArrayPattern'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ArrayPattern]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ArrayPattern *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ArrayPattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ArrayPattern *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ArrayPatternE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ArrayPatternE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ObjectPattern'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ObjectPattern]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ObjectPattern *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ObjectPattern]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ObjectPattern *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13ObjectPatternE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13ObjectPatternE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PatternElementList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.PatternElementList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(PatternElementList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PatternElementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(PatternElementList *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18PatternElementListE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18PatternElementL'
          'istE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PatternPropertyList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.PatternPropertyList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(PatternPropertyList
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PatternPropertyList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(PatternPropertyList *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19PatternPropertyListE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19PatternProperty'
          'ListE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PatternElement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.PatternElement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(PatternElement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PatternElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(PatternElement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14PatternElementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14PatternElementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PatternProperty'])
  def endVisit(self, a0: Optional[QQmlJS.AST.PatternProperty]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(PatternProperty *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PatternProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(PatternProperty *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15PatternPropertyE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15PatternProperty'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Elision'])
  def endVisit(self, a0: Optional[QQmlJS.AST.Elision]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(Elision *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Elision]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(Elision *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7ElisionE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7ElisionE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NestedExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.NestedExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(NestedExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NestedExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(NestedExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16NestedExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16NestedExpressio'
          'nE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.IdentifierPropertyName'])
  def endVisit(
      self,
      a0: Optional[QQmlJS.AST.IdentifierPropertyName],
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(IdentifierPropertyName
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.IdentifierPropertyName]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(IdentifierPropertyName *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22IdentifierPropertyNam'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22IdentifierPrope'
          'rtyNameE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.StringLiteralPropertyName'])
  def endVisit(
      self,
      a0: Optional[QQmlJS.AST.StringLiteralPropertyName],
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(StringLiteralPropertyName
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.StringLiteralPropertyName]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(StringLiteralPropertyName *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_25StringLiteralProperty'
        'NameE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_25StringLiteralPr'
          'opertyNameE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NumericLiteralPropertyName'])
  def endVisit(
      self,
      a0: Optional[QQmlJS.AST.NumericLiteralPropertyName],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJS::AST::Visitor::endVisit(NumericLiteralPropertyName *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NumericLiteralPropertyName]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(NumericLiteralPropertyName *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_26NumericLiteralPropert'
        'yNameE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_26NumericLiteralP'
          'ropertyNameE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ComputedPropertyName'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ComputedPropertyName]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ComputedPropertyName
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ComputedPropertyName]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ComputedPropertyName *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20ComputedPropertyNameE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20ComputedPropert'
          'yNameE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ArrayMemberExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ArrayMemberExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ArrayMemberExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ArrayMemberExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ArrayMemberExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21ArrayMemberExpression'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21ArrayMemberExpr'
          'essionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FieldMemberExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FieldMemberExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(FieldMemberExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FieldMemberExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(FieldMemberExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21FieldMemberExpression'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21FieldMemberExpr'
          'essionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TaggedTemplate'])
  def endVisit(self, a0: Optional[QQmlJS.AST.TaggedTemplate]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(TaggedTemplate *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TaggedTemplate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(TaggedTemplate *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TaggedTemplateE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TaggedTemplateE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NewMemberExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.NewMemberExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(NewMemberExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NewMemberExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(NewMemberExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19NewMemberExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19NewMemberExpres'
          'sionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NewExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.NewExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(NewExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NewExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(NewExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13NewExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13NewExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.CallExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.CallExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(CallExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.CallExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(CallExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14CallExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14CallExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ArgumentList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ArgumentList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ArgumentList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ArgumentList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ArgumentList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ArgumentListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ArgumentListE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PostIncrementExpression'])
  def endVisit(
      self,
      a0: Optional[QQmlJS.AST.PostIncrementExpression],
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(PostIncrementExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PostIncrementExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(PostIncrementExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23PostIncrementExpressi'
        'onE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23PostIncrementEx'
          'pressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PostDecrementExpression'])
  def endVisit(
      self,
      a0: Optional[QQmlJS.AST.PostDecrementExpression],
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(PostDecrementExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PostDecrementExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(PostDecrementExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23PostDecrementExpressi'
        'onE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23PostDecrementEx'
          'pressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.DeleteExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.DeleteExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(DeleteExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.DeleteExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(DeleteExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16DeleteExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16DeleteExpressio'
          'nE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.VoidExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.VoidExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(VoidExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.VoidExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(VoidExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14VoidExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14VoidExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TypeOfExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.TypeOfExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(TypeOfExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TypeOfExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(TypeOfExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16TypeOfExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16TypeOfExpressio'
          'nE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PreIncrementExpression'])
  def endVisit(
      self,
      a0: Optional[QQmlJS.AST.PreIncrementExpression],
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(PreIncrementExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PreIncrementExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(PreIncrementExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22PreIncrementExpressio'
        'nE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22PreIncrementExp'
          'ressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.PreDecrementExpression'])
  def endVisit(
      self,
      a0: Optional[QQmlJS.AST.PreDecrementExpression],
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(PreDecrementExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PreDecrementExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(PreDecrementExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22PreDecrementExpressio'
        'nE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22PreDecrementExp'
          'ressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UnaryPlusExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UnaryPlusExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UnaryPlusExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UnaryPlusExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UnaryPlusExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19UnaryPlusExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19UnaryPlusExpres'
          'sionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UnaryMinusExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UnaryMinusExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(UnaryMinusExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UnaryMinusExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(UnaryMinusExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20UnaryMinusExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20UnaryMinusExpre'
          'ssionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TildeExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.TildeExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(TildeExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TildeExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(TildeExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15TildeExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15TildeExpression'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NotExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.NotExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(NotExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NotExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(NotExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13NotExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13NotExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.BinaryExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.BinaryExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(BinaryExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.BinaryExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(BinaryExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16BinaryExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16BinaryExpressio'
          'nE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ConditionalExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ConditionalExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ConditionalExpression
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ConditionalExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ConditionalExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21ConditionalExpression'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21ConditionalExpr'
          'essionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.CommaExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.CommaExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(CommaExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.CommaExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(CommaExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15CommaExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15CommaExpression'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Block'])
  def endVisit(self, a0: Optional[QQmlJS.AST.Block]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(Block *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Block]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(Block *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_5BlockE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_5BlockE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.StatementList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.StatementList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(StatementList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.StatementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(StatementList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13StatementListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13StatementListE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.VariableStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.VariableStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(VariableStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.VariableStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(VariableStatement *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17VariableStatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17VariableStateme'
          'ntE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.VariableDeclarationList'])
  def endVisit(
      self,
      a0: Optional[QQmlJS.AST.VariableDeclarationList],
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(VariableDeclarationList
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.VariableDeclarationList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(VariableDeclarationList *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23VariableDeclarationLi'
        'stE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23VariableDeclara'
          'tionListE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.EmptyStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.EmptyStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(EmptyStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.EmptyStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(EmptyStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14EmptyStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14EmptyStatementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExpressionStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ExpressionStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ExpressionStatement
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ExpressionStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ExpressionStatement *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19ExpressionStatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19ExpressionState'
          'mentE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.IfStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.IfStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(IfStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.IfStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(IfStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11IfStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11IfStatementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.DoWhileStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.DoWhileStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(DoWhileStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.DoWhileStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(DoWhileStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16DoWhileStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16DoWhileStatemen'
          'tE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.WhileStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.WhileStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(WhileStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.WhileStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(WhileStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14WhileStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14WhileStatementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ForStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ForStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ForStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ForStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ForStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ForStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ForStatementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ForEachStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ForEachStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ForEachStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ForEachStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ForEachStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ForEachStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ForEachStatemen'
          'tE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ContinueStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ContinueStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ContinueStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ContinueStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ContinueStatement *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ContinueStatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ContinueStateme'
          'ntE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.BreakStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.BreakStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(BreakStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.BreakStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(BreakStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14BreakStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14BreakStatementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ReturnStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ReturnStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ReturnStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ReturnStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ReturnStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ReturnStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ReturnStatement'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.YieldExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.YieldExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(YieldExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.YieldExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(YieldExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15YieldExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15YieldExpression'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.WithStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.WithStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(WithStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.WithStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(WithStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13WithStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13WithStatementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.SwitchStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.SwitchStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(SwitchStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.SwitchStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(SwitchStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15SwitchStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15SwitchStatement'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.CaseBlock'])
  def endVisit(self, a0: Optional[QQmlJS.AST.CaseBlock]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(CaseBlock *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.CaseBlock]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(CaseBlock *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_9CaseBlockE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_9CaseBlockE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.CaseClauses'])
  def endVisit(self, a0: Optional[QQmlJS.AST.CaseClauses]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(CaseClauses *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.CaseClauses]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(CaseClauses *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11CaseClausesE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11CaseClausesE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.CaseClause'])
  def endVisit(self, a0: Optional[QQmlJS.AST.CaseClause]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(CaseClause *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.CaseClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(CaseClause *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10CaseClauseE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10CaseClauseE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.DefaultClause'])
  def endVisit(self, a0: Optional[QQmlJS.AST.DefaultClause]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(DefaultClause *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.DefaultClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(DefaultClause *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13DefaultClauseE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13DefaultClauseE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.LabelledStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.LabelledStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(LabelledStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.LabelledStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(LabelledStatement *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17LabelledStatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17LabelledStateme'
          'ntE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ThrowStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ThrowStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ThrowStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ThrowStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ThrowStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14ThrowStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14ThrowStatementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TryStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.TryStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(TryStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TryStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(TryStatement *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12TryStatementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12TryStatementE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Catch'])
  def endVisit(self, a0: Optional[QQmlJS.AST.Catch]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(Catch *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Catch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(Catch *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_5CatchE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_5CatchE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Finally'])
  def endVisit(self, a0: Optional[QQmlJS.AST.Finally]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(Finally *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Finally]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(Finally *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7FinallyE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7FinallyE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FunctionDeclaration'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FunctionDeclaration]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(FunctionDeclaration
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FunctionDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(FunctionDeclaration *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19FunctionDeclarationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19FunctionDeclara'
          'tionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FunctionExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FunctionExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(FunctionExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(FunctionExpression *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18FunctionExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18FunctionExpress'
          'ionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FormalParameterList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FormalParameterList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(FormalParameterList
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FormalParameterList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(FormalParameterList *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19FormalParameterListE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19FormalParameter'
          'ListE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ClassExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ClassExpression]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ClassExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ClassExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ClassExpression *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ClassExpressionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ClassExpression'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ClassDeclaration'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ClassDeclaration]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ClassDeclaration *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ClassDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ClassDeclaration *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ClassDeclarationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ClassDeclaratio'
          'nE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ClassElementList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ClassElementList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ClassElementList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ClassElementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ClassElementList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ClassElementListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ClassElementLis'
          'tE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Program'])
  def endVisit(self, a0: Optional[QQmlJS.AST.Program]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(Program *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Program]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(Program *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7ProgramE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7ProgramE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NameSpaceImport'])
  def endVisit(self, a0: Optional[QQmlJS.AST.NameSpaceImport]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(NameSpaceImport *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NameSpaceImport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(NameSpaceImport *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15NameSpaceImportE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15NameSpaceImport'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ImportSpecifier'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ImportSpecifier]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ImportSpecifier *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ImportSpecifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ImportSpecifier *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ImportSpecifierE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ImportSpecifier'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ImportsList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ImportsList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ImportsList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ImportsList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ImportsList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11ImportsListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11ImportsListE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.NamedImports'])
  def endVisit(self, a0: Optional[QQmlJS.AST.NamedImports]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(NamedImports *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.NamedImports]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(NamedImports *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12NamedImportsE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12NamedImportsE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FromClause'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FromClause]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(FromClause *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FromClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(FromClause *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10FromClauseE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10FromClauseE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ImportClause'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ImportClause]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ImportClause *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ImportClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ImportClause *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ImportClauseE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ImportClauseE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ImportDeclaration'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ImportDeclaration]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ImportDeclaration *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ImportDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ImportDeclaration *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ImportDeclarationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ImportDeclarati'
          'onE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExportSpecifier'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ExportSpecifier]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ExportSpecifier *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ExportSpecifier]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ExportSpecifier *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ExportSpecifierE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ExportSpecifier'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExportsList'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ExportsList]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ExportsList *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ExportsList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ExportsList *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11ExportsListE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11ExportsListE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExportClause'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ExportClause]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ExportClause *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ExportClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ExportClause *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ExportClauseE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ExportClauseE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExportDeclaration'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ExportDeclaration]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ExportDeclaration *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ExportDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ExportDeclaration *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ExportDeclarationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ExportDeclarati'
          'onE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ESModule'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ESModule]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(ESModule *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ESModule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(ESModule *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8ESModuleE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8ESModuleE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.DebuggerStatement'])
  def endVisit(self, a0: Optional[QQmlJS.AST.DebuggerStatement]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(DebuggerStatement *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.DebuggerStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(DebuggerStatement *a0)
    ritual = (
        'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17DebuggerStatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17DebuggerStateme'
          'ntE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.Type'])
  def endVisit(self, a0: Optional[QQmlJS.AST.Type]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(Type *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.Type]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(Type *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_4TypeE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_4TypeE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.TypeAnnotation'])
  def endVisit(self, a0: Optional[QQmlJS.AST.TypeAnnotation]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::Visitor::endVisit(TypeAnnotation *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-visitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.TypeAnnotation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::Visitor::endVisit(TypeAnnotation *a0)
    ritual = 'ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TypeAnnotationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TypeAnnotationE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @staticmethod
  def postVisit(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::Visitor::postVisit(Node *a0)': names
    'QQmlJS::AST::Node', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.Visitor.postVisit' has no cute function yet. Qt's "
        "'void QQmlJS::AST::Visitor::postVisit(Node *a0)': names "
        "'QQmlJS::AST::Node', which has no cute class yet.")

  @staticmethod
  def preVisit(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJS::AST::Visitor::preVisit(Node *a0)': names
    'QQmlJS::AST::Node', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.Visitor.preVisit' has no cute function yet. Qt's 'bool "
        "QQmlJS::AST::Visitor::preVisit(Node *a0)': names "
        "'QQmlJS::AST::Node', which has no cute class yet.")
