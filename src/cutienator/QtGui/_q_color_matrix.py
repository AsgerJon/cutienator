"""
QColorMatrix binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolormatrix_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QColorMatrix to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QColorVector
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColorVector = WAIT['QColorVector']


class QColorMatrix(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorMatrix: a plain Python object standing in front
  of one C++ QColorMatrix.

  C++ hands a QColorMatrix around as a copy, so every C++ QColorMatrix behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorMatrix that has a ritual and that Python can
  call so far, 18 names in all: 'isNull', 'determinant', 'isValid',
  'isIdentity', 'inverted', '__mul__', 'map', 'transposed', 'identity',
  'fromScale', 'chromaticAdaptation', 'toXyzFromSRgb', 'toXyzFromAdobeRgb',
  'toXyzFromDciP3D65', 'toXyzFromProPhotoRgb', 'toXyzFromBt2020', '__eq__',
  '__ne__'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorMatrix::~QColorMatrix()': the destructor: Python removes its
    C++ QColorMatrix by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QColorMatrix is created at the first use, not by
    'QColorMatrix(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorMatrix back gives a copy the ritual made for
    Python, in a new cute QColorMatrix.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def identity() -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix QColorMatrix::identity()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#identity

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix QColorMatrix::identity()
    address = Rituals.call('ritual_ZN12QColorMatrix8identityEv')
    return QColorMatrix._cuteOwning(address)

  @staticmethod
  @overload(QColorVector)
  def fromScale(v: QColorVector) -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix QColorMatrix::fromScale(QColorVector v)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#fromScale

    Parameters
    ----------

    v : QColorVector
      Passed on as a value: Qt reads the C++ QColorVector, which stays
      Python's own.

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix QColorMatrix::fromScale(QColorVector v)
    address = Rituals.call(
        'ritual_ZN12QColorMatrix9fromScaleE12QColorVector',
        CuteMixin._valueOf(v),
    )
    return QColorMatrix._cuteOwning(address)

  @staticmethod
  @overload(QColorVector)
  def chromaticAdaptation(whitePoint: QColorVector) -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix QColorMatrix::chromaticAdaptation(const
    QColorVector &whitePoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolormatrix.html#chromaticAdaptation

    Parameters
    ----------

    whitePoint : QColorVector
      Passed on as a value: Qt reads the C++ QColorVector, which stays
      Python's own.

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix QColorMatrix::chromaticAdaptation(const QColorVector
    #      &whitePoint)
    address = Rituals.call(
        'ritual_ZN12QColorMatrix19chromaticAdaptationERK12QColorVector',
        CuteMixin._valueOf(whitePoint),
    )
    return QColorMatrix._cuteOwning(address)

  @staticmethod
  def toXyzFromSRgb() -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix QColorMatrix::toXyzFromSRgb()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#toXyzFromSRgb

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix QColorMatrix::toXyzFromSRgb()
    address = Rituals.call('ritual_ZN12QColorMatrix13toXyzFromSRgbEv')
    return QColorMatrix._cuteOwning(address)

  @staticmethod
  def toXyzFromAdobeRgb() -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix QColorMatrix::toXyzFromAdobeRgb()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolormatrix.html#toXyzFromAdobeRgb

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix QColorMatrix::toXyzFromAdobeRgb()
    address = Rituals.call('ritual_ZN12QColorMatrix17toXyzFromAdobeRgbEv')
    return QColorMatrix._cuteOwning(address)

  @staticmethod
  def toXyzFromDciP3D65() -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix QColorMatrix::toXyzFromDciP3D65()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolormatrix.html#toXyzFromDciP3D65

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix QColorMatrix::toXyzFromDciP3D65()
    address = Rituals.call('ritual_ZN12QColorMatrix17toXyzFromDciP3D65Ev')
    return QColorMatrix._cuteOwning(address)

  @staticmethod
  def toXyzFromProPhotoRgb() -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix QColorMatrix::toXyzFromProPhotoRgb()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolormatrix.html#toXyzFromProPhotoRgb

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix QColorMatrix::toXyzFromProPhotoRgb()
    address = Rituals.call('ritual_ZN12QColorMatrix20toXyzFromProPhotoRgbEv')
    return QColorMatrix._cuteOwning(address)

  @staticmethod
  def toXyzFromBt2020() -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix QColorMatrix::toXyzFromBt2020()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#toXyzFromBt2020

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix QColorMatrix::toXyzFromBt2020()
    address = Rituals.call('ritual_ZN12QColorMatrix15toXyzFromBt2020Ev')
    return QColorMatrix._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorMatrix'

  #  Qt's '~QColorMatrix()'. Naming it makes this a value class: Python owns
  #  every C++ QColorMatrix behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QColorMatrixD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QColorMatrix::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#isNull
    """
    #  bool QColorMatrix::isNull() const
    return self.uglySide.call('ritual_ZNK12QColorMatrix6isNullEv')

  def determinant(self) -> float:
    """
    Calls Qt's 'float QColorMatrix::determinant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#determinant
    """
    #  float QColorMatrix::determinant() const
    return self.uglySide.call('ritual_ZNK12QColorMatrix11determinantEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QColorMatrix::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#isValid
    """
    #  bool QColorMatrix::isValid() const
    return self.uglySide.call('ritual_ZNK12QColorMatrix7isValidEv')

  def isIdentity(self) -> bool:
    """
    Calls Qt's 'bool QColorMatrix::isIdentity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#isIdentity
    """
    #  bool QColorMatrix::isIdentity() const
    return self.uglySide.call('ritual_ZNK12QColorMatrix10isIdentityEv')

  def inverted(self) -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix QColorMatrix::inverted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#inverted

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix QColorMatrix::inverted() const
    address = self.uglySide.call('ritual_ZNK12QColorMatrix8invertedEv')
    return QColorMatrix._cuteOwning(address)

  @overload(QColorVector)
  def map(self, c: QColorVector) -> QColorVector:
    """
    Calls Qt's 'QColorVector QColorMatrix::map(const QColorVector &c) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#map

    Parameters
    ----------

    c : QColorVector
      Passed on as a value: Qt reads the C++ QColorVector, which stays
      Python's own.

    Returns
    -------

    QColorVector
      A new cute QColorVector around the copy Qt gave back. Python owns it.
    """
    #  QColorVector QColorMatrix::map(const QColorVector &c) const
    address = self.uglySide.call(
        'ritual_ZNK12QColorMatrix3mapERK12QColorVector', self._valueOf(c),
    )
    from . import QColorVector
    return QColorVector._cuteOwning(address)

  def transposed(self) -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix QColorMatrix::transposed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#transposed

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix QColorMatrix::transposed() const
    address = self.uglySide.call('ritual_ZNK12QColorMatrix10transposedEv')
    return QColorMatrix._cuteOwning(address)

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
  def __mul__(self, o: QColorMatrix) -> QColorMatrix:
    """
    Calls Qt's 'QColorMatrix operator*(const QColorMatrix &a, const
    QColorMatrix &o)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#operator*

    Parameters
    ----------

    o : QColorMatrix
      Passed on as a value: Qt reads the C++ QColorMatrix, which stays
      Python's own.

    Returns
    -------

    QColorMatrix
      A new cute QColorMatrix around the copy Qt gave back. Python owns it.
    """
    #  QColorMatrix operator*(const QColorMatrix &a, const QColorMatrix &o)
    address = Rituals.call(
        'ritual_ZmlRK12QColorMatrixS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(o),
    )
    return QColorMatrix._cuteOwning(address)

  @overload.fallback
  def __mul__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __eq__(self, rhs: QColorMatrix) -> bool:
    """
    Calls Qt's 'bool operator==(const QColorMatrix &lhs, const QColorMatrix
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#operator==

    Parameters
    ----------

    rhs : QColorMatrix
      Passed on as a value: Qt reads the C++ QColorMatrix, which stays
      Python's own.
    """
    #  bool operator==(const QColorMatrix &lhs, const QColorMatrix &rhs)
    return Rituals.call(
        'ritual_ZeqRK12QColorMatrixS1_',
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
  def __ne__(self, rhs: QColorMatrix) -> bool:
    """
    Calls Qt's 'bool operator!=(const QColorMatrix &lhs, const QColorMatrix
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolormatrix.html#operator!=

    Parameters
    ----------

    rhs : QColorMatrix
      Passed on as a value: Qt reads the C++ QColorMatrix, which stays
      Python's own.
    """
    #  bool operator!=(const QColorMatrix &lhs, const QColorMatrix &rhs)
    return Rituals.call(
        'ritual_ZneRK12QColorMatrixS1_',
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
