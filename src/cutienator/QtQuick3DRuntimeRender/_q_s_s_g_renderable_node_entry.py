"""
QSSGRenderableNodeEntry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderableNodeEntry to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSSGRenderNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderNode = WAIT['QSSGRenderNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRenderableNodeEntry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderableNodeEntry: a plain Python object
  standing in front of one C++ QSSGRenderableNodeEntry.

  C++ hands a QSSGRenderableNodeEntry around as a copy, so every C++
  QSSGRenderableNodeEntry behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderableNodeEntry that has a ritual and that
  Python can call so far, 1 name in all: 'isNull'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderableNodeEntry::QSSGRenderableNodeEntry(QSSGRenderNode
    &inNode)': takes a type Python has no way to hand over yet.
  - Qt's 'QSSGRenderableNodeEntry::~QSSGRenderableNodeEntry()': the
    destructor: Python removes its C++ QSSGRenderableNodeEntry by it, and has
    no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderableNodeEntry is created at the first use, not by
    'QSSGRenderableNodeEntry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderableNodeEntry back gives a copy the ritual
    made for Python, in a new cute QSSGRenderableNodeEntry.
  """

  #  The enums Qt writes inside QSSGRenderableNodeEntry, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Overridden(CuteNum):
    """
    The enum 'QSSGRenderableNodeEntry::Overridden' of Qt, with the 5 names Qt
    gives in it.
    """

    Original = Kee[int](0)
    Disabled = Kee[int](1)
    GlobalTransform = Kee[int](2)
    Materials = Kee[int](4)
    GlobalOpacity = Kee[int](8)

  #  The classes Qt writes inside QSSGRenderableNodeEntry, each a class in
  #  here as in C++.

  class ExtensionOverrides(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderableNodeEntry::ExtensionOverrides: a
    plain Python object standing in front of one C++
    QSSGRenderableNodeEntry::ExtensionOverrides.

    C++ hands a QSSGRenderableNodeEntry::ExtensionOverrides around as a copy,
    so every C++ QSSGRenderableNodeEntry::ExtensionOverrides behind a cute
    one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderableNodeEntry::ExtensionOverrides yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QSSGRenderableNodeEntry::ExtensionOverrides::~ExtensionOverrides()':
      the destructor: Python removes its C++
      QSSGRenderableNodeEntry::ExtensionOverrides by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGRenderableNodeEntry::ExtensionOverrides is created at the
      first use, not by 'QSSGRenderableNodeEntry::ExtensionOverrides(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderableNodeEntry::ExtensionOverrides back
      gives a copy the ritual made for Python, in a new cute
      QSSGRenderableNodeEntry::ExtensionOverrides.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderableNodeEntry::ExtensionOverrides'

    #  Qt's '~QSSGRenderableNodeEntry::ExtensionOverrides()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSSGRenderableNodeEntry::ExtensionOverrides behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN23QSSGRenderableNodeEntry18ExtensionOverridesD1Ev')

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
  __qt_class__ = 'QSSGRenderableNodeEntry'

  #  Qt's '~QSSGRenderableNodeEntry()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGRenderableNodeEntry behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QSSGRenderableNodeEntryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderableNodeEntry::isNull() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderablenodeentry.html#isNull
    """
    #  bool QSSGRenderableNodeEntry::isNull() const
    return self.uglySide.call('ritual_ZNK23QSSGRenderableNodeEntry6isNullEv')

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
    'QSSGRenderableNodeEntry::QSSGRenderableNodeEntry()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderablenodeentry.html
    """
    #  QSSGRenderableNodeEntry::QSSGRenderableNodeEntry()
    self._noteCreation(QSSGRenderableNodeEntry, lambda: Rituals.call(
        'ritual_ZN23QSSGRenderableNodeEntryC1Ev',
    ))

  @overload(QSSGRenderNode)
  @overload(NoneType)
  def __init__(self, inNode: Optional[QSSGRenderNode]) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderableNodeEntry::QSSGRenderableNodeEntry(QSSGRenderNode
    *inNode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderablenodeentry.html

    Parameters
    ----------

    inNode : Optional[QSSGRenderNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSSGRenderableNodeEntry::QSSGRenderableNodeEntry(QSSGRenderNode
    #      *inNode)
    self._noteCreation(QSSGRenderableNodeEntry, lambda: Rituals.call(
        'ritual_ZN23QSSGRenderableNodeEntryC1EP14QSSGRenderNode',
        self._addressOf(inNode),
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
