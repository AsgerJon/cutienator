"""
QRhiShaderStage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QShader


class QRhiShaderStage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiShaderStage: a plain Python object standing in
  front of one C++ QRhiShaderStage.

  C++ hands a QRhiShaderStage around as a copy, so every C++ QRhiShaderStage
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiShaderStage that has a ritual and that Python
  can call so far, 8 names in all: 'type', 'setType', 'shader', 'setShader',
  'shaderVariant', 'setShaderVariant', '__eq__', '__ne__'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiShaderStage::~QRhiShaderStage()': the destructor: Python
    removes its C++ QRhiShaderStage by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QRhiShaderStage is created at the first use, not by
    'QRhiShaderStage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiShaderStage back gives a copy the ritual made for
    Python, in a new cute QRhiShaderStage.
  """

  #  The enums Qt writes inside QRhiShaderStage, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QRhiShaderStage::Type' of Qt, with the 6 names Qt gives in it.
    """

    Vertex = Kee[int](0)
    TessellationControl = Kee[int](1)
    TessellationEvaluation = Kee[int](2)
    Geometry = Kee[int](3)
    Fragment = Kee[int](4)
    Compute = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiShaderStage'

  #  Qt's '~QRhiShaderStage()'. Naming it makes this a value class: Python
  #  owns every C++ QRhiShaderStage behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QRhiShaderStageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Type:
    """
    Calls Qt's 'Type QRhiShaderStage::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhishaderstage.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QRhiShaderStage::type() const
    return QRhiShaderStage.Type(self.uglySide.call(
        'ritual_ZNK15QRhiShaderStage4typeEv',
    ))

  def shader(self) -> QShader:
    """
    Calls Qt's 'QShader QRhiShaderStage::shader() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhishaderstage.html#shader

    Returns
    -------

    QShader
      A new cute QShader around the copy Qt gave back. Python owns it.
    """
    #  QShader QRhiShaderStage::shader() const
    address = self.uglySide.call('ritual_ZNK15QRhiShaderStage6shaderEv')
    return QShader._cuteOwning(address)

  def shaderVariant(self) -> QShader.Variant:
    """
    Calls Qt's 'QShader::Variant QRhiShaderStage::shaderVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhishaderstage.html#shaderVariant

    Returns
    -------

    QShader.Variant
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QShader.Variant(number)'
      gives.
    """
    #  QShader::Variant QRhiShaderStage::shaderVariant() const
    return QShader.Variant(self.uglySide.call(
        'ritual_ZNK15QRhiShaderStage13shaderVariantEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Type)
  def setType(self, t: Type) -> None:
    """
    Calls Qt's 'void QRhiShaderStage::setType(Type t)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhishaderstage.html#setType

    Parameters
    ----------

    t : Type
      Passed on as its number.
    """
    #  void QRhiShaderStage::setType(Type t)
    self.uglySide.call(
        'ritual_ZN15QRhiShaderStage7setTypeENS_4TypeE', t.value,
    )

  @overload(QShader)
  def setShader(self, s: QShader) -> None:
    """
    Calls Qt's 'void QRhiShaderStage::setShader(const QShader &s)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhishaderstage.html#setShader

    Parameters
    ----------

    s : QShader
      Passed on as a value: Qt reads the C++ QShader, which stays Python's
      own.
    """
    #  void QRhiShaderStage::setShader(const QShader &s)
    self.uglySide.call(
        'ritual_ZN15QRhiShaderStage9setShaderERK7QShader', self._valueOf(s),
    )

  @overload(QShader.Variant)
  def setShaderVariant(self, v: QShader.Variant) -> None:
    """
    Calls Qt's 'void QRhiShaderStage::setShaderVariant(QShader::Variant v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderstage.html#setShaderVariant

    Parameters
    ----------

    v : QShader.Variant
      Passed on as its number.
    """
    #  void QRhiShaderStage::setShaderVariant(QShader::Variant v)
    self.uglySide.call(
        'ritual_ZN15QRhiShaderStage16setShaderVariantEN7QShader7VariantE',
        v.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QRhiShaderStage) -> bool:
    """
    Calls Qt's 'bool operator==(const QRhiShaderStage &a, const
    QRhiShaderStage &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhishaderstage.html#operator==

    Parameters
    ----------

    b : QRhiShaderStage
      Passed on as a value: Qt reads the C++ QRhiShaderStage, which stays
      Python's own.
    """
    #  bool operator==(const QRhiShaderStage &a, const QRhiShaderStage &b)
    return Rituals.call(
        'ritual_ZeqRK15QRhiShaderStageS1_',
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
  def __ne__(self, b: QRhiShaderStage) -> bool:
    """
    Calls Qt's 'bool operator!=(const QRhiShaderStage &a, const
    QRhiShaderStage &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhishaderstage.html#operator!=

    Parameters
    ----------

    b : QRhiShaderStage
      Passed on as a value: Qt reads the C++ QRhiShaderStage, which stays
      Python's own.
    """
    #  bool operator!=(const QRhiShaderStage &a, const QRhiShaderStage &b)
    return Rituals.call(
        'ritual_ZneRK15QRhiShaderStageS1_',
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
    Notes what was given, for Qt's 'QRhiShaderStage::QRhiShaderStage()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderstage.html#QRhiShaderStage
    """
    #  QRhiShaderStage::QRhiShaderStage()
    self._noteCreation(QRhiShaderStage, lambda: Rituals.call(
        'ritual_ZN15QRhiShaderStageC1Ev',
    ))

  @overload(Type, QShader)
  @overload(Type, QShader, QShader.Variant)
  def __init__(
      self,
      type: Type,
      shader: QShader,
      v: QShader.Variant = QShader.Variant.StandardShader,
  ) -> None:
    """
    Notes what was given, for Qt's 'QRhiShaderStage::QRhiShaderStage(Type
    type, const QShader &shader, QShader::Variant v)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishaderstage.html#QRhiShaderStage

    Parameters
    ----------

    type : Type
      Passed on as its number.

    shader : QShader
      Passed on as a value: Qt reads the C++ QShader, which stays Python's
      own.

    v : QShader.Variant
      Passed on as its number. May be left out, as in Qt: it is then
      QShader.Variant.StandardShader.
    """
    #  QRhiShaderStage::QRhiShaderStage(Type type, const QShader &shader,
    #      QShader::Variant v)
    self._noteCreation(QRhiShaderStage, lambda: Rituals.call(
        'ritual_ZN15QRhiShaderStageC1ENS_4TypeERK7QShaderNS1_7VariantE',
        type.value, self._valueOf(shader), v.value,
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
