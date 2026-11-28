"""
QQuick3DParticleShapeDataUtils binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleshapedatautils_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleShapeDataUtils to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQuick3DParticleShapeDataUtils(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DParticleShapeDataUtils: a plain Python object
  standing in front of one C++ QQuick3DParticleShapeDataUtils.

  C++ hands a QQuick3DParticleShapeDataUtils around as a copy, so every C++
  QQuick3DParticleShapeDataUtils behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QQuick3DParticleShapeDataUtils yet. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVariant
    QQuick3DParticleShapeDataUtils::readValue(QCborStreamReader &reader,
    QMetaType::Type type)': takes a type Python has no way to hand over yet.
  - Qt's 'QString
    QQuick3DParticleShapeDataUtils::readString(QCborStreamReader &reader)':
    takes a type Python has no way to hand over yet.
  - Qt's 'double QQuick3DParticleShapeDataUtils::readReal(QCborStreamReader
    &reader)': takes a type Python has no way to hand over yet.
  - Qt's 'int
    QQuick3DParticleShapeDataUtils::readShapeHeader(QCborStreamReader
    &reader)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QQuick3DParticleShapeDataUtils::writeShapeHeader(QCborStreamWriter
    &writer, int version)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuick3DParticleShapeDataUtils::writeValue(QCborStreamWriter
    &writer, const QVariant &value)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQuick3DParticleShapeDataUtils::~QQuick3DParticleShapeDataUtils()':
    the destructor: Python removes its C++ QQuick3DParticleShapeDataUtils by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuick3DParticleShapeDataUtils is created at the first use, not
    by 'QQuick3DParticleShapeDataUtils(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DParticleShapeDataUtils back gives a copy the
    ritual made for Python, in a new cute QQuick3DParticleShapeDataUtils.
  - Each name of Qt's QQuick3DParticleShapeDataUtils that has no cute
    function yet, 'readReal', 'readShapeHeader', 'readString', 'readValue',
    'writeShapeHeader', 'writeValue', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleShapeDataUtils'

  #  Qt's '~QQuick3DParticleShapeDataUtils()'. Naming it makes this a value
  #  class: Python owns every C++ QQuick3DParticleShapeDataUtils behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QQuick3DParticleShapeDataUtilsD1Ev'

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
  def readReal(*__, **_) -> Never:
    """
    Qt's 'double QQuick3DParticleShapeDataUtils::readReal(QCborStreamReader
    &reader)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleShapeDataUtils.readReal' has no cute function "
        "yet. Qt's 'double "
        "QQuick3DParticleShapeDataUtils::readReal(QCborStreamReader "
        "&reader)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def readShapeHeader(*__, **_) -> Never:
    """
    Qt's 'int
    QQuick3DParticleShapeDataUtils::readShapeHeader(QCborStreamReader
    &reader)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleShapeDataUtils.readShapeHeader' has no cute "
        "function yet. Qt's 'int "
        "QQuick3DParticleShapeDataUtils::readShapeHeader(QCborStreamReader "
        "&reader)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def readString(*__, **_) -> Never:
    """
    Qt's 'QString
    QQuick3DParticleShapeDataUtils::readString(QCborStreamReader &reader)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleShapeDataUtils.readString' has no cute function "
        "yet. Qt's 'QString "
        "QQuick3DParticleShapeDataUtils::readString(QCborStreamReader "
        "&reader)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def readValue(*__, **_) -> Never:
    """
    Qt's 'QVariant
    QQuick3DParticleShapeDataUtils::readValue(QCborStreamReader &reader,
    QMetaType::Type type)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleShapeDataUtils.readValue' has no cute function "
        "yet. Qt's 'QVariant "
        "QQuick3DParticleShapeDataUtils::readValue(QCborStreamReader "
        "&reader, QMetaType::Type type)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def writeShapeHeader(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DParticleShapeDataUtils::writeShapeHeader(QCborStreamWriter
    &writer, int version)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleShapeDataUtils.writeShapeHeader' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DParticleShapeDataUtils::writeShapeHeader(QCborStreamWriter "
        "&writer, int version)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def writeValue(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DParticleShapeDataUtils::writeValue(QCborStreamWriter
    &writer, const QVariant &value)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleShapeDataUtils.writeValue' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DParticleShapeDataUtils::writeValue(QCborStreamWriter "
        "&writer, const QVariant &value)': takes a type Python has no way "
        "to hand over yet.")
