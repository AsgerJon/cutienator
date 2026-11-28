"""
QSSGRenderSubset binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermesh_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderSubset to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QSSGRenderSubset(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderSubset: a plain Python object standing in
  front of one C++ QSSGRenderSubset.

  C++ hands a QSSGRenderSubset around as a copy, so every C++
  QSSGRenderSubset behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderSubset that has a ritual and that Python
  can call so far, 2 names in all: 'lodCount', 'lodOffset'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderSubset &QSSGRenderSubset::operator=(const
    QSSGRenderSubset &inOther)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QSSGRenderSubset::~QSSGRenderSubset()': the destructor: Python
    removes its C++ QSSGRenderSubset by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderSubset is created at the first use, not by
    'QSSGRenderSubset(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderSubset back gives a copy the ritual made
    for Python, in a new cute QSSGRenderSubset.
  """

  #  The classes Qt writes inside QSSGRenderSubset, each a class in here as
  #  in C++.

  class Lod(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderSubset::Lod: a plain Python object
    standing in front of one C++ QSSGRenderSubset::Lod.

    C++ hands a QSSGRenderSubset::Lod around as a copy, so every C++
    QSSGRenderSubset::Lod behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderSubset::Lod yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderSubset::Lod::~Lod()': the destructor: Python removes
      its C++ QSSGRenderSubset::Lod by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderSubset::Lod is created at the first use, not by
      'QSSGRenderSubset::Lod(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderSubset::Lod back gives a copy the ritual
      made for Python, in a new cute QSSGRenderSubset::Lod.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderSubset::Lod'

    #  Qt's '~QSSGRenderSubset::Lod()'. Naming it makes this a value class:
    #  Python owns every C++ QSSGRenderSubset::Lod behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QSSGRenderSubset3LodD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderSubset'

  #  Qt's '~QSSGRenderSubset()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGRenderSubset behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QSSGRenderSubsetD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def lodCount(self, lodLevel: int) -> int:
    """
    Calls Qt's 'quint32 QSSGRenderSubset::lodCount(int lodLevel) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendersubset.html#lodCount

    Parameters
    ----------

    lodLevel : int
      Passed on as it is.
    """
    #  quint32 QSSGRenderSubset::lodCount(int lodLevel) const
    return self.uglySide.call(
        'ritual_ZNK16QSSGRenderSubset8lodCountEi', lodLevel,
    )

  @overload(int)
  def lodOffset(self, lodLevel: int) -> int:
    """
    Calls Qt's 'quint32 QSSGRenderSubset::lodOffset(int lodLevel) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendersubset.html#lodOffset

    Parameters
    ----------

    lodLevel : int
      Passed on as it is.
    """
    #  quint32 QSSGRenderSubset::lodOffset(int lodLevel) const
    return self.uglySide.call(
        'ritual_ZNK16QSSGRenderSubset9lodOffsetEi', lodLevel,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderSubset::QSSGRenderSubset()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendersubset.html#QSSGRenderSubset
    """
    #  QSSGRenderSubset::QSSGRenderSubset()
    self._noteCreation(QSSGRenderSubset, lambda: Rituals.call(
        'ritual_ZN16QSSGRenderSubsetC1Ev',
    ))

  @overload(THIS)
  def __init__(self, inOther: QSSGRenderSubset) -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderSubset::QSSGRenderSubset(const
    QSSGRenderSubset &inOther)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendersubset.html#QSSGRenderSubset

    Parameters
    ----------

    inOther : QSSGRenderSubset
      Passed on as a value: Qt reads the C++ QSSGRenderSubset, which stays
      Python's own.
    """
    #  QSSGRenderSubset::QSSGRenderSubset(const QSSGRenderSubset &inOther)
    self._noteCreation(QSSGRenderSubset, lambda: Rituals.call(
        'ritual_ZN16QSSGRenderSubsetC1ERKS_', self._valueOf(inOther),
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
