"""
QMetaStringTable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmetaobjectbuilder_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QMetaStringTable to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QMetaStringTable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaStringTable: a plain Python object standing in
  front of one C++ QMetaStringTable.

  What exists
  -----------

  Every function of Qt's QMetaStringTable that has a ritual and that Python
  can call so far, 3 names in all: 'enter', 'preferredAlignment', 'blobSize'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMetaStringTable::writeBlob(char *out) const': names 'char',
    which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QMetaStringTable is created at the first use, not by
    'QMetaStringTable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMetaStringTable.
  - Each name of Qt's QMetaStringTable that has no cute function yet,
    'writeBlob', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def preferredAlignment() -> int:
    """
    Calls Qt's 'int QMetaStringTable::preferredAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetastringtable.html#preferredAlignment
    """
    #  int QMetaStringTable::preferredAlignment()
    return Rituals.call('ritual_ZN16QMetaStringTable18preferredAlignmentEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaStringTable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def blobSize(self) -> int:
    """
    Calls Qt's 'int QMetaStringTable::blobSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetastringtable.html#blobSize
    """
    #  int QMetaStringTable::blobSize() const
    return self.uglySide.call('ritual_ZNK16QMetaStringTable8blobSizeEv')

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

  @overload(QByteArray)
  def __init__(self, className: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QMetaStringTable::QMetaStringTable(const
    QByteArray &className)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetastringtable.html#QMetaStringTable

    Parameters
    ----------

    className : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QMetaStringTable::QMetaStringTable(const QByteArray &className)
    self._noteCreation(QMetaStringTable, lambda: Rituals.call(
        'ritual_ZN16QMetaStringTableC1ERK10QByteArray',
        self._valueOf(className),
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

  @overload(QByteArray)
  def enter(self, value: QByteArray) -> int:
    """
    Calls Qt's 'int QMetaStringTable::enter(const QByteArray &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmetastringtable.html#enter

    Parameters
    ----------

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QMetaStringTable::enter(const QByteArray &value)
    return self.uglySide.call(
        'ritual_ZN16QMetaStringTable5enterERK10QByteArray',
        self._valueOf(value),
    )

  @staticmethod
  def writeBlob(*__, **_) -> Never:
    """
    Qt's 'void QMetaStringTable::writeBlob(char *out) const': names 'char',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMetaStringTable.writeBlob' has no cute function yet. Qt's 'void "
        "QMetaStringTable::writeBlob(char *out) const': names 'char', which "
        "has no cute class yet.")
