"""
QSSGRenderCameraFieldOfView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercamera_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderCameraFieldOfView to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderCameraFieldOfView(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderCameraFieldOfView: a plain Python object
  standing in front of one C++ QSSGRenderCameraFieldOfView.

  C++ hands a QSSGRenderCameraFieldOfView around as a copy, so every C++
  QSSGRenderCameraFieldOfView behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderCameraFieldOfView that has a ritual and
  that Python can call so far, 6 names in all: 'orientation', 'degrees',
  'radians', 'setDegrees', 'asVerticalFov', 'setRadians'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderCameraFieldOfView::QSSGRenderCameraFieldOfView(
    QSSGRenderCameraFieldOfView &&a0)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QSSGRenderCameraFieldOfView
    &QSSGRenderCameraFieldOfView::operator=(const QSSGRenderCameraFieldOfView
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QSSGRenderCameraFieldOfView::QSSGRenderCameraFieldOfView(float fov,
    FovValue value, Orientation angleOfView)': names the enum
    'QSSGRenderCameraFieldOfView::FovValue', whose class cannot be named
    here.
  - Qt's 'QSSGRenderCameraFieldOfView::~QSSGRenderCameraFieldOfView()': the
    destructor: Python removes its C++ QSSGRenderCameraFieldOfView by it, and
    has no other use for it.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QSSGRenderCameraFieldOfView is created at the first use, not by
    'QSSGRenderCameraFieldOfView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderCameraFieldOfView back gives a copy the
    ritual made for Python, in a new cute QSSGRenderCameraFieldOfView.
  - Each name of Qt's QSSGRenderCameraFieldOfView that has no cute function
    yet, 'fromDegrees', 'fromRadians', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderCameraFieldOfView, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Orientation(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderCameraFieldOfView::Orientation' of Qt, with the 2
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Vertical = Kee[int](0)
    Horizontal = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderCameraFieldOfView'

  #  Qt's '~QSSGRenderCameraFieldOfView()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGRenderCameraFieldOfView behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QSSGRenderCameraFieldOfViewD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def orientation(self) -> Orientation:
    """
    Calls Qt's 'Orientation QSSGRenderCameraFieldOfView::orientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamerafieldofview.html#orientation

    Returns
    -------

    Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Orientation(number)'
      gives.
    """
    #  Orientation QSSGRenderCameraFieldOfView::orientation() const
    return QSSGRenderCameraFieldOfView.Orientation(self.uglySide.call(
        'ritual_ZNK27QSSGRenderCameraFieldOfView11orientationEv',
    ))

  def degrees(self) -> float:
    """
    Calls Qt's 'float QSSGRenderCameraFieldOfView::degrees() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamerafieldofview.html#degrees
    """
    #  float QSSGRenderCameraFieldOfView::degrees() const
    return self.uglySide.call(
        'ritual_ZNK27QSSGRenderCameraFieldOfView7degreesEv',
    )

  def radians(self) -> float:
    """
    Calls Qt's 'float QSSGRenderCameraFieldOfView::radians() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamerafieldofview.html#radians
    """
    #  float QSSGRenderCameraFieldOfView::radians() const
    return self.uglySide.call(
        'ritual_ZNK27QSSGRenderCameraFieldOfView7radiansEv',
    )

  @overload(float)
  def asVerticalFov(self, aspectRatio: float) -> QSSGRenderCameraFieldOfView:
    """
    Calls Qt's 'QSSGRenderCameraFieldOfView
    QSSGRenderCameraFieldOfView::asVerticalFov(float aspectRatio) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamerafieldofview.html#asVerticalFov

    Parameters
    ----------

    aspectRatio : float
      Passed on as it is.

    Returns
    -------

    QSSGRenderCameraFieldOfView
      A new cute QSSGRenderCameraFieldOfView around the copy Qt gave back.
      Python owns it.
    """
    #  QSSGRenderCameraFieldOfView
    #      QSSGRenderCameraFieldOfView::asVerticalFov(float aspectRatio)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QSSGRenderCameraFieldOfView13asVerticalFovEf',
        aspectRatio,
    )
    return QSSGRenderCameraFieldOfView._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDegrees(self, fov: float) -> None:
    """
    Calls Qt's 'void QSSGRenderCameraFieldOfView::setDegrees(float fov)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamerafieldofview.html#setDegrees

    Parameters
    ----------

    fov : float
      Passed on as it is.
    """
    #  void QSSGRenderCameraFieldOfView::setDegrees(float fov)
    self.uglySide.call(
        'ritual_ZN27QSSGRenderCameraFieldOfView10setDegreesEf', fov,
    )

  @overload(float)
  def setRadians(self, fov: float) -> None:
    """
    Calls Qt's 'void QSSGRenderCameraFieldOfView::setRadians(float fov)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamerafieldofview.html#setRadians

    Parameters
    ----------

    fov : float
      Passed on as it is.
    """
    #  void QSSGRenderCameraFieldOfView::setRadians(float fov)
    self.uglySide.call(
        'ritual_ZN27QSSGRenderCameraFieldOfView10setRadiansEf', fov,
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
  @overload(Orientation)
  def __init__(
      self,
      orientation: Orientation = Orientation.Vertical,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderCameraFieldOfView::QSSGRenderCameraFieldOfView(Orientation
    orientation)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamerafieldofview.html

    Parameters
    ----------

    orientation : Orientation
      Passed on as its number. May be left out, as in Qt: it is then
      Orientation.Vertical.
    """
    #  QSSGRenderCameraFieldOfView::QSSGRenderCameraFieldOfView(Orientation
    #      orientation)
    self._noteCreation(QSSGRenderCameraFieldOfView, lambda: Rituals.call(
        'ritual_ZN27QSSGRenderCameraFieldOfViewC1ENS_11OrientationE',
        orientation.value,
    ))

  @overload(THIS)
  def __init__(self, a0: QSSGRenderCameraFieldOfView) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderCameraFieldOfView::QSSGRenderCameraFieldOfView(const
    QSSGRenderCameraFieldOfView &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamerafieldofview.html

    Parameters
    ----------

    a0 : QSSGRenderCameraFieldOfView
      Passed on as a value: Qt reads the C++ QSSGRenderCameraFieldOfView,
      which stays Python's own.
    """
    #  QSSGRenderCameraFieldOfView::QSSGRenderCameraFieldOfView(const
    #      QSSGRenderCameraFieldOfView &a0)
    self._noteCreation(QSSGRenderCameraFieldOfView, lambda: Rituals.call(
        'ritual_ZN27QSSGRenderCameraFieldOfViewC1ERKS_', self._valueOf(a0),
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
  def fromDegrees(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderCameraFieldOfView::fromDegrees': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QSSGRenderCameraFieldOfView.fromDegrees' has no cute function "
        "yet. Qt's 'QSSGRenderCameraFieldOfView::fromDegrees': a template: "
        "a pattern and no single function.")

  @staticmethod
  def fromRadians(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderCameraFieldOfView::fromRadians': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QSSGRenderCameraFieldOfView.fromRadians' has no cute function "
        "yet. Qt's 'QSSGRenderCameraFieldOfView::fromRadians': a template: "
        "a pattern and no single function.")
