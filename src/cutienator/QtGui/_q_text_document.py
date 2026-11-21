"""
QTextDocument binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextdocument.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QChar, QMetaObject, QRectF, QRegularExpression, QSizeF
  from ..QtCore import QUrl, QVariant
  from . import QAbstractTextDocumentLayout, QAbstractUndoItem, QFont
  from . import QPagedPaintDevice, QPainter, QTextBlock, QTextCursor
  from . import QTextFormat, QTextFrame, QTextObject, QTextOption
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractTextDocumentLayout = WAIT['QAbstractTextDocumentLayout']
  QAbstractUndoItem = WAIT['QAbstractUndoItem']
  QFont = WAIT['QFont']
  QPagedPaintDevice = WAIT['QPagedPaintDevice']
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QRegularExpression = WAIT['QRegularExpression']
  QSizeF = WAIT['QSizeF']
  QTextCursor = WAIT['QTextCursor']
  QTextFormat = WAIT['QTextFormat']
  QTextOption = WAIT['QTextOption']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextDocument(QObject):
  """
  The cute side of Qt's QTextDocument: a plain Python object standing in
  front of one C++ QTextDocument.

  It is built on the cute 'QObject', as Qt's QTextDocument is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextDocument that has a ritual and that Python can
  call so far, 84 names in all: 'metaObject', 'tr', 'clone', 'isEmpty',
  'clear', 'setUndoRedoEnabled', 'isUndoRedoEnabled', 'isUndoAvailable',
  'isRedoAvailable', 'availableUndoSteps', 'availableRedoSteps', 'revision',
  'setDocumentLayout', 'documentLayout', 'setMetaInformation',
  'metaInformation', 'toHtml', 'setHtml', 'toMarkdown', 'setMarkdown',
  'toRawText', 'toPlainText', 'setPlainText', 'characterAt', 'find',
  'frameAt', 'rootFrame', 'object', 'objectForFormat', 'findBlock',
  'findBlockByNumber', 'findBlockByLineNumber', 'begin', 'end', 'firstBlock',
  'lastBlock', 'setPageSize', 'pageSize', 'setDefaultFont', 'defaultFont',
  'setSuperScriptBaseline', 'superScriptBaseline', 'setSubScriptBaseline',
  'subScriptBaseline', 'setBaselineOffset', 'baselineOffset', 'pageCount',
  'isModified', 'print', 'resource', 'addResource', 'markContentsDirty',
  'setUseDesignMetrics', 'useDesignMetrics', 'setLayoutEnabled',
  'isLayoutEnabled', 'drawContents', 'setTextWidth', 'textWidth',
  'idealWidth', 'indentWidth', 'setIndentWidth', 'documentMargin',
  'setDocumentMargin', 'adjustSize', 'size', 'blockCount', 'lineCount',
  'characterCount', 'setDefaultStyleSheet', 'defaultStyleSheet', 'undo',
  'redo', 'clearUndoRedoStacks', 'maximumBlockCount', 'setMaximumBlockCount',
  'defaultTextOption', 'setDefaultTextOption', 'baseUrl', 'setBaseUrl',
  'defaultCursorMoveStyle', 'setDefaultCursorMoveStyle', 'appendUndoItem',
  'setModified'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextDocument::~QTextDocument()': the destructor: Python never
    removes a C++ QTextDocument.

  What has no ritual
  ------------------

  26 of the 118 functions Qt declares: 10 a signal; 7 takes or gives a type
  that cannot be passed yet; 3 private; 3 protected; 2 forbidden; 1 a
  template.

  What to expect
  --------------

  - The C++ QTextDocument is created at the first use, not by
    'QTextDocument(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextDocument.
  - Qt tells when it has removed the C++ QTextDocument. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QTextDocument, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class FindFlag(CuteFlags):
    """
    The flags enum 'QTextDocument::FindFlag' of Qt, with the 3 names Qt gives
    in it. Qt names the type of its combinations 'QTextDocument::FindFlags'.
    """

    FindBackward = 0x1
    FindCaseSensitively = 0x2
    FindWholeWords = 0x4

  FindFlags = FindFlag

  class MarkdownFeature(CuteFlags):
    """
    The flags enum 'QTextDocument::MarkdownFeature' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QTextDocument::MarkdownFeatures'.
    """

    MarkdownNoHTML = 0x60
    MarkdownDialectCommonMark = 0x0
    MarkdownDialectGitHub = 0x104f0c

  MarkdownFeatures = MarkdownFeature

  class MetaInformation(CuteNum):
    """
    The enum 'QTextDocument::MetaInformation' of Qt, with the 4 names Qt
    gives in it.
    """

    DocumentTitle = Kee[int](0)
    DocumentUrl = Kee[int](1)
    CssMedia = Kee[int](2)
    FrontMatter = Kee[int](3)

  class ResourceType(CuteNum):
    """
    The enum 'QTextDocument::ResourceType' of Qt, with the 6 names Qt gives
    in it.
    """

    UnknownResource = Kee[int](0)
    HtmlResource = Kee[int](1)
    ImageResource = Kee[int](2)
    StyleSheetResource = Kee[int](3)
    MarkdownResource = Kee[int](4)
    UserResource = Kee[int](100)

  class Stacks(CuteNum):
    """
    The enum 'QTextDocument::Stacks' of Qt, with the 3 names Qt gives in it.
    """

    UndoStack = Kee[int](1)
    RedoStack = Kee[int](2)
    UndoAndRedoStacks = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QTextDocument::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocument::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QTextDocument2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextDocument'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextDocument::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextDocument::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QTextDocument10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def clone(
      self,
      parent: Optional[QObject] = None,
  ) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QTextDocument::clone(QObject *parent) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#clone

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QTextDocument::clone(QObject *parent) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument5cloneEP7QObject', self._addressOf(parent),
    )
    return QTextDocument._cuteAt(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QTextDocument::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#isEmpty
    """
    #  bool QTextDocument::isEmpty() const
    return self.uglySide.call('ritual_ZNK13QTextDocument7isEmptyEv')

  def isUndoRedoEnabled(self) -> bool:
    """
    Calls Qt's 'bool QTextDocument::isUndoRedoEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#isUndoRedoEnabled
    """
    #  bool QTextDocument::isUndoRedoEnabled() const
    return self.uglySide.call(
        'ritual_ZNK13QTextDocument17isUndoRedoEnabledEv',
    )

  def isUndoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QTextDocument::isUndoAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#isUndoAvailable
    """
    #  bool QTextDocument::isUndoAvailable() const
    return self.uglySide.call('ritual_ZNK13QTextDocument15isUndoAvailableEv')

  def isRedoAvailable(self) -> bool:
    """
    Calls Qt's 'bool QTextDocument::isRedoAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#isRedoAvailable
    """
    #  bool QTextDocument::isRedoAvailable() const
    return self.uglySide.call('ritual_ZNK13QTextDocument15isRedoAvailableEv')

  def availableUndoSteps(self) -> int:
    """
    Calls Qt's 'int QTextDocument::availableUndoSteps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#availableUndoSteps
    """
    #  int QTextDocument::availableUndoSteps() const
    return self.uglySide.call(
        'ritual_ZNK13QTextDocument18availableUndoStepsEv',
    )

  def availableRedoSteps(self) -> int:
    """
    Calls Qt's 'int QTextDocument::availableRedoSteps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#availableRedoSteps
    """
    #  int QTextDocument::availableRedoSteps() const
    return self.uglySide.call(
        'ritual_ZNK13QTextDocument18availableRedoStepsEv',
    )

  def revision(self) -> int:
    """
    Calls Qt's 'int QTextDocument::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#revision
    """
    #  int QTextDocument::revision() const
    return self.uglySide.call('ritual_ZNK13QTextDocument8revisionEv')

  def documentLayout(self) -> Optional[QAbstractTextDocumentLayout]:
    """
    Calls Qt's 'QAbstractTextDocumentLayout *QTextDocument::documentLayout()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#documentLayout

    Returns
    -------

    Optional[QAbstractTextDocumentLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTextDocumentLayout *QTextDocument::documentLayout() const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument14documentLayoutEv',
    )
    from . import QAbstractTextDocumentLayout
    return QAbstractTextDocumentLayout._cuteAt(address)

  @overload(MetaInformation)
  def metaInformation(self, info: MetaInformation) -> str:
    """
    Calls Qt's 'QString QTextDocument::metaInformation(MetaInformation info)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#metaInformation

    Parameters
    ----------

    info : MetaInformation
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocument::metaInformation(MetaInformation info) const
    return self.uglySide.call(
        'ritual_ZNK13QTextDocument15metaInformationENS_15MetaInformationE',
        info.value,
    )

  def toHtml(self) -> str:
    """
    Calls Qt's 'QString QTextDocument::toHtml() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#toHtml

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocument::toHtml() const
    return self.uglySide.call('ritual_ZNK13QTextDocument6toHtmlEv')

  @overload()
  @overload(MarkdownFeatures)
  def toMarkdown(
      self,
      features: MarkdownFeatures = MarkdownFeatures.MarkdownDialectGitHub,
  ) -> str:
    """
    Calls Qt's 'QString QTextDocument::toMarkdown(MarkdownFeatures features)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#toMarkdown

    Parameters
    ----------

    features : MarkdownFeatures
      Passed on as its number. May be left out, as in Qt: it is then
      MarkdownFeatures.MarkdownDialectGitHub.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocument::toMarkdown(MarkdownFeatures features) const
    return self.uglySide.call(
        'ritual_ZNK13QTextDocument10toMarkdownE6QFlagsINS_15MarkdownFeature'
        'EE',
        features.value,
    )

  def toRawText(self) -> str:
    """
    Calls Qt's 'QString QTextDocument::toRawText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#toRawText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocument::toRawText() const
    return self.uglySide.call('ritual_ZNK13QTextDocument9toRawTextEv')

  def toPlainText(self) -> str:
    """
    Calls Qt's 'QString QTextDocument::toPlainText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#toPlainText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocument::toPlainText() const
    return self.uglySide.call('ritual_ZNK13QTextDocument11toPlainTextEv')

  @overload(int)
  def characterAt(self, pos: int) -> QChar:
    """
    Calls Qt's 'QChar QTextDocument::characterAt(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#characterAt

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QChar
      A new cute QChar around the copy Qt gave back. Python owns it.
    """
    #  QChar QTextDocument::characterAt(int pos) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument11characterAtEi', pos,
    )
    from ..QtCore import QChar
    return QChar._cuteOwning(address)

  @overload(str)
  @overload(str, int)
  @overload(str, int, FindFlags)
  def find(
      self,
      subString: str,
      from_: int = 0,
      options: FindFlags = FindFlags(),
  ) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextDocument::find(const QString &subString, int
    from, FindFlags options) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#find

    Parameters
    ----------

    subString : str
      Passed on as it is: a QString is made of it for the call.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    options : FindFlags
      Passed on as its number. May be left out, as in Qt: it is then
      FindFlags().

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextDocument::find(const QString &subString, int from,
    #      FindFlags options) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument4findERK7QStringi6QFlagsINS_8FindFlagEE',
        subString, from_, options.value,
    )
    from . import QTextCursor
    return QTextCursor._cuteOwning(address)

  @overload(str, QTextCursor)
  @overload(str, QTextCursor, FindFlags)
  def find(
      self,
      subString: str,
      cursor: QTextCursor,
      options: FindFlags = FindFlags(),
  ) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextDocument::find(const QString &subString,
    const QTextCursor &cursor, FindFlags options) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#find

    Parameters
    ----------

    subString : str
      Passed on as it is: a QString is made of it for the call.

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    options : FindFlags
      Passed on as its number. May be left out, as in Qt: it is then
      FindFlags().

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextDocument::find(const QString &subString, const
    #      QTextCursor &cursor, FindFlags options) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument4findERK7QStringRK11QTextCursor6QFlagsINS'
        '_8FindFlagEE',
        subString, self._valueOf(cursor), options.value,
    )
    from . import QTextCursor
    return QTextCursor._cuteOwning(address)

  @overload(QRegularExpression)
  @overload(QRegularExpression, int)
  @overload(QRegularExpression, int, FindFlags)
  def find(
      self,
      expr: QRegularExpression,
      from_: int = 0,
      options: FindFlags = FindFlags(),
  ) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextDocument::find(const QRegularExpression
    &expr, int from, FindFlags options) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#find

    Parameters
    ----------

    expr : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    options : FindFlags
      Passed on as its number. May be left out, as in Qt: it is then
      FindFlags().

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextDocument::find(const QRegularExpression &expr, int
    #      from, FindFlags options) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument4findERK18QRegularExpressioni6QFlagsINS_8'
        'FindFlagEE',
        self._valueOf(expr), from_, options.value,
    )
    from . import QTextCursor
    return QTextCursor._cuteOwning(address)

  @overload(QRegularExpression, QTextCursor)
  @overload(QRegularExpression, QTextCursor, FindFlags)
  def find(
      self,
      expr: QRegularExpression,
      cursor: QTextCursor,
      options: FindFlags = FindFlags(),
  ) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QTextDocument::find(const QRegularExpression
    &expr, const QTextCursor &cursor, FindFlags options) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#find

    Parameters
    ----------

    expr : QRegularExpression
      Passed on as a value: Qt reads the C++ QRegularExpression, which stays
      Python's own.

    cursor : QTextCursor
      Passed on as a value: Qt reads the C++ QTextCursor, which stays
      Python's own.

    options : FindFlags
      Passed on as its number. May be left out, as in Qt: it is then
      FindFlags().

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QTextDocument::find(const QRegularExpression &expr, const
    #      QTextCursor &cursor, FindFlags options) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument4findERK18QRegularExpressionRK11QTextCurs'
        'or6QFlagsINS_8FindFlagEE',
        self._valueOf(expr), self._valueOf(cursor), options.value,
    )
    from . import QTextCursor
    return QTextCursor._cuteOwning(address)

  @overload(int)
  def frameAt(self, pos: int) -> Optional[QTextFrame]:
    """
    Calls Qt's 'QTextFrame *QTextDocument::frameAt(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#frameAt

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    Optional[QTextFrame]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextFrame *QTextDocument::frameAt(int pos) const
    address = self.uglySide.call('ritual_ZNK13QTextDocument7frameAtEi', pos)
    from . import QTextFrame
    return QTextFrame._cuteAt(address)

  def rootFrame(self) -> Optional[QTextFrame]:
    """
    Calls Qt's 'QTextFrame *QTextDocument::rootFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#rootFrame

    Returns
    -------

    Optional[QTextFrame]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextFrame *QTextDocument::rootFrame() const
    address = self.uglySide.call('ritual_ZNK13QTextDocument9rootFrameEv')
    from . import QTextFrame
    return QTextFrame._cuteAt(address)

  @overload(int)
  def object(self, objectIndex: int) -> Optional[QTextObject]:
    """
    Calls Qt's 'QTextObject *QTextDocument::object(int objectIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#object

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QTextObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextObject *QTextDocument::object(int objectIndex) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument6objectEi', objectIndex,
    )
    from . import QTextObject
    return QTextObject._cuteAt(address)

  @overload(QTextFormat)
  def objectForFormat(self, a0: QTextFormat) -> Optional[QTextObject]:
    """
    Calls Qt's 'QTextObject *QTextDocument::objectForFormat(const QTextFormat
    &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#objectForFormat

    Parameters
    ----------

    a0 : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.

    Returns
    -------

    Optional[QTextObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextObject *QTextDocument::objectForFormat(const QTextFormat &a0)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument15objectForFormatERK11QTextFormat',
        self._valueOf(a0),
    )
    from . import QTextObject
    return QTextObject._cuteAt(address)

  @overload(int)
  def findBlock(self, pos: int) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextDocument::findBlock(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#findBlock

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextDocument::findBlock(int pos) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument9findBlockEi', pos,
    )
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  @overload(int)
  def findBlockByNumber(self, blockNumber: int) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextDocument::findBlockByNumber(int blockNumber)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#findBlockByNumber

    Parameters
    ----------

    blockNumber : int
      Passed on as it is.

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextDocument::findBlockByNumber(int blockNumber) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument17findBlockByNumberEi', blockNumber,
    )
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  @overload(int)
  def findBlockByLineNumber(self, blockNumber: int) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextDocument::findBlockByLineNumber(int
    blockNumber) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#findBlockByLineNumber

    Parameters
    ----------

    blockNumber : int
      Passed on as it is.

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextDocument::findBlockByLineNumber(int blockNumber) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument21findBlockByLineNumberEi', blockNumber,
    )
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  def begin(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextDocument::begin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#begin

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextDocument::begin() const
    address = self.uglySide.call('ritual_ZNK13QTextDocument5beginEv')
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  def end(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextDocument::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#end

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextDocument::end() const
    address = self.uglySide.call('ritual_ZNK13QTextDocument3endEv')
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  def firstBlock(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextDocument::firstBlock() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#firstBlock

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextDocument::firstBlock() const
    address = self.uglySide.call('ritual_ZNK13QTextDocument10firstBlockEv')
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  def lastBlock(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextDocument::lastBlock() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#lastBlock

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextDocument::lastBlock() const
    address = self.uglySide.call('ritual_ZNK13QTextDocument9lastBlockEv')
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  def pageSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QTextDocument::pageSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#pageSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QTextDocument::pageSize() const
    address = self.uglySide.call('ritual_ZNK13QTextDocument8pageSizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QTextDocument::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTextDocument::defaultFont() const
    address = self.uglySide.call('ritual_ZNK13QTextDocument11defaultFontEv')
    from . import QFont
    return QFont._cuteOwning(address)

  def superScriptBaseline(self) -> float:
    """
    Calls Qt's 'qreal QTextDocument::superScriptBaseline() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#superScriptBaseline
    """
    #  qreal QTextDocument::superScriptBaseline() const
    return self.uglySide.call(
        'ritual_ZNK13QTextDocument19superScriptBaselineEv',
    )

  def subScriptBaseline(self) -> float:
    """
    Calls Qt's 'qreal QTextDocument::subScriptBaseline() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#subScriptBaseline
    """
    #  qreal QTextDocument::subScriptBaseline() const
    return self.uglySide.call(
        'ritual_ZNK13QTextDocument17subScriptBaselineEv',
    )

  def baselineOffset(self) -> float:
    """
    Calls Qt's 'qreal QTextDocument::baselineOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#baselineOffset
    """
    #  qreal QTextDocument::baselineOffset() const
    return self.uglySide.call('ritual_ZNK13QTextDocument14baselineOffsetEv')

  def pageCount(self) -> int:
    """
    Calls Qt's 'int QTextDocument::pageCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#pageCount
    """
    #  int QTextDocument::pageCount() const
    return self.uglySide.call('ritual_ZNK13QTextDocument9pageCountEv')

  def isModified(self) -> bool:
    """
    Calls Qt's 'bool QTextDocument::isModified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#isModified
    """
    #  bool QTextDocument::isModified() const
    return self.uglySide.call('ritual_ZNK13QTextDocument10isModifiedEv')

  @overload(int, QUrl)
  def resource(self, type: int, name: QUrl) -> QVariant:
    """
    Calls Qt's 'QVariant QTextDocument::resource(int type, const QUrl &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#resource

    Parameters
    ----------

    type : int
      Passed on as it is.

    name : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTextDocument::resource(int type, const QUrl &name) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument8resourceEiRK4QUrl',
        type, self._valueOf(name),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def useDesignMetrics(self) -> bool:
    """
    Calls Qt's 'bool QTextDocument::useDesignMetrics() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#useDesignMetrics
    """
    #  bool QTextDocument::useDesignMetrics() const
    return self.uglySide.call(
        'ritual_ZNK13QTextDocument16useDesignMetricsEv',
    )

  def isLayoutEnabled(self) -> bool:
    """
    Calls Qt's 'bool QTextDocument::isLayoutEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#isLayoutEnabled
    """
    #  bool QTextDocument::isLayoutEnabled() const
    return self.uglySide.call('ritual_ZNK13QTextDocument15isLayoutEnabledEv')

  def textWidth(self) -> float:
    """
    Calls Qt's 'qreal QTextDocument::textWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#textWidth
    """
    #  qreal QTextDocument::textWidth() const
    return self.uglySide.call('ritual_ZNK13QTextDocument9textWidthEv')

  def idealWidth(self) -> float:
    """
    Calls Qt's 'qreal QTextDocument::idealWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#idealWidth
    """
    #  qreal QTextDocument::idealWidth() const
    return self.uglySide.call('ritual_ZNK13QTextDocument10idealWidthEv')

  def indentWidth(self) -> float:
    """
    Calls Qt's 'qreal QTextDocument::indentWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#indentWidth
    """
    #  qreal QTextDocument::indentWidth() const
    return self.uglySide.call('ritual_ZNK13QTextDocument11indentWidthEv')

  def documentMargin(self) -> float:
    """
    Calls Qt's 'qreal QTextDocument::documentMargin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#documentMargin
    """
    #  qreal QTextDocument::documentMargin() const
    return self.uglySide.call('ritual_ZNK13QTextDocument14documentMarginEv')

  def size(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QTextDocument::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#size

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QTextDocument::size() const
    address = self.uglySide.call('ritual_ZNK13QTextDocument4sizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def blockCount(self) -> int:
    """
    Calls Qt's 'int QTextDocument::blockCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#blockCount
    """
    #  int QTextDocument::blockCount() const
    return self.uglySide.call('ritual_ZNK13QTextDocument10blockCountEv')

  def lineCount(self) -> int:
    """
    Calls Qt's 'int QTextDocument::lineCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#lineCount
    """
    #  int QTextDocument::lineCount() const
    return self.uglySide.call('ritual_ZNK13QTextDocument9lineCountEv')

  def characterCount(self) -> int:
    """
    Calls Qt's 'int QTextDocument::characterCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#characterCount
    """
    #  int QTextDocument::characterCount() const
    return self.uglySide.call('ritual_ZNK13QTextDocument14characterCountEv')

  def defaultStyleSheet(self) -> str:
    """
    Calls Qt's 'QString QTextDocument::defaultStyleSheet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#defaultStyleSheet

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextDocument::defaultStyleSheet() const
    return self.uglySide.call(
        'ritual_ZNK13QTextDocument17defaultStyleSheetEv',
    )

  def maximumBlockCount(self) -> int:
    """
    Calls Qt's 'int QTextDocument::maximumBlockCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#maximumBlockCount
    """
    #  int QTextDocument::maximumBlockCount() const
    return self.uglySide.call(
        'ritual_ZNK13QTextDocument17maximumBlockCountEv',
    )

  def defaultTextOption(self) -> QTextOption:
    """
    Calls Qt's 'QTextOption QTextDocument::defaultTextOption() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#defaultTextOption

    Returns
    -------

    QTextOption
      A new cute QTextOption around the copy Qt gave back. Python owns it.
    """
    #  QTextOption QTextDocument::defaultTextOption() const
    address = self.uglySide.call(
        'ritual_ZNK13QTextDocument17defaultTextOptionEv',
    )
    from . import QTextOption
    return QTextOption._cuteOwning(address)

  def baseUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QTextDocument::baseUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#baseUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QTextDocument::baseUrl() const
    address = self.uglySide.call('ritual_ZNK13QTextDocument7baseUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def defaultCursorMoveStyle(self) -> Qt.CursorMoveStyle:
    """
    Calls Qt's 'Qt::CursorMoveStyle QTextDocument::defaultCursorMoveStyle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#defaultCursorMoveStyle

    Returns
    -------

    Qt.CursorMoveStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CursorMoveStyle(number)' gives.
    """
    #  Qt::CursorMoveStyle QTextDocument::defaultCursorMoveStyle() const
    return Qt.CursorMoveStyle(self.uglySide.call(
        'ritual_ZNK13QTextDocument22defaultCursorMoveStyleEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setUndoRedoEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QTextDocument::setUndoRedoEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setUndoRedoEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QTextDocument::setUndoRedoEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN13QTextDocument18setUndoRedoEnabledEb', enable,
    )

  @overload(QAbstractTextDocumentLayout)
  @overload(NoneType)
  def setDocumentLayout(
      self,
      layout: Optional[QAbstractTextDocumentLayout],
  ) -> None:
    """
    Calls Qt's 'void
    QTextDocument::setDocumentLayout(QAbstractTextDocumentLayout *layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setDocumentLayout

    Parameters
    ----------

    layout : Optional[QAbstractTextDocumentLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocument::setDocumentLayout(QAbstractTextDocumentLayout
    #      *layout)
    self.uglySide.call(
        'ritual_ZN13QTextDocument17setDocumentLayoutEP27QAbstractTextDocume'
        'ntLayout',
        self._addressOf(layout),
    )

  @overload(MetaInformation, str)
  def setMetaInformation(self, info: MetaInformation, a1: str) -> None:
    """
    Calls Qt's 'void QTextDocument::setMetaInformation(MetaInformation info,
    const QString &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setMetaInformation

    Parameters
    ----------

    info : MetaInformation
      Passed on as its number.

    a1 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextDocument::setMetaInformation(MetaInformation info, const
    #      QString &a1)
    self.uglySide.call(
        'ritual_ZN13QTextDocument18setMetaInformationENS_15MetaInformationE'
        'RK7QString',
        info.value, a1,
    )

  @overload(str)
  def setHtml(self, html: str) -> None:
    """
    Calls Qt's 'void QTextDocument::setHtml(const QString &html)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#setHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextDocument::setHtml(const QString &html)
    self.uglySide.call('ritual_ZN13QTextDocument7setHtmlERK7QString', html)

  @overload(str)
  @overload(str, MarkdownFeatures)
  def setMarkdown(
      self,
      markdown: str,
      features: MarkdownFeatures = MarkdownFeatures.MarkdownDialectGitHub,
  ) -> None:
    """
    Calls Qt's 'void QTextDocument::setMarkdown(const QString &markdown,
    MarkdownFeatures features)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#setMarkdown

    Parameters
    ----------

    markdown : str
      Passed on as it is: a QString is made of it for the call.

    features : MarkdownFeatures
      Passed on as its number. May be left out, as in Qt: it is then
      MarkdownFeatures.MarkdownDialectGitHub.
    """
    #  void QTextDocument::setMarkdown(const QString &markdown,
    #      MarkdownFeatures features)
    self.uglySide.call(
        'ritual_ZN13QTextDocument11setMarkdownERK7QString6QFlagsINS_15Markd'
        'ownFeatureEE',
        markdown, features.value,
    )

  @overload(str)
  def setPlainText(self, text: str) -> None:
    """
    Calls Qt's 'void QTextDocument::setPlainText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#setPlainText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextDocument::setPlainText(const QString &text)
    self.uglySide.call(
        'ritual_ZN13QTextDocument12setPlainTextERK7QString', text,
    )

  @overload(QSizeF)
  def setPageSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QTextDocument::setPageSize(const QSizeF &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#setPageSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QTextDocument::setPageSize(const QSizeF &size)
    self.uglySide.call(
        'ritual_ZN13QTextDocument11setPageSizeERK6QSizeF',
        self._valueOf(size),
    )

  @overload(QFont)
  def setDefaultFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QTextDocument::setDefaultFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#setDefaultFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QTextDocument::setDefaultFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN13QTextDocument14setDefaultFontERK5QFont',
        self._valueOf(font),
    )

  @overload(float)
  def setSuperScriptBaseline(self, baseline: float) -> None:
    """
    Calls Qt's 'void QTextDocument::setSuperScriptBaseline(qreal baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setSuperScriptBaseline

    Parameters
    ----------

    baseline : float
      Passed on as it is.
    """
    #  void QTextDocument::setSuperScriptBaseline(qreal baseline)
    self.uglySide.call(
        'ritual_ZN13QTextDocument22setSuperScriptBaselineEd', baseline,
    )

  @overload(float)
  def setSubScriptBaseline(self, baseline: float) -> None:
    """
    Calls Qt's 'void QTextDocument::setSubScriptBaseline(qreal baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setSubScriptBaseline

    Parameters
    ----------

    baseline : float
      Passed on as it is.
    """
    #  void QTextDocument::setSubScriptBaseline(qreal baseline)
    self.uglySide.call(
        'ritual_ZN13QTextDocument20setSubScriptBaselineEd', baseline,
    )

  @overload(float)
  def setBaselineOffset(self, baseline: float) -> None:
    """
    Calls Qt's 'void QTextDocument::setBaselineOffset(qreal baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setBaselineOffset

    Parameters
    ----------

    baseline : float
      Passed on as it is.
    """
    #  void QTextDocument::setBaselineOffset(qreal baseline)
    self.uglySide.call(
        'ritual_ZN13QTextDocument17setBaselineOffsetEd', baseline,
    )

  @overload(bool)
  def setUseDesignMetrics(self, b: bool) -> None:
    """
    Calls Qt's 'void QTextDocument::setUseDesignMetrics(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setUseDesignMetrics

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTextDocument::setUseDesignMetrics(bool b)
    self.uglySide.call('ritual_ZN13QTextDocument19setUseDesignMetricsEb', b)

  @overload(bool)
  def setLayoutEnabled(self, b: bool) -> None:
    """
    Calls Qt's 'void QTextDocument::setLayoutEnabled(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setLayoutEnabled

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTextDocument::setLayoutEnabled(bool b)
    self.uglySide.call('ritual_ZN13QTextDocument16setLayoutEnabledEb', b)

  @overload(float)
  def setTextWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QTextDocument::setTextWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#setTextWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QTextDocument::setTextWidth(qreal width)
    self.uglySide.call('ritual_ZN13QTextDocument12setTextWidthEd', width)

  @overload(float)
  def setIndentWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QTextDocument::setIndentWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#setIndentWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QTextDocument::setIndentWidth(qreal width)
    self.uglySide.call('ritual_ZN13QTextDocument14setIndentWidthEd', width)

  @overload(float)
  def setDocumentMargin(self, margin: float) -> None:
    """
    Calls Qt's 'void QTextDocument::setDocumentMargin(qreal margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setDocumentMargin

    Parameters
    ----------

    margin : float
      Passed on as it is.
    """
    #  void QTextDocument::setDocumentMargin(qreal margin)
    self.uglySide.call(
        'ritual_ZN13QTextDocument17setDocumentMarginEd', margin,
    )

  @overload(str)
  def setDefaultStyleSheet(self, sheet: str) -> None:
    """
    Calls Qt's 'void QTextDocument::setDefaultStyleSheet(const QString
    &sheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setDefaultStyleSheet

    Parameters
    ----------

    sheet : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextDocument::setDefaultStyleSheet(const QString &sheet)
    self.uglySide.call(
        'ritual_ZN13QTextDocument20setDefaultStyleSheetERK7QString', sheet,
    )

  @overload(int)
  def setMaximumBlockCount(self, maximum: int) -> None:
    """
    Calls Qt's 'void QTextDocument::setMaximumBlockCount(int maximum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setMaximumBlockCount

    Parameters
    ----------

    maximum : int
      Passed on as it is.
    """
    #  void QTextDocument::setMaximumBlockCount(int maximum)
    self.uglySide.call(
        'ritual_ZN13QTextDocument20setMaximumBlockCountEi', maximum,
    )

  @overload(QTextOption)
  def setDefaultTextOption(self, option: QTextOption) -> None:
    """
    Calls Qt's 'void QTextDocument::setDefaultTextOption(const QTextOption
    &option)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setDefaultTextOption

    Parameters
    ----------

    option : QTextOption
      Passed on as a value: Qt reads the C++ QTextOption, which stays
      Python's own.
    """
    #  void QTextDocument::setDefaultTextOption(const QTextOption &option)
    self.uglySide.call(
        'ritual_ZN13QTextDocument20setDefaultTextOptionERK11QTextOption',
        self._valueOf(option),
    )

  @overload(QUrl)
  def setBaseUrl(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QTextDocument::setBaseUrl(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#setBaseUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QTextDocument::setBaseUrl(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN13QTextDocument10setBaseUrlERK4QUrl', self._valueOf(url),
    )

  @overload(Qt.CursorMoveStyle)
  def setDefaultCursorMoveStyle(self, style: Qt.CursorMoveStyle) -> None:
    """
    Calls Qt's 'void
    QTextDocument::setDefaultCursorMoveStyle(Qt::CursorMoveStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#setDefaultCursorMoveStyle

    Parameters
    ----------

    style : Qt.CursorMoveStyle
      Passed on as its number.
    """
    #  void QTextDocument::setDefaultCursorMoveStyle(Qt::CursorMoveStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN13QTextDocument25setDefaultCursorMoveStyleEN2Qt15CursorMo'
        'veStyleE',
        style.value,
    )

  @overload()
  @overload(bool)
  def setModified(self, m: bool = True) -> None:
    """
    Calls Qt's 'void QTextDocument::setModified(bool m)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#setModified

    Parameters
    ----------

    m : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QTextDocument::setModified(bool m)
    self.uglySide.call('ritual_ZN13QTextDocument11setModifiedEb', m)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QTextDocument::QTextDocument(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#QTextDocument

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextDocument::QTextDocument(QObject *parent)
    self._noteCreation(QTextDocument, lambda: Rituals.call(
        'ritual_ZN13QTextDocumentC1EP7QObject', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, text: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QTextDocument::QTextDocument(const
    QString &text, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#QTextDocument

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextDocument::QTextDocument(const QString &text, QObject *parent)
    self._noteCreation(QTextDocument, lambda: Rituals.call(
        'ritual_ZN13QTextDocumentC1ERK7QStringP7QObject',
        text, self._addressOf(parent),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QTextDocument::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#clear
    """
    #  void QTextDocument::clear()
    self.uglySide.call('ritual_ZN13QTextDocument5clearEv')

  @overload(QPagedPaintDevice)
  @overload(NoneType)
  def print(self, printer: Optional[QPagedPaintDevice]) -> None:
    """
    Calls Qt's 'void QTextDocument::print(QPagedPaintDevice *printer) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#print

    Parameters
    ----------

    printer : Optional[QPagedPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocument::print(QPagedPaintDevice *printer) const
    self.uglySide.call(
        'ritual_ZNK13QTextDocument5printEP17QPagedPaintDevice',
        self._addressOf(printer),
    )

  @overload(int, QUrl, QVariant)
  def addResource(self, type: int, name: QUrl, resource: QVariant) -> None:
    """
    Calls Qt's 'void QTextDocument::addResource(int type, const QUrl &name,
    const QVariant &resource)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#addResource

    Parameters
    ----------

    type : int
      Passed on as it is.

    name : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    resource : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QTextDocument::addResource(int type, const QUrl &name, const
    #      QVariant &resource)
    self.uglySide.call(
        'ritual_ZN13QTextDocument11addResourceEiRK4QUrlRK8QVariant',
        type, self._valueOf(name), self._valueOf(resource),
    )

  @overload(int, int)
  def markContentsDirty(self, from_: int, length: int) -> None:
    """
    Calls Qt's 'void QTextDocument::markContentsDirty(int from, int length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#markContentsDirty

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QTextDocument::markContentsDirty(int from, int length)
    self.uglySide.call(
        'ritual_ZN13QTextDocument17markContentsDirtyEii', from_, length,
    )

  @overload(QPainter)
  @overload(NoneType)
  @overload(QPainter, QRectF)
  @overload(NoneType, QRectF)
  def drawContents(
      self,
      painter: Optional[QPainter],
      rect: Optional[QRectF] = None,
  ) -> None:
    """
    Calls Qt's 'void QTextDocument::drawContents(QPainter *painter, const
    QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#drawContents

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : Optional[QRectF]
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own. May be left out, as in Qt: a new 'QRectF()' is then passed on.
    """
    #  void QTextDocument::drawContents(QPainter *painter, const QRectF
    #      &rect)
    if rect is None:
      from ..QtCore import QRectF
      rect = QRectF()
    self.uglySide.call(
        'ritual_ZN13QTextDocument12drawContentsEP8QPainterRK6QRectF',
        self._addressOf(painter), self._valueOf(rect),
    )

  def adjustSize(self) -> None:
    """
    Calls Qt's 'void QTextDocument::adjustSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#adjustSize
    """
    #  void QTextDocument::adjustSize()
    self.uglySide.call('ritual_ZN13QTextDocument10adjustSizeEv')

  @overload(QTextCursor)
  @overload(NoneType)
  def undo(self, cursor: Optional[QTextCursor]) -> None:
    """
    Calls Qt's 'void QTextDocument::undo(QTextCursor *cursor)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#undo

    Parameters
    ----------

    cursor : Optional[QTextCursor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocument::undo(QTextCursor *cursor)
    self.uglySide.call(
        'ritual_ZN13QTextDocument4undoEP11QTextCursor',
        self._addressOf(cursor),
    )

  @overload()
  def undo(self) -> None:
    """
    Calls Qt's 'void QTextDocument::undo()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#undo
    """
    #  void QTextDocument::undo()
    self.uglySide.call('ritual_ZN13QTextDocument4undoEv')

  @overload(QTextCursor)
  @overload(NoneType)
  def redo(self, cursor: Optional[QTextCursor]) -> None:
    """
    Calls Qt's 'void QTextDocument::redo(QTextCursor *cursor)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#redo

    Parameters
    ----------

    cursor : Optional[QTextCursor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocument::redo(QTextCursor *cursor)
    self.uglySide.call(
        'ritual_ZN13QTextDocument4redoEP11QTextCursor',
        self._addressOf(cursor),
    )

  @overload()
  def redo(self) -> None:
    """
    Calls Qt's 'void QTextDocument::redo()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#redo
    """
    #  void QTextDocument::redo()
    self.uglySide.call('ritual_ZN13QTextDocument4redoEv')

  @overload()
  @overload(Stacks)
  def clearUndoRedoStacks(
      self,
      historyToClear: Stacks = Stacks.UndoAndRedoStacks,
  ) -> None:
    """
    Calls Qt's 'void QTextDocument::clearUndoRedoStacks(Stacks
    historyToClear)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextdocument.html#clearUndoRedoStacks

    Parameters
    ----------

    historyToClear : Stacks
      Passed on as its number. May be left out, as in Qt: it is then
      Stacks.UndoAndRedoStacks.
    """
    #  void QTextDocument::clearUndoRedoStacks(Stacks historyToClear)
    self.uglySide.call(
        'ritual_ZN13QTextDocument19clearUndoRedoStacksENS_6StacksE',
        historyToClear.value,
    )

  @overload(QAbstractUndoItem)
  @overload(NoneType)
  def appendUndoItem(self, a0: Optional[QAbstractUndoItem]) -> None:
    """
    Calls Qt's 'void QTextDocument::appendUndoItem(QAbstractUndoItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextdocument.html#appendUndoItem

    Parameters
    ----------

    a0 : Optional[QAbstractUndoItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextDocument::appendUndoItem(QAbstractUndoItem *a0)
    self.uglySide.call(
        'ritual_ZN13QTextDocument14appendUndoItemEP17QAbstractUndoItem',
        self._addressOf(a0),
    )
