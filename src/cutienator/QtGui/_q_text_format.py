"""
QTextFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ._q_brush import QBrush
from ._q_color import QColor
from ._q_pen import QPen
from ..QtCore import QVariant
from ._q_text_format_format_type import FormatType
from ._q_text_format_object_types import ObjectTypes
from ._q_text_format_page_break_flag import PageBreakFlag
from ._q_text_format_property import Property


class QTextFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextFormat: a plain Python object standing in front
  of one C++ QTextFormat.

  C++ hands a QTextFormat around as a copy, so every C++ QTextFormat behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextFormat that has a ritual and that Python can
  call so far, 37 names in all: 'merge', 'isValid', 'isEmpty', 'type',
  'objectIndex', 'setObjectIndex', 'property', 'setProperty',
  'clearProperty', 'hasProperty', 'boolProperty', 'intProperty',
  'doubleProperty', 'stringProperty', 'colorProperty', 'penProperty',
  'brushProperty', 'propertyCount', 'setObjectType', 'objectType',
  'isCharFormat', 'isBlockFormat', 'isListFormat', 'isFrameFormat',
  'isImageFormat', 'isTableFormat', 'isTableCellFormat', 'toBlockFormat',
  'toCharFormat', 'setLayoutDirection', 'layoutDirection', 'setBackground',
  'background', 'clearBackground', 'setForeground', 'foreground',
  'clearForeground'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextFormat::~QTextFormat()': the destructor: Python removes its
    C++ QTextFormat by it, and has no other use for it.
  - Qt's 'QTextLength QTextFormat::lengthProperty(int propertyId) const':
    gives 'QTextLength', which has no cute class yet.
  - Qt's 'QTextListFormat QTextFormat::toListFormat() const': gives
    'QTextListFormat', which has no cute class yet.
  - Qt's 'QTextTableFormat QTextFormat::toTableFormat() const': gives
    'QTextTableFormat', which has no cute class yet.
  - Qt's 'QTextFrameFormat QTextFormat::toFrameFormat() const': gives
    'QTextFrameFormat', which has no cute class yet.
  - Qt's 'QTextImageFormat QTextFormat::toImageFormat() const': gives
    'QTextImageFormat', which has no cute class yet.
  - Qt's 'QTextTableCellFormat QTextFormat::toTableCellFormat() const': gives
    'QTextTableCellFormat', which has no cute class yet.
  - Qt's 'bool QTextFormat::operator==(const QTextFormat &rhs) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QTextFormat::operator!=(const QTextFormat &rhs) const': an
    operator, which is not reflected yet.
  - Qt's 'QVariant QTextFormat::operator QVariant() const': an operator,
    which is not reflected yet.

  What has no ritual
  ------------------

  8 of the 58 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 1 declared and nowhere to be found; 1 a template; 1 private.

  What to expect
  --------------

  - The C++ QTextFormat is created at the first use, not by
    'QTextFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextFormat back gives a copy the ritual made for
    Python, in a new cute QTextFormat.
  """

  #  The enums Qt writes inside QTextFormat, and the names Qt has for the
  #  combinations of its flags enums.
  FormatType = FormatType
  ObjectTypes = ObjectTypes
  PageBreakFlag = PageBreakFlag
  PageBreakFlags = PageBreakFlag
  Property = Property

  #  The cute classes made after this one that its functions take or give;
  #  see 'WAIT'.
  QTextBlockFormat = WAIT['QTextBlockFormat']
  QTextCharFormat = WAIT['QTextCharFormat']

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextFormat'

  #  Qt's '~QTextFormat()'. Naming it makes this a value class: Python owns
  #  every C++ QTextFormat behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QTextFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isValid
    """
    #  bool QTextFormat::isValid() const
    return self.uglySide.call('ritual_ZNK11QTextFormat7isValidEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isEmpty
    """
    #  bool QTextFormat::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QTextFormat7isEmptyEv')

  def type(self) -> int:
    """
    Calls Qt's 'int QTextFormat::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#type
    """
    #  int QTextFormat::type() const
    return self.uglySide.call('ritual_ZNK11QTextFormat4typeEv')

  def objectIndex(self) -> int:
    """
    Calls Qt's 'int QTextFormat::objectIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#objectIndex
    """
    #  int QTextFormat::objectIndex() const
    return self.uglySide.call('ritual_ZNK11QTextFormat11objectIndexEv')

  @overload(int)
  def property(self, propertyId: int) -> QVariant:
    """
    Calls Qt's 'QVariant QTextFormat::property(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#property

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTextFormat::property(int propertyId) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat8propertyEi', propertyId,
    )
    return QVariant._cuteOwning(address)

  @overload(int)
  def hasProperty(self, propertyId: int) -> bool:
    """
    Calls Qt's 'bool QTextFormat::hasProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#hasProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.
    """
    #  bool QTextFormat::hasProperty(int propertyId) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormat11hasPropertyEi', propertyId,
    )

  @overload(int)
  def boolProperty(self, propertyId: int) -> bool:
    """
    Calls Qt's 'bool QTextFormat::boolProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#boolProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.
    """
    #  bool QTextFormat::boolProperty(int propertyId) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormat12boolPropertyEi', propertyId,
    )

  @overload(int)
  def intProperty(self, propertyId: int) -> int:
    """
    Calls Qt's 'int QTextFormat::intProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#intProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.
    """
    #  int QTextFormat::intProperty(int propertyId) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormat11intPropertyEi', propertyId,
    )

  @overload(int)
  def doubleProperty(self, propertyId: int) -> float:
    """
    Calls Qt's 'qreal QTextFormat::doubleProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#doubleProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.
    """
    #  qreal QTextFormat::doubleProperty(int propertyId) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormat14doublePropertyEi', propertyId,
    )

  @overload(int)
  def stringProperty(self, propertyId: int) -> str:
    """
    Calls Qt's 'QString QTextFormat::stringProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#stringProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextFormat::stringProperty(int propertyId) const
    return self.uglySide.call(
        'ritual_ZNK11QTextFormat14stringPropertyEi', propertyId,
    )

  @overload(int)
  def colorProperty(self, propertyId: int) -> QColor:
    """
    Calls Qt's 'QColor QTextFormat::colorProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#colorProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QTextFormat::colorProperty(int propertyId) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat13colorPropertyEi', propertyId,
    )
    return QColor._cuteOwning(address)

  @overload(int)
  def penProperty(self, propertyId: int) -> QPen:
    """
    Calls Qt's 'QPen QTextFormat::penProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#penProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QTextFormat::penProperty(int propertyId) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat11penPropertyEi', propertyId,
    )
    return QPen._cuteOwning(address)

  @overload(int)
  def brushProperty(self, propertyId: int) -> QBrush:
    """
    Calls Qt's 'QBrush QTextFormat::brushProperty(int propertyId) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#brushProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextFormat::brushProperty(int propertyId) const
    address = self.uglySide.call(
        'ritual_ZNK11QTextFormat13brushPropertyEi', propertyId,
    )
    return QBrush._cuteOwning(address)

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int QTextFormat::propertyCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#propertyCount
    """
    #  int QTextFormat::propertyCount() const
    return self.uglySide.call('ritual_ZNK11QTextFormat13propertyCountEv')

  def objectType(self) -> int:
    """
    Calls Qt's 'int QTextFormat::objectType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#objectType
    """
    #  int QTextFormat::objectType() const
    return self.uglySide.call('ritual_ZNK11QTextFormat10objectTypeEv')

  def isCharFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isCharFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isCharFormat
    """
    #  bool QTextFormat::isCharFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat12isCharFormatEv')

  def isBlockFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isBlockFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isBlockFormat
    """
    #  bool QTextFormat::isBlockFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat13isBlockFormatEv')

  def isListFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isListFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isListFormat
    """
    #  bool QTextFormat::isListFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat12isListFormatEv')

  def isFrameFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isFrameFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isFrameFormat
    """
    #  bool QTextFormat::isFrameFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat13isFrameFormatEv')

  def isImageFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isImageFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isImageFormat
    """
    #  bool QTextFormat::isImageFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat13isImageFormatEv')

  def isTableFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isTableFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isTableFormat
    """
    #  bool QTextFormat::isTableFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat13isTableFormatEv')

  def isTableCellFormat(self) -> bool:
    """
    Calls Qt's 'bool QTextFormat::isTableCellFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#isTableCellFormat
    """
    #  bool QTextFormat::isTableCellFormat() const
    return self.uglySide.call('ritual_ZNK11QTextFormat17isTableCellFormatEv')

  def toBlockFormat(self) -> QTextBlockFormat:
    """
    Calls Qt's 'QTextBlockFormat QTextFormat::toBlockFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#toBlockFormat

    Returns
    -------

    QTextBlockFormat
      A new cute QTextBlockFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextBlockFormat QTextFormat::toBlockFormat() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat13toBlockFormatEv')
    return self.QTextBlockFormat._cuteOwning(address)

  def toCharFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QTextFormat::toCharFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#toCharFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QTextFormat::toCharFormat() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat12toCharFormatEv')
    return self.QTextCharFormat._cuteOwning(address)

  def layoutDirection(self) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection QTextFormat::layoutDirection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#layoutDirection

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection QTextFormat::layoutDirection() const
    return Qt.LayoutDirection(self.uglySide.call(
        'ritual_ZNK11QTextFormat15layoutDirectionEv',
    ))

  def background(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTextFormat::background() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#background

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextFormat::background() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat10backgroundEv')
    return QBrush._cuteOwning(address)

  def foreground(self) -> QBrush:
    """
    Calls Qt's 'QBrush QTextFormat::foreground() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#foreground

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QTextFormat::foreground() const
    address = self.uglySide.call('ritual_ZNK11QTextFormat10foregroundEv')
    return QBrush._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setObjectIndex(self, object: int) -> None:
    """
    Calls Qt's 'void QTextFormat::setObjectIndex(int object)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setObjectIndex

    Parameters
    ----------

    object : int
      Passed on as it is.
    """
    #  void QTextFormat::setObjectIndex(int object)
    self.uglySide.call('ritual_ZN11QTextFormat14setObjectIndexEi', object)

  @overload(int, QVariant)
  def setProperty(self, propertyId: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QTextFormat::setProperty(int propertyId, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QTextFormat::setProperty(int propertyId, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN11QTextFormat11setPropertyEiRK8QVariant',
        propertyId, self._valueOf(value),
    )

  @overload(int)
  def setObjectType(self, type: int) -> None:
    """
    Calls Qt's 'void QTextFormat::setObjectType(int type)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setObjectType

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  void QTextFormat::setObjectType(int type)
    self.uglySide.call('ritual_ZN11QTextFormat13setObjectTypeEi', type)

  @overload(Qt.LayoutDirection)
  def setLayoutDirection(self, direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void QTextFormat::setLayoutDirection(Qt::LayoutDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextformat.html#setLayoutDirection

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QTextFormat::setLayoutDirection(Qt::LayoutDirection direction)
    self.uglySide.call(
        'ritual_ZN11QTextFormat18setLayoutDirectionEN2Qt15LayoutDirectionE',
        direction.value,
    )

  @overload(QBrush)
  def setBackground(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTextFormat::setBackground(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setBackground

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTextFormat::setBackground(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN11QTextFormat13setBackgroundERK6QBrush',
        self._valueOf(brush),
    )

  @overload(QBrush)
  def setForeground(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QTextFormat::setForeground(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#setForeground

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QTextFormat::setForeground(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN11QTextFormat13setForegroundERK6QBrush',
        self._valueOf(brush),
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
    Notes what was given, for Qt's 'QTextFormat::QTextFormat()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#QTextFormat
    """
    #  QTextFormat::QTextFormat()
    self._noteCreation(QTextFormat, lambda: Rituals.call(
        'ritual_ZN11QTextFormatC1Ev',
    ))

  @overload(int)
  def __init__(self, type: int) -> None:
    """
    Notes what was given, for Qt's 'QTextFormat::QTextFormat(int type)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#QTextFormat

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  QTextFormat::QTextFormat(int type)
    self._noteCreation(QTextFormat, lambda: Rituals.call(
        'ritual_ZN11QTextFormatC1Ei', type,
    ))

  @overload(THIS)
  def __init__(self, rhs: QTextFormat) -> None:
    """
    Notes what was given, for Qt's 'QTextFormat::QTextFormat(const
    QTextFormat &rhs)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#QTextFormat

    Parameters
    ----------

    rhs : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  QTextFormat::QTextFormat(const QTextFormat &rhs)
    self._noteCreation(QTextFormat, lambda: Rituals.call(
        'ritual_ZN11QTextFormatC1ERKS_', self._valueOf(rhs),
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

  @overload(THIS)
  def merge(self, other: QTextFormat) -> None:
    """
    Calls Qt's 'void QTextFormat::merge(const QTextFormat &other)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#merge

    Parameters
    ----------

    other : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QTextFormat::merge(const QTextFormat &other)
    self.uglySide.call(
        'ritual_ZN11QTextFormat5mergeERKS_', self._valueOf(other),
    )

  @overload(int)
  def clearProperty(self, propertyId: int) -> None:
    """
    Calls Qt's 'void QTextFormat::clearProperty(int propertyId)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#clearProperty

    Parameters
    ----------

    propertyId : int
      Passed on as it is.
    """
    #  void QTextFormat::clearProperty(int propertyId)
    self.uglySide.call('ritual_ZN11QTextFormat13clearPropertyEi', propertyId)

  def clearBackground(self) -> None:
    """
    Calls Qt's 'void QTextFormat::clearBackground()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#clearBackground
    """
    #  void QTextFormat::clearBackground()
    self.uglySide.call('ritual_ZN11QTextFormat15clearBackgroundEv')

  def clearForeground(self) -> None:
    """
    Calls Qt's 'void QTextFormat::clearForeground()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextformat.html#clearForeground
    """
    #  void QTextFormat::clearForeground()
    self.uglySide.call('ritual_ZN11QTextFormat15clearForegroundEv')
