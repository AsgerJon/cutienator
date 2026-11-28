"""
Qt3DRender::Render::StateVariant binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/statevariant_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::StateVariant to be private: it declares the
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


class StateVariant(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::StateVariant: a plain Python
  object standing in front of one C++ Qt3DRender::Render::StateVariant.

  C++ hands a Qt3DRender::Render::StateVariant around as a copy, so every C++
  Qt3DRender::Render::StateVariant behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::StateVariant that has a ritual
  and that Python can call so far, 4 names in all: 'state', 'constState',
  '__eq__', '__ne__'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::StateVariant::~StateVariant()': the destructor:
    Python removes its C++ Qt3DRender::Render::StateVariant by it, and has no
    other use for it.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::StateVariant is created at the first use, not
    by 'Qt3DRender::Render::StateVariant(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::StateVariant back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::Render::StateVariant.
  - Each name of Qt's Qt3DRender::Render::StateVariant that has no cute
    function yet, 'createState', 'fromValue', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside Qt3DRender::Render::StateVariant, each a
  #  class in here as in C++.

  class u_Data(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's Qt3DRender::Render::StateVariant::u_Data: a plain
    Python object standing in front of one C++
    Qt3DRender::Render::StateVariant::u_Data.

    C++ hands a Qt3DRender::Render::StateVariant::u_Data around as a copy, so
    every C++ Qt3DRender::Render::StateVariant::u_Data behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's Qt3DRender::Render::StateVariant::u_Data yet. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'u_Data &Qt3DRender::Render::StateVariant::u_Data::operator=(const
      u_Data &other)': assignment: Python binds a name and has no operator
      for it.
    - Qt's 'Qt3DRender::Render::StateVariant::u_Data::~u_Data()': the
      destructor: Python removes its C++
      Qt3DRender::Render::StateVariant::u_Data by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ Qt3DRender::Render::StateVariant::u_Data is created at the
      first use, not by 'Qt3DRender::Render::StateVariant::u_Data(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a Qt3DRender::Render::StateVariant::u_Data back gives
      a copy the ritual made for Python, in a new cute
      Qt3DRender::Render::StateVariant::u_Data.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DRender::Render::StateVariant::u_Data'

    #  Qt's '~Qt3DRender::Render::StateVariant::u_Data()'. Naming it makes
    #  this a value class: Python owns every C++
    #  Qt3DRender::Render::StateVariant::u_Data behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN10Qt3DRender6Render12StateVariant6u_DataD1Ev')

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DRender::Render::StateVariant::u_Data::u_Data()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3drender-render-statevariant-u_data.html
      """
      #  Qt3DRender::Render::StateVariant::u_Data::u_Data()
      self._noteCreation(StateVariant.u_Data, lambda: Rituals.call(
          'ritual_ZN10Qt3DRender6Render12StateVariant6u_DataC1Ev',
      ))

    @overload(THIS)
    def __init__(self, other: StateVariant.u_Data) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DRender::Render::StateVariant::u_Data::u_Data(const u_Data
      &other)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3drender-render-statevariant-u_data.html

      Parameters
      ----------

      other : StateVariant.u_Data
        Passed on as a value: Qt reads the C++
        Qt3DRender::Render::StateVariant::u_Data, which stays Python's own.
      """
      #  Qt3DRender::Render::StateVariant::u_Data::u_Data(const u_Data
      #      &other)
      self._noteCreation(StateVariant.u_Data, lambda: Rituals.call(
          'ritual_ZN10Qt3DRender6Render12StateVariant6u_DataC1ERKS2_',
          self._valueOf(other),
      ))

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
  __qt_class__ = 'Qt3DRender::Render::StateVariant'

  #  Qt's '~Qt3DRender::Render::StateVariant()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::Render::StateVariant behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render12StateVariantD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def constState(self) -> Optional[Qt3DRender.Render.RenderStateImpl]:
    """
    Calls Qt's 'const RenderStateImpl
    *Qt3DRender::Render::StateVariant::constState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-statevariant.html#constState

    Returns
    -------

    Optional[Qt3DRender.Render.RenderStateImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const RenderStateImpl *Qt3DRender::Render::StateVariant::constState()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12StateVariant10constStateEv',
    )
    return Qt3DRender.Render.RenderStateImpl._cuteAt(address)

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
  def __eq__(self, other: StateVariant) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::StateVariant::operator==(const
    StateVariant &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-statevariant.html#operator==

    Parameters
    ----------

    other : StateVariant
      Passed on as a value: Qt reads the C++
      Qt3DRender::Render::StateVariant, which stays Python's own.
    """
    #  bool Qt3DRender::Render::StateVariant::operator==(const StateVariant
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12StateVarianteqERKS1_',
        self._valueOf(other),
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
  def __ne__(self, other: StateVariant) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::StateVariant::operator!=(const
    StateVariant &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-statevariant.html#operator!=

    Parameters
    ----------

    other : StateVariant
      Passed on as a value: Qt reads the C++
      Qt3DRender::Render::StateVariant, which stays Python's own.
    """
    #  bool Qt3DRender::Render::StateVariant::operator!=(const StateVariant
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12StateVariantneERKS1_',
        self._valueOf(other),
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

  def state(self) -> Optional[Qt3DRender.Render.RenderStateImpl]:
    """
    Calls Qt's 'RenderStateImpl *Qt3DRender::Render::StateVariant::state()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-statevariant.html#state

    Returns
    -------

    Optional[Qt3DRender.Render.RenderStateImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  RenderStateImpl *Qt3DRender::Render::StateVariant::state()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12StateVariant5stateEv',
    )
    return Qt3DRender.Render.RenderStateImpl._cuteAt(address)

  @staticmethod
  def createState(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::StateVariant::createState': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.StateVariant.createState' has no cute function "
        "yet. Qt's 'Qt3DRender::Render::StateVariant::createState': a "
        "template: a pattern and no single function.")

  @staticmethod
  def fromValue(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::StateVariant::fromValue': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.StateVariant.fromValue' has no cute function "
        "yet. Qt's 'Qt3DRender::Render::StateVariant::fromValue': a "
        "template: a pattern and no single function.")
