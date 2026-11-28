"""
DomProperty binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomProperty to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import DomBrush, DomChar, DomColor, DomDate, DomDateTime, DomFont
  from . import DomLocale, DomPalette, DomPoint, DomPointF, DomRect, DomRectF
  from . import DomResourceIcon, DomResourcePixmap, DomSize, DomSizeF
  from . import DomSizePolicy, DomString, DomStringList, DomTime, DomUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomBrush = WAIT['DomBrush']
  DomChar = WAIT['DomChar']
  DomColor = WAIT['DomColor']
  DomDate = WAIT['DomDate']
  DomDateTime = WAIT['DomDateTime']
  DomFont = WAIT['DomFont']
  DomLocale = WAIT['DomLocale']
  DomPalette = WAIT['DomPalette']
  DomPoint = WAIT['DomPoint']
  DomPointF = WAIT['DomPointF']
  DomRect = WAIT['DomRect']
  DomRectF = WAIT['DomRectF']
  DomResourceIcon = WAIT['DomResourceIcon']
  DomResourcePixmap = WAIT['DomResourcePixmap']
  DomSize = WAIT['DomSize']
  DomSizeF = WAIT['DomSizeF']
  DomSizePolicy = WAIT['DomSizePolicy']
  DomString = WAIT['DomString']
  DomStringList = WAIT['DomStringList']
  DomTime = WAIT['DomTime']
  DomUrl = WAIT['DomUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomProperty(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomProperty: a plain Python object standing in front
  of one C++ DomProperty.

  What exists
  -----------

  Every function of Qt's DomProperty that has a ritual and that Python can
  call so far, 97 names in all: 'hasAttributeName', 'attributeName',
  'setAttributeName', 'clearAttributeName', 'hasAttributeStdset',
  'attributeStdset', 'setAttributeStdset', 'clearAttributeStdset', 'kind',
  'elementBool', 'setElementBool', 'elementColor', 'takeElementColor',
  'setElementColor', 'elementCstring', 'setElementCstring', 'elementCursor',
  'setElementCursor', 'elementCursorShape', 'setElementCursorShape',
  'elementEnum', 'setElementEnum', 'elementFont', 'takeElementFont',
  'setElementFont', 'elementIconSet', 'takeElementIconSet',
  'setElementIconSet', 'elementPixmap', 'takeElementPixmap',
  'setElementPixmap', 'elementPalette', 'takeElementPalette',
  'setElementPalette', 'elementPoint', 'takeElementPoint', 'setElementPoint',
  'elementRect', 'takeElementRect', 'setElementRect', 'elementSet',
  'setElementSet', 'elementLocale', 'takeElementLocale', 'setElementLocale',
  'elementSizePolicy', 'takeElementSizePolicy', 'setElementSizePolicy',
  'elementSize', 'takeElementSize', 'setElementSize', 'elementString',
  'takeElementString', 'setElementString', 'elementStringList',
  'takeElementStringList', 'setElementStringList', 'elementNumber',
  'setElementNumber', 'elementFloat', 'setElementFloat', 'elementDouble',
  'setElementDouble', 'elementDate', 'takeElementDate', 'setElementDate',
  'elementTime', 'takeElementTime', 'setElementTime', 'elementDateTime',
  'takeElementDateTime', 'setElementDateTime', 'elementPointF',
  'takeElementPointF', 'setElementPointF', 'elementRectF',
  'takeElementRectF', 'setElementRectF', 'elementSizeF', 'takeElementSizeF',
  'setElementSizeF', 'elementLongLong', 'setElementLongLong', 'elementChar',
  'takeElementChar', 'setElementChar', 'elementUrl', 'takeElementUrl',
  'setElementUrl', 'elementUInt', 'setElementUInt', 'elementULongLong',
  'setElementULongLong', 'elementBrush', 'takeElementBrush',
  'setElementBrush', 'clear'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomProperty::~DomProperty()': the destructor: Python never removes
    a C++ DomProperty.
  - Qt's 'void DomProperty::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomProperty::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 105 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomProperty is created at the first use, not by
    'DomProperty(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomProperty.
  - Each name of Qt's DomProperty that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside DomProperty, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Kind(CuteNum):
    """
    The enum 'DomProperty::Kind' of Qt, with the 34 names Qt gives in it.
    """

    Unknown = Kee[int](0)
    Bool = Kee[int](1)
    Color = Kee[int](2)
    Cstring = Kee[int](3)
    Cursor = Kee[int](4)
    CursorShape = Kee[int](5)
    Enum = Kee[int](6)
    Font = Kee[int](7)
    IconSet = Kee[int](8)
    Pixmap = Kee[int](9)
    Palette = Kee[int](10)
    Point = Kee[int](11)
    Rect = Kee[int](12)
    Set = Kee[int](13)
    Locale = Kee[int](14)
    SizePolicy = Kee[int](15)
    Size = Kee[int](16)
    String = Kee[int](17)
    StringList = Kee[int](18)
    Number = Kee[int](19)
    Float = Kee[int](20)
    Double = Kee[int](21)
    Date = Kee[int](22)
    Time = Kee[int](23)
    DateTime = Kee[int](24)
    PointF = Kee[int](25)
    RectF = Kee[int](26)
    SizeF = Kee[int](27)
    LongLong = Kee[int](28)
    Char = Kee[int](29)
    Url = Kee[int](30)
    UInt = Kee[int](31)
    ULongLong = Kee[int](32)
    Brush = Kee[int](33)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomProperty'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomProperty::hasAttributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#hasAttributeName
    """
    #  bool DomProperty::hasAttributeName() const
    return self.uglySide.call('ritual_ZNK11DomProperty16hasAttributeNameEv')

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomProperty::attributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomProperty::attributeName() const
    return self.uglySide.call('ritual_ZNK11DomProperty13attributeNameEv')

  def hasAttributeStdset(self) -> bool:
    """
    Calls Qt's 'bool DomProperty::hasAttributeStdset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#hasAttributeStdset
    """
    #  bool DomProperty::hasAttributeStdset() const
    return self.uglySide.call(
        'ritual_ZNK11DomProperty18hasAttributeStdsetEv',
    )

  def attributeStdset(self) -> int:
    """
    Calls Qt's 'int DomProperty::attributeStdset() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#attributeStdset
    """
    #  int DomProperty::attributeStdset() const
    return self.uglySide.call('ritual_ZNK11DomProperty15attributeStdsetEv')

  def kind(self) -> Kind:
    """
    Calls Qt's 'Kind DomProperty::kind() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#kind

    Returns
    -------

    Kind
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Kind(number)' gives.
    """
    #  Kind DomProperty::kind() const
    return DomProperty.Kind(self.uglySide.call(
        'ritual_ZNK11DomProperty4kindEv',
    ))

  def elementBool(self) -> str:
    """
    Calls Qt's 'QString DomProperty::elementBool() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementBool

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomProperty::elementBool() const
    return self.uglySide.call('ritual_ZNK11DomProperty11elementBoolEv')

  def elementColor(self) -> Optional[DomColor]:
    """
    Calls Qt's 'DomColor *DomProperty::elementColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementColor

    Returns
    -------

    Optional[DomColor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColor *DomProperty::elementColor() const
    address = self.uglySide.call('ritual_ZNK11DomProperty12elementColorEv')
    from . import DomColor
    return DomColor._cuteAt(address)

  def elementCstring(self) -> str:
    """
    Calls Qt's 'QString DomProperty::elementCstring() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementCstring

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomProperty::elementCstring() const
    return self.uglySide.call('ritual_ZNK11DomProperty14elementCstringEv')

  def elementCursor(self) -> int:
    """
    Calls Qt's 'int DomProperty::elementCursor() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementCursor
    """
    #  int DomProperty::elementCursor() const
    return self.uglySide.call('ritual_ZNK11DomProperty13elementCursorEv')

  def elementCursorShape(self) -> str:
    """
    Calls Qt's 'QString DomProperty::elementCursorShape() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#elementCursorShape

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomProperty::elementCursorShape() const
    return self.uglySide.call(
        'ritual_ZNK11DomProperty18elementCursorShapeEv',
    )

  def elementEnum(self) -> str:
    """
    Calls Qt's 'QString DomProperty::elementEnum() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementEnum

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomProperty::elementEnum() const
    return self.uglySide.call('ritual_ZNK11DomProperty11elementEnumEv')

  def elementFont(self) -> Optional[DomFont]:
    """
    Calls Qt's 'DomFont *DomProperty::elementFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementFont

    Returns
    -------

    Optional[DomFont]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomFont *DomProperty::elementFont() const
    address = self.uglySide.call('ritual_ZNK11DomProperty11elementFontEv')
    from . import DomFont
    return DomFont._cuteAt(address)

  def elementIconSet(self) -> Optional[DomResourceIcon]:
    """
    Calls Qt's 'DomResourceIcon *DomProperty::elementIconSet() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementIconSet

    Returns
    -------

    Optional[DomResourceIcon]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourceIcon *DomProperty::elementIconSet() const
    address = self.uglySide.call('ritual_ZNK11DomProperty14elementIconSetEv')
    from . import DomResourceIcon
    return DomResourceIcon._cuteAt(address)

  def elementPixmap(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomProperty::elementPixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementPixmap

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomProperty::elementPixmap() const
    address = self.uglySide.call('ritual_ZNK11DomProperty13elementPixmapEv')
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def elementPalette(self) -> Optional[DomPalette]:
    """
    Calls Qt's 'DomPalette *DomProperty::elementPalette() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementPalette

    Returns
    -------

    Optional[DomPalette]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomPalette *DomProperty::elementPalette() const
    address = self.uglySide.call('ritual_ZNK11DomProperty14elementPaletteEv')
    from . import DomPalette
    return DomPalette._cuteAt(address)

  def elementPoint(self) -> Optional[DomPoint]:
    """
    Calls Qt's 'DomPoint *DomProperty::elementPoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementPoint

    Returns
    -------

    Optional[DomPoint]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomPoint *DomProperty::elementPoint() const
    address = self.uglySide.call('ritual_ZNK11DomProperty12elementPointEv')
    from . import DomPoint
    return DomPoint._cuteAt(address)

  def elementRect(self) -> Optional[DomRect]:
    """
    Calls Qt's 'DomRect *DomProperty::elementRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementRect

    Returns
    -------

    Optional[DomRect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomRect *DomProperty::elementRect() const
    address = self.uglySide.call('ritual_ZNK11DomProperty11elementRectEv')
    from . import DomRect
    return DomRect._cuteAt(address)

  def elementSet(self) -> str:
    """
    Calls Qt's 'QString DomProperty::elementSet() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementSet

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomProperty::elementSet() const
    return self.uglySide.call('ritual_ZNK11DomProperty10elementSetEv')

  def elementLocale(self) -> Optional[DomLocale]:
    """
    Calls Qt's 'DomLocale *DomProperty::elementLocale() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementLocale

    Returns
    -------

    Optional[DomLocale]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomLocale *DomProperty::elementLocale() const
    address = self.uglySide.call('ritual_ZNK11DomProperty13elementLocaleEv')
    from . import DomLocale
    return DomLocale._cuteAt(address)

  def elementSizePolicy(self) -> Optional[DomSizePolicy]:
    """
    Calls Qt's 'DomSizePolicy *DomProperty::elementSizePolicy() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementSizePolicy

    Returns
    -------

    Optional[DomSizePolicy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSizePolicy *DomProperty::elementSizePolicy() const
    address = self.uglySide.call(
        'ritual_ZNK11DomProperty17elementSizePolicyEv',
    )
    from . import DomSizePolicy
    return DomSizePolicy._cuteAt(address)

  def elementSize(self) -> Optional[DomSize]:
    """
    Calls Qt's 'DomSize *DomProperty::elementSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementSize

    Returns
    -------

    Optional[DomSize]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSize *DomProperty::elementSize() const
    address = self.uglySide.call('ritual_ZNK11DomProperty11elementSizeEv')
    from . import DomSize
    return DomSize._cuteAt(address)

  def elementString(self) -> Optional[DomString]:
    """
    Calls Qt's 'DomString *DomProperty::elementString() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementString

    Returns
    -------

    Optional[DomString]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomString *DomProperty::elementString() const
    address = self.uglySide.call('ritual_ZNK11DomProperty13elementStringEv')
    from . import DomString
    return DomString._cuteAt(address)

  def elementStringList(self) -> Optional[DomStringList]:
    """
    Calls Qt's 'DomStringList *DomProperty::elementStringList() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementStringList

    Returns
    -------

    Optional[DomStringList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomStringList *DomProperty::elementStringList() const
    address = self.uglySide.call(
        'ritual_ZNK11DomProperty17elementStringListEv',
    )
    from . import DomStringList
    return DomStringList._cuteAt(address)

  def elementNumber(self) -> int:
    """
    Calls Qt's 'int DomProperty::elementNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementNumber
    """
    #  int DomProperty::elementNumber() const
    return self.uglySide.call('ritual_ZNK11DomProperty13elementNumberEv')

  def elementFloat(self) -> float:
    """
    Calls Qt's 'float DomProperty::elementFloat() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementFloat
    """
    #  float DomProperty::elementFloat() const
    return self.uglySide.call('ritual_ZNK11DomProperty12elementFloatEv')

  def elementDouble(self) -> float:
    """
    Calls Qt's 'double DomProperty::elementDouble() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementDouble
    """
    #  double DomProperty::elementDouble() const
    return self.uglySide.call('ritual_ZNK11DomProperty13elementDoubleEv')

  def elementDate(self) -> Optional[DomDate]:
    """
    Calls Qt's 'DomDate *DomProperty::elementDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementDate

    Returns
    -------

    Optional[DomDate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomDate *DomProperty::elementDate() const
    address = self.uglySide.call('ritual_ZNK11DomProperty11elementDateEv')
    from . import DomDate
    return DomDate._cuteAt(address)

  def elementTime(self) -> Optional[DomTime]:
    """
    Calls Qt's 'DomTime *DomProperty::elementTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementTime

    Returns
    -------

    Optional[DomTime]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomTime *DomProperty::elementTime() const
    address = self.uglySide.call('ritual_ZNK11DomProperty11elementTimeEv')
    from . import DomTime
    return DomTime._cuteAt(address)

  def elementDateTime(self) -> Optional[DomDateTime]:
    """
    Calls Qt's 'DomDateTime *DomProperty::elementDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementDateTime

    Returns
    -------

    Optional[DomDateTime]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomDateTime *DomProperty::elementDateTime() const
    address = self.uglySide.call(
        'ritual_ZNK11DomProperty15elementDateTimeEv',
    )
    from . import DomDateTime
    return DomDateTime._cuteAt(address)

  def elementPointF(self) -> Optional[DomPointF]:
    """
    Calls Qt's 'DomPointF *DomProperty::elementPointF() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementPointF

    Returns
    -------

    Optional[DomPointF]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomPointF *DomProperty::elementPointF() const
    address = self.uglySide.call('ritual_ZNK11DomProperty13elementPointFEv')
    from . import DomPointF
    return DomPointF._cuteAt(address)

  def elementRectF(self) -> Optional[DomRectF]:
    """
    Calls Qt's 'DomRectF *DomProperty::elementRectF() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementRectF

    Returns
    -------

    Optional[DomRectF]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomRectF *DomProperty::elementRectF() const
    address = self.uglySide.call('ritual_ZNK11DomProperty12elementRectFEv')
    from . import DomRectF
    return DomRectF._cuteAt(address)

  def elementSizeF(self) -> Optional[DomSizeF]:
    """
    Calls Qt's 'DomSizeF *DomProperty::elementSizeF() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementSizeF

    Returns
    -------

    Optional[DomSizeF]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSizeF *DomProperty::elementSizeF() const
    address = self.uglySide.call('ritual_ZNK11DomProperty12elementSizeFEv')
    from . import DomSizeF
    return DomSizeF._cuteAt(address)

  def elementLongLong(self) -> int:
    """
    Calls Qt's 'qlonglong DomProperty::elementLongLong() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementLongLong
    """
    #  qlonglong DomProperty::elementLongLong() const
    return self.uglySide.call('ritual_ZNK11DomProperty15elementLongLongEv')

  def elementChar(self) -> Optional[DomChar]:
    """
    Calls Qt's 'DomChar *DomProperty::elementChar() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementChar

    Returns
    -------

    Optional[DomChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomChar *DomProperty::elementChar() const
    address = self.uglySide.call('ritual_ZNK11DomProperty11elementCharEv')
    from . import DomChar
    return DomChar._cuteAt(address)

  def elementUrl(self) -> Optional[DomUrl]:
    """
    Calls Qt's 'DomUrl *DomProperty::elementUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementUrl

    Returns
    -------

    Optional[DomUrl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomUrl *DomProperty::elementUrl() const
    address = self.uglySide.call('ritual_ZNK11DomProperty10elementUrlEv')
    from . import DomUrl
    return DomUrl._cuteAt(address)

  def elementUInt(self) -> int:
    """
    Calls Qt's 'uint DomProperty::elementUInt() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementUInt
    """
    #  uint DomProperty::elementUInt() const
    return self.uglySide.call('ritual_ZNK11DomProperty11elementUIntEv')

  def elementULongLong(self) -> int:
    """
    Calls Qt's 'qulonglong DomProperty::elementULongLong() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementULongLong
    """
    #  qulonglong DomProperty::elementULongLong() const
    return self.uglySide.call('ritual_ZNK11DomProperty16elementULongLongEv')

  def elementBrush(self) -> Optional[DomBrush]:
    """
    Calls Qt's 'DomBrush *DomProperty::elementBrush() const'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#elementBrush

    Returns
    -------

    Optional[DomBrush]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomBrush *DomProperty::elementBrush() const
    address = self.uglySide.call('ritual_ZNK11DomProperty12elementBrushEv')
    from . import DomBrush
    return DomBrush._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomProperty::setAttributeName(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setAttributeName

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomProperty::setAttributeName(const QString &a)
    self.uglySide.call(
        'ritual_ZN11DomProperty16setAttributeNameERK7QString', a,
    )

  @overload(int)
  def setAttributeStdset(self, a: int) -> None:
    """
    Calls Qt's 'void DomProperty::setAttributeStdset(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#setAttributeStdset

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomProperty::setAttributeStdset(int a)
    self.uglySide.call('ritual_ZN11DomProperty18setAttributeStdsetEi', a)

  @overload(str)
  def setElementBool(self, a: str) -> None:
    """
    Calls Qt's 'void DomProperty::setElementBool(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementBool

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomProperty::setElementBool(const QString &a)
    self.uglySide.call(
        'ritual_ZN11DomProperty14setElementBoolERK7QString', a,
    )

  @overload(DomColor)
  @overload(NoneType)
  def setElementColor(self, a: Optional[DomColor]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementColor(DomColor *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementColor

    Parameters
    ----------

    a : Optional[DomColor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementColor(DomColor *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty15setElementColorEP8DomColor',
        self._addressOf(a),
    )

  @overload(str)
  def setElementCstring(self, a: str) -> None:
    """
    Calls Qt's 'void DomProperty::setElementCstring(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementCstring

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomProperty::setElementCstring(const QString &a)
    self.uglySide.call(
        'ritual_ZN11DomProperty17setElementCstringERK7QString', a,
    )

  @overload(int)
  def setElementCursor(self, a: int) -> None:
    """
    Calls Qt's 'void DomProperty::setElementCursor(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementCursor

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomProperty::setElementCursor(int a)
    self.uglySide.call('ritual_ZN11DomProperty16setElementCursorEi', a)

  @overload(str)
  def setElementCursorShape(self, a: str) -> None:
    """
    Calls Qt's 'void DomProperty::setElementCursorShape(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#setElementCursorShape

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomProperty::setElementCursorShape(const QString &a)
    self.uglySide.call(
        'ritual_ZN11DomProperty21setElementCursorShapeERK7QString', a,
    )

  @overload(str)
  def setElementEnum(self, a: str) -> None:
    """
    Calls Qt's 'void DomProperty::setElementEnum(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementEnum

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomProperty::setElementEnum(const QString &a)
    self.uglySide.call(
        'ritual_ZN11DomProperty14setElementEnumERK7QString', a,
    )

  @overload(DomFont)
  @overload(NoneType)
  def setElementFont(self, a: Optional[DomFont]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementFont(DomFont *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementFont

    Parameters
    ----------

    a : Optional[DomFont]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementFont(DomFont *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty14setElementFontEP7DomFont',
        self._addressOf(a),
    )

  @overload(DomResourceIcon)
  @overload(NoneType)
  def setElementIconSet(self, a: Optional[DomResourceIcon]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementIconSet(DomResourceIcon *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementIconSet

    Parameters
    ----------

    a : Optional[DomResourceIcon]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementIconSet(DomResourceIcon *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty17setElementIconSetEP15DomResourceIcon',
        self._addressOf(a),
    )

  @overload(DomResourcePixmap)
  @overload(NoneType)
  def setElementPixmap(self, a: Optional[DomResourcePixmap]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementPixmap(DomResourcePixmap *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementPixmap

    Parameters
    ----------

    a : Optional[DomResourcePixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementPixmap(DomResourcePixmap *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty16setElementPixmapEP17DomResourcePixmap',
        self._addressOf(a),
    )

  @overload(DomPalette)
  @overload(NoneType)
  def setElementPalette(self, a: Optional[DomPalette]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementPalette(DomPalette *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementPalette

    Parameters
    ----------

    a : Optional[DomPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementPalette(DomPalette *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty17setElementPaletteEP10DomPalette',
        self._addressOf(a),
    )

  @overload(DomPoint)
  @overload(NoneType)
  def setElementPoint(self, a: Optional[DomPoint]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementPoint(DomPoint *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementPoint

    Parameters
    ----------

    a : Optional[DomPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementPoint(DomPoint *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty15setElementPointEP8DomPoint',
        self._addressOf(a),
    )

  @overload(DomRect)
  @overload(NoneType)
  def setElementRect(self, a: Optional[DomRect]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementRect(DomRect *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementRect

    Parameters
    ----------

    a : Optional[DomRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementRect(DomRect *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty14setElementRectEP7DomRect',
        self._addressOf(a),
    )

  @overload(str)
  def setElementSet(self, a: str) -> None:
    """
    Calls Qt's 'void DomProperty::setElementSet(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementSet

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomProperty::setElementSet(const QString &a)
    self.uglySide.call('ritual_ZN11DomProperty13setElementSetERK7QString', a)

  @overload(DomLocale)
  @overload(NoneType)
  def setElementLocale(self, a: Optional[DomLocale]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementLocale(DomLocale *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementLocale

    Parameters
    ----------

    a : Optional[DomLocale]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementLocale(DomLocale *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty16setElementLocaleEP9DomLocale',
        self._addressOf(a),
    )

  @overload(DomSizePolicy)
  @overload(NoneType)
  def setElementSizePolicy(self, a: Optional[DomSizePolicy]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementSizePolicy(DomSizePolicy *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#setElementSizePolicy

    Parameters
    ----------

    a : Optional[DomSizePolicy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementSizePolicy(DomSizePolicy *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty20setElementSizePolicyEP13DomSizePolicy',
        self._addressOf(a),
    )

  @overload(DomSize)
  @overload(NoneType)
  def setElementSize(self, a: Optional[DomSize]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementSize(DomSize *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementSize

    Parameters
    ----------

    a : Optional[DomSize]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementSize(DomSize *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty14setElementSizeEP7DomSize',
        self._addressOf(a),
    )

  @overload(DomString)
  @overload(NoneType)
  def setElementString(self, a: Optional[DomString]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementString(DomString *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementString

    Parameters
    ----------

    a : Optional[DomString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementString(DomString *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty16setElementStringEP9DomString',
        self._addressOf(a),
    )

  @overload(DomStringList)
  @overload(NoneType)
  def setElementStringList(self, a: Optional[DomStringList]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementStringList(DomStringList *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#setElementStringList

    Parameters
    ----------

    a : Optional[DomStringList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementStringList(DomStringList *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty20setElementStringListEP13DomStringList',
        self._addressOf(a),
    )

  @overload(int)
  def setElementNumber(self, a: int) -> None:
    """
    Calls Qt's 'void DomProperty::setElementNumber(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementNumber

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomProperty::setElementNumber(int a)
    self.uglySide.call('ritual_ZN11DomProperty16setElementNumberEi', a)

  @overload(float)
  def setElementFloat(self, a: float) -> None:
    """
    Calls Qt's 'void DomProperty::setElementFloat(float a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementFloat

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomProperty::setElementFloat(float a)
    self.uglySide.call('ritual_ZN11DomProperty15setElementFloatEf', a)

  @overload(float)
  def setElementDouble(self, a: float) -> None:
    """
    Calls Qt's 'void DomProperty::setElementDouble(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementDouble

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomProperty::setElementDouble(double a)
    self.uglySide.call('ritual_ZN11DomProperty16setElementDoubleEd', a)

  @overload(DomDate)
  @overload(NoneType)
  def setElementDate(self, a: Optional[DomDate]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementDate(DomDate *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementDate

    Parameters
    ----------

    a : Optional[DomDate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementDate(DomDate *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty14setElementDateEP7DomDate',
        self._addressOf(a),
    )

  @overload(DomTime)
  @overload(NoneType)
  def setElementTime(self, a: Optional[DomTime]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementTime(DomTime *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementTime

    Parameters
    ----------

    a : Optional[DomTime]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementTime(DomTime *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty14setElementTimeEP7DomTime',
        self._addressOf(a),
    )

  @overload(DomDateTime)
  @overload(NoneType)
  def setElementDateTime(self, a: Optional[DomDateTime]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementDateTime(DomDateTime *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#setElementDateTime

    Parameters
    ----------

    a : Optional[DomDateTime]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementDateTime(DomDateTime *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty18setElementDateTimeEP11DomDateTime',
        self._addressOf(a),
    )

  @overload(DomPointF)
  @overload(NoneType)
  def setElementPointF(self, a: Optional[DomPointF]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementPointF(DomPointF *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementPointF

    Parameters
    ----------

    a : Optional[DomPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementPointF(DomPointF *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty16setElementPointFEP9DomPointF',
        self._addressOf(a),
    )

  @overload(DomRectF)
  @overload(NoneType)
  def setElementRectF(self, a: Optional[DomRectF]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementRectF(DomRectF *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementRectF

    Parameters
    ----------

    a : Optional[DomRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementRectF(DomRectF *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty15setElementRectFEP8DomRectF',
        self._addressOf(a),
    )

  @overload(DomSizeF)
  @overload(NoneType)
  def setElementSizeF(self, a: Optional[DomSizeF]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementSizeF(DomSizeF *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementSizeF

    Parameters
    ----------

    a : Optional[DomSizeF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementSizeF(DomSizeF *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty15setElementSizeFEP8DomSizeF',
        self._addressOf(a),
    )

  @overload(int)
  def setElementLongLong(self, a: int) -> None:
    """
    Calls Qt's 'void DomProperty::setElementLongLong(qlonglong a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#setElementLongLong

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomProperty::setElementLongLong(qlonglong a)
    self.uglySide.call('ritual_ZN11DomProperty18setElementLongLongEx', a)

  @overload(DomChar)
  @overload(NoneType)
  def setElementChar(self, a: Optional[DomChar]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementChar(DomChar *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementChar

    Parameters
    ----------

    a : Optional[DomChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementChar(DomChar *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty14setElementCharEP7DomChar',
        self._addressOf(a),
    )

  @overload(DomUrl)
  @overload(NoneType)
  def setElementUrl(self, a: Optional[DomUrl]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementUrl(DomUrl *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementUrl

    Parameters
    ----------

    a : Optional[DomUrl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementUrl(DomUrl *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty13setElementUrlEP6DomUrl', self._addressOf(a),
    )

  @overload(int)
  def setElementUInt(self, a: int) -> None:
    """
    Calls Qt's 'void DomProperty::setElementUInt(uint a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementUInt

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomProperty::setElementUInt(uint a)
    self.uglySide.call('ritual_ZN11DomProperty14setElementUIntEj', a)

  @overload(int)
  def setElementULongLong(self, a: int) -> None:
    """
    Calls Qt's 'void DomProperty::setElementULongLong(qulonglong a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#setElementULongLong

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomProperty::setElementULongLong(qulonglong a)
    self.uglySide.call('ritual_ZN11DomProperty19setElementULongLongEy', a)

  @overload(DomBrush)
  @overload(NoneType)
  def setElementBrush(self, a: Optional[DomBrush]) -> None:
    """
    Calls Qt's 'void DomProperty::setElementBrush(DomBrush *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#setElementBrush

    Parameters
    ----------

    a : Optional[DomBrush]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomProperty::setElementBrush(DomBrush *a)
    self.uglySide.call(
        'ritual_ZN11DomProperty15setElementBrushEP8DomBrush',
        self._addressOf(a),
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
    Notes what was given, for Qt's 'DomProperty::DomProperty()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#DomProperty
    """
    #  DomProperty::DomProperty()
    self._noteCreation(DomProperty, lambda: Rituals.call(
        'ritual_ZN11DomPropertyC1Ev',
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

  def clearAttributeName(self) -> None:
    """
    Calls Qt's 'void DomProperty::clearAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#clearAttributeName
    """
    #  void DomProperty::clearAttributeName()
    self.uglySide.call('ritual_ZN11DomProperty18clearAttributeNameEv')

  def clearAttributeStdset(self) -> None:
    """
    Calls Qt's 'void DomProperty::clearAttributeStdset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#clearAttributeStdset
    """
    #  void DomProperty::clearAttributeStdset()
    self.uglySide.call('ritual_ZN11DomProperty20clearAttributeStdsetEv')

  def takeElementColor(self) -> Optional[DomColor]:
    """
    Calls Qt's 'DomColor *DomProperty::takeElementColor()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementColor

    Returns
    -------

    Optional[DomColor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomColor *DomProperty::takeElementColor()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty16takeElementColorEv',
    )
    from . import DomColor
    return DomColor._cuteAt(address)

  def takeElementFont(self) -> Optional[DomFont]:
    """
    Calls Qt's 'DomFont *DomProperty::takeElementFont()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementFont

    Returns
    -------

    Optional[DomFont]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomFont *DomProperty::takeElementFont()
    address = self.uglySide.call('ritual_ZN11DomProperty15takeElementFontEv')
    from . import DomFont
    return DomFont._cuteAt(address)

  def takeElementIconSet(self) -> Optional[DomResourceIcon]:
    """
    Calls Qt's 'DomResourceIcon *DomProperty::takeElementIconSet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#takeElementIconSet

    Returns
    -------

    Optional[DomResourceIcon]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourceIcon *DomProperty::takeElementIconSet()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty18takeElementIconSetEv',
    )
    from . import DomResourceIcon
    return DomResourceIcon._cuteAt(address)

  def takeElementPixmap(self) -> Optional[DomResourcePixmap]:
    """
    Calls Qt's 'DomResourcePixmap *DomProperty::takeElementPixmap()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementPixmap

    Returns
    -------

    Optional[DomResourcePixmap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomResourcePixmap *DomProperty::takeElementPixmap()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty17takeElementPixmapEv',
    )
    from . import DomResourcePixmap
    return DomResourcePixmap._cuteAt(address)

  def takeElementPalette(self) -> Optional[DomPalette]:
    """
    Calls Qt's 'DomPalette *DomProperty::takeElementPalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#takeElementPalette

    Returns
    -------

    Optional[DomPalette]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomPalette *DomProperty::takeElementPalette()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty18takeElementPaletteEv',
    )
    from . import DomPalette
    return DomPalette._cuteAt(address)

  def takeElementPoint(self) -> Optional[DomPoint]:
    """
    Calls Qt's 'DomPoint *DomProperty::takeElementPoint()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementPoint

    Returns
    -------

    Optional[DomPoint]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomPoint *DomProperty::takeElementPoint()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty16takeElementPointEv',
    )
    from . import DomPoint
    return DomPoint._cuteAt(address)

  def takeElementRect(self) -> Optional[DomRect]:
    """
    Calls Qt's 'DomRect *DomProperty::takeElementRect()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementRect

    Returns
    -------

    Optional[DomRect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomRect *DomProperty::takeElementRect()
    address = self.uglySide.call('ritual_ZN11DomProperty15takeElementRectEv')
    from . import DomRect
    return DomRect._cuteAt(address)

  def takeElementLocale(self) -> Optional[DomLocale]:
    """
    Calls Qt's 'DomLocale *DomProperty::takeElementLocale()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementLocale

    Returns
    -------

    Optional[DomLocale]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomLocale *DomProperty::takeElementLocale()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty17takeElementLocaleEv',
    )
    from . import DomLocale
    return DomLocale._cuteAt(address)

  def takeElementSizePolicy(self) -> Optional[DomSizePolicy]:
    """
    Calls Qt's 'DomSizePolicy *DomProperty::takeElementSizePolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#takeElementSizePolicy

    Returns
    -------

    Optional[DomSizePolicy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSizePolicy *DomProperty::takeElementSizePolicy()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty21takeElementSizePolicyEv',
    )
    from . import DomSizePolicy
    return DomSizePolicy._cuteAt(address)

  def takeElementSize(self) -> Optional[DomSize]:
    """
    Calls Qt's 'DomSize *DomProperty::takeElementSize()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementSize

    Returns
    -------

    Optional[DomSize]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSize *DomProperty::takeElementSize()
    address = self.uglySide.call('ritual_ZN11DomProperty15takeElementSizeEv')
    from . import DomSize
    return DomSize._cuteAt(address)

  def takeElementString(self) -> Optional[DomString]:
    """
    Calls Qt's 'DomString *DomProperty::takeElementString()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementString

    Returns
    -------

    Optional[DomString]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomString *DomProperty::takeElementString()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty17takeElementStringEv',
    )
    from . import DomString
    return DomString._cuteAt(address)

  def takeElementStringList(self) -> Optional[DomStringList]:
    """
    Calls Qt's 'DomStringList *DomProperty::takeElementStringList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#takeElementStringList

    Returns
    -------

    Optional[DomStringList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomStringList *DomProperty::takeElementStringList()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty21takeElementStringListEv',
    )
    from . import DomStringList
    return DomStringList._cuteAt(address)

  def takeElementDate(self) -> Optional[DomDate]:
    """
    Calls Qt's 'DomDate *DomProperty::takeElementDate()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementDate

    Returns
    -------

    Optional[DomDate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomDate *DomProperty::takeElementDate()
    address = self.uglySide.call('ritual_ZN11DomProperty15takeElementDateEv')
    from . import DomDate
    return DomDate._cuteAt(address)

  def takeElementTime(self) -> Optional[DomTime]:
    """
    Calls Qt's 'DomTime *DomProperty::takeElementTime()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementTime

    Returns
    -------

    Optional[DomTime]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomTime *DomProperty::takeElementTime()
    address = self.uglySide.call('ritual_ZN11DomProperty15takeElementTimeEv')
    from . import DomTime
    return DomTime._cuteAt(address)

  def takeElementDateTime(self) -> Optional[DomDateTime]:
    """
    Calls Qt's 'DomDateTime *DomProperty::takeElementDateTime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domproperty.html#takeElementDateTime

    Returns
    -------

    Optional[DomDateTime]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomDateTime *DomProperty::takeElementDateTime()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty19takeElementDateTimeEv',
    )
    from . import DomDateTime
    return DomDateTime._cuteAt(address)

  def takeElementPointF(self) -> Optional[DomPointF]:
    """
    Calls Qt's 'DomPointF *DomProperty::takeElementPointF()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementPointF

    Returns
    -------

    Optional[DomPointF]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomPointF *DomProperty::takeElementPointF()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty17takeElementPointFEv',
    )
    from . import DomPointF
    return DomPointF._cuteAt(address)

  def takeElementRectF(self) -> Optional[DomRectF]:
    """
    Calls Qt's 'DomRectF *DomProperty::takeElementRectF()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementRectF

    Returns
    -------

    Optional[DomRectF]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomRectF *DomProperty::takeElementRectF()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty16takeElementRectFEv',
    )
    from . import DomRectF
    return DomRectF._cuteAt(address)

  def takeElementSizeF(self) -> Optional[DomSizeF]:
    """
    Calls Qt's 'DomSizeF *DomProperty::takeElementSizeF()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementSizeF

    Returns
    -------

    Optional[DomSizeF]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomSizeF *DomProperty::takeElementSizeF()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty16takeElementSizeFEv',
    )
    from . import DomSizeF
    return DomSizeF._cuteAt(address)

  def takeElementChar(self) -> Optional[DomChar]:
    """
    Calls Qt's 'DomChar *DomProperty::takeElementChar()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementChar

    Returns
    -------

    Optional[DomChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomChar *DomProperty::takeElementChar()
    address = self.uglySide.call('ritual_ZN11DomProperty15takeElementCharEv')
    from . import DomChar
    return DomChar._cuteAt(address)

  def takeElementUrl(self) -> Optional[DomUrl]:
    """
    Calls Qt's 'DomUrl *DomProperty::takeElementUrl()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementUrl

    Returns
    -------

    Optional[DomUrl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomUrl *DomProperty::takeElementUrl()
    address = self.uglySide.call('ritual_ZN11DomProperty14takeElementUrlEv')
    from . import DomUrl
    return DomUrl._cuteAt(address)

  def takeElementBrush(self) -> Optional[DomBrush]:
    """
    Calls Qt's 'DomBrush *DomProperty::takeElementBrush()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#takeElementBrush

    Returns
    -------

    Optional[DomBrush]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomBrush *DomProperty::takeElementBrush()
    address = self.uglySide.call(
        'ritual_ZN11DomProperty16takeElementBrushEv',
    )
    from . import DomBrush
    return DomBrush._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void DomProperty::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/domproperty.html#clear
    """
    #  void DomProperty::clear()
    self.uglySide.call('ritual_ZN11DomProperty5clearEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomProperty::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomProperty.read' has no cute function yet. Qt's 'void "
        "DomProperty::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomProperty::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomProperty.write' has no cute function yet. Qt's 'void "
        "DomProperty::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomProperty *>': the list of DomProperty, which
#  'QList[DomProperty]' gives. It is made here, so that there is one as soon
#  as there can be a DomProperty.
QList.createKind(
    DomProperty, 'address',
    make='ritual_list_make_DomProperty_ptr',
    add='ritual_list_add_DomProperty_ptr',
    size='ritual_list_size_DomProperty_ptr',
    at='ritual_list_at_DomProperty_ptr',
    drop='ritual_list_drop_DomProperty_ptr',
)
