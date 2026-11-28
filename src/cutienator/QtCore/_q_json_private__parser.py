"""
QJsonPrivate::Parser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qjsonparser_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QJsonPrivate::Parser to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QCborValue


class Parser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJsonPrivate::Parser: a plain Python object standing
  in front of one C++ QJsonPrivate::Parser.

  What exists
  -----------

  Every function of Qt's QJsonPrivate::Parser that has a ritual and that
  Python can call so far, 2 names in all: 'eatBOM', 'parseNumber'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QJsonPrivate::Parser::Parser(QUtf8StringView json)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  10 of the 13 functions Qt declares: 7 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QJsonPrivate; 1 leans on
  'QExplicitlySharedDataPointer<QCborContainerPrivate>.

  What to expect
  --------------

  - The C++ QJsonPrivate::Parser is created at the first use, not by
    'QJsonPrivate::Parser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QJsonPrivate::Parser.
  - Each name of Qt's QJsonPrivate::Parser that has no cute function yet,
    '__init__', 'eatSpace', 'nextToken', 'parse', 'parseArray',
    'parseMember', 'parseObject', 'parseString', 'parseValue',
    'parseValueIntoContainer', holds a function that raises
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
  __qt_class__ = 'QJsonPrivate::Parser'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QJsonPrivate::Parser::Parser(QUtf8StringView json)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Parser.__init__' has no cute function yet. Qt's "
        "'QJsonPrivate::Parser::Parser(QUtf8StringView json)': takes a type "
        "Python has no way to hand over yet.")

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

  def eatBOM(self) -> None:
    """
    Calls Qt's 'void QJsonPrivate::Parser::eatBOM()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsonprivate-parser.html#eatBOM
    """
    #  void QJsonPrivate::Parser::eatBOM()
    self.uglySide.call('ritual_ZN12QJsonPrivate6Parser6eatBOMEv')

  def parseNumber(self) -> QCborValue:
    """
    Calls Qt's 'QCborValue QJsonPrivate::Parser::parseNumber()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsonprivate-parser.html#parseNumber

    Returns
    -------

    QCborValue
      A new cute QCborValue around the copy Qt gave back. Python owns it.
    """
    #  QCborValue QJsonPrivate::Parser::parseNumber()
    address = self.uglySide.call(
        'ritual_ZN12QJsonPrivate6Parser11parseNumberEv',
    )
    from . import QCborValue
    return QCborValue._cuteOwning(address)

  @staticmethod
  def eatSpace(*__, **_) -> Never:
    """
    Qt's 'bool QJsonPrivate::Parser::eatSpace()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'Space'.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Parser.eatSpace' has no cute function yet. Qt's "
        "'bool QJsonPrivate::Parser::eatSpace()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'Space'.")

  @staticmethod
  def nextToken(*__, **_) -> Never:
    """
    Qt's 'char QJsonPrivate::Parser::nextToken()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'Quote'.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Parser.nextToken' has no cute function yet. Qt's "
        "'char QJsonPrivate::Parser::nextToken()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'Quote'.")

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    Qt's 'QCborValue QJsonPrivate::Parser::parse(QJsonParseError *error)':
    leans on 'QJsonPrivate::Parser::parseValue()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Parser.parse' has no cute function yet. Qt's "
        "'QCborValue QJsonPrivate::Parser::parse(QJsonParseError *error)': "
        "leans on 'QJsonPrivate::Parser::parseValue()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def parseArray(*__, **_) -> Never:
    """
    Qt's 'bool QJsonPrivate::Parser::parseArray()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'nestingLimit'; did you mean
    'nestingLevel'?.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Parser.parseArray' has no cute function yet. Qt's "
        "'bool QJsonPrivate::Parser::parseArray()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'nestingLimit'; did "
        "you mean 'nestingLevel'?.")

  @staticmethod
  def parseMember(*__, **_) -> Never:
    """
    Qt's 'bool QJsonPrivate::Parser::parseMember()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'NameSeparator'.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Parser.parseMember' has no cute function yet. Qt's "
        "'bool QJsonPrivate::Parser::parseMember()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'NameSeparator'.")

  @staticmethod
  def parseObject(*__, **_) -> Never:
    """
    Qt's 'bool QJsonPrivate::Parser::parseObject()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'Quote'.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Parser.parseObject' has no cute function yet. Qt's "
        "'bool QJsonPrivate::Parser::parseObject()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'Quote'.")

  @staticmethod
  def parseString(*__, **_) -> Never:
    """
    Qt's 'bool QJsonPrivate::Parser::parseString()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'scanUtf8Char'.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Parser.parseString' has no cute function yet. Qt's "
        "'bool QJsonPrivate::Parser::parseString()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'scanUtf8Char'.")

  @staticmethod
  def parseValue(*__, **_) -> Never:
    """
    Qt's 'QCborValue QJsonPrivate::Parser::parseValue()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'Quote'.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Parser.parseValue' has no cute function yet. Qt's "
        "'QCborValue QJsonPrivate::Parser::parseValue()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'Quote'.")

  @staticmethod
  def parseValueIntoContainer(*__, **_) -> Never:
    """
    Qt's 'bool QJsonPrivate::Parser::parseValueIntoContainer()': leans on
    'QJsonPrivate::Parser::parseValue()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QJsonPrivate.Parser.parseValueIntoContainer' has no cute function "
        "yet. Qt's 'bool QJsonPrivate::Parser::parseValueIntoContainer()': "
        "leans on 'QJsonPrivate::Parser::parseValue()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
