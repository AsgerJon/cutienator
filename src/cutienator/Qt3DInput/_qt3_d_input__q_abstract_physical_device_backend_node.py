"""
Qt3DInput::QAbstractPhysicalDeviceBackendNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldevicebackendnode_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means Qt3DInput::QAbstractPhysicalDeviceBackendNode to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DInput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractPhysicalDeviceBackendNode(Qt3DInput.Input.BackendNode):
  """
  The cute side of Qt's Qt3DInput::QAbstractPhysicalDeviceBackendNode: a
  plain Python object standing in front of one C++
  Qt3DInput::QAbstractPhysicalDeviceBackendNode.

  It is built on the cute 'Qt3DInput::Input::BackendNode', as Qt's
  Qt3DInput::QAbstractPhysicalDeviceBackendNode is built on Qt's
  Qt3DInput::Input::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QAbstractPhysicalDeviceBackendNode that
  has a ritual and that Python can call so far, 7 names in all: 'cleanup',
  'syncFromFrontEnd', 'setInputAspect', 'inputAspect', 'processedAxisValue',
  'axisValue', 'isButtonPressed'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DInput::QAbstractPhysicalDeviceBackendNode::
    QAbstractPhysicalDeviceBackendNode(
    QAbstractPhysicalDeviceBackendNodePrivate &dd)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QAbstractPhysicalDeviceBackendNodePrivate
    *Qt3DInput::QAbstractPhysicalDeviceBackendNode::d_func()': gives
    'Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate', which has no cute
    class yet.
  - Qt's 'const QAbstractPhysicalDeviceBackendNodePrivate
    *Qt3DInput::QAbstractPhysicalDeviceBackendNode::d_func() const': gives
    'Qt3DInput::QAbstractPhysicalDeviceBackendNodePrivate', which has no cute
    class yet.

  What to expect
  --------------

  - The C++ Qt3DInput::QAbstractPhysicalDeviceBackendNode is created at the
    first use, not by 'Qt3DInput::QAbstractPhysicalDeviceBackendNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DInput::QAbstractPhysicalDeviceBackendNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QAbstractPhysicalDeviceBackendNode'

  #  A C++ Qt3DInput::QAbstractPhysicalDeviceBackendNode Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QAbstractPhysicalDeviceBackendNode'

  #  The functions Qt calls itself that
  #  Qt3DInput::QAbstractPhysicalDeviceBackendNode is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'cleanup': (
          ('_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode7cleanupEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'axisValue': (
          ('_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode9axisValueEi',
           ('float', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'isButtonPressed': (
          ('_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode15isButtonPre'
           'ssedEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def inputAspect(self) -> Optional[Qt3DInput.QInputAspect]:
    """
    Calls Qt's 'QInputAspect
    *Qt3DInput::QAbstractPhysicalDeviceBackendNode::inputAspect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevicebackendnode.html

    Returns
    -------

    Optional[Qt3DInput.QInputAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputAspect
    #      *Qt3DInput::QAbstractPhysicalDeviceBackendNode::inputAspect()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode11inputAsp'
        'ectEv',
    )
    return Qt3DInput.QInputAspect._cuteAt(address)

  @overload(int)
  def axisValue(self, axisIdentifier: int) -> float:
    """
    Calls Qt's 'float
    Qt3DInput::QAbstractPhysicalDeviceBackendNode::axisValue(int
    axisIdentifier) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevicebackendnode.html

    Parameters
    ----------

    axisIdentifier : int
      Passed on as it is.
    """
    #  float Qt3DInput::QAbstractPhysicalDeviceBackendNode::axisValue(int
    #      axisIdentifier) const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode9axisValue'
        'Ei',
        axisIdentifier,
    )

  @overload(int)
  def isButtonPressed(self, buttonIdentifier: int) -> bool:
    """
    Calls Qt's 'bool
    Qt3DInput::QAbstractPhysicalDeviceBackendNode::isButtonPressed(int
    buttonIdentifier) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevicebackendnode.html

    Parameters
    ----------

    buttonIdentifier : int
      Passed on as it is.
    """
    #  bool
    #      Qt3DInput::QAbstractPhysicalDeviceBackendNode::isButtonPressed(int
    #      buttonIdentifier) const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput34QAbstractPhysicalDeviceBackendNode15isButton'
        'PressedEi',
        buttonIdentifier,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DInput.QInputAspect'])
  @overload(NoneType)
  def setInputAspect(self, aspect: Optional[Qt3DInput.QInputAspect]) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractPhysicalDeviceBackendNode::setInputAspect(
    QInputAspect *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevicebackendnode.html

    Parameters
    ----------

    aspect : Optional[Qt3DInput.QInputAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DInput::QAbstractPhysicalDeviceBackendNode::setInputAspect(
    #      QInputAspect *aspect)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode14setInputA'
        'spectEPNS_12QInputAspectE',
        self._addressOf(aspect),
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

  @overload(Qt3DCore.QBackendNode.Mode)
  def __init__(self, mode: Qt3DCore.QBackendNode.Mode) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DInput::QAbstractPhysicalDeviceBackendNode::
    QAbstractPhysicalDeviceBackendNode(QBackendNode::Mode mode)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevicebackendnode.html

    Parameters
    ----------

    mode : Qt3DCore.QBackendNode.Mode
      Passed on as its number.
    """
    #  Qt3DInput::QAbstractPhysicalDeviceBackendNode::
    #      QAbstractPhysicalDeviceBackendNode(QBackendNode::Mode mode)
    self._noteCreation(
        QAbstractPhysicalDeviceBackendNode, lambda: Rituals.call(
            'ritual_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNodeC1EN8Qt'
            '3DCore12QBackendNode4ModeE',
            mode.value,
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractPhysicalDeviceBackendNode::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevicebackendnode.html
    """
    #  void Qt3DInput::QAbstractPhysicalDeviceBackendNode::cleanup()
    ritual = (
        'ritual_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode7cleanupEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode7clea'
          'nupEv')
    self.uglySide.call(ritual)

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DInput::QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevicebackendnode.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(
    #      const Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode16syncFromF'
        'rontEndEPKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode16syn'
          'cFromFrontEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @overload(int)
  def processedAxisValue(self, axisIdentifier: int) -> float:
    """
    Calls Qt's 'float
    Qt3DInput::QAbstractPhysicalDeviceBackendNode::processedAxisValue(int
    axisIdentifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qabstractphysicaldevicebackendnode.html

    Parameters
    ----------

    axisIdentifier : int
      Passed on as it is.
    """
    #  float
    #      Qt3DInput::QAbstractPhysicalDeviceBackendNode::processedAxisValue(
    #      int axisIdentifier)
    return self.uglySide.call(
        'ritual_ZN9Qt3DInput34QAbstractPhysicalDeviceBackendNode18processed'
        'AxisValueEi',
        axisIdentifier,
    )
