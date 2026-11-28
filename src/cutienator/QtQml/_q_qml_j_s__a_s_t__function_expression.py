"""
QQmlJS::AST::FunctionExpression binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::FunctionExpression to be private: it declares the
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


class FunctionExpression(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::FunctionExpression: a plain Python
  object standing in front of one C++ QQmlJS::AST::FunctionExpression.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::FunctionExpression that has a ritual
  and that Python can call so far, 3 names in all: 'firstSourceLocation',
  'lastSourceLocation', 'asFunctionDefinition'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::FunctionExpression::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::FunctionExpression is created at the first use, not
    by 'QQmlJS::AST::FunctionExpression(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::FunctionExpression.
  - Each name of Qt's QQmlJS::AST::FunctionExpression that has no cute
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
  __qt_class__ = 'QQmlJS::AST::FunctionExpression'

  #  A C++ QQmlJS::AST::FunctionExpression Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_FunctionExpression'

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
    QQmlJS::AST::FunctionExpression::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-functionexpression.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::FunctionExpression::firstSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST18FunctionExpression19firstSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST18FunctionExpression19firstSourceLocati'
          'onEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::FunctionExpression::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-functionexpression.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::FunctionExpression::lastSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST18FunctionExpression18lastSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST18FunctionExpression18lastSourceLocatio'
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
      WAIT['QQmlJS.MemoryPool'], str, WAIT['QQmlJS.AST.FormalParameterList'],
      WAIT['QQmlJS.AST.StatementList'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], str, WAIT['QQmlJS.AST.FormalParameterList'],
      NoneType,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], str, NoneType,
      WAIT['QQmlJS.AST.StatementList'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], str, NoneType, NoneType)
  @overload(
      NoneType, str, WAIT['QQmlJS.AST.FormalParameterList'],
      WAIT['QQmlJS.AST.StatementList'],
  )
  @overload(NoneType, str, WAIT['QQmlJS.AST.FormalParameterList'], NoneType)
  @overload(NoneType, str, NoneType, WAIT['QQmlJS.AST.StatementList'])
  @overload(NoneType, str, NoneType, NoneType)
  @overload(
      WAIT['QQmlJS.MemoryPool'], str, WAIT['QQmlJS.AST.FormalParameterList'],
      WAIT['QQmlJS.AST.StatementList'], WAIT['QQmlJS.AST.TypeAnnotation'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], str, WAIT['QQmlJS.AST.FormalParameterList'],
      WAIT['QQmlJS.AST.StatementList'], NoneType,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], str, WAIT['QQmlJS.AST.FormalParameterList'],
      NoneType, WAIT['QQmlJS.AST.TypeAnnotation'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], str, WAIT['QQmlJS.AST.FormalParameterList'],
      NoneType, NoneType,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], str, NoneType,
      WAIT['QQmlJS.AST.StatementList'], WAIT['QQmlJS.AST.TypeAnnotation'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], str, NoneType,
      WAIT['QQmlJS.AST.StatementList'], NoneType,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], str, NoneType, NoneType,
      WAIT['QQmlJS.AST.TypeAnnotation'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], str, NoneType, NoneType, NoneType)
  @overload(
      NoneType, str, WAIT['QQmlJS.AST.FormalParameterList'],
      WAIT['QQmlJS.AST.StatementList'], WAIT['QQmlJS.AST.TypeAnnotation'],
  )
  @overload(
      NoneType, str, WAIT['QQmlJS.AST.FormalParameterList'],
      WAIT['QQmlJS.AST.StatementList'], NoneType,
  )
  @overload(
      NoneType, str, WAIT['QQmlJS.AST.FormalParameterList'], NoneType,
      WAIT['QQmlJS.AST.TypeAnnotation'],
  )
  @overload(
      NoneType, str, WAIT['QQmlJS.AST.FormalParameterList'], NoneType,
      NoneType,
  )
  @overload(
      NoneType, str, NoneType, WAIT['QQmlJS.AST.StatementList'],
      WAIT['QQmlJS.AST.TypeAnnotation'],
  )
  @overload(
      NoneType, str, NoneType, WAIT['QQmlJS.AST.StatementList'], NoneType,
  )
  @overload(
      NoneType, str, NoneType, NoneType, WAIT['QQmlJS.AST.TypeAnnotation'],
  )
  @overload(NoneType, str, NoneType, NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      n: str,
      f: Optional[QQmlJS.AST.FormalParameterList],
      b: Optional[QQmlJS.AST.StatementList],
      typeAnnotation: Optional[QQmlJS.AST.TypeAnnotation] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::FunctionExpression::FunctionExpression(QStringView n,
    FormalParameterList *f, StatementList *b, TypeAnnotation
    *typeAnnotation)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-functionexpression.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : str
      Passed on as it is: a QString is made of it for the call.

    f : Optional[QQmlJS.AST.FormalParameterList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    b : Optional[QQmlJS.AST.StatementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeAnnotation : Optional[QQmlJS.AST.TypeAnnotation]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlJS::AST::FunctionExpression::FunctionExpression(QStringView n,
    #      FormalParameterList *f, StatementList *b, TypeAnnotation
    #      *typeAnnotation)
    self._noteCreation(FunctionExpression, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST18FunctionExpressionC1E11QStringViewPNS0_19For'
        'malParameterListEPNS0_13StatementListEPNS0_14TypeAnnotationE',
        self._addressOf(pool), n, self._addressOf(f), self._addressOf(b),
        self._addressOf(typeAnnotation),
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

  def asFunctionDefinition(self) -> Optional[FunctionExpression]:
    """
    Calls Qt's 'FunctionExpression
    *QQmlJS::AST::FunctionExpression::asFunctionDefinition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-functionexpression.html

    Returns
    -------

    Optional[FunctionExpression]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionExpression
    #      *QQmlJS::AST::FunctionExpression::asFunctionDefinition()
    ritual = (
        'ritual_ZN6QQmlJS3AST18FunctionExpression20asFunctionDefinitionEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST18FunctionExpression20asFunctionDefiniti'
          'onEv')
    address = self.uglySide.call(ritual)
    return FunctionExpression._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::FunctionExpression::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.FunctionExpression.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::FunctionExpression::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
