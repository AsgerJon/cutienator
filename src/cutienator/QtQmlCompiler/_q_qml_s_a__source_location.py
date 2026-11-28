"""
QQmlSA::SourceLocation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/qqmlsasourcelocation.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class SourceLocation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::SourceLocation: a plain Python object
  standing in front of one C++ QQmlSA::SourceLocation.

  C++ hands a QQmlSA::SourceLocation around as a copy, so every C++
  QQmlSA::SourceLocation behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::SourceLocation that has a ritual and that
  Python can call so far, 13 names in all: 'isValid', 'begin', 'end',
  'offset', 'length', 'startLine', 'startColumn', 'startZeroLengthLocation',
  'endZeroLengthLocation', '__eq__', '__ne__', 'documentOrigin', 'qHashImpl'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlSA::SourceLocation::SourceLocation(SourceLocation &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'SourceLocation &QQmlSA::SourceLocation::operator=(const
    SourceLocation &a0)': assignment: Python binds a name and has no operator
    for it.
  - Qt's 'SourceLocation &QQmlSA::SourceLocation::operator=(SourceLocation
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QQmlSA::SourceLocation::~SourceLocation()': the destructor: Python
    removes its C++ QQmlSA::SourceLocation by it, and has no other use for
    it.
  - Qt's 'bool QQmlSA::SourceLocation::operatorEqualsImpl(const
    SourceLocation &a0, const SourceLocation &a1)': an operator Python has no
    name for.

  What to expect
  --------------

  - The C++ QQmlSA::SourceLocation is created at the first use, not by
    'QQmlSA::SourceLocation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::SourceLocation back gives a copy the ritual
    made for Python, in a new cute QQmlSA::SourceLocation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def documentOrigin() -> SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlSA::SourceLocation::documentOrigin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#documentOrigin

    Returns
    -------

    SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlSA::SourceLocation::documentOrigin()
    address = Rituals.call(
        'ritual_ZN6QQmlSA14SourceLocation14documentOriginEv',
    )
    return SourceLocation._cuteOwning(address)

  @staticmethod
  @overload(THIS, int)
  def qHashImpl(location: SourceLocation, seed: int) -> int:
    """
    Calls Qt's 'qsizetype QQmlSA::SourceLocation::qHashImpl(const
    SourceLocation &location, qsizetype seed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#qHashImpl

    Parameters
    ----------

    location : SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.

    seed : int
      Passed on as it is.
    """
    #  qsizetype QQmlSA::SourceLocation::qHashImpl(const SourceLocation
    #      &location, qsizetype seed)
    return Rituals.call(
        'ritual_ZN6QQmlSA14SourceLocation9qHashImplERKS0_x',
        CuteMixin._valueOf(location), seed,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::SourceLocation'

  #  Qt's '~QQmlSA::SourceLocation()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlSA::SourceLocation behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA14SourceLocationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlSA::SourceLocation::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#isValid
    """
    #  bool QQmlSA::SourceLocation::isValid() const
    return self.uglySide.call('ritual_ZNK6QQmlSA14SourceLocation7isValidEv')

  def begin(self) -> int:
    """
    Calls Qt's 'quint32 QQmlSA::SourceLocation::begin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#begin
    """
    #  quint32 QQmlSA::SourceLocation::begin() const
    return self.uglySide.call('ritual_ZNK6QQmlSA14SourceLocation5beginEv')

  def end(self) -> int:
    """
    Calls Qt's 'quint32 QQmlSA::SourceLocation::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#end
    """
    #  quint32 QQmlSA::SourceLocation::end() const
    return self.uglySide.call('ritual_ZNK6QQmlSA14SourceLocation3endEv')

  def offset(self) -> int:
    """
    Calls Qt's 'quint32 QQmlSA::SourceLocation::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#offset
    """
    #  quint32 QQmlSA::SourceLocation::offset() const
    return self.uglySide.call('ritual_ZNK6QQmlSA14SourceLocation6offsetEv')

  def length(self) -> int:
    """
    Calls Qt's 'quint32 QQmlSA::SourceLocation::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#length
    """
    #  quint32 QQmlSA::SourceLocation::length() const
    return self.uglySide.call('ritual_ZNK6QQmlSA14SourceLocation6lengthEv')

  def startLine(self) -> int:
    """
    Calls Qt's 'quint32 QQmlSA::SourceLocation::startLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#startLine
    """
    #  quint32 QQmlSA::SourceLocation::startLine() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA14SourceLocation9startLineEv',
    )

  def startColumn(self) -> int:
    """
    Calls Qt's 'quint32 QQmlSA::SourceLocation::startColumn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#startColumn
    """
    #  quint32 QQmlSA::SourceLocation::startColumn() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlSA14SourceLocation11startColumnEv',
    )

  def startZeroLengthLocation(self) -> SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlSA::SourceLocation::startZeroLengthLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#startZeroLengthLocation

    Returns
    -------

    SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlSA::SourceLocation::startZeroLengthLocation() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA14SourceLocation23startZeroLengthLocationEv',
    )
    return SourceLocation._cuteOwning(address)

  @overload(str)
  def endZeroLengthLocation(self, text: str) -> SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlSA::SourceLocation::endZeroLengthLocation(QStringView text) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#endZeroLengthLocation

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    SourceLocation
      A new cute QQmlSA::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation
    #      QQmlSA::SourceLocation::endZeroLengthLocation(QStringView text)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlSA14SourceLocation21endZeroLengthLocationE11QString'
        'View',
        text,
    )
    return SourceLocation._cuteOwning(address)

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
  def __eq__(self, rhs: SourceLocation) -> bool:
    """
    Calls Qt's 'bool operator==(const SourceLocation &lhs, const
    SourceLocation &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#operator==

    Parameters
    ----------

    rhs : SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  bool operator==(const SourceLocation &lhs, const SourceLocation &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAeqERKNS_14SourceLocationES2_',
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
  def __ne__(self, rhs: SourceLocation) -> bool:
    """
    Calls Qt's 'bool operator!=(const SourceLocation &lhs, const
    SourceLocation &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#operator!=

    Parameters
    ----------

    rhs : SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  bool operator!=(const SourceLocation &lhs, const SourceLocation &rhs)
    return Rituals.call(
        'ritual_ZN6QQmlSAneERKNS_14SourceLocationES2_',
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
  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  @overload(int, int, int, int)
  def __init__(
      self,
      offset: int = 0,
      length: int = 0,
      line: int = 0,
      column: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::SourceLocation::SourceLocation(quint32 offset, quint32 length,
    quint32 line, quint32 column)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#SourceLocation

    Parameters
    ----------

    offset : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    length : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    line : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QQmlSA::SourceLocation::SourceLocation(quint32 offset, quint32 length,
    #      quint32 line, quint32 column)
    self._noteCreation(SourceLocation, lambda: Rituals.call(
        'ritual_ZN6QQmlSA14SourceLocationC1Ejjjj',
        offset, length, line, column,
    ))

  @overload(THIS)
  def __init__(self, a0: SourceLocation) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::SourceLocation::SourceLocation(const SourceLocation &a0)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-sourcelocation.html#SourceLocation

    Parameters
    ----------

    a0 : SourceLocation
      Passed on as a value: Qt reads the C++ QQmlSA::SourceLocation, which
      stays Python's own.
    """
    #  QQmlSA::SourceLocation::SourceLocation(const SourceLocation &a0)
    self._noteCreation(SourceLocation, lambda: Rituals.call(
        'ritual_ZN6QQmlSA14SourceLocationC1ERKS0_', self._valueOf(a0),
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
