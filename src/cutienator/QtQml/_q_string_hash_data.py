"""
QStringHashData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qstringhash_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QStringHashData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QStringHashData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStringHashData: a plain Python object standing in
  front of one C++ QStringHashData.

  What exists
  -----------

  Every function of Qt's QStringHashData that has a ritual and that Python
  can call so far, 2 names in all: 'rehashToBits', 'rehashToSize'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStringHashData::~QStringHashData()': the destructor: Python never
    removes a C++ QStringHashData.
  - Qt's 'void QStringHashData::rehashNode(QStringHashNode **newBuckets, int
    nb, QStringHashNode *node)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 9 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QStringHashData is created at the first use, not by
    'QStringHashData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStringHashData.
  - Each name of Qt's QStringHashData that has no cute function yet,
    'rehashNode', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStringHashData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's 'QStringHashData::QStringHashData()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstringhashdata.html#QStringHashData
    """
    #  QStringHashData::QStringHashData()
    self._noteCreation(QStringHashData, lambda: Rituals.call(
        'ritual_ZN15QStringHashDataC1Ev',
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

  @overload(int)
  def rehashToBits(self, bits: int) -> None:
    """
    Calls Qt's 'void QStringHashData::rehashToBits(short bits)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashdata.html#rehashToBits

    Parameters
    ----------

    bits : int
      Passed on as it is.
    """
    #  void QStringHashData::rehashToBits(short bits)
    self.uglySide.call('ritual_ZN15QStringHashData12rehashToBitsEs', bits)

  @overload(int)
  def rehashToSize(self, size: int) -> None:
    """
    Calls Qt's 'void QStringHashData::rehashToSize(int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qstringhashdata.html#rehashToSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QStringHashData::rehashToSize(int size)
    self.uglySide.call('ritual_ZN15QStringHashData12rehashToSizeEi', size)

  @staticmethod
  def rehashNode(*__, **_) -> Never:
    """
    Qt's 'void QStringHashData::rehashNode(QStringHashNode **newBuckets, int
    nb, QStringHashNode *node)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QStringHashData.rehashNode' has no cute function yet. Qt's 'void "
        "QStringHashData::rehashNode(QStringHashNode **newBuckets, int nb, "
        "QStringHashNode *node)': takes a type Python has no way to hand "
        "over yet.")
