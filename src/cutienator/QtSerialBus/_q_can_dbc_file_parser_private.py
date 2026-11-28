"""
QCanDbcFileParserPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qcandbcfileparser_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCanDbcFileParserPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRegularExpressionMatch
  from . import QCanMessageDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRegularExpressionMatch = WAIT['QRegularExpressionMatch']


class QCanDbcFileParserPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanDbcFileParserPrivate: a plain Python object
  standing in front of one C++ QCanDbcFileParserPrivate.

  C++ hands a QCanDbcFileParserPrivate around as a copy, so every C++
  QCanDbcFileParserPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanDbcFileParserPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'reset', 'parseFile',
  'extractMessage', 'parseSignal', 'addCurrentMessage', 'getMessages'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QCanDbcFileParserPrivate::addWarning(QString &&warning)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QCanDbcFileParserPrivate::~QCanDbcFileParserPrivate()': the
    destructor: Python removes its C++ QCanDbcFileParserPrivate by it, and
    has no other use for it.

  What has no ritual
  ------------------

  9 of the 17 functions Qt declares: 9 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QCanDbcFileParserPrivate is created at the first use, not by
    'QCanDbcFileParserPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanDbcFileParserPrivate back gives a copy the ritual
    made for Python, in a new cute QCanDbcFileParserPrivate.
  - Each name of Qt's QCanDbcFileParserPrivate that has no cute function yet,
    'addWarning', 'extractSignal', 'parseComment', 'parseData',
    'parseExtendedMux', 'parseMessage', 'parseSignalType',
    'parseValueDescriptions', 'postProcessSignalMultiplexing', 'processLine',
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
  __qt_class__ = 'QCanDbcFileParserPrivate'

  #  Qt's '~QCanDbcFileParserPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QCanDbcFileParserPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QCanDbcFileParserPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getMessages(self) -> QList[QCanMessageDescription]:
    """
    Calls Qt's 'QList<QCanMessageDescription>
    QCanDbcFileParserPrivate::getMessages() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandbcfileparserprivate.html#getMessages

    Returns
    -------

    QList[QCanMessageDescription]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCanMessageDescription> QCanDbcFileParserPrivate::getMessages()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QCanDbcFileParserPrivate11getMessagesEv',
    )
    from . import QCanMessageDescription
    return QList[QCanMessageDescription]._cuteOwning(address)

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

  def reset(self) -> None:
    """
    Calls Qt's 'void QCanDbcFileParserPrivate::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandbcfileparserprivate.html#reset
    """
    #  void QCanDbcFileParserPrivate::reset()
    self.uglySide.call('ritual_ZN24QCanDbcFileParserPrivate5resetEv')

  @overload(str)
  def parseFile(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QCanDbcFileParserPrivate::parseFile(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandbcfileparserprivate.html#parseFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QCanDbcFileParserPrivate::parseFile(const QString &fileName)
    return self.uglySide.call(
        'ritual_ZN24QCanDbcFileParserPrivate9parseFileERK7QString', fileName,
    )

  @overload(QRegularExpressionMatch)
  def extractMessage(
      self,
      match: QRegularExpressionMatch,
  ) -> QCanMessageDescription:
    """
    Calls Qt's 'QCanMessageDescription
    QCanDbcFileParserPrivate::extractMessage(const QRegularExpressionMatch
    &match)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandbcfileparserprivate.html#extractMessage

    Parameters
    ----------

    match : QRegularExpressionMatch
      Passed on as a value: Qt reads the C++ QRegularExpressionMatch, which
      stays Python's own.

    Returns
    -------

    QCanMessageDescription
      A new cute QCanMessageDescription around the copy Qt gave back. Python
      owns it.
    """
    #  QCanMessageDescription QCanDbcFileParserPrivate::extractMessage(const
    #      QRegularExpressionMatch &match)
    address = self.uglySide.call(
        'ritual_ZN24QCanDbcFileParserPrivate14extractMessageERK23QRegularEx'
        'pressionMatch',
        self._valueOf(match),
    )
    from . import QCanMessageDescription
    return QCanMessageDescription._cuteOwning(address)

  @overload(str)
  def parseSignal(self, data: str) -> bool:
    """
    Calls Qt's 'bool QCanDbcFileParserPrivate::parseSignal(const QStringView
    data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandbcfileparserprivate.html#parseSignal

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QCanDbcFileParserPrivate::parseSignal(const QStringView data)
    return self.uglySide.call(
        'ritual_ZN24QCanDbcFileParserPrivate11parseSignalE11QStringView',
        data,
    )

  def addCurrentMessage(self) -> None:
    """
    Calls Qt's 'void QCanDbcFileParserPrivate::addCurrentMessage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandbcfileparserprivate.html#addCurrentMessage
    """
    #  void QCanDbcFileParserPrivate::addCurrentMessage()
    self.uglySide.call(
        'ritual_ZN24QCanDbcFileParserPrivate17addCurrentMessageEv',
    )

  @staticmethod
  def addWarning(*__, **_) -> Never:
    """
    Qt's 'void QCanDbcFileParserPrivate::addWarning(QString &&warning)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanDbcFileParserPrivate.addWarning' has no cute function yet. "
        "Qt's 'void QCanDbcFileParserPrivate::addWarning(QString "
        "&&warning)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def extractSignal(*__, **_) -> Never:
    """
    Qt's 'QCanSignalDescription QCanDbcFileParserPrivate::extractSignal(const
    QRegularExpressionMatch &match)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'kQtDummySignal'.
    """
    raise NotImplementedError(
        "'QCanDbcFileParserPrivate.extractSignal' has no cute function yet. "
        "Qt's 'QCanSignalDescription "
        "QCanDbcFileParserPrivate::extractSignal(const "
        "QRegularExpressionMatch &match)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'kQtDummySignal'.")

  @staticmethod
  def parseComment(*__, **_) -> Never:
    """
    Qt's 'void QCanDbcFileParserPrivate::parseComment(const QStringView
    data)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'kMessageDef'.
    """
    raise NotImplementedError(
        "'QCanDbcFileParserPrivate.parseComment' has no cute function yet. "
        "Qt's 'void QCanDbcFileParserPrivate::parseComment(const "
        "QStringView data)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'kMessageDef'.")

  @staticmethod
  def parseData(*__, **_) -> Never:
    """
    Qt's 'bool QCanDbcFileParserPrivate::parseData(QStringView data)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'readUntilNewline'.
    """
    raise NotImplementedError(
        "'QCanDbcFileParserPrivate.parseData' has no cute function yet. "
        "Qt's 'bool QCanDbcFileParserPrivate::parseData(QStringView data)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'readUntilNewline'.")

  @staticmethod
  def parseExtendedMux(*__, **_) -> Never:
    """
    Qt's 'void QCanDbcFileParserPrivate::parseExtendedMux(const QStringView
    data)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'kQtDummySignal'.
    """
    raise NotImplementedError(
        "'QCanDbcFileParserPrivate.parseExtendedMux' has no cute function "
        "yet. Qt's 'void QCanDbcFileParserPrivate::parseExtendedMux(const "
        "QStringView data)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'kQtDummySignal'.")

  @staticmethod
  def parseMessage(*__, **_) -> Never:
    """
    Qt's 'bool QCanDbcFileParserPrivate::parseMessage(const QStringView
    data)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'kMessageDef'.
    """
    raise NotImplementedError(
        "'QCanDbcFileParserPrivate.parseMessage' has no cute function yet. "
        "Qt's 'bool QCanDbcFileParserPrivate::parseMessage(const "
        "QStringView data)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'kMessageDef'.")

  @staticmethod
  def parseSignalType(*__, **_) -> Never:
    """
    Qt's 'void QCanDbcFileParserPrivate::parseSignalType(const QStringView
    data)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'kMaybeSpaceRegExp'.
    """
    raise NotImplementedError(
        "'QCanDbcFileParserPrivate.parseSignalType' has no cute function "
        "yet. Qt's 'void QCanDbcFileParserPrivate::parseSignalType(const "
        "QStringView data)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'kMaybeSpaceRegExp'.")

  @staticmethod
  def parseValueDescriptions(*__, **_) -> Never:
    """
    Qt's 'void QCanDbcFileParserPrivate::parseValueDescriptions(const
    QStringView data)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'kDbcIdentRegExp'.
    """
    raise NotImplementedError(
        "'QCanDbcFileParserPrivate.parseValueDescriptions' has no cute "
        "function yet. Qt's 'void "
        "QCanDbcFileParserPrivate::parseValueDescriptions(const QStringView "
        "data)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'kDbcIdentRegExp'.")

  @staticmethod
  def postProcessSignalMultiplexing(*__, **_) -> Never:
    """
    Qt's 'void QCanDbcFileParserPrivate::postProcessSignalMultiplexing()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'kQtDummySignal'.
    """
    raise NotImplementedError(
        "'QCanDbcFileParserPrivate.postProcessSignalMultiplexing' has no "
        "cute function yet. Qt's 'void "
        "QCanDbcFileParserPrivate::postProcessSignalMultiplexing()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'kQtDummySignal'.")

  @staticmethod
  def processLine(*__, **_) -> Never:
    """
    Qt's 'bool QCanDbcFileParserPrivate::processLine(const QStringView
    line)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'kMessageDef'.
    """
    raise NotImplementedError(
        "'QCanDbcFileParserPrivate.processLine' has no cute function yet. "
        "Qt's 'bool QCanDbcFileParserPrivate::processLine(const QStringView "
        "line)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'kMessageDef'.")
