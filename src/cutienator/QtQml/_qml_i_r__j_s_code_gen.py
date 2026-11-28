"""
QmlIR::JSCodeGen binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::JSCodeGen to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4, QmlIR

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class JSCodeGen(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QmlIR::JSCodeGen: a plain Python object standing in
  front of one C++ QmlIR::JSCodeGen.

  What exists
  -----------

  Every function of Qt's QmlIR::JSCodeGen that has a ritual and that Python
  can call so far, 1 name in all: 'generateRuntimeFunctions'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<int>
    QmlIR::JSCodeGen::generateJSCodeForFunctionsAndBindings(const
    QList<CompiledFunctionOrExpression> &functions)': takes a type Python has
    no way to hand over yet.

  What to expect
  --------------

  - The C++ QmlIR::JSCodeGen is created at the first use, not by
    'QmlIR::JSCodeGen(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlIR::JSCodeGen.
  - Each name of Qt's QmlIR::JSCodeGen that has no cute function yet,
    'generateJSCodeForFunctionsAndBindings', holds a function that raises
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
  __qt_class__ = 'QmlIR::JSCodeGen'

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
      WAIT['QmlIR.Document'], WAIT['QV4.Compiler.CodegenWarningInterface'],
  )
  @overload(WAIT['QmlIR.Document'], NoneType)
  @overload(NoneType, WAIT['QV4.Compiler.CodegenWarningInterface'])
  @overload(NoneType, NoneType)
  @overload(
      WAIT['QmlIR.Document'], WAIT['QV4.Compiler.CodegenWarningInterface'],
      bool,
  )
  @overload(WAIT['QmlIR.Document'], NoneType, bool)
  @overload(NoneType, WAIT['QV4.Compiler.CodegenWarningInterface'], bool)
  @overload(NoneType, NoneType, bool)
  def __init__(
      self,
      document: Optional[QmlIR.Document],
      iface: Optional[QV4.Compiler.CodegenWarningInterface],
      storeSourceLocations: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's 'QmlIR::JSCodeGen::JSCodeGen(Document
    *document, QV4::Compiler::CodegenWarningInterface *iface, bool
    storeSourceLocations)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-jscodegen.html#JSCodeGen

    Parameters
    ----------

    document : Optional[QmlIR.Document]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iface : Optional[QV4.Compiler.CodegenWarningInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    storeSourceLocations : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QmlIR::JSCodeGen::JSCodeGen(Document *document,
    #      QV4::Compiler::CodegenWarningInterface *iface, bool
    #      storeSourceLocations)
    self._noteCreation(JSCodeGen, lambda: Rituals.call(
        'ritual_ZN5QmlIR9JSCodeGenC1EPNS_8DocumentEPN3QV48Compiler23Codegen'
        'WarningInterfaceEb',
        self._addressOf(document), self._addressOf(iface),
        storeSourceLocations,
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

  @overload(WAIT['QmlIR.Object'])
  @overload(NoneType)
  def generateRuntimeFunctions(self, object: Optional[QmlIR.Object]) -> bool:
    """
    Calls Qt's 'bool QmlIR::JSCodeGen::generateRuntimeFunctions(QmlIR::Object
    *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-jscodegen.html#generateRuntimeFunctions

    Parameters
    ----------

    object : Optional[QmlIR.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::JSCodeGen::generateRuntimeFunctions(QmlIR::Object *object)
    return self.uglySide.call(
        'ritual_ZN5QmlIR9JSCodeGen24generateRuntimeFunctionsEPNS_6ObjectE',
        self._addressOf(object),
    )

  @staticmethod
  def generateJSCodeForFunctionsAndBindings(*__, **_) -> Never:
    """
    Qt's 'QList<int>
    QmlIR::JSCodeGen::generateJSCodeForFunctionsAndBindings(const
    QList<CompiledFunctionOrExpression> &functions)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QmlIR.JSCodeGen.generateJSCodeForFunctionsAndBindings' has no "
        "cute function yet. Qt's 'QList<int> "
        "QmlIR::JSCodeGen::generateJSCodeForFunctionsAndBindings(const "
        "QList<CompiledFunctionOrExpression> &functions)': takes a type "
        "Python has no way to hand over yet.")
