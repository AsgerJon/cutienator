"""
QSSGRenderExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.keenum import Kee

from ..cute import CuteNum
from . import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderExtension(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderExtension: a plain Python object standing
  in front of one C++ QSSGRenderExtension.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's
  QSSGRenderExtension is built on Qt's QSSGRenderGraphObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderExtension that has a ritual and that
  Python can call so far, 3 names in all: 'resetForFrame', 'mode', 'stage'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderExtension::~QSSGRenderExtension()': the destructor:
    Python never removes a C++ QSSGRenderExtension.
  - Qt's 'bool QSSGRenderExtension::prepareData(QSSGFrameData &data)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderExtension::prepareRender(QSSGFrameData &data)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderExtension::render(QSSGFrameData &data)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QSSGRenderExtension is created at the first use, not by
    'QSSGRenderExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderExtension.
  - Each name of Qt's QSSGRenderExtension that has no cute function yet,
    '__init__', 'prepareData', 'prepareRender', 'render', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderExtension, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class RenderMode(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderExtension::RenderMode' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Standalone = Kee[int](0)
    Main = Kee[int](1)

  class RenderStage(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderExtension::RenderStage' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    PreColor = Kee[int](0)
    PostColor = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderExtension'

  #  A C++ QSSGRenderExtension Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSSGRenderExtension'

  #  The functions Qt calls itself that QSSGRenderExtension is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'prepareData': (
          'bool QSSGRenderExtension::prepareData(QSSGFrameData &)',
      ),
      'prepareRender': (
          'void QSSGRenderExtension::prepareRender(QSSGFrameData &)',
      ),
      'render': (
          'void QSSGRenderExtension::render(QSSGFrameData &)',
      ),
  }

  #  The functions Qt calls itself that QSSGRenderExtension is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'resetForFrame': (
          ('_ZN19QSSGRenderExtension13resetForFrameEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'mode': (
          ('_ZNK19QSSGRenderExtension4modeEv',
           ('int', 'enum',
            'QtQuick3DRuntimeRender:QSSGRenderExtension.RenderMode'),
           ()),
      ),
      'stage': (
          ('_ZNK19QSSGRenderExtension5stageEv',
           ('int', 'enum',
            'QtQuick3DRuntimeRender:QSSGRenderExtension.RenderStage'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def mode(self) -> RenderMode:
    """
    Calls Qt's 'RenderMode QSSGRenderExtension::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderextension.html#mode

    Returns
    -------

    RenderMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderMode(number)'
      gives.
    """
    #  RenderMode QSSGRenderExtension::mode() const
    return QSSGRenderExtension.RenderMode(self.uglySide.call(
        'ritual_ZNK19QSSGRenderExtension4modeEv',
    ))

  def stage(self) -> RenderStage:
    """
    Calls Qt's 'RenderStage QSSGRenderExtension::stage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderextension.html#stage

    Returns
    -------

    RenderStage
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RenderStage(number)'
      gives.
    """
    #  RenderStage QSSGRenderExtension::stage() const
    return QSSGRenderExtension.RenderStage(self.uglySide.call(
        'ritual_ZNK19QSSGRenderExtension5stageEv',
    ))

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QSSGRenderExtension::QSSGRenderExtension()': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    - Qt's 'QSSGRenderExtension::QSSGRenderExtension(Type inType, FlagT
      inFlags)': the class is abstract, so C++ cannot make one, and the C++
      class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QSSGRenderExtension.__init__' has no cute function yet. Qt's "
        "'QSSGRenderExtension::QSSGRenderExtension()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open. Qt's "
        "'QSSGRenderExtension::QSSGRenderExtension(Type inType, FlagT "
        "inFlags)': the class is abstract, so C++ cannot make one, and the "
        "C++ class of ours does not fill in every function it leaves open.")

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

  def resetForFrame(self) -> None:
    """
    Calls Qt's 'void QSSGRenderExtension::resetForFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderextension.html#resetForFrame
    """
    #  void QSSGRenderExtension::resetForFrame()
    self.uglySide.call('ritual_ZN19QSSGRenderExtension13resetForFrameEv')

  @staticmethod
  def prepareData(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRenderExtension::prepareData(QSSGFrameData &data)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderExtension.prepareData' has no cute function yet. Qt's "
        "'bool QSSGRenderExtension::prepareData(QSSGFrameData &data)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def prepareRender(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderExtension::prepareRender(QSSGFrameData &data)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderExtension.prepareRender' has no cute function yet. Qt's "
        "'void QSSGRenderExtension::prepareRender(QSSGFrameData &data)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def render(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderExtension::render(QSSGFrameData &data)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderExtension.render' has no cute function yet. Qt's 'void "
        "QSSGRenderExtension::render(QSSGFrameData &data)': takes a type "
        "Python has no way to hand over yet.")
