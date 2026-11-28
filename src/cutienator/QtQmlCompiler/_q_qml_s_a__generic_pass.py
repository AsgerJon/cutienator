"""
QQmlSA::GenericPass binding of the Qt C++
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

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class GenericPass(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::GenericPass: a plain Python object standing
  in front of one C++ QQmlSA::GenericPass.

  What exists
  -----------

  Every function of Qt's QQmlSA::GenericPass that has a ritual and that
  Python can call so far, 10 names in all: 'emitWarning',
  'resolveTypeInFileScope', 'resolveAttachedInFileScope', 'resolveType',
  'resolveBuiltinType', 'resolveAttached', 'resolveLiteralType',
  'resolveIdToElement', 'resolveElementToId', 'sourceCode'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlSA::GenericPass::~GenericPass()': the destructor: Python never
    removes a C++ QQmlSA::GenericPass.

  What has no ritual
  ------------------

  6 of the 20 functions Qt declares: 4 forbidden; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QQmlSA::GenericPass is created at the first use, not by
    'QQmlSA::GenericPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlSA::GenericPass.
  - Each name of Qt's QQmlSA::GenericPass that has no cute function yet,
    'd_func', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::GenericPass'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def resolveBuiltinType(self, typeName: str) -> QQmlSA.Element:
    """
    Calls Qt's 'Element
    QQmlSA::GenericPass::resolveBuiltinType(QAnyStringView typeName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#resolveBuiltinType

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::GenericPass::resolveBuiltinType(QAnyStringView
    #      typeName) const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA11GenericPass18resolveBuiltinTypeE14QAnyStringVie'
        'w',
        typeName,
    )
    return QQmlSA.Element._cuteOwning(address)

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

  @overload(WAIT['QQmlSA.PassManager'])
  @overload(NoneType)
  def __init__(self, manager: Optional[QQmlSA.PassManager]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::GenericPass::GenericPass(PassManager *manager)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#GenericPass

    Parameters
    ----------

    manager : Optional[QQmlSA.PassManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlSA::GenericPass::GenericPass(PassManager *manager)
    self._noteCreation(GenericPass, lambda: Rituals.call(
        'ritual_ZN6QQmlSA11GenericPassC1EPNS_11PassManagerE',
        self._addressOf(manager),
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

  @overload(str, WAIT['QQmlSA.LoggerWarningId'])
  def emitWarning(self, diagnostic: str, id: QQmlSA.LoggerWarningId) -> None:
    """
    Calls Qt's 'void QQmlSA::GenericPass::emitWarning(QAnyStringView
    diagnostic, LoggerWarningId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#emitWarning

    Parameters
    ----------

    diagnostic : str
      Passed on as it is: a QString is made of it for the call.

    id : QQmlSA.LoggerWarningId
      Passed on as a value: Qt reads the C++ QQmlSA::LoggerWarningId, which
      stays Python's own.
    """
    #  void QQmlSA::GenericPass::emitWarning(QAnyStringView diagnostic,
    #      LoggerWarningId id)
    self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass11emitWarningE14QAnyStringViewNS_15Lo'
        'ggerWarningIdE',
        diagnostic, self._valueOf(id),
    )

  @overload(
      str, WAIT['QQmlSA.LoggerWarningId'], WAIT['QQmlSA.SourceLocation'],
  )
  def emitWarning(
      self,
      diagnostic: str,
      id: QQmlSA.LoggerWarningId,
      srcLocation: QQmlSA.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::GenericPass::emitWarning(QAnyStringView
    diagnostic, LoggerWarningId id, QQmlSA::SourceLocation srcLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#emitWarning

    Parameters
    ----------

    diagnostic : str
      Passed on as it is: a QString is made of it for the call.

    id : QQmlSA.LoggerWarningId
      Passed on as a value: Qt reads the C++ QQmlSA::LoggerWarningId, which
      stays Python's own.

    srcLocation : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlSA::GenericPass::emitWarning(QAnyStringView diagnostic,
    #      LoggerWarningId id, QQmlSA::SourceLocation srcLocation)
    self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass11emitWarningE14QAnyStringViewNS_15Lo'
        'ggerWarningIdENS_14SourceLocationE',
        diagnostic, self._valueOf(id), self._valueOf(srcLocation),
    )

  @overload(
      str, WAIT['QQmlSA.LoggerWarningId'], WAIT['QQmlSA.SourceLocation'],
      WAIT['QQmlSA.FixSuggestion'],
  )
  def emitWarning(
      self,
      diagnostic: str,
      id: QQmlSA.LoggerWarningId,
      srcLocation: QQmlSA.SourceLocation,
      fix: QQmlSA.FixSuggestion,
  ) -> None:
    """
    Calls Qt's 'void QQmlSA::GenericPass::emitWarning(QAnyStringView
    diagnostic, LoggerWarningId id, QQmlSA::SourceLocation srcLocation, const
    QQmlSA::FixSuggestion &fix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#emitWarning

    Parameters
    ----------

    diagnostic : str
      Passed on as it is: a QString is made of it for the call.

    id : QQmlSA.LoggerWarningId
      Passed on as a value: Qt reads the C++ QQmlSA::LoggerWarningId, which
      stays Python's own.

    srcLocation : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.

    fix : QQmlSA.FixSuggestion
      Passed on as a value: Qt reads the C++ QQmlSA::FixSuggestion, which
      stays Python's own.
    """
    #  void QQmlSA::GenericPass::emitWarning(QAnyStringView diagnostic,
    #      LoggerWarningId id, QQmlSA::SourceLocation srcLocation, const
    #      QQmlSA::FixSuggestion &fix)
    self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass11emitWarningE14QAnyStringViewNS_15Lo'
        'ggerWarningIdENS_14SourceLocationERKNS_13FixSuggestionE',
        diagnostic, self._valueOf(id), self._valueOf(srcLocation),
        self._valueOf(fix),
    )

  @overload(str)
  def resolveTypeInFileScope(self, typeName: str) -> QQmlSA.Element:
    """
    Calls Qt's 'Element
    QQmlSA::GenericPass::resolveTypeInFileScope(QAnyStringView typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#resolveTypeInFileScope

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::GenericPass::resolveTypeInFileScope(QAnyStringView
    #      typeName)
    address = self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass22resolveTypeInFileScopeE14QAnyString'
        'View',
        typeName,
    )
    return QQmlSA.Element._cuteOwning(address)

  @overload(str)
  def resolveAttachedInFileScope(self, typeName: str) -> QQmlSA.Element:
    """
    Calls Qt's 'Element
    QQmlSA::GenericPass::resolveAttachedInFileScope(QAnyStringView
    typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#resolveAttachedInFileScope

    Parameters
    ----------

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::GenericPass::resolveAttachedInFileScope(QAnyStringView
    #      typeName)
    address = self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass26resolveAttachedInFileScopeE14QAnySt'
        'ringView',
        typeName,
    )
    return QQmlSA.Element._cuteOwning(address)

  @overload(str, str)
  def resolveType(self, moduleName: str, typeName: str) -> QQmlSA.Element:
    """
    Calls Qt's 'Element QQmlSA::GenericPass::resolveType(QAnyStringView
    moduleName, QAnyStringView typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#resolveType

    Parameters
    ----------

    moduleName : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::GenericPass::resolveType(QAnyStringView moduleName,
    #      QAnyStringView typeName)
    address = self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass11resolveTypeE14QAnyStringViewS1_',
        moduleName, typeName,
    )
    return QQmlSA.Element._cuteOwning(address)

  @overload(str, str)
  def resolveAttached(
      self,
      moduleName: str,
      typeName: str,
  ) -> QQmlSA.Element:
    """
    Calls Qt's 'Element QQmlSA::GenericPass::resolveAttached(QAnyStringView
    moduleName, QAnyStringView typeName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#resolveAttached

    Parameters
    ----------

    moduleName : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::GenericPass::resolveAttached(QAnyStringView
    #      moduleName, QAnyStringView typeName)
    address = self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass15resolveAttachedE14QAnyStringViewS1_',
        moduleName, typeName,
    )
    return QQmlSA.Element._cuteOwning(address)

  @overload(WAIT['QQmlSA.Binding'])
  def resolveLiteralType(self, binding: QQmlSA.Binding) -> QQmlSA.Element:
    """
    Calls Qt's 'Element QQmlSA::GenericPass::resolveLiteralType(const Binding
    &binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#resolveLiteralType

    Parameters
    ----------

    binding : QQmlSA.Binding
      Passed on as a value: Qt reads the C++ QQmlSA::Binding, which stays
      Python's own.

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::GenericPass::resolveLiteralType(const Binding
    #      &binding)
    address = self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass18resolveLiteralTypeERKNS_7BindingE',
        self._valueOf(binding),
    )
    return QQmlSA.Element._cuteOwning(address)

  @overload(str, WAIT['QQmlSA.Element'])
  def resolveIdToElement(
      self,
      id: str,
      context: QQmlSA.Element,
  ) -> QQmlSA.Element:
    """
    Calls Qt's 'Element
    QQmlSA::GenericPass::resolveIdToElement(QAnyStringView id, const Element
    &context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#resolveIdToElement

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    context : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    Returns
    -------

    QQmlSA.Element
      A new cute QQmlSA::Element around the copy Qt gave back. Python owns
      it.
    """
    #  Element QQmlSA::GenericPass::resolveIdToElement(QAnyStringView id,
    #      const Element &context)
    address = self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass18resolveIdToElementE14QAnyStringView'
        'RKNS_7ElementE',
        id, self._valueOf(context),
    )
    return QQmlSA.Element._cuteOwning(address)

  @overload(WAIT['QQmlSA.Element'], WAIT['QQmlSA.Element'])
  def resolveElementToId(
      self,
      element: QQmlSA.Element,
      context: QQmlSA.Element,
  ) -> str:
    """
    Calls Qt's 'QString QQmlSA::GenericPass::resolveElementToId(const Element
    &element, const Element &context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-genericpass.html#resolveElementToId

    Parameters
    ----------

    element : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    context : QQmlSA.Element
      Passed on as a value: Qt reads the C++ QQmlSA::Element, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::GenericPass::resolveElementToId(const Element
    #      &element, const Element &context)
    return self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass18resolveElementToIdERKNS_7ElementES3'
        '_',
        self._valueOf(element), self._valueOf(context),
    )

  @overload(WAIT['QQmlSA.SourceLocation'])
  def sourceCode(self, location: QQmlSA.SourceLocation) -> str:
    """
    Calls Qt's 'QString
    QQmlSA::GenericPass::sourceCode(QQmlSA::SourceLocation location)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-genericpass.html#sourceCode

    Parameters
    ----------

    location : QQmlSA.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlSA::GenericPass::sourceCode(QQmlSA::SourceLocation
    #      location)
    return self.uglySide.call(
        'ritual_ZN6QQmlSA11GenericPass10sourceCodeENS_14SourceLocationE',
        self._valueOf(location),
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'GenericPassPrivate *QQmlSA::GenericPass::d_func()': the compiler
      refuses its ritual as it would be written here: unknown type name
      'GenericPassPrivate'; did you mean 'QQmlSA::GenericPassPrivate'?.
    - Qt's 'const GenericPassPrivate *QQmlSA::GenericPass::d_func() const':
      the compiler refuses its ritual as it would be written here: unknown
      type name 'GenericPassPrivate'; did you mean
      'QQmlSA::GenericPassPrivate'?.
    """
    raise NotImplementedError(
        "'QQmlSA.GenericPass.d_func' has no cute function yet. Qt's "
        "'GenericPassPrivate *QQmlSA::GenericPass::d_func()': the compiler "
        "refuses its ritual as it would be written here: unknown type name "
        "'GenericPassPrivate'; did you mean 'QQmlSA::GenericPassPrivate'?. "
        "Qt's 'const GenericPassPrivate *QQmlSA::GenericPass::d_func() "
        "const': the compiler refuses its ritual as it would be written "
        "here: unknown type name 'GenericPassPrivate'; did you mean "
        "'QQmlSA::GenericPassPrivate'?.")
