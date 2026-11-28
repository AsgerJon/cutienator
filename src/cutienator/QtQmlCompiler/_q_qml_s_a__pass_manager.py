"""
QQmlSA::PassManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlSA

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class PassManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::PassManager: a plain Python object standing
  in front of one C++ QQmlSA::PassManager.

  What exists
  -----------

  Every function of Qt's QQmlSA::PassManager that has a ritual and that
  Python can call so far, 4 names in all: 'd_func', 'analyze',
  'hasImportedModule', 'isCategoryEnabled'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const PassManagerPrivate *QQmlSA::PassManager::d_func() const':
    takes in Python what 'PassManagerPrivate *QQmlSA::PassManager::d_func()'
    takes.
  - Qt's 'bool
    QQmlSA::PassManager::registerPropertyPass(std::shared_ptr<PropertyPass>
    pass, QAnyStringView moduleName, QAnyStringView typeName, QAnyStringView
    propertyName, bool allowInheritance)': takes a type Python has no way to
    hand over yet.
  - Qt's 'std::unordered_map<quint32, Binding>
    QQmlSA::PassManager::bindingsByLocation() const': gives a type Python has
    no way to take yet.
  - Qt's 'QQmlSA::PassManager::~PassManager()': the destructor: Python never
    removes a C++ QQmlSA::PassManager.

  What has no ritual
  ------------------

  5 of the 14 functions Qt declares: 4 forbidden; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QQmlSA::PassManager is created at the first use, not by
    'QQmlSA::PassManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSA::PassManager.
  - Each name of Qt's QQmlSA::PassManager that has no cute function yet,
    'bindingsByLocation', 'registerElementPass', 'registerPropertyPass',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::PassManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def hasImportedModule(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlSA::PassManager::hasImportedModule(QAnyStringView
    name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanager.html#hasImportedModule

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlSA::PassManager::hasImportedModule(QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA11PassManager17hasImportedModuleE14QAnyStringView',
        name,
    )

  @overload(WAIT['QQmlSA.LoggerWarningId'])
  def isCategoryEnabled(self, category: QQmlSA.LoggerWarningId) -> bool:
    """
    Calls Qt's 'bool QQmlSA::PassManager::isCategoryEnabled(LoggerWarningId
    category) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanager.html#isCategoryEnabled

    Parameters
    ----------

    category : QQmlSA.LoggerWarningId
      Passed on as a value: Qt reads the C++ QQmlSA::LoggerWarningId, which
      stays Python's own.
    """
    #  bool QQmlSA::PassManager::isCategoryEnabled(LoggerWarningId category)
    #      const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA11PassManager17isCategoryEnabledENS_15LoggerWarni'
        'ngIdE',
        self._valueOf(category),
    )

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlSA::PassManager::PassManager()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-passmanager.html#PassManager
    """
    #  QQmlSA::PassManager::PassManager()
    self._noteCreation(PassManager, lambda: Rituals.call(
        'ritual_ZN6QQmlSA11PassManagerC1Ev',
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

  def d_func(self) -> Optional[QQmlSA.PassManagerPrivate]:
    """
    Calls Qt's 'PassManagerPrivate *QQmlSA::PassManager::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-passmanager.html#d_func

    Returns
    -------

    Optional[QQmlSA.PassManagerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PassManagerPrivate *QQmlSA::PassManager::d_func()
    address = self.uglySide.call('ritual_ZN6QQmlSA11PassManager6d_funcEv')
    return QQmlSA.PassManagerPrivate._cuteAt(address)

  @overload(WAIT['QQmlSA.Element'])
  def analyze(self, root: QQmlSA.Element) -> None:
    """
    Calls Qt's 'void QQmlSA::PassManager::analyze(const Element &root)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-passmanager.html#analyze

    Parameters
    ----------

    root : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.
    """
    #  void QQmlSA::PassManager::analyze(const Element &root)
    self.uglySide.call(
        'ritual_ZN6QQmlSA11PassManager7analyzeERKNS_7ElementE',
        self._valueOf(root),
    )

  @staticmethod
  def bindingsByLocation(*__, **_) -> Never:
    """
    Qt's 'std::unordered_map<quint32, Binding>
    QQmlSA::PassManager::bindingsByLocation() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PassManager.bindingsByLocation' has no cute function yet. "
        "Qt's 'std::unordered_map<quint32, Binding> "
        "QQmlSA::PassManager::bindingsByLocation() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def registerElementPass(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlSA::PassManager::registerElementPass(std::unique_ptr<ElementPass>
    pass)': the compiler refuses its ritual as it would be written here: call
    to deleted constructor of 'std::unique_ptr<ElementPass>'.
    """
    raise NotImplementedError(
        "'QQmlSA.PassManager.registerElementPass' has no cute function yet. "
        "Qt's 'void "
        "QQmlSA::PassManager::registerElementPass(std::unique_ptr<ElementPas"
        "s> pass)': the compiler refuses its ritual as it would be written "
        "here: call to deleted constructor of "
        "'std::unique_ptr<ElementPass>'.")

  @staticmethod
  def registerPropertyPass(*__, **_) -> Never:
    """
    Qt's 'bool
    QQmlSA::PassManager::registerPropertyPass(std::shared_ptr<PropertyPass>
    pass, QAnyStringView moduleName, QAnyStringView typeName, QAnyStringView
    propertyName, bool allowInheritance)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlSA.PassManager.registerPropertyPass' has no cute function "
        "yet. Qt's 'bool "
        "QQmlSA::PassManager::registerPropertyPass(std::shared_ptr<PropertyP"
        "ass> pass, QAnyStringView moduleName, QAnyStringView typeName, "
        "QAnyStringView propertyName, bool allowInheritance)': takes a type "
        "Python has no way to hand over yet.")
