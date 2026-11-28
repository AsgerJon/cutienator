"""
QV4::JsonParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4jsonobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::JsonParser to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QChar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class JsonParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::JsonParser: a plain Python object standing in
  front of one C++ QV4::JsonParser.

  C++ hands a QV4::JsonParser around as a copy, so every C++ QV4::JsonParser
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::JsonParser that has a ritual and that Python
  can call so far, 1 name in all: 'nextToken'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::JsonParser::~JsonParser()': the destructor: Python removes its
    C++ QV4::JsonParser by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 11 functions Qt declares: 8 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::JsonParser is created at the first use, not by
    'QV4::JsonParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::JsonParser back gives a copy the ritual made for
    Python, in a new cute QV4::JsonParser.
  - Each name of Qt's QV4::JsonParser that has no cute function yet,
    'eatSpace', 'parse', 'parseArray', 'parseMember', 'parseNumber',
    'parseObject', 'parseString', 'parseValue', holds a function that raises
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
  __qt_class__ = 'QV4::JsonParser'

  #  Qt's '~QV4::JsonParser()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::JsonParser behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN3QV410JsonParserD1Ev'

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

  @overload(WAIT['QV4.ExecutionEngine'], QChar, int)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, int)
  @overload(NoneType, QChar, int)
  @overload(NoneType, NoneType, int)
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      json: Optional[QChar],
      length: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::JsonParser::JsonParser(ExecutionEngine *engine, const QChar *json,
    int length)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonparser.html#JsonParser

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    json : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    length : int
      Passed on as it is.
    """
    #  QV4::JsonParser::JsonParser(ExecutionEngine *engine, const QChar
    #      *json, int length)
    self._noteCreation(JsonParser, lambda: Rituals.call(
        'ritual_ZN3QV410JsonParserC1EPNS_15ExecutionEngineEPK5QChari',
        self._addressOf(engine), self._addressOf(json), length,
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

  def nextToken(self) -> QChar:
    """
    Calls Qt's 'QChar QV4::JsonParser::nextToken()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jsonparser.html#nextToken

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QV4::JsonParser::nextToken()
    address = self.uglySide.call('ritual_ZN3QV410JsonParser9nextTokenEv')
    from ..QtCore import QChar
    return QChar._cuteOwning(address)

  @staticmethod
  def eatSpace(*__, **_) -> Never:
    """
    Qt's 'bool QV4::JsonParser::eatSpace()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'Space'.
    """
    raise NotImplementedError(
        "'QV4.JsonParser.eatSpace' has no cute function yet. Qt's 'bool "
        "QV4::JsonParser::eatSpace()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'Space'.")

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::JsonParser::parse(QJsonParseError *error)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'END'.
    """
    raise NotImplementedError(
        "'QV4.JsonParser.parse' has no cute function yet. Qt's "
        "'ReturnedValue QV4::JsonParser::parse(QJsonParseError *error)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'END'.")

  @staticmethod
  def parseArray(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::JsonParser::parseArray()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'BEGIN'.
    """
    raise NotImplementedError(
        "'QV4.JsonParser.parseArray' has no cute function yet. Qt's "
        "'ReturnedValue QV4::JsonParser::parseArray()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'BEGIN'.")

  @staticmethod
  def parseMember(*__, **_) -> Never:
    """
    Qt's 'bool QV4::JsonParser::parseMember(Object *o)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'BEGIN'.
    """
    raise NotImplementedError(
        "'QV4.JsonParser.parseMember' has no cute function yet. Qt's 'bool "
        "QV4::JsonParser::parseMember(Object *o)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'BEGIN'.")

  @staticmethod
  def parseNumber(*__, **_) -> Never:
    """
    Qt's 'bool QV4::JsonParser::parseNumber(Value *val)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'BEGIN'.
    """
    raise NotImplementedError(
        "'QV4.JsonParser.parseNumber' has no cute function yet. Qt's 'bool "
        "QV4::JsonParser::parseNumber(Value *val)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'BEGIN'.")

  @staticmethod
  def parseObject(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::JsonParser::parseObject()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'Quote'.
    """
    raise NotImplementedError(
        "'QV4.JsonParser.parseObject' has no cute function yet. Qt's "
        "'ReturnedValue QV4::JsonParser::parseObject()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'Quote'.")

  @staticmethod
  def parseString(*__, **_) -> Never:
    """
    Qt's 'bool QV4::JsonParser::parseString(QString *string)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'BEGIN'.
    """
    raise NotImplementedError(
        "'QV4.JsonParser.parseString' has no cute function yet. Qt's 'bool "
        "QV4::JsonParser::parseString(QString *string)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'BEGIN'.")

  @staticmethod
  def parseValue(*__, **_) -> Never:
    """
    Qt's 'bool QV4::JsonParser::parseValue(Value *val)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'BEGIN'.
    """
    raise NotImplementedError(
        "'QV4.JsonParser.parseValue' has no cute function yet. Qt's 'bool "
        "QV4::JsonParser::parseValue(Value *val)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'BEGIN'.")
