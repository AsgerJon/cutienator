"""
QDBusXmlParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusxmlparser_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusXmlParser to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QDBusXmlParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusXmlParser: a plain Python object standing in
  front of one C++ QDBusXmlParser.

  What exists
  -----------

  Every function of Qt's QDBusXmlParser that has a ritual and that Python can
  call so far, 2 names in all: 'readNextStartElement',
  'updateCurrentLocation'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusIntrospection::Interfaces QDBusXmlParser::interfaces() const':
    gives a type Python has no way to take yet.
  - Qt's 'QSharedDataPointer<QDBusIntrospection::Object>
    QDBusXmlParser::object() const': gives a type Python has no way to take
    yet.

  What has no ritual
  ------------------

  8 of the 12 functions Qt declares: 8 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QDBusXmlParser is created at the first use, not by
    'QDBusXmlParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusXmlParser.
  - Each name of Qt's QDBusXmlParser that has no cute function yet,
    '__init__', 'interfaces', 'object', 'parseAnnotation', 'parseArg',
    'parseMethod', 'parseProperty', 'parseSignal', 'readInterface',
    'readNode', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QDBusXmlParser'

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
    Qt's 'QDBusXmlParser::QDBusXmlParser(const QString &service, const
    QString &path, const QString &xmlData,
    QDBusIntrospection::DiagnosticsReporter *reporter)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'qDBusParserError'; did you mean
    'QCborParserError'?.
    """
    raise NotImplementedError(
        "'QDBusXmlParser.__init__' has no cute function yet. Qt's "
        "'QDBusXmlParser::QDBusXmlParser(const QString &service, const "
        "QString &path, const QString &xmlData, "
        "QDBusIntrospection::DiagnosticsReporter *reporter)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'qDBusParserError'; did you mean 'QCborParserError'?.")

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

  def readNextStartElement(self) -> bool:
    """
    Calls Qt's 'bool QDBusXmlParser::readNextStartElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusxmlparser.html#readNextStartElement
    """
    #  bool QDBusXmlParser::readNextStartElement()
    return self.uglySide.call(
        'ritual_ZN14QDBusXmlParser20readNextStartElementEv',
    )

  def updateCurrentLocation(self) -> None:
    """
    Calls Qt's 'void QDBusXmlParser::updateCurrentLocation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusxmlparser.html#updateCurrentLocation
    """
    #  void QDBusXmlParser::updateCurrentLocation()
    self.uglySide.call('ritual_ZN14QDBusXmlParser21updateCurrentLocationEv')

  @staticmethod
  def interfaces(*__, **_) -> Never:
    """
    Qt's 'QDBusIntrospection::Interfaces QDBusXmlParser::interfaces() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusXmlParser.interfaces' has no cute function yet. Qt's "
        "'QDBusIntrospection::Interfaces QDBusXmlParser::interfaces() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def object(*__, **_) -> Never:
    """
    Qt's 'QSharedDataPointer<QDBusIntrospection::Object>
    QDBusXmlParser::object() const': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QDBusXmlParser.object' has no cute function yet. Qt's "
        "'QSharedDataPointer<QDBusIntrospection::Object> "
        "QDBusXmlParser::object() const': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def parseAnnotation(*__, **_) -> Never:
    """
    Qt's 'bool
    QDBusXmlParser::parseAnnotation(QDBusIntrospection::Annotations
    &annotations, bool interfaceAnnotation)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qDBusParserError'; did you mean
    'QCborParserError'?.
    """
    raise NotImplementedError(
        "'QDBusXmlParser.parseAnnotation' has no cute function yet. Qt's "
        "'bool "
        "QDBusXmlParser::parseAnnotation(QDBusIntrospection::Annotations "
        "&annotations, bool interfaceAnnotation)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qDBusParserError'; did you "
        "mean 'QCborParserError'?.")

  @staticmethod
  def parseArg(*__, **_) -> Never:
    """
    Qt's 'bool QDBusXmlParser::parseArg(const QXmlStreamAttributes
    &attributes, QDBusIntrospection::Argument &argData)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'qDBusParserError'; did you mean
    'QCborParserError'?.
    """
    raise NotImplementedError(
        "'QDBusXmlParser.parseArg' has no cute function yet. Qt's 'bool "
        "QDBusXmlParser::parseArg(const QXmlStreamAttributes &attributes, "
        "QDBusIntrospection::Argument &argData)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qDBusParserError'; did you "
        "mean 'QCborParserError'?.")

  @staticmethod
  def parseMethod(*__, **_) -> Never:
    """
    Qt's 'bool QDBusXmlParser::parseMethod(QDBusIntrospection::Method
    &methodData)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'qDBusParserError'; did you mean 'QCborParserError'?.
    """
    raise NotImplementedError(
        "'QDBusXmlParser.parseMethod' has no cute function yet. Qt's 'bool "
        "QDBusXmlParser::parseMethod(QDBusIntrospection::Method "
        "&methodData)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qDBusParserError'; did you mean "
        "'QCborParserError'?.")

  @staticmethod
  def parseProperty(*__, **_) -> Never:
    """
    Qt's 'bool QDBusXmlParser::parseProperty(QDBusIntrospection::Property
    &propertyData)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'qDBusParserWarning'.
    """
    raise NotImplementedError(
        "'QDBusXmlParser.parseProperty' has no cute function yet. Qt's "
        "'bool QDBusXmlParser::parseProperty(QDBusIntrospection::Property "
        "&propertyData)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qDBusParserWarning'.")

  @staticmethod
  def parseSignal(*__, **_) -> Never:
    """
    Qt's 'bool QDBusXmlParser::parseSignal(QDBusIntrospection::Signal
    &signalData)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'qDBusParserError'; did you mean 'QCborParserError'?.
    """
    raise NotImplementedError(
        "'QDBusXmlParser.parseSignal' has no cute function yet. Qt's 'bool "
        "QDBusXmlParser::parseSignal(QDBusIntrospection::Signal "
        "&signalData)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qDBusParserError'; did you mean "
        "'QCborParserError'?.")

  @staticmethod
  def readInterface(*__, **_) -> Never:
    """
    Qt's 'void QDBusXmlParser::readInterface()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qDBusParserError'; did you mean
    'QCborParserError'?.
    """
    raise NotImplementedError(
        "'QDBusXmlParser.readInterface' has no cute function yet. Qt's "
        "'void QDBusXmlParser::readInterface()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qDBusParserError'; did you "
        "mean 'QCborParserError'?.")

  @staticmethod
  def readNode(*__, **_) -> Never:
    """
    Qt's 'void QDBusXmlParser::readNode(int nodeLevel)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'qDBusParserError'; did you mean
    'QCborParserError'?.
    """
    raise NotImplementedError(
        "'QDBusXmlParser.readNode' has no cute function yet. Qt's 'void "
        "QDBusXmlParser::readNode(int nodeLevel)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qDBusParserError'; did you "
        "mean 'QCborParserError'?.")
