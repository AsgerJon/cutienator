"""
QShader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qshader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray, QDebug
  from . import QShaderCode, QShaderDescription, QShaderKey
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QDebug = WAIT['QDebug']
  QShaderCode = WAIT['QShaderCode']
  QShaderDescription = WAIT['QShaderDescription']
  QShaderKey = WAIT['QShaderKey']


class QShader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QShader: a plain Python object standing in front of
  one C++ QShader.

  C++ hands a QShader around as a copy, so every C++ QShader behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QShader that has a ritual and that Python can call
  so far, 19 names in all: 'detach', 'isValid', 'stage', 'setStage',
  'description', 'setDescription', 'availableShaders', 'shader', 'setShader',
  'removeShader', 'serialized', 'fromSerialized', 'removeResourceBindingMap',
  'removeSeparateToCombinedImageSamplerMappingList', 'nativeShaderInfo',
  'setNativeShaderInfo', 'removeNativeShaderInfo', '__eq__', '__rlshift__'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QShader &QShader::operator=(const QShader &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QShader::QShader(QShader &&other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QShader &QShader::operator=(QShader &&other)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QShader::~QShader()': the destructor: Python removes its C++
    QShader by it, and has no other use for it.
  - Qt's 'void QShader::swap(QShader &other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'NativeResourceBindingMap QShader::nativeResourceBindingMap(const
    QShaderKey &key) const': gives a type Python has no way to take yet.
  - Qt's 'void QShader::setResourceBindingMap(const QShaderKey &key, const
    NativeResourceBindingMap &map)': takes a type Python has no way to hand
    over yet.
  - Qt's 'SeparateToCombinedImageSamplerMappingList
    QShader::separateToCombinedImageSamplerMappingList(const QShaderKey &key)
    const': gives a type Python has no way to take yet.
  - Qt's 'void QShader::setSeparateToCombinedImageSamplerMappingList(const
    QShaderKey &key, const SeparateToCombinedImageSamplerMappingList &list)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QShader is created at the first use, not by 'QShader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QShader back gives a copy the ritual made for Python,
    in a new cute QShader.
  - Each name of Qt's QShader that has no cute function yet,
    'nativeResourceBindingMap', 'separateToCombinedImageSamplerMappingList',
    'setResourceBindingMap', 'setSeparateToCombinedImageSamplerMappingList',
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QShader, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class SerializedFormatVersion(CuteNum, scoped=True):
    """
    The enum 'QShader::SerializedFormatVersion' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Latest = Kee[int](0)
    Qt_6_5 = Kee[int](1)
    Qt_6_4 = Kee[int](2)

  class Source(CuteNum):
    """The enum 'QShader::Source' of Qt, with the 8 names Qt gives in it."""

    SpirvShader = Kee[int](0)
    GlslShader = Kee[int](1)
    HlslShader = Kee[int](2)
    DxbcShader = Kee[int](3)
    MslShader = Kee[int](4)
    DxilShader = Kee[int](5)
    MetalLibShader = Kee[int](6)
    WgslShader = Kee[int](7)

  class Stage(CuteNum):
    """The enum 'QShader::Stage' of Qt, with the 6 names Qt gives in it."""

    VertexStage = Kee[int](0)
    TessellationControlStage = Kee[int](1)
    TessellationEvaluationStage = Kee[int](2)
    GeometryStage = Kee[int](3)
    FragmentStage = Kee[int](4)
    ComputeStage = Kee[int](5)

  class Variant(CuteNum):
    """The enum 'QShader::Variant' of Qt, with the 6 names Qt gives in it."""

    StandardShader = Kee[int](0)
    BatchableVertexShader = Kee[int](1)
    UInt16IndexedVertexAsComputeShader = Kee[int](2)
    UInt32IndexedVertexAsComputeShader = Kee[int](3)
    NonIndexedVertexAsComputeShader = Kee[int](4)
    HdrCapableFragmentShader = Kee[int](5)

  #  The classes Qt writes inside QShader, each a class in here as in C++.

  class NativeShaderInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QShader::NativeShaderInfo: a plain Python object
    standing in front of one C++ QShader::NativeShaderInfo.

    C++ hands a QShader::NativeShaderInfo around as a copy, so every C++
    QShader::NativeShaderInfo behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QShader::NativeShaderInfo yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QShader::NativeShaderInfo::~NativeShaderInfo()': the destructor:
      Python removes its C++ QShader::NativeShaderInfo by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QShader::NativeShaderInfo is created at the first use, not by
      'QShader::NativeShaderInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QShader::NativeShaderInfo back gives a copy the
      ritual made for Python, in a new cute QShader::NativeShaderInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QShader::NativeShaderInfo'

    #  Qt's '~QShader::NativeShaderInfo()'. Naming it makes this a value
    #  class: Python owns every C++ QShader::NativeShaderInfo behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN7QShader16NativeShaderInfoD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class SeparateToCombinedImageSamplerMapping(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QShader::SeparateToCombinedImageSamplerMapping: a
    plain Python object standing in front of one C++
    QShader::SeparateToCombinedImageSamplerMapping.

    C++ hands a QShader::SeparateToCombinedImageSamplerMapping around as a
    copy, so every C++ QShader::SeparateToCombinedImageSamplerMapping behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QShader::SeparateToCombinedImageSamplerMapping yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QShader::SeparateToCombinedImageSamplerMapping::
      ~SeparateToCombinedImageSamplerMapping()': the destructor: Python
      removes its C++ QShader::SeparateToCombinedImageSamplerMapping by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QShader::SeparateToCombinedImageSamplerMapping is created at
      the first use, not by
      'QShader::SeparateToCombinedImageSamplerMapping(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QShader::SeparateToCombinedImageSamplerMapping back
      gives a copy the ritual made for Python, in a new cute
      QShader::SeparateToCombinedImageSamplerMapping.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QShader::SeparateToCombinedImageSamplerMapping'

    #  Qt's '~QShader::SeparateToCombinedImageSamplerMapping()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QShader::SeparateToCombinedImageSamplerMapping behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN7QShader37SeparateToCombinedImageSamplerMappingD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray)
  def fromSerialized(data: QByteArray) -> QShader:
    """
    Calls Qt's 'QShader QShader::fromSerialized(const QByteArray &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#fromSerialized

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QShader
      A new cute QShader around the copy Qt gave back. Python owns it.
    """
    #  QShader QShader::fromSerialized(const QByteArray &data)
    address = Rituals.call(
        'ritual_ZN7QShader14fromSerializedERK10QByteArray',
        CuteMixin._valueOf(data),
    )
    return QShader._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShader'

  #  Qt's '~QShader()'. Naming it makes this a value class: Python owns every
  #  C++ QShader behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QShaderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QShader::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#isValid
    """
    #  bool QShader::isValid() const
    return self.uglySide.call('ritual_ZNK7QShader7isValidEv')

  def stage(self) -> Stage:
    """
    Calls Qt's 'Stage QShader::stage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#stage

    Returns
    -------

    Stage
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Stage(number)' gives.
    """
    #  Stage QShader::stage() const
    return QShader.Stage(self.uglySide.call('ritual_ZNK7QShader5stageEv'))

  def description(self) -> QShaderDescription:
    """
    Calls Qt's 'QShaderDescription QShader::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#description

    Returns
    -------

    QShaderDescription
      A new cute QShaderDescription around the copy Qt gave back. Python owns
      it.
    """
    #  QShaderDescription QShader::description() const
    address = self.uglySide.call('ritual_ZNK7QShader11descriptionEv')
    from . import QShaderDescription
    return QShaderDescription._cuteOwning(address)

  def availableShaders(self) -> QList[QShaderKey]:
    """
    Calls Qt's 'QList<QShaderKey> QShader::availableShaders() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#availableShaders

    Returns
    -------

    QList[QShaderKey]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QShaderKey> QShader::availableShaders() const
    address = self.uglySide.call('ritual_ZNK7QShader16availableShadersEv')
    from . import QShaderKey
    return QList[QShaderKey]._cuteOwning(address)

  @overload(QShaderKey)
  def shader(self, key: QShaderKey) -> QShaderCode:
    """
    Calls Qt's 'QShaderCode QShader::shader(const QShaderKey &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#shader

    Parameters
    ----------

    key : QShaderKey
      Passed on as a value: Qt reads the C++ QShaderKey, which stays Python's
      own.

    Returns
    -------

    QShaderCode
      A new cute QShaderCode around the copy Qt gave back. Python owns it.
    """
    #  QShaderCode QShader::shader(const QShaderKey &key) const
    address = self.uglySide.call(
        'ritual_ZNK7QShader6shaderERK10QShaderKey', self._valueOf(key),
    )
    from . import QShaderCode
    return QShaderCode._cuteOwning(address)

  @overload()
  @overload(SerializedFormatVersion)
  def serialized(
      self,
      version: SerializedFormatVersion = SerializedFormatVersion.Latest,
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QShader::serialized(SerializedFormatVersion
    version) const'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#serialized

    Parameters
    ----------

    version : SerializedFormatVersion
      Passed on as its number. May be left out, as in Qt: it is then
      SerializedFormatVersion.Latest.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QShader::serialized(SerializedFormatVersion version) const
    address = self.uglySide.call(
        'ritual_ZNK7QShader10serializedENS_23SerializedFormatVersionE',
        version.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QShaderKey)
  def nativeShaderInfo(self, key: QShaderKey) -> NativeShaderInfo:
    """
    Calls Qt's 'NativeShaderInfo QShader::nativeShaderInfo(const QShaderKey
    &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#nativeShaderInfo

    Parameters
    ----------

    key : QShaderKey
      Passed on as a value: Qt reads the C++ QShaderKey, which stays Python's
      own.

    Returns
    -------

    NativeShaderInfo
      A new cute QShader::NativeShaderInfo around the copy Qt gave back.
      Python owns it.
    """
    #  NativeShaderInfo QShader::nativeShaderInfo(const QShaderKey &key)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK7QShader16nativeShaderInfoERK10QShaderKey',
        self._valueOf(key),
    )
    return QShader.NativeShaderInfo._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Stage)
  def setStage(self, stage: Stage) -> None:
    """
    Calls Qt's 'void QShader::setStage(Stage stage)'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#setStage

    Parameters
    ----------

    stage : Stage
      Passed on as its number.
    """
    #  void QShader::setStage(Stage stage)
    self.uglySide.call('ritual_ZN7QShader8setStageENS_5StageE', stage.value)

  @overload(QShaderDescription)
  def setDescription(self, desc: QShaderDescription) -> None:
    """
    Calls Qt's 'void QShader::setDescription(const QShaderDescription
    &desc)'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#setDescription

    Parameters
    ----------

    desc : QShaderDescription
      Passed on as a value: Qt reads the C++ QShaderDescription, which stays
      Python's own.
    """
    #  void QShader::setDescription(const QShaderDescription &desc)
    self.uglySide.call(
        'ritual_ZN7QShader14setDescriptionERK18QShaderDescription',
        self._valueOf(desc),
    )

  @overload(QShaderKey, QShaderCode)
  def setShader(self, key: QShaderKey, shader: QShaderCode) -> None:
    """
    Calls Qt's 'void QShader::setShader(const QShaderKey &key, const
    QShaderCode &shader)'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#setShader

    Parameters
    ----------

    key : QShaderKey
      Passed on as a value: Qt reads the C++ QShaderKey, which stays Python's
      own.

    shader : QShaderCode
      Passed on as a value: Qt reads the C++ QShaderCode, which stays
      Python's own.
    """
    #  void QShader::setShader(const QShaderKey &key, const QShaderCode
    #      &shader)
    self.uglySide.call(
        'ritual_ZN7QShader9setShaderERK10QShaderKeyRK11QShaderCode',
        self._valueOf(key), self._valueOf(shader),
    )

  @overload(QShaderKey, NativeShaderInfo)
  def setNativeShaderInfo(
      self,
      key: QShaderKey,
      info: NativeShaderInfo,
  ) -> None:
    """
    Calls Qt's 'void QShader::setNativeShaderInfo(const QShaderKey &key,
    const NativeShaderInfo &info)'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#setNativeShaderInfo

    Parameters
    ----------

    key : QShaderKey
      Passed on as a value: Qt reads the C++ QShaderKey, which stays Python's
      own.

    info : NativeShaderInfo
      Passed on as a value: Qt reads the C++ QShader::NativeShaderInfo, which
      stays Python's own.
    """
    #  void QShader::setNativeShaderInfo(const QShaderKey &key, const
    #      NativeShaderInfo &info)
    self.uglySide.call(
        'ritual_ZN7QShader19setNativeShaderInfoERK10QShaderKeyRKNS_16Native'
        'ShaderInfoE',
        self._valueOf(key), self._valueOf(info),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, a1: QShader) -> bool:
    """
    Calls Qt's 'bool operator==(const QShader &a0, const QShader &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#operator==

    Parameters
    ----------

    a1 : QShader
      Passed on as a value: Qt reads the C++ QShader, which stays Python's
      own.
    """
    #  bool operator==(const QShader &a0, const QShader &a1)
    return Rituals.call(
        'ritual_ZeqRK7QShaderS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
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
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QShader &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QShader &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK7QShader',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QShader::QShader()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#QShader
    """
    #  QShader::QShader()
    self._noteCreation(QShader, lambda: Rituals.call(
        'ritual_ZN7QShaderC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QShader) -> None:
    """
    Notes what was given, for Qt's 'QShader::QShader(const QShader &other)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#QShader

    Parameters
    ----------

    other : QShader
      Passed on as a value: Qt reads the C++ QShader, which stays Python's
      own.
    """
    #  QShader::QShader(const QShader &other)
    self._noteCreation(QShader, lambda: Rituals.call(
        'ritual_ZN7QShaderC1ERKS_', self._valueOf(other),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QShader::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#detach
    """
    #  void QShader::detach()
    self.uglySide.call('ritual_ZN7QShader6detachEv')

  @overload(QShaderKey)
  def removeShader(self, key: QShaderKey) -> None:
    """
    Calls Qt's 'void QShader::removeShader(const QShaderKey &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qshader.html#removeShader

    Parameters
    ----------

    key : QShaderKey
      Passed on as a value: Qt reads the C++ QShaderKey, which stays Python's
      own.
    """
    #  void QShader::removeShader(const QShaderKey &key)
    self.uglySide.call(
        'ritual_ZN7QShader12removeShaderERK10QShaderKey', self._valueOf(key),
    )

  @overload(QShaderKey)
  def removeResourceBindingMap(self, key: QShaderKey) -> None:
    """
    Calls Qt's 'void QShader::removeResourceBindingMap(const QShaderKey
    &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshader.html#removeResourceBindingMap

    Parameters
    ----------

    key : QShaderKey
      Passed on as a value: Qt reads the C++ QShaderKey, which stays Python's
      own.
    """
    #  void QShader::removeResourceBindingMap(const QShaderKey &key)
    self.uglySide.call(
        'ritual_ZN7QShader24removeResourceBindingMapERK10QShaderKey',
        self._valueOf(key),
    )

  @overload(QShaderKey)
  def removeSeparateToCombinedImageSamplerMappingList(
      self,
      key: QShaderKey,
  ) -> None:
    """
    Calls Qt's 'void
    QShader::removeSeparateToCombinedImageSamplerMappingList(const QShaderKey
    &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshader.html

    Parameters
    ----------

    key : QShaderKey
      Passed on as a value: Qt reads the C++ QShaderKey, which stays Python's
      own.
    """
    #  void QShader::removeSeparateToCombinedImageSamplerMappingList(const
    #      QShaderKey &key)
    self.uglySide.call(
        'ritual_ZN7QShader47removeSeparateToCombinedImageSamplerMappingList'
        'ERK10QShaderKey',
        self._valueOf(key),
    )

  @overload(QShaderKey)
  def removeNativeShaderInfo(self, key: QShaderKey) -> None:
    """
    Calls Qt's 'void QShader::removeNativeShaderInfo(const QShaderKey &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qshader.html#removeNativeShaderInfo

    Parameters
    ----------

    key : QShaderKey
      Passed on as a value: Qt reads the C++ QShaderKey, which stays Python's
      own.
    """
    #  void QShader::removeNativeShaderInfo(const QShaderKey &key)
    self.uglySide.call(
        'ritual_ZN7QShader22removeNativeShaderInfoERK10QShaderKey',
        self._valueOf(key),
    )

  @staticmethod
  def nativeResourceBindingMap(*__, **_) -> Never:
    """
    Qt's 'NativeResourceBindingMap QShader::nativeResourceBindingMap(const
    QShaderKey &key) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShader.nativeResourceBindingMap' has no cute function yet. Qt's "
        "'NativeResourceBindingMap QShader::nativeResourceBindingMap(const "
        "QShaderKey &key) const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def separateToCombinedImageSamplerMappingList(*__, **_) -> Never:
    """
    Qt's 'SeparateToCombinedImageSamplerMappingList
    QShader::separateToCombinedImageSamplerMappingList(const QShaderKey &key)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QShader.separateToCombinedImageSamplerMappingList' has no cute "
        "function yet. Qt's 'SeparateToCombinedImageSamplerMappingList "
        "QShader::separateToCombinedImageSamplerMappingList(const "
        "QShaderKey &key) const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def setResourceBindingMap(*__, **_) -> Never:
    """
    Qt's 'void QShader::setResourceBindingMap(const QShaderKey &key, const
    NativeResourceBindingMap &map)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QShader.setResourceBindingMap' has no cute function yet. Qt's "
        "'void QShader::setResourceBindingMap(const QShaderKey &key, const "
        "NativeResourceBindingMap &map)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def setSeparateToCombinedImageSamplerMappingList(*__, **_) -> Never:
    """
    Qt's 'void QShader::setSeparateToCombinedImageSamplerMappingList(const
    QShaderKey &key, const SeparateToCombinedImageSamplerMappingList &list)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QShader.setSeparateToCombinedImageSamplerMappingList' has no cute "
        "function yet. Qt's 'void "
        "QShader::setSeparateToCombinedImageSamplerMappingList(const "
        "QShaderKey &key, const SeparateToCombinedImageSamplerMappingList "
        "&list)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QShader::swap(QShader &other)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QShader.swap' has no cute function yet. Qt's 'void "
        "QShader::swap(QShader &other)': takes a type Python has no way to "
        "hand over yet.")
