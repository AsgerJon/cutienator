"""
QSGBatchRenderer::Visualizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGBatchRenderer::Visualizer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QSGBatchRenderer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Visualizer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGBatchRenderer::Visualizer: a plain Python object
  standing in front of one C++ QSGBatchRenderer::Visualizer.

  What exists
  -----------

  Every function of Qt's QSGBatchRenderer::Visualizer that has a ritual and
  that Python can call so far, 6 names in all: 'mode', 'setMode',
  'visualizeChangesPrepare', 'prepareVisualize', 'visualize',
  'releaseResources'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGBatchRenderer::Visualizer::~Visualizer()': the destructor:
    Python never removes a C++ QSGBatchRenderer::Visualizer.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 leans on 'QSGBatchRenderer.

  What to expect
  --------------

  - The C++ QSGBatchRenderer::Visualizer is created at the first use, not by
    'QSGBatchRenderer::Visualizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGBatchRenderer::Visualizer.
  - Each name of Qt's QSGBatchRenderer::Visualizer that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QSGBatchRenderer::Visualizer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class VisualizeMode(CuteNum):
    """
    The enum 'QSGBatchRenderer::Visualizer::VisualizeMode' of Qt, with the 5
    names Qt gives in it.
    """

    VisualizeNothing = Kee[int](0)
    VisualizeBatches = Kee[int](1)
    VisualizeClipping = Kee[int](2)
    VisualizeChanges = Kee[int](3)
    VisualizeOverdraw = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBatchRenderer::Visualizer'

  #  A C++ QSGBatchRenderer::Visualizer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGBatchRenderer_Visualizer'

  #  The functions Qt calls itself that QSGBatchRenderer::Visualizer is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'visualizeChangesPrepare': (
          ('_ZN16QSGBatchRenderer10Visualizer23visualizeChangesPrepareEPNS_'
           '4NodeEj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGBatchRenderer.Node'),
               ('unsigned int', 'number', ''),
           )),
      ),
      'prepareVisualize': (
          ('_ZN16QSGBatchRenderer10Visualizer16prepareVisualizeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'visualize': (
          ('_ZN16QSGBatchRenderer10Visualizer9visualizeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'releaseResources': (
          ('_ZN16QSGBatchRenderer10Visualizer16releaseResourcesEv',
           ('nothing', 'nothing', ''),
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

  def mode(self) -> VisualizeMode:
    """
    Calls Qt's 'VisualizeMode QSGBatchRenderer::Visualizer::mode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-visualizer.html#mode

    Returns
    -------

    VisualizeMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'VisualizeMode(number)'
      gives.
    """
    #  VisualizeMode QSGBatchRenderer::Visualizer::mode() const
    return Visualizer.VisualizeMode(self.uglySide.call(
        'ritual_ZNK16QSGBatchRenderer10Visualizer4modeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(VisualizeMode)
  def setMode(self, mode: VisualizeMode) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Visualizer::setMode(VisualizeMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-visualizer.html#setMode

    Parameters
    ----------

    mode : VisualizeMode
      Passed on as its number.
    """
    #  void QSGBatchRenderer::Visualizer::setMode(VisualizeMode mode)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer10Visualizer7setModeENS0_13VisualizeMod'
        'eE',
        mode.value,
    )

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
    Qt's 'QSGBatchRenderer::Visualizer::Visualizer(Renderer *renderer)':
    leans on 'QSGBatchRenderer::Visualizer::visualizeChangesPrepare(
    QSGBatchRenderer::Node*, unsigned int)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGBatchRenderer.Visualizer.__init__' has no cute function yet. "
        "Qt's 'QSGBatchRenderer::Visualizer::Visualizer(Renderer "
        "*renderer)': leans on "
        "'QSGBatchRenderer::Visualizer::visualizeChangesPrepare(QSGBatchRend"
        "erer::Node*, unsigned int)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  @overload(WAIT['QSGBatchRenderer.Node'])
  @overload(NoneType)
  @overload(WAIT['QSGBatchRenderer.Node'], int)
  @overload(NoneType, int)
  def visualizeChangesPrepare(
      self,
      n: Optional[QSGBatchRenderer.Node],
      parentChanges: int = 0,
  ) -> None:
    """
    Calls Qt's 'void
    QSGBatchRenderer::Visualizer::visualizeChangesPrepare(Node *n, uint
    parentChanges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-visualizer.html

    Parameters
    ----------

    n : Optional[QSGBatchRenderer.Node]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentChanges : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QSGBatchRenderer::Visualizer::visualizeChangesPrepare(Node *n,
    #      uint parentChanges)
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer10Visualizer23visualizeChangesPrepareEP'
        'NS_4NodeEj',
        self._addressOf(n), parentChanges,
    )

  def prepareVisualize(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Visualizer::prepareVisualize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-visualizer.html#prepareVisualize
    """
    #  void QSGBatchRenderer::Visualizer::prepareVisualize()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer10Visualizer16prepareVisualizeEv',
    )

  def visualize(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Visualizer::visualize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-visualizer.html#visualize
    """
    #  void QSGBatchRenderer::Visualizer::visualize()
    self.uglySide.call('ritual_ZN16QSGBatchRenderer10Visualizer9visualizeEv')

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QSGBatchRenderer::Visualizer::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbatchrenderer-visualizer.html#releaseResources
    """
    #  void QSGBatchRenderer::Visualizer::releaseResources()
    self.uglySide.call(
        'ritual_ZN16QSGBatchRenderer10Visualizer16releaseResourcesEv',
    )
