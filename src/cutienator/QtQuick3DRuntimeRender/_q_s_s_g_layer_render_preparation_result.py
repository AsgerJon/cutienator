"""
QSSGLayerRenderPreparationResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGLayerRenderPreparationResult to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QSize
  from . import QSSGLayerRenderPreparationResultFlags, QSSGRenderLayer


class QSSGLayerRenderPreparationResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGLayerRenderPreparationResult: a plain Python
  object standing in front of one C++ QSSGLayerRenderPreparationResult.

  C++ hands a QSSGLayerRenderPreparationResult around as a copy, so every C++
  QSSGLayerRenderPreparationResult behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGLayerRenderPreparationResult that has a ritual
  and that Python can call so far, 8 names in all: 'setState', 'getState',
  'isNull', 'isLayerVisible', 'textureDimensions', 'getViewport', 'getFlags',
  'getLayer'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QSSGLayerRenderPreparationResult::QSSGLayerRenderPreparationResult(const
    QRectF &inViewport, QSSGRenderLayer &inLayer)': takes a type Python has
    no way to hand over yet.
  - Qt's
    'QSSGLayerRenderPreparationResult::~QSSGLayerRenderPreparationResult()':
    the destructor: Python removes its C++ QSSGLayerRenderPreparationResult
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGLayerRenderPreparationResult is created at the first use, not
    by 'QSSGLayerRenderPreparationResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGLayerRenderPreparationResult back gives a copy
    the ritual made for Python, in a new cute
    QSSGLayerRenderPreparationResult.
  """

  #  The enums Qt writes inside QSSGLayerRenderPreparationResult, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class State(CuteNum, scoped=True):
    """
    The enum 'QSSGLayerRenderPreparationResult::State' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Null = Kee[int](0)
    DataPrep = Kee[int](1)
    Done = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGLayerRenderPreparationResult'

  #  Qt's '~QSSGLayerRenderPreparationResult()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGLayerRenderPreparationResult behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN32QSSGLayerRenderPreparationResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getState(self) -> State:
    """
    Calls Qt's 'State QSSGLayerRenderPreparationResult::getState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresult.html#getState

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QSSGLayerRenderPreparationResult::getState() const
    return QSSGLayerRenderPreparationResult.State(self.uglySide.call(
        'ritual_ZNK32QSSGLayerRenderPreparationResult8getStateEv',
    ))

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSSGLayerRenderPreparationResult::isNull() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresult.html#isNull
    """
    #  bool QSSGLayerRenderPreparationResult::isNull() const
    return self.uglySide.call(
        'ritual_ZNK32QSSGLayerRenderPreparationResult6isNullEv',
    )

  def isLayerVisible(self) -> bool:
    """
    Calls Qt's 'bool QSSGLayerRenderPreparationResult::isLayerVisible()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresult.html
    """
    #  bool QSSGLayerRenderPreparationResult::isLayerVisible() const
    return self.uglySide.call(
        'ritual_ZNK32QSSGLayerRenderPreparationResult14isLayerVisibleEv',
    )

  def textureDimensions(self) -> QSize:
    """
    Calls Qt's 'QSize QSSGLayerRenderPreparationResult::textureDimensions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresult.html

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSSGLayerRenderPreparationResult::textureDimensions() const
    address = self.uglySide.call(
        'ritual_ZNK32QSSGLayerRenderPreparationResult17textureDimensionsEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def getViewport(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSSGLayerRenderPreparationResult::getViewport()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresult.html#getViewport

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSSGLayerRenderPreparationResult::getViewport() const
    address = self.uglySide.call(
        'ritual_ZNK32QSSGLayerRenderPreparationResult11getViewportEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def getFlags(self) -> QSSGLayerRenderPreparationResultFlags:
    """
    Calls Qt's 'const QSSGLayerRenderPreparationResultFlags
    &QSSGLayerRenderPreparationResult::getFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresult.html#getFlags

    Returns
    -------

    QSSGLayerRenderPreparationResultFlags
      A new cute QSSGLayerRenderPreparationResultFlags around the copy Qt
      gave back. Python owns it.
    """
    #  const QSSGLayerRenderPreparationResultFlags
    #      &QSSGLayerRenderPreparationResult::getFlags() const
    address = self.uglySide.call(
        'ritual_ZNK32QSSGLayerRenderPreparationResult8getFlagsEv',
    )
    from . import QSSGLayerRenderPreparationResultFlags
    return QSSGLayerRenderPreparationResultFlags._cuteOwning(address)

  def getLayer(self) -> Optional[QSSGRenderLayer]:
    """
    Calls Qt's 'QSSGRenderLayer *QSSGLayerRenderPreparationResult::getLayer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresult.html#getLayer

    Returns
    -------

    Optional[QSSGRenderLayer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderLayer *QSSGLayerRenderPreparationResult::getLayer() const
    address = self.uglySide.call(
        'ritual_ZNK32QSSGLayerRenderPreparationResult8getLayerEv',
    )
    from . import QSSGRenderLayer
    return QSSGRenderLayer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(State)
  def setState(self, state: State) -> None:
    """
    Calls Qt's 'void QSSGLayerRenderPreparationResult::setState(State
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresult.html#setState

    Parameters
    ----------

    state : State
      Passed on as its number.
    """
    #  void QSSGLayerRenderPreparationResult::setState(State state)
    self.uglySide.call(
        'ritual_ZN32QSSGLayerRenderPreparationResult8setStateENS_5StateE',
        state.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGLayerRenderPreparationResult::QSSGLayerRenderPreparationResult()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssglayerrenderpreparationresult.html
    """
    #  QSSGLayerRenderPreparationResult::QSSGLayerRenderPreparationResult()
    self._noteCreation(
        QSSGLayerRenderPreparationResult, lambda: Rituals.call(
            'ritual_ZN32QSSGLayerRenderPreparationResultC1Ev',
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
