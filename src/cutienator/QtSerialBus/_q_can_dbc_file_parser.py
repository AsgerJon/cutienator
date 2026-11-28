"""
QCanDbcFileParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qcandbcfileparser.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from ..QtCore import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QCanMessageDescription, QCanUniqueIdDescription


class QCanDbcFileParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanDbcFileParser: a plain Python object standing in
  front of one C++ QCanDbcFileParser.

  What exists
  -----------

  Every function of Qt's QCanDbcFileParser that has a ritual and that Python
  can call so far, 7 names in all: 'parse', 'parseData',
  'messageDescriptions', 'error', 'errorString', 'warnings',
  'uniqueIdDescription'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanDbcFileParser::~QCanDbcFileParser()': the destructor: Python
    never removes a C++ QCanDbcFileParser.
  - Qt's 'MessageValueDescriptions
    QCanDbcFileParser::messageValueDescriptions() const': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QCanDbcFileParser is created at the first use, not by
    'QCanDbcFileParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanDbcFileParser.
  - Each name of Qt's QCanDbcFileParser that has no cute function yet,
    'messageValueDescriptions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QCanDbcFileParser, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum, scoped=True):
    """
    The enum 'QCanDbcFileParser::Error' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    FileReading = Kee[int](1)
    Parsing = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def uniqueIdDescription() -> QCanUniqueIdDescription:
    """
    Calls Qt's 'QCanUniqueIdDescription
    QCanDbcFileParser::uniqueIdDescription()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandbcfileparser.html#uniqueIdDescription

    Returns
    -------

    QCanUniqueIdDescription
      A new cute QCanUniqueIdDescription around the copy Qt gave back. Python
      owns it.
    """
    #  QCanUniqueIdDescription QCanDbcFileParser::uniqueIdDescription()
    address = Rituals.call(
        'ritual_ZN17QCanDbcFileParser19uniqueIdDescriptionEv',
    )
    from . import QCanUniqueIdDescription
    return QCanUniqueIdDescription._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanDbcFileParser'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def messageDescriptions(self) -> QList[QCanMessageDescription]:
    """
    Calls Qt's 'QList<QCanMessageDescription>
    QCanDbcFileParser::messageDescriptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandbcfileparser.html#messageDescriptions

    Returns
    -------

    QList[QCanMessageDescription]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCanMessageDescription> QCanDbcFileParser::messageDescriptions()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QCanDbcFileParser19messageDescriptionsEv',
    )
    from . import QCanMessageDescription
    return QList[QCanMessageDescription]._cuteOwning(address)

  def error(self) -> Error:
    """
    Calls Qt's 'Error QCanDbcFileParser::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandbcfileparser.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QCanDbcFileParser::error() const
    return QCanDbcFileParser.Error(self.uglySide.call(
        'ritual_ZNK17QCanDbcFileParser5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QCanDbcFileParser::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandbcfileparser.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanDbcFileParser::errorString() const
    return self.uglySide.call('ritual_ZNK17QCanDbcFileParser11errorStringEv')

  def warnings(self) -> QStringList:
    """
    Calls Qt's 'QStringList QCanDbcFileParser::warnings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcandbcfileparser.html#warnings

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCanDbcFileParser::warnings() const
    address = self.uglySide.call('ritual_ZNK17QCanDbcFileParser8warningsEv')
    return QStringList._cuteOwning(address)

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
    Notes what was given, for Qt's 'QCanDbcFileParser::QCanDbcFileParser()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcandbcfileparser.html#QCanDbcFileParser
    """
    #  QCanDbcFileParser::QCanDbcFileParser()
    self._noteCreation(QCanDbcFileParser, lambda: Rituals.call(
        'ritual_ZN17QCanDbcFileParserC1Ev',
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

  @overload(str)
  def parse(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool QCanDbcFileParser::parse(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandbcfileparser.html#parse

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QCanDbcFileParser::parse(const QString &fileName)
    return self.uglySide.call(
        'ritual_ZN17QCanDbcFileParser5parseERK7QString', fileName,
    )

  @overload(QStringList)
  def parse(self, fileNames: QStringList) -> bool:
    """
    Calls Qt's 'bool QCanDbcFileParser::parse(const QStringList &fileNames)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandbcfileparser.html#parse

    Parameters
    ----------

    fileNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QCanDbcFileParser::parse(const QStringList &fileNames)
    return self.uglySide.call(
        'ritual_ZN17QCanDbcFileParser5parseERK5QListI7QStringE',
        self._valueOf(fileNames),
    )

  @overload(str)
  def parseData(self, data: str) -> bool:
    """
    Calls Qt's 'bool QCanDbcFileParser::parseData(QStringView data)'.

    Qt's own words: https://doc.qt.io/qt-6/qcandbcfileparser.html#parseData

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QCanDbcFileParser::parseData(QStringView data)
    return self.uglySide.call(
        'ritual_ZN17QCanDbcFileParser9parseDataE11QStringView', data,
    )

  @staticmethod
  def messageValueDescriptions(*__, **_) -> Never:
    """
    Qt's 'MessageValueDescriptions
    QCanDbcFileParser::messageValueDescriptions() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QCanDbcFileParser.messageValueDescriptions' has no cute function "
        "yet. Qt's 'MessageValueDescriptions "
        "QCanDbcFileParser::messageValueDescriptions() const': gives a type "
        "Python has no way to take yet.")
