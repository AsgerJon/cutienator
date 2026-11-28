"""
QDBusDemarshaller binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusargument_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusDemarshaller to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QDBusArgumentPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QDBusDemarshaller(QDBusArgumentPrivate):
  """
  The cute side of Qt's QDBusDemarshaller: a plain Python object standing in
  front of one C++ QDBusDemarshaller.

  It is built on the cute 'QDBusArgumentPrivate', as Qt's QDBusDemarshaller
  is built on Qt's QDBusArgumentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusDemarshaller that has a ritual and that Python
  can call so far, 1 name in all: 'close'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  43 of the 44 functions Qt declares: 27 leans on 'qdbus_resolve_me(char
  const*)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken; 12 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 forbidden.

  What to expect
  --------------

  - The C++ QDBusDemarshaller is created at the first use, not by
    'QDBusDemarshaller(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusDemarshaller.
  - Each name of Qt's QDBusDemarshaller that has no cute function yet,
    '__init__', 'atEnd', 'beginArray', 'beginCommon', 'beginMap',
    'beginMapEntry', 'beginStructure', 'currentSignature', 'currentType',
    'duplicate', 'endArray', 'endCommon', 'endMap', 'endMapEntry',
    'endStructure', 'isCurrentTypeStringLike', 'toBool', 'toByte',
    'toByteArray', 'toByteArrayUnchecked', 'toDouble', 'toInt', 'toLongLong',
    'toObjectPath', 'toObjectPathUnchecked', 'toShort', 'toSignature',
    'toSignatureUnchecked', 'toString', 'toStringList',
    'toStringListUnchecked', 'toStringUnchecked', 'toUInt', 'toULongLong',
    'toUShort', 'toUnixFileDescriptor', 'toVariant', 'toVariantInternal',
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
  __qt_class__ = 'QDBusDemarshaller'

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
    Qt's 'QDBusDemarshaller::QDBusDemarshaller(QDBusConnection::
    ConnectionCapabilities flags)': leans on 'qdbus_resolve_me(char const*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.__init__' has no cute function yet. Qt's "
        "'QDBusDemarshaller::QDBusDemarshaller(QDBusConnection::ConnectionCa"
        "pabilities flags)': leans on 'qdbus_resolve_me(char const*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def close(self) -> None:
    """
    Calls Qt's 'void QDBusDemarshaller::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusdemarshaller.html#close
    """
    #  void QDBusDemarshaller::close()
    self.uglySide.call('ritual_ZN17QDBusDemarshaller5closeEv')

  @staticmethod
  def atEnd(*__, **_) -> Never:
    """
    Qt's 'bool QDBusDemarshaller::atEnd()': leans on 'qdbus_resolve_me(char
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.atEnd' has no cute function yet. Qt's 'bool "
        "QDBusDemarshaller::atEnd()': leans on 'qdbus_resolve_me(char "
        "const*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def beginArray(*__, **_) -> Never:
    """
    Qt's 'QDBusDemarshaller *QDBusDemarshaller::beginArray()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.beginArray' has no cute function yet. Qt's "
        "'QDBusDemarshaller *QDBusDemarshaller::beginArray()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def beginCommon(*__, **_) -> Never:
    """
    Qt's 'QDBusDemarshaller *QDBusDemarshaller::beginCommon()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.beginCommon' has no cute function yet. Qt's "
        "'QDBusDemarshaller *QDBusDemarshaller::beginCommon()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def beginMap(*__, **_) -> Never:
    """
    Qt's 'QDBusDemarshaller *QDBusDemarshaller::beginMap()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.beginMap' has no cute function yet. Qt's "
        "'QDBusDemarshaller *QDBusDemarshaller::beginMap()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def beginMapEntry(*__, **_) -> Never:
    """
    Qt's 'QDBusDemarshaller *QDBusDemarshaller::beginMapEntry()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.beginMapEntry' has no cute function yet. Qt's "
        "'QDBusDemarshaller *QDBusDemarshaller::beginMapEntry()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def beginStructure(*__, **_) -> Never:
    """
    Qt's 'QDBusDemarshaller *QDBusDemarshaller::beginStructure()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.beginStructure' has no cute function yet. Qt's "
        "'QDBusDemarshaller *QDBusDemarshaller::beginStructure()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def currentSignature(*__, **_) -> Never:
    """
    Qt's 'QString QDBusDemarshaller::currentSignature()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.currentSignature' has no cute function yet. "
        "Qt's 'QString QDBusDemarshaller::currentSignature()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def currentType(*__, **_) -> Never:
    """
    Qt's 'QDBusArgument::ElementType QDBusDemarshaller::currentType()': leans
    on 'qdbus_resolve_me(char const*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.currentType' has no cute function yet. Qt's "
        "'QDBusArgument::ElementType QDBusDemarshaller::currentType()': "
        "leans on 'qdbus_resolve_me(char const*)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def duplicate(*__, **_) -> Never:
    """
    Qt's 'QDBusArgument QDBusDemarshaller::duplicate()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.duplicate' has no cute function yet. Qt's "
        "'QDBusArgument QDBusDemarshaller::duplicate()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def endArray(*__, **_) -> Never:
    """
    Qt's 'QDBusDemarshaller *QDBusDemarshaller::endArray()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.endArray' has no cute function yet. Qt's "
        "'QDBusDemarshaller *QDBusDemarshaller::endArray()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def endCommon(*__, **_) -> Never:
    """
    Qt's 'QDBusDemarshaller *QDBusDemarshaller::endCommon()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.endCommon' has no cute function yet. Qt's "
        "'QDBusDemarshaller *QDBusDemarshaller::endCommon()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def endMap(*__, **_) -> Never:
    """
    Qt's 'QDBusDemarshaller *QDBusDemarshaller::endMap()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.endMap' has no cute function yet. Qt's "
        "'QDBusDemarshaller *QDBusDemarshaller::endMap()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def endMapEntry(*__, **_) -> Never:
    """
    Qt's 'QDBusDemarshaller *QDBusDemarshaller::endMapEntry()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.endMapEntry' has no cute function yet. Qt's "
        "'QDBusDemarshaller *QDBusDemarshaller::endMapEntry()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def endStructure(*__, **_) -> Never:
    """
    Qt's 'QDBusDemarshaller *QDBusDemarshaller::endStructure()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.endStructure' has no cute function yet. Qt's "
        "'QDBusDemarshaller *QDBusDemarshaller::endStructure()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def isCurrentTypeStringLike(*__, **_) -> Never:
    """
    Qt's 'bool QDBusDemarshaller::isCurrentTypeStringLike()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.isCurrentTypeStringLike' has no cute function "
        "yet. Qt's 'bool QDBusDemarshaller::isCurrentTypeStringLike()': "
        "leans on 'qdbus_resolve_me(char const*)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def toBool(*__, **_) -> Never:
    """
    Qt's 'bool QDBusDemarshaller::toBool()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toBool' has no cute function yet. Qt's 'bool "
        "QDBusDemarshaller::toBool()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'qIterGet'.")

  @staticmethod
  def toByte(*__, **_) -> Never:
    """
    Qt's 'uchar QDBusDemarshaller::toByte()': leans on 'qdbus_resolve_me(char
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toByte' has no cute function yet. Qt's 'uchar "
        "QDBusDemarshaller::toByte()': leans on 'qdbus_resolve_me(char "
        "const*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def toByteArray(*__, **_) -> Never:
    """
    Qt's 'QByteArray QDBusDemarshaller::toByteArray()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toByteArray' has no cute function yet. Qt's "
        "'QByteArray QDBusDemarshaller::toByteArray()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def toByteArrayUnchecked(*__, **_) -> Never:
    """
    Qt's 'QByteArray QDBusDemarshaller::toByteArrayUnchecked()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toByteArrayUnchecked' has no cute function yet. "
        "Qt's 'QByteArray QDBusDemarshaller::toByteArrayUnchecked()': leans "
        "on 'qdbus_resolve_me(char const*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def toDouble(*__, **_) -> Never:
    """
    Qt's 'double QDBusDemarshaller::toDouble()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toDouble' has no cute function yet. Qt's "
        "'double QDBusDemarshaller::toDouble()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qIterGet'.")

  @staticmethod
  def toInt(*__, **_) -> Never:
    """
    Qt's 'int QDBusDemarshaller::toInt()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toInt' has no cute function yet. Qt's 'int "
        "QDBusDemarshaller::toInt()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'qIterGet'.")

  @staticmethod
  def toLongLong(*__, **_) -> Never:
    """
    Qt's 'qlonglong QDBusDemarshaller::toLongLong()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toLongLong' has no cute function yet. Qt's "
        "'qlonglong QDBusDemarshaller::toLongLong()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qIterGet'.")

  @staticmethod
  def toObjectPath(*__, **_) -> Never:
    """
    Qt's 'QDBusObjectPath QDBusDemarshaller::toObjectPath()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toObjectPath' has no cute function yet. Qt's "
        "'QDBusObjectPath QDBusDemarshaller::toObjectPath()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def toObjectPathUnchecked(*__, **_) -> Never:
    """
    Qt's 'QDBusObjectPath QDBusDemarshaller::toObjectPathUnchecked()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toObjectPathUnchecked' has no cute function "
        "yet. Qt's 'QDBusObjectPath "
        "QDBusDemarshaller::toObjectPathUnchecked()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qIterGet'.")

  @staticmethod
  def toShort(*__, **_) -> Never:
    """
    Qt's 'short QDBusDemarshaller::toShort()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toShort' has no cute function yet. Qt's 'short "
        "QDBusDemarshaller::toShort()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'qIterGet'.")

  @staticmethod
  def toSignature(*__, **_) -> Never:
    """
    Qt's 'QDBusSignature QDBusDemarshaller::toSignature()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toSignature' has no cute function yet. Qt's "
        "'QDBusSignature QDBusDemarshaller::toSignature()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def toSignatureUnchecked(*__, **_) -> Never:
    """
    Qt's 'QDBusSignature QDBusDemarshaller::toSignatureUnchecked()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toSignatureUnchecked' has no cute function yet. "
        "Qt's 'QDBusSignature QDBusDemarshaller::toSignatureUnchecked()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'qIterGet'.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'QString QDBusDemarshaller::toString()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toString' has no cute function yet. Qt's "
        "'QString QDBusDemarshaller::toString()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def toStringList(*__, **_) -> Never:
    """
    Qt's 'QStringList QDBusDemarshaller::toStringList()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toStringList' has no cute function yet. Qt's "
        "'QStringList QDBusDemarshaller::toStringList()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def toStringListUnchecked(*__, **_) -> Never:
    """
    Qt's 'QStringList QDBusDemarshaller::toStringListUnchecked()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toStringListUnchecked' has no cute function "
        "yet. Qt's 'QStringList "
        "QDBusDemarshaller::toStringListUnchecked()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def toStringUnchecked(*__, **_) -> Never:
    """
    Qt's 'QString QDBusDemarshaller::toStringUnchecked()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toStringUnchecked' has no cute function yet. "
        "Qt's 'QString QDBusDemarshaller::toStringUnchecked()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qIterGet'.")

  @staticmethod
  def toUInt(*__, **_) -> Never:
    """
    Qt's 'uint QDBusDemarshaller::toUInt()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toUInt' has no cute function yet. Qt's 'uint "
        "QDBusDemarshaller::toUInt()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'qIterGet'.")

  @staticmethod
  def toULongLong(*__, **_) -> Never:
    """
    Qt's 'qulonglong QDBusDemarshaller::toULongLong()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toULongLong' has no cute function yet. Qt's "
        "'qulonglong QDBusDemarshaller::toULongLong()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qIterGet'.")

  @staticmethod
  def toUShort(*__, **_) -> Never:
    """
    Qt's 'ushort QDBusDemarshaller::toUShort()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toUShort' has no cute function yet. Qt's "
        "'ushort QDBusDemarshaller::toUShort()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qIterGet'.")

  @staticmethod
  def toUnixFileDescriptor(*__, **_) -> Never:
    """
    Qt's 'QDBusUnixFileDescriptor QDBusDemarshaller::toUnixFileDescriptor()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'qIterGet'.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toUnixFileDescriptor' has no cute function yet. "
        "Qt's 'QDBusUnixFileDescriptor "
        "QDBusDemarshaller::toUnixFileDescriptor()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qIterGet'.")

  @staticmethod
  def toVariant(*__, **_) -> Never:
    """
    Qt's 'QDBusVariant QDBusDemarshaller::toVariant()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toVariant' has no cute function yet. Qt's "
        "'QDBusVariant QDBusDemarshaller::toVariant()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def toVariantInternal(*__, **_) -> Never:
    """
    Qt's 'QVariant QDBusDemarshaller::toVariantInternal()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusDemarshaller.toVariantInternal' has no cute function yet. "
        "Qt's 'QVariant QDBusDemarshaller::toVariantInternal()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
