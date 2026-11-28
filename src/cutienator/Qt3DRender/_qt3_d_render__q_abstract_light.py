"""
Qt3DRender::QAbstractLight binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qabstractlight.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractLight(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DRender::QAbstractLight: a plain Python object
  standing in front of one C++ Qt3DRender::QAbstractLight.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DRender::QAbstractLight is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QAbstractLight that has a ritual and
  that Python can call so far, 10 names in all: 'metaObject', 'tr', 'type',
  'color', 'intensity', 'setColor', 'setIntensity', 'colorChanged',
  'intensityChanged', 'd_func'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QAbstractLight::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QAbstractLight::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QAbstractLight::~QAbstractLight()': the destructor:
    Python never removes a C++ Qt3DRender::QAbstractLight.
  - Qt's 'Qt3DRender::QAbstractLight::QAbstractLight(QAbstractLightPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QAbstractLightPrivate *Qt3DRender::QAbstractLight::d_func()
    const': takes in Python what 'QAbstractLightPrivate
    *Qt3DRender::QAbstractLight::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QAbstractLight is created at the first use, not by
    'Qt3DRender::QAbstractLight(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QAbstractLight.
  - Qt tells when it has removed the C++ Qt3DRender::QAbstractLight. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QAbstractLight that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::QAbstractLight, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Type(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractLight::Type' of Qt, with the 3 names Qt
    gives in it.
    """

    PointLight = Kee[int](0)
    DirectionalLight = Kee[int](1)
    SpotLight = Kee[int](2)

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
    Calls Qt's 'QString Qt3DRender::QAbstractLight::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qabstractlight.html#tr

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
    #  QString Qt3DRender::QAbstractLight::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender14QAbstractLight2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QAbstractLight'

  #  A C++ Qt3DRender::QAbstractLight Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QAbstractLight'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QAbstractLight::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlight.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QAbstractLight::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QAbstractLight10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type Qt3DRender::QAbstractLight::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlight.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type Qt3DRender::QAbstractLight::type() const
    return QAbstractLight.Type(self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QAbstractLight4typeEv',
    ))

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor Qt3DRender::QAbstractLight::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlight.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor Qt3DRender::QAbstractLight::color() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QAbstractLight5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def intensity(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QAbstractLight::intensity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlight.html#intensity
    """
    #  float Qt3DRender::QAbstractLight::intensity() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QAbstractLight9intensityEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractLight::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlight.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DRender::QAbstractLight::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QAbstractLight8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setIntensity(self, intensity: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractLight::setIntensity(float
    intensity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlight.html#setIntensity

    Parameters
    ----------

    intensity : float
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractLight::setIntensity(float intensity)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QAbstractLight12setIntensityEf', intensity,
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
    Qt's 'Qt3DRender::QAbstractLight::QAbstractLight(QAbstractLightPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractLight.__init__' has no cute function yet. "
        "Qt's "
        "'Qt3DRender::QAbstractLight::QAbstractLight(QAbstractLightPrivate "
        "&dd, Qt3DCore::QNode *parent)': takes a type Python has no way to "
        "hand over yet.")

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

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractLight::colorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlight.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Qt3DRender::QAbstractLight::colorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QAbstractLight12colorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def intensityChanged(self, intensity: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractLight::intensityChanged(float
    intensity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlight.html#intensityChanged

    Parameters
    ----------

    intensity : float
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractLight::intensityChanged(float intensity)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QAbstractLight16intensityChangedEf',
        intensity,
    )

  def d_func(self) -> Optional[Qt3DRender.QAbstractLightPrivate]:
    """
    Calls Qt's 'QAbstractLightPrivate *Qt3DRender::QAbstractLight::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlight.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QAbstractLightPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractLightPrivate *Qt3DRender::QAbstractLight::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QAbstractLight6d_funcEv',
    )
    return Qt3DRender.QAbstractLightPrivate._cuteAt(address)
