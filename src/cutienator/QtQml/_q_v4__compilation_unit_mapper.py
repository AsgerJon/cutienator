"""
QV4::CompilationUnitMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compilationunitmapper_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QV4::CompilationUnitMapper to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class CompilationUnitMapper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompilationUnitMapper: a plain Python object
  standing in front of one C++ QV4::CompilationUnitMapper.

  C++ hands a QV4::CompilationUnitMapper around as a copy, so every C++
  QV4::CompilationUnitMapper behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QV4::CompilationUnitMapper yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompilationUnitMapper::~CompilationUnitMapper()': the
    destructor: Python removes its C++ QV4::CompilationUnitMapper by it, and
    has no other use for it.

  What has no ritual
  ------------------

  4 of the 5 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::CompilationUnitMapper is created at the first use, not by
    'QV4::CompilationUnitMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompilationUnitMapper back gives a copy the
    ritual made for Python, in a new cute QV4::CompilationUnitMapper.
  - Each name of Qt's QV4::CompilationUnitMapper that has no cute function
    yet, 'close', 'get', 'invalidate', 'open', holds a function that raises
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
  __qt_class__ = 'QV4::CompilationUnitMapper'

  #  Qt's '~QV4::CompilationUnitMapper()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::CompilationUnitMapper behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV421CompilationUnitMapperD1Ev'

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
  def close(*__, **_) -> Never:
    """
    Qt's 'void QV4::CompilationUnitMapper::close()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QV4.CompilationUnitMapper.close' has no cute function yet. Qt's "
        "'void QV4::CompilationUnitMapper::close()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'CompiledData::Unit *QV4::CompilationUnitMapper::get(const QString
    &cacheFilePath, const QDateTime &sourceTimeStamp, QString *errorString)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'StaticUnitCache'.
    """
    raise NotImplementedError(
        "'QV4.CompilationUnitMapper.get' has no cute function yet. Qt's "
        "'CompiledData::Unit *QV4::CompilationUnitMapper::get(const QString "
        "&cacheFilePath, const QDateTime &sourceTimeStamp, QString "
        "*errorString)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: unknown type "
        "name 'StaticUnitCache'.")

  @staticmethod
  def invalidate(*__, **_) -> Never:
    """
    Qt's 'void QV4::CompilationUnitMapper::invalidate(const QString
    &cacheFilePath)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: unknown type name
    'StaticUnitCache'.
    """
    raise NotImplementedError(
        "'QV4.CompilationUnitMapper.invalidate' has no cute function yet. "
        "Qt's 'void QV4::CompilationUnitMapper::invalidate(const QString "
        "&cacheFilePath)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: unknown type "
        "name 'StaticUnitCache'.")

  @staticmethod
  def open(*__, **_) -> Never:
    """
    Qt's 'CompiledData::Unit *QV4::CompilationUnitMapper::open(const QString
    &cacheFilePath, const QDateTime &sourceTimeStamp, QString *errorString)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QV4.CompilationUnitMapper.open' has no cute function yet. Qt's "
        "'CompiledData::Unit *QV4::CompilationUnitMapper::open(const "
        "QString &cacheFilePath, const QDateTime &sourceTimeStamp, QString "
        "*errorString)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
