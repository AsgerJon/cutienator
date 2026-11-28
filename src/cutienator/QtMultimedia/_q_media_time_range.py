"""
QMediaTimeRange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qmediatimerange.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QMediaTimeRange(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMediaTimeRange: a plain Python object standing in
  front of one C++ QMediaTimeRange.

  C++ hands a QMediaTimeRange around as a copy, so every C++ QMediaTimeRange
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMediaTimeRange that has a ritual and that Python
  can call so far, 15 names in all: 'detach', 'earliestTime', 'latestTime',
  'isEmpty', 'isContinuous', 'contains', 'addInterval', 'addTimeRange',
  'removeInterval', 'removeTimeRange', '__iadd__', '__isub__', 'clear',
  '__eq__', '__ne__'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMediaTimeRange::~QMediaTimeRange()': the destructor: Python
    removes its C++ QMediaTimeRange by it, and has no other use for it.
  - Qt's 'QMediaTimeRange &QMediaTimeRange::operator=(const QMediaTimeRange
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QMediaTimeRange::QMediaTimeRange(QMediaTimeRange &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QMediaTimeRange &QMediaTimeRange::operator=(QMediaTimeRange
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QMediaTimeRange::swap(QMediaTimeRange &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QMediaTimeRange &QMediaTimeRange::operator=(const Interval &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QList<QMediaTimeRange::Interval> QMediaTimeRange::intervals()
    const': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QMediaTimeRange is created at the first use, not by
    'QMediaTimeRange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMediaTimeRange back gives a copy the ritual made for
    Python, in a new cute QMediaTimeRange.
  - Each name of Qt's QMediaTimeRange that has no cute function yet,
    'intervals', 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QMediaTimeRange, each a class in here as in
  #  C++.

  class Interval(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QMediaTimeRange::Interval: a plain Python object
    standing in front of one C++ QMediaTimeRange::Interval.

    C++ hands a QMediaTimeRange::Interval around as a copy, so every C++
    QMediaTimeRange::Interval behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QMediaTimeRange::Interval that has a ritual and
    that Python can call so far, 8 names in all: 'start', 'end', 'contains',
    'isNormal', 'normalized', 'translated', '__eq__', '__ne__'. It can be
    made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QMediaTimeRange::Interval::~Interval()': the destructor: Python
      removes its C++ QMediaTimeRange::Interval by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QMediaTimeRange::Interval is created at the first use, not by
      'QMediaTimeRange::Interval(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QMediaTimeRange::Interval back gives a copy the
      ritual made for Python, in a new cute QMediaTimeRange::Interval.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QMediaTimeRange::Interval'

    #  Qt's '~QMediaTimeRange::Interval()'. Naming it makes this a value
    #  class: Python owns every C++ QMediaTimeRange::Interval behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QMediaTimeRange8IntervalD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def start(self) -> int:
      """
      Calls Qt's 'qint64 QMediaTimeRange::Interval::start() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmediatimerange-interval.html#start
      """
      #  qint64 QMediaTimeRange::Interval::start() const
      return self.uglySide.call(
          'ritual_ZNK15QMediaTimeRange8Interval5startEv',
      )

    def end(self) -> int:
      """
      Calls Qt's 'qint64 QMediaTimeRange::Interval::end() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmediatimerange-interval.html#end
      """
      #  qint64 QMediaTimeRange::Interval::end() const
      return self.uglySide.call('ritual_ZNK15QMediaTimeRange8Interval3endEv')

    @overload(int)
    def contains(self, time: int) -> bool:
      """
      Calls Qt's 'bool QMediaTimeRange::Interval::contains(qint64 time)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmediatimerange-interval.html#contains

      Parameters
      ----------

      time : int
        Passed on as it is.
      """
      #  bool QMediaTimeRange::Interval::contains(qint64 time) const
      return self.uglySide.call(
          'ritual_ZNK15QMediaTimeRange8Interval8containsEx', time,
      )

    def isNormal(self) -> bool:
      """
      Calls Qt's 'bool QMediaTimeRange::Interval::isNormal() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmediatimerange-interval.html#isNormal
      """
      #  bool QMediaTimeRange::Interval::isNormal() const
      return self.uglySide.call(
          'ritual_ZNK15QMediaTimeRange8Interval8isNormalEv',
      )

    def normalized(self) -> QMediaTimeRange.Interval:
      """
      Calls Qt's 'Interval QMediaTimeRange::Interval::normalized() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmediatimerange-interval.html#normalized

      Returns
      -------

      QMediaTimeRange.Interval
        A new cute QMediaTimeRange::Interval around the copy Qt gave back.
        Python owns it.
      """
      #  Interval QMediaTimeRange::Interval::normalized() const
      address = self.uglySide.call(
          'ritual_ZNK15QMediaTimeRange8Interval10normalizedEv',
      )
      return QMediaTimeRange.Interval._cuteOwning(address)

    @overload(int)
    def translated(self, offset: int) -> QMediaTimeRange.Interval:
      """
      Calls Qt's 'Interval QMediaTimeRange::Interval::translated(qint64
      offset) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmediatimerange-interval.html#translated

      Parameters
      ----------

      offset : int
        Passed on as it is.

      Returns
      -------

      QMediaTimeRange.Interval
        A new cute QMediaTimeRange::Interval around the copy Qt gave back.
        Python owns it.
      """
      #  Interval QMediaTimeRange::Interval::translated(qint64 offset) const
      address = self.uglySide.call(
          'ritual_ZNK15QMediaTimeRange8Interval10translatedEx', offset,
      )
      return QMediaTimeRange.Interval._cuteOwning(address)

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
    def __eq__(self, rhs: QMediaTimeRange.Interval) -> bool:
      """
      Calls Qt's 'bool operator==(Interval lhs, Interval rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmediatimerange-interval.html#operator==

      Parameters
      ----------

      rhs : QMediaTimeRange.Interval
        Passed on as a value: Qt reads the C++ QMediaTimeRange::Interval,
        which stays Python's own.
      """
      #  bool operator==(Interval lhs, Interval rhs)
      return Rituals.call(
          'ritual_ZeqN15QMediaTimeRange8IntervalES0_',
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
    def __ne__(self, rhs: QMediaTimeRange.Interval) -> bool:
      """
      Calls Qt's 'bool operator!=(Interval lhs, Interval rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmediatimerange-interval.html#operator!=

      Parameters
      ----------

      rhs : QMediaTimeRange.Interval
        Passed on as a value: Qt reads the C++ QMediaTimeRange::Interval,
        which stays Python's own.
      """
      #  bool operator!=(Interval lhs, Interval rhs)
      return Rituals.call(
          'ritual_ZneN15QMediaTimeRange8IntervalES0_',
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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QMediaTimeRange::Interval::Interval()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qmediatimerange-interval.html#Interval
      """
      #  QMediaTimeRange::Interval::Interval()
      self._noteCreation(QMediaTimeRange.Interval, lambda: Rituals.call(
          'ritual_ZN15QMediaTimeRange8IntervalC1Ev',
      ))

    @overload(int, int)
    def __init__(self, start: int, end: int) -> None:
      """
      Notes what was given, for Qt's
      'QMediaTimeRange::Interval::Interval(qint64 start, qint64 end)', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qmediatimerange-interval.html#Interval

      Parameters
      ----------

      start : int
        Passed on as it is.

      end : int
        Passed on as it is.
      """
      #  QMediaTimeRange::Interval::Interval(qint64 start, qint64 end)
      self._noteCreation(QMediaTimeRange.Interval, lambda: Rituals.call(
          'ritual_ZN15QMediaTimeRange8IntervalC1Exx', start, end,
      ))

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaTimeRange'

  #  Qt's '~QMediaTimeRange()'. Naming it makes this a value class: Python
  #  owns every C++ QMediaTimeRange behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QMediaTimeRangeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def earliestTime(self) -> int:
    """
    Calls Qt's 'qint64 QMediaTimeRange::earliestTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#earliestTime
    """
    #  qint64 QMediaTimeRange::earliestTime() const
    return self.uglySide.call('ritual_ZNK15QMediaTimeRange12earliestTimeEv')

  def latestTime(self) -> int:
    """
    Calls Qt's 'qint64 QMediaTimeRange::latestTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#latestTime
    """
    #  qint64 QMediaTimeRange::latestTime() const
    return self.uglySide.call('ritual_ZNK15QMediaTimeRange10latestTimeEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QMediaTimeRange::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#isEmpty
    """
    #  bool QMediaTimeRange::isEmpty() const
    return self.uglySide.call('ritual_ZNK15QMediaTimeRange7isEmptyEv')

  def isContinuous(self) -> bool:
    """
    Calls Qt's 'bool QMediaTimeRange::isContinuous() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#isContinuous
    """
    #  bool QMediaTimeRange::isContinuous() const
    return self.uglySide.call('ritual_ZNK15QMediaTimeRange12isContinuousEv')

  @overload(int)
  def contains(self, time: int) -> bool:
    """
    Calls Qt's 'bool QMediaTimeRange::contains(qint64 time) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#contains

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  bool QMediaTimeRange::contains(qint64 time) const
    return self.uglySide.call('ritual_ZNK15QMediaTimeRange8containsEx', time)

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
  def __iadd__(self, a0: QMediaTimeRange) -> QMediaTimeRange:
    """
    Calls Qt's 'QMediaTimeRange &QMediaTimeRange::operator+=(const
    QMediaTimeRange &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#operator+=

    Parameters
    ----------

    a0 : QMediaTimeRange
      Passed on as a value: Qt reads the C++ QMediaTimeRange, which stays
      Python's own.
    """
    #  QMediaTimeRange &QMediaTimeRange::operator+=(const QMediaTimeRange
    #      &a0)
    self.uglySide.call(
        'ritual_ZN15QMediaTimeRangepLERKS_', self._valueOf(a0),
    )
    return self

  @overload(Interval)
  def __iadd__(self, a0: Interval) -> QMediaTimeRange:
    """
    Calls Qt's 'QMediaTimeRange &QMediaTimeRange::operator+=(const Interval
    &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#operator+=

    Parameters
    ----------

    a0 : Interval
      Passed on as a value: Qt reads the C++ QMediaTimeRange::Interval, which
      stays Python's own.
    """
    #  QMediaTimeRange &QMediaTimeRange::operator+=(const Interval &a0)
    self.uglySide.call(
        'ritual_ZN15QMediaTimeRangepLERKNS_8IntervalE', self._valueOf(a0),
    )
    return self

  @overload.fallback
  def __iadd__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __isub__(self, a0: QMediaTimeRange) -> QMediaTimeRange:
    """
    Calls Qt's 'QMediaTimeRange &QMediaTimeRange::operator-=(const
    QMediaTimeRange &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#operator-=

    Parameters
    ----------

    a0 : QMediaTimeRange
      Passed on as a value: Qt reads the C++ QMediaTimeRange, which stays
      Python's own.
    """
    #  QMediaTimeRange &QMediaTimeRange::operator-=(const QMediaTimeRange
    #      &a0)
    self.uglySide.call(
        'ritual_ZN15QMediaTimeRangemIERKS_', self._valueOf(a0),
    )
    return self

  @overload(Interval)
  def __isub__(self, a0: Interval) -> QMediaTimeRange:
    """
    Calls Qt's 'QMediaTimeRange &QMediaTimeRange::operator-=(const Interval
    &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#operator-=

    Parameters
    ----------

    a0 : Interval
      Passed on as a value: Qt reads the C++ QMediaTimeRange::Interval, which
      stays Python's own.
    """
    #  QMediaTimeRange &QMediaTimeRange::operator-=(const Interval &a0)
    self.uglySide.call(
        'ritual_ZN15QMediaTimeRangemIERKNS_8IntervalE', self._valueOf(a0),
    )
    return self

  @overload.fallback
  def __isub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QMediaTimeRange) -> bool:
    """
    Calls Qt's 'bool operator==(const QMediaTimeRange &lhs, const
    QMediaTimeRange &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#operator==

    Parameters
    ----------

    rhs : QMediaTimeRange
      Passed on as a value: Qt reads the C++ QMediaTimeRange, which stays
      Python's own.
    """
    #  bool operator==(const QMediaTimeRange &lhs, const QMediaTimeRange
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK15QMediaTimeRangeS1_',
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
  def __ne__(self, rhs: QMediaTimeRange) -> bool:
    """
    Calls Qt's 'bool operator!=(const QMediaTimeRange &lhs, const
    QMediaTimeRange &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#operator!=

    Parameters
    ----------

    rhs : QMediaTimeRange
      Passed on as a value: Qt reads the C++ QMediaTimeRange, which stays
      Python's own.
    """
    #  bool operator!=(const QMediaTimeRange &lhs, const QMediaTimeRange
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK15QMediaTimeRangeS1_',
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
    Notes what was given, for Qt's 'QMediaTimeRange::QMediaTimeRange()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediatimerange.html#QMediaTimeRange
    """
    #  QMediaTimeRange::QMediaTimeRange()
    self._noteCreation(QMediaTimeRange, lambda: Rituals.call(
        'ritual_ZN15QMediaTimeRangeC1Ev',
    ))

  @overload(int, int)
  def __init__(self, start: int, end: int) -> None:
    """
    Notes what was given, for Qt's 'QMediaTimeRange::QMediaTimeRange(qint64
    start, qint64 end)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediatimerange.html#QMediaTimeRange

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  QMediaTimeRange::QMediaTimeRange(qint64 start, qint64 end)
    self._noteCreation(QMediaTimeRange, lambda: Rituals.call(
        'ritual_ZN15QMediaTimeRangeC1Exx', start, end,
    ))

  @overload(Interval)
  def __init__(self, a0: Interval) -> None:
    """
    Notes what was given, for Qt's 'QMediaTimeRange::QMediaTimeRange(const
    Interval &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediatimerange.html#QMediaTimeRange

    Parameters
    ----------

    a0 : Interval
      Passed on as a value: Qt reads the C++ QMediaTimeRange::Interval, which
      stays Python's own.
    """
    #  QMediaTimeRange::QMediaTimeRange(const Interval &a0)
    self._noteCreation(QMediaTimeRange, lambda: Rituals.call(
        'ritual_ZN15QMediaTimeRangeC1ERKNS_8IntervalE', self._valueOf(a0),
    ))

  @overload(THIS)
  def __init__(self, range: QMediaTimeRange) -> None:
    """
    Notes what was given, for Qt's 'QMediaTimeRange::QMediaTimeRange(const
    QMediaTimeRange &range)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediatimerange.html#QMediaTimeRange

    Parameters
    ----------

    range : QMediaTimeRange
      Passed on as a value: Qt reads the C++ QMediaTimeRange, which stays
      Python's own.
    """
    #  QMediaTimeRange::QMediaTimeRange(const QMediaTimeRange &range)
    self._noteCreation(QMediaTimeRange, lambda: Rituals.call(
        'ritual_ZN15QMediaTimeRangeC1ERKS_', self._valueOf(range),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QMediaTimeRange::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#detach
    """
    #  void QMediaTimeRange::detach()
    self.uglySide.call('ritual_ZN15QMediaTimeRange6detachEv')

  @overload(int, int)
  def addInterval(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QMediaTimeRange::addInterval(qint64 start, qint64 end)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#addInterval

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QMediaTimeRange::addInterval(qint64 start, qint64 end)
    self.uglySide.call(
        'ritual_ZN15QMediaTimeRange11addIntervalExx', start, end,
    )

  @overload(Interval)
  def addInterval(self, interval: Interval) -> None:
    """
    Calls Qt's 'void QMediaTimeRange::addInterval(const Interval &interval)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#addInterval

    Parameters
    ----------

    interval : Interval
      Passed on as a value: Qt reads the C++ QMediaTimeRange::Interval, which
      stays Python's own.
    """
    #  void QMediaTimeRange::addInterval(const Interval &interval)
    self.uglySide.call(
        'ritual_ZN15QMediaTimeRange11addIntervalERKNS_8IntervalE',
        self._valueOf(interval),
    )

  @overload(THIS)
  def addTimeRange(self, a0: QMediaTimeRange) -> None:
    """
    Calls Qt's 'void QMediaTimeRange::addTimeRange(const QMediaTimeRange
    &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#addTimeRange

    Parameters
    ----------

    a0 : QMediaTimeRange
      Passed on as a value: Qt reads the C++ QMediaTimeRange, which stays
      Python's own.
    """
    #  void QMediaTimeRange::addTimeRange(const QMediaTimeRange &a0)
    self.uglySide.call(
        'ritual_ZN15QMediaTimeRange12addTimeRangeERKS_', self._valueOf(a0),
    )

  @overload(int, int)
  def removeInterval(self, start: int, end: int) -> None:
    """
    Calls Qt's 'void QMediaTimeRange::removeInterval(qint64 start, qint64
    end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediatimerange.html#removeInterval

    Parameters
    ----------

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QMediaTimeRange::removeInterval(qint64 start, qint64 end)
    self.uglySide.call(
        'ritual_ZN15QMediaTimeRange14removeIntervalExx', start, end,
    )

  @overload(Interval)
  def removeInterval(self, interval: Interval) -> None:
    """
    Calls Qt's 'void QMediaTimeRange::removeInterval(const Interval
    &interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediatimerange.html#removeInterval

    Parameters
    ----------

    interval : Interval
      Passed on as a value: Qt reads the C++ QMediaTimeRange::Interval, which
      stays Python's own.
    """
    #  void QMediaTimeRange::removeInterval(const Interval &interval)
    self.uglySide.call(
        'ritual_ZN15QMediaTimeRange14removeIntervalERKNS_8IntervalE',
        self._valueOf(interval),
    )

  @overload(THIS)
  def removeTimeRange(self, a0: QMediaTimeRange) -> None:
    """
    Calls Qt's 'void QMediaTimeRange::removeTimeRange(const QMediaTimeRange
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediatimerange.html#removeTimeRange

    Parameters
    ----------

    a0 : QMediaTimeRange
      Passed on as a value: Qt reads the C++ QMediaTimeRange, which stays
      Python's own.
    """
    #  void QMediaTimeRange::removeTimeRange(const QMediaTimeRange &a0)
    self.uglySide.call(
        'ritual_ZN15QMediaTimeRange15removeTimeRangeERKS_',
        self._valueOf(a0),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QMediaTimeRange::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediatimerange.html#clear
    """
    #  void QMediaTimeRange::clear()
    self.uglySide.call('ritual_ZN15QMediaTimeRange5clearEv')

  @staticmethod
  def intervals(*__, **_) -> Never:
    """
    Qt's 'QList<QMediaTimeRange::Interval> QMediaTimeRange::intervals()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QMediaTimeRange.intervals' has no cute function yet. Qt's "
        "'QList<QMediaTimeRange::Interval> QMediaTimeRange::intervals() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QMediaTimeRange::swap(QMediaTimeRange &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMediaTimeRange.swap' has no cute function yet. Qt's 'void "
        "QMediaTimeRange::swap(QMediaTimeRange &other)': takes a type "
        "Python has no way to hand over yet.")
