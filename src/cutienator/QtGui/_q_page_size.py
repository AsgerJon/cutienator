"""
QPageSize binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpagesize.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRect, QRectF, QSize, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']


class QPageSize(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPageSize: a plain Python object standing in front of
  one C++ QPageSize.

  C++ hands a QPageSize around as a copy, so every C++ QPageSize behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPageSize that has a ritual and that Python can call
  so far, 17 names in all: 'isEquivalentTo', 'isValid', 'key', 'name', 'id',
  'windowsId', 'definitionSize', 'definitionUnits', 'size', 'sizePoints',
  'sizePixels', 'rect', 'rectPoints', 'rectPixels', 'equals', '__eq__',
  '__ne__'. It can be made from Python, in 7 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPageSize &QPageSize::operator=(QPageSize &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QPageSize &QPageSize::operator=(const QPageSize &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QPageSize::~QPageSize()': the destructor: Python removes its C++
    QPageSize by it, and has no other use for it.
  - Qt's 'void QPageSize::swap(QPageSize &other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QPageSize::QPageSize(QPageSizePrivate &dd)': takes a type Python
    has no way to hand over yet.

  What to expect
  --------------

  - The C++ QPageSize is created at the first use, not by 'QPageSize(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPageSize back gives a copy the ritual made for
    Python, in a new cute QPageSize.
  - Each name of Qt's QPageSize that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPageSize, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class PageSizeId(CuteNum):
    """
    The enum 'QPageSize::PageSizeId' of Qt, with the 125 names Qt gives in
    it.
    """

    Letter = Kee[int](0)
    Legal = Kee[int](1)
    Executive = Kee[int](2)
    A0 = Kee[int](3)
    A1 = Kee[int](4)
    A2 = Kee[int](5)
    A3 = Kee[int](6)
    A4 = Kee[int](7)
    A5 = Kee[int](8)
    A6 = Kee[int](9)
    A7 = Kee[int](10)
    A8 = Kee[int](11)
    A9 = Kee[int](12)
    A10 = Kee[int](13)
    B0 = Kee[int](14)
    B1 = Kee[int](15)
    B2 = Kee[int](16)
    B3 = Kee[int](17)
    B4 = Kee[int](18)
    B5 = Kee[int](19)
    B6 = Kee[int](20)
    B7 = Kee[int](21)
    B8 = Kee[int](22)
    B9 = Kee[int](23)
    B10 = Kee[int](24)
    C5E = Kee[int](25)
    Comm10E = Kee[int](26)
    DLE = Kee[int](27)
    Folio = Kee[int](28)
    Ledger = Kee[int](29)
    Tabloid = Kee[int](30)
    Custom = Kee[int](31)
    A3Extra = Kee[int](32)
    A4Extra = Kee[int](33)
    A4Plus = Kee[int](34)
    A4Small = Kee[int](35)
    A5Extra = Kee[int](36)
    B5Extra = Kee[int](37)
    JisB0 = Kee[int](38)
    JisB1 = Kee[int](39)
    JisB2 = Kee[int](40)
    JisB3 = Kee[int](41)
    JisB4 = Kee[int](42)
    JisB5 = Kee[int](43)
    JisB6 = Kee[int](44)
    JisB7 = Kee[int](45)
    JisB8 = Kee[int](46)
    JisB9 = Kee[int](47)
    JisB10 = Kee[int](48)
    AnsiC = Kee[int](49)
    AnsiD = Kee[int](50)
    AnsiE = Kee[int](51)
    LegalExtra = Kee[int](52)
    LetterExtra = Kee[int](53)
    LetterPlus = Kee[int](54)
    LetterSmall = Kee[int](55)
    TabloidExtra = Kee[int](56)
    ArchA = Kee[int](57)
    ArchB = Kee[int](58)
    ArchC = Kee[int](59)
    ArchD = Kee[int](60)
    ArchE = Kee[int](61)
    Imperial7x9 = Kee[int](62)
    Imperial8x10 = Kee[int](63)
    Imperial9x11 = Kee[int](64)
    Imperial9x12 = Kee[int](65)
    Imperial10x11 = Kee[int](66)
    Imperial10x13 = Kee[int](67)
    Imperial10x14 = Kee[int](68)
    Imperial12x11 = Kee[int](69)
    Imperial15x11 = Kee[int](70)
    ExecutiveStandard = Kee[int](71)
    Note = Kee[int](72)
    Quarto = Kee[int](73)
    Statement = Kee[int](74)
    SuperA = Kee[int](75)
    SuperB = Kee[int](76)
    Postcard = Kee[int](77)
    DoublePostcard = Kee[int](78)
    Prc16K = Kee[int](79)
    Prc32K = Kee[int](80)
    Prc32KBig = Kee[int](81)
    FanFoldUS = Kee[int](82)
    FanFoldGerman = Kee[int](83)
    FanFoldGermanLegal = Kee[int](84)
    EnvelopeB4 = Kee[int](85)
    EnvelopeB5 = Kee[int](86)
    EnvelopeB6 = Kee[int](87)
    EnvelopeC0 = Kee[int](88)
    EnvelopeC1 = Kee[int](89)
    EnvelopeC2 = Kee[int](90)
    EnvelopeC3 = Kee[int](91)
    EnvelopeC4 = Kee[int](92)
    EnvelopeC6 = Kee[int](93)
    EnvelopeC65 = Kee[int](94)
    EnvelopeC7 = Kee[int](95)
    Envelope9 = Kee[int](96)
    Envelope11 = Kee[int](97)
    Envelope12 = Kee[int](98)
    Envelope14 = Kee[int](99)
    EnvelopeMonarch = Kee[int](100)
    EnvelopePersonal = Kee[int](101)
    EnvelopeChou3 = Kee[int](102)
    EnvelopeChou4 = Kee[int](103)
    EnvelopeInvite = Kee[int](104)
    EnvelopeItalian = Kee[int](105)
    EnvelopeKaku2 = Kee[int](106)
    EnvelopeKaku3 = Kee[int](107)
    EnvelopePrc1 = Kee[int](108)
    EnvelopePrc2 = Kee[int](109)
    EnvelopePrc3 = Kee[int](110)
    EnvelopePrc4 = Kee[int](111)
    EnvelopePrc5 = Kee[int](112)
    EnvelopePrc6 = Kee[int](113)
    EnvelopePrc7 = Kee[int](114)
    EnvelopePrc8 = Kee[int](115)
    EnvelopePrc9 = Kee[int](116)
    EnvelopePrc10 = Kee[int](117)
    EnvelopeYou4 = Kee[int](118)
    LastPageSize = Kee[int](118)
    AnsiA = Kee[int](0)
    AnsiB = Kee[int](29)
    EnvelopeC5 = Kee[int](25)
    EnvelopeDL = Kee[int](27)
    Envelope10 = Kee[int](26)

  class SizeMatchPolicy(CuteNum):
    """
    The enum 'QPageSize::SizeMatchPolicy' of Qt, with the 3 names Qt gives in
    it.
    """

    FuzzyMatch = Kee[int](0)
    FuzzyOrientationMatch = Kee[int](1)
    ExactMatch = Kee[int](2)

  class Unit(CuteNum):
    """The enum 'QPageSize::Unit' of Qt, with the 6 names Qt gives in it."""

    Millimeter = Kee[int](0)
    Point = Kee[int](1)
    Inch = Kee[int](2)
    Pica = Kee[int](3)
    Didot = Kee[int](4)
    Cicero = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPageSize'

  #  Qt's '~QPageSize()'. Naming it makes this a value class: Python owns
  #  every C++ QPageSize behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QPageSizeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def isEquivalentTo(self, other: QPageSize) -> bool:
    """
    Calls Qt's 'bool QPageSize::isEquivalentTo(const QPageSize &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#isEquivalentTo

    Parameters
    ----------

    other : QPageSize
      Passed on as a value: Qt reads the C++ QPageSize, which stays Python's
      own.
    """
    #  bool QPageSize::isEquivalentTo(const QPageSize &other) const
    return self.uglySide.call(
        'ritual_ZNK9QPageSize14isEquivalentToERKS_', self._valueOf(other),
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPageSize::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#isValid
    """
    #  bool QPageSize::isValid() const
    return self.uglySide.call('ritual_ZNK9QPageSize7isValidEv')

  @overload()
  def key(self) -> str:
    """
    Calls Qt's 'QString QPageSize::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPageSize::key() const
    return self.uglySide.call('ritual_ZNK9QPageSize3keyEv')

  @staticmethod
  @overload(PageSizeId)
  def key(pageSizeId: PageSizeId) -> str:
    """
    Calls Qt's 'QString QPageSize::key(PageSizeId pageSizeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#key

    Parameters
    ----------

    pageSizeId : PageSizeId
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPageSize::key(PageSizeId pageSizeId)
    return Rituals.call(
        'ritual_ZN9QPageSize3keyENS_10PageSizeIdE', pageSizeId.value,
    )

  @overload()
  def name(self) -> str:
    """
    Calls Qt's 'QString QPageSize::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPageSize::name() const
    return self.uglySide.call('ritual_ZNK9QPageSize4nameEv')

  @staticmethod
  @overload(PageSizeId)
  def name(pageSizeId: PageSizeId) -> str:
    """
    Calls Qt's 'QString QPageSize::name(PageSizeId pageSizeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#name

    Parameters
    ----------

    pageSizeId : PageSizeId
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPageSize::name(PageSizeId pageSizeId)
    return Rituals.call(
        'ritual_ZN9QPageSize4nameENS_10PageSizeIdE', pageSizeId.value,
    )

  @overload()
  def id(self) -> PageSizeId:
    """
    Calls Qt's 'PageSizeId QPageSize::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#id

    Returns
    -------

    PageSizeId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PageSizeId(number)'
      gives.
    """
    #  PageSizeId QPageSize::id() const
    return QPageSize.PageSizeId(self.uglySide.call(
        'ritual_ZNK9QPageSize2idEv',
    ))

  @staticmethod
  @overload(QSize)
  @overload(QSize, SizeMatchPolicy)
  def id(
      pointSize: QSize,
      matchPolicy: SizeMatchPolicy = SizeMatchPolicy.FuzzyMatch,
  ) -> PageSizeId:
    """
    Calls Qt's 'PageSizeId QPageSize::id(const QSize &pointSize,
    SizeMatchPolicy matchPolicy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#id

    Parameters
    ----------

    pointSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    matchPolicy : SizeMatchPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      SizeMatchPolicy.FuzzyMatch.

    Returns
    -------

    PageSizeId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PageSizeId(number)'
      gives.
    """
    #  PageSizeId QPageSize::id(const QSize &pointSize, SizeMatchPolicy
    #      matchPolicy)
    return QPageSize.PageSizeId(Rituals.call(
        'ritual_ZN9QPageSize2idERK5QSizeNS_15SizeMatchPolicyE',
        CuteMixin._valueOf(pointSize), matchPolicy.value,
    ))

  @staticmethod
  @overload(QSizeF, Unit)
  @overload(QSizeF, Unit, SizeMatchPolicy)
  def id(
      size: QSizeF,
      units: Unit,
      matchPolicy: SizeMatchPolicy = SizeMatchPolicy.FuzzyMatch,
  ) -> PageSizeId:
    """
    Calls Qt's 'PageSizeId QPageSize::id(const QSizeF &size, Unit units,
    SizeMatchPolicy matchPolicy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#id

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    units : Unit
      Passed on as its number.

    matchPolicy : SizeMatchPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      SizeMatchPolicy.FuzzyMatch.

    Returns
    -------

    PageSizeId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PageSizeId(number)'
      gives.
    """
    #  PageSizeId QPageSize::id(const QSizeF &size, Unit units,
    #      SizeMatchPolicy matchPolicy)
    return QPageSize.PageSizeId(Rituals.call(
        'ritual_ZN9QPageSize2idERK6QSizeFNS_4UnitENS_15SizeMatchPolicyE',
        CuteMixin._valueOf(size), units.value, matchPolicy.value,
    ))

  @staticmethod
  @overload(int)
  def id(windowsId: int) -> PageSizeId:
    """
    Calls Qt's 'PageSizeId QPageSize::id(int windowsId)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#id

    Parameters
    ----------

    windowsId : int
      Passed on as it is.

    Returns
    -------

    PageSizeId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PageSizeId(number)'
      gives.
    """
    #  PageSizeId QPageSize::id(int windowsId)
    return QPageSize.PageSizeId(Rituals.call(
        'ritual_ZN9QPageSize2idEi', windowsId,
    ))

  @overload()
  def windowsId(self) -> int:
    """
    Calls Qt's 'int QPageSize::windowsId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#windowsId
    """
    #  int QPageSize::windowsId() const
    return self.uglySide.call('ritual_ZNK9QPageSize9windowsIdEv')

  @staticmethod
  @overload(PageSizeId)
  def windowsId(pageSizeId: PageSizeId) -> int:
    """
    Calls Qt's 'int QPageSize::windowsId(PageSizeId pageSizeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#windowsId

    Parameters
    ----------

    pageSizeId : PageSizeId
      Passed on as its number.
    """
    #  int QPageSize::windowsId(PageSizeId pageSizeId)
    return Rituals.call(
        'ritual_ZN9QPageSize9windowsIdENS_10PageSizeIdE', pageSizeId.value,
    )

  @overload()
  def definitionSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QPageSize::definitionSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#definitionSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QPageSize::definitionSize() const
    address = self.uglySide.call('ritual_ZNK9QPageSize14definitionSizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @staticmethod
  @overload(PageSizeId)
  def definitionSize(pageSizeId: PageSizeId) -> QSizeF:
    """
    Calls Qt's 'QSizeF QPageSize::definitionSize(PageSizeId pageSizeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#definitionSize

    Parameters
    ----------

    pageSizeId : PageSizeId
      Passed on as its number.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QPageSize::definitionSize(PageSizeId pageSizeId)
    address = Rituals.call(
        'ritual_ZN9QPageSize14definitionSizeENS_10PageSizeIdE',
        pageSizeId.value,
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload()
  def definitionUnits(self) -> Unit:
    """
    Calls Qt's 'Unit QPageSize::definitionUnits() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#definitionUnits

    Returns
    -------

    Unit
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Unit(number)' gives.
    """
    #  Unit QPageSize::definitionUnits() const
    return QPageSize.Unit(self.uglySide.call(
        'ritual_ZNK9QPageSize15definitionUnitsEv',
    ))

  @staticmethod
  @overload(PageSizeId)
  def definitionUnits(pageSizeId: PageSizeId) -> Unit:
    """
    Calls Qt's 'Unit QPageSize::definitionUnits(PageSizeId pageSizeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#definitionUnits

    Parameters
    ----------

    pageSizeId : PageSizeId
      Passed on as its number.

    Returns
    -------

    Unit
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Unit(number)' gives.
    """
    #  Unit QPageSize::definitionUnits(PageSizeId pageSizeId)
    return QPageSize.Unit(Rituals.call(
        'ritual_ZN9QPageSize15definitionUnitsENS_10PageSizeIdE',
        pageSizeId.value,
    ))

  @overload(Unit)
  def size(self, units: Unit) -> QSizeF:
    """
    Calls Qt's 'QSizeF QPageSize::size(Unit units) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#size

    Parameters
    ----------

    units : Unit
      Passed on as its number.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QPageSize::size(Unit units) const
    address = self.uglySide.call(
        'ritual_ZNK9QPageSize4sizeENS_4UnitE', units.value,
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @staticmethod
  @overload(PageSizeId, Unit)
  def size(pageSizeId: PageSizeId, units: Unit) -> QSizeF:
    """
    Calls Qt's 'QSizeF QPageSize::size(PageSizeId pageSizeId, Unit units)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#size

    Parameters
    ----------

    pageSizeId : PageSizeId
      Passed on as its number.

    units : Unit
      Passed on as its number.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QPageSize::size(PageSizeId pageSizeId, Unit units)
    address = Rituals.call(
        'ritual_ZN9QPageSize4sizeENS_10PageSizeIdENS_4UnitE',
        pageSizeId.value, units.value,
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload()
  def sizePoints(self) -> QSize:
    """
    Calls Qt's 'QSize QPageSize::sizePoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#sizePoints

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPageSize::sizePoints() const
    address = self.uglySide.call('ritual_ZNK9QPageSize10sizePointsEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @staticmethod
  @overload(PageSizeId)
  def sizePoints(pageSizeId: PageSizeId) -> QSize:
    """
    Calls Qt's 'QSize QPageSize::sizePoints(PageSizeId pageSizeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#sizePoints

    Parameters
    ----------

    pageSizeId : PageSizeId
      Passed on as its number.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPageSize::sizePoints(PageSizeId pageSizeId)
    address = Rituals.call(
        'ritual_ZN9QPageSize10sizePointsENS_10PageSizeIdE', pageSizeId.value,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def sizePixels(self, resolution: int) -> QSize:
    """
    Calls Qt's 'QSize QPageSize::sizePixels(int resolution) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#sizePixels

    Parameters
    ----------

    resolution : int
      Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPageSize::sizePixels(int resolution) const
    address = self.uglySide.call(
        'ritual_ZNK9QPageSize10sizePixelsEi', resolution,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @staticmethod
  @overload(PageSizeId, int)
  def sizePixels(pageSizeId: PageSizeId, resolution: int) -> QSize:
    """
    Calls Qt's 'QSize QPageSize::sizePixels(PageSizeId pageSizeId, int
    resolution)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#sizePixels

    Parameters
    ----------

    pageSizeId : PageSizeId
      Passed on as its number.

    resolution : int
      Passed on as it is.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPageSize::sizePixels(PageSizeId pageSizeId, int resolution)
    address = Rituals.call(
        'ritual_ZN9QPageSize10sizePixelsENS_10PageSizeIdEi',
        pageSizeId.value, resolution,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(Unit)
  def rect(self, units: Unit) -> QRectF:
    """
    Calls Qt's 'QRectF QPageSize::rect(Unit units) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#rect

    Parameters
    ----------

    units : Unit
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPageSize::rect(Unit units) const
    address = self.uglySide.call(
        'ritual_ZNK9QPageSize4rectENS_4UnitE', units.value,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def rectPoints(self) -> QRect:
    """
    Calls Qt's 'QRect QPageSize::rectPoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#rectPoints

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPageSize::rectPoints() const
    address = self.uglySide.call('ritual_ZNK9QPageSize10rectPointsEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int)
  def rectPixels(self, resolution: int) -> QRect:
    """
    Calls Qt's 'QRect QPageSize::rectPixels(int resolution) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#rectPixels

    Parameters
    ----------

    resolution : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPageSize::rectPixels(int resolution) const
    address = self.uglySide.call(
        'ritual_ZNK9QPageSize10rectPixelsEi', resolution,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(THIS)
  def equals(self, other: QPageSize) -> bool:
    """
    Calls Qt's 'bool QPageSize::equals(const QPageSize &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#equals

    Parameters
    ----------

    other : QPageSize
      Passed on as a value: Qt reads the C++ QPageSize, which stays Python's
      own.
    """
    #  bool QPageSize::equals(const QPageSize &other) const
    return self.uglySide.call(
        'ritual_ZNK9QPageSize6equalsERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPageSize) -> bool:
    """
    Calls Qt's 'bool operator==(const QPageSize &lhs, const QPageSize &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#operator==

    Parameters
    ----------

    rhs : QPageSize
      Passed on as a value: Qt reads the C++ QPageSize, which stays Python's
      own.
    """
    #  bool operator==(const QPageSize &lhs, const QPageSize &rhs)
    return Rituals.call(
        'ritual_ZeqRK9QPageSizeS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QPageSize) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPageSize &lhs, const QPageSize &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#operator!=

    Parameters
    ----------

    rhs : QPageSize
      Passed on as a value: Qt reads the C++ QPageSize, which stays Python's
      own.
    """
    #  bool operator!=(const QPageSize &lhs, const QPageSize &rhs)
    return Rituals.call(
        'ritual_ZneRK9QPageSizeS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPageSize::QPageSize()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#QPageSize
    """
    #  QPageSize::QPageSize()
    self._noteCreation(QPageSize, lambda: Rituals.call(
        'ritual_ZN9QPageSizeC1Ev',
    ))

  @overload(PageSizeId)
  def __init__(self, pageSizeId: PageSizeId) -> None:
    """
    Notes what was given, for Qt's 'QPageSize::QPageSize(PageSizeId
    pageSizeId)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#QPageSize

    Parameters
    ----------

    pageSizeId : PageSizeId
      Passed on as its number.
    """
    #  QPageSize::QPageSize(PageSizeId pageSizeId)
    self._noteCreation(QPageSize, lambda: Rituals.call(
        'ritual_ZN9QPageSizeC1ENS_10PageSizeIdE', pageSizeId.value,
    ))

  @overload(QSize)
  @overload(QSize, str)
  @overload(QSize, str, SizeMatchPolicy)
  def __init__(
      self,
      pointSize: QSize,
      name: str = '',
      matchPolicy: SizeMatchPolicy = SizeMatchPolicy.FuzzyMatch,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPageSize::QPageSize(const QSize
    &pointSize, const QString &name, SizeMatchPolicy matchPolicy)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#QPageSize

    Parameters
    ----------

    pointSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    matchPolicy : SizeMatchPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      SizeMatchPolicy.FuzzyMatch.
    """
    #  QPageSize::QPageSize(const QSize &pointSize, const QString &name,
    #      SizeMatchPolicy matchPolicy)
    self._noteCreation(QPageSize, lambda: Rituals.call(
        'ritual_ZN9QPageSizeC1ERK5QSizeRK7QStringNS_15SizeMatchPolicyE',
        self._valueOf(pointSize), name, matchPolicy.value,
    ))

  @overload(QSizeF, Unit)
  @overload(QSizeF, Unit, str)
  @overload(QSizeF, Unit, str, SizeMatchPolicy)
  def __init__(
      self,
      size: QSizeF,
      units: Unit,
      name: str = '',
      matchPolicy: SizeMatchPolicy = SizeMatchPolicy.FuzzyMatch,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPageSize::QPageSize(const QSizeF &size,
    Unit units, const QString &name, SizeMatchPolicy matchPolicy)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#QPageSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    units : Unit
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    matchPolicy : SizeMatchPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      SizeMatchPolicy.FuzzyMatch.
    """
    #  QPageSize::QPageSize(const QSizeF &size, Unit units, const QString
    #      &name, SizeMatchPolicy matchPolicy)
    self._noteCreation(QPageSize, lambda: Rituals.call(
        'ritual_ZN9QPageSizeC1ERK6QSizeFNS_4UnitERK7QStringNS_15SizeMatchPo'
        'licyE',
        self._valueOf(size), units.value, name, matchPolicy.value,
    ))

  @overload(THIS)
  def __init__(self, other: QPageSize) -> None:
    """
    Notes what was given, for Qt's 'QPageSize::QPageSize(const QPageSize
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#QPageSize

    Parameters
    ----------

    other : QPageSize
      Passed on as a value: Qt reads the C++ QPageSize, which stays Python's
      own.
    """
    #  QPageSize::QPageSize(const QPageSize &other)
    self._noteCreation(QPageSize, lambda: Rituals.call(
        'ritual_ZN9QPageSizeC1ERKS_', self._valueOf(other),
    ))

  @overload(str, QSize, str)
  def __init__(self, key: str, pointSize: QSize, name: str) -> None:
    """
    Notes what was given, for Qt's 'QPageSize::QPageSize(const QString &key,
    const QSize &pointSize, const QString &name)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#QPageSize

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    pointSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QPageSize::QPageSize(const QString &key, const QSize &pointSize, const
    #      QString &name)
    self._noteCreation(QPageSize, lambda: Rituals.call(
        'ritual_ZN9QPageSizeC1ERK7QStringRK5QSizeS2_',
        key, self._valueOf(pointSize), name,
    ))

  @overload(int, QSize, str)
  def __init__(self, windowsId: int, pointSize: QSize, name: str) -> None:
    """
    Notes what was given, for Qt's 'QPageSize::QPageSize(int windowsId, const
    QSize &pointSize, const QString &name)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#QPageSize

    Parameters
    ----------

    windowsId : int
      Passed on as it is.

    pointSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QPageSize::QPageSize(int windowsId, const QSize &pointSize, const
    #      QString &name)
    self._noteCreation(QPageSize, lambda: Rituals.call(
        'ritual_ZN9QPageSizeC1EiRK5QSizeRK7QString',
        windowsId, self._valueOf(pointSize), name,
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPageSize::swap(QPageSize &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QPageSize.swap' has no cute function yet. Qt's 'void "
        "QPageSize::swap(QPageSize &other)': takes a type Python has no way "
        "to hand over yet.")


#  Qt's 'QList<QPageSize>': the list of QPageSize, which 'QList[QPageSize]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QPageSize.
QList.createKind(
    QPageSize, 'value',
    make='ritual_list_make_QPageSize',
    add='ritual_list_add_QPageSize',
    size='ritual_list_size_QPageSize',
    at='ritual_list_at_QPageSize',
    drop='ritual_list_drop_QPageSize',
)
