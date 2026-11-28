"""
QQmlJS::Directives binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlJS::Directives to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute


class Directives(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::Directives: a plain Python object standing in
  front of one C++ QQmlJS::Directives.

  C++ hands a QQmlJS::Directives around as a copy, so every C++
  QQmlJS::Directives behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJS::Directives that has a ritual and that Python
  can call so far, 3 names in all: 'pragmaLibrary', 'importFile',
  'importModule'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::Directives::~Directives()': the destructor: Python removes
    its C++ QQmlJS::Directives by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJS::Directives is created at the first use, not by
    'QQmlJS::Directives(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJS::Directives back gives a copy the ritual made
    for Python, in a new cute QQmlJS::Directives.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::Directives'

  #  A C++ QQmlJS::Directives Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_Directives'

  #  The functions Qt calls itself that QQmlJS::Directives is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'pragmaLibrary': (
          ('_ZN6QQmlJS10Directives13pragmaLibraryEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'importFile': (
          ('_ZN6QQmlJS10Directives10importFileERK7QStringS3_ii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'importModule': (
          ('_ZN6QQmlJS10Directives12importModuleERK7QStringS3_S3_ii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('address', 'text', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QQmlJS::Directives()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJS::Directives behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlJS10DirectivesD1Ev'

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

  def pragmaLibrary(self) -> None:
    """
    Calls Qt's 'void QQmlJS::Directives::pragmaLibrary()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-directives.html#pragmaLibrary
    """
    #  void QQmlJS::Directives::pragmaLibrary()
    ritual = 'ritual_ZN6QQmlJS10Directives13pragmaLibraryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS10Directives13pragmaLibraryEv'
    self.uglySide.call(ritual)

  @overload(str, str, int, int)
  def importFile(
      self,
      jsfile: str,
      module: str,
      line: int,
      column: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::Directives::importFile(const QString &jsfile,
    const QString &module, int line, int column)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-directives.html#importFile

    Parameters
    ----------

    jsfile : str
      Passed on as it is: a QString is made of it for the call.

    module : str
      Passed on as it is: a QString is made of it for the call.

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  void QQmlJS::Directives::importFile(const QString &jsfile, const
    #      QString &module, int line, int column)
    ritual = 'ritual_ZN6QQmlJS10Directives10importFileERK7QStringS3_ii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QQmlJS10Directives10importFileERK7QStringS3_ii'
    self.uglySide.call(ritual, jsfile, module, line, column)

  @overload(str, str, str, int, int)
  def importModule(
      self,
      uri: str,
      version: str,
      module: str,
      line: int,
      column: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlJS::Directives::importModule(const QString &uri,
    const QString &version, const QString &module, int line, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-directives.html#importModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    version : str
      Passed on as it is: a QString is made of it for the call.

    module : str
      Passed on as it is: a QString is made of it for the call.

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  void QQmlJS::Directives::importModule(const QString &uri, const
    #      QString &version, const QString &module, int line, int column)
    ritual = 'ritual_ZN6QQmlJS10Directives12importModuleERK7QStringS3_S3_ii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS10Directives12importModuleERK7QStringS3_S3_i'
          'i')
    self.uglySide.call(ritual, uri, version, module, line, column)
