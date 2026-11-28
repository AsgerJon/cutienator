"""
Qt3DExtras::QFirstPersonCameraController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/qfirstpersoncameracontroller.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFirstPersonCameraController(Qt3DExtras.QAbstractCameraController):
  """
  The cute side of Qt's Qt3DExtras::QFirstPersonCameraController: a plain
  Python object standing in front of one C++
  Qt3DExtras::QFirstPersonCameraController.

  It is built on the cute 'Qt3DExtras::QAbstractCameraController', as Qt's
  Qt3DExtras::QFirstPersonCameraController is built on Qt's
  Qt3DExtras::QAbstractCameraController, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QFirstPersonCameraController that has a
  ritual and that Python can call so far, 3 names in all: 'metaObject', 'tr',
  'moveCamera'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::QFirstPersonCameraController::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::QFirstPersonCameraController::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DExtras::QFirstPersonCameraController::~QFirstPersonCameraController(
    )': the destructor: Python never removes a C++
    Qt3DExtras::QFirstPersonCameraController.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::QFirstPersonCameraController is created at the first
    use, not by 'Qt3DExtras::QFirstPersonCameraController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QFirstPersonCameraController.
  - Qt tells when it has removed the C++
    Qt3DExtras::QFirstPersonCameraController. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DExtras::QFirstPersonCameraController::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qfirstpersoncameracontroller.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DExtras::QFirstPersonCameraController::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras28QFirstPersonCameraController2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QFirstPersonCameraController'

  #  A C++ Qt3DExtras::QFirstPersonCameraController Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QFirstPersonCameraController'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DExtras::QFirstPersonCameraController::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qfirstpersoncameracontroller.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DExtras::QFirstPersonCameraController::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras28QFirstPersonCameraController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::QFirstPersonCameraController::QFirstPersonCameraController(
    Qt3DCore::QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qfirstpersoncameracontroller.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::QFirstPersonCameraController::
    #      QFirstPersonCameraController(Qt3DCore::QNode *parent)
    self._noteCreation(QFirstPersonCameraController, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras28QFirstPersonCameraControllerC1EPN8Qt3DCore5'
        'QNodeE',
        self._addressOf(parent),
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

  @overload(Qt3DExtras.QAbstractCameraController.InputState, float)
  def moveCamera(
      self,
      state: Qt3DExtras.QAbstractCameraController.InputState,
      dt: float,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QFirstPersonCameraController::moveCamera(const
    QAbstractCameraController::InputState &state, float dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qfirstpersoncameracontroller.html

    Parameters
    ----------

    state : Qt3DExtras.QAbstractCameraController.InputState
      Passed on as a value: Qt reads the C++
      Qt3DExtras::QAbstractCameraController::InputState, which stays Python's
      own.

    dt : float
      Passed on as it is.
    """
    #  void Qt3DExtras::QFirstPersonCameraController::moveCamera(const
    #      QAbstractCameraController::InputState &state, float dt)
    ritual = (
        'ritual_ZN10Qt3DExtras28QFirstPersonCameraController10moveCameraERK'
        'NS_25QAbstractCameraController10InputStateEf')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DExtras28QFirstPersonCameraController10moveCam'
          'eraERKNS_25QAbstractCameraController10InputStateEf')
    self.uglySide.call(ritual, self._valueOf(state), dt)
