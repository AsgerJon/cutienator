"""
QRhiViewport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QRhiViewport(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiViewport: a plain Python object standing in front
  of one C++ QRhiViewport.

  C++ hands a QRhiViewport around as a copy, so every C++ QRhiViewport behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiViewport that has a ritual and that Python can
  call so far, 7 names in all: 'setViewport', 'minDepth', 'setMinDepth',
  'maxDepth', 'setMaxDepth', '__eq__', '__ne__'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::array<float, 4> QRhiViewport::viewport() const': gives a type
    Python has no way to take yet.
  - Qt's 'QRhiViewport::~QRhiViewport()': the destructor: Python removes its
    C++ QRhiViewport by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QRhiViewport is created at the first use, not by
    'QRhiViewport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiViewport back gives a copy the ritual made for
    Python, in a new cute QRhiViewport.
  - Each name of Qt's QRhiViewport that has no cute function yet, 'viewport',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiViewport'

  #  Qt's '~QRhiViewport()'. Naming it makes this a value class: Python owns
  #  every C++ QRhiViewport behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QRhiViewportD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def minDepth(self) -> float:
    """
    Calls Qt's 'float QRhiViewport::minDepth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiviewport.html#minDepth
    """
    #  float QRhiViewport::minDepth() const
    return self.uglySide.call('ritual_ZNK12QRhiViewport8minDepthEv')

  def maxDepth(self) -> float:
    """
    Calls Qt's 'float QRhiViewport::maxDepth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiviewport.html#maxDepth
    """
    #  float QRhiViewport::maxDepth() const
    return self.uglySide.call('ritual_ZNK12QRhiViewport8maxDepthEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float, float, float)
  def setViewport(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QRhiViewport::setViewport(float x, float y, float w,
    float h)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiviewport.html#setViewport

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QRhiViewport::setViewport(float x, float y, float w, float h)
    self.uglySide.call(
        'ritual_ZN12QRhiViewport11setViewportEffff', x, y, w, h,
    )

  @overload(float)
  def setMinDepth(self, minDepth: float) -> None:
    """
    Calls Qt's 'void QRhiViewport::setMinDepth(float minDepth)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiviewport.html#setMinDepth

    Parameters
    ----------

    minDepth : float
      Passed on as it is.
    """
    #  void QRhiViewport::setMinDepth(float minDepth)
    self.uglySide.call('ritual_ZN12QRhiViewport11setMinDepthEf', minDepth)

  @overload(float)
  def setMaxDepth(self, maxDepth: float) -> None:
    """
    Calls Qt's 'void QRhiViewport::setMaxDepth(float maxDepth)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiviewport.html#setMaxDepth

    Parameters
    ----------

    maxDepth : float
      Passed on as it is.
    """
    #  void QRhiViewport::setMaxDepth(float maxDepth)
    self.uglySide.call('ritual_ZN12QRhiViewport11setMaxDepthEf', maxDepth)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QRhiViewport) -> bool:
    """
    Calls Qt's 'bool operator==(const QRhiViewport &a, const QRhiViewport
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiviewport.html#operator==

    Parameters
    ----------

    b : QRhiViewport
      Passed on as a value: Qt reads the C++ QRhiViewport, which stays
      Python's own.
    """
    #  bool operator==(const QRhiViewport &a, const QRhiViewport &b)
    return Rituals.call(
        'ritual_ZeqRK12QRhiViewportS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: QRhiViewport) -> bool:
    """
    Calls Qt's 'bool operator!=(const QRhiViewport &a, const QRhiViewport
    &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiviewport.html#operator!=

    Parameters
    ----------

    b : QRhiViewport
      Passed on as a value: Qt reads the C++ QRhiViewport, which stays
      Python's own.
    """
    #  bool operator!=(const QRhiViewport &a, const QRhiViewport &b)
    return Rituals.call(
        'ritual_ZneRK12QRhiViewportS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QRhiViewport::QRhiViewport()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhiviewport.html#QRhiViewport
    """
    #  QRhiViewport::QRhiViewport()
    self._noteCreation(QRhiViewport, lambda: Rituals.call(
        'ritual_ZN12QRhiViewportC1Ev',
    ))

  @overload(float, float, float, float)
  @overload(float, float, float, float, float)
  @overload(float, float, float, float, float, float)
  def __init__(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      minDepth: float = 0.0,
      maxDepth: float = 1.0,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRhiViewport::QRhiViewport(float x, float
    y, float w, float h, float minDepth, float maxDepth)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qrhiviewport.html#QRhiViewport

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    minDepth : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    maxDepth : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.
    """
    #  QRhiViewport::QRhiViewport(float x, float y, float w, float h, float
    #      minDepth, float maxDepth)
    self._noteCreation(QRhiViewport, lambda: Rituals.call(
        'ritual_ZN12QRhiViewportC1Effffff', x, y, w, h, minDepth, maxDepth,
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

  @staticmethod
  def viewport(*__, **_) -> Never:
    """
    Qt's 'std::array<float, 4> QRhiViewport::viewport() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QRhiViewport.viewport' has no cute function yet. Qt's "
        "'std::array<float, 4> QRhiViewport::viewport() const': gives a "
        "type Python has no way to take yet.")
