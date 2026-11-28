"""
QSSGRenderVertexBufferEntry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmesh_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSSGRenderVertexBufferEntry to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QSSGRenderVertexBufferEntry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderVertexBufferEntry: a plain Python object
  standing in front of one C++ QSSGRenderVertexBufferEntry.

  C++ hands a QSSGRenderVertexBufferEntry around as a copy, so every C++
  QSSGRenderVertexBufferEntry behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QSSGRenderVertexBufferEntry yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderVertexBufferEntry::QSSGRenderVertexBufferEntry(const
    QByteArray &nm, QSSGRenderComponentType type, quint32 numComponents,
    quint32 firstItemOffset)': names the enum 'QSSGRenderComponentType',
    whose class cannot be named here.
  - Qt's 'QSSGRenderVertexBufferEntry
    &QSSGRenderVertexBufferEntry::operator=(const QSSGRenderVertexBufferEntry
    &inOther)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QSSGRenderVertexBufferEntry::~QSSGRenderVertexBufferEntry()': the
    destructor: Python removes its C++ QSSGRenderVertexBufferEntry by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderVertexBufferEntry is created at the first use, not by
    'QSSGRenderVertexBufferEntry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderVertexBufferEntry back gives a copy the
    ritual made for Python, in a new cute QSSGRenderVertexBufferEntry.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderVertexBufferEntry'

  #  Qt's '~QSSGRenderVertexBufferEntry()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGRenderVertexBufferEntry behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QSSGRenderVertexBufferEntryD1Ev'

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
    'QSSGRenderVertexBufferEntry::QSSGRenderVertexBufferEntry()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendervertexbufferentry.html
    """
    #  QSSGRenderVertexBufferEntry::QSSGRenderVertexBufferEntry()
    self._noteCreation(QSSGRenderVertexBufferEntry, lambda: Rituals.call(
        'ritual_ZN27QSSGRenderVertexBufferEntryC1Ev',
    ))

  @overload(THIS)
  def __init__(self, inOther: QSSGRenderVertexBufferEntry) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderVertexBufferEntry::QSSGRenderVertexBufferEntry(const
    QSSGRenderVertexBufferEntry &inOther)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendervertexbufferentry.html

    Parameters
    ----------

    inOther : QSSGRenderVertexBufferEntry
      Passed on as a value: Qt reads the C++ QSSGRenderVertexBufferEntry,
      which stays Python's own.
    """
    #  QSSGRenderVertexBufferEntry::QSSGRenderVertexBufferEntry(const
    #      QSSGRenderVertexBufferEntry &inOther)
    self._noteCreation(QSSGRenderVertexBufferEntry, lambda: Rituals.call(
        'ritual_ZN27QSSGRenderVertexBufferEntryC1ERKS_',
        self._valueOf(inOther),
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
