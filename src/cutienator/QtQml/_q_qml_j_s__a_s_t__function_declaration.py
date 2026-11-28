"""
QQmlJS::AST::FunctionDeclaration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::FunctionDeclaration to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FunctionDeclaration(QQmlJS.AST.FunctionExpression):
  """
  The cute side of Qt's QQmlJS::AST::FunctionDeclaration: a plain Python
  object standing in front of one C++ QQmlJS::AST::FunctionDeclaration.

  It is built on the cute 'QQmlJS::AST::FunctionExpression', as Qt's
  QQmlJS::AST::FunctionDeclaration is built on Qt's
  QQmlJS::AST::FunctionExpression, and has everything that class has.

  What exists
  -----------

  No function of Qt's QQmlJS::AST::FunctionDeclaration yet. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::FunctionDeclaration::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::FunctionDeclaration is created at the first use, not
    by 'QQmlJS::AST::FunctionDeclaration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::FunctionDeclaration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::AST::FunctionDeclaration'

  #  A C++ QQmlJS::AST::FunctionDeclaration Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_FunctionDeclaration'

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
    'QQmlJS::AST::FunctionDeclaration::FunctionDeclaration(QStringView n,
    FormalParameterList *f, StatementList *b, TypeAnnotation
    *typeAnnotation)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-functiondeclaration.html

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
    #  QQmlJS::AST::FunctionDeclaration::FunctionDeclaration(QStringView n,
    #      FormalParameterList *f, StatementList *b, TypeAnnotation
    #      *typeAnnotation)
    self._noteCreation(FunctionDeclaration, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST19FunctionDeclarationC1E11QStringViewPNS0_19Fo'
        'rmalParameterListEPNS0_13StatementListEPNS0_14TypeAnnotationE',
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
