"""
QTextList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextlist.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QTextBlockGroup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QTextBlock, QTextDocument, QTextListFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextBlock = WAIT['QTextBlock']
  QTextDocument = WAIT['QTextDocument']
  QTextListFormat = WAIT['QTextListFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextList(QTextBlockGroup):
  """
  The cute side of Qt's QTextList: a plain Python object standing in front of
  one C++ QTextList.

  It is built on the cute 'QTextBlockGroup', as Qt's QTextList is built on
  Qt's QTextBlockGroup, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextList that has a ritual and that Python can call
  so far, 11 names in all: 'metaObject', 'tr', 'count', 'item', 'itemNumber',
  'itemText', 'removeItem', 'remove', 'add', 'setFormat', 'format'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextList::~QTextList()': the destructor: Python never removes a
    C++ QTextList.

  What has no ritual
  ------------------

  8 of the 21 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QTextList is created at the first use, not by 'QTextList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextList.
  - Qt tells when it has removed the C++ QTextList. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QTextList::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#tr

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
    #  QString QTextList::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QTextList2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextList'

  #  A C++ QTextList Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextList'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextList::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextList::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QTextList10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QTextList::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#count
    """
    #  int QTextList::count() const
    return self.uglySide.call('ritual_ZNK9QTextList5countEv')

  @overload(int)
  def item(self, i: int) -> QTextBlock:
    """
    Calls Qt's 'QTextBlock QTextList::item(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#item

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QTextBlock
      A new cute QTextBlock around the copy Qt gave back. Python owns it.
    """
    #  QTextBlock QTextList::item(int i) const
    address = self.uglySide.call('ritual_ZNK9QTextList4itemEi', i)
    from . import QTextBlock
    return QTextBlock._cuteOwning(address)

  @overload(QTextBlock)
  def itemNumber(self, a0: QTextBlock) -> int:
    """
    Calls Qt's 'int QTextList::itemNumber(const QTextBlock &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#itemNumber

    Parameters
    ----------

    a0 : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  int QTextList::itemNumber(const QTextBlock &a0) const
    return self.uglySide.call(
        'ritual_ZNK9QTextList10itemNumberERK10QTextBlock', self._valueOf(a0),
    )

  @overload(QTextBlock)
  def itemText(self, a0: QTextBlock) -> str:
    """
    Calls Qt's 'QString QTextList::itemText(const QTextBlock &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#itemText

    Parameters
    ----------

    a0 : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextList::itemText(const QTextBlock &a0) const
    return self.uglySide.call(
        'ritual_ZNK9QTextList8itemTextERK10QTextBlock', self._valueOf(a0),
    )

  def format(self) -> QTextListFormat:
    """
    Calls Qt's 'QTextListFormat QTextList::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#format

    Returns
    -------

    QTextListFormat
      A new cute QTextListFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextListFormat QTextList::format() const
    address = self.uglySide.call('ritual_ZNK9QTextList6formatEv')
    from . import QTextListFormat
    return QTextListFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextListFormat)
  def setFormat(self, format: QTextListFormat) -> None:
    """
    Calls Qt's 'void QTextList::setFormat(const QTextListFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#setFormat

    Parameters
    ----------

    format : QTextListFormat
      Passed on as a value: Qt reads the C++ QTextListFormat, which stays
      Python's own.
    """
    #  void QTextList::setFormat(const QTextListFormat &format)
    self.uglySide.call(
        'ritual_ZN9QTextList9setFormatERK15QTextListFormat',
        self._valueOf(format),
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
  @overload(NoneType)
  def __init__(self, doc: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's 'QTextList::QTextList(QTextDocument
    *doc)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#QTextList

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextList::QTextList(QTextDocument *doc)
    self._noteCreation(QTextList, lambda: Rituals.call(
        'ritual_ZN9QTextListC1EP13QTextDocument', self._addressOf(doc),
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

  @overload(int)
  def removeItem(self, i: int) -> None:
    """
    Calls Qt's 'void QTextList::removeItem(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#removeItem

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QTextList::removeItem(int i)
    self.uglySide.call('ritual_ZN9QTextList10removeItemEi', i)

  @overload(QTextBlock)
  def remove(self, a0: QTextBlock) -> None:
    """
    Calls Qt's 'void QTextList::remove(const QTextBlock &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#remove

    Parameters
    ----------

    a0 : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QTextList::remove(const QTextBlock &a0)
    self.uglySide.call(
        'ritual_ZN9QTextList6removeERK10QTextBlock', self._valueOf(a0),
    )

  @overload(QTextBlock)
  def add(self, block: QTextBlock) -> None:
    """
    Calls Qt's 'void QTextList::add(const QTextBlock &block)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlist.html#add

    Parameters
    ----------

    block : QTextBlock
      Passed on as a value: Qt reads the C++ QTextBlock, which stays Python's
      own.
    """
    #  void QTextList::add(const QTextBlock &block)
    self.uglySide.call(
        'ritual_ZN9QTextList3addERK10QTextBlock', self._valueOf(block),
    )
