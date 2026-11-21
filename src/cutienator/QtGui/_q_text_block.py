"""
QTextBlock binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QTextBlockFormat, QTextBlockUserData, QTextCharFormat
  from . import QTextDocument, QTextLayout
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextBlockUserData = WAIT['QTextBlockUserData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextBlock(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextBlock: a plain Python object standing in front
  of one C++ QTextBlock.

  C++ hands a QTextBlock around as a copy, so every C++ QTextBlock behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextBlock that has a ritual and that Python can
  call so far, 28 names in all: 'isValid', 'position', 'length', 'contains',
  'layout', 'clearLayout', 'blockFormat', 'blockFormatIndex', 'charFormat',
  'charFormatIndex', 'textDirection', 'text', 'document', 'userData',
  'setUserData', 'userState', 'setUserState', 'revision', 'setRevision',
  'isVisible', 'setVisible', 'blockNumber', 'firstLineNumber',
  'setLineCount', 'lineCount', 'next', 'previous', 'fragmentIndex'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QTextBlock::operator==(const QTextBlock &o) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextBlock::operator!=(const QTextBlock &o) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextBlock::operator<(const QTextBlock &o) const': an
    operator, which is not reflected yet.
  - Qt's 'QTextList *QTextBlock::textList() const': gives 'QTextList', which
    has no cute class yet.
  - Qt's 'iterator QTextBlock::begin() const': gives 'QTextBlock::iterator',
    which has no cute class yet.
  - Qt's 'iterator QTextBlock::end() const': gives 'QTextBlock::iterator',
    which has no cute class yet.
  - Qt's 'QTextBlock::~QTextBlock()': the destructor: Python removes its C++
    QTextBlock by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 40 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QTextBlock is created at the first use, not by 'QTextBlock(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextBlock back gives a copy the ritual made for
    Python, in a new cute QTextBlock.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextBlock'

  #  Qt's '~QTextBlock()'. Naming it makes this a value class: Python owns
  #  every C++ QTextBlock behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QTextBlockD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextBlock::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#isValid
    """
    #  bool QTextBlock::isValid() const
    return self.uglySide.call('ritual_ZNK10QTextBlock7isValidEv')

  def position(self) -> int:
    """
    Calls Qt's 'int QTextBlock::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#position
    """
    #  int QTextBlock::position() const
    return self.uglySide.call('ritual_ZNK10QTextBlock8positionEv')

  def length(self) -> int:
    """
    Calls Qt's 'int QTextBlock::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#length
    """
    #  int QTextBlock::length() const
    return self.uglySide.call('ritual_ZNK10QTextBlock6lengthEv')

  @overload(int)
  def contains(self, position: int) -> bool:
    """
    Calls Qt's 'bool QTextBlock::contains(int position) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#contains

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  bool QTextBlock::contains(int position) const
    return self.uglySide.call('ritual_ZNK10QTextBlock8containsEi', position)

  def layout(self) -> Optional[QTextLayout]:
    """
    Calls Qt's 'QTextLayout *QTextBlock::layout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#layout

    Returns
    -------

    Optional[QTextLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextLayout *QTextBlock::layout() const
    address = self.uglySide.call('ritual_ZNK10QTextBlock6layoutEv')
    from . import QTextLayout
    return QTextLayout._cuteAt(address)

  def blockFormat(self) -> QTextBlockFormat:
    """
    Calls Qt's 'QTextBlockFormat QTextBlock::blockFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#blockFormat

    Returns
    -------

    QTextBlockFormat
      A new cute QTextBlockFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextBlockFormat QTextBlock::blockFormat() const
    address = self.uglySide.call('ritual_ZNK10QTextBlock11blockFormatEv')
    from . import QTextBlockFormat
    return QTextBlockFormat._cuteOwning(address)

  def blockFormatIndex(self) -> int:
    """
    Calls Qt's 'int QTextBlock::blockFormatIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#blockFormatIndex
    """
    #  int QTextBlock::blockFormatIndex() const
    return self.uglySide.call('ritual_ZNK10QTextBlock16blockFormatIndexEv')

  def charFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextBlock::charFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#charFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextBlock::charFormat() const
    address = self.uglySide.call('ritual_ZNK10QTextBlock10charFormatEv')
    from . import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def charFormatIndex(self) -> int:
    """
    Calls Qt's 'int QTextBlock::charFormatIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#charFormatIndex
    """
    #  int QTextBlock::charFormatIndex() const
    return self.uglySide.call('ritual_ZNK10QTextBlock15charFormatIndexEv')

  def textDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QTextBlock::textDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#textDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QTextBlock::textDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK10QTextBlock13textDirectionEv',
    ))

  def text(self) -> str:
    """
    Calls Qt's 'QString QTextBlock::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextBlock::text() const
    return self.uglySide.call('ritual_ZNK10QTextBlock4textEv')

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'const QTextDocument *QTextBlock::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QTextDocument *QTextBlock::document() const
    address = self.uglySide.call('ritual_ZNK10QTextBlock8documentEv')
    from . import QTextDocument
    return QTextDocument._cuteAt(address)

  def userData(self) -> Optional[QTextBlockUserData]:
    """
    Calls Qt's 'QTextBlockUserData *QTextBlock::userData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#userData

    Returns
    -------

    Optional[QTextBlockUserData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextBlockUserData *QTextBlock::userData() const
    address = self.uglySide.call('ritual_ZNK10QTextBlock8userDataEv')
    from . import QTextBlockUserData
    return QTextBlockUserData._cuteAt(address)

  def userState(self) -> int:
    """
    Calls Qt's 'int QTextBlock::userState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#userState
    """
    #  int QTextBlock::userState() const
    return self.uglySide.call('ritual_ZNK10QTextBlock9userStateEv')

  def revision(self) -> int:
    """
    Calls Qt's 'int QTextBlock::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#revision
    """
    #  int QTextBlock::revision() const
    return self.uglySide.call('ritual_ZNK10QTextBlock8revisionEv')

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QTextBlock::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#isVisible
    """
    #  bool QTextBlock::isVisible() const
    return self.uglySide.call('ritual_ZNK10QTextBlock9isVisibleEv')

  def blockNumber(self) -> int:
    """
    Calls Qt's 'int QTextBlock::blockNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#blockNumber
    """
    #  int QTextBlock::blockNumber() const
    return self.uglySide.call('ritual_ZNK10QTextBlock11blockNumberEv')

  def firstLineNumber(self) -> int:
    """
    Calls Qt's 'int QTextBlock::firstLineNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#firstLineNumber
    """
    #  int QTextBlock::firstLineNumber() const
    return self.uglySide.call('ritual_ZNK10QTextBlock15firstLineNumberEv')

  def lineCount(self) -> int:
    """
    Calls Qt's 'int QTextBlock::lineCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#lineCount
    """
    #  int QTextBlock::lineCount() const
    return self.uglySide.call('ritual_ZNK10QTextBlock9lineCountEv')

  def next(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextBlock::next() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#next

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextBlock::next() const
    address = self.uglySide.call('ritual_ZNK10QTextBlock4nextEv')
    return QTextBlock._cuteOwning(address)

  def previous(self) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextBlock::previous() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#previous

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextBlock::previous() const
    address = self.uglySide.call('ritual_ZNK10QTextBlock8previousEv')
    return QTextBlock._cuteOwning(address)

  def fragmentIndex(self) -> int:
    """
    Calls Qt's 'int QTextBlock::fragmentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#fragmentIndex
    """
    #  int QTextBlock::fragmentIndex() const
    return self.uglySide.call('ritual_ZNK10QTextBlock13fragmentIndexEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextBlockUserData)
  @overload(NoneType)
  def setUserData(self, data: Optional[QTextBlockUserData]) -> None:
    """
    Calls Qt's 'void QTextBlock::setUserData(QTextBlockUserData *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#setUserData

    Parameters
    ----------

    data : Optional[QTextBlockUserData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextBlock::setUserData(QTextBlockUserData *data)
    self.uglySide.call(
        'ritual_ZN10QTextBlock11setUserDataEP18QTextBlockUserData',
        self._addressOf(data),
    )

  @overload(int)
  def setUserState(self, state: int) -> None:
    """
    Calls Qt's 'void QTextBlock::setUserState(int state)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#setUserState

    Parameters
    ----------

    state : int
      Passed on as it is.
    """
    #  void QTextBlock::setUserState(int state)
    self.uglySide.call('ritual_ZN10QTextBlock12setUserStateEi', state)

  @overload(int)
  def setRevision(self, rev: int) -> None:
    """
    Calls Qt's 'void QTextBlock::setRevision(int rev)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#setRevision

    Parameters
    ----------

    rev : int
      Passed on as it is.
    """
    #  void QTextBlock::setRevision(int rev)
    self.uglySide.call('ritual_ZN10QTextBlock11setRevisionEi', rev)

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QTextBlock::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QTextBlock::setVisible(bool visible)
    self.uglySide.call('ritual_ZN10QTextBlock10setVisibleEb', visible)

  @overload(int)
  def setLineCount(self, count: int) -> None:
    """
    Calls Qt's 'void QTextBlock::setLineCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#setLineCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QTextBlock::setLineCount(int count)
    self.uglySide.call('ritual_ZN10QTextBlock12setLineCountEi', count)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTextBlock::QTextBlock()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#QTextBlock
    """
    #  QTextBlock::QTextBlock()
    self._noteCreation(QTextBlock, lambda: Rituals.call(
        'ritual_ZN10QTextBlockC1Ev',
    ))

  @overload(THIS)
  def __init__(self, o: QTextBlock) -> None:
    """
    Notes what was given, for Qt's 'QTextBlock::QTextBlock(const QTextBlock
    &o)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#QTextBlock

    Parameters
    ----------

    o : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  QTextBlock::QTextBlock(const QTextBlock &o)
    self._noteCreation(QTextBlock, lambda: Rituals.call(
        'ritual_ZN10QTextBlockC1ERKS_', self._valueOf(o),
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

  def clearLayout(self) -> None:
    """
    Calls Qt's 'void QTextBlock::clearLayout()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextblock.html#clearLayout
    """
    #  void QTextBlock::clearLayout()
    self.uglySide.call('ritual_ZN10QTextBlock11clearLayoutEv')
