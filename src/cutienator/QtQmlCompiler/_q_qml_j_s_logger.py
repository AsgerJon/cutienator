"""
QQmlJSLogger binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSLogger to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQml import QQmlJS
from . import QQmlSA, QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import Message, QQmlJSFixSuggestion
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Message = WAIT['Message']
  QQmlJSFixSuggestion = WAIT['QQmlJSFixSuggestion']


class QQmlJSLogger(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSLogger: a plain Python object standing in front
  of one C++ QQmlJSLogger.

  What exists
  -----------

  Every function of Qt's QQmlJSLogger that has a ritual and that Python can
  call so far, 39 names in all: 'registerCategory', 'hasWarnings',
  'hasErrors', 'numWarnings', 'numErrors', 'categorySeverity',
  'setCategorySeverity', 'wasCategoryChanged', 'compileErrorSeverity',
  'setCompileErrorSeverity', 'compileErrorPrefix', 'setCompileErrorPrefix',
  'compileSkipPrefix', 'setCompileSkipPrefix', 'logCompileError',
  'logCompileSkip', 'setSilent', 'isSilent', 'setManualFlush',
  'hasManualFlush', 'manualFlush', 'setIsDisabled', 'isDisabled', 'setCode',
  'code', 'setFilePath', 'filePath', 'currentFunctionHasCompileError',
  'currentFunctionWasSkipped', 'currentFunctionHasErrorOrSkip',
  'currentFunctionCompileErrorMessage', 'currentFunctionCompileSkipMessage',
  'startTransaction', 'commit', 'rollback', 'finalizeFunction',
  'printContext', 'printFix', 'countMessage'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QQmlJS::LoggerCategory> QQmlJSLogger::categories() const':
    gives a type Python has no way to take yet.
  - Qt's 'const QList<QQmlJS::LoggerCategory>
    &QQmlJSLogger::builtinCategories()': gives a type Python has no way to
    take yet.
  - Qt's 'QQmlJSLogger::~QQmlJSLogger()': the destructor: Python never
    removes a C++ QQmlJSLogger.
  - Qt's 'void QQmlJSLogger::log(const QString &message,
    QQmlJS::LoggerWarningId id, const QQmlJS::SourceLocation &srcLocation,
    bool showContext, bool showFileName, const
    std::optional<QQmlJSFixSuggestion> &suggestion, std::optional<quint32>
    customLineForDisabling)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQmlJSLogger::processMessages(QSpan<const
    QQmlJS::DiagnosticMessage> messages, const QQmlJS::LoggerWarningId id,
    const QQmlJS::SourceLocation &sourceLocation)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QQmlJSLogger::ignoreWarnings(uint32_t line, const
    QSet<QString> &categories)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQmlJSLogger::log(Message &&diagMsg, bool showContext, bool
    showFileName)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 53 functions Qt declares: 4 forbidden; 2 a template.

  What to expect
  --------------

  - The C++ QQmlJSLogger is created at the first use, not by
    'QQmlJSLogger(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSLogger.
  - Each name of Qt's QQmlJSLogger that has no cute function yet,
    'builtinCategories', 'categories', 'ignoreWarnings',
    'iterateAllMessages', 'iterateCurrentFunctionMessages', 'log',
    'processMessages', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSLogger'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasWarnings(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSLogger::hasWarnings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#hasWarnings
    """
    #  bool QQmlJSLogger::hasWarnings() const
    return self.uglySide.call('ritual_ZNK12QQmlJSLogger11hasWarningsEv')

  def hasErrors(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSLogger::hasErrors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#hasErrors
    """
    #  bool QQmlJSLogger::hasErrors() const
    return self.uglySide.call('ritual_ZNK12QQmlJSLogger9hasErrorsEv')

  def numWarnings(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlJSLogger::numWarnings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#numWarnings
    """
    #  qsizetype QQmlJSLogger::numWarnings() const
    return self.uglySide.call('ritual_ZNK12QQmlJSLogger11numWarningsEv')

  def numErrors(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlJSLogger::numErrors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#numErrors
    """
    #  qsizetype QQmlJSLogger::numErrors() const
    return self.uglySide.call('ritual_ZNK12QQmlJSLogger9numErrorsEv')

  @overload(WAIT['QQmlSA.LoggerWarningId'])
  def categorySeverity(
      self,
      id: QQmlSA.LoggerWarningId,
  ) -> QQmlSA.WarningSeverity:
    """
    Calls Qt's 'QQmlJS::WarningSeverity
    QQmlJSLogger::categorySeverity(QQmlJS::LoggerWarningId id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#categorySeverity

    Parameters
    ----------

    id : QQmlSA.LoggerWarningId
      Passed on as a value: Qt reads the C++ QQmlSA::LoggerWarningId, which
      stays Python's own.

    Returns
    -------

    QQmlSA.WarningSeverity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.WarningSeverity(number)' gives.
    """
    #  QQmlJS::WarningSeverity
    #      QQmlJSLogger::categorySeverity(QQmlJS::LoggerWarningId id) const
    return QQmlSA.WarningSeverity(self.uglySide.call(
        'ritual_ZNK12QQmlJSLogger16categorySeverityEN6QQmlSA15LoggerWarning'
        'IdE',
        self._valueOf(id),
    ))

  @overload(WAIT['QQmlSA.LoggerWarningId'])
  def wasCategoryChanged(self, id: QQmlSA.LoggerWarningId) -> bool:
    """
    Calls Qt's 'bool QQmlJSLogger::wasCategoryChanged(QQmlJS::LoggerWarningId
    id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#wasCategoryChanged

    Parameters
    ----------

    id : QQmlSA.LoggerWarningId
      Passed on as a value: Qt reads the C++ QQmlSA::LoggerWarningId, which
      stays Python's own.
    """
    #  bool QQmlJSLogger::wasCategoryChanged(QQmlJS::LoggerWarningId id)
    #      const
    return self.uglySide.call(
        'ritual_ZNK12QQmlJSLogger18wasCategoryChangedEN6QQmlSA15LoggerWarni'
        'ngIdE',
        self._valueOf(id),
    )

  def compileErrorSeverity(self) -> QQmlSA.WarningSeverity:
    """
    Calls Qt's 'QQmlJS::WarningSeverity QQmlJSLogger::compileErrorSeverity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#compileErrorSeverity

    Returns
    -------

    QQmlSA.WarningSeverity
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlSA.WarningSeverity(number)' gives.
    """
    #  QQmlJS::WarningSeverity QQmlJSLogger::compileErrorSeverity() const
    return QQmlSA.WarningSeverity(self.uglySide.call(
        'ritual_ZNK12QQmlJSLogger20compileErrorSeverityEv',
    ))

  def compileErrorPrefix(self) -> str:
    """
    Calls Qt's 'QString QQmlJSLogger::compileErrorPrefix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#compileErrorPrefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSLogger::compileErrorPrefix() const
    return self.uglySide.call(
        'ritual_ZNK12QQmlJSLogger18compileErrorPrefixEv',
    )

  def compileSkipPrefix(self) -> str:
    """
    Calls Qt's 'QString QQmlJSLogger::compileSkipPrefix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#compileSkipPrefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSLogger::compileSkipPrefix() const
    return self.uglySide.call(
        'ritual_ZNK12QQmlJSLogger17compileSkipPrefixEv',
    )

  def isSilent(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSLogger::isSilent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#isSilent
    """
    #  bool QQmlJSLogger::isSilent() const
    return self.uglySide.call('ritual_ZNK12QQmlJSLogger8isSilentEv')

  def hasManualFlush(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSLogger::hasManualFlush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#hasManualFlush
    """
    #  bool QQmlJSLogger::hasManualFlush() const
    return self.uglySide.call('ritual_ZNK12QQmlJSLogger14hasManualFlushEv')

  def isDisabled(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSLogger::isDisabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#isDisabled
    """
    #  bool QQmlJSLogger::isDisabled() const
    return self.uglySide.call('ritual_ZNK12QQmlJSLogger10isDisabledEv')

  def code(self) -> str:
    """
    Calls Qt's 'QString QQmlJSLogger::code() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#code

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSLogger::code() const
    return self.uglySide.call('ritual_ZNK12QQmlJSLogger4codeEv')

  def filePath(self) -> str:
    """
    Calls Qt's 'QString QQmlJSLogger::filePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#filePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSLogger::filePath() const
    return self.uglySide.call('ritual_ZNK12QQmlJSLogger8filePathEv')

  def currentFunctionHasCompileError(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSLogger::currentFunctionHasCompileError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#currentFunctionHasCompileError
    """
    #  bool QQmlJSLogger::currentFunctionHasCompileError() const
    return self.uglySide.call(
        'ritual_ZNK12QQmlJSLogger30currentFunctionHasCompileErrorEv',
    )

  def currentFunctionWasSkipped(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSLogger::currentFunctionWasSkipped() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#currentFunctionWasSkipped
    """
    #  bool QQmlJSLogger::currentFunctionWasSkipped() const
    return self.uglySide.call(
        'ritual_ZNK12QQmlJSLogger25currentFunctionWasSkippedEv',
    )

  def currentFunctionHasErrorOrSkip(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSLogger::currentFunctionHasErrorOrSkip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#currentFunctionHasErrorOrSkip
    """
    #  bool QQmlJSLogger::currentFunctionHasErrorOrSkip() const
    return self.uglySide.call(
        'ritual_ZNK12QQmlJSLogger29currentFunctionHasErrorOrSkipEv',
    )

  def currentFunctionCompileErrorMessage(self) -> str:
    """
    Calls Qt's 'QString QQmlJSLogger::currentFunctionCompileErrorMessage()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSLogger::currentFunctionCompileErrorMessage() const
    return self.uglySide.call(
        'ritual_ZNK12QQmlJSLogger34currentFunctionCompileErrorMessageEv',
    )

  def currentFunctionCompileSkipMessage(self) -> str:
    """
    Calls Qt's 'QString QQmlJSLogger::currentFunctionCompileSkipMessage()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSLogger::currentFunctionCompileSkipMessage() const
    return self.uglySide.call(
        'ritual_ZNK12QQmlJSLogger33currentFunctionCompileSkipMessageEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QQmlSA.LoggerWarningId'], QQmlSA.WarningSeverity)
  def setCategorySeverity(
      self,
      id: QQmlSA.LoggerWarningId,
      severity: QQmlSA.WarningSeverity,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSLogger::setCategorySeverity(QQmlJS::LoggerWarningId id,
    QQmlJS::WarningSeverity severity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#setCategorySeverity

    Parameters
    ----------

    id : QQmlSA.LoggerWarningId
      Passed on as a value: Qt reads the C++ QQmlSA::LoggerWarningId, which
      stays Python's own.

    severity : QQmlSA.WarningSeverity
      Passed on as its number.
    """
    #  void QQmlJSLogger::setCategorySeverity(QQmlJS::LoggerWarningId id,
    #      QQmlJS::WarningSeverity severity)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger19setCategorySeverityEN6QQmlSA15LoggerWarni'
        'ngIdENS0_15WarningSeverityE',
        self._valueOf(id), severity.value,
    )

  @overload(QQmlSA.WarningSeverity)
  def setCompileErrorSeverity(
      self,
      severity: QQmlSA.WarningSeverity,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSLogger::setCompileErrorSeverity(QQmlJS::WarningSeverity severity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#setCompileErrorSeverity

    Parameters
    ----------

    severity : QQmlSA.WarningSeverity
      Passed on as its number.
    """
    #  void QQmlJSLogger::setCompileErrorSeverity(QQmlJS::WarningSeverity
    #      severity)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger23setCompileErrorSeverityEN6QQmlSA15Warning'
        'SeverityE',
        severity.value,
    )

  @overload(str)
  def setCompileErrorPrefix(self, prefix: str) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::setCompileErrorPrefix(const QString
    &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#setCompileErrorPrefix

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSLogger::setCompileErrorPrefix(const QString &prefix)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger21setCompileErrorPrefixERK7QString', prefix,
    )

  @overload(str)
  def setCompileSkipPrefix(self, prefix: str) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::setCompileSkipPrefix(const QString
    &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslogger.html#setCompileSkipPrefix

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSLogger::setCompileSkipPrefix(const QString &prefix)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger20setCompileSkipPrefixERK7QString', prefix,
    )

  @overload(bool)
  def setSilent(self, silent: bool) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::setSilent(bool silent)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#setSilent

    Parameters
    ----------

    silent : bool
      Passed on as it is.
    """
    #  void QQmlJSLogger::setSilent(bool silent)
    self.uglySide.call('ritual_ZN12QQmlJSLogger9setSilentEb', silent)

  @overload(bool)
  def setManualFlush(self, manualFlush: bool) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::setManualFlush(bool manualFlush)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#setManualFlush

    Parameters
    ----------

    manualFlush : bool
      Passed on as it is.
    """
    #  void QQmlJSLogger::setManualFlush(bool manualFlush)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger14setManualFlushEb', manualFlush,
    )

  @overload(bool)
  def setIsDisabled(self, isDisabled: bool) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::setIsDisabled(bool isDisabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#setIsDisabled

    Parameters
    ----------

    isDisabled : bool
      Passed on as it is.
    """
    #  void QQmlJSLogger::setIsDisabled(bool isDisabled)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger13setIsDisabledEb', isDisabled,
    )

  @overload(str)
  def setCode(self, code: str) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::setCode(const QString &code)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#setCode

    Parameters
    ----------

    code : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSLogger::setCode(const QString &code)
    self.uglySide.call('ritual_ZN12QQmlJSLogger7setCodeERK7QString', code)

  @overload(str)
  def setFilePath(self, filePath: str) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::setFilePath(const QString &filePath)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#setFilePath

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSLogger::setFilePath(const QString &filePath)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger11setFilePathERK7QString', filePath,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlJSLogger::QQmlJSLogger()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#QQmlJSLogger
    """
    #  QQmlJSLogger::QQmlJSLogger()
    self._noteCreation(QQmlJSLogger, lambda: Rituals.call(
        'ritual_ZN12QQmlJSLoggerC1Ev',
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

  @overload(WAIT['QQmlJS.LoggerCategory'])
  def registerCategory(self, category: QQmlJS.LoggerCategory) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::registerCategory(const
    QQmlJS::LoggerCategory &category)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#registerCategory

    Parameters
    ----------

    category : QQmlJS.LoggerCategory
      Passed on as a value: Qt reads the C++ QQmlJS::LoggerCategory, which
      stays Python's own.
    """
    #  void QQmlJSLogger::registerCategory(const QQmlJS::LoggerCategory
    #      &category)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger16registerCategoryERKN6QQmlJS14LoggerCatego'
        'ryE',
        self._valueOf(category),
    )

  @overload(str, WAIT['QQmlJS.SourceLocation'])
  def logCompileError(
      self,
      message: str,
      srcLocation: QQmlJS.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::logCompileError(const QString &message,
    const QQmlJS::SourceLocation &srcLocation)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#logCompileError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    srcLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJSLogger::logCompileError(const QString &message, const
    #      QQmlJS::SourceLocation &srcLocation)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger15logCompileErrorERK7QStringRKN6QQmlJS14Sou'
        'rceLocationE',
        message, self._valueOf(srcLocation),
    )

  @overload(str, WAIT['QQmlJS.SourceLocation'])
  def logCompileSkip(
      self,
      message: str,
      srcLocation: QQmlJS.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::logCompileSkip(const QString &message,
    const QQmlJS::SourceLocation &srcLocation)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#logCompileSkip

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    srcLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJSLogger::logCompileSkip(const QString &message, const
    #      QQmlJS::SourceLocation &srcLocation)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger14logCompileSkipERK7QStringRKN6QQmlJS14Sour'
        'ceLocationE',
        message, self._valueOf(srcLocation),
    )

  def manualFlush(self) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::manualFlush()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#manualFlush
    """
    #  void QQmlJSLogger::manualFlush()
    self.uglySide.call('ritual_ZN12QQmlJSLogger11manualFlushEv')

  def startTransaction(self) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::startTransaction()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#startTransaction
    """
    #  void QQmlJSLogger::startTransaction()
    self.uglySide.call('ritual_ZN12QQmlJSLogger16startTransactionEv')

  def commit(self) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::commit()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#commit
    """
    #  void QQmlJSLogger::commit()
    self.uglySide.call('ritual_ZN12QQmlJSLogger6commitEv')

  def rollback(self) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::rollback()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#rollback
    """
    #  void QQmlJSLogger::rollback()
    self.uglySide.call('ritual_ZN12QQmlJSLogger8rollbackEv')

  def finalizeFunction(self) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::finalizeFunction()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#finalizeFunction
    """
    #  void QQmlJSLogger::finalizeFunction()
    self.uglySide.call('ritual_ZN12QQmlJSLogger16finalizeFunctionEv')

  @overload(WAIT['QQmlJS.SourceLocation'])
  def printContext(self, location: QQmlJS.SourceLocation) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::printContext(const QQmlJS::SourceLocation
    &location)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#printContext

    Parameters
    ----------

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJSLogger::printContext(const QQmlJS::SourceLocation
    #      &location)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger12printContextERKN6QQmlJS14SourceLocationE',
        self._valueOf(location),
    )

  @overload(QQmlJSFixSuggestion)
  def printFix(self, fix: QQmlJSFixSuggestion) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::printFix(const QQmlJSFixSuggestion &fix)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#printFix

    Parameters
    ----------

    fix : QQmlJSFixSuggestion
      Passed on as a value: Qt reads the C++ QQmlJSFixSuggestion, which stays
      Python's own.
    """
    #  void QQmlJSLogger::printFix(const QQmlJSFixSuggestion &fix)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger8printFixERK19QQmlJSFixSuggestion',
        self._valueOf(fix),
    )

  @overload(Message)
  def countMessage(self, message: Message) -> None:
    """
    Calls Qt's 'void QQmlJSLogger::countMessage(const Message &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljslogger.html#countMessage

    Parameters
    ----------

    message : Message
      Passed on as a value: Qt reads the C++ Message, which stays Python's
      own.
    """
    #  void QQmlJSLogger::countMessage(const Message &message)
    self.uglySide.call(
        'ritual_ZN12QQmlJSLogger12countMessageERK7Message',
        self._valueOf(message),
    )

  @staticmethod
  def builtinCategories(*__, **_) -> Never:
    """
    Qt's 'const QList<QQmlJS::LoggerCategory>
    &QQmlJSLogger::builtinCategories()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlJSLogger.builtinCategories' has no cute function yet. Qt's "
        "'const QList<QQmlJS::LoggerCategory> "
        "&QQmlJSLogger::builtinCategories()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def categories(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlJS::LoggerCategory> QQmlJSLogger::categories() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSLogger.categories' has no cute function yet. Qt's "
        "'QList<QQmlJS::LoggerCategory> QQmlJSLogger::categories() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def ignoreWarnings(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSLogger::ignoreWarnings(uint32_t line, const
    QSet<QString> &categories)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlJSLogger.ignoreWarnings' has no cute function yet. Qt's 'void "
        "QQmlJSLogger::ignoreWarnings(uint32_t line, const QSet<QString> "
        "&categories)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def iterateAllMessages(*__, **_) -> Never:
    """
    Qt's 'QQmlJSLogger::iterateAllMessages': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlJSLogger.iterateAllMessages' has no cute function yet. Qt's "
        "'QQmlJSLogger::iterateAllMessages': a template: a pattern and no "
        "single function.")

  @staticmethod
  def iterateCurrentFunctionMessages(*__, **_) -> Never:
    """
    Qt's 'QQmlJSLogger::iterateCurrentFunctionMessages': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlJSLogger.iterateCurrentFunctionMessages' has no cute function "
        "yet. Qt's 'QQmlJSLogger::iterateCurrentFunctionMessages': a "
        "template: a pattern and no single function.")

  @staticmethod
  def log(*__, **_) -> Never:
    """
    - Qt's 'void QQmlJSLogger::log(const QString &message,
      QQmlJS::LoggerWarningId id, const QQmlJS::SourceLocation &srcLocation,
      bool showContext, bool showFileName, const
      std::optional<QQmlJSFixSuggestion> &suggestion, std::optional<quint32>
      customLineForDisabling)': takes a type Python has no way to hand over
      yet.
    - Qt's 'void QQmlJSLogger::log(Message &&diagMsg, bool showContext, bool
      showFileName)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSLogger.log' has no cute function yet. Qt's 'void "
        "QQmlJSLogger::log(const QString &message, QQmlJS::LoggerWarningId "
        "id, const QQmlJS::SourceLocation &srcLocation, bool showContext, "
        "bool showFileName, const std::optional<QQmlJSFixSuggestion> "
        "&suggestion, std::optional<quint32> customLineForDisabling)': "
        "takes a type Python has no way to hand over yet. Qt's 'void "
        "QQmlJSLogger::log(Message &&diagMsg, bool showContext, bool "
        "showFileName)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def processMessages(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSLogger::processMessages(QSpan<const
    QQmlJS::DiagnosticMessage> messages, const QQmlJS::LoggerWarningId id,
    const QQmlJS::SourceLocation &sourceLocation)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSLogger.processMessages' has no cute function yet. Qt's "
        "'void QQmlJSLogger::processMessages(QSpan<const "
        "QQmlJS::DiagnosticMessage> messages, const QQmlJS::LoggerWarningId "
        "id, const QQmlJS::SourceLocation &sourceLocation)': takes a type "
        "Python has no way to hand over yet.")
