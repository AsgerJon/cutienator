"""
QColorVector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolormatrix_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QColorVector to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']


class QColorVector(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorVector: a plain Python object standing in front
  of one C++ QColorVector.

  C++ hands a QColorVector around as a copy, so every C++ QColorVector behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorVector that has a ritual and that Python can
  call so far, 17 names in all: 'fromXYChromaticity', 'isNull', 'isValid',
  'isValidChromaticity', '__mul__', '__add__', '__sub__', 'toChromaticity',
  'D50Chromaticity', 'D65Chromaticity', 'D50', 'D65', 'xyzToLab', 'labToXyz',
  '__eq__', '__ne__', 'fastCbrt'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QColorVector::operator+=(const QColorVector &v)': an operator
    Python has no name for.
  - Qt's 'QColorVector::~QColorVector()': the destructor: Python removes its
    C++ QColorVector by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QColorVector is created at the first use, not by
    'QColorVector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorVector back gives a copy the ritual made for
    Python, in a new cute QColorVector.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPointF)
  def fromXYChromaticity(chr: QPointF) -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorVector::fromXYChromaticity(QPointF chr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorvector.html#fromXYChromaticity

    Parameters
    ----------

    chr : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorVector::fromXYChromaticity(QPointF chr)
    address = Rituals.call(
        'ritual_ZN12QColorVector18fromXYChromaticityE7QPointF',
        CuteMixin._valueOf(chr, 'QPointF'),
    )
    return QColorVector._cuteOwning(address)

  @staticmethod
  @overload(QPointF)
  def isValidChromaticity(chr: QPointF) -> bool:
    """
    Calls Qt's 'bool QColorVector::isValidChromaticity(const QPointF &chr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolorvector.html#isValidChromaticity

    Parameters
    ----------

    chr : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QColorVector::isValidChromaticity(const QPointF &chr)
    return Rituals.call(
        'ritual_ZN12QColorVector19isValidChromaticityERK7QPointF',
        CuteMixin._valueOf(chr, 'QPointF'),
    )

  @staticmethod
  def D50Chromaticity() -> QPointF:
    """
    Calls Qt's 'QPointF QColorVector::D50Chromaticity()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#D50Chromaticity

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QColorVector::D50Chromaticity()
    address = Rituals.call('ritual_ZN12QColorVector15D50ChromaticityEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @staticmethod
  def D65Chromaticity() -> QPointF:
    """
    Calls Qt's 'QPointF QColorVector::D65Chromaticity()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#D65Chromaticity

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QColorVector::D65Chromaticity()
    address = Rituals.call('ritual_ZN12QColorVector15D65ChromaticityEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @staticmethod
  def D50() -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorVector::D50()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#D50

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorVector::D50()
    address = Rituals.call('ritual_ZN12QColorVector3D50Ev')
    return QColorVector._cuteOwning(address)

  @staticmethod
  def D65() -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorVector::D65()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#D65

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorVector::D65()
    address = Rituals.call('ritual_ZN12QColorVector3D65Ev')
    return QColorVector._cuteOwning(address)

  @staticmethod
  @overload(float)
  def fastCbrt(x: float) -> float:
    """
    Calls Qt's 'float QColorVector::fastCbrt(float x)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#fastCbrt

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorVector::fastCbrt(float x)
    return Rituals.call('ritual_ZN12QColorVector8fastCbrtEf', x)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorVector'

  #  Qt's '~QColorVector()'. Naming it makes this a value class: Python owns
  #  every C++ QColorVector behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QColorVectorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QColorVector::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#isNull
    """
    #  bool QColorVector::isNull() const
    return self.uglySide.call('ritual_ZNK12QColorVector6isNullEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QColorVector::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#isValid
    """
    #  bool QColorVector::isValid() const
    return self.uglySide.call('ritual_ZNK12QColorVector7isValidEv')

  def toChromaticity(self) -> QPointF:
    """
    Calls Qt's 'QPointF QColorVector::toChromaticity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#toChromaticity

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QColorVector::toChromaticity() const
    address = self.uglySide.call(
        'ritual_ZNK12QColorVector14toChromaticityEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def xyzToLab(self) -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorVector::xyzToLab() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#xyzToLab

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorVector::xyzToLab() const
    address = self.uglySide.call('ritual_ZNK12QColorVector8xyzToLabEv')
    return QColorVector._cuteOwning(address)

  def labToXyz(self) -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorVector::labToXyz() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#labToXyz

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorVector::labToXyz() const
    address = self.uglySide.call('ritual_ZNK12QColorVector8labToXyzEv')
    return QColorVector._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def __mul__(self, f: float) -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorVector::operator*(float f) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#operator*

    Parameters
    ----------

    f : float
      Passed on as it is.

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorVector::operator*(float f) const
    address = self.uglySide.call('ritual_ZNK12QColorVectormlEf', f)
    return QColorVector._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __add__(self, v: QColorVector) -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorVector::operator+(const QColorVector &v)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#operator+

    Parameters
    ----------

    v : QColorVector
      Passed on as a value: Qt reads the C++ QColorVector, which stays
      Python's own.

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorVector::operator+(const QColorVector &v) const
    address = self.uglySide.call(
        'ritual_ZNK12QColorVectorplERKS_', self._valueOf(v),
    )
    return QColorVector._cuteOwning(address)

  @overload.fallback
  def __add__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __sub__(self, v: QColorVector) -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorVector::operator-(const QColorVector &v)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#operator-

    Parameters
    ----------

    v : QColorVector
      Passed on as a value: Qt reads the C++ QColorVector, which stays
      Python's own.

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorVector::operator-(const QColorVector &v) const
    address = self.uglySide.call(
        'ritual_ZNK12QColorVectormiERKS_', self._valueOf(v),
    )
    return QColorVector._cuteOwning(address)

  @overload.fallback
  def __sub__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QColorVector) -> bool:
    """
    Calls Qt's 'bool operator==(const QColorVector &lhs, const QColorVector
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#operator==

    Parameters
    ----------

    rhs : QColorVector
      Passed on as a value: Qt reads the C++ QColorVector, which stays
      Python's own.
    """
    #  bool operator==(const QColorVector &lhs, const QColorVector &rhs)
    return Rituals.call(
        'ritual_ZeqRK12QColorVectorS1_',
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
  def __ne__(self, rhs: QColorVector) -> bool:
    """
    Calls Qt's 'bool operator!=(const QColorVector &lhs, const QColorVector
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#operator!=

    Parameters
    ----------

    rhs : QColorVector
      Passed on as a value: Qt reads the C++ QColorVector, which stays
      Python's own.
    """
    #  bool operator!=(const QColorVector &lhs, const QColorVector &rhs)
    return Rituals.call(
        'ritual_ZneRK12QColorVectorS1_',
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
    Notes what was given, for Qt's 'QColorVector::QColorVector()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#QColorVector
    """
    #  QColorVector::QColorVector()
    self._noteCreation(QColorVector, lambda: Rituals.call(
        'ritual_ZN12QColorVectorC1Ev',
    ))

  @overload(float, float, float)
  @overload(float, float, float, float)
  def __init__(self, x: float, y: float, z: float, w: float = 0.0) -> None:
    """
    Notes what was given, for Qt's 'QColorVector::QColorVector(float x, float
    y, float z, float w)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolorvector.html#QColorVector

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    w : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QColorVector::QColorVector(float x, float y, float z, float w)
    self._noteCreation(QColorVector, lambda: Rituals.call(
        'ritual_ZN12QColorVectorC1Effff', x, y, z, w,
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
