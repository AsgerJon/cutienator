"""
QmlIR::ScriptDirectivesCollector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::ScriptDirectivesCollector to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlJS, QmlIR

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ScriptDirectivesCollector(QQmlJS.Directives):
  """
  The cute side of Qt's QmlIR::ScriptDirectivesCollector: a plain Python
  object standing in front of one C++ QmlIR::ScriptDirectivesCollector.

  It is built on the cute 'QQmlJS::Directives', as Qt's
  QmlIR::ScriptDirectivesCollector is built on Qt's QQmlJS::Directives, and
  has everything that class has.

  C++ hands a QmlIR::ScriptDirectivesCollector around as a copy, so every C++
  QmlIR::ScriptDirectivesCollector behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QmlIR::ScriptDirectivesCollector that has a ritual
  and that Python can call so far, 3 names in all: 'pragmaLibrary',
  'importFile', 'importModule'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QmlIR::ScriptDirectivesCollector::~ScriptDirectivesCollector()':
    the destructor: Python removes its C++ QmlIR::ScriptDirectivesCollector
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QmlIR::ScriptDirectivesCollector is created at the first use, not
    by 'QmlIR::ScriptDirectivesCollector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QmlIR::ScriptDirectivesCollector back gives a copy
    the ritual made for Python, in a new cute
    QmlIR::ScriptDirectivesCollector.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlIR::ScriptDirectivesCollector'

  #  A C++ QmlIR::ScriptDirectivesCollector Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlIR_ScriptDirectivesCollector'

  #  Qt's '~QmlIR::ScriptDirectivesCollector()'. Naming it makes this a value
  #  class: Python owns every C++ QmlIR::ScriptDirectivesCollector behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QmlIR25ScriptDirectivesCollectorD1Ev'

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

  @overload(WAIT['QmlIR.Document'])
  @overload(NoneType)
  def __init__(self, doc: Optional[QmlIR.Document]) -> None:
    """
    Notes what was given, for Qt's
    'QmlIR::ScriptDirectivesCollector::ScriptDirectivesCollector(QmlIR::
    Document *doc)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-scriptdirectivescollector.html

    Parameters
    ----------

    doc : Optional[QmlIR.Document]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlIR::ScriptDirectivesCollector::ScriptDirectivesCollector(
    #      QmlIR::Document *doc)
    self._noteCreation(ScriptDirectivesCollector, lambda: Rituals.call(
        'ritual_ZN5QmlIR25ScriptDirectivesCollectorC1EPNS_8DocumentE',
        self._addressOf(doc),
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

  def pragmaLibrary(self) -> None:
    """
    Calls Qt's 'void QmlIR::ScriptDirectivesCollector::pragmaLibrary()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-scriptdirectivescollector.html#pragmaLibrary
    """
    #  void QmlIR::ScriptDirectivesCollector::pragmaLibrary()
    ritual = 'ritual_ZN5QmlIR25ScriptDirectivesCollector13pragmaLibraryEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR25ScriptDirectivesCollector13pragmaLibraryEv')
    self.uglySide.call(ritual)

  @overload(str, str, int, int)
  def importFile(
      self,
      jsfile: str,
      module: str,
      lineNumber: int,
      column: int,
  ) -> None:
    """
    Calls Qt's 'void QmlIR::ScriptDirectivesCollector::importFile(const
    QString &jsfile, const QString &module, int lineNumber, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-scriptdirectivescollector.html#importFile

    Parameters
    ----------

    jsfile : str
      Passed on as it is: a QString is made of it for the call.

    module : str
      Passed on as it is: a QString is made of it for the call.

    lineNumber : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  void QmlIR::ScriptDirectivesCollector::importFile(const QString
    #      &jsfile, const QString &module, int lineNumber, int column)
    ritual = (
        'ritual_ZN5QmlIR25ScriptDirectivesCollector10importFileERK7QStringS'
        '3_ii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR25ScriptDirectivesCollector10importFileERK7QS'
          'tringS3_ii')
    self.uglySide.call(ritual, jsfile, module, lineNumber, column)

  @overload(str, str, str, int, int)
  def importModule(
      self,
      uri: str,
      version: str,
      module: str,
      lineNumber: int,
      column: int,
  ) -> None:
    """
    Calls Qt's 'void QmlIR::ScriptDirectivesCollector::importModule(const
    QString &uri, const QString &version, const QString &module, int
    lineNumber, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-scriptdirectivescollector.html#importModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    version : str
      Passed on as it is: a QString is made of it for the call.

    module : str
      Passed on as it is: a QString is made of it for the call.

    lineNumber : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  void QmlIR::ScriptDirectivesCollector::importModule(const QString
    #      &uri, const QString &version, const QString &module, int
    #      lineNumber, int column)
    ritual = (
        'ritual_ZN5QmlIR25ScriptDirectivesCollector12importModuleERK7QStrin'
        'gS3_S3_ii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR25ScriptDirectivesCollector12importModuleERK7'
          'QStringS3_S3_ii')
    self.uglySide.call(ritual, uri, version, module, lineNumber, column)
