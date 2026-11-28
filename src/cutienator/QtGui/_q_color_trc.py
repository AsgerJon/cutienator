"""
QColorTrc binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qcolortrc_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QColorTrc to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QColorTransferFunction, QColorTransferGenericFunction
  from . import QColorTransferTable
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColorTransferFunction = WAIT['QColorTransferFunction']
  QColorTransferGenericFunction = WAIT['QColorTransferGenericFunction']
  QColorTransferTable = WAIT['QColorTransferTable']


class QColorTrc(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorTrc: a plain Python object standing in front of
  one C++ QColorTrc.

  C++ hands a QColorTrc around as a copy, so every C++ QColorTrc behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QColorTrc that has a ritual and that Python can call
  so far, 12 names in all: 'isIdentity', 'isValid', 'apply', 'applyExtended',
  'applyInverse', 'applyInverseExtended', 'table', 'fun', 'hdr', 'type',
  '__eq__', '__ne__'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorTrc::QColorTrc(QColorTransferFunction &&fun)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QColorTrc::QColorTrc(QColorTransferTable &&table)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QColorTrc::QColorTrc(QColorTransferGenericFunction &&hdr)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QColorTrc::~QColorTrc()': the destructor: Python removes its C++
    QColorTrc by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QColorTrc is created at the first use, not by 'QColorTrc(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QColorTrc back gives a copy the ritual made for
    Python, in a new cute QColorTrc.
  """

  #  The enums Qt writes inside QColorTrc, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QColorTrc::Type' of Qt, with the 4 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Uninitialized = Kee[int](0)
    ParameterizedFunction = Kee[int](1)
    GenericFunction = Kee[int](2)
    Table = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorTrc'

  #  Qt's '~QColorTrc()'. Naming it makes this a value class: Python owns
  #  every C++ QColorTrc behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QColorTrcD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isIdentity(self) -> bool:
    """
    Calls Qt's 'bool QColorTrc::isIdentity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#isIdentity
    """
    #  bool QColorTrc::isIdentity() const
    return self.uglySide.call('ritual_ZNK9QColorTrc10isIdentityEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QColorTrc::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#isValid
    """
    #  bool QColorTrc::isValid() const
    return self.uglySide.call('ritual_ZNK9QColorTrc7isValidEv')

  @overload(float)
  def apply(self, x: float) -> float:
    """
    Calls Qt's 'float QColorTrc::apply(float x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#apply

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorTrc::apply(float x) const
    return self.uglySide.call('ritual_ZNK9QColorTrc5applyEf', x)

  @overload(float)
  def applyExtended(self, x: float) -> float:
    """
    Calls Qt's 'float QColorTrc::applyExtended(float x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#applyExtended

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorTrc::applyExtended(float x) const
    return self.uglySide.call('ritual_ZNK9QColorTrc13applyExtendedEf', x)

  @overload(float)
  def applyInverse(self, x: float) -> float:
    """
    Calls Qt's 'float QColorTrc::applyInverse(float x) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#applyInverse

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorTrc::applyInverse(float x) const
    return self.uglySide.call('ritual_ZNK9QColorTrc12applyInverseEf', x)

  @overload(float)
  def applyInverseExtended(self, x: float) -> float:
    """
    Calls Qt's 'float QColorTrc::applyInverseExtended(float x) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolortrc.html#applyInverseExtended

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  float QColorTrc::applyInverseExtended(float x) const
    return self.uglySide.call(
        'ritual_ZNK9QColorTrc20applyInverseExtendedEf', x,
    )

  def table(self) -> QColorTransferTable:
    """
    Calls Qt's 'const QColorTransferTable &QColorTrc::table() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#table

    Returns
    -------

    QColorTransferTable
      A new cute QColorTransferTable around the copy Qt gave back. Python
      owns it.
    """
    #  const QColorTransferTable &QColorTrc::table() const
    address = self.uglySide.call('ritual_ZNK9QColorTrc5tableEv')
    from . import QColorTransferTable
    return QColorTransferTable._cuteOwning(address)

  def fun(self) -> QColorTransferFunction:
    """
    Calls Qt's 'const QColorTransferFunction &QColorTrc::fun() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#fun

    Returns
    -------

    QColorTransferFunction
      A new cute QColorTransferFunction around the copy Qt gave back. Python
      owns it.
    """
    #  const QColorTransferFunction &QColorTrc::fun() const
    address = self.uglySide.call('ritual_ZNK9QColorTrc3funEv')
    from . import QColorTransferFunction
    return QColorTransferFunction._cuteOwning(address)

  def hdr(self) -> QColorTransferGenericFunction:
    """
    Calls Qt's 'const QColorTransferGenericFunction &QColorTrc::hdr() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#hdr

    Returns
    -------

    QColorTransferGenericFunction
      A new cute QColorTransferGenericFunction around the copy Qt gave back.
      Python owns it.
    """
    #  const QColorTransferGenericFunction &QColorTrc::hdr() const
    address = self.uglySide.call('ritual_ZNK9QColorTrc3hdrEv')
    from . import QColorTransferGenericFunction
    return QColorTransferGenericFunction._cuteOwning(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type QColorTrc::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QColorTrc::type() const
    return QColorTrc.Type(self.uglySide.call('ritual_ZNK9QColorTrc4typeEv'))

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
  def __eq__(self, rhs: QColorTrc) -> bool:
    """
    Calls Qt's 'bool operator==(const QColorTrc &lhs, const QColorTrc &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#operator==

    Parameters
    ----------

    rhs : QColorTrc
      Passed on as a value: Qt reads the C++ QColorTrc, which stays Python's
      own.
    """
    #  bool operator==(const QColorTrc &lhs, const QColorTrc &rhs)
    return Rituals.call(
        'ritual_ZeqRK9QColorTrcS1_',
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
  def __ne__(self, rhs: QColorTrc) -> bool:
    """
    Calls Qt's 'bool operator!=(const QColorTrc &lhs, const QColorTrc &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#operator!=

    Parameters
    ----------

    rhs : QColorTrc
      Passed on as a value: Qt reads the C++ QColorTrc, which stays Python's
      own.
    """
    #  bool operator!=(const QColorTrc &lhs, const QColorTrc &rhs)
    return Rituals.call(
        'ritual_ZneRK9QColorTrcS1_',
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
    Notes what was given, for Qt's 'QColorTrc::QColorTrc()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#QColorTrc
    """
    #  QColorTrc::QColorTrc()
    self._noteCreation(QColorTrc, lambda: Rituals.call(
        'ritual_ZN9QColorTrcC1Ev',
    ))

  @overload(QColorTransferFunction)
  def __init__(self, fun: QColorTransferFunction) -> None:
    """
    Notes what was given, for Qt's 'QColorTrc::QColorTrc(const
    QColorTransferFunction &fun)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#QColorTrc

    Parameters
    ----------

    fun : QColorTransferFunction
      Passed on as a value: Qt reads the C++ QColorTransferFunction, which
      stays Python's own.
    """
    #  QColorTrc::QColorTrc(const QColorTransferFunction &fun)
    self._noteCreation(QColorTrc, lambda: Rituals.call(
        'ritual_ZN9QColorTrcC1ERK22QColorTransferFunction',
        self._valueOf(fun),
    ))

  @overload(QColorTransferTable)
  def __init__(self, table: QColorTransferTable) -> None:
    """
    Notes what was given, for Qt's 'QColorTrc::QColorTrc(const
    QColorTransferTable &table)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#QColorTrc

    Parameters
    ----------

    table : QColorTransferTable
      Passed on as a value: Qt reads the C++ QColorTransferTable, which stays
      Python's own.
    """
    #  QColorTrc::QColorTrc(const QColorTransferTable &table)
    self._noteCreation(QColorTrc, lambda: Rituals.call(
        'ritual_ZN9QColorTrcC1ERK19QColorTransferTable',
        self._valueOf(table),
    ))

  @overload(QColorTransferGenericFunction)
  def __init__(self, hdr: QColorTransferGenericFunction) -> None:
    """
    Notes what was given, for Qt's 'QColorTrc::QColorTrc(const
    QColorTransferGenericFunction &hdr)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolortrc.html#QColorTrc

    Parameters
    ----------

    hdr : QColorTransferGenericFunction
      Passed on as a value: Qt reads the C++ QColorTransferGenericFunction,
      which stays Python's own.
    """
    #  QColorTrc::QColorTrc(const QColorTransferGenericFunction &hdr)
    self._noteCreation(QColorTrc, lambda: Rituals.call(
        'ritual_ZN9QColorTrcC1ERK29QColorTransferGenericFunction',
        self._valueOf(hdr),
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
