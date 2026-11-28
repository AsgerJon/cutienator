"""
QClipperUtils binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/6.12.0/QtPositioning/private/qclipperutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QClipperUtils to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
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

  from . import QDoubleVector2D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDoubleVector2D = WAIT['QDoubleVector2D']


class QClipperUtils(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QClipperUtils: a plain Python object standing in
  front of one C++ QClipperUtils.

  C++ hands a QClipperUtils around as a copy, so every C++ QClipperUtils
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QClipperUtils that has a ritual and that Python can
  call so far, 6 names in all: 'clipperScaleFactor', 'pointInPolygon',
  'clearClipper', 'addSubjectPath', 'addClipPolygon', 'setPolygon'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QClipperUtils::~QClipperUtils()': the destructor: Python removes
    its C++ QClipperUtils by it, and has no other use for it.
  - Qt's 'QList<QList<QDoubleVector2D>> QClipperUtils::execute(Operation op,
    PolyFillType subjFillType, PolyFillType clipFillType)': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ QClipperUtils is created at the first use, not by
    'QClipperUtils(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QClipperUtils back gives a copy the ritual made for
    Python, in a new cute QClipperUtils.
  - Each name of Qt's QClipperUtils that has no cute function yet, 'execute',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QClipperUtils, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Operation(CuteNum):
    """
    The enum 'QClipperUtils::Operation' of Qt, with the 4 names Qt gives in
    it.
    """

    Union = Kee[int](0)
    Intersection = Kee[int](1)
    Difference = Kee[int](2)
    Xor = Kee[int](3)

  class PolyFillType(CuteNum):
    """
    The enum 'QClipperUtils::PolyFillType' of Qt, with the 4 names Qt gives
    in it.
    """

    pftEvenOdd = Kee[int](0)
    pftNonZero = Kee[int](1)
    pftPositive = Kee[int](2)
    pftNegative = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def clipperScaleFactor() -> float:
    """
    Calls Qt's 'double QClipperUtils::clipperScaleFactor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qclipperutils.html#clipperScaleFactor
    """
    #  double QClipperUtils::clipperScaleFactor()
    return Rituals.call('ritual_ZN13QClipperUtils18clipperScaleFactorEv')

  @staticmethod
  @overload(QDoubleVector2D, QList[QDoubleVector2D])
  def pointInPolygon(
      point: QDoubleVector2D,
      polygon: QList[QDoubleVector2D],
  ) -> int:
    """
    Calls Qt's 'int QClipperUtils::pointInPolygon(const QDoubleVector2D
    &point, const QList<QDoubleVector2D> &polygon)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipperutils.html#pointInPolygon

    Parameters
    ----------

    point : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    polygon : QList[QDoubleVector2D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  int QClipperUtils::pointInPolygon(const QDoubleVector2D &point, const
    #      QList<QDoubleVector2D> &polygon)
    return Rituals.call(
        'ritual_ZN13QClipperUtils14pointInPolygonERK15QDoubleVector2DRK5QLi'
        'stIS0_E',
        CuteMixin._valueOf(point), CuteMixin._valueOf(polygon),
    )

  @overload(QDoubleVector2D)
  def pointInPolygon(self, point: QDoubleVector2D) -> int:
    """
    Calls Qt's 'int QClipperUtils::pointInPolygon(const QDoubleVector2D
    &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qclipperutils.html#pointInPolygon

    Parameters
    ----------

    point : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  int QClipperUtils::pointInPolygon(const QDoubleVector2D &point) const
    return self.uglySide.call(
        'ritual_ZNK13QClipperUtils14pointInPolygonERK15QDoubleVector2D',
        self._valueOf(point),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QClipperUtils'

  #  Qt's '~QClipperUtils()'. Naming it makes this a value class: Python owns
  #  every C++ QClipperUtils behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QClipperUtilsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QDoubleVector2D])
  def setPolygon(self, polygon: QList[QDoubleVector2D]) -> None:
    """
    Calls Qt's 'void QClipperUtils::setPolygon(const QList<QDoubleVector2D>
    &polygon)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipperutils.html#setPolygon

    Parameters
    ----------

    polygon : QList[QDoubleVector2D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QClipperUtils::setPolygon(const QList<QDoubleVector2D> &polygon)
    self.uglySide.call(
        'ritual_ZN13QClipperUtils10setPolygonERK5QListI15QDoubleVector2DE',
        self._valueOf(polygon),
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
    Notes what was given, for Qt's 'QClipperUtils::QClipperUtils()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qclipperutils.html#QClipperUtils
    """
    #  QClipperUtils::QClipperUtils()
    self._noteCreation(QClipperUtils, lambda: Rituals.call(
        'ritual_ZN13QClipperUtilsC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QClipperUtils) -> None:
    """
    Notes what was given, for Qt's 'QClipperUtils::QClipperUtils(const
    QClipperUtils &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qclipperutils.html#QClipperUtils

    Parameters
    ----------

    other : QClipperUtils
      Passed on as a value: Qt reads the C++ QClipperUtils, which stays
      Python's own.
    """
    #  QClipperUtils::QClipperUtils(const QClipperUtils &other)
    self._noteCreation(QClipperUtils, lambda: Rituals.call(
        'ritual_ZN13QClipperUtilsC1ERKS_', self._valueOf(other),
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

  def clearClipper(self) -> None:
    """
    Calls Qt's 'void QClipperUtils::clearClipper()'.

    Qt's own words: https://doc.qt.io/qt-6/qclipperutils.html#clearClipper
    """
    #  void QClipperUtils::clearClipper()
    self.uglySide.call('ritual_ZN13QClipperUtils12clearClipperEv')

  @overload(QList[QDoubleVector2D], bool)
  def addSubjectPath(
      self,
      path: QList[QDoubleVector2D],
      closed: bool,
  ) -> None:
    """
    Calls Qt's 'void QClipperUtils::addSubjectPath(const
    QList<QDoubleVector2D> &path, bool closed)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipperutils.html#addSubjectPath

    Parameters
    ----------

    path : QList[QDoubleVector2D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    closed : bool
      Passed on as it is.
    """
    #  void QClipperUtils::addSubjectPath(const QList<QDoubleVector2D> &path,
    #      bool closed)
    self.uglySide.call(
        'ritual_ZN13QClipperUtils14addSubjectPathERK5QListI15QDoubleVector2'
        'DEb',
        self._valueOf(path), closed,
    )

  @overload(QList[QDoubleVector2D])
  def addClipPolygon(self, path: QList[QDoubleVector2D]) -> None:
    """
    Calls Qt's 'void QClipperUtils::addClipPolygon(const
    QList<QDoubleVector2D> &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qclipperutils.html#addClipPolygon

    Parameters
    ----------

    path : QList[QDoubleVector2D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QClipperUtils::addClipPolygon(const QList<QDoubleVector2D> &path)
    self.uglySide.call(
        'ritual_ZN13QClipperUtils14addClipPolygonERK5QListI15QDoubleVector2'
        'DE',
        self._valueOf(path),
    )

  @staticmethod
  def execute(*__, **_) -> Never:
    """
    Qt's 'QList<QList<QDoubleVector2D>> QClipperUtils::execute(Operation op,
    PolyFillType subjFillType, PolyFillType clipFillType)': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QClipperUtils.execute' has no cute function yet. Qt's "
        "'QList<QList<QDoubleVector2D>> QClipperUtils::execute(Operation "
        "op, PolyFillType subjFillType, PolyFillType clipFillType)': gives "
        "a type Python has no way to take yet.")
