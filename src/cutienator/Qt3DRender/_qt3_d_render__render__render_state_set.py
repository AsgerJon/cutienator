"""
Qt3DRender::Render::RenderStateSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/renderstateset_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::RenderStateSet to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderStateSet(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::RenderStateSet: a plain Python
  object standing in front of one C++ Qt3DRender::Render::RenderStateSet.

  C++ hands a Qt3DRender::Render::RenderStateSet around as a copy, so every
  C++ Qt3DRender::Render::RenderStateSet behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::RenderStateSet that has a ritual
  and that Python can call so far, 7 names in all: 'changeCost', 'stateMask',
  'merge', 'canAddStateOfType', 'contains', 'hasStateOfType',
  'allowMultipleStatesOfType'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::RenderStateSet::~RenderStateSet()': the
    destructor: Python removes its C++ Qt3DRender::Render::RenderStateSet by
    it, and has no other use for it.
  - Qt's 'const std::vector<StateVariant>
    &Qt3DRender::Render::RenderStateSet::states() const': gives a type Python
    has no way to take yet.
  - Qt's 'std::vector<StateVariant>
    &Qt3DRender::Render::RenderStateSet::states()': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RenderStateSet is created at the first use,
    not by 'Qt3DRender::Render::RenderStateSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::RenderStateSet back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::Render::RenderStateSet.
  - Each name of Qt's Qt3DRender::Render::RenderStateSet that has no cute
    function yet, 'addState', 'states', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::RenderStateSet'

  #  Qt's '~Qt3DRender::Render::RenderStateSet()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::RenderStateSet
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render14RenderStateSetD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def stateMask(self) -> int:
    """
    Calls Qt's 'StateMaskSet Qt3DRender::Render::RenderStateSet::stateMask()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderstateset.html#stateMask
    """
    #  StateMaskSet Qt3DRender::Render::RenderStateSet::stateMask() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderStateSet9stateMaskEv',
    )

  @overload(Qt3DRender.Render.StateMask)
  def canAddStateOfType(self, type: Qt3DRender.Render.StateMask) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::RenderStateSet::canAddStateOfType(StateMask type)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderstateset.html

    Parameters
    ----------

    type : Qt3DRender.Render.StateMask
      Passed on as its number.
    """
    #  bool Qt3DRender::Render::RenderStateSet::canAddStateOfType(StateMask
    #      type) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderStateSet17canAddStateOfTypeEN'
        'S0_9StateMaskE',
        type.value,
    )

  @overload(WAIT['Qt3DRender.Render.StateVariant'])
  def contains(self, ds: Qt3DRender.Render.StateVariant) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::RenderStateSet::contains(const
    StateVariant &ds) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderstateset.html#contains

    Parameters
    ----------

    ds : Qt3DRender.Render.StateVariant
      Passed on as a value: Qt reads the C++
      Qt3DRender::Render::StateVariant, which stays Python's own.
    """
    #  bool Qt3DRender::Render::RenderStateSet::contains(const StateVariant
    #      &ds) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderStateSet8containsERKNS0_12Sta'
        'teVariantE',
        self._valueOf(ds),
    )

  @overload(Qt3DRender.Render.StateMask)
  def hasStateOfType(self, type: Qt3DRender.Render.StateMask) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::RenderStateSet::hasStateOfType(StateMask type)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderstateset.html

    Parameters
    ----------

    type : Qt3DRender.Render.StateMask
      Passed on as its number.
    """
    #  bool Qt3DRender::Render::RenderStateSet::hasStateOfType(StateMask
    #      type) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderStateSet14hasStateOfTypeENS0_'
        '9StateMaskE',
        type.value,
    )

  @overload(Qt3DRender.Render.StateMask)
  def allowMultipleStatesOfType(
      self,
      type: Qt3DRender.Render.StateMask,
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::Render::RenderStateSet::allowMultipleStatesOfType(StateMask
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderstateset.html

    Parameters
    ----------

    type : Qt3DRender.Render.StateMask
      Passed on as its number.
    """
    #  bool Qt3DRender::Render::RenderStateSet::allowMultipleStatesOfType(
    #      StateMask type) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14RenderStateSet25allowMultipleStates'
        'OfTypeENS0_9StateMaskE',
        type.value,
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
    Notes what was given, for Qt's
    'Qt3DRender::Render::RenderStateSet::RenderStateSet()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderstateset.html
    """
    #  Qt3DRender::Render::RenderStateSet::RenderStateSet()
    self._noteCreation(RenderStateSet, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render14RenderStateSetC1Ev',
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

  @overload(THIS)
  @overload(NoneType)
  def changeCost(self, previousState: Optional[RenderStateSet]) -> int:
    """
    Calls Qt's 'int
    Qt3DRender::Render::RenderStateSet::changeCost(RenderStateSet
    *previousState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderstateset.html#changeCost

    Parameters
    ----------

    previousState : Optional[RenderStateSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int Qt3DRender::Render::RenderStateSet::changeCost(RenderStateSet
    #      *previousState)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render14RenderStateSet10changeCostEPS1_',
        self._addressOf(previousState),
    )

  @overload(THIS)
  @overload(NoneType)
  def merge(self, other: Optional[RenderStateSet]) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::RenderStateSet::merge(const
    RenderStateSet *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderstateset.html#merge

    Parameters
    ----------

    other : Optional[RenderStateSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::RenderStateSet::merge(const RenderStateSet
    #      *other)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render14RenderStateSet5mergeEPKS1_',
        self._addressOf(other),
    )

  @staticmethod
  def addState(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::RenderStateSet::addState': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RenderStateSet.addState' has no cute function "
        "yet. Qt's 'Qt3DRender::Render::RenderStateSet::addState': a "
        "template: a pattern and no single function.")

  @staticmethod
  def states(*__, **_) -> Never:
    """
    - Qt's 'const std::vector<StateVariant>
      &Qt3DRender::Render::RenderStateSet::states() const': gives a type
      Python has no way to take yet.
    - Qt's 'std::vector<StateVariant>
      &Qt3DRender::Render::RenderStateSet::states()': gives a type Python has
      no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RenderStateSet.states' has no cute function "
        "yet. Qt's 'const std::vector<StateVariant> "
        "&Qt3DRender::Render::RenderStateSet::states() const': gives a type "
        "Python has no way to take yet. Qt's 'std::vector<StateVariant> "
        "&Qt3DRender::Render::RenderStateSet::states()': gives a type "
        "Python has no way to take yet.")
