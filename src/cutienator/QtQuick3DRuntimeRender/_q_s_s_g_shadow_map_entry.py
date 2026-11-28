"""
QSSGShadowMapEntry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadowmap_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShadowMapEntry to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QSSGShadowMapEntry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShadowMapEntry: a plain Python object standing in
  front of one C++ QSSGShadowMapEntry.

  C++ hands a QSSGShadowMapEntry around as a copy, so every C++
  QSSGShadowMapEntry behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGShadowMapEntry that has a ritual and that Python
  can call so far, 2 names in all: 'withAtlas', 'destroyRhiResources'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGShadowMapEntry::~QSSGShadowMapEntry()': the destructor: Python
    removes its C++ QSSGShadowMapEntry by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGShadowMapEntry is created at the first use, not by
    'QSSGShadowMapEntry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShadowMapEntry back gives a copy the ritual made
    for Python, in a new cute QSSGShadowMapEntry.
  """

  #  The classes Qt writes inside QSSGShadowMapEntry, each a class in here as
  #  in C++.

  class AtlasEntry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGShadowMapEntry::AtlasEntry: a plain Python
    object standing in front of one C++ QSSGShadowMapEntry::AtlasEntry.

    C++ hands a QSSGShadowMapEntry::AtlasEntry around as a copy, so every C++
    QSSGShadowMapEntry::AtlasEntry behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGShadowMapEntry::AtlasEntry yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGShadowMapEntry::AtlasEntry::~AtlasEntry()': the destructor:
      Python removes its C++ QSSGShadowMapEntry::AtlasEntry by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGShadowMapEntry::AtlasEntry is created at the first use, not
      by 'QSSGShadowMapEntry::AtlasEntry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGShadowMapEntry::AtlasEntry back gives a copy
      the ritual made for Python, in a new cute
      QSSGShadowMapEntry::AtlasEntry.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGShadowMapEntry::AtlasEntry'

    #  Qt's '~QSSGShadowMapEntry::AtlasEntry()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGShadowMapEntry::AtlasEntry behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QSSGShadowMapEntry10AtlasEntryD1Ev'

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

  @staticmethod
  @overload(int)
  def withAtlas(lightIdx: int) -> QSSGShadowMapEntry:
    """
    Calls Qt's 'QSSGShadowMapEntry QSSGShadowMapEntry::withAtlas(quint32
    lightIdx)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgshadowmapentry.html#withAtlas

    Parameters
    ----------

    lightIdx : int
      Passed on as it is.

    Returns
    -------

    QSSGShadowMapEntry
      A new cute QSSGShadowMapEntry around the copy Qt gave back. Python owns
      it.
    """
    #  QSSGShadowMapEntry QSSGShadowMapEntry::withAtlas(quint32 lightIdx)
    address = Rituals.call(
        'ritual_ZN18QSSGShadowMapEntry9withAtlasEj', lightIdx,
    )
    return QSSGShadowMapEntry._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShadowMapEntry'

  #  Qt's '~QSSGShadowMapEntry()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGShadowMapEntry behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSSGShadowMapEntryD1Ev'

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
    Notes what was given, for Qt's
    'QSSGShadowMapEntry::QSSGShadowMapEntry()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadowmapentry.html#QSSGShadowMapEntry
    """
    #  QSSGShadowMapEntry::QSSGShadowMapEntry()
    self._noteCreation(QSSGShadowMapEntry, lambda: Rituals.call(
        'ritual_ZN18QSSGShadowMapEntryC1Ev',
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

  def destroyRhiResources(self) -> None:
    """
    Calls Qt's 'void QSSGShadowMapEntry::destroyRhiResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshadowmapentry.html#destroyRhiResources
    """
    #  void QSSGShadowMapEntry::destroyRhiResources()
    self.uglySide.call(
        'ritual_ZN18QSSGShadowMapEntry19destroyRhiResourcesEv',
    )
