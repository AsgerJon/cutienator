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

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QPageSizePageSizeId, QPageSizeSizeMatchPolicy, QPageSizeUnit

if TYPE_CHECKING:  # pragma: no cover, no mutate
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
  so far, 14 names in all: 'isEquivalentTo', 'isValid', 'key', 'name', 'id',
  'windowsId', 'definitionSize', 'definitionUnits', 'size', 'sizePoints',
  'sizePixels', 'rect', 'rectPoints', 'rectPixels'. It can be made from
  Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPageSize::~QPageSize()': the destructor: Python removes its C++
    QPageSize by it, and has no other use for it.
  - Qt's 'PageSizeId QPageSize::id() const': another kind of method than most
    functions of its name, and one name is one kind of method.
  - Qt's 'QString QPageSize::key(PageSizeId pageSizeId)': another kind of
    method than most functions of its name, and one name is one kind of
    method.
  - Qt's 'QString QPageSize::name(PageSizeId pageSizeId)': another kind of
    method than most functions of its name, and one name is one kind of
    method.
  - Qt's 'int QPageSize::windowsId(PageSizeId pageSizeId)': another kind of
    method than most functions of its name, and one name is one kind of
    method.
  - Qt's 'QSizeF QPageSize::definitionSize(PageSizeId pageSizeId)': another
    kind of method than most functions of its name, and one name is one kind
    of method.
  - Qt's 'Unit QPageSize::definitionUnits(PageSizeId pageSizeId)': another
    kind of method than most functions of its name, and one name is one kind
    of method.
  - Qt's 'QSizeF QPageSize::size(PageSizeId pageSizeId, Unit units)': another
    kind of method than most functions of its name, and one name is one kind
    of method.
  - Qt's 'QSize QPageSize::sizePoints(PageSizeId pageSizeId)': another kind
    of method than most functions of its name, and one name is one kind of
    method.
  - Qt's 'QSize QPageSize::sizePixels(PageSizeId pageSizeId, int
    resolution)': another kind of method than most functions of its name, and
    one name is one kind of method.

  What has no ritual
  ------------------

  7 of the 38 functions Qt declares: 4 private; 3 takes or gives a type that
  cannot be passed yet.

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
  """

  #  The enums Qt writes inside QPageSize, and the names Qt has for the
  #  combinations of its flags enums.
  PageSizeId = QPageSizePageSizeId
  SizeMatchPolicy = QPageSizeSizeMatchPolicy
  Unit = QPageSizeUnit

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def windowsId(self) -> int:
    """
    Calls Qt's 'int QPageSize::windowsId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesize.html#windowsId
    """
    #  int QPageSize::windowsId() const
    return self.uglySide.call('ritual_ZNK9QPageSize9windowsIdEv')

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
