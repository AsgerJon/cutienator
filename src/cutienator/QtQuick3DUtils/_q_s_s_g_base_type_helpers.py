"""
QSSGBaseTypeHelpers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSSGBaseTypeHelpers to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QSSGRenderTextureFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QSSGBaseTypeHelpers(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGBaseTypeHelpers: a plain Python object standing
  in front of one C++ QSSGBaseTypeHelpers.

  C++ hands a QSSGBaseTypeHelpers around as a copy, so every C++
  QSSGBaseTypeHelpers behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGBaseTypeHelpers that has a ritual and that
  Python can call so far, 1 name in all: 'toString'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const char *QSSGBaseTypeHelpers::toString(QSSGRenderTextureCubeFace
    value)': names the enum 'QSSGRenderTextureCubeFace', whose class cannot
    be named here.
  - Qt's 'const char
    *QSSGBaseTypeHelpers::toString(QSSGRenderTextureTypeValue value)': names
    the enum 'QSSGRenderTextureTypeValue', whose class cannot be named here.
  - Qt's 'const char *QSSGBaseTypeHelpers::toString(QSSGDepthDrawMode
    value)': names the enum 'QSSGDepthDrawMode', whose class cannot be named
    here.
  - Qt's 'const char *QSSGBaseTypeHelpers::toString(QSSGRenderWinding
    value)': names the enum 'QSSGRenderWinding', whose class cannot be named
    here.
  - Qt's 'const char *QSSGBaseTypeHelpers::toString(QSSGCullFaceMode value)':
    names the enum 'QSSGCullFaceMode', whose class cannot be named here.
  - Qt's 'const char *QSSGBaseTypeHelpers::toString(QSSGRenderComponentType
    value)': names the enum 'QSSGRenderComponentType', whose class cannot be
    named here.
  - Qt's 'const char *QSSGBaseTypeHelpers::toString(QSSGRenderTextureCoordOp
    value)': names the enum 'QSSGRenderTextureCoordOp', whose class cannot be
    named here.
  - Qt's 'const char *QSSGBaseTypeHelpers::toString(QSSGRenderTextureFilterOp
    value)': names the enum 'QSSGRenderTextureFilterOp', whose class cannot
    be named here.
  - Qt's 'QByteArray QSSGBaseTypeHelpers::toString(QSSGRenderSamplerType
    value)': names the enum 'QSSGRenderSamplerType', whose class cannot be
    named here.
  - Qt's 'const char
    *QSSGBaseTypeHelpers::displayName(QSSGRenderTextureCubeFace face)': names
    the enum 'QSSGRenderTextureCubeFace', whose class cannot be named here.
  - Qt's 'size_t QSSGBaseTypeHelpers::getSizeOfType(QSSGRenderComponentType
    type)': names the enum 'QSSGRenderComponentType', whose class cannot be
    named here.
  - Qt's 'QSSGRenderTextureCubeFace
    QSSGBaseTypeHelpers::next(QSSGRenderTextureCubeFace face)': names the
    enum 'QSSGRenderTextureCubeFace', whose class cannot be named here.
  - Qt's 'QSSGRenderTextureCubeFace
    QSSGBaseTypeHelpers::prev(QSSGRenderTextureCubeFace face)': names the
    enum 'QSSGRenderTextureCubeFace', whose class cannot be named here.
  - Qt's 'QSSGRenderTextureCubeFaceT
    QSSGBaseTypeHelpers::indexOfCubeFace(QSSGRenderTextureCubeFace face)':
    names the enum 'QSSGRenderTextureCubeFace', whose class cannot be named
    here.
  - Qt's 'QSSGBaseTypeHelpers::~QSSGBaseTypeHelpers()': the destructor:
    Python removes its C++ QSSGBaseTypeHelpers by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGBaseTypeHelpers is created at the first use, not by
    'QSSGBaseTypeHelpers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGBaseTypeHelpers back gives a copy the ritual made
    for Python, in a new cute QSSGBaseTypeHelpers.
  - Each name of Qt's QSSGBaseTypeHelpers that has no cute function yet,
    'displayName', 'getSizeOfType', 'indexOfCubeFace', 'next', 'prev', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSSGRenderTextureFormat.Format)
  def toString(value: QSSGRenderTextureFormat.Format) -> Optional[str]:
    """
    Calls Qt's 'const char
    *QSSGBaseTypeHelpers::toString(QSSGRenderTextureFormat::Format value)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgbasetypehelpers.html#toString

    Parameters
    ----------

    value : QSSGRenderTextureFormat.Format
      Passed on as its number.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char
    #      *QSSGBaseTypeHelpers::toString(QSSGRenderTextureFormat::Format
    #      value)
    chars = Rituals.call(
        'ritual_ZN19QSSGBaseTypeHelpers8toStringEN23QSSGRenderTextureFormat'
        '6FormatE',
        value.value,
    )
    return None if chars is None else chars.decode()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGBaseTypeHelpers'

  #  Qt's '~QSSGBaseTypeHelpers()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGBaseTypeHelpers behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSSGBaseTypeHelpersD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGBaseTypeHelpers::QSSGBaseTypeHelpers()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgbasetypehelpers.html#QSSGBaseTypeHelpers
    """
    #  QSSGBaseTypeHelpers::QSSGBaseTypeHelpers()
    self._noteCreation(QSSGBaseTypeHelpers, lambda: Rituals.call(
        'ritual_ZN19QSSGBaseTypeHelpersC1Ev',
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
  def displayName(*__, **_) -> Never:
    """
    Qt's 'const char
    *QSSGBaseTypeHelpers::displayName(QSSGRenderTextureCubeFace face)': names
    the enum 'QSSGRenderTextureCubeFace', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGBaseTypeHelpers.displayName' has no cute function yet. Qt's "
        "'const char "
        "*QSSGBaseTypeHelpers::displayName(QSSGRenderTextureCubeFace "
        "face)': names the enum 'QSSGRenderTextureCubeFace', whose class "
        "cannot be named here.")

  @staticmethod
  def getSizeOfType(*__, **_) -> Never:
    """
    Qt's 'size_t QSSGBaseTypeHelpers::getSizeOfType(QSSGRenderComponentType
    type)': names the enum 'QSSGRenderComponentType', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QSSGBaseTypeHelpers.getSizeOfType' has no cute function yet. Qt's "
        "'size_t QSSGBaseTypeHelpers::getSizeOfType(QSSGRenderComponentType "
        "type)': names the enum 'QSSGRenderComponentType', whose class "
        "cannot be named here.")

  @staticmethod
  def indexOfCubeFace(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderTextureCubeFaceT
    QSSGBaseTypeHelpers::indexOfCubeFace(QSSGRenderTextureCubeFace face)':
    names the enum 'QSSGRenderTextureCubeFace', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QSSGBaseTypeHelpers.indexOfCubeFace' has no cute function yet. "
        "Qt's 'QSSGRenderTextureCubeFaceT "
        "QSSGBaseTypeHelpers::indexOfCubeFace(QSSGRenderTextureCubeFace "
        "face)': names the enum 'QSSGRenderTextureCubeFace', whose class "
        "cannot be named here.")

  @staticmethod
  def next(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderTextureCubeFace
    QSSGBaseTypeHelpers::next(QSSGRenderTextureCubeFace face)': names the
    enum 'QSSGRenderTextureCubeFace', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGBaseTypeHelpers.next' has no cute function yet. Qt's "
        "'QSSGRenderTextureCubeFace "
        "QSSGBaseTypeHelpers::next(QSSGRenderTextureCubeFace face)': names "
        "the enum 'QSSGRenderTextureCubeFace', whose class cannot be named "
        "here.")

  @staticmethod
  def prev(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderTextureCubeFace
    QSSGBaseTypeHelpers::prev(QSSGRenderTextureCubeFace face)': names the
    enum 'QSSGRenderTextureCubeFace', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGBaseTypeHelpers.prev' has no cute function yet. Qt's "
        "'QSSGRenderTextureCubeFace "
        "QSSGBaseTypeHelpers::prev(QSSGRenderTextureCubeFace face)': names "
        "the enum 'QSSGRenderTextureCubeFace', whose class cannot be named "
        "here.")
