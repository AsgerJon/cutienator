"""
QSSGShaderFeatures binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderFeatures to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QSSGShaderFeatures(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderFeatures: a plain Python object standing in
  front of one C++ QSSGShaderFeatures.

  C++ hands a QSSGShaderFeatures around as a copy, so every C++
  QSSGShaderFeatures behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGShaderFeatures that has a ritual and that Python
  can call so far, 8 names in all: 'asDefineString', 'fromIndex', 'isNull',
  'isSet', 'set', '__eq__', 'disableTonemapping', '__rlshift__'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGShaderFeatures::~QSSGShaderFeatures()': the destructor: Python
    removes its C++ QSSGShaderFeatures by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGShaderFeatures is created at the first use, not by
    'QSSGShaderFeatures(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderFeatures back gives a copy the ritual made
    for Python, in a new cute QSSGShaderFeatures.
  """

  #  The enums Qt writes inside QSSGShaderFeatures, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Feature(CuteNum, scoped=True):
    """
    The enum 'QSSGShaderFeatures::Feature' of Qt, with the 22 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    LightProbe = Kee[int](256)
    IblOrientation = Kee[int](513)
    Ssm = Kee[int](1026)
    Ssao = Kee[int](2051)
    DepthPass = Kee[int](4100)
    OrthoShadowPass = Kee[int](8197)
    PerspectiveShadowPass = Kee[int](16390)
    LinearTonemapping = Kee[int](32775)
    AcesTonemapping = Kee[int](65544)
    HejlDawsonTonemapping = Kee[int](131081)
    FilmicTonemapping = Kee[int](262154)
    RGBELightProbe = Kee[int](524299)
    OpaqueDepthPrePass = Kee[int](1048588)
    ReflectionProbe = Kee[int](2097165)
    ReduceMaxNumLights = Kee[int](4194318)
    Lightmap = Kee[int](8388623)
    DisableMultiView = Kee[int](16777232)
    ForceIblExposure = Kee[int](33554449)
    NormalPass = Kee[int](67108882)
    UserRenderPass = Kee[int](134217747)
    MotionVector = Kee[int](268435476)
    LastFeature = Kee[int](268435477)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(Feature)
  def asDefineString(feature: Feature) -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGShaderFeatures::asDefineString(QSSGShaderFeatures::Feature
    feature)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderfeatures.html#asDefineString

    Parameters
    ----------

    feature : Feature
      Passed on as its number.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QSSGShaderFeatures::asDefineString(QSSGShaderFeatures::Feature
    #      feature)
    chars = Rituals.call(
        'ritual_ZN18QSSGShaderFeatures14asDefineStringENS_7FeatureE',
        feature.value,
    )
    return None if chars is None else chars.decode()

  @staticmethod
  @overload(int)
  def fromIndex(idx: int) -> Feature:
    """
    Calls Qt's 'Feature QSSGShaderFeatures::fromIndex(quint32 idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgshaderfeatures.html#fromIndex

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Feature
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Feature(number)' gives.
    """
    #  Feature QSSGShaderFeatures::fromIndex(quint32 idx)
    return QSSGShaderFeatures.Feature(Rituals.call(
        'ritual_ZN18QSSGShaderFeatures9fromIndexEj', idx,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderFeatures'

  #  Qt's '~QSSGShaderFeatures()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGShaderFeatures behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSSGShaderFeaturesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QSSGShaderFeatures::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgshaderfeatures.html#isNull
    """
    #  bool QSSGShaderFeatures::isNull() const
    return self.uglySide.call('ritual_ZNK18QSSGShaderFeatures6isNullEv')

  @overload(Feature)
  def isSet(self, feature: Feature) -> bool:
    """
    Calls Qt's 'bool QSSGShaderFeatures::isSet(Feature feature) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgshaderfeatures.html#isSet

    Parameters
    ----------

    feature : Feature
      Passed on as its number.
    """
    #  bool QSSGShaderFeatures::isSet(Feature feature) const
    return self.uglySide.call(
        'ritual_ZNK18QSSGShaderFeatures5isSetENS_7FeatureE', feature.value,
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

  @overload(THIS)
  def __eq__(self, b: QSSGShaderFeatures) -> bool:
    """
    Calls Qt's 'bool operator==(QSSGShaderFeatures a, QSSGShaderFeatures b)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgshaderfeatures.html#operator==

    Parameters
    ----------

    b : QSSGShaderFeatures
      Passed on as a value: Qt reads the C++ QSSGShaderFeatures, which stays
      Python's own.
    """
    #  bool operator==(QSSGShaderFeatures a, QSSGShaderFeatures b)
    return Rituals.call(
        'ritual_Zeq18QSSGShaderFeaturesS_',
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

  @overload(QDebug)
  def __rlshift__(self, stream: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug stream, const QSSGShaderFeatures
    &features)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgshaderfeatures.html#operator<<

    Parameters
    ----------

    stream : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug stream, const QSSGShaderFeatures &features)
    address = Rituals.call(
        'ritual_Zls6QDebugRK18QSSGShaderFeatures',
        CuteMixin._valueOf(stream), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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

  @overload(Feature, bool)
  def set(self, feature: Feature, val: bool) -> None:
    """
    Calls Qt's 'void QSSGShaderFeatures::set(Feature feature, bool val)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgshaderfeatures.html#set

    Parameters
    ----------

    feature : Feature
      Passed on as its number.

    val : bool
      Passed on as it is.
    """
    #  void QSSGShaderFeatures::set(Feature feature, bool val)
    self.uglySide.call(
        'ritual_ZN18QSSGShaderFeatures3setENS_7FeatureEb',
        feature.value, val,
    )

  def disableTonemapping(self) -> None:
    """
    Calls Qt's 'void QSSGShaderFeatures::disableTonemapping()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderfeatures.html#disableTonemapping
    """
    #  void QSSGShaderFeatures::disableTonemapping()
    self.uglySide.call('ritual_ZN18QSSGShaderFeatures18disableTonemappingEv')
