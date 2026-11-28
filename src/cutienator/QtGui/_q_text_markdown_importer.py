"""
QTextMarkdownImporter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextmarkdownimporter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTextMarkdownImporter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from . import QTextDocument

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextMarkdownImporter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextMarkdownImporter: a plain Python object standing
  in front of one C++ QTextMarkdownImporter.

  C++ hands a QTextMarkdownImporter around as a copy, so every C++
  QTextMarkdownImporter behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextMarkdownImporter that has a ritual and that
  Python can call so far, 3 names in all: 'import_', 'cbText', 'insertBlock'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QTextMarkdownImporter::cbEnterBlock(int blockType, void
    *detail)': names 'void', which has no cute class yet.
  - Qt's 'int QTextMarkdownImporter::cbLeaveBlock(int blockType, void
    *detail)': names 'void', which has no cute class yet.
  - Qt's 'int QTextMarkdownImporter::cbEnterSpan(int spanType, void
    *detail)': names 'void', which has no cute class yet.
  - Qt's 'int QTextMarkdownImporter::cbLeaveSpan(int spanType, void
    *detail)': names 'void', which has no cute class yet.
  - Qt's 'QTextMarkdownImporter::~QTextMarkdownImporter()': the destructor:
    Python removes its C++ QTextMarkdownImporter by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QTextMarkdownImporter is created at the first use, not by
    'QTextMarkdownImporter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextMarkdownImporter back gives a copy the ritual
    made for Python, in a new cute QTextMarkdownImporter.
  - Each name of Qt's QTextMarkdownImporter that has no cute function yet,
    'cbEnterBlock', 'cbEnterSpan', 'cbLeaveBlock', 'cbLeaveSpan', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTextMarkdownImporter, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Feature(CuteFlags):
    """
    The flags enum 'QTextMarkdownImporter::Feature' of Qt, with the 17 names
    Qt gives in it. Qt names the type of its combinations
    'QTextMarkdownImporter::Features'.
    """

    FeatureCollapseWhitespace = 0x1
    FeaturePermissiveATXHeaders = 0x2
    FeaturePermissiveURLAutoLinks = 0x4
    FeaturePermissiveMailAutoLinks = 0x8
    FeatureNoIndentedCodeBlocks = 0x10
    FeatureNoHTMLBlocks = 0x20
    FeatureNoHTMLSpans = 0x40
    FeatureTables = 0x100
    FeatureStrikeThrough = 0x200
    FeaturePermissiveWWWAutoLinks = 0x400
    FeatureTasklists = 0x800
    FeatureUnderline = 0x4000
    FeatureFrontMatter = 0x100000
    FeaturePermissiveAutoLinks = 0x40c
    FeatureNoHTML = 0x60
    DialectCommonMark = 0x0
    DialectGitHub = 0x104f0c

  Features = Feature

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextMarkdownImporter'

  #  Qt's '~QTextMarkdownImporter()'. Naming it makes this a value class:
  #  Python owns every C++ QTextMarkdownImporter behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QTextMarkdownImporterD1Ev'

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

  @overload(QTextDocument, Features)
  @overload(NoneType, Features)
  def __init__(
      self,
      doc: Optional[QTextDocument],
      features: Features,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTextMarkdownImporter::QTextMarkdownImporter(QTextDocument *doc,
    Features features)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextmarkdownimporter.html#QTextMarkdownImporter

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    features : Features
      Passed on as its number.
    """
    #  QTextMarkdownImporter::QTextMarkdownImporter(QTextDocument *doc,
    #      Features features)
    self._noteCreation(QTextMarkdownImporter, lambda: Rituals.call(
        'ritual_ZN21QTextMarkdownImporterC1EP13QTextDocument6QFlagsINS_7Fea'
        'tureEE',
        self._addressOf(doc), features.value,
    ))

  @overload(QTextDocument, QTextDocument.MarkdownFeatures)
  @overload(NoneType, QTextDocument.MarkdownFeatures)
  def __init__(
      self,
      doc: Optional[QTextDocument],
      features: QTextDocument.MarkdownFeatures,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTextMarkdownImporter::QTextMarkdownImporter(QTextDocument *doc,
    QTextDocument::MarkdownFeatures features)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextmarkdownimporter.html#QTextMarkdownImporter

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    features : QTextDocument.MarkdownFeatures
      Passed on as its number.
    """
    #  QTextMarkdownImporter::QTextMarkdownImporter(QTextDocument *doc,
    #      QTextDocument::MarkdownFeatures features)
    self._noteCreation(QTextMarkdownImporter, lambda: Rituals.call(
        'ritual_ZN21QTextMarkdownImporterC1EP13QTextDocument6QFlagsINS0_15M'
        'arkdownFeatureEE',
        self._addressOf(doc), features.value,
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

  @overload(str)
  def import_(self, markdown: str) -> None:
    """
    Calls Qt's 'void QTextMarkdownImporter::import(const QString &markdown)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextmarkdownimporter.html#import

    Parameters
    ----------

    markdown : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextMarkdownImporter::import(const QString &markdown)
    self.uglySide.call(
        'ritual_ZN21QTextMarkdownImporter6importERK7QString', markdown,
    )

  @overload(int, str, int)
  @overload(int, NoneType, int)
  def cbText(self, textType: int, text: Optional[str], size: int) -> int:
    """
    Calls Qt's 'int QTextMarkdownImporter::cbText(int textType, const char
    *text, unsigned int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextmarkdownimporter.html#cbText

    Parameters
    ----------

    textType : int
      Passed on as it is.

    text : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.
    """
    #  int QTextMarkdownImporter::cbText(int textType, const char *text,
    #      unsigned int size)
    return self.uglySide.call(
        'ritual_ZN21QTextMarkdownImporter6cbTextEiPKcj',
        textType, self._bytesOf(text), size,
    )

  def insertBlock(self) -> None:
    """
    Calls Qt's 'void QTextMarkdownImporter::insertBlock()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextmarkdownimporter.html#insertBlock
    """
    #  void QTextMarkdownImporter::insertBlock()
    self.uglySide.call('ritual_ZN21QTextMarkdownImporter11insertBlockEv')

  @staticmethod
  def cbEnterBlock(*__, **_) -> Never:
    """
    Qt's 'int QTextMarkdownImporter::cbEnterBlock(int blockType, void
    *detail)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTextMarkdownImporter.cbEnterBlock' has no cute function yet. "
        "Qt's 'int QTextMarkdownImporter::cbEnterBlock(int blockType, void "
        "*detail)': names 'void', which has no cute class yet.")

  @staticmethod
  def cbEnterSpan(*__, **_) -> Never:
    """
    Qt's 'int QTextMarkdownImporter::cbEnterSpan(int spanType, void
    *detail)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTextMarkdownImporter.cbEnterSpan' has no cute function yet. Qt's "
        "'int QTextMarkdownImporter::cbEnterSpan(int spanType, void "
        "*detail)': names 'void', which has no cute class yet.")

  @staticmethod
  def cbLeaveBlock(*__, **_) -> Never:
    """
    Qt's 'int QTextMarkdownImporter::cbLeaveBlock(int blockType, void
    *detail)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTextMarkdownImporter.cbLeaveBlock' has no cute function yet. "
        "Qt's 'int QTextMarkdownImporter::cbLeaveBlock(int blockType, void "
        "*detail)': names 'void', which has no cute class yet.")

  @staticmethod
  def cbLeaveSpan(*__, **_) -> Never:
    """
    Qt's 'int QTextMarkdownImporter::cbLeaveSpan(int spanType, void
    *detail)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QTextMarkdownImporter.cbLeaveSpan' has no cute function yet. Qt's "
        "'int QTextMarkdownImporter::cbLeaveSpan(int spanType, void "
        "*detail)': names 'void', which has no cute class yet.")
