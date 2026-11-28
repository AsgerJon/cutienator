"""
QQuickTextSelection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextselection_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTextSelection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QColor, QFont, QTextCharFormat, QTextCursor
  from . import QQuickTextDocument
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QFont = WAIT['QFont']
  QQuickTextDocument = WAIT['QQuickTextDocument']
  QTextCharFormat = WAIT['QTextCharFormat']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextSelection(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickTextSelection: a plain Python object standing
  in front of one C++ QQuickTextSelection.

  It is built on the cute 'QObject', as Qt's QQuickTextSelection is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickTextSelection is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextSelection that has a ritual and that
  Python can call so far, 32 names in all: 'metaObject', 'tr', 'classBegin',
  'componentComplete', 'document', 'setDocument', 'selectionStart',
  'setSelectionStart', 'selectionEnd', 'setSelectionEnd', 'text', 'setText',
  'font', 'setFont', 'color', 'setColor', 'alignment', 'setAlignment',
  'moveSelectionStart', 'moveSelectionEnd', 'duplicate', 'linkTo',
  'documentChanged', 'selectionStartChanged', 'selectionEndChanged',
  'textChanged', 'fontChanged', 'colorChanged', 'alignmentChanged', 'cursor',
  'updateFromCharFormat', 'updateFromBlockFormat'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextSelection::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickTextSelection::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 37 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTextSelection is created at the first use, not by
    'QQuickTextSelection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextSelection.
  - Qt tells when it has removed the C++ QQuickTextSelection. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickTextSelection, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class MoveOperation(CuteNum):
    """
    The enum 'QQuickTextSelection::MoveOperation' of Qt, with the 25 names Qt
    gives in it.
    """

    NoMove = Kee[int](0)
    Start = Kee[int](1)
    Up = Kee[int](2)
    StartOfLine = Kee[int](3)
    StartOfBlock = Kee[int](4)
    StartOfWord = Kee[int](5)
    PreviousBlock = Kee[int](6)
    PreviousCharacter = Kee[int](7)
    PreviousWord = Kee[int](8)
    Left = Kee[int](9)
    WordLeft = Kee[int](10)
    End = Kee[int](11)
    Down = Kee[int](12)
    EndOfLine = Kee[int](13)
    EndOfWord = Kee[int](14)
    EndOfBlock = Kee[int](15)
    NextBlock = Kee[int](16)
    NextCharacter = Kee[int](17)
    NextWord = Kee[int](18)
    Right = Kee[int](19)
    WordRight = Kee[int](20)
    NextCell = Kee[int](21)
    PreviousCell = Kee[int](22)
    NextRow = Kee[int](23)
    PreviousRow = Kee[int](24)

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
    Calls Qt's 'QString QQuickTextSelection::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#tr

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
    #  QString QQuickTextSelection::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickTextSelection2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextSelection'

  #  Qt's QQuickTextSelection is built on more than one class. The part of a
  #  C++ QQuickTextSelection that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickTextSelection_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *QQuickTextSelection::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextSelection::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickTextSelection10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def document(self) -> Optional[QQuickTextDocument]:
    """
    Calls Qt's 'QQuickTextDocument *QQuickTextSelection::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#document

    Returns
    -------

    Optional[QQuickTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextDocument *QQuickTextSelection::document() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickTextSelection8documentEv',
    )
    from . import QQuickTextDocument
    return QQuickTextDocument._cuteAt(address)

  def selectionStart(self) -> int:
    """
    Calls Qt's 'int QQuickTextSelection::selectionStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#selectionStart
    """
    #  int QQuickTextSelection::selectionStart() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickTextSelection14selectionStartEv',
    )

  def selectionEnd(self) -> int:
    """
    Calls Qt's 'int QQuickTextSelection::selectionEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#selectionEnd
    """
    #  int QQuickTextSelection::selectionEnd() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickTextSelection12selectionEndEv',
    )

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickTextSelection::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextSelection::text() const
    return self.uglySide.call('ritual_ZNK19QQuickTextSelection4textEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickTextSelection::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTextSelection::font() const
    address = self.uglySide.call('ritual_ZNK19QQuickTextSelection4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickTextSelection::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickTextSelection::color() const
    address = self.uglySide.call('ritual_ZNK19QQuickTextSelection5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QQuickTextSelection::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QQuickTextSelection::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK19QQuickTextSelection9alignmentEv',
    ))

  def cursor(self) -> QTextCursor:
    """
    Calls Qt's 'QTextCursor QQuickTextSelection::cursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#cursor

    Returns
    -------

    QTextCursor
      A new cute QTextCursor around the copy Qt gave back. Python owns it.
    """
    #  QTextCursor QQuickTextSelection::cursor() const
    address = self.uglySide.call('ritual_ZNK19QQuickTextSelection6cursorEv')
    from ..QtGui import QTextCursor
    return QTextCursor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickTextDocument)
  @overload(NoneType)
  def setDocument(self, doc: Optional[QQuickTextDocument]) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::setDocument(QQuickTextDocument
    *doc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#setDocument

    Parameters
    ----------

    doc : Optional[QQuickTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextSelection::setDocument(QQuickTextDocument *doc)
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection11setDocumentEP18QQuickTextDocument',
        self._addressOf(doc),
    )

  @overload(int)
  def setSelectionStart(self, start: int) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::setSelectionStart(int start)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#setSelectionStart

    Parameters
    ----------

    start : int
      Passed on as it is.
    """
    #  void QQuickTextSelection::setSelectionStart(int start)
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection17setSelectionStartEi', start,
    )

  @overload(int)
  def setSelectionEnd(self, end: int) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::setSelectionEnd(int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#setSelectionEnd

    Parameters
    ----------

    end : int
      Passed on as it is.
    """
    #  void QQuickTextSelection::setSelectionEnd(int end)
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection15setSelectionEndEi', end,
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextSelection::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection7setTextERK7QString', text,
    )

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickTextSelection::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection7setFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::setColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickTextSelection::setColor(QColor color)
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection8setColorE6QColor',
        self._valueOf(color),
    )

  @overload(Qt.Alignment)
  def setAlignment(self, align: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::setAlignment(Qt::Alignment align)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#setAlignment

    Parameters
    ----------

    align : Qt.Alignment
      Passed on as its number.
    """
    #  void QQuickTextSelection::setAlignment(Qt::Alignment align)
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection12setAlignmentE6QFlagsIN2Qt13Alignme'
        'ntFlagEE',
        align.value,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTextSelection::QQuickTextSelection(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#QQuickTextSelection

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTextSelection::QQuickTextSelection(QObject *parent)
    self._noteCreation(QQuickTextSelection, lambda: Rituals.call(
        'ritual_ZN19QQuickTextSelectionC1EP7QObject',
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#classBegin
    """
    #  void QQuickTextSelection::classBegin()
    ritual = 'ritual_ZN19QQuickTextSelection10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickTextSelection10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#componentComplete
    """
    #  void QQuickTextSelection::componentComplete()
    ritual = 'ritual_ZN19QQuickTextSelection17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickTextSelection17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(MoveOperation)
  @overload(MoveOperation, int)
  def moveSelectionStart(self, op: MoveOperation, n: int = 1) -> bool:
    """
    Calls Qt's 'bool QQuickTextSelection::moveSelectionStart(MoveOperation
    op, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#moveSelectionStart

    Parameters
    ----------

    op : MoveOperation
      Passed on as its number.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  bool QQuickTextSelection::moveSelectionStart(MoveOperation op, int n)
    return self.uglySide.call(
        'ritual_ZN19QQuickTextSelection18moveSelectionStartENS_13MoveOperat'
        'ionEi',
        op.value, n,
    )

  @overload(MoveOperation)
  @overload(MoveOperation, int)
  def moveSelectionEnd(self, op: MoveOperation, n: int = 1) -> bool:
    """
    Calls Qt's 'bool QQuickTextSelection::moveSelectionEnd(MoveOperation op,
    int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#moveSelectionEnd

    Parameters
    ----------

    op : MoveOperation
      Passed on as its number.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  bool QQuickTextSelection::moveSelectionEnd(MoveOperation op, int n)
    return self.uglySide.call(
        'ritual_ZN19QQuickTextSelection16moveSelectionEndENS_13MoveOperatio'
        'nEi',
        op.value, n,
    )

  def duplicate(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::duplicate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#duplicate
    """
    #  void QQuickTextSelection::duplicate()
    self.uglySide.call('ritual_ZN19QQuickTextSelection9duplicateEv')

  @overload(QUrl)
  def linkTo(self, destination: QUrl) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::linkTo(const QUrl &destination)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextselection.html#linkTo

    Parameters
    ----------

    destination : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickTextSelection::linkTo(const QUrl &destination)
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection6linkToERK4QUrl',
        self._valueOf(destination),
    )

  def documentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::documentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#documentChanged
    """
    #  void QQuickTextSelection::documentChanged()
    self.uglySide.call('ritual_ZN19QQuickTextSelection15documentChangedEv')

  def selectionStartChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::selectionStartChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#selectionStartChanged
    """
    #  void QQuickTextSelection::selectionStartChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection21selectionStartChangedEv',
    )

  def selectionEndChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::selectionEndChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#selectionEndChanged
    """
    #  void QQuickTextSelection::selectionEndChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection19selectionEndChangedEv',
    )

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::textChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#textChanged
    """
    #  void QQuickTextSelection::textChanged()
    self.uglySide.call('ritual_ZN19QQuickTextSelection11textChangedEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::fontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#fontChanged
    """
    #  void QQuickTextSelection::fontChanged()
    self.uglySide.call('ritual_ZN19QQuickTextSelection11fontChangedEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#colorChanged
    """
    #  void QQuickTextSelection::colorChanged()
    self.uglySide.call('ritual_ZN19QQuickTextSelection12colorChangedEv')

  def alignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::alignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#alignmentChanged
    """
    #  void QQuickTextSelection::alignmentChanged()
    self.uglySide.call('ritual_ZN19QQuickTextSelection16alignmentChangedEv')

  @overload(QTextCharFormat)
  def updateFromCharFormat(self, fmt: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::updateFromCharFormat(const
    QTextCharFormat &fmt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#updateFromCharFormat

    Parameters
    ----------

    fmt : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QQuickTextSelection::updateFromCharFormat(const QTextCharFormat
    #      &fmt)
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection20updateFromCharFormatERK15QTextChar'
        'Format',
        self._valueOf(fmt),
    )

  def updateFromBlockFormat(self) -> None:
    """
    Calls Qt's 'void QQuickTextSelection::updateFromBlockFormat()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextselection.html#updateFromBlockFormat
    """
    #  void QQuickTextSelection::updateFromBlockFormat()
    self.uglySide.call(
        'ritual_ZN19QQuickTextSelection21updateFromBlockFormatEv',
    )
