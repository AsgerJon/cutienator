"""
QTextHtmlImporter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextdocumentfragment_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTextHtmlImporter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from . import QTextHtmlParser

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QTextBlockFormat, QTextCharFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextBlockFormat = WAIT['QTextBlockFormat']
  QTextCharFormat = WAIT['QTextCharFormat']


class QTextHtmlImporter(QTextHtmlParser):
  """
  The cute side of Qt's QTextHtmlImporter: a plain Python object standing in
  front of one C++ QTextHtmlImporter.

  It is built on the cute 'QTextHtmlParser', as Qt's QTextHtmlImporter is
  built on Qt's QTextHtmlParser, and has everything that class has.

  C++ hands a QTextHtmlImporter around as a copy, so every C++
  QTextHtmlImporter behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextHtmlImporter that has a ritual and that Python
  can call so far, 4 names in all: 'import_', 'closeTag', 'appendBlock',
  'appendNodeText'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Table QTextHtmlImporter::scanTable(int tableNodeIdx)': gives a type
    Python has no way to take yet.
  - Qt's 'ProcessNodeResult QTextHtmlImporter::processBlockNode()': gives the
    enum 'QTextHtmlImporter::ProcessNodeResult', whose class cannot be named
    here.
  - Qt's 'ProcessNodeResult QTextHtmlImporter::processSpecialNodes()': gives
    the enum 'QTextHtmlImporter::ProcessNodeResult', whose class cannot be
    named here.
  - Qt's 'QTextHtmlImporter::~QTextHtmlImporter()': the destructor: Python
    removes its C++ QTextHtmlImporter by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 leans on 'QTextHtmlParser.

  What to expect
  --------------

  - The C++ QTextHtmlImporter is created at the first use, not by
    'QTextHtmlImporter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextHtmlImporter back gives a copy the ritual made
    for Python, in a new cute QTextHtmlImporter.
  - Each name of Qt's QTextHtmlImporter that has no cute function yet,
    '__init__', 'processBlockNode', 'processSpecialNodes', 'scanTable', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTextHtmlImporter, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ImportMode(CuteNum):
    """
    The enum 'QTextHtmlImporter::ImportMode' of Qt, with the 2 names Qt gives
    in it.
    """

    ImportToFragment = Kee[int](0)
    ImportToDocument = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextHtmlImporter'

  #  Qt's '~QTextHtmlImporter()'. Naming it makes this a value class: Python
  #  owns every C++ QTextHtmlImporter behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QTextHtmlImporterD1Ev'

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
    Qt's 'QTextHtmlImporter::QTextHtmlImporter(QTextDocument *_doc, const
    QString &html, ImportMode mode, const QTextDocument *resourceProvider)':
    leans on 'QTextHtmlParser::parseTag()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTextHtmlImporter.__init__' has no cute function yet. Qt's "
        "'QTextHtmlImporter::QTextHtmlImporter(QTextDocument *_doc, const "
        "QString &html, ImportMode mode, const QTextDocument "
        "*resourceProvider)': leans on 'QTextHtmlParser::parseTag()', which "
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

  def import_(self) -> None:
    """
    Calls Qt's 'void QTextHtmlImporter::import()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlimporter.html#import
    """
    #  void QTextHtmlImporter::import()
    self.uglySide.call('ritual_ZN17QTextHtmlImporter6importEv')

  def closeTag(self) -> bool:
    """
    Calls Qt's 'bool QTextHtmlImporter::closeTag()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlimporter.html#closeTag
    """
    #  bool QTextHtmlImporter::closeTag()
    return self.uglySide.call('ritual_ZN17QTextHtmlImporter8closeTagEv')

  @overload(QTextBlockFormat)
  @overload(QTextBlockFormat, QTextCharFormat)
  def appendBlock(
      self,
      format: QTextBlockFormat,
      charFmt: Optional[QTextCharFormat] = None,
  ) -> None:
    """
    Calls Qt's 'void QTextHtmlImporter::appendBlock(const QTextBlockFormat
    &format, QTextCharFormat charFmt)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlimporter.html#appendBlock

    Parameters
    ----------

    format : QTextBlockFormat
      Passed on as a value: Qt reads the C++ QTextBlockFormat, which stays
      Python's own.

    charFmt : Optional[QTextCharFormat]
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own. May be left out, as in Qt: a new 'QTextCharFormat()' is
      then passed on.
    """
    #  void QTextHtmlImporter::appendBlock(const QTextBlockFormat &format,
    #      QTextCharFormat charFmt)
    if charFmt is None:
      from . import QTextCharFormat
      charFmt = QTextCharFormat()
    self.uglySide.call(
        'ritual_ZN17QTextHtmlImporter11appendBlockERK16QTextBlockFormat15QT'
        'extCharFormat',
        self._valueOf(format), self._valueOf(charFmt),
    )

  def appendNodeText(self) -> bool:
    """
    Calls Qt's 'bool QTextHtmlImporter::appendNodeText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlimporter.html#appendNodeText
    """
    #  bool QTextHtmlImporter::appendNodeText()
    return self.uglySide.call(
        'ritual_ZN17QTextHtmlImporter14appendNodeTextEv',
    )

  @staticmethod
  def processBlockNode(*__, **_) -> Never:
    """
    Qt's 'ProcessNodeResult QTextHtmlImporter::processBlockNode()': gives the
    enum 'QTextHtmlImporter::ProcessNodeResult', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QTextHtmlImporter.processBlockNode' has no cute function yet. "
        "Qt's 'ProcessNodeResult QTextHtmlImporter::processBlockNode()': "
        "gives the enum 'QTextHtmlImporter::ProcessNodeResult', whose class "
        "cannot be named here.")

  @staticmethod
  def processSpecialNodes(*__, **_) -> Never:
    """
    Qt's 'ProcessNodeResult QTextHtmlImporter::processSpecialNodes()': gives
    the enum 'QTextHtmlImporter::ProcessNodeResult', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QTextHtmlImporter.processSpecialNodes' has no cute function yet. "
        "Qt's 'ProcessNodeResult QTextHtmlImporter::processSpecialNodes()': "
        "gives the enum 'QTextHtmlImporter::ProcessNodeResult', whose class "
        "cannot be named here.")

  @staticmethod
  def scanTable(*__, **_) -> Never:
    """
    Qt's 'Table QTextHtmlImporter::scanTable(int tableNodeIdx)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextHtmlImporter.scanTable' has no cute function yet. Qt's "
        "'Table QTextHtmlImporter::scanTable(int tableNodeIdx)': gives a "
        "type Python has no way to take yet.")
