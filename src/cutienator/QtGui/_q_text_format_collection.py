"""
QTextFormatCollection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextformat_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextFormatCollection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QFont, QTextBlockFormat, QTextCharFormat, QTextFormat
  from . import QTextImageFormat, QTextListFormat, QTextTableFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QTextFormat = WAIT['QTextFormat']


class QTextFormatCollection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextFormatCollection: a plain Python object standing
  in front of one C++ QTextFormatCollection.

  What exists
  -----------

  Every function of Qt's QTextFormatCollection that has a ritual and that
  Python can call so far, 21 names in all: 'clear', 'objectFormat',
  'setObjectFormat', 'objectFormatIndex', 'setObjectFormatIndex',
  'createObjectIndex', 'indexForFormat', 'hasFormatCached', 'format',
  'blockFormat', 'charFormat', 'listFormat', 'tableFormat', 'imageFormat',
  'numFormats', 'defaultFont', 'setDefaultFont', 'setSuperScriptBaseline',
  'setSubScriptBaseline', 'setBaselineOffset', 'defaultTextFormat'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextFormatCollection::~QTextFormatCollection()': the destructor:
    Python never removes a C++ QTextFormatCollection.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QTextFormatCollection is created at the first use, not by
    'QTextFormatCollection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextFormatCollection.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextFormatCollection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def objectFormat(self, objectIndex: int) -> QTextFormat:
    """
    Calls Qt's 'QTextFormat QTextFormatCollection::objectFormat(int
    objectIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#objectFormat

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.

    Returns
    -------

    QTextFormat
      A new cute QTextFormat around the copy Qt gave back. Python owns it.
    """
    #  QTextFormat QTextFormatCollection::objectFormat(int objectIndex) const
    address = self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection12objectFormatEi', objectIndex,
    )
    from . import QTextFormat
    return QTextFormat._cuteOwning(address)

  @overload(int)
  def objectFormatIndex(self, objectIndex: int) -> int:
    """
    Calls Qt's 'int QTextFormatCollection::objectFormatIndex(int objectIndex)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#objectFormatIndex

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.
    """
    #  int QTextFormatCollection::objectFormatIndex(int objectIndex) const
    return self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection17objectFormatIndexEi',
        objectIndex,
    )

  @overload(QTextFormat)
  def hasFormatCached(self, format: QTextFormat) -> bool:
    """
    Calls Qt's 'bool QTextFormatCollection::hasFormatCached(const QTextFormat
    &format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#hasFormatCached

    Parameters
    ----------

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  bool QTextFormatCollection::hasFormatCached(const QTextFormat &format)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection15hasFormatCachedERK11QTextFormat',
        self._valueOf(format),
    )

  @overload(int)
  def format(self, idx: int) -> QTextFormat:
    """
    Calls Qt's 'QTextFormat QTextFormatCollection::format(int idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformatcollection.html#format

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    QTextFormat
      A new cute QTextFormat around the copy Qt gave back. Python owns it.
    """
    #  QTextFormat QTextFormatCollection::format(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection6formatEi', idx,
    )
    from . import QTextFormat
    return QTextFormat._cuteOwning(address)

  @overload(int)
  def blockFormat(self, index: int) -> QTextBlockFormat:
    """
    Calls Qt's 'QTextBlockFormat QTextFormatCollection::blockFormat(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#blockFormat

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QTextBlockFormat
      A new cute QTextBlockFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextBlockFormat QTextFormatCollection::blockFormat(int index) const
    address = self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection11blockFormatEi', index,
    )
    from . import QTextBlockFormat
    return QTextBlockFormat._cuteOwning(address)

  @overload(int)
  def charFormat(self, index: int) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextFormatCollection::charFormat(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#charFormat

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextFormatCollection::charFormat(int index) const
    address = self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection10charFormatEi', index,
    )
    from . import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  @overload(int)
  def listFormat(self, index: int) -> QTextListFormat:
    """
    Calls Qt's 'QTextListFormat QTextFormatCollection::listFormat(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#listFormat

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QTextListFormat
      A new cute QTextListFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextListFormat QTextFormatCollection::listFormat(int index) const
    address = self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection10listFormatEi', index,
    )
    from . import QTextListFormat
    return QTextListFormat._cuteOwning(address)

  @overload(int)
  def tableFormat(self, index: int) -> QTextTableFormat:
    """
    Calls Qt's 'QTextTableFormat QTextFormatCollection::tableFormat(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#tableFormat

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QTextTableFormat
      A new cute QTextTableFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextTableFormat QTextFormatCollection::tableFormat(int index) const
    address = self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection11tableFormatEi', index,
    )
    from . import QTextTableFormat
    return QTextTableFormat._cuteOwning(address)

  @overload(int)
  def imageFormat(self, index: int) -> QTextImageFormat:
    """
    Calls Qt's 'QTextImageFormat QTextFormatCollection::imageFormat(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#imageFormat

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QTextImageFormat
      A new cute QTextImageFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextImageFormat QTextFormatCollection::imageFormat(int index) const
    address = self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection11imageFormatEi', index,
    )
    from . import QTextImageFormat
    return QTextImageFormat._cuteOwning(address)

  def numFormats(self) -> int:
    """
    Calls Qt's 'int QTextFormatCollection::numFormats() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#numFormats
    """
    #  int QTextFormatCollection::numFormats() const
    return self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection10numFormatsEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QTextFormatCollection::defaultFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QTextFormatCollection::defaultFont() const
    address = self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection11defaultFontEv',
    )
    from . import QFont
    return QFont._cuteOwning(address)

  def defaultTextFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextFormatCollection::defaultTextFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#defaultTextFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextFormatCollection::defaultTextFormat() const
    address = self.uglySide.call(
        'ritual_ZNK21QTextFormatCollection17defaultTextFormatEv',
    )
    from . import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QTextFormat)
  def setObjectFormat(self, objectIndex: int, format: QTextFormat) -> None:
    """
    Calls Qt's 'void QTextFormatCollection::setObjectFormat(int objectIndex,
    const QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#setObjectFormat

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QTextFormatCollection::setObjectFormat(int objectIndex, const
    #      QTextFormat &format)
    self.uglySide.call(
        'ritual_ZN21QTextFormatCollection15setObjectFormatEiRK11QTextFormat',
        objectIndex, self._valueOf(format),
    )

  @overload(int, int)
  def setObjectFormatIndex(self, objectIndex: int, formatIndex: int) -> None:
    """
    Calls Qt's 'void QTextFormatCollection::setObjectFormatIndex(int
    objectIndex, int formatIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#setObjectFormatIndex

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.

    formatIndex : int
      Passed on as it is.
    """
    #  void QTextFormatCollection::setObjectFormatIndex(int objectIndex, int
    #      formatIndex)
    self.uglySide.call(
        'ritual_ZN21QTextFormatCollection20setObjectFormatIndexEii',
        objectIndex, formatIndex,
    )

  @overload(QFont)
  def setDefaultFont(self, f: QFont) -> None:
    """
    Calls Qt's 'void QTextFormatCollection::setDefaultFont(const QFont &f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#setDefaultFont

    Parameters
    ----------

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QTextFormatCollection::setDefaultFont(const QFont &f)
    self.uglySide.call(
        'ritual_ZN21QTextFormatCollection14setDefaultFontERK5QFont',
        self._valueOf(f),
    )

  @overload(float)
  def setSuperScriptBaseline(self, baseline: float) -> None:
    """
    Calls Qt's 'void QTextFormatCollection::setSuperScriptBaseline(qreal
    baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#setSuperScriptBaseline

    Parameters
    ----------

    baseline : float
      Passed on as it is.
    """
    #  void QTextFormatCollection::setSuperScriptBaseline(qreal baseline)
    self.uglySide.call(
        'ritual_ZN21QTextFormatCollection22setSuperScriptBaselineEd',
        baseline,
    )

  @overload(float)
  def setSubScriptBaseline(self, baseline: float) -> None:
    """
    Calls Qt's 'void QTextFormatCollection::setSubScriptBaseline(qreal
    baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#setSubScriptBaseline

    Parameters
    ----------

    baseline : float
      Passed on as it is.
    """
    #  void QTextFormatCollection::setSubScriptBaseline(qreal baseline)
    self.uglySide.call(
        'ritual_ZN21QTextFormatCollection20setSubScriptBaselineEd', baseline,
    )

  @overload(float)
  def setBaselineOffset(self, baseline: float) -> None:
    """
    Calls Qt's 'void QTextFormatCollection::setBaselineOffset(qreal
    baseline)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#setBaselineOffset

    Parameters
    ----------

    baseline : float
      Passed on as it is.
    """
    #  void QTextFormatCollection::setBaselineOffset(qreal baseline)
    self.uglySide.call(
        'ritual_ZN21QTextFormatCollection17setBaselineOffsetEd', baseline,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QTextFormatCollection::QTextFormatCollection()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#QTextFormatCollection
    """
    #  QTextFormatCollection::QTextFormatCollection()
    self._noteCreation(QTextFormatCollection, lambda: Rituals.call(
        'ritual_ZN21QTextFormatCollectionC1Ev',
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
    Calls Qt's 'void QTextFormatCollection::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformatcollection.html#clear
    """
    #  void QTextFormatCollection::clear()
    self.uglySide.call('ritual_ZN21QTextFormatCollection5clearEv')

  @overload(QTextFormat)
  def createObjectIndex(self, f: QTextFormat) -> int:
    """
    Calls Qt's 'int QTextFormatCollection::createObjectIndex(const
    QTextFormat &f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#createObjectIndex

    Parameters
    ----------

    f : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  int QTextFormatCollection::createObjectIndex(const QTextFormat &f)
    return self.uglySide.call(
        'ritual_ZN21QTextFormatCollection17createObjectIndexERK11QTextForma'
        't',
        self._valueOf(f),
    )

  @overload(QTextFormat)
  def indexForFormat(self, f: QTextFormat) -> int:
    """
    Calls Qt's 'int QTextFormatCollection::indexForFormat(const QTextFormat
    &f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformatcollection.html#indexForFormat

    Parameters
    ----------

    f : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  int QTextFormatCollection::indexForFormat(const QTextFormat &f)
    return self.uglySide.call(
        'ritual_ZN21QTextFormatCollection14indexForFormatERK11QTextFormat',
        self._valueOf(f),
    )
