"""
QDBusMarshaller binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusargument_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusMarshaller to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QDBusArgumentPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QMetaType, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QVariant = WAIT['QVariant']


class QDBusMarshaller(QDBusArgumentPrivate):
  """
  The cute side of Qt's QDBusMarshaller: a plain Python object standing in
  front of one C++ QDBusMarshaller.

  It is built on the cute 'QDBusArgumentPrivate', as Qt's QDBusMarshaller is
  built on Qt's QDBusArgumentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusMarshaller that has a ritual and that Python
  can call so far, 3 names in all: 'error', 'appendRegisteredType',
  'unregisteredTypeError'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  37 of the 40 functions Qt declares: 21 leans on 'qdbus_resolve_me(char
  const*)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken; 12 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 forbidden.

  What to expect
  --------------

  - The C++ QDBusMarshaller is created at the first use, not by
    'QDBusMarshaller(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusMarshaller.
  - Each name of Qt's QDBusMarshaller that has no cute function yet,
    '__init__', 'append', 'appendCrossMarshalling', 'appendVariantInternal',
    'beginArray', 'beginCommon', 'beginMap', 'beginMapEntry',
    'beginStructure', 'close', 'currentSignature', 'endArray', 'endCommon',
    'endMap', 'endMapEntry', 'endStructure', 'open', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusMarshaller'

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
    Qt's
    'QDBusMarshaller::QDBusMarshaller(QDBusConnection::ConnectionCapabilities
    flags)': leans on 'qdbus_resolve_me(char const*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.__init__' has no cute function yet. Qt's "
        "'QDBusMarshaller::QDBusMarshaller(QDBusConnection::ConnectionCapabi"
        "lities flags)': leans on 'qdbus_resolve_me(char const*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
  def error(self, message: str) -> None:
    """
    Calls Qt's 'void QDBusMarshaller::error(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusmarshaller.html#error

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusMarshaller::error(const QString &message)
    self.uglySide.call(
        'ritual_ZN15QDBusMarshaller5errorERK7QString', message,
    )

  @overload(QVariant)
  def appendRegisteredType(self, arg: QVariant) -> bool:
    """
    Calls Qt's 'bool QDBusMarshaller::appendRegisteredType(const QVariant
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmarshaller.html#appendRegisteredType

    Parameters
    ----------

    arg : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QDBusMarshaller::appendRegisteredType(const QVariant &arg)
    return self.uglySide.call(
        'ritual_ZN15QDBusMarshaller20appendRegisteredTypeERK8QVariant',
        self._valueOf(arg),
    )

  @overload(QMetaType)
  def unregisteredTypeError(self, t: QMetaType) -> None:
    """
    Calls Qt's 'void QDBusMarshaller::unregisteredTypeError(QMetaType t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmarshaller.html#unregisteredTypeError

    Parameters
    ----------

    t : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QDBusMarshaller::unregisteredTypeError(QMetaType t)
    self.uglySide.call(
        'ritual_ZN15QDBusMarshaller21unregisteredTypeErrorE9QMetaType',
        self._valueOf(t),
    )

  @staticmethod
  def append(*__, **_) -> Never:
    """
    - Qt's 'void QDBusMarshaller::append(bool arg)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(short arg)': Qt's library has no
      name for it, and its code in Qt's source does not compile apart from
      its file: use of undeclared identifier 'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(ushort arg)': Qt's library has no
      name for it, and its code in Qt's source does not compile apart from
      its file: use of undeclared identifier 'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(int arg)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(uint arg)': Qt's library has no name
      for it, and its code in Qt's source does not compile apart from its
      file: use of undeclared identifier 'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(qlonglong arg)': Qt's library has no
      name for it, and its code in Qt's source does not compile apart from
      its file: use of undeclared identifier 'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(qulonglong arg)': Qt's library has
      no name for it, and its code in Qt's source does not compile apart from
      its file: use of undeclared identifier 'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(double arg)': Qt's library has no
      name for it, and its code in Qt's source does not compile apart from
      its file: use of undeclared identifier 'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(const QString &arg)': Qt's library
      has no name for it, and its code in Qt's source does not compile apart
      from its file: use of undeclared identifier 'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(const QDBusObjectPath &arg)': Qt's
      library has no name for it, and its code in Qt's source does not
      compile apart from its file: use of undeclared identifier
      'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(const QDBusSignature &arg)': Qt's
      library has no name for it, and its code in Qt's source does not
      compile apart from its file: use of undeclared identifier
      'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(const QDBusUnixFileDescriptor
      &arg)': Qt's library has no name for it, and its code in Qt's source
      does not compile apart from its file: use of undeclared identifier
      'qIterAppend'.
    - Qt's 'void QDBusMarshaller::append(uchar arg)': leans on
      'qdbus_resolve_me(char const*)', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    - Qt's 'void QDBusMarshaller::append(const QStringList &arg)': leans on
      'qdbus_resolve_me(char const*)', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    - Qt's 'void QDBusMarshaller::append(const QByteArray &arg)': leans on
      'qdbus_resolve_me(char const*)', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    - Qt's 'bool QDBusMarshaller::append(const QDBusVariant &arg)': leans on
      'qdbus_resolve_me(char const*)', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.append' has no cute function yet. Qt's 'void "
        "QDBusMarshaller::append(bool arg)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'qIterAppend'. Qt's 'void "
        "QDBusMarshaller::append(short arg)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'qIterAppend'. Qt's 'void "
        "QDBusMarshaller::append(ushort arg)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'qIterAppend'. Qt's 'void "
        "QDBusMarshaller::append(int arg)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'qIterAppend'. Qt's 'void "
        "QDBusMarshaller::append(uint arg)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'qIterAppend'. Qt's 'void "
        "QDBusMarshaller::append(qlonglong arg)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qIterAppend'. Qt's 'void "
        "QDBusMarshaller::append(qulonglong arg)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qIterAppend'. Qt's 'void "
        "QDBusMarshaller::append(double arg)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier 'qIterAppend'. Qt's 'void "
        "QDBusMarshaller::append(const QString &arg)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qIterAppend'. Qt's "
        "'void QDBusMarshaller::append(const QDBusObjectPath &arg)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qIterAppend'. Qt's 'void QDBusMarshaller::append(const "
        "QDBusSignature &arg)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qIterAppend'. Qt's 'void "
        "QDBusMarshaller::append(const QDBusUnixFileDescriptor &arg)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qIterAppend'. Qt's 'void QDBusMarshaller::append(uchar arg)': "
        "leans on 'qdbus_resolve_me(char const*)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'void QDBusMarshaller::append(const QStringList "
        "&arg)': leans on 'qdbus_resolve_me(char const*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken. Qt's 'void QDBusMarshaller::append(const "
        "QByteArray &arg)': leans on 'qdbus_resolve_me(char const*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's 'bool QDBusMarshaller::append(const "
        "QDBusVariant &arg)': leans on 'qdbus_resolve_me(char const*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def appendCrossMarshalling(*__, **_) -> Never:
    """
    Qt's 'bool QDBusMarshaller::appendCrossMarshalling(QDBusDemarshaller
    *arg)': leans on 'qdbus_resolve_me(char const*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.appendCrossMarshalling' has no cute function yet. "
        "Qt's 'bool "
        "QDBusMarshaller::appendCrossMarshalling(QDBusDemarshaller *arg)': "
        "leans on 'qdbus_resolve_me(char const*)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def appendVariantInternal(*__, **_) -> Never:
    """
    Qt's 'bool QDBusMarshaller::appendVariantInternal(const QVariant &arg)':
    leans on 'qdbus_resolve_me(char const*)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.appendVariantInternal' has no cute function yet. "
        "Qt's 'bool QDBusMarshaller::appendVariantInternal(const QVariant "
        "&arg)': leans on 'qdbus_resolve_me(char const*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def beginArray(*__, **_) -> Never:
    """
    Qt's 'QDBusMarshaller *QDBusMarshaller::beginArray(QMetaType id)': leans
    on 'qdbus_resolve_me(char const*)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.beginArray' has no cute function yet. Qt's "
        "'QDBusMarshaller *QDBusMarshaller::beginArray(QMetaType id)': "
        "leans on 'qdbus_resolve_me(char const*)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def beginCommon(*__, **_) -> Never:
    """
    Qt's 'QDBusMarshaller *QDBusMarshaller::beginCommon(int code, const char
    *signature)': leans on 'qdbus_resolve_me(char const*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.beginCommon' has no cute function yet. Qt's "
        "'QDBusMarshaller *QDBusMarshaller::beginCommon(int code, const "
        "char *signature)': leans on 'qdbus_resolve_me(char const*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def beginMap(*__, **_) -> Never:
    """
    Qt's 'QDBusMarshaller *QDBusMarshaller::beginMap(QMetaType kid, QMetaType
    vid)': leans on 'qdbus_resolve_me(char const*)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.beginMap' has no cute function yet. Qt's "
        "'QDBusMarshaller *QDBusMarshaller::beginMap(QMetaType kid, "
        "QMetaType vid)': leans on 'qdbus_resolve_me(char const*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def beginMapEntry(*__, **_) -> Never:
    """
    Qt's 'QDBusMarshaller *QDBusMarshaller::beginMapEntry()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.beginMapEntry' has no cute function yet. Qt's "
        "'QDBusMarshaller *QDBusMarshaller::beginMapEntry()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def beginStructure(*__, **_) -> Never:
    """
    Qt's 'QDBusMarshaller *QDBusMarshaller::beginStructure()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.beginStructure' has no cute function yet. Qt's "
        "'QDBusMarshaller *QDBusMarshaller::beginStructure()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def close(*__, **_) -> Never:
    """
    Qt's 'void QDBusMarshaller::close()': leans on 'qdbus_resolve_me(char
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.close' has no cute function yet. Qt's 'void "
        "QDBusMarshaller::close()': leans on 'qdbus_resolve_me(char "
        "const*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def currentSignature(*__, **_) -> Never:
    """
    Qt's 'QString QDBusMarshaller::currentSignature()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.currentSignature' has no cute function yet. Qt's "
        "'QString QDBusMarshaller::currentSignature()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def endArray(*__, **_) -> Never:
    """
    Qt's 'QDBusMarshaller *QDBusMarshaller::endArray()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.endArray' has no cute function yet. Qt's "
        "'QDBusMarshaller *QDBusMarshaller::endArray()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def endCommon(*__, **_) -> Never:
    """
    Qt's 'QDBusMarshaller *QDBusMarshaller::endCommon()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.endCommon' has no cute function yet. Qt's "
        "'QDBusMarshaller *QDBusMarshaller::endCommon()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def endMap(*__, **_) -> Never:
    """
    Qt's 'QDBusMarshaller *QDBusMarshaller::endMap()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.endMap' has no cute function yet. Qt's "
        "'QDBusMarshaller *QDBusMarshaller::endMap()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def endMapEntry(*__, **_) -> Never:
    """
    Qt's 'QDBusMarshaller *QDBusMarshaller::endMapEntry()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.endMapEntry' has no cute function yet. Qt's "
        "'QDBusMarshaller *QDBusMarshaller::endMapEntry()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def endStructure(*__, **_) -> Never:
    """
    Qt's 'QDBusMarshaller *QDBusMarshaller::endStructure()': leans on
    'qdbus_resolve_me(char const*)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.endStructure' has no cute function yet. Qt's "
        "'QDBusMarshaller *QDBusMarshaller::endStructure()': leans on "
        "'qdbus_resolve_me(char const*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def open(*__, **_) -> Never:
    """
    Qt's 'void QDBusMarshaller::open(QDBusMarshaller &sub, int code, const
    char *signature)': leans on 'qdbus_resolve_me(char const*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QDBusMarshaller.open' has no cute function yet. Qt's 'void "
        "QDBusMarshaller::open(QDBusMarshaller &sub, int code, const char "
        "*signature)': leans on 'qdbus_resolve_me(char const*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
