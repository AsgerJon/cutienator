"""
QQmlImportInstance binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlimport_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlImportInstance to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlImportInstance(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlImportInstance: a plain Python object standing in
  front of one C++ QQmlImportInstance.

  C++ hands a QQmlImportInstance around as a copy, so every C++
  QQmlImportInstance behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlImportInstance yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDirScripts QQmlImportInstance::getVersionedScripts(const
    QQmlDirScripts &qmldirscripts, QTypeRevision version)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlImportInstance::~QQmlImportInstance()': the destructor: Python
    removes its C++ QQmlImportInstance by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQmlImportInstance is created at the first use, not by
    'QQmlImportInstance(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlImportInstance back gives a copy the ritual made
    for Python, in a new cute QQmlImportInstance.
  - Each name of Qt's QQmlImportInstance that has no cute function yet,
    'getVersionedScripts', 'resolveType', 'setQmldirContent', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlImportInstance, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Precedence(CuteNum):
    """
    The enum 'QQmlImportInstance::Precedence' of Qt, with the 3 names Qt
    gives in it.
    """

    Lowest = Kee[int](255)
    Implicit = Kee[int](127)
    Highest = Kee[int](0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlImportInstance'

  #  Qt's '~QQmlImportInstance()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlImportInstance behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlImportInstanceD1Ev'

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

  @staticmethod
  def getVersionedScripts(*__, **_) -> Never:
    """
    Qt's 'QQmlDirScripts QQmlImportInstance::getVersionedScripts(const
    QQmlDirScripts &qmldirscripts, QTypeRevision version)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlImportInstance.getVersionedScripts' has no cute function yet. "
        "Qt's 'QQmlDirScripts QQmlImportInstance::getVersionedScripts(const "
        "QQmlDirScripts &qmldirscripts, QTypeRevision version)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def resolveType(*__, **_) -> Never:
    """
    Qt's 'bool QQmlImportInstance::resolveType(QQmlTypeLoader *typeLoader,
    const QHashedStringRef &type, QTypeRevision *version_return, QQmlType
    *type_return, const QString *base, bool *typeRecursionDetected,
    QQmlType::RegistrationType a6, QQmlImport::RecursionRestriction
    recursionRestriction, QList<QQmlError> *errors) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'dotqml_string'.
    """
    raise NotImplementedError(
        "'QQmlImportInstance.resolveType' has no cute function yet. Qt's "
        "'bool QQmlImportInstance::resolveType(QQmlTypeLoader *typeLoader, "
        "const QHashedStringRef &type, QTypeRevision *version_return, "
        "QQmlType *type_return, const QString *base, bool "
        "*typeRecursionDetected, QQmlType::RegistrationType a6, "
        "QQmlImport::RecursionRestriction recursionRestriction, "
        "QList<QQmlError> *errors) const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'dotqml_string'.")

  @staticmethod
  def setQmldirContent(*__, **_) -> Never:
    """
    Qt's 'bool QQmlImportInstance::setQmldirContent(const QString
    &resolvedUrl, const QQmlTypeLoaderQmldirContent &qmldir,
    QQmlImportNamespace *nameSpace, QList<QQmlError> *errors)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'Slash'.
    """
    raise NotImplementedError(
        "'QQmlImportInstance.setQmldirContent' has no cute function yet. "
        "Qt's 'bool QQmlImportInstance::setQmldirContent(const QString "
        "&resolvedUrl, const QQmlTypeLoaderQmldirContent &qmldir, "
        "QQmlImportNamespace *nameSpace, QList<QQmlError> *errors)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'Slash'.")
