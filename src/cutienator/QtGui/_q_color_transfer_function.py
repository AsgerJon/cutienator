"""
QColorTransferFunction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolortransferfunction_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QColorTransferFunction to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals


class QColorTransferFunction(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorTransferFunction: a plain Python object
  standing in front of one C++ QColorTransferFunction.

  C++ hands a QColorTransferFunction around as a copy, so every C++
  QColorTransferFunction behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorTransferFunction that has a ritual and that
  Python can call so far, 14 names in all: 'isGamma', 'isIdentity', 'isSRgb',
  'apply', 'inverted', 'fromGamma', 'fromSRgb', 'fromProPhotoRgb',
  'fromBt2020', 'matches', '__eq__', '__ne__', 'paramCompare', 'updateHints'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorTransferFunction::~QColorTransferFunction()': the destructor:
    Python removes its C++ QColorTransferFunction by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QColorTransferFunction is created at the first use, not by
    'QColorTransferFunction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorTransferFunction back gives a copy the ritual
    made for Python, in a new cute QColorTransferFunction.
  """

  #  The enums Qt writes inside QColorTransferFunction, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Hint(CuteFlags, number='unsigned int', scoped=True):
    """
    The flags enum 'QColorTransferFunction::Hint' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QColorTransferFunction::Hints'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    NoHint = 0x0
    Calculated = 0x1
    IsGamma = 0x2
    IsIdentity = 0x4
    IsSRgb = 0x8

  Hints = Hint

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(float)
  def fromGamma(gamma: float) -> QColorTransferFunction:
    """
    Calls Qt's 'QColorTransferFunction
    QColorTransferFunction::fromGamma(float gamma)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#fromGamma

    Parameters
    ----------

    gamma : float
      Passed on as it is.

    Returns
    -------

    QColorTransferFunction
      A new cute QColorTransferFunction around the copy Qt gave back. Python
      owns it.
    """
    #  QColorTransferFunction QColorTransferFunction::fromGamma(float gamma)
    address = Rituals.call(
        'ritual_ZN22QColorTransferFunction9fromGammaEf', gamma,
    )
    return QColorTransferFunction._cuteOwning(address)

  @staticmethod
  def fromSRgb() -> QColorTransferFunction:
    """
    Calls Qt's 'QColorTransferFunction QColorTransferFunction::fromSRgb()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#fromSRgb

    Returns
    -------

    QColorTransferFunction
      A new cute QColorTransferFunction around the copy Qt gave back. Python
      owns it.
    """
    #  QColorTransferFunction QColorTransferFunction::fromSRgb()
    address = Rituals.call('ritual_ZN22QColorTransferFunction8fromSRgbEv')
    return QColorTransferFunction._cuteOwning(address)

  @staticmethod
  def fromProPhotoRgb() -> QColorTransferFunction:
    """
    Calls Qt's 'QColorTransferFunction
    QColorTransferFunction::fromProPhotoRgb()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#fromProPhotoRgb

    Returns
    -------

    QColorTransferFunction
      A new cute QColorTransferFunction around the copy Qt gave back. Python
      owns it.
    """
    #  QColorTransferFunction QColorTransferFunction::fromProPhotoRgb()
    address = Rituals.call(
        'ritual_ZN22QColorTransferFunction15fromProPhotoRgbEv',
    )
    return QColorTransferFunction._cuteOwning(address)

  @staticmethod
  def fromBt2020() -> QColorTransferFunction:
    """
    Calls Qt's 'QColorTransferFunction QColorTransferFunction::fromBt2020()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#fromBt2020

    Returns
    -------

    QColorTransferFunction
      A new cute QColorTransferFunction around the copy Qt gave back. Python
      owns it.
    """
    #  QColorTransferFunction QColorTransferFunction::fromBt2020()
    address = Rituals.call('ritual_ZN22QColorTransferFunction10fromBt2020Ev')
    return QColorTransferFunction._cuteOwning(address)

  @staticmethod
  @overload(float, float)
  def paramCompare(p1: float, p2: float) -> bool:
    """
    Calls Qt's 'bool QColorTransferFunction::paramCompare(float p1, float
    p2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#paramCompare

    Parameters
    ----------

    p1 : float
      Passed on as it is.

    p2 : float
      Passed on as it is.
    """
    #  bool QColorTransferFunction::paramCompare(float p1, float p2)
    return Rituals.call(
        'ritual_ZN22QColorTransferFunction12paramCompareEff', p1, p2,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorTransferFunction'

  #  Qt's '~QColorTransferFunction()'. Naming it makes this a value class:
  #  Python owns every C++ QColorTransferFunction behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QColorTransferFunctionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isGamma(self) -> bool:
    """
    Calls Qt's 'bool QColorTransferFunction::isGamma() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#isGamma
    """
    #  bool QColorTransferFunction::isGamma() const
    return self.uglySide.call('ritual_ZNK22QColorTransferFunction7isGammaEv')

  def isIdentity(self) -> bool:
    """
    Calls Qt's 'bool QColorTransferFunction::isIdentity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#isIdentity
    """
    #  bool QColorTransferFunction::isIdentity() const
    return self.uglySide.call(
        'ritual_ZNK22QColorTransferFunction10isIdentityEv',
    )

  def isSRgb(self) -> bool:
    """
    Calls Qt's 'bool QColorTransferFunction::isSRgb() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransferfunction.html#isSRgb
    """
    #  bool QColorTransferFunction::isSRgb() const
    return self.uglySide.call('ritual_ZNK22QColorTransferFunction6isSRgbEv')

  @overload(float)
  def apply(self, x: float) -> float:
    """
    Calls Qt's 'float QColorTransferFunction::apply(float x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortransferfunction.html#apply

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorTransferFunction::apply(float x) const
    return self.uglySide.call(
        'ritual_ZNK22QColorTransferFunction5applyEf', x,
    )

  def inverted(self) -> QColorTransferFunction:
    """
    Calls Qt's 'QColorTransferFunction QColorTransferFunction::inverted()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#inverted

    Returns
    -------

    QColorTransferFunction
      A new cute QColorTransferFunction around the copy Qt gave back. Python
      owns it.
    """
    #  QColorTransferFunction QColorTransferFunction::inverted() const
    address = self.uglySide.call(
        'ritual_ZNK22QColorTransferFunction8invertedEv',
    )
    return QColorTransferFunction._cuteOwning(address)

  @overload(THIS)
  def matches(self, o: QColorTransferFunction) -> bool:
    """
    Calls Qt's 'bool QColorTransferFunction::matches(const
    QColorTransferFunction &o) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#matches

    Parameters
    ----------

    o : QColorTransferFunction
      Passed on as a value: Qt reads the C++ QColorTransferFunction, which
      stays Python's own.
    """
    #  bool QColorTransferFunction::matches(const QColorTransferFunction &o)
    #      const
    return self.uglySide.call(
        'ritual_ZNK22QColorTransferFunction7matchesERKS_', self._valueOf(o),
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
  def __eq__(self, f2: QColorTransferFunction) -> bool:
    """
    Calls Qt's 'bool operator==(const QColorTransferFunction &f1, const
    QColorTransferFunction &f2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#operator==

    Parameters
    ----------

    f2 : QColorTransferFunction
      Passed on as a value: Qt reads the C++ QColorTransferFunction, which
      stays Python's own.
    """
    #  bool operator==(const QColorTransferFunction &f1, const
    #      QColorTransferFunction &f2)
    return Rituals.call(
        'ritual_ZeqRK22QColorTransferFunctionS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(f2),
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
  def __ne__(self, f2: QColorTransferFunction) -> bool:
    """
    Calls Qt's 'bool operator!=(const QColorTransferFunction &f1, const
    QColorTransferFunction &f2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#operator!=

    Parameters
    ----------

    f2 : QColorTransferFunction
      Passed on as a value: Qt reads the C++ QColorTransferFunction, which
      stays Python's own.
    """
    #  bool operator!=(const QColorTransferFunction &f1, const
    #      QColorTransferFunction &f2)
    return Rituals.call(
        'ritual_ZneRK22QColorTransferFunctionS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(f2),
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
    Notes what was given, for Qt's
    'QColorTransferFunction::QColorTransferFunction()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#QColorTransferFunction
    """
    #  QColorTransferFunction::QColorTransferFunction()
    self._noteCreation(QColorTransferFunction, lambda: Rituals.call(
        'ritual_ZN22QColorTransferFunctionC1Ev',
    ))

  @overload(float, float, float, float, float, float, float)
  def __init__(
      self,
      a: float,
      b: float,
      c: float,
      d: float,
      e: float,
      f: float,
      g: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QColorTransferFunction::QColorTransferFunction(float a, float b, float
    c, float d, float e, float f, float g)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#QColorTransferFunction

    Parameters
    ----------

    a : float
      Passed on as it is.

    b : float
      Passed on as it is.

    c : float
      Passed on as it is.

    d : float
      Passed on as it is.

    e : float
      Passed on as it is.

    f : float
      Passed on as it is.

    g : float
      Passed on as it is.
    """
    #  QColorTransferFunction::QColorTransferFunction(float a, float b, float
    #      c, float d, float e, float f, float g)
    self._noteCreation(QColorTransferFunction, lambda: Rituals.call(
        'ritual_ZN22QColorTransferFunctionC1Efffffff', a, b, c, d, e, f, g,
    ))

  @overload(float, float, float, float, float, float, float, Hints)
  def __init__(
      self,
      a: float,
      b: float,
      c: float,
      d: float,
      e: float,
      f: float,
      g: float,
      flags: Hints,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QColorTransferFunction::QColorTransferFunction(float a, float b, float
    c, float d, float e, float f, float g, Hints flags)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#QColorTransferFunction

    Parameters
    ----------

    a : float
      Passed on as it is.

    b : float
      Passed on as it is.

    c : float
      Passed on as it is.

    d : float
      Passed on as it is.

    e : float
      Passed on as it is.

    f : float
      Passed on as it is.

    g : float
      Passed on as it is.

    flags : Hints
      Passed on as its number.
    """
    #  QColorTransferFunction::QColorTransferFunction(float a, float b, float
    #      c, float d, float e, float f, float g, Hints flags)
    self._noteCreation(QColorTransferFunction, lambda: Rituals.call(
        'ritual_ZN22QColorTransferFunctionC1Efffffff6QFlagsINS_4HintEE',
        a, b, c, d, e, f, g, flags.value,
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

  def updateHints(self) -> None:
    """
    Calls Qt's 'void QColorTransferFunction::updateHints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortransferfunction.html#updateHints
    """
    #  void QColorTransferFunction::updateHints() const
    self.uglySide.call('ritual_ZNK22QColorTransferFunction11updateHintsEv')
