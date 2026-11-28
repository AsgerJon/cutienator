"""
QV4::Script binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4script_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Script to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Script(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Script: a plain Python object standing in front
  of one C++ QV4::Script.

  What exists
  -----------

  Every function of Qt's QV4::Script that has a ritual and that Python can
  call so far, 6 names in all: 'setStrictMode', 'setInheritContext',
  'setParseAsBinding', 'parse', 'run', 'function'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    QV4::Script::precompile(QV4::Compiler::Module *module, QQmlJS::Engine
    *jsEngine, Compiler::JSUnitGenerator *unitGenerator, const QString
    &fileName, const QString &source, QList<QQmlError> *reportedErrors,
    QV4::Compiler::ContextType contextType, InheritContext inheritContext)':
    names 'QList<QQmlError>', which has no cute class yet.
  - Qt's 'QV4::Script::Script(ExecutionEngine *engine, QmlContext *qml, const
    QQmlRefPointer<ExecutableCompilationUnit> &compilationUnit)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QV4::Script::~Script()': the destructor: Python never removes a C++
    QV4::Script.
  - Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::Script::compilationUnit() const': gives a type Python has no way to
    take yet.

  What to expect
  --------------

  - The C++ QV4::Script is created at the first use, not by
    'QV4::Script(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Script.
  - Each name of Qt's QV4::Script that has no cute function yet,
    'compilationUnit', 'precompile', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::Script, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class InheritContext(CuteNum, scoped=True):
    """
    The enum 'QV4::Script::InheritContext' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Script'

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

  @overload()
  @overload(bool)
  def setStrictMode(self, strictMode: bool = True) -> None:
    """
    Calls Qt's 'void QV4::Script::setStrictMode(bool strictMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-script.html#setStrictMode

    Parameters
    ----------

    strictMode : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QV4::Script::setStrictMode(bool strictMode)
    self.uglySide.call('ritual_ZN3QV46Script13setStrictModeEb', strictMode)

  @overload()
  @overload(bool)
  def setInheritContext(self, inheritContext: bool = True) -> None:
    """
    Calls Qt's 'void QV4::Script::setInheritContext(bool inheritContext)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-script.html#setInheritContext

    Parameters
    ----------

    inheritContext : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QV4::Script::setInheritContext(bool inheritContext)
    self.uglySide.call(
        'ritual_ZN3QV46Script17setInheritContextEb', inheritContext,
    )

  @overload()
  @overload(bool)
  def setParseAsBinding(self, parseAsBinding: bool = True) -> None:
    """
    Calls Qt's 'void QV4::Script::setParseAsBinding(bool parseAsBinding)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-script.html#setParseAsBinding

    Parameters
    ----------

    parseAsBinding : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QV4::Script::setParseAsBinding(bool parseAsBinding)
    self.uglySide.call(
        'ritual_ZN3QV46Script17setParseAsBindingEb', parseAsBinding,
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

  @overload(WAIT['QV4.ExecutionContext'], QV4.Compiler.ContextType, str)
  @overload(NoneType, QV4.Compiler.ContextType, str)
  @overload(WAIT['QV4.ExecutionContext'], QV4.Compiler.ContextType, str, str)
  @overload(NoneType, QV4.Compiler.ContextType, str, str)
  @overload(
      WAIT['QV4.ExecutionContext'], QV4.Compiler.ContextType, str, str, int,
  )
  @overload(NoneType, QV4.Compiler.ContextType, str, str, int)
  def __init__(
      self,
      scope: Optional[QV4.ExecutionContext],
      mode: QV4.Compiler.ContextType,
      sourceCode: str,
      source: str = '',
      line: int = 1,
  ) -> None:
    """
    Notes what was given, for Qt's 'QV4::Script::Script(ExecutionContext
    *scope, QV4::Compiler::ContextType mode, const QString &sourceCode, const
    QString &source, int line)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-script.html#Script

    Parameters
    ----------

    scope : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : QV4.Compiler.ContextType
      Passed on as its number.

    sourceCode : str
      Passed on as it is: a QString is made of it for the call.

    source : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    line : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  QV4::Script::Script(ExecutionContext *scope,
    #      QV4::Compiler::ContextType mode, const QString &sourceCode, const
    #      QString &source, int line)
    self._noteCreation(Script, lambda: Rituals.call(
        'ritual_ZN3QV46ScriptC1EPNS_16ExecutionContextENS_8Compiler11Contex'
        'tTypeERK7QStringS7_i',
        self._addressOf(scope), mode.value, sourceCode, source, line,
    ))

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], bool, str)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, bool, str)
  @overload(NoneType, WAIT['QV4.QmlContext'], bool, str)
  @overload(NoneType, NoneType, bool, str)
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], bool, str, str,
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, bool, str, str)
  @overload(NoneType, WAIT['QV4.QmlContext'], bool, str, str)
  @overload(NoneType, NoneType, bool, str, str)
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.QmlContext'], bool, str, str,
      int,
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, bool, str, str, int)
  @overload(NoneType, WAIT['QV4.QmlContext'], bool, str, str, int)
  @overload(NoneType, NoneType, bool, str, str, int)
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      qml: Optional[QV4.QmlContext],
      parseAsBinding: bool,
      sourceCode: str,
      source: str = '',
      line: int = 1,
  ) -> None:
    """
    Notes what was given, for Qt's 'QV4::Script::Script(ExecutionEngine
    *engine, QmlContext *qml, bool parseAsBinding, const QString &sourceCode,
    const QString &source, int line)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-script.html#Script

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    qml : Optional[QV4.QmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parseAsBinding : bool
      Passed on as it is.

    sourceCode : str
      Passed on as it is: a QString is made of it for the call.

    source : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    line : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  QV4::Script::Script(ExecutionEngine *engine, QmlContext *qml, bool
    #      parseAsBinding, const QString &sourceCode, const QString &source,
    #      int line)
    self._noteCreation(Script, lambda: Rituals.call(
        'ritual_ZN3QV46ScriptC1EPNS_15ExecutionEngineEPNS_10QmlContextEbRK7'
        'QStringS7_i',
        self._addressOf(engine), self._addressOf(qml), parseAsBinding,
        sourceCode, source, line,
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

  def parse(self) -> None:
    """
    Calls Qt's 'void QV4::Script::parse()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-script.html#parse
    """
    #  void QV4::Script::parse()
    self.uglySide.call('ritual_ZN3QV46Script5parseEv')

  @overload()
  @overload(WAIT['QV4.Value'])
  @overload(NoneType)
  def run(self, thisObject: Optional[QV4.Value] = None) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Script::run(const QV4::Value
    *thisObject)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-script.html#run

    Parameters
    ----------

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  ReturnedValue QV4::Script::run(const QV4::Value *thisObject)
    return self.uglySide.call(
        'ritual_ZN3QV46Script3runEPKNS_5ValueE', self._addressOf(thisObject),
    )

  def function(self) -> Optional[QV4.Function]:
    """
    Calls Qt's 'Function *QV4::Script::function()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-script.html#function

    Returns
    -------

    Optional[QV4.Function]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Function *QV4::Script::function()
    address = self.uglySide.call('ritual_ZN3QV46Script8functionEv')
    return QV4.Function._cuteAt(address)

  @staticmethod
  def compilationUnit(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<ExecutableCompilationUnit>
    QV4::Script::compilationUnit() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QV4.Script.compilationUnit' has no cute function yet. Qt's "
        "'QQmlRefPointer<ExecutableCompilationUnit> "
        "QV4::Script::compilationUnit() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def precompile(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    QV4::Script::precompile(QV4::Compiler::Module *module, QQmlJS::Engine
    *jsEngine, Compiler::JSUnitGenerator *unitGenerator, const QString
    &fileName, const QString &source, QList<QQmlError> *reportedErrors,
    QV4::Compiler::ContextType contextType, InheritContext inheritContext)':
    names 'QList<QQmlError>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Script.precompile' has no cute function yet. Qt's "
        "'QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "QV4::Script::precompile(QV4::Compiler::Module *module, "
        "QQmlJS::Engine *jsEngine, Compiler::JSUnitGenerator "
        "*unitGenerator, const QString &fileName, const QString &source, "
        "QList<QQmlError> *reportedErrors, QV4::Compiler::ContextType "
        "contextType, InheritContext inheritContext)': names "
        "'QList<QQmlError>', which has no cute class yet.")
