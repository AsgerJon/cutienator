"""
QColorTransferGenericFunction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolortransfergeneric_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QColorTransferGenericFunction to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QColorTransferGenericFunction(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorTransferGenericFunction: a plain Python object
  standing in front of one C++ QColorTransferGenericFunction.

  C++ hands a QColorTransferGenericFunction around as a copy, so every C++
  QColorTransferGenericFunction behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QColorTransferGenericFunction that has a ritual and
  that Python can call so far, 10 names in all: 'hlg', 'pq', 'apply',
  'applyInverse', '__eq__', '__ne__', 'hlgFromLinear', 'hlgToLinear',
  'pqToLinear', 'pqFromLinear'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorTransferGenericFunction::QColorTransferGenericFunction(
    ConverterPtr toLinear, ConverterPtr fromLinear)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QColorTransferGenericFunction::~QColorTransferGenericFunction()':
    the destructor: Python removes its C++ QColorTransferGenericFunction by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QColorTransferGenericFunction is created at the first use, not by
    'QColorTransferGenericFunction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorTransferGenericFunction back gives a copy the
    ritual made for Python, in a new cute QColorTransferGenericFunction.
  - Each name of Qt's QColorTransferGenericFunction that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def hlg() -> QColorTransferGenericFunction:
    """
    Calls Qt's 'QColorTransferGenericFunction
    QColorTransferGenericFunction::hlg()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfergenericfunction.html#hlg

    Returns
    -------

    QColorTransferGenericFunction
      A new cute QColorTransferGenericFunction around the copy Qt gave back.
      Python owns it.
    """
    #  QColorTransferGenericFunction QColorTransferGenericFunction::hlg()
    address = Rituals.call('ritual_ZN29QColorTransferGenericFunction3hlgEv')
    return QColorTransferGenericFunction._cuteOwning(address)

  @staticmethod
  def pq() -> QColorTransferGenericFunction:
    """
    Calls Qt's 'QColorTransferGenericFunction
    QColorTransferGenericFunction::pq()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfergenericfunction.html#pq

    Returns
    -------

    QColorTransferGenericFunction
      A new cute QColorTransferGenericFunction around the copy Qt gave back.
      Python owns it.
    """
    #  QColorTransferGenericFunction QColorTransferGenericFunction::pq()
    address = Rituals.call('ritual_ZN29QColorTransferGenericFunction2pqEv')
    return QColorTransferGenericFunction._cuteOwning(address)

  @staticmethod
  @overload(float)
  def hlgFromLinear(x: float) -> float:
    """
    Calls Qt's 'float QColorTransferGenericFunction::hlgFromLinear(float x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfergenericfunction.html#hlgFromLinear

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorTransferGenericFunction::hlgFromLinear(float x)
    return Rituals.call(
        'ritual_ZN29QColorTransferGenericFunction13hlgFromLinearEf', x,
    )

  @staticmethod
  @overload(float)
  def hlgToLinear(x: float) -> float:
    """
    Calls Qt's 'float QColorTransferGenericFunction::hlgToLinear(float x)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfergenericfunction.html#hlgToLinear

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorTransferGenericFunction::hlgToLinear(float x)
    return Rituals.call(
        'ritual_ZN29QColorTransferGenericFunction11hlgToLinearEf', x,
    )

  @staticmethod
  @overload(float)
  def pqToLinear(e: float) -> float:
    """
    Calls Qt's 'float QColorTransferGenericFunction::pqToLinear(float e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfergenericfunction.html#pqToLinear

    Parameters
    ----------

    e : float
      Passed on as it is.
    """
    #  float QColorTransferGenericFunction::pqToLinear(float e)
    return Rituals.call(
        'ritual_ZN29QColorTransferGenericFunction10pqToLinearEf', e,
    )

  @staticmethod
  @overload(float)
  def pqFromLinear(fd: float) -> float:
    """
    Calls Qt's 'float QColorTransferGenericFunction::pqFromLinear(float fd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfergenericfunction.html#pqFromLinear

    Parameters
    ----------

    fd : float
      Passed on as it is.
    """
    #  float QColorTransferGenericFunction::pqFromLinear(float fd)
    return Rituals.call(
        'ritual_ZN29QColorTransferGenericFunction12pqFromLinearEf', fd,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorTransferGenericFunction'

  #  Qt's '~QColorTransferGenericFunction()'. Naming it makes this a value
  #  class: Python owns every C++ QColorTransferGenericFunction behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QColorTransferGenericFunctionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def apply(self, x: float) -> float:
    """
    Calls Qt's 'float QColorTransferGenericFunction::apply(float x) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfergenericfunction.html#apply

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorTransferGenericFunction::apply(float x) const
    return self.uglySide.call(
        'ritual_ZNK29QColorTransferGenericFunction5applyEf', x,
    )

  @overload(float)
  def applyInverse(self, x: float) -> float:
    """
    Calls Qt's 'float QColorTransferGenericFunction::applyInverse(float x)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfergenericfunction.html#applyInverse

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorTransferGenericFunction::applyInverse(float x) const
    return self.uglySide.call(
        'ritual_ZNK29QColorTransferGenericFunction12applyInverseEf', x,
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
  def __eq__(self, o: QColorTransferGenericFunction) -> bool:
    """
    Calls Qt's 'bool QColorTransferGenericFunction::operator==(const
    QColorTransferGenericFunction &o) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfergenericfunction.html#operator==

    Parameters
    ----------

    o : QColorTransferGenericFunction
      Passed on as a value: Qt reads the C++ QColorTransferGenericFunction,
      which stays Python's own.
    """
    #  bool QColorTransferGenericFunction::operator==(const
    #      QColorTransferGenericFunction &o) const
    return self.uglySide.call(
        'ritual_ZNK29QColorTransferGenericFunctioneqERKS_', self._valueOf(o),
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
  def __ne__(self, o: QColorTransferGenericFunction) -> bool:
    """
    Calls Qt's 'bool QColorTransferGenericFunction::operator!=(const
    QColorTransferGenericFunction &o) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransfergenericfunction.html#operator!=

    Parameters
    ----------

    o : QColorTransferGenericFunction
      Passed on as a value: Qt reads the C++ QColorTransferGenericFunction,
      which stays Python's own.
    """
    #  bool QColorTransferGenericFunction::operator!=(const
    #      QColorTransferGenericFunction &o) const
    return self.uglySide.call(
        'ritual_ZNK29QColorTransferGenericFunctionneERKS_', self._valueOf(o),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QColorTransferGenericFunction::QColorTransferGenericFunction(
    ConverterPtr toLinear, ConverterPtr fromLinear)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QColorTransferGenericFunction.__init__' has no cute function yet. "
        "Qt's "
        "'QColorTransferGenericFunction::QColorTransferGenericFunction(Conve"
        "rterPtr toLinear, ConverterPtr fromLinear)': takes a type Python "
        "has no way to hand over yet.")

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
