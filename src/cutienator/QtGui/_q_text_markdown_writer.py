"""
QTextMarkdownWriter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextmarkdownwriter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTextMarkdownWriter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractItemModel
  from . import QTextBlock, QTextDocument, QTextFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QTextBlock = WAIT['QTextBlock']
  QTextDocument = WAIT['QTextDocument']
  QTextFrame = WAIT['QTextFrame']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextMarkdownWriter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextMarkdownWriter: a plain Python object standing
  in front of one C++ QTextMarkdownWriter.

  C++ hands a QTextMarkdownWriter around as a copy, so every C++
  QTextMarkdownWriter behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextMarkdownWriter that has a ritual and that
  Python can call so far, 6 names in all: 'writeAll', 'writeTable',
  'writeBlock', 'writeFrame', 'writeFrontMatter',
  'setLinePrefixForBlockQuote'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextMarkdownWriter::QTextMarkdownWriter(QTextStream &stream,
    QTextDocument::MarkdownFeatures features)': takes a type Python has no
    way to hand over yet.
  - Qt's 'ListInfo QTextMarkdownWriter::listInfo(QTextList *list)': gives a
    type Python has no way to take yet.
  - Qt's 'QTextMarkdownWriter::~QTextMarkdownWriter()': the destructor:
    Python removes its C++ QTextMarkdownWriter by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QTextMarkdownWriter is created at the first use, not by
    'QTextMarkdownWriter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextMarkdownWriter back gives a copy the ritual made
    for Python, in a new cute QTextMarkdownWriter.
  - Each name of Qt's QTextMarkdownWriter that has no cute function yet,
    '__init__', 'listInfo', holds a function that raises
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
  __qt_class__ = 'QTextMarkdownWriter'

  #  Qt's '~QTextMarkdownWriter()'. Naming it makes this a value class:
  #  Python owns every C++ QTextMarkdownWriter behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QTextMarkdownWriterD1Ev'

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

  @overload(int)
  def setLinePrefixForBlockQuote(self, level: int) -> None:
    """
    Calls Qt's 'void QTextMarkdownWriter::setLinePrefixForBlockQuote(int
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextmarkdownwriter.html

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  void QTextMarkdownWriter::setLinePrefixForBlockQuote(int level)
    self.uglySide.call(
        'ritual_ZN19QTextMarkdownWriter26setLinePrefixForBlockQuoteEi',
        level,
    )

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
    Qt's 'QTextMarkdownWriter::QTextMarkdownWriter(QTextStream &stream,
    QTextDocument::MarkdownFeatures features)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextMarkdownWriter.__init__' has no cute function yet. Qt's "
        "'QTextMarkdownWriter::QTextMarkdownWriter(QTextStream &stream, "
        "QTextDocument::MarkdownFeatures features)': takes a type Python "
        "has no way to hand over yet.")

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

  @overload(QTextDocument)
  @overload(NoneType)
  def writeAll(self, document: Optional[QTextDocument]) -> bool:
    """
    Calls Qt's 'bool QTextMarkdownWriter::writeAll(const QTextDocument
    *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextmarkdownwriter.html#writeAll

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTextMarkdownWriter::writeAll(const QTextDocument *document)
    return self.uglySide.call(
        'ritual_ZN19QTextMarkdownWriter8writeAllEPK13QTextDocument',
        self._addressOf(document),
    )

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def writeTable(self, table: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QTextMarkdownWriter::writeTable(const QAbstractItemModel
    *table)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextmarkdownwriter.html#writeTable

    Parameters
    ----------

    table : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextMarkdownWriter::writeTable(const QAbstractItemModel *table)
    self.uglySide.call(
        'ritual_ZN19QTextMarkdownWriter10writeTableEPK18QAbstractItemModel',
        self._addressOf(table),
    )

  @overload(QTextBlock, bool, bool, bool)
  def writeBlock(
      self,
      block: QTextBlock,
      table: bool,
      ignoreFormat: bool,
      ignoreEmpty: bool,
  ) -> int:
    """
    Calls Qt's 'int QTextMarkdownWriter::writeBlock(const QTextBlock &block,
    bool table, bool ignoreFormat, bool ignoreEmpty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextmarkdownwriter.html#writeBlock

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    table : bool
      Passed on as it is.

    ignoreFormat : bool
      Passed on as it is.

    ignoreEmpty : bool
      Passed on as it is.
    """
    #  int QTextMarkdownWriter::writeBlock(const QTextBlock &block, bool
    #      table, bool ignoreFormat, bool ignoreEmpty)
    return self.uglySide.call(
        'ritual_ZN19QTextMarkdownWriter10writeBlockERK10QTextBlockbbb',
        self._valueOf(block), table, ignoreFormat, ignoreEmpty,
    )

  @overload(QTextFrame)
  @overload(NoneType)
  def writeFrame(self, frame: Optional[QTextFrame]) -> None:
    """
    Calls Qt's 'void QTextMarkdownWriter::writeFrame(const QTextFrame
    *frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextmarkdownwriter.html#writeFrame

    Parameters
    ----------

    frame : Optional[QTextFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextMarkdownWriter::writeFrame(const QTextFrame *frame)
    self.uglySide.call(
        'ritual_ZN19QTextMarkdownWriter10writeFrameEPK10QTextFrame',
        self._addressOf(frame),
    )

  @overload(str)
  def writeFrontMatter(self, fm: str) -> None:
    """
    Calls Qt's 'void QTextMarkdownWriter::writeFrontMatter(const QString
    &fm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextmarkdownwriter.html#writeFrontMatter

    Parameters
    ----------

    fm : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextMarkdownWriter::writeFrontMatter(const QString &fm)
    self.uglySide.call(
        'ritual_ZN19QTextMarkdownWriter16writeFrontMatterERK7QString', fm,
    )

  @staticmethod
  def listInfo(*__, **_) -> Never:
    """
    Qt's 'ListInfo QTextMarkdownWriter::listInfo(QTextList *list)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTextMarkdownWriter.listInfo' has no cute function yet. Qt's "
        "'ListInfo QTextMarkdownWriter::listInfo(QTextList *list)': gives a "
        "type Python has no way to take yet.")
