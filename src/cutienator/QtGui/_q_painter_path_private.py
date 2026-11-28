"""
QPainterPathPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpainterpath_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPainterPathPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from . import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPainterPathPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPainterPathPrivate: a plain Python object standing
  in front of one C++ QPainterPathPrivate.

  C++ hands a QPainterPathPrivate around as a copy, so every C++
  QPainterPathPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPainterPathPrivate that has a ritual and that
  Python can call so far, 13 names in all: 'isClosed', 'close',
  'maybeMoveTo', 'clear', 'endPointOfElement', 'computeRunLengths',
  'elementAtLength', 'elementAtT', 'appendTrimmedElement',
  'appendStartOfElement', 'appendEndOfElement', 'appendSliceOfElement',
  'appendElementRange'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPainterPathPrivate::~QPainterPathPrivate()': the destructor:
    Python removes its C++ QPainterPathPrivate by it, and has no other use
    for it.
  - Qt's 'QBezier QPainterPathPrivate::bezierAtT(const QPainterPath &path,
    qreal t, qreal *startingLength, qreal *bezierLength) const': takes a
    number to change where it is.
  - Qt's 'const QVectorPath &QPainterPathPrivate::vectorPath()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 22 functions Qt declares: 2 written with the class 'QPainterPath',
  which declares it as well and stands first in it; 1 forbidden.

  What to expect
  --------------

  - The C++ QPainterPathPrivate is created at the first use, not by
    'QPainterPathPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPainterPathPrivate back gives a copy the ritual made
    for Python, in a new cute QPainterPathPrivate.
  - Each name of Qt's QPainterPathPrivate that has no cute function yet,
    'bezierAtT', 'vectorPath', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPainterPathPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class TrimFlags(CuteNum):
    """
    The enum 'QPainterPathPrivate::TrimFlags' of Qt, with the 2 names Qt
    gives in it.
    """

    TrimStart = Kee[int](1)
    TrimEnd = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPainterPathPrivate'

  #  Qt's '~QPainterPathPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QPainterPathPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QPainterPathPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isClosed(self) -> bool:
    """
    Calls Qt's 'bool QPainterPathPrivate::isClosed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpathprivate.html#isClosed
    """
    #  bool QPainterPathPrivate::isClosed() const
    return self.uglySide.call('ritual_ZNK19QPainterPathPrivate8isClosedEv')

  @overload(int)
  def endPointOfElement(self, elemIdx: int) -> QPointF:
    """
    Calls Qt's 'QPointF QPainterPathPrivate::endPointOfElement(int elemIdx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#endPointOfElement

    Parameters
    ----------

    elemIdx : int
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPainterPathPrivate::endPointOfElement(int elemIdx) const
    address = self.uglySide.call(
        'ritual_ZNK19QPainterPathPrivate17endPointOfElementEi', elemIdx,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

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
    Notes what was given, for Qt's
    'QPainterPathPrivate::QPainterPathPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#QPainterPathPrivate
    """
    #  QPainterPathPrivate::QPainterPathPrivate()
    self._noteCreation(QPainterPathPrivate, lambda: Rituals.call(
        'ritual_ZN19QPainterPathPrivateC1Ev',
    ))

  @overload(QPointF)
  def __init__(self, startPoint: QPointF) -> None:
    """
    Notes what was given, for Qt's
    'QPainterPathPrivate::QPainterPathPrivate(QPointF startPoint)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#QPainterPathPrivate

    Parameters
    ----------

    startPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QPainterPathPrivate::QPainterPathPrivate(QPointF startPoint)
    self._noteCreation(QPainterPathPrivate, lambda: Rituals.call(
        'ritual_ZN19QPainterPathPrivateC1E7QPointF',
        self._valueOf(startPoint, 'QPointF'),
    ))

  @overload(THIS)
  def __init__(self, other: QPainterPathPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QPainterPathPrivate::QPainterPathPrivate(const QPainterPathPrivate
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#QPainterPathPrivate

    Parameters
    ----------

    other : QPainterPathPrivate
      Passed on as a value: Qt reads the C++ QPainterPathPrivate, which stays
      Python's own.
    """
    #  QPainterPathPrivate::QPainterPathPrivate(const QPainterPathPrivate
    #      &other)
    self._noteCreation(QPainterPathPrivate, lambda: Rituals.call(
        'ritual_ZN19QPainterPathPrivateC1ERKS_', self._valueOf(other),
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

  def close(self) -> None:
    """
    Calls Qt's 'void QPainterPathPrivate::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpathprivate.html#close
    """
    #  void QPainterPathPrivate::close()
    self.uglySide.call('ritual_ZN19QPainterPathPrivate5closeEv')

  def maybeMoveTo(self) -> None:
    """
    Calls Qt's 'void QPainterPathPrivate::maybeMoveTo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#maybeMoveTo
    """
    #  void QPainterPathPrivate::maybeMoveTo()
    self.uglySide.call('ritual_ZN19QPainterPathPrivate11maybeMoveToEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QPainterPathPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpathprivate.html#clear
    """
    #  void QPainterPathPrivate::clear()
    self.uglySide.call('ritual_ZN19QPainterPathPrivate5clearEv')

  def computeRunLengths(self) -> None:
    """
    Calls Qt's 'void QPainterPathPrivate::computeRunLengths()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#computeRunLengths
    """
    #  void QPainterPathPrivate::computeRunLengths()
    self.uglySide.call('ritual_ZN19QPainterPathPrivate17computeRunLengthsEv')

  @overload(float)
  def elementAtLength(self, len: float) -> int:
    """
    Calls Qt's 'int QPainterPathPrivate::elementAtLength(qreal len)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#elementAtLength

    Parameters
    ----------

    len : float
      Passed on as it is.
    """
    #  int QPainterPathPrivate::elementAtLength(qreal len)
    return self.uglySide.call(
        'ritual_ZN19QPainterPathPrivate15elementAtLengthEd', len,
    )

  @overload(float)
  def elementAtT(self, t: float) -> int:
    """
    Calls Qt's 'int QPainterPathPrivate::elementAtT(qreal t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#elementAtT

    Parameters
    ----------

    t : float
      Passed on as it is.
    """
    #  int QPainterPathPrivate::elementAtT(qreal t)
    return self.uglySide.call(
        'ritual_ZN19QPainterPathPrivate10elementAtTEd', t,
    )

  @overload(QPainterPath, int, int, float, float)
  @overload(NoneType, int, int, float, float)
  def appendTrimmedElement(
      self,
      to: Optional[QPainterPath],
      elemIdx: int,
      trimFlags: int,
      startLen: float,
      endLen: float,
  ) -> None:
    """
    Calls Qt's 'void QPainterPathPrivate::appendTrimmedElement(QPainterPath
    *to, int elemIdx, int trimFlags, qreal startLen, qreal endLen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#appendTrimmedElement

    Parameters
    ----------

    to : Optional[QPainterPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    elemIdx : int
      Passed on as it is.

    trimFlags : int
      Passed on as it is.

    startLen : float
      Passed on as it is.

    endLen : float
      Passed on as it is.
    """
    #  void QPainterPathPrivate::appendTrimmedElement(QPainterPath *to, int
    #      elemIdx, int trimFlags, qreal startLen, qreal endLen)
    self.uglySide.call(
        'ritual_ZN19QPainterPathPrivate20appendTrimmedElementEP12QPainterPa'
        'thiidd',
        self._addressOf(to), elemIdx, trimFlags, startLen, endLen,
    )

  @overload(QPainterPath, int, float)
  @overload(NoneType, int, float)
  def appendStartOfElement(
      self,
      to: Optional[QPainterPath],
      elemIdx: int,
      len: float,
  ) -> None:
    """
    Calls Qt's 'void QPainterPathPrivate::appendStartOfElement(QPainterPath
    *to, int elemIdx, qreal len)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#appendStartOfElement

    Parameters
    ----------

    to : Optional[QPainterPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    elemIdx : int
      Passed on as it is.

    len : float
      Passed on as it is.
    """
    #  void QPainterPathPrivate::appendStartOfElement(QPainterPath *to, int
    #      elemIdx, qreal len)
    self.uglySide.call(
        'ritual_ZN19QPainterPathPrivate20appendStartOfElementEP12QPainterPa'
        'thid',
        self._addressOf(to), elemIdx, len,
    )

  @overload(QPainterPath, int, float)
  @overload(NoneType, int, float)
  def appendEndOfElement(
      self,
      to: Optional[QPainterPath],
      elemIdx: int,
      len: float,
  ) -> None:
    """
    Calls Qt's 'void QPainterPathPrivate::appendEndOfElement(QPainterPath
    *to, int elemIdx, qreal len)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#appendEndOfElement

    Parameters
    ----------

    to : Optional[QPainterPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    elemIdx : int
      Passed on as it is.

    len : float
      Passed on as it is.
    """
    #  void QPainterPathPrivate::appendEndOfElement(QPainterPath *to, int
    #      elemIdx, qreal len)
    self.uglySide.call(
        'ritual_ZN19QPainterPathPrivate18appendEndOfElementEP12QPainterPath'
        'id',
        self._addressOf(to), elemIdx, len,
    )

  @overload(QPainterPath, int, float, float)
  @overload(NoneType, int, float, float)
  def appendSliceOfElement(
      self,
      to: Optional[QPainterPath],
      elemIdx: int,
      fromLen: float,
      toLen: float,
  ) -> None:
    """
    Calls Qt's 'void QPainterPathPrivate::appendSliceOfElement(QPainterPath
    *to, int elemIdx, qreal fromLen, qreal toLen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#appendSliceOfElement

    Parameters
    ----------

    to : Optional[QPainterPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    elemIdx : int
      Passed on as it is.

    fromLen : float
      Passed on as it is.

    toLen : float
      Passed on as it is.
    """
    #  void QPainterPathPrivate::appendSliceOfElement(QPainterPath *to, int
    #      elemIdx, qreal fromLen, qreal toLen)
    self.uglySide.call(
        'ritual_ZN19QPainterPathPrivate20appendSliceOfElementEP12QPainterPa'
        'thidd',
        self._addressOf(to), elemIdx, fromLen, toLen,
    )

  @overload(QPainterPath, int, int)
  @overload(NoneType, int, int)
  def appendElementRange(
      self,
      to: Optional[QPainterPath],
      first: int,
      last: int,
  ) -> None:
    """
    Calls Qt's 'void QPainterPathPrivate::appendElementRange(QPainterPath
    *to, int first, int last)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpathprivate.html#appendElementRange

    Parameters
    ----------

    to : Optional[QPainterPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    first : int
      Passed on as it is.

    last : int
      Passed on as it is.
    """
    #  void QPainterPathPrivate::appendElementRange(QPainterPath *to, int
    #      first, int last)
    self.uglySide.call(
        'ritual_ZN19QPainterPathPrivate18appendElementRangeEP12QPainterPath'
        'ii',
        self._addressOf(to), first, last,
    )

  @staticmethod
  def bezierAtT(*__, **_) -> Never:
    """
    Qt's 'QBezier QPainterPathPrivate::bezierAtT(const QPainterPath &path,
    qreal t, qreal *startingLength, qreal *bezierLength) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QPainterPathPrivate.bezierAtT' has no cute function yet. Qt's "
        "'QBezier QPainterPathPrivate::bezierAtT(const QPainterPath &path, "
        "qreal t, qreal *startingLength, qreal *bezierLength) const': takes "
        "a number to change where it is.")

  @staticmethod
  def vectorPath(*__, **_) -> Never:
    """
    Qt's 'const QVectorPath &QPainterPathPrivate::vectorPath()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPainterPathPrivate.vectorPath' has no cute function yet. Qt's "
        "'const QVectorPath &QPainterPathPrivate::vectorPath()': gives a "
        "type Python has no way to take yet.")
