"""
QV4::Compiler::CodegenWarningInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4codegen_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Compiler::CodegenWarningInterface to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class CodegenWarningInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Compiler::CodegenWarningInterface: a plain
  Python object standing in front of one C++
  QV4::Compiler::CodegenWarningInterface.

  C++ hands a QV4::Compiler::CodegenWarningInterface around as a copy, so
  every C++ QV4::Compiler::CodegenWarningInterface behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::Compiler::CodegenWarningInterface that has a
  ritual and that Python can call so far, 3 names in all:
  'reportVarUsedBeforeDeclaration', 'reportFunctionUsedBeforeDeclaration',
  'unreachableVisitor'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QV4::Compiler::CodegenWarningInterface::~CodegenWarningInterface()': the
    destructor: Python removes its C++ QV4::Compiler::CodegenWarningInterface
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::Compiler::CodegenWarningInterface is created at the first
    use, not by 'QV4::Compiler::CodegenWarningInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Compiler::CodegenWarningInterface back gives a
    copy the ritual made for Python, in a new cute
    QV4::Compiler::CodegenWarningInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Compiler::CodegenWarningInterface'

  #  A C++ QV4::Compiler::CodegenWarningInterface Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QV4_Compiler_CodegenWarningInterface'

  #  The functions Qt calls itself that
  #  QV4::Compiler::CodegenWarningInterface is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'reportVarUsedBeforeDeclaration': (
          ('_ZN3QV48Compiler23CodegenWarningInterface30reportVarUsedBeforeD'
           'eclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'value', 'QtQml:QQmlJS.SourceLocation'),
               ('address', 'value', 'QtQml:QQmlJS.SourceLocation'),
           )),
      ),
      'reportFunctionUsedBeforeDeclaration': (
          ('_ZN3QV48Compiler23CodegenWarningInterface35reportFunctionUsedBe'
           'foreDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'value', 'QtQml:QQmlJS.SourceLocation'),
               ('address', 'value', 'QtQml:QQmlJS.SourceLocation'),
           )),
      ),
      'unreachableVisitor': (
          ('_ZN3QV48Compiler23CodegenWarningInterface18unreachableVisitorEv',
           ('address', 'address', 'QtQml:QQmlJS.AST.Visitor'),
           ()),
      ),
  }

  #  Qt's '~QV4::Compiler::CodegenWarningInterface()'. Naming it makes this a
  #  value class: Python owns every C++
  #  QV4::Compiler::CodegenWarningInterface behind a cute one, and removes it
  #  by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV48Compiler23CodegenWarningInterfaceD1Ev'

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

  @overload(
      str, str, WAIT['QQmlJS.SourceLocation'], WAIT['QQmlJS.SourceLocation'],
  )
  def reportVarUsedBeforeDeclaration(
      self,
      name: str,
      fileName: str,
      declarationLocation: QQmlJS.SourceLocation,
      accessLocation: QQmlJS.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::CodegenWarningInterface::reportVarUsedBeforeDeclaration(
    const QString &name, const QString &fileName, QQmlJS::SourceLocation
    declarationLocation, QQmlJS::SourceLocation accessLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-codegenwarninginterface.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    declarationLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    accessLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QV4::Compiler::CodegenWarningInterface::
    #      reportVarUsedBeforeDeclaration(const QString &name, const QString
    #      &fileName, QQmlJS::SourceLocation declarationLocation,
    #      QQmlJS::SourceLocation accessLocation)
    ritual = (
        'ritual_ZN3QV48Compiler23CodegenWarningInterface30reportVarUsedBefo'
        'reDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler23CodegenWarningInterface30reportVarUs'
          'edBeforeDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_')
    self.uglySide.call(
        ritual,
        name, fileName, self._valueOf(declarationLocation),
        self._valueOf(accessLocation),
    )

  @overload(
      str, str, WAIT['QQmlJS.SourceLocation'], WAIT['QQmlJS.SourceLocation'],
  )
  def reportFunctionUsedBeforeDeclaration(
      self,
      name: str,
      fileName: str,
      declarationLocation: QQmlJS.SourceLocation,
      accessLocation: QQmlJS.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QV4::Compiler::CodegenWarningInterface::
    reportFunctionUsedBeforeDeclaration(const QString &name, const QString
    &fileName, QQmlJS::SourceLocation declarationLocation,
    QQmlJS::SourceLocation accessLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-codegenwarninginterface.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    declarationLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    accessLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QV4::Compiler::CodegenWarningInterface::
    #      reportFunctionUsedBeforeDeclaration(const QString &name, const
    #      QString &fileName, QQmlJS::SourceLocation declarationLocation,
    #      QQmlJS::SourceLocation accessLocation)
    ritual = (
        'ritual_ZN3QV48Compiler23CodegenWarningInterface35reportFunctionUse'
        'dBeforeDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES6_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler23CodegenWarningInterface35reportFunct'
          'ionUsedBeforeDeclarationERK7QStringS4_N6QQmlJS14SourceLocationES'
          '6_')
    self.uglySide.call(
        ritual,
        name, fileName, self._valueOf(declarationLocation),
        self._valueOf(accessLocation),
    )

  def unreachableVisitor(self) -> Optional[QQmlJS.AST.Visitor]:
    """
    Calls Qt's 'QQmlJS::AST::Visitor
    *QV4::Compiler::CodegenWarningInterface::unreachableVisitor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-codegenwarninginterface.html

    Returns
    -------

    Optional[QQmlJS.AST.Visitor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJS::AST::Visitor
    #      *QV4::Compiler::CodegenWarningInterface::unreachableVisitor()
    ritual = (
        'ritual_ZN3QV48Compiler23CodegenWarningInterface18unreachableVisito'
        'rEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3QV48Compiler23CodegenWarningInterface18unreachable'
          'VisitorEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.AST.Visitor._cuteAt(address)
