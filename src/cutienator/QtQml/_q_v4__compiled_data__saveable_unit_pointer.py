"""
QV4::CompiledData::SaveableUnitPointer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::SaveableUnitPointer to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SaveableUnitPointer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::SaveableUnitPointer: a plain
  Python object standing in front of one C++
  QV4::CompiledData::SaveableUnitPointer.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::SaveableUnitPointer that has a
  ritual and that Python can call so far, 2 names in all: 'writeDataToFile',
  'size'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::SaveableUnitPointer::~SaveableUnitPointer()':
    the destructor: Python never removes a C++
    QV4::CompiledData::SaveableUnitPointer.
  - Qt's 'quint32_le &QV4::CompiledData::SaveableUnitPointer::mutableFlags()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  6 of the 11 functions Qt declares: 4 forbidden; 2 a template.

  What to expect
  --------------

  - The C++ QV4::CompiledData::SaveableUnitPointer is created at the first
    use, not by 'QV4::CompiledData::SaveableUnitPointer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::CompiledData::SaveableUnitPointer.
  - Each name of Qt's QV4::CompiledData::SaveableUnitPointer that has no cute
    function yet, 'data', 'mutableFlags', 'saveToDisk', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, str, int, QString)
  @overload(str, str, int, NoneType)
  @overload(str, NoneType, int, QString)
  @overload(str, NoneType, int, NoneType)
  def writeDataToFile(
      outputFileName: str,
      data: Optional[str],
      size: int,
      errorString: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool
    QV4::CompiledData::SaveableUnitPointer::writeDataToFile(const QString
    &outputFileName, const char *data, quint32 size, QString *errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-saveableunitpointer.html

    Parameters
    ----------

    outputFileName : str
      Passed on as it is: a QString is made of it for the call.

    data : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    size : int
      Passed on as it is.

    errorString : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::CompiledData::SaveableUnitPointer::writeDataToFile(const
    #      QString &outputFileName, const char *data, quint32 size, QString
    #      *errorString)
    return Rituals.call(
        'ritual_ZN3QV412CompiledData19SaveableUnitPointer15writeDataToFileE'
        'RK7QStringPKcjPS2_',
        outputFileName, CuteMixin._bytesOf(data), size,
        CuteMixin._addressOf(errorString),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::SaveableUnitPointer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::SaveableUnitPointer::size()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-saveableunitpointer.html#size
    """
    #  quint32 QV4::CompiledData::SaveableUnitPointer::size() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData19SaveableUnitPointer4sizeEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.CompiledData.Unit'], int)
  @overload(NoneType, int)
  def __init__(
      self,
      unit: Optional[QV4.CompiledData.Unit],
      temporaryFlags: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::CompiledData::SaveableUnitPointer::SaveableUnitPointer(const Unit
    *unit, quint32 temporaryFlags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-saveableunitpointer.html

    Parameters
    ----------

    unit : Optional[QV4.CompiledData.Unit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    temporaryFlags : int
      Passed on as it is.
    """
    #  QV4::CompiledData::SaveableUnitPointer::SaveableUnitPointer(const Unit
    #      *unit, quint32 temporaryFlags)
    self._noteCreation(SaveableUnitPointer, lambda: Rituals.call(
        'ritual_ZN3QV412CompiledData19SaveableUnitPointerC1EPKNS0_4UnitEj',
        self._addressOf(unit), temporaryFlags,
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
  def data(*__, **_) -> Never:
    """
    Qt's 'QV4::CompiledData::SaveableUnitPointer::data': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.SaveableUnitPointer.data' has no cute function "
        "yet. Qt's 'QV4::CompiledData::SaveableUnitPointer::data': a "
        "template: a pattern and no single function.")

  @staticmethod
  def mutableFlags(*__, **_) -> Never:
    """
    Qt's 'quint32_le &QV4::CompiledData::SaveableUnitPointer::mutableFlags()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.SaveableUnitPointer.mutableFlags' has no cute "
        "function yet. Qt's 'quint32_le "
        "&QV4::CompiledData::SaveableUnitPointer::mutableFlags() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def saveToDisk(*__, **_) -> Never:
    """
    Qt's 'QV4::CompiledData::SaveableUnitPointer::saveToDisk': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.SaveableUnitPointer.saveToDisk' has no cute "
        "function yet. Qt's "
        "'QV4::CompiledData::SaveableUnitPointer::saveToDisk': a template: "
        "a pattern and no single function.")
