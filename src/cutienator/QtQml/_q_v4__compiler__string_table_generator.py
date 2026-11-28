"""
QV4::Compiler::StringTableGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compiler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Compiler::StringTableGenerator to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class StringTableGenerator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Compiler::StringTableGenerator: a plain Python
  object standing in front of one C++ QV4::Compiler::StringTableGenerator.

  C++ hands a QV4::Compiler::StringTableGenerator around as a copy, so every
  C++ QV4::Compiler::StringTableGenerator behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QV4::Compiler::StringTableGenerator that has a
  ritual and that Python can call so far, 11 names in all: 'registerString',
  'getStringId', 'hasStringId', 'stringForIndex', 'stringCount',
  'sizeOfTableAndData', 'freeze', 'clear', 'initializeFromBackingUnit',
  'serialize', 'allStrings'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Compiler::StringTableGenerator::~StringTableGenerator()': the
    destructor: Python removes its C++ QV4::Compiler::StringTableGenerator by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::Compiler::StringTableGenerator is created at the first use,
    not by 'QV4::Compiler::StringTableGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Compiler::StringTableGenerator back gives a copy
    the ritual made for Python, in a new cute
    QV4::Compiler::StringTableGenerator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Compiler::StringTableGenerator'

  #  Qt's '~QV4::Compiler::StringTableGenerator()'. Naming it makes this a
  #  value class: Python owns every C++ QV4::Compiler::StringTableGenerator
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV48Compiler20StringTableGeneratorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def getStringId(self, string: str) -> int:
    """
    Calls Qt's 'int QV4::Compiler::StringTableGenerator::getStringId(const
    QString &string) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html#getStringId

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QV4::Compiler::StringTableGenerator::getStringId(const QString
    #      &string) const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler20StringTableGenerator11getStringIdERK7QStr'
        'ing',
        string,
    )

  @overload(str)
  def hasStringId(self, string: str) -> bool:
    """
    Calls Qt's 'bool QV4::Compiler::StringTableGenerator::hasStringId(const
    QString &string) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html#hasStringId

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QV4::Compiler::StringTableGenerator::hasStringId(const QString
    #      &string) const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler20StringTableGenerator11hasStringIdERK7QStr'
        'ing',
        string,
    )

  @overload(int)
  def stringForIndex(self, index: int) -> str:
    """
    Calls Qt's 'QString
    QV4::Compiler::StringTableGenerator::stringForIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Compiler::StringTableGenerator::stringForIndex(int index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler20StringTableGenerator14stringForIndexEi',
        index,
    )

  def stringCount(self) -> int:
    """
    Calls Qt's 'uint QV4::Compiler::StringTableGenerator::stringCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html#stringCount
    """
    #  uint QV4::Compiler::StringTableGenerator::stringCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler20StringTableGenerator11stringCountEv',
    )

  def sizeOfTableAndData(self) -> int:
    """
    Calls Qt's 'uint
    QV4::Compiler::StringTableGenerator::sizeOfTableAndData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html
    """
    #  uint QV4::Compiler::StringTableGenerator::sizeOfTableAndData() const
    return self.uglySide.call(
        'ritual_ZNK3QV48Compiler20StringTableGenerator18sizeOfTableAndDataE'
        'v',
    )

  def allStrings(self) -> QStringList:
    """
    Calls Qt's 'QStringList QV4::Compiler::StringTableGenerator::allStrings()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html#allStrings

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QV4::Compiler::StringTableGenerator::allStrings() const
    address = self.uglySide.call(
        'ritual_ZNK3QV48Compiler20StringTableGenerator10allStringsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's
    'QV4::Compiler::StringTableGenerator::StringTableGenerator()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html
    """
    #  QV4::Compiler::StringTableGenerator::StringTableGenerator()
    self._noteCreation(StringTableGenerator, lambda: Rituals.call(
        'ritual_ZN3QV48Compiler20StringTableGeneratorC1Ev',
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

  @overload(str)
  def registerString(self, str: str) -> int:
    """
    Calls Qt's 'int QV4::Compiler::StringTableGenerator::registerString(const
    QString &str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QV4::Compiler::StringTableGenerator::registerString(const QString
    #      &str)
    return self.uglySide.call(
        'ritual_ZN3QV48Compiler20StringTableGenerator14registerStringERK7QS'
        'tring',
        str,
    )

  def freeze(self) -> None:
    """
    Calls Qt's 'void QV4::Compiler::StringTableGenerator::freeze()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html#freeze
    """
    #  void QV4::Compiler::StringTableGenerator::freeze()
    self.uglySide.call(
        'ritual_ZN3QV48Compiler20StringTableGenerator6freezeEv',
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QV4::Compiler::StringTableGenerator::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html#clear
    """
    #  void QV4::Compiler::StringTableGenerator::clear()
    self.uglySide.call(
        'ritual_ZN3QV48Compiler20StringTableGenerator5clearEv',
    )

  @overload(WAIT['QV4.CompiledData.Unit'])
  @overload(NoneType)
  def initializeFromBackingUnit(
      self,
      unit: Optional[QV4.CompiledData.Unit],
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::StringTableGenerator::initializeFromBackingUnit(const
    CompiledData::Unit *unit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html

    Parameters
    ----------

    unit : Optional[QV4.CompiledData.Unit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::StringTableGenerator::initializeFromBackingUnit(
    #      const CompiledData::Unit *unit)
    self.uglySide.call(
        'ritual_ZN3QV48Compiler20StringTableGenerator25initializeFromBackin'
        'gUnitEPKNS_12CompiledData4UnitE',
        self._addressOf(unit),
    )

  @overload(WAIT['QV4.CompiledData.Unit'])
  @overload(NoneType)
  def serialize(self, unit: Optional[QV4.CompiledData.Unit]) -> None:
    """
    Calls Qt's 'void
    QV4::Compiler::StringTableGenerator::serialize(CompiledData::Unit
    *unit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compiler-stringtablegenerator.html#serialize

    Parameters
    ----------

    unit : Optional[QV4.CompiledData.Unit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Compiler::StringTableGenerator::serialize(CompiledData::Unit
    #      *unit)
    self.uglySide.call(
        'ritual_ZN3QV48Compiler20StringTableGenerator9serializeEPNS_12Compi'
        'ledData4UnitE',
        self._addressOf(unit),
    )
