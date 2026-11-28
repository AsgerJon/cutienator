"""
QPageRanges binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpageranges.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QPageRanges(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPageRanges: a plain Python object standing in front
  of one C++ QPageRanges.

  C++ hands a QPageRanges around as a copy, so every C++ QPageRanges behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPageRanges that has a ritual and that Python can
  call so far, 13 names in all: '__eq__', '__ne__', 'addPage', 'addRange',
  'clear', 'toString', 'fromString', 'contains', 'isEmpty', 'firstPage',
  'lastPage', 'detach', 'isEqual'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPageRanges::~QPageRanges()': the destructor: Python removes its
    C++ QPageRanges by it, and has no other use for it.
  - Qt's 'QPageRanges &QPageRanges::operator=(const QPageRanges &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QPageRanges::QPageRanges(QPageRanges &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QPageRanges &QPageRanges::operator=(QPageRanges &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QPageRanges::swap(QPageRanges &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QList<Range> QPageRanges::toRangeList() const': gives a type Python
    has no way to take yet.

  What to expect
  --------------

  - The C++ QPageRanges is created at the first use, not by
    'QPageRanges(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPageRanges back gives a copy the ritual made for
    Python, in a new cute QPageRanges.
  - Each name of Qt's QPageRanges that has no cute function yet, 'swap',
    'toRangeList', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QPageRanges, each a class in here as in
  #  C++.

  class Range(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QPageRanges::Range: a plain Python object standing
    in front of one C++ QPageRanges::Range.

    C++ hands a QPageRanges::Range around as a copy, so every C++
    QPageRanges::Range behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QPageRanges::Range that has a ritual and that
    Python can call so far, 4 names in all: 'contains', '__eq__', '__ne__',
    '__lt__'. None can be made from Python: one comes out of a function of
    another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QPageRanges::Range::~Range()': the destructor: Python removes its
      C++ QPageRanges::Range by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QPageRanges::Range is created at the first use, not by
      'QPageRanges::Range(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QPageRanges::Range back gives a copy the ritual
      made for Python, in a new cute QPageRanges::Range.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QPageRanges::Range'

    #  Qt's '~QPageRanges::Range()'. Naming it makes this a value class:
    #  Python owns every C++ QPageRanges::Range behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QPageRanges5RangeD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    def contains(self, pageNumber: int) -> bool:
      """
      Calls Qt's 'bool QPageRanges::Range::contains(int pageNumber) const'.

      Qt's own words: https://doc.qt.io/qt-6/qpageranges-range.html#contains

      Parameters
      ----------

      pageNumber : int
        Passed on as it is.
      """
      #  bool QPageRanges::Range::contains(int pageNumber) const
      return self.uglySide.call(
          'ritual_ZNK11QPageRanges5Range8containsEi', pageNumber,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, rhs: QPageRanges.Range) -> bool:
      """
      Calls Qt's 'bool operator==(Range lhs, Range rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qpageranges-range.html#operator==

      Parameters
      ----------

      rhs : QPageRanges.Range
        Passed on as a value: Qt reads the C++ QPageRanges::Range, which
        stays Python's own.
      """
      #  bool operator==(Range lhs, Range rhs)
      return Rituals.call(
          'ritual_ZeqN11QPageRanges5RangeES0_',
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
    def __ne__(self, rhs: QPageRanges.Range) -> bool:
      """
      Calls Qt's 'bool operator!=(Range lhs, Range rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qpageranges-range.html#operator!=

      Parameters
      ----------

      rhs : QPageRanges.Range
        Passed on as a value: Qt reads the C++ QPageRanges::Range, which
        stays Python's own.
      """
      #  bool operator!=(Range lhs, Range rhs)
      return Rituals.call(
          'ritual_ZneN11QPageRanges5RangeES0_',
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

    @overload(THIS)
    def __lt__(self, rhs: QPageRanges.Range) -> bool:
      """
      Calls Qt's 'bool operator<(Range lhs, Range rhs)'.

      Qt's own words: https://doc.qt.io/qt-6/qpageranges-range.html#operator<

      Parameters
      ----------

      rhs : QPageRanges.Range
        Passed on as a value: Qt reads the C++ QPageRanges::Range, which
        stays Python's own.
      """
      #  bool operator<(Range lhs, Range rhs)
      return Rituals.call(
          'ritual_ZltN11QPageRanges5RangeES0_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __lt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def fromString(ranges: str) -> QPageRanges:
    """
    Calls Qt's 'QPageRanges QPageRanges::fromString(const QString &ranges)'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#fromString

    Parameters
    ----------

    ranges : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QPageRanges
      A new cute QPageRanges around the copy Qt gave back. Python owns it.
    """
    #  QPageRanges QPageRanges::fromString(const QString &ranges)
    address = Rituals.call(
        'ritual_ZN11QPageRanges10fromStringERK7QString', ranges,
    )
    return QPageRanges._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPageRanges'

  #  Qt's '~QPageRanges()'. Naming it makes this a value class: Python owns
  #  every C++ QPageRanges behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QPageRangesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toString(self) -> str:
    """
    Calls Qt's 'QString QPageRanges::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPageRanges::toString() const
    return self.uglySide.call('ritual_ZNK11QPageRanges8toStringEv')

  @overload(int)
  def contains(self, pageNumber: int) -> bool:
    """
    Calls Qt's 'bool QPageRanges::contains(int pageNumber) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#contains

    Parameters
    ----------

    pageNumber : int
      Passed on as it is.
    """
    #  bool QPageRanges::contains(int pageNumber) const
    return self.uglySide.call(
        'ritual_ZNK11QPageRanges8containsEi', pageNumber,
    )

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPageRanges::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#isEmpty
    """
    #  bool QPageRanges::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QPageRanges7isEmptyEv')

  def firstPage(self) -> int:
    """
    Calls Qt's 'int QPageRanges::firstPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#firstPage
    """
    #  int QPageRanges::firstPage() const
    return self.uglySide.call('ritual_ZNK11QPageRanges9firstPageEv')

  def lastPage(self) -> int:
    """
    Calls Qt's 'int QPageRanges::lastPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#lastPage
    """
    #  int QPageRanges::lastPage() const
    return self.uglySide.call('ritual_ZNK11QPageRanges8lastPageEv')

  @overload(THIS)
  def isEqual(self, other: QPageRanges) -> bool:
    """
    Calls Qt's 'bool QPageRanges::isEqual(const QPageRanges &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#isEqual

    Parameters
    ----------

    other : QPageRanges
      Passed on as a value: Qt reads the C++ QPageRanges, which stays
      Python's own.
    """
    #  bool QPageRanges::isEqual(const QPageRanges &other) const
    return self.uglySide.call(
        'ritual_ZNK11QPageRanges7isEqualERKS_', self._valueOf(other),
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
  def __eq__(self, rhs: QPageRanges) -> bool:
    """
    Calls Qt's 'bool operator==(const QPageRanges &lhs, const QPageRanges
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#operator==

    Parameters
    ----------

    rhs : QPageRanges
      Passed on as a value: Qt reads the C++ QPageRanges, which stays
      Python's own.
    """
    #  bool operator==(const QPageRanges &lhs, const QPageRanges &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QPageRangesS1_',
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
  def __ne__(self, rhs: QPageRanges) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPageRanges &lhs, const QPageRanges
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#operator!=

    Parameters
    ----------

    rhs : QPageRanges
      Passed on as a value: Qt reads the C++ QPageRanges, which stays
      Python's own.
    """
    #  bool operator!=(const QPageRanges &lhs, const QPageRanges &rhs)
    return Rituals.call(
        'ritual_ZneRK11QPageRangesS1_',
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
    Notes what was given, for Qt's 'QPageRanges::QPageRanges()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#QPageRanges
    """
    #  QPageRanges::QPageRanges()
    self._noteCreation(QPageRanges, lambda: Rituals.call(
        'ritual_ZN11QPageRangesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPageRanges) -> None:
    """
    Notes what was given, for Qt's 'QPageRanges::QPageRanges(const
    QPageRanges &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#QPageRanges

    Parameters
    ----------

    other : QPageRanges
      Passed on as a value: Qt reads the C++ QPageRanges, which stays
      Python's own.
    """
    #  QPageRanges::QPageRanges(const QPageRanges &other)
    self._noteCreation(QPageRanges, lambda: Rituals.call(
        'ritual_ZN11QPageRangesC1ERKS_', self._valueOf(other),
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
  def addPage(self, pageNumber: int) -> None:
    """
    Calls Qt's 'void QPageRanges::addPage(int pageNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#addPage

    Parameters
    ----------

    pageNumber : int
      Passed on as it is.
    """
    #  void QPageRanges::addPage(int pageNumber)
    self.uglySide.call('ritual_ZN11QPageRanges7addPageEi', pageNumber)

  @overload(int, int)
  def addRange(self, from_: int, to: int) -> None:
    """
    Calls Qt's 'void QPageRanges::addRange(int from, int to)'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#addRange

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.
    """
    #  void QPageRanges::addRange(int from, int to)
    self.uglySide.call('ritual_ZN11QPageRanges8addRangeEii', from_, to)

  def clear(self) -> None:
    """
    Calls Qt's 'void QPageRanges::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#clear
    """
    #  void QPageRanges::clear()
    self.uglySide.call('ritual_ZN11QPageRanges5clearEv')

  def detach(self) -> None:
    """
    Calls Qt's 'void QPageRanges::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qpageranges.html#detach
    """
    #  void QPageRanges::detach()
    self.uglySide.call('ritual_ZN11QPageRanges6detachEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPageRanges::swap(QPageRanges &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPageRanges.swap' has no cute function yet. Qt's 'void "
        "QPageRanges::swap(QPageRanges &other)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def toRangeList(*__, **_) -> Never:
    """
    Qt's 'QList<Range> QPageRanges::toRangeList() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QPageRanges.toRangeList' has no cute function yet. Qt's "
        "'QList<Range> QPageRanges::toRangeList() const': gives a type "
        "Python has no way to take yet.")
