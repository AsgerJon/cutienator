"""
QSGTransform binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgtransform_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGTransform to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QMatrix4x4
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']


class QSGTransform(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGTransform: a plain Python object standing in front
  of one C++ QSGTransform.

  C++ hands a QSGTransform around as a copy, so every C++ QSGTransform behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGTransform that has a ritual and that Python can
  call so far, 6 names in all: 'setMatrix', 'matrix', 'isIdentity', '__eq__',
  '__ne__', 'compareTo'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const float *QSGTransform::invertedData() const': gives 'float',
    which has no cute class yet.
  - Qt's 'QSGTransform::~QSGTransform()': the destructor: Python removes its
    C++ QSGTransform by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSGTransform is created at the first use, not by
    'QSGTransform(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGTransform back gives a copy the ritual made for
    Python, in a new cute QSGTransform.
  - Each name of Qt's QSGTransform that has no cute function yet,
    'invertedData', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGTransform'

  #  Qt's '~QSGTransform()'. Naming it makes this a value class: Python owns
  #  every C++ QSGTransform behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QSGTransformD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def matrix(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QSGTransform::matrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtransform.html#matrix

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QSGTransform::matrix() const
    address = self.uglySide.call('ritual_ZNK12QSGTransform6matrixEv')
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def isIdentity(self) -> bool:
    """
    Calls Qt's 'bool QSGTransform::isIdentity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtransform.html#isIdentity
    """
    #  bool QSGTransform::isIdentity() const
    return self.uglySide.call('ritual_ZNK12QSGTransform10isIdentityEv')

  @overload(THIS)
  def compareTo(self, other: QSGTransform) -> int:
    """
    Calls Qt's 'int QSGTransform::compareTo(const QSGTransform &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtransform.html#compareTo

    Parameters
    ----------

    other : QSGTransform
      Passed on as a value: Qt reads the C++ QSGTransform, which stays
      Python's own.
    """
    #  int QSGTransform::compareTo(const QSGTransform &other) const
    return self.uglySide.call(
        'ritual_ZNK12QSGTransform9compareToERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMatrix4x4)
  def setMatrix(self, matrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QSGTransform::setMatrix(const QMatrix4x4 &matrix)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtransform.html#setMatrix

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QSGTransform::setMatrix(const QMatrix4x4 &matrix)
    self.uglySide.call(
        'ritual_ZN12QSGTransform9setMatrixERK10QMatrix4x4',
        self._valueOf(matrix),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMatrix4x4)
  def __eq__(self, other: QMatrix4x4) -> bool:
    """
    Calls Qt's 'bool QSGTransform::operator==(const QMatrix4x4 &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtransform.html#operator==

    Parameters
    ----------

    other : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  bool QSGTransform::operator==(const QMatrix4x4 &other) const
    return self.uglySide.call(
        'ritual_ZNK12QSGTransformeqERK10QMatrix4x4', self._valueOf(other),
    )

  @overload(THIS)
  def __eq__(self, other: QSGTransform) -> bool:
    """
    Calls Qt's 'bool QSGTransform::operator==(const QSGTransform &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtransform.html#operator==

    Parameters
    ----------

    other : QSGTransform
      Passed on as a value: Qt reads the C++ QSGTransform, which stays
      Python's own.
    """
    #  bool QSGTransform::operator==(const QSGTransform &other) const
    return self.uglySide.call(
        'ritual_ZNK12QSGTransformeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QMatrix4x4)
  def __ne__(self, other: QMatrix4x4) -> bool:
    """
    Calls Qt's 'bool QSGTransform::operator!=(const QMatrix4x4 &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtransform.html#operator!=

    Parameters
    ----------

    other : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  bool QSGTransform::operator!=(const QMatrix4x4 &other) const
    return self.uglySide.call(
        'ritual_ZNK12QSGTransformneERK10QMatrix4x4', self._valueOf(other),
    )

  @overload(THIS)
  def __ne__(self, other: QSGTransform) -> bool:
    """
    Calls Qt's 'bool QSGTransform::operator!=(const QSGTransform &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgtransform.html#operator!=

    Parameters
    ----------

    other : QSGTransform
      Passed on as a value: Qt reads the C++ QSGTransform, which stays
      Python's own.
    """
    #  bool QSGTransform::operator!=(const QSGTransform &other) const
    return self.uglySide.call(
        'ritual_ZNK12QSGTransformneERKS_', self._valueOf(other),
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

  @staticmethod
  def invertedData(*__, **_) -> Never:
    """
    Qt's 'const float *QSGTransform::invertedData() const': gives 'float',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSGTransform.invertedData' has no cute function yet. Qt's 'const "
        "float *QSGTransform::invertedData() const': gives 'float', which "
        "has no cute class yet.")
