"""
QSyntaxHighlighter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qsyntaxhighlighter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QColor, QFont, QTextBlock, QTextBlockUserData
  from . import QTextCharFormat, QTextDocument
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QTextBlock = WAIT['QTextBlock']
  QTextBlockUserData = WAIT['QTextBlockUserData']
  QTextCharFormat = WAIT['QTextCharFormat']
  QTextDocument = WAIT['QTextDocument']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSyntaxHighlighter(QObject):
  """
  The cute side of Qt's QSyntaxHighlighter: a plain Python object standing in
  front of one C++ QSyntaxHighlighter.

  It is built on the cute 'QObject', as Qt's QSyntaxHighlighter is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSyntaxHighlighter that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'setDocument',
  'document', 'rehighlight', 'rehighlightBlock', 'highlightBlock',
  'setFormat', 'format', 'previousBlockState', 'currentBlockState',
  'setCurrentBlockState', 'setCurrentBlockUserData', 'currentBlockUserData',
  'currentBlock'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSyntaxHighlighter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSyntaxHighlighter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSyntaxHighlighterPrivate *QSyntaxHighlighter::d_func()': gives
    'QSyntaxHighlighterPrivate', which has no cute class yet.
  - Qt's 'const QSyntaxHighlighterPrivate *QSyntaxHighlighter::d_func()
    const': gives 'QSyntaxHighlighterPrivate', which has no cute class yet.
  - Qt's 'QSyntaxHighlighter::~QSyntaxHighlighter()': the destructor: Python
    never removes a C++ QSyntaxHighlighter.

  What has no ritual
  ------------------

  4 of the 28 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSyntaxHighlighter is created at the first use, not by
    'QSyntaxHighlighter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSyntaxHighlighter.
  - Qt tells when it has removed the C++ QSyntaxHighlighter. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QSyntaxHighlighter::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsyntaxhighlighter.html#tr

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
    #  QString QSyntaxHighlighter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QSyntaxHighlighter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSyntaxHighlighter'

  #  A C++ QSyntaxHighlighter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSyntaxHighlighter'

  #  The functions Qt calls itself that QSyntaxHighlighter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'highlightBlock': (
          ('_ZN18QSyntaxHighlighter14highlightBlockERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSyntaxHighlighter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsyntaxhighlighter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSyntaxHighlighter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QSyntaxHighlighter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QSyntaxHighlighter::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsyntaxhighlighter.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QSyntaxHighlighter::document() const
    address = self.uglySide.call('ritual_ZNK18QSyntaxHighlighter8documentEv')
    from . import QTextDocument
    return QTextDocument._cuteAt(address)

  @overload(int)
  def format(self, pos: int) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QSyntaxHighlighter::format(int pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsyntaxhighlighter.html#format

    Parameters
    ----------

    pos : int
      Passed on as it is.

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QSyntaxHighlighter::format(int pos) const
    address = self.uglySide.call(
        'ritual_ZNK18QSyntaxHighlighter6formatEi', pos,
    )
    from . import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def previousBlockState(self) -> int:
    """
    Calls Qt's 'int QSyntaxHighlighter::previousBlockState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#previousBlockState
    """
    #  int QSyntaxHighlighter::previousBlockState() const
    return self.uglySide.call(
        'ritual_ZNK18QSyntaxHighlighter18previousBlockStateEv',
    )

  def currentBlockState(self) -> int:
    """
    Calls Qt's 'int QSyntaxHighlighter::currentBlockState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#currentBlockState
    """
    #  int QSyntaxHighlighter::currentBlockState() const
    return self.uglySide.call(
        'ritual_ZNK18QSyntaxHighlighter17currentBlockStateEv',
    )

  def currentBlockUserData(self) -> Optional[QTextBlockUserData]:
    """
    Calls Qt's 'QTextBlockUserData
    *QSyntaxHighlighter::currentBlockUserData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#currentBlockUserData

    Returns
    -------

    Optional[QTextBlockUserData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextBlockUserData *QSyntaxHighlighter::currentBlockUserData() const
    address = self.uglySide.call(
        'ritual_ZNK18QSyntaxHighlighter20currentBlockUserDataEv',
    )
    from . import QTextBlockUserData
    return QTextBlockUserData._cuteAt(address)

  def currentBlock(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QSyntaxHighlighter::currentBlock() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#currentBlock

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QSyntaxHighlighter::currentBlock() const
    address = self.uglySide.call(
        'ritual_ZNK18QSyntaxHighlighter12currentBlockEv',
    )
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextDocument)
  @overload(NoneType)
  def setDocument(self, doc: Optional[QTextDocument]) -> None:
    """
    Calls Qt's 'void QSyntaxHighlighter::setDocument(QTextDocument *doc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#setDocument

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSyntaxHighlighter::setDocument(QTextDocument *doc)
    self.uglySide.call(
        'ritual_ZN18QSyntaxHighlighter11setDocumentEP13QTextDocument',
        self._addressOf(doc),
    )

  @overload(int, int, QTextCharFormat)
  def setFormat(
      self,
      start: int,
      count: int,
      format: QTextCharFormat,
  ) -> None:
    """
    Calls Qt's 'void QSyntaxHighlighter::setFormat(int start, int count,
    const QTextCharFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qsyntaxhighlighter.html#setFormat

    Parameters
    ----------

    start : int
      Passed on as it is.

    count : int
      Passed on as it is.

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QSyntaxHighlighter::setFormat(int start, int count, const
    #      QTextCharFormat &format)
    self.uglySide.call(
        'ritual_ZN18QSyntaxHighlighter9setFormatEiiRK15QTextCharFormat',
        start, count, self._valueOf(format),
    )

  @overload(int, int, QColor)
  def setFormat(self, start: int, count: int, color: QColor) -> None:
    """
    Calls Qt's 'void QSyntaxHighlighter::setFormat(int start, int count,
    const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsyntaxhighlighter.html#setFormat

    Parameters
    ----------

    start : int
      Passed on as it is.

    count : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSyntaxHighlighter::setFormat(int start, int count, const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN18QSyntaxHighlighter9setFormatEiiRK6QColor',
        start, count, self._valueOf(color),
    )

  @overload(int, int, QFont)
  def setFormat(self, start: int, count: int, font: QFont) -> None:
    """
    Calls Qt's 'void QSyntaxHighlighter::setFormat(int start, int count,
    const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qsyntaxhighlighter.html#setFormat

    Parameters
    ----------

    start : int
      Passed on as it is.

    count : int
      Passed on as it is.

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QSyntaxHighlighter::setFormat(int start, int count, const QFont
    #      &font)
    self.uglySide.call(
        'ritual_ZN18QSyntaxHighlighter9setFormatEiiRK5QFont',
        start, count, self._valueOf(font),
    )

  @overload(int)
  def setCurrentBlockState(self, newState: int) -> None:
    """
    Calls Qt's 'void QSyntaxHighlighter::setCurrentBlockState(int newState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#setCurrentBlockState

    Parameters
    ----------

    newState : int
      Passed on as it is.
    """
    #  void QSyntaxHighlighter::setCurrentBlockState(int newState)
    self.uglySide.call(
        'ritual_ZN18QSyntaxHighlighter20setCurrentBlockStateEi', newState,
    )

  @overload(QTextBlockUserData)
  @overload(NoneType)
  def setCurrentBlockUserData(
      self,
      data: Optional[QTextBlockUserData],
  ) -> None:
    """
    Calls Qt's 'void
    QSyntaxHighlighter::setCurrentBlockUserData(QTextBlockUserData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#setCurrentBlockUserData

    Parameters
    ----------

    data : Optional[QTextBlockUserData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSyntaxHighlighter::setCurrentBlockUserData(QTextBlockUserData
    #      *data)
    self.uglySide.call(
        'ritual_ZN18QSyntaxHighlighter23setCurrentBlockUserDataEP18QTextBlo'
        'ckUserData',
        self._addressOf(data),
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

  @overload(QTextDocument)
  def __init__(self, parent: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's
    'QSyntaxHighlighter::QSyntaxHighlighter(QTextDocument *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#QSyntaxHighlighter

    Parameters
    ----------

    parent : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSyntaxHighlighter::QSyntaxHighlighter(QTextDocument *parent)
    self._noteCreation(QSyntaxHighlighter, lambda: Rituals.call(
        'ritual_ZN18QSyntaxHighlighterC1EP13QTextDocument',
        self._addressOf(parent),
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QSyntaxHighlighter::QSyntaxHighlighter(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#QSyntaxHighlighter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSyntaxHighlighter::QSyntaxHighlighter(QObject *parent)
    self._noteCreation(QSyntaxHighlighter, lambda: Rituals.call(
        'ritual_ZN18QSyntaxHighlighterC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def rehighlight(self) -> None:
    """
    Calls Qt's 'void QSyntaxHighlighter::rehighlight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#rehighlight
    """
    #  void QSyntaxHighlighter::rehighlight()
    self.uglySide.call('ritual_ZN18QSyntaxHighlighter11rehighlightEv')

  @overload(QTextBlock)
  def rehighlightBlock(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QSyntaxHighlighter::rehighlightBlock(const QTextBlock
    &block)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#rehighlightBlock

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QSyntaxHighlighter::rehighlightBlock(const QTextBlock &block)
    self.uglySide.call(
        'ritual_ZN18QSyntaxHighlighter16rehighlightBlockERK10QTextBlock',
        self._valueOf(block),
    )

  @overload(str)
  def highlightBlock(self, text: str) -> None:
    """
    Calls Qt's 'void QSyntaxHighlighter::highlightBlock(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsyntaxhighlighter.html#highlightBlock

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSyntaxHighlighter::highlightBlock(const QString &text)
    self.uglySide.call(
        'ritual_ZN18QSyntaxHighlighter14highlightBlockERK7QString', text,
    )
