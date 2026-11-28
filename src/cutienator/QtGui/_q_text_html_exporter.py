"""
QTextHtmlExporter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextdocument_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextHtmlExporter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QStringList
from . import QTextFormat, QTextFrameFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QTextBlock, QTextDocument, QTextFragment, QTextFrame
  from . import QTextLength
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextBlock = WAIT['QTextBlock']
  QTextDocument = WAIT['QTextDocument']
  QTextFragment = WAIT['QTextFragment']
  QTextFrame = WAIT['QTextFrame']
  QTextLength = WAIT['QTextLength']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextHtmlExporter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextHtmlExporter: a plain Python object standing in
  front of one C++ QTextHtmlExporter.

  C++ hands a QTextHtmlExporter around as a copy, so every C++
  QTextHtmlExporter behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextHtmlExporter that has a ritual and that Python
  can call so far, 11 names in all: 'toHtml', 'emitTextFrame', 'emitBlock',
  'emitFragment', 'emitTextLength', 'emitAlignment', 'emitMargins',
  'emitAttribute', 'emitPageBreakPolicy', 'emitFontFamily',
  'findUrlForImage'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QTextHtmlExporter::emitFrame(const QTextFrame::Iterator
    &frameIt)': takes a type Python has no way to hand over yet.
  - Qt's 'void QTextHtmlExporter::emitFloatStyle(QTextFrameFormat::Position
    pos, StyleMode mode)': names the enum 'QTextHtmlExporter::StyleMode',
    whose class cannot be named here.
  - Qt's 'QTextHtmlExporter::~QTextHtmlExporter()': the destructor: Python
    removes its C++ QTextHtmlExporter by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 21 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QTextHtmlExporter is created at the first use, not by
    'QTextHtmlExporter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextHtmlExporter back gives a copy the ritual made
    for Python, in a new cute QTextHtmlExporter.
  - Each name of Qt's QTextHtmlExporter that has no cute function yet,
    'emitBackgroundAttribute', 'emitBlockAttributes', 'emitBorderStyle',
    'emitCharFormatStyle', 'emitFloatStyle', 'emitFrame', 'emitFrameStyle',
    'emitTable', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QTextHtmlExporter, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ExportMode(CuteNum):
    """
    The enum 'QTextHtmlExporter::ExportMode' of Qt, with the 2 names Qt gives
    in it.
    """

    ExportEntireDocument = Kee[int](0)
    ExportFragment = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextHtmlExporter'

  #  Qt's '~QTextHtmlExporter()'. Naming it makes this a value class: Python
  #  owns every C++ QTextHtmlExporter behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QTextHtmlExporterD1Ev'

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

  @overload(QTextDocument)
  @overload(NoneType)
  def __init__(self, _doc: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's
    'QTextHtmlExporter::QTextHtmlExporter(const QTextDocument *_doc)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlexporter.html#QTextHtmlExporter

    Parameters
    ----------

    _doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextHtmlExporter::QTextHtmlExporter(const QTextDocument *_doc)
    self._noteCreation(QTextHtmlExporter, lambda: Rituals.call(
        'ritual_ZN17QTextHtmlExporterC1EPK13QTextDocument',
        self._addressOf(_doc),
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

  @overload()
  @overload(ExportMode)
  def toHtml(
      self,
      mode: ExportMode = ExportMode.ExportEntireDocument,
  ) -> str:
    """
    Calls Qt's 'QString QTextHtmlExporter::toHtml(ExportMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlexporter.html#toHtml

    Parameters
    ----------

    mode : ExportMode
      Passed on as its number. May be left out, as in Qt: it is then
      ExportMode.ExportEntireDocument.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextHtmlExporter::toHtml(ExportMode mode)
    return self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter6toHtmlENS_10ExportModeE', mode.value,
    )

  @overload(QTextFrame)
  @overload(NoneType)
  def emitTextFrame(self, frame: Optional[QTextFrame]) -> None:
    """
    Calls Qt's 'void QTextHtmlExporter::emitTextFrame(const QTextFrame
    *frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlexporter.html#emitTextFrame

    Parameters
    ----------

    frame : Optional[QTextFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextHtmlExporter::emitTextFrame(const QTextFrame *frame)
    self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter13emitTextFrameEPK10QTextFrame',
        self._addressOf(frame),
    )

  @overload(QTextBlock)
  def emitBlock(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QTextHtmlExporter::emitBlock(const QTextBlock &block)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlexporter.html#emitBlock

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QTextHtmlExporter::emitBlock(const QTextBlock &block)
    self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter9emitBlockERK10QTextBlock',
        self._valueOf(block),
    )

  @overload(QTextFragment)
  def emitFragment(self, fragment: QTextFragment) -> None:
    """
    Calls Qt's 'void QTextHtmlExporter::emitFragment(const QTextFragment
    &fragment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlexporter.html#emitFragment

    Parameters
    ----------

    fragment : QTextFragment
      Passed on as a value: Qt reads the C++ QTextFragment, which stays
      Python's own.
    """
    #  void QTextHtmlExporter::emitFragment(const QTextFragment &fragment)
    self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter12emitFragmentERK13QTextFragment',
        self._valueOf(fragment),
    )

  @overload(str, QTextLength)
  @overload(NoneType, QTextLength)
  def emitTextLength(
      self,
      attribute: Optional[str],
      length: QTextLength,
  ) -> None:
    """
    Calls Qt's 'void QTextHtmlExporter::emitTextLength(const char *attribute,
    const QTextLength &length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlexporter.html#emitTextLength

    Parameters
    ----------

    attribute : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    length : QTextLength
      Passed on as a value: Qt reads the C++ QTextLength, which stays
      Python's own.
    """
    #  void QTextHtmlExporter::emitTextLength(const char *attribute, const
    #      QTextLength &length)
    self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter14emitTextLengthEPKcRK11QTextLength',
        self._bytesOf(attribute), self._valueOf(length),
    )

  @overload(Qt.Alignment)
  def emitAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QTextHtmlExporter::emitAlignment(Qt::Alignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlexporter.html#emitAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QTextHtmlExporter::emitAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter13emitAlignmentE6QFlagsIN2Qt13Alignmen'
        'tFlagEE',
        alignment.value,
    )

  @overload(str, str, str, str)
  def emitMargins(
      self,
      top: str,
      bottom: str,
      left: str,
      right: str,
  ) -> None:
    """
    Calls Qt's 'void QTextHtmlExporter::emitMargins(const QString &top, const
    QString &bottom, const QString &left, const QString &right)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexthtmlexporter.html#emitMargins

    Parameters
    ----------

    top : str
      Passed on as it is: a QString is made of it for the call.

    bottom : str
      Passed on as it is: a QString is made of it for the call.

    left : str
      Passed on as it is: a QString is made of it for the call.

    right : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextHtmlExporter::emitMargins(const QString &top, const QString
    #      &bottom, const QString &left, const QString &right)
    self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter11emitMarginsERK7QStringS2_S2_S2_',
        top, bottom, left, right,
    )

  @overload(str, str)
  @overload(NoneType, str)
  def emitAttribute(self, attribute: Optional[str], value: str) -> None:
    """
    Calls Qt's 'void QTextHtmlExporter::emitAttribute(const char *attribute,
    const QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlexporter.html#emitAttribute

    Parameters
    ----------

    attribute : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextHtmlExporter::emitAttribute(const char *attribute, const
    #      QString &value)
    self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter13emitAttributeEPKcRK7QString',
        self._bytesOf(attribute), value,
    )

  @overload(QTextFormat.PageBreakFlags)
  def emitPageBreakPolicy(self, policy: QTextFormat.PageBreakFlags) -> None:
    """
    Calls Qt's 'void
    QTextHtmlExporter::emitPageBreakPolicy(QTextFormat::PageBreakFlags
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlexporter.html#emitPageBreakPolicy

    Parameters
    ----------

    policy : QTextFormat.PageBreakFlags
      Passed on as its number.
    """
    #  void
    #      QTextHtmlExporter::emitPageBreakPolicy(QTextFormat::PageBreakFlags
    #      policy)
    self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter19emitPageBreakPolicyE6QFlagsIN11QText'
        'Format13PageBreakFlagEE',
        policy.value,
    )

  @overload(QStringList)
  def emitFontFamily(self, families: QStringList) -> None:
    """
    Calls Qt's 'void QTextHtmlExporter::emitFontFamily(const QStringList
    &families)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlexporter.html#emitFontFamily

    Parameters
    ----------

    families : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QTextHtmlExporter::emitFontFamily(const QStringList &families)
    self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter14emitFontFamilyERK5QListI7QStringE',
        self._valueOf(families),
    )

  @overload(QTextDocument, int, bool)
  @overload(NoneType, int, bool)
  def findUrlForImage(
      self,
      doc: Optional[QTextDocument],
      cacheKey: int,
      isPixmap: bool,
  ) -> str:
    """
    Calls Qt's 'QString QTextHtmlExporter::findUrlForImage(const
    QTextDocument *doc, qint64 cacheKey, bool isPixmap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexthtmlexporter.html#findUrlForImage

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cacheKey : int
      Passed on as it is.

    isPixmap : bool
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextHtmlExporter::findUrlForImage(const QTextDocument *doc,
    #      qint64 cacheKey, bool isPixmap)
    return self.uglySide.call(
        'ritual_ZN17QTextHtmlExporter15findUrlForImageEPK13QTextDocumentxb',
        self._addressOf(doc), cacheKey, isPixmap,
    )

  @staticmethod
  def emitBackgroundAttribute(*__, **_) -> Never:
    """
    Qt's 'void QTextHtmlExporter::emitBackgroundAttribute(const QTextFormat
    &format)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'colorValue'; did you mean 'QCborValue'?.
    """
    raise NotImplementedError(
        "'QTextHtmlExporter.emitBackgroundAttribute' has no cute function "
        "yet. Qt's 'void QTextHtmlExporter::emitBackgroundAttribute(const "
        "QTextFormat &format)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'colorValue'; did you mean 'QCborValue'?.")

  @staticmethod
  def emitBlockAttributes(*__, **_) -> Never:
    """
    Qt's 'void QTextHtmlExporter::emitBlockAttributes(const QTextBlock
    &block)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'formatDifference'.
    """
    raise NotImplementedError(
        "'QTextHtmlExporter.emitBlockAttributes' has no cute function yet. "
        "Qt's 'void QTextHtmlExporter::emitBlockAttributes(const QTextBlock "
        "&block)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'formatDifference'.")

  @staticmethod
  def emitBorderStyle(*__, **_) -> Never:
    """
    Qt's 'void
    QTextHtmlExporter::emitBorderStyle(QTextFrameFormat::BorderStyle style)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'richtextBorderStyleToHtmlBorderStyle'.
    """
    raise NotImplementedError(
        "'QTextHtmlExporter.emitBorderStyle' has no cute function yet. Qt's "
        "'void "
        "QTextHtmlExporter::emitBorderStyle(QTextFrameFormat::BorderStyle "
        "style)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'richtextBorderStyleToHtmlBorderStyle'.")

  @staticmethod
  def emitCharFormatStyle(*__, **_) -> Never:
    """
    Qt's 'bool QTextHtmlExporter::emitCharFormatStyle(const QTextCharFormat
    &format)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'resolvedFontFamilies'.
    """
    raise NotImplementedError(
        "'QTextHtmlExporter.emitCharFormatStyle' has no cute function yet. "
        "Qt's 'bool QTextHtmlExporter::emitCharFormatStyle(const "
        "QTextCharFormat &format)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'resolvedFontFamilies'.")

  @staticmethod
  def emitFloatStyle(*__, **_) -> Never:
    """
    Qt's 'void QTextHtmlExporter::emitFloatStyle(QTextFrameFormat::Position
    pos, StyleMode mode)': names the enum 'QTextHtmlExporter::StyleMode',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QTextHtmlExporter.emitFloatStyle' has no cute function yet. Qt's "
        "'void QTextHtmlExporter::emitFloatStyle(QTextFrameFormat::Position "
        "pos, StyleMode mode)': names the enum "
        "'QTextHtmlExporter::StyleMode', whose class cannot be named here.")

  @staticmethod
  def emitFrame(*__, **_) -> Never:
    """
    Qt's 'void QTextHtmlExporter::emitFrame(const QTextFrame::Iterator
    &frameIt)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextHtmlExporter.emitFrame' has no cute function yet. Qt's 'void "
        "QTextHtmlExporter::emitFrame(const QTextFrame::Iterator "
        "&frameIt)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def emitFrameStyle(*__, **_) -> Never:
    """
    Qt's 'void QTextHtmlExporter::emitFrameStyle(const QTextFrameFormat
    &format, FrameType frameType)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'colorValue'; did you mean 'QCborValue'?.
    """
    raise NotImplementedError(
        "'QTextHtmlExporter.emitFrameStyle' has no cute function yet. Qt's "
        "'void QTextHtmlExporter::emitFrameStyle(const QTextFrameFormat "
        "&format, FrameType frameType)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'colorValue'; did you mean "
        "'QCborValue'?.")

  @staticmethod
  def emitTable(*__, **_) -> Never:
    """
    Qt's 'void QTextHtmlExporter::emitTable(const QTextTable *table)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'richtextBorderStyleToHtmlBorderStyle'.
    """
    raise NotImplementedError(
        "'QTextHtmlExporter.emitTable' has no cute function yet. Qt's 'void "
        "QTextHtmlExporter::emitTable(const QTextTable *table)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'richtextBorderStyleToHtmlBorderStyle'.")
