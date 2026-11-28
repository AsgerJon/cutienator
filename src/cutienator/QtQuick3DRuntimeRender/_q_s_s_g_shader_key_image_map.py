"""
QSSGShaderKeyImageMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGShaderKeyImageMap to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGShaderKeyImageMap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGShaderKeyImageMap: a plain Python object standing
  in front of one C++ QSSGShaderKeyImageMap.

  C++ hands a QSSGShaderKeyImageMap around as a copy, so every C++
  QSSGShaderKeyImageMap behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGShaderKeyImageMap yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QSSGShaderKeyImageMap::getBitValue(ImageMapBits imageBit,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSSGShaderKeyImageMap::setBitValue(ImageMapBits imageBit, bool
    inValue, QSSGDataRef<quint32> inKeySet)': takes a type Python has no way
    to hand over yet.
  - Qt's 'bool QSSGShaderKeyImageMap::isEnabled(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyImageMap::setEnabled(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSSGShaderKeyImageMap::isEnvMap(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyImageMap::setEnvMap(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSSGShaderKeyImageMap::isLightProbe(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyImageMap::setLightProbe(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
  - Qt's 'bool
    QSSGShaderKeyImageMap::isIdentityTransform(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QSSGShaderKeyImageMap::setIdentityTransform(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSSGShaderKeyImageMap::isUsingUV1(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyImageMap::setUsesUV1(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSSGShaderKeyImageMap::isLinear(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyImageMap::setLinear(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
  - Qt's 'bool
    QSSGShaderKeyImageMap::isPreMultipliedAlpha(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QSSGShaderKeyImageMap::setPreMultipliedAlpha(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGShaderKeyImageMap::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'QSSGShaderKeyImageMap::~QSSGShaderKeyImageMap()': the destructor:
    Python removes its C++ QSSGShaderKeyImageMap by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGShaderKeyImageMap is created at the first use, not by
    'QSSGShaderKeyImageMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGShaderKeyImageMap back gives a copy the ritual
    made for Python, in a new cute QSSGShaderKeyImageMap.
  - Each name of Qt's QSSGShaderKeyImageMap that has no cute function yet,
    'getBitValue', 'isEnabled', 'isEnvMap', 'isIdentityTransform',
    'isLightProbe', 'isLinear', 'isPreMultipliedAlpha', 'isUsingUV1',
    'setBitValue', 'setEnabled', 'setEnvMap', 'setIdentityTransform',
    'setLightProbe', 'setLinear', 'setPreMultipliedAlpha', 'setUsesUV1',
    'toString', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QSSGShaderKeyImageMap, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ImageMapBits(CuteNum):
    """
    The enum 'QSSGShaderKeyImageMap::ImageMapBits' of Qt, with the 7 names Qt
    gives in it.
    """

    Enabled = Kee[int](1)
    EnvMap = Kee[int](2)
    LightProbe = Kee[int](4)
    Identity = Kee[int](8)
    UsesUV1 = Kee[int](16)
    Linear = Kee[int](32)
    PreMultipliedAlpha = Kee[int](64)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGShaderKeyImageMap'

  #  Qt's '~QSSGShaderKeyImageMap()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGShaderKeyImageMap behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QSSGShaderKeyImageMapD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(str)
  @overload(NoneType)
  def __init__(self, inName: Optional[str]) -> None:
    """
    Notes what was given, for Qt's
    'QSSGShaderKeyImageMap::QSSGShaderKeyImageMap(const char *inName)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgshaderkeyimagemap.html#QSSGShaderKeyImageMap

    Parameters
    ----------

    inName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QSSGShaderKeyImageMap::QSSGShaderKeyImageMap(const char *inName)
    self._noteCreation(QSSGShaderKeyImageMap, lambda: Rituals.call(
        'ritual_ZN21QSSGShaderKeyImageMapC1EPKc', self._bytesOf(inName),
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
  def getBitValue(*__, **_) -> Never:
    """
    Qt's 'bool QSSGShaderKeyImageMap::getBitValue(ImageMapBits imageBit,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.getBitValue' has no cute function yet. Qt's "
        "'bool QSSGShaderKeyImageMap::getBitValue(ImageMapBits imageBit, "
        "QSSGDataView<quint32> inKeySet) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def isEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QSSGShaderKeyImageMap::isEnabled(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.isEnabled' has no cute function yet. Qt's "
        "'bool QSSGShaderKeyImageMap::isEnabled(QSSGDataView<quint32> "
        "inKeySet) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def isEnvMap(*__, **_) -> Never:
    """
    Qt's 'bool QSSGShaderKeyImageMap::isEnvMap(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.isEnvMap' has no cute function yet. Qt's "
        "'bool QSSGShaderKeyImageMap::isEnvMap(QSSGDataView<quint32> "
        "inKeySet) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def isIdentityTransform(*__, **_) -> Never:
    """
    Qt's 'bool
    QSSGShaderKeyImageMap::isIdentityTransform(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.isIdentityTransform' has no cute function "
        "yet. Qt's 'bool "
        "QSSGShaderKeyImageMap::isIdentityTransform(QSSGDataView<quint32> "
        "inKeySet) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def isLightProbe(*__, **_) -> Never:
    """
    Qt's 'bool QSSGShaderKeyImageMap::isLightProbe(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.isLightProbe' has no cute function yet. "
        "Qt's 'bool "
        "QSSGShaderKeyImageMap::isLightProbe(QSSGDataView<quint32> "
        "inKeySet) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def isLinear(*__, **_) -> Never:
    """
    Qt's 'bool QSSGShaderKeyImageMap::isLinear(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.isLinear' has no cute function yet. Qt's "
        "'bool QSSGShaderKeyImageMap::isLinear(QSSGDataView<quint32> "
        "inKeySet) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def isPreMultipliedAlpha(*__, **_) -> Never:
    """
    Qt's 'bool
    QSSGShaderKeyImageMap::isPreMultipliedAlpha(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.isPreMultipliedAlpha' has no cute function "
        "yet. Qt's 'bool "
        "QSSGShaderKeyImageMap::isPreMultipliedAlpha(QSSGDataView<quint32> "
        "inKeySet) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def isUsingUV1(*__, **_) -> Never:
    """
    Qt's 'bool QSSGShaderKeyImageMap::isUsingUV1(QSSGDataView<quint32>
    inKeySet) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.isUsingUV1' has no cute function yet. Qt's "
        "'bool QSSGShaderKeyImageMap::isUsingUV1(QSSGDataView<quint32> "
        "inKeySet) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setBitValue(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyImageMap::setBitValue(ImageMapBits imageBit, bool
    inValue, QSSGDataRef<quint32> inKeySet)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.setBitValue' has no cute function yet. Qt's "
        "'void QSSGShaderKeyImageMap::setBitValue(ImageMapBits imageBit, "
        "bool inValue, QSSGDataRef<quint32> inKeySet)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setEnabled(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyImageMap::setEnabled(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.setEnabled' has no cute function yet. Qt's "
        "'void QSSGShaderKeyImageMap::setEnabled(QSSGDataRef<quint32> "
        "inKeySet, bool val)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setEnvMap(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyImageMap::setEnvMap(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.setEnvMap' has no cute function yet. Qt's "
        "'void QSSGShaderKeyImageMap::setEnvMap(QSSGDataRef<quint32> "
        "inKeySet, bool val)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setIdentityTransform(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGShaderKeyImageMap::setIdentityTransform(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.setIdentityTransform' has no cute function "
        "yet. Qt's 'void "
        "QSSGShaderKeyImageMap::setIdentityTransform(QSSGDataRef<quint32> "
        "inKeySet, bool val)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setLightProbe(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyImageMap::setLightProbe(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.setLightProbe' has no cute function yet. "
        "Qt's 'void "
        "QSSGShaderKeyImageMap::setLightProbe(QSSGDataRef<quint32> "
        "inKeySet, bool val)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setLinear(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyImageMap::setLinear(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.setLinear' has no cute function yet. Qt's "
        "'void QSSGShaderKeyImageMap::setLinear(QSSGDataRef<quint32> "
        "inKeySet, bool val)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setPreMultipliedAlpha(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGShaderKeyImageMap::setPreMultipliedAlpha(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.setPreMultipliedAlpha' has no cute function "
        "yet. Qt's 'void "
        "QSSGShaderKeyImageMap::setPreMultipliedAlpha(QSSGDataRef<quint32> "
        "inKeySet, bool val)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setUsesUV1(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyImageMap::setUsesUV1(QSSGDataRef<quint32>
    inKeySet, bool val)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.setUsesUV1' has no cute function yet. Qt's "
        "'void QSSGShaderKeyImageMap::setUsesUV1(QSSGDataRef<quint32> "
        "inKeySet, bool val)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'void QSSGShaderKeyImageMap::toString(QByteArray &ioStr,
    QSSGDataView<quint32> inKeySet) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSSGShaderKeyImageMap.toString' has no cute function yet. Qt's "
        "'void QSSGShaderKeyImageMap::toString(QByteArray &ioStr, "
        "QSSGDataView<quint32> inKeySet) const': takes a type Python has no "
        "way to hand over yet.")
