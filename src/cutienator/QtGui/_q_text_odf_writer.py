"""
QTextOdfWriter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextodfwriter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTextOdfWriter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QTextTableCellFormat, QTextTableFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextTableCellFormat = WAIT['QTextTableCellFormat']
  QTextTableFormat = WAIT['QTextTableFormat']


class QTextOdfWriter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextOdfWriter: a plain Python object standing in
  front of one C++ QTextOdfWriter.

  C++ hands a QTextOdfWriter around as a copy, so every C++ QTextOdfWriter
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextOdfWriter that has a ritual and that Python can
  call so far, 4 names in all: 'writeAll', 'setCreateArchive',
  'createArchive', 'mergeFormats'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextOdfWriter::QTextOdfWriter(const QTextDocument &document,
    QIODevice *device)': takes a type Python has no way to hand over yet.
  - Qt's 'void QTextOdfWriter::writeBlock(QXmlStreamWriter &writer, const
    QTextBlock &block)': takes a type Python has no way to hand over yet.
  - Qt's 'void QTextOdfWriter::writeFormats(QXmlStreamWriter &writer, const
    QSet<int> &formatIds) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QTextOdfWriter::writeTableFormat(QXmlStreamWriter &writer,
    const QTextTableFormat &format, int formatIndex) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QTextOdfWriter::writeTableCellFormat(QXmlStreamWriter &writer,
    const QTextTableCellFormat &format, int formatIndex, const
    QList<QTextFormat> &styles) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QTextOdfWriter::writeFrame(QXmlStreamWriter &writer, const
    QTextFrame *frame)': takes a type Python has no way to hand over yet.
  - Qt's 'QTextOdfWriter::~QTextOdfWriter()': the destructor: Python removes
    its C++ QTextOdfWriter by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 17 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QTextOdfWriter is created at the first use, not by
    'QTextOdfWriter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextOdfWriter back gives a copy the ritual made for
    Python, in a new cute QTextOdfWriter.
  - Each name of Qt's QTextOdfWriter that has no cute function yet,
    '__init__', 'tableCellStyleElement', 'writeBlock', 'writeBlockFormat',
    'writeCharacterFormat', 'writeFormats', 'writeFrame', 'writeFrameFormat',
    'writeInlineCharacter', 'writeListFormat', 'writeTableCellFormat',
    'writeTableFormat', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QTextTableCellFormat, QTextTableFormat)
  def mergeFormats(
      cell: QTextTableCellFormat,
      table: QTextTableFormat,
  ) -> QTextTableCellFormat:
    """
    Calls Qt's 'QTextTableCellFormat QTextOdfWriter::mergeFormats(const
    QTextTableCellFormat &cell, const QTextTableFormat &table)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextodfwriter.html#mergeFormats

    Parameters
    ----------

    cell : QTextTableCellFormat
      Passed on as a value: Qt reads the C++ QTextTableCellFormat, which
      stays Python's own.

    table : QTextTableFormat
      Passed on as a value: Qt reads the C++ QTextTableFormat, which stays
      Python's own.

    Returns
    -------

    QTextTableCellFormat
      A new cute QTextTableCellFormat around the copy Qt gave back. Python
      owns it.
    """
    #  QTextTableCellFormat QTextOdfWriter::mergeFormats(const
    #      QTextTableCellFormat &cell, const QTextTableFormat &table)
    address = Rituals.call(
        'ritual_ZN14QTextOdfWriter12mergeFormatsERK20QTextTableCellFormatRK'
        '16QTextTableFormat',
        CuteMixin._valueOf(cell), CuteMixin._valueOf(table),
    )
    from . import QTextTableCellFormat
    return QTextTableCellFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextOdfWriter'

  #  Qt's '~QTextOdfWriter()'. Naming it makes this a value class: Python
  #  owns every C++ QTextOdfWriter behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QTextOdfWriterD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def createArchive(self) -> bool:
    """
    Calls Qt's 'bool QTextOdfWriter::createArchive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextodfwriter.html#createArchive
    """
    #  bool QTextOdfWriter::createArchive() const
    return self.uglySide.call('ritual_ZNK14QTextOdfWriter13createArchiveEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setCreateArchive(self, on: bool) -> None:
    """
    Calls Qt's 'void QTextOdfWriter::setCreateArchive(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextodfwriter.html#setCreateArchive

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QTextOdfWriter::setCreateArchive(bool on)
    self.uglySide.call('ritual_ZN14QTextOdfWriter16setCreateArchiveEb', on)

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
    Qt's 'QTextOdfWriter::QTextOdfWriter(const QTextDocument &document,
    QIODevice *device)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.__init__' has no cute function yet. Qt's "
        "'QTextOdfWriter::QTextOdfWriter(const QTextDocument &document, "
        "QIODevice *device)': takes a type Python has no way to hand over "
        "yet.")

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

  def writeAll(self) -> bool:
    """
    Calls Qt's 'bool QTextOdfWriter::writeAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextodfwriter.html#writeAll
    """
    #  bool QTextOdfWriter::writeAll()
    return self.uglySide.call('ritual_ZN14QTextOdfWriter8writeAllEv')

  @staticmethod
  def tableCellStyleElement(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::tableCellStyleElement(QXmlStreamWriter
    &writer, int formatIndex, const QTextTableCellFormat &format, bool
    hasBorder) const': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'pixelToPoint'.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.tableCellStyleElement' has no cute function yet. "
        "Qt's 'void QTextOdfWriter::tableCellStyleElement(QXmlStreamWriter "
        "&writer, int formatIndex, const QTextTableCellFormat &format, bool "
        "hasBorder) const': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'pixelToPoint'.")

  @staticmethod
  def writeBlock(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::writeBlock(QXmlStreamWriter &writer, const
    QTextBlock &block)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.writeBlock' has no cute function yet. Qt's 'void "
        "QTextOdfWriter::writeBlock(QXmlStreamWriter &writer, const "
        "QTextBlock &block)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def writeBlockFormat(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::writeBlockFormat(QXmlStreamWriter &writer,
    const QTextBlockFormat &format, int formatIndex) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'pixelToPoint'.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.writeBlockFormat' has no cute function yet. Qt's "
        "'void QTextOdfWriter::writeBlockFormat(QXmlStreamWriter &writer, "
        "const QTextBlockFormat &format, int formatIndex) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'pixelToPoint'.")

  @staticmethod
  def writeCharacterFormat(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::writeCharacterFormat(QXmlStreamWriter &writer,
    const QTextCharFormat &format, int formatIndex) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'pixelToPoint'.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.writeCharacterFormat' has no cute function yet. "
        "Qt's 'void QTextOdfWriter::writeCharacterFormat(QXmlStreamWriter "
        "&writer, const QTextCharFormat &format, int formatIndex) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'pixelToPoint'.")

  @staticmethod
  def writeFormats(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::writeFormats(QXmlStreamWriter &writer, const
    QSet<int> &formatIds) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.writeFormats' has no cute function yet. Qt's 'void "
        "QTextOdfWriter::writeFormats(QXmlStreamWriter &writer, const "
        "QSet<int> &formatIds) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def writeFrame(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::writeFrame(QXmlStreamWriter &writer, const
    QTextFrame *frame)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.writeFrame' has no cute function yet. Qt's 'void "
        "QTextOdfWriter::writeFrame(QXmlStreamWriter &writer, const "
        "QTextFrame *frame)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def writeFrameFormat(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::writeFrameFormat(QXmlStreamWriter &writer,
    const QTextFrameFormat &format, int formatIndex) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'pixelToPoint'.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.writeFrameFormat' has no cute function yet. Qt's "
        "'void QTextOdfWriter::writeFrameFormat(QXmlStreamWriter &writer, "
        "const QTextFrameFormat &format, int formatIndex) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'pixelToPoint'.")

  @staticmethod
  def writeInlineCharacter(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::writeInlineCharacter(QXmlStreamWriter &writer,
    const QTextFragment &fragment) const': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'probeImageData'.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.writeInlineCharacter' has no cute function yet. "
        "Qt's 'void QTextOdfWriter::writeInlineCharacter(QXmlStreamWriter "
        "&writer, const QTextFragment &fragment) const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'probeImageData'.")

  @staticmethod
  def writeListFormat(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::writeListFormat(QXmlStreamWriter &writer,
    const QTextListFormat &format, int formatIndex) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'bulletChar'.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.writeListFormat' has no cute function yet. Qt's "
        "'void QTextOdfWriter::writeListFormat(QXmlStreamWriter &writer, "
        "const QTextListFormat &format, int formatIndex) const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'bulletChar'.")

  @staticmethod
  def writeTableCellFormat(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::writeTableCellFormat(QXmlStreamWriter &writer,
    const QTextTableCellFormat &format, int formatIndex, const
    QList<QTextFormat> &styles) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.writeTableCellFormat' has no cute function yet. "
        "Qt's 'void QTextOdfWriter::writeTableCellFormat(QXmlStreamWriter "
        "&writer, const QTextTableCellFormat &format, int formatIndex, "
        "const QList<QTextFormat> &styles) const': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def writeTableFormat(*__, **_) -> Never:
    """
    Qt's 'void QTextOdfWriter::writeTableFormat(QXmlStreamWriter &writer,
    const QTextTableFormat &format, int formatIndex) const': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextOdfWriter.writeTableFormat' has no cute function yet. Qt's "
        "'void QTextOdfWriter::writeTableFormat(QXmlStreamWriter &writer, "
        "const QTextTableFormat &format, int formatIndex) const': takes a "
        "type Python has no way to hand over yet.")
