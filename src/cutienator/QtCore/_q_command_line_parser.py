"""
QCommandLineParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcommandlineparser.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCommandLineOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCommandLineOption = WAIT['QCommandLineOption']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCommandLineParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCommandLineParser: a plain Python object standing in
  front of one C++ QCommandLineParser.

  What exists
  -----------

  Every function of Qt's QCommandLineParser that has a ritual and that Python
  can call so far, 24 names in all: 'tr', 'setSingleDashWordOptionMode',
  'setOptionsAfterPositionalArgumentsMode', 'addOption', 'addOptions',
  'addVersionOption', 'addHelpOption', 'setApplicationDescription',
  'applicationDescription', 'addPositionalArgument',
  'clearPositionalArguments', 'process', 'parse', 'errorText', 'isSet',
  'value', 'values', 'positionalArguments', 'optionNames',
  'unknownOptionNames', 'showVersion', 'showHelp', 'helpText',
  'showMessageAndExit'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCommandLineParser::~QCommandLineParser()': the destructor: Python
    never removes a C++ QCommandLineParser.
  - Qt's 'void QCommandLineParser::process(const QCoreApplication &app)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QCommandLineParser is created at the first use, not by
    'QCommandLineParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCommandLineParser.
  """

  #  The enums Qt writes inside QCommandLineParser, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class MessageType(CuteNum, scoped=True):
    """
    The enum 'QCommandLineParser::MessageType' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Information = Kee[int](0)
    Error = Kee[int](1)

  class OptionsAfterPositionalArgumentsMode(CuteNum):
    """
    The enum 'QCommandLineParser::OptionsAfterPositionalArgumentsMode' of Qt,
    with the 2 names Qt gives in it.
    """

    ParseAsOptions = Kee[int](0)
    ParseAsPositionalArguments = Kee[int](1)

  class SingleDashWordOptionMode(CuteNum):
    """
    The enum 'QCommandLineParser::SingleDashWordOptionMode' of Qt, with the 2
    names Qt gives in it.
    """

    ParseAsCompactedShortOptions = Kee[int](0)
    ParseAsLongOptions = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QCommandLineParser::tr(const char *sourceText, const
    char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommandLineParser::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN18QCommandLineParser2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  @staticmethod
  @overload(MessageType, str)
  @overload(MessageType, str, int)
  def showMessageAndExit(
      type: MessageType,
      message: str,
      exitCode: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QCommandLineParser::showMessageAndExit(MessageType type,
    const QString &message, int exitCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#showMessageAndExit

    Parameters
    ----------

    type : MessageType
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.

    exitCode : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QCommandLineParser::showMessageAndExit(MessageType type, const
    #      QString &message, int exitCode)
    Rituals.call(
        'ritual_ZN18QCommandLineParser18showMessageAndExitENS_11MessageType'
        'ERK7QStringi',
        type.value, message, exitCode,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCommandLineParser'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def applicationDescription(self) -> str:
    """
    Calls Qt's 'QString QCommandLineParser::applicationDescription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#applicationDescription

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommandLineParser::applicationDescription() const
    return self.uglySide.call(
        'ritual_ZNK18QCommandLineParser22applicationDescriptionEv',
    )

  def errorText(self) -> str:
    """
    Calls Qt's 'QString QCommandLineParser::errorText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#errorText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommandLineParser::errorText() const
    return self.uglySide.call('ritual_ZNK18QCommandLineParser9errorTextEv')

  @overload(str)
  def isSet(self, name: str) -> bool:
    """
    Calls Qt's 'bool QCommandLineParser::isSet(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#isSet

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QCommandLineParser::isSet(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK18QCommandLineParser5isSetERK7QString', name,
    )

  @overload(QCommandLineOption)
  def isSet(self, option: QCommandLineOption) -> bool:
    """
    Calls Qt's 'bool QCommandLineParser::isSet(const QCommandLineOption
    &option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#isSet

    Parameters
    ----------

    option : QCommandLineOption
      Passed on as a value: Qt reads the C++ QCommandLineOption, which stays
      Python's own.
    """
    #  bool QCommandLineParser::isSet(const QCommandLineOption &option) const
    return self.uglySide.call(
        'ritual_ZNK18QCommandLineParser5isSetERK18QCommandLineOption',
        self._valueOf(option),
    )

  @overload(str)
  def value(self, name: str) -> str:
    """
    Calls Qt's 'QString QCommandLineParser::value(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#value

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommandLineParser::value(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK18QCommandLineParser5valueERK7QString', name,
    )

  @overload(QCommandLineOption)
  def value(self, option: QCommandLineOption) -> str:
    """
    Calls Qt's 'QString QCommandLineParser::value(const QCommandLineOption
    &option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#value

    Parameters
    ----------

    option : QCommandLineOption
      Passed on as a value: Qt reads the C++ QCommandLineOption, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommandLineParser::value(const QCommandLineOption &option)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QCommandLineParser5valueERK18QCommandLineOption',
        self._valueOf(option),
    )

  @overload(str)
  def values(self, name: str) -> QStringList:
    """
    Calls Qt's 'QStringList QCommandLineParser::values(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#values

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCommandLineParser::values(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK18QCommandLineParser6valuesERK7QString', name,
    )
    return QStringList._cuteOwning(address)

  @overload(QCommandLineOption)
  def values(self, option: QCommandLineOption) -> QStringList:
    """
    Calls Qt's 'QStringList QCommandLineParser::values(const
    QCommandLineOption &option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#values

    Parameters
    ----------

    option : QCommandLineOption
      Passed on as a value: Qt reads the C++ QCommandLineOption, which stays
      Python's own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCommandLineParser::values(const QCommandLineOption
    #      &option) const
    address = self.uglySide.call(
        'ritual_ZNK18QCommandLineParser6valuesERK18QCommandLineOption',
        self._valueOf(option),
    )
    return QStringList._cuteOwning(address)

  def positionalArguments(self) -> QStringList:
    """
    Calls Qt's 'QStringList QCommandLineParser::positionalArguments() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#positionalArguments

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCommandLineParser::positionalArguments() const
    address = self.uglySide.call(
        'ritual_ZNK18QCommandLineParser19positionalArgumentsEv',
    )
    return QStringList._cuteOwning(address)

  def optionNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QCommandLineParser::optionNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#optionNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCommandLineParser::optionNames() const
    address = self.uglySide.call(
        'ritual_ZNK18QCommandLineParser11optionNamesEv',
    )
    return QStringList._cuteOwning(address)

  def unknownOptionNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QCommandLineParser::unknownOptionNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#unknownOptionNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCommandLineParser::unknownOptionNames() const
    address = self.uglySide.call(
        'ritual_ZNK18QCommandLineParser18unknownOptionNamesEv',
    )
    return QStringList._cuteOwning(address)

  def helpText(self) -> str:
    """
    Calls Qt's 'QString QCommandLineParser::helpText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#helpText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommandLineParser::helpText() const
    return self.uglySide.call('ritual_ZNK18QCommandLineParser8helpTextEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(SingleDashWordOptionMode)
  def setSingleDashWordOptionMode(
      self,
      parsingMode: SingleDashWordOptionMode,
  ) -> None:
    """
    Calls Qt's 'void
    QCommandLineParser::setSingleDashWordOptionMode(SingleDashWordOptionMode
    parsingMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html

    Parameters
    ----------

    parsingMode : SingleDashWordOptionMode
      Passed on as its number.
    """
    #  void QCommandLineParser::setSingleDashWordOptionMode(
    #      SingleDashWordOptionMode parsingMode)
    self.uglySide.call(
        'ritual_ZN18QCommandLineParser27setSingleDashWordOptionModeENS_24Si'
        'ngleDashWordOptionModeE',
        parsingMode.value,
    )

  @overload(OptionsAfterPositionalArgumentsMode)
  def setOptionsAfterPositionalArgumentsMode(
      self,
      mode: OptionsAfterPositionalArgumentsMode,
  ) -> None:
    """
    Calls Qt's 'void
    QCommandLineParser::setOptionsAfterPositionalArgumentsMode(
    OptionsAfterPositionalArgumentsMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html

    Parameters
    ----------

    mode : OptionsAfterPositionalArgumentsMode
      Passed on as its number.
    """
    #  void QCommandLineParser::setOptionsAfterPositionalArgumentsMode(
    #      OptionsAfterPositionalArgumentsMode mode)
    self.uglySide.call(
        'ritual_ZN18QCommandLineParser38setOptionsAfterPositionalArgumentsM'
        'odeENS_35OptionsAfterPositionalArgumentsModeE',
        mode.value,
    )

  @overload(str)
  def setApplicationDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QCommandLineParser::setApplicationDescription(const
    QString &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#setApplicationDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCommandLineParser::setApplicationDescription(const QString
    #      &description)
    self.uglySide.call(
        'ritual_ZN18QCommandLineParser25setApplicationDescriptionERK7QStrin'
        'g',
        description,
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
    Notes what was given, for Qt's
    'QCommandLineParser::QCommandLineParser()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#QCommandLineParser
    """
    #  QCommandLineParser::QCommandLineParser()
    self._noteCreation(QCommandLineParser, lambda: Rituals.call(
        'ritual_ZN18QCommandLineParserC1Ev',
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

  @overload(QCommandLineOption)
  def addOption(self, commandLineOption: QCommandLineOption) -> bool:
    """
    Calls Qt's 'bool QCommandLineParser::addOption(const QCommandLineOption
    &commandLineOption)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#addOption

    Parameters
    ----------

    commandLineOption : QCommandLineOption
      Passed on as a value: Qt reads the C++ QCommandLineOption, which stays
      Python's own.
    """
    #  bool QCommandLineParser::addOption(const QCommandLineOption
    #      &commandLineOption)
    return self.uglySide.call(
        'ritual_ZN18QCommandLineParser9addOptionERK18QCommandLineOption',
        self._valueOf(commandLineOption),
    )

  @overload(QList[QCommandLineOption])
  def addOptions(self, options: QList[QCommandLineOption]) -> bool:
    """
    Calls Qt's 'bool QCommandLineParser::addOptions(const
    QList<QCommandLineOption> &options)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#addOptions

    Parameters
    ----------

    options : QList[QCommandLineOption]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QCommandLineParser::addOptions(const QList<QCommandLineOption>
    #      &options)
    return self.uglySide.call(
        'ritual_ZN18QCommandLineParser10addOptionsERK5QListI18QCommandLineO'
        'ptionE',
        self._valueOf(options),
    )

  def addVersionOption(self) -> QCommandLineOption:
    """
    Calls Qt's 'QCommandLineOption QCommandLineParser::addVersionOption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#addVersionOption

    Returns
    -------

    QCommandLineOption
      A new cute QCommandLineOption around the copy Qt gave back. Python owns
      it.
    """
    #  QCommandLineOption QCommandLineParser::addVersionOption()
    address = self.uglySide.call(
        'ritual_ZN18QCommandLineParser16addVersionOptionEv',
    )
    from . import QCommandLineOption
    return QCommandLineOption._cuteOwning(address)

  def addHelpOption(self) -> QCommandLineOption:
    """
    Calls Qt's 'QCommandLineOption QCommandLineParser::addHelpOption()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#addHelpOption

    Returns
    -------

    QCommandLineOption
      A new cute QCommandLineOption around the copy Qt gave back. Python owns
      it.
    """
    #  QCommandLineOption QCommandLineParser::addHelpOption()
    address = self.uglySide.call(
        'ritual_ZN18QCommandLineParser13addHelpOptionEv',
    )
    from . import QCommandLineOption
    return QCommandLineOption._cuteOwning(address)

  @overload(str, str)
  @overload(str, str, str)
  def addPositionalArgument(
      self,
      name: str,
      description: str,
      syntax: str = '',
  ) -> None:
    """
    Calls Qt's 'void QCommandLineParser::addPositionalArgument(const QString
    &name, const QString &description, const QString &syntax)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#addPositionalArgument

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    description : str
      Passed on as it is: a QString is made of it for the call.

    syntax : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QCommandLineParser::addPositionalArgument(const QString &name,
    #      const QString &description, const QString &syntax)
    self.uglySide.call(
        'ritual_ZN18QCommandLineParser21addPositionalArgumentERK7QStringS2_'
        'S2_',
        name, description, syntax,
    )

  def clearPositionalArguments(self) -> None:
    """
    Calls Qt's 'void QCommandLineParser::clearPositionalArguments()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#clearPositionalArguments
    """
    #  void QCommandLineParser::clearPositionalArguments()
    self.uglySide.call(
        'ritual_ZN18QCommandLineParser24clearPositionalArgumentsEv',
    )

  @overload(QStringList)
  def process(self, arguments: QStringList) -> None:
    """
    Calls Qt's 'void QCommandLineParser::process(const QStringList
    &arguments)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#process

    Parameters
    ----------

    arguments : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCommandLineParser::process(const QStringList &arguments)
    self.uglySide.call(
        'ritual_ZN18QCommandLineParser7processERK5QListI7QStringE',
        self._valueOf(arguments),
    )

  @overload(QStringList)
  def parse(self, arguments: QStringList) -> bool:
    """
    Calls Qt's 'bool QCommandLineParser::parse(const QStringList
    &arguments)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#parse

    Parameters
    ----------

    arguments : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QCommandLineParser::parse(const QStringList &arguments)
    return self.uglySide.call(
        'ritual_ZN18QCommandLineParser5parseERK5QListI7QStringE',
        self._valueOf(arguments),
    )

  def showVersion(self) -> None:
    """
    Calls Qt's 'void QCommandLineParser::showVersion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineparser.html#showVersion
    """
    #  void QCommandLineParser::showVersion()
    self.uglySide.call('ritual_ZN18QCommandLineParser11showVersionEv')

  @overload()
  @overload(int)
  def showHelp(self, exitCode: int = 0) -> None:
    """
    Calls Qt's 'void QCommandLineParser::showHelp(int exitCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineparser.html#showHelp

    Parameters
    ----------

    exitCode : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QCommandLineParser::showHelp(int exitCode)
    self.uglySide.call('ritual_ZN18QCommandLineParser8showHelpEi', exitCode)
