"""
QQmlJS::SourceLocation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlJS::SourceLocation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class SourceLocation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::SourceLocation: a plain Python object
  standing in front of one C++ QQmlJS::SourceLocation.

  C++ hands a QQmlJS::SourceLocation around as a copy, so every C++
  QQmlJS::SourceLocation behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJS::SourceLocation that has a ritual and that
  Python can call so far, 10 names in all: 'qSizeTypeCanHoldQuint32',
  'fromQSizeType', 'offsetFrom', 'isValid', 'begin', 'end',
  'startZeroLengthLocation', 'endZeroLengthLocation', '__eq__', '__ne__'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::pair<quint32, quint32>
    QQmlJS::SourceLocation::rowAndColumnFrom(QStringView text, quint32
    offset, const SourceLocation &startHint)': gives a type Python has no way
    to take yet.
  - Qt's 'QQmlJS::SourceLocation::~SourceLocation()': the destructor: Python
    removes its C++ QQmlJS::SourceLocation by it, and has no other use for
    it.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlJS::SourceLocation is created at the first use, not by
    'QQmlJS::SourceLocation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJS::SourceLocation back gives a copy the ritual
    made for Python, in a new cute QQmlJS::SourceLocation.
  - Each name of Qt's QQmlJS::SourceLocation that has no cute function yet,
    'findLocationIf', 'rowAndColumnFrom', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qSizeTypeCanHoldQuint32() -> bool:
    """
    Calls Qt's 'bool QQmlJS::SourceLocation::qSizeTypeCanHoldQuint32()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#qSizeTypeCanHoldQuint32
    """
    #  bool QQmlJS::SourceLocation::qSizeTypeCanHoldQuint32()
    return Rituals.call(
        'ritual_ZN6QQmlJS14SourceLocation23qSizeTypeCanHoldQuint32Ev',
    )

  @staticmethod
  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  @overload(int, int, int, int)
  def fromQSizeType(
      offset: int,
      length: int = 0,
      line: int = 0,
      column: int = 0,
  ) -> SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::SourceLocation::fromQSizeType(qsizetype offset, qsizetype length,
    qsizetype line, qsizetype column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#fromQSizeType

    Parameters
    ----------

    offset : int
      Passed on as it is.

    length : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    line : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::SourceLocation::fromQSizeType(qsizetype offset,
    #      qsizetype length, qsizetype line, qsizetype column)
    address = Rituals.call(
        'ritual_ZN6QQmlJS14SourceLocation13fromQSizeTypeExxxx',
        offset, length, line, column,
    )
    return SourceLocation._cuteOwning(address)

  @staticmethod
  @overload(str, int, int, THIS)
  def offsetFrom(
      text: str,
      line: int,
      column: int,
      startHint: SourceLocation,
  ) -> int:
    """
    Calls Qt's 'quint32 QQmlJS::SourceLocation::offsetFrom(QStringView text,
    quint32 line, quint32 column, const SourceLocation &startHint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#offsetFrom

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.

    startHint : SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  quint32 QQmlJS::SourceLocation::offsetFrom(QStringView text, quint32
    #      line, quint32 column, const SourceLocation &startHint)
    return Rituals.call(
        'ritual_ZN6QQmlJS14SourceLocation10offsetFromE11QStringViewjjRKS0_',
        text, line, column, CuteMixin._valueOf(startHint),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::SourceLocation'

  #  Qt's '~QQmlJS::SourceLocation()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlJS::SourceLocation behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlJS14SourceLocationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::SourceLocation::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#isValid
    """
    #  bool QQmlJS::SourceLocation::isValid() const
    return self.uglySide.call('ritual_ZNK6QQmlJS14SourceLocation7isValidEv')

  def begin(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlJS::SourceLocation::begin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#begin
    """
    #  qsizetype QQmlJS::SourceLocation::begin() const
    return self.uglySide.call('ritual_ZNK6QQmlJS14SourceLocation5beginEv')

  def end(self) -> int:
    """
    Calls Qt's 'qsizetype QQmlJS::SourceLocation::end() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#end
    """
    #  qsizetype QQmlJS::SourceLocation::end() const
    return self.uglySide.call('ritual_ZNK6QQmlJS14SourceLocation3endEv')

  def startZeroLengthLocation(self) -> SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::SourceLocation::startZeroLengthLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#startZeroLengthLocation

    Returns
    -------

    SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::SourceLocation::startZeroLengthLocation() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS14SourceLocation23startZeroLengthLocationEv',
    )
    return SourceLocation._cuteOwning(address)

  @overload(str)
  def endZeroLengthLocation(self, text: str) -> SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::SourceLocation::endZeroLengthLocation(QStringView text) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#endZeroLengthLocation

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation
    #      QQmlJS::SourceLocation::endZeroLengthLocation(QStringView text)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS14SourceLocation21endZeroLengthLocationE11QString'
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
  def __eq__(self, b: SourceLocation) -> bool:
    """
    Calls Qt's 'bool operator==(const SourceLocation &a, const SourceLocation
    &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#operator==

    Parameters
    ----------

    b : SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  bool operator==(const SourceLocation &a, const SourceLocation &b)
    return Rituals.call(
        'ritual_ZN6QQmlJSeqERKNS_14SourceLocationES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: SourceLocation) -> bool:
    """
    Calls Qt's 'bool operator!=(const SourceLocation &a, const SourceLocation
    &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#operator!=

    Parameters
    ----------

    b : SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  bool operator!=(const SourceLocation &a, const SourceLocation &b)
    return Rituals.call(
        'ritual_ZN6QQmlJSneERKNS_14SourceLocationES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
    'QQmlJS::SourceLocation::SourceLocation(quint32 offset, quint32 length,
    quint32 line, quint32 column)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-sourcelocation.html#SourceLocation

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
    #  QQmlJS::SourceLocation::SourceLocation(quint32 offset, quint32 length,
    #      quint32 line, quint32 column)
    self._noteCreation(SourceLocation, lambda: Rituals.call(
        'ritual_ZN6QQmlJS14SourceLocationC1Ejjjj',
        offset, length, line, column,
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
  def findLocationIf(*__, **_) -> Never:
    """
    Qt's 'QQmlJS::SourceLocation::findLocationIf': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QQmlJS.SourceLocation.findLocationIf' has no cute function yet. "
        "Qt's 'QQmlJS::SourceLocation::findLocationIf': a template: a "
        "pattern and no single function.")

  @staticmethod
  def rowAndColumnFrom(*__, **_) -> Never:
    """
    Qt's 'std::pair<quint32, quint32>
    QQmlJS::SourceLocation::rowAndColumnFrom(QStringView text, quint32
    offset, const SourceLocation &startHint)': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQmlJS.SourceLocation.rowAndColumnFrom' has no cute function yet. "
        "Qt's 'std::pair<quint32, quint32> "
        "QQmlJS::SourceLocation::rowAndColumnFrom(QStringView text, quint32 "
        "offset, const SourceLocation &startHint)': gives a type Python has "
        "no way to take yet.")
