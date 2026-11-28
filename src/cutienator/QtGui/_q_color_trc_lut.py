"""
QColorTrcLut binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolortrclut_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QColorTrcLut to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QColorTransferFunction, QColorTransferGenericFunction
  from . import QColorTransferTable, QColorTrc, QRgba64
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColorTransferFunction = WAIT['QColorTransferFunction']
  QColorTransferGenericFunction = WAIT['QColorTransferGenericFunction']
  QColorTransferTable = WAIT['QColorTransferTable']
  QColorTrc = WAIT['QColorTrc']
  QRgba64 = WAIT['QRgba64']


class QColorTrcLut(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorTrcLut: a plain Python object standing in front
  of one C++ QColorTrcLut.

  What exists
  -----------

  Every function of Qt's QColorTrcLut that has a ritual and that Python can
  call so far, 13 names in all: 'setFromGamma', 'setFromTransferFunction',
  'setFromTransferTable', 'setFromTransferGenericFunction', 'setFromTrc',
  'toLinear64', 'toLinear', 'u8ToLinearF32', 'u16ToLinearF32',
  'fromLinear64', 'fromLinear', 'u8FromLinearF32', 'u16FromLinearF32'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::shared_ptr<QColorTrcLut> QColorTrcLut::fromGamma(float gamma,
    Direction dir)': gives a type Python has no way to take yet.
  - Qt's 'std::shared_ptr<QColorTrcLut> QColorTrcLut::fromTrc(const QColorTrc
    &trc, Direction dir)': gives a type Python has no way to take yet.
  - Qt's 'std::shared_ptr<QColorTrcLut> QColorTrcLut::create()': gives a type
    Python has no way to take yet.
  - Qt's 'QRgb QColorTrcLut::convertWithTable(QRgb rgb32, const ushort
    *table)': names 'ushort', which has no cute class yet.
  - Qt's 'QRgba64 QColorTrcLut::convertWithTable(QRgba64 rgb64, const ushort
    *table)': names 'ushort', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 24 functions Qt declares: 1 forbidden.

  What to expect
  --------------

  - The C++ QColorTrcLut is created at the first use, not by
    'QColorTrcLut(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QColorTrcLut.
  - Each name of Qt's QColorTrcLut that has no cute function yet,
    'convertWithTable', 'create', 'fromGamma', 'fromTrc', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QColorTrcLut, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Direction(CuteNum):
    """
    The enum 'QColorTrcLut::Direction' of Qt, with the 3 names Qt gives in
    it.
    """

    ToLinear = Kee[int](1)
    FromLinear = Kee[int](2)
    BiLinear = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorTrcLut'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def toLinear64(self, rgb32: int) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QColorTrcLut::toLinear64(QRgb rgb32) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#toLinear64

    Parameters
    ----------

    rgb32 : int
      Passed on as it is.

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QColorTrcLut::toLinear64(QRgb rgb32) const
    address = self.uglySide.call(
        'ritual_ZNK12QColorTrcLut10toLinear64Ej', rgb32,
    )
    from . import QRgba64
    return QRgba64._cuteOwning(address)

  @overload(int)
  def toLinear(self, rgb32: int) -> int:
    """
    Calls Qt's 'QRgb QColorTrcLut::toLinear(QRgb rgb32) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#toLinear

    Parameters
    ----------

    rgb32 : int
      Passed on as it is.
    """
    #  QRgb QColorTrcLut::toLinear(QRgb rgb32) const
    return self.uglySide.call('ritual_ZNK12QColorTrcLut8toLinearEj', rgb32)

  @overload(QRgba64)
  def toLinear(self, rgb64: QRgba64) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QColorTrcLut::toLinear(QRgba64 rgb64) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#toLinear

    Parameters
    ----------

    rgb64 : QRgba64
      Passed on as a value: Qt reads the C++ QRgba64, which stays Python's
      own.

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QColorTrcLut::toLinear(QRgba64 rgb64) const
    address = self.uglySide.call(
        'ritual_ZNK12QColorTrcLut8toLinearE7QRgba64', self._valueOf(rgb64),
    )
    from . import QRgba64
    return QRgba64._cuteOwning(address)

  @overload(float)
  def toLinear(self, f: float) -> float:
    """
    Calls Qt's 'float QColorTrcLut::toLinear(float f) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#toLinear

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  float QColorTrcLut::toLinear(float f) const
    return self.uglySide.call('ritual_ZNK12QColorTrcLut8toLinearEf', f)

  @overload(int)
  def u8ToLinearF32(self, c: int) -> float:
    """
    Calls Qt's 'float QColorTrcLut::u8ToLinearF32(int c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#u8ToLinearF32

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  float QColorTrcLut::u8ToLinearF32(int c) const
    return self.uglySide.call('ritual_ZNK12QColorTrcLut13u8ToLinearF32Ei', c)

  @overload(int)
  def u16ToLinearF32(self, c: int) -> float:
    """
    Calls Qt's 'float QColorTrcLut::u16ToLinearF32(int c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#u16ToLinearF32

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  float QColorTrcLut::u16ToLinearF32(int c) const
    return self.uglySide.call(
        'ritual_ZNK12QColorTrcLut14u16ToLinearF32Ei', c,
    )

  @overload(QRgba64)
  def fromLinear64(self, rgb64: QRgba64) -> int:
    """
    Calls Qt's 'QRgb QColorTrcLut::fromLinear64(QRgba64 rgb64) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#fromLinear64

    Parameters
    ----------

    rgb64 : QRgba64
      Passed on as a value: Qt reads the C++ QRgba64, which stays Python's
      own.
    """
    #  QRgb QColorTrcLut::fromLinear64(QRgba64 rgb64) const
    return self.uglySide.call(
        'ritual_ZNK12QColorTrcLut12fromLinear64E7QRgba64',
        self._valueOf(rgb64),
    )

  @overload(int)
  def fromLinear(self, rgb32: int) -> int:
    """
    Calls Qt's 'QRgb QColorTrcLut::fromLinear(QRgb rgb32) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#fromLinear

    Parameters
    ----------

    rgb32 : int
      Passed on as it is.
    """
    #  QRgb QColorTrcLut::fromLinear(QRgb rgb32) const
    return self.uglySide.call(
        'ritual_ZNK12QColorTrcLut10fromLinearEj', rgb32,
    )

  @overload(QRgba64)
  def fromLinear(self, rgb64: QRgba64) -> QRgba64:
    """
    Calls Qt's 'QRgba64 QColorTrcLut::fromLinear(QRgba64 rgb64) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#fromLinear

    Parameters
    ----------

    rgb64 : QRgba64
      Passed on as a value: Qt reads the C++ QRgba64, which stays Python's
      own.

    Returns
    -------

    QRgba64
      A new cute QRgba64 around the copy Qt gave back. Python owns it.
    """
    #  QRgba64 QColorTrcLut::fromLinear(QRgba64 rgb64) const
    address = self.uglySide.call(
        'ritual_ZNK12QColorTrcLut10fromLinearE7QRgba64',
        self._valueOf(rgb64),
    )
    from . import QRgba64
    return QRgba64._cuteOwning(address)

  @overload(float)
  def fromLinear(self, f: float) -> float:
    """
    Calls Qt's 'float QColorTrcLut::fromLinear(float f) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#fromLinear

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  float QColorTrcLut::fromLinear(float f) const
    return self.uglySide.call('ritual_ZNK12QColorTrcLut10fromLinearEf', f)

  @overload(float)
  def u8FromLinearF32(self, f: float) -> int:
    """
    Calls Qt's 'int QColorTrcLut::u8FromLinearF32(float f) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#u8FromLinearF32

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  int QColorTrcLut::u8FromLinearF32(float f) const
    return self.uglySide.call(
        'ritual_ZNK12QColorTrcLut15u8FromLinearF32Ef', f,
    )

  @overload(float)
  def u16FromLinearF32(self, f: float) -> int:
    """
    Calls Qt's 'int QColorTrcLut::u16FromLinearF32(float f) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#u16FromLinearF32

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  int QColorTrcLut::u16FromLinearF32(float f) const
    return self.uglySide.call(
        'ritual_ZNK12QColorTrcLut16u16FromLinearF32Ef', f,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  @overload(float, Direction)
  def setFromGamma(
      self,
      gamma: float,
      dir: Direction = Direction.BiLinear,
  ) -> None:
    """
    Calls Qt's 'void QColorTrcLut::setFromGamma(float gamma, Direction dir)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#setFromGamma

    Parameters
    ----------

    gamma : float
      Passed on as it is.

    dir : Direction
      Passed on as its number. May be left out, as in Qt: it is then
      Direction.BiLinear.
    """
    #  void QColorTrcLut::setFromGamma(float gamma, Direction dir)
    self.uglySide.call(
        'ritual_ZN12QColorTrcLut12setFromGammaEfNS_9DirectionE',
        gamma, dir.value,
    )

  @overload(QColorTransferFunction)
  @overload(QColorTransferFunction, Direction)
  def setFromTransferFunction(
      self,
      transFn: QColorTransferFunction,
      dir: Direction = Direction.BiLinear,
  ) -> None:
    """
    Calls Qt's 'void QColorTrcLut::setFromTransferFunction(const
    QColorTransferFunction &transFn, Direction dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortrclut.html#setFromTransferFunction

    Parameters
    ----------

    transFn : QColorTransferFunction
      Passed on as a value: Qt reads the C++ QColorTransferFunction, which
      stays Python's own.

    dir : Direction
      Passed on as its number. May be left out, as in Qt: it is then
      Direction.BiLinear.
    """
    #  void QColorTrcLut::setFromTransferFunction(const
    #      QColorTransferFunction &transFn, Direction dir)
    self.uglySide.call(
        'ritual_ZN12QColorTrcLut23setFromTransferFunctionERK22QColorTransfe'
        'rFunctionNS_9DirectionE',
        self._valueOf(transFn), dir.value,
    )

  @overload(QColorTransferTable)
  @overload(QColorTransferTable, Direction)
  def setFromTransferTable(
      self,
      transTable: QColorTransferTable,
      dir: Direction = Direction.BiLinear,
  ) -> None:
    """
    Calls Qt's 'void QColorTrcLut::setFromTransferTable(const
    QColorTransferTable &transTable, Direction dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortrclut.html#setFromTransferTable

    Parameters
    ----------

    transTable : QColorTransferTable
      Passed on as a value: Qt reads the C++ QColorTransferTable, which stays
      Python's own.

    dir : Direction
      Passed on as its number. May be left out, as in Qt: it is then
      Direction.BiLinear.
    """
    #  void QColorTrcLut::setFromTransferTable(const QColorTransferTable
    #      &transTable, Direction dir)
    self.uglySide.call(
        'ritual_ZN12QColorTrcLut20setFromTransferTableERK19QColorTransferTa'
        'bleNS_9DirectionE',
        self._valueOf(transTable), dir.value,
    )

  @overload(QColorTransferGenericFunction, Direction)
  def setFromTransferGenericFunction(
      self,
      transfn: QColorTransferGenericFunction,
      dir: Direction,
  ) -> None:
    """
    Calls Qt's 'void QColorTrcLut::setFromTransferGenericFunction(const
    QColorTransferGenericFunction &transfn, Direction dir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortrclut.html#setFromTransferGenericFunction

    Parameters
    ----------

    transfn : QColorTransferGenericFunction
      Passed on as a value: Qt reads the C++ QColorTransferGenericFunction,
      which stays Python's own.

    dir : Direction
      Passed on as its number.
    """
    #  void QColorTrcLut::setFromTransferGenericFunction(const
    #      QColorTransferGenericFunction &transfn, Direction dir)
    self.uglySide.call(
        'ritual_ZN12QColorTrcLut30setFromTransferGenericFunctionERK29QColor'
        'TransferGenericFunctionNS_9DirectionE',
        self._valueOf(transfn), dir.value,
    )

  @overload(QColorTrc, Direction)
  def setFromTrc(self, trc: QColorTrc, dir: Direction) -> None:
    """
    Calls Qt's 'void QColorTrcLut::setFromTrc(const QColorTrc &trc, Direction
    dir)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#setFromTrc

    Parameters
    ----------

    trc : QColorTrc
      Passed on as a value: Qt reads the C++ QColorTrc, which stays Python's
      own.

    dir : Direction
      Passed on as its number.
    """
    #  void QColorTrcLut::setFromTrc(const QColorTrc &trc, Direction dir)
    self.uglySide.call(
        'ritual_ZN12QColorTrcLut10setFromTrcERK9QColorTrcNS_9DirectionE',
        self._valueOf(trc), dir.value,
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
    Notes what was given, for Qt's 'QColorTrcLut::QColorTrcLut()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrclut.html#QColorTrcLut
    """
    #  QColorTrcLut::QColorTrcLut()
    self._noteCreation(QColorTrcLut, lambda: Rituals.call(
        'ritual_ZN12QColorTrcLutC1Ev',
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
  def convertWithTable(*__, **_) -> Never:
    """
    - Qt's 'QRgb QColorTrcLut::convertWithTable(QRgb rgb32, const ushort
      *table)': names 'ushort', which has no cute class yet.
    - Qt's 'QRgba64 QColorTrcLut::convertWithTable(QRgba64 rgb64, const
      ushort *table)': names 'ushort', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QColorTrcLut.convertWithTable' has no cute function yet. Qt's "
        "'QRgb QColorTrcLut::convertWithTable(QRgb rgb32, const ushort "
        "*table)': names 'ushort', which has no cute class yet. Qt's "
        "'QRgba64 QColorTrcLut::convertWithTable(QRgba64 rgb64, const "
        "ushort *table)': names 'ushort', which has no cute class yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QColorTrcLut> QColorTrcLut::create()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QColorTrcLut.create' has no cute function yet. Qt's "
        "'std::shared_ptr<QColorTrcLut> QColorTrcLut::create()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def fromGamma(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QColorTrcLut> QColorTrcLut::fromGamma(float gamma,
    Direction dir)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QColorTrcLut.fromGamma' has no cute function yet. Qt's "
        "'std::shared_ptr<QColorTrcLut> QColorTrcLut::fromGamma(float "
        "gamma, Direction dir)': gives a type Python has no way to take yet."
    )

  @staticmethod
  def fromTrc(*__, **_) -> Never:
    """
    Qt's 'std::shared_ptr<QColorTrcLut> QColorTrcLut::fromTrc(const QColorTrc
    &trc, Direction dir)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QColorTrcLut.fromTrc' has no cute function yet. Qt's "
        "'std::shared_ptr<QColorTrcLut> QColorTrcLut::fromTrc(const "
        "QColorTrc &trc, Direction dir)': gives a type Python has no way to "
        "take yet.")
