"""
Qt3DRender::Render::UniformValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/uniform_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::UniformValue to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from ..QtGui import QMatrix4x4, QVector2D, QVector3D, QVector4D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QVariant = WAIT['QVariant']
  QVector2D = WAIT['QVector2D']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']


class UniformValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::UniformValue: a plain Python
  object standing in front of one C++ Qt3DRender::Render::UniformValue.

  C++ hands a Qt3DRender::Render::UniformValue around as a copy, so every C++
  Qt3DRender::Render::UniformValue behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::UniformValue that has a ritual
  and that Python can call so far, 8 names in all: 'valueType', 'storedType',
  'fromVariant', 'byteSize', 'elementCount', 'elementByteSize', '__eq__',
  '__ne__'. It can be made from Python, in 10 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::UniformValue::UniformValue(uint i)': takes in
    Python what 'Qt3DRender::Render::UniformValue::UniformValue(int i)'
    takes.
  - Qt's 'Qt3DRender::Render::UniformValue::UniformValue(double d)': takes in
    Python what 'Qt3DRender::Render::UniformValue::UniformValue(float f)'
    takes.
  - Qt's 'Qt3DRender::Render::UniformValue::UniformValue(const QMatrix3x3
    &mat33)': takes a type Python has no way to hand over yet.
  - Qt's 'Qt3DRender::Render::UniformValue::UniformValue(const
    QVector<QMatrix4x4> &v)': takes a type Python has no way to hand over
    yet.
  - Qt's 'Qt3DRender::Render::UniformValue::~UniformValue()': the destructor:
    Python removes its C++ Qt3DRender::Render::UniformValue by it, and has no
    other use for it.

  What has no ritual
  ------------------

  3 of the 26 functions Qt declares: 3 a template.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::UniformValue is created at the first use, not
    by 'Qt3DRender::Render::UniformValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::UniformValue back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::Render::UniformValue.
  - Each name of Qt's Qt3DRender::Render::UniformValue that has no cute
    function yet, 'constData', 'data', 'setData', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::Render::UniformValue, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class ValueType(CuteNum):
    """
    The enum 'Qt3DRender::Render::UniformValue::ValueType' of Qt, with the 5
    names Qt gives in it.
    """

    ScalarValue = Kee[int](0)
    NodeId = Kee[int](1)
    TextureValue = Kee[int](2)
    BufferValue = Kee[int](3)
    ShaderImageValue = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QVariant)
  def fromVariant(variant: QVariant) -> UniformValue:
    """
    Calls Qt's 'UniformValue
    Qt3DRender::Render::UniformValue::fromVariant(const QVariant &variant)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#fromVariant

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    UniformValue
      A new cute Qt3DRender::Render::UniformValue around the copy Qt gave
      back. Python owns it.
    """
    #  UniformValue Qt3DRender::Render::UniformValue::fromVariant(const
    #      QVariant &variant)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValue11fromVariantERK8QVarian'
        't',
        CuteMixin._valueOf(variant),
    )
    return UniformValue._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::UniformValue'

  #  Qt's '~Qt3DRender::Render::UniformValue()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DRender::Render::UniformValue behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render12UniformValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def valueType(self) -> ValueType:
    """
    Calls Qt's 'ValueType Qt3DRender::Render::UniformValue::valueType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#valueType

    Returns
    -------

    ValueType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ValueType(number)' gives.
    """
    #  ValueType Qt3DRender::Render::UniformValue::valueType() const
    return UniformValue.ValueType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12UniformValue9valueTypeEv',
    ))

  def storedType(self) -> Qt3DRender.Render.UniformType:
    """
    Calls Qt's 'UniformType Qt3DRender::Render::UniformValue::storedType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#storedType

    Returns
    -------

    Qt3DRender.Render.UniformType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.Render.UniformType(number)' gives.
    """
    #  UniformType Qt3DRender::Render::UniformValue::storedType() const
    return Qt3DRender.Render.UniformType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12UniformValue10storedTypeEv',
    ))

  def byteSize(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::UniformValue::byteSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#byteSize
    """
    #  int Qt3DRender::Render::UniformValue::byteSize() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12UniformValue8byteSizeEv',
    )

  def elementCount(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::UniformValue::elementCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#elementCount
    """
    #  int Qt3DRender::Render::UniformValue::elementCount() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12UniformValue12elementCountEv',
    )

  def elementByteSize(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::UniformValue::elementByteSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html
    """
    #  int Qt3DRender::Render::UniformValue::elementByteSize() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12UniformValue15elementByteSizeEv',
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
  def __eq__(self, other: UniformValue) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::UniformValue::operator==(const
    UniformValue &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#operator==

    Parameters
    ----------

    other : UniformValue
      Passed on as a value: Qt reads the C++
      Qt3DRender::Render::UniformValue, which stays Python's own.
    """
    #  bool Qt3DRender::Render::UniformValue::operator==(const UniformValue
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12UniformValueeqERKS1_',
        self._valueOf(other),
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
  def __ne__(self, other: UniformValue) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::UniformValue::operator!=(const
    UniformValue &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#operator!=

    Parameters
    ----------

    other : UniformValue
      Passed on as a value: Qt reads the C++
      Qt3DRender::Render::UniformValue, which stays Python's own.
    """
    #  bool Qt3DRender::Render::UniformValue::operator!=(const UniformValue
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12UniformValueneERKS1_',
        self._valueOf(other),
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
    Notes what was given, for Qt's
    'Qt3DRender::Render::UniformValue::UniformValue()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#UniformValue
    """
    #  Qt3DRender::Render::UniformValue::UniformValue()
    self._noteCreation(UniformValue, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValueC1Ev',
    ))

  @overload(int)
  def __init__(self, i: int) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::UniformValue::UniformValue(int i)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#UniformValue

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  Qt3DRender::Render::UniformValue::UniformValue(int i)
    self._noteCreation(UniformValue, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValueC1Ei', i,
    ))

  @overload(float)
  def __init__(self, f: float) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::UniformValue::UniformValue(float f)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#UniformValue

    Parameters
    ----------

    f : float
      Passed on as it is.
    """
    #  Qt3DRender::Render::UniformValue::UniformValue(float f)
    self._noteCreation(UniformValue, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValueC1Ef', f,
    ))

  @overload(bool)
  def __init__(self, b: bool) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::UniformValue::UniformValue(bool b)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#UniformValue

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  Qt3DRender::Render::UniformValue::UniformValue(bool b)
    self._noteCreation(UniformValue, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValueC1Eb', b,
    ))

  @overload(QVector2D)
  def __init__(self, vec2: QVector2D) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::UniformValue::UniformValue(const QVector2D &vec2)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#UniformValue

    Parameters
    ----------

    vec2 : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  Qt3DRender::Render::UniformValue::UniformValue(const QVector2D &vec2)
    self._noteCreation(UniformValue, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValueC1ERK9QVector2D',
        self._valueOf(vec2),
    ))

  @overload(QVector3D)
  def __init__(self, vec3: QVector3D) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::UniformValue::UniformValue(const Vector3D &vec3)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#UniformValue

    Parameters
    ----------

    vec3 : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  Qt3DRender::Render::UniformValue::UniformValue(const Vector3D &vec3)
    self._noteCreation(UniformValue, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValueC1ERK9QVector3D',
        self._valueOf(vec3),
    ))

  @overload(QVector4D)
  def __init__(self, vec4: QVector4D) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::UniformValue::UniformValue(const Vector4D &vec4)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#UniformValue

    Parameters
    ----------

    vec4 : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  Qt3DRender::Render::UniformValue::UniformValue(const Vector4D &vec4)
    self._noteCreation(UniformValue, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValueC1ERK9QVector4D',
        self._valueOf(vec4),
    ))

  @overload(QMatrix4x4)
  def __init__(self, mat44: QMatrix4x4) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::UniformValue::UniformValue(const QMatrix4x4
    &mat44)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#UniformValue

    Parameters
    ----------

    mat44 : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  Qt3DRender::Render::UniformValue::UniformValue(const QMatrix4x4
    #      &mat44)
    self._noteCreation(UniformValue, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValueC1ERK10QMatrix4x4',
        self._valueOf(mat44),
    ))

  @overload(int, ValueType)
  def __init__(self, byteSize: int, valueType: ValueType) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::UniformValue::UniformValue(int byteSize, ValueType
    valueType)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#UniformValue

    Parameters
    ----------

    byteSize : int
      Passed on as it is.

    valueType : ValueType
      Passed on as its number.
    """
    #  Qt3DRender::Render::UniformValue::UniformValue(int byteSize, ValueType
    #      valueType)
    self._noteCreation(UniformValue, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValueC1EiNS1_9ValueTypeE',
        byteSize, valueType.value,
    ))

  @overload(WAIT['Qt3DCore.QNodeId'])
  def __init__(self, id: Qt3DCore.QNodeId) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::UniformValue::UniformValue(Qt3DCore::QNodeId id)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformvalue.html#UniformValue

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  Qt3DRender::Render::UniformValue::UniformValue(Qt3DCore::QNodeId id)
    self._noteCreation(UniformValue, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12UniformValueC1EN8Qt3DCore7QNodeIdE',
        self._valueOf(id),
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
  def constData(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::UniformValue::constData': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.UniformValue.constData' has no cute function "
        "yet. Qt's 'Qt3DRender::Render::UniformValue::constData': a "
        "template: a pattern and no single function.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::UniformValue::data': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.UniformValue.data' has no cute function yet. "
        "Qt's 'Qt3DRender::Render::UniformValue::data': a template: a "
        "pattern and no single function.")

  @staticmethod
  def setData(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::UniformValue::setData': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.UniformValue.setData' has no cute function yet. "
        "Qt's 'Qt3DRender::Render::UniformValue::setData': a template: a "
        "pattern and no single function.")
