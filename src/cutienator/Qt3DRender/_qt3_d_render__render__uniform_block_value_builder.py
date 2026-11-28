"""
Qt3DRender::Render::UniformBlockValueBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/uniformblockbuilder_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::UniformBlockValueBuilder to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class UniformBlockValueBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::UniformBlockValueBuilder: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::UniformBlockValueBuilder.

  C++ hands a Qt3DRender::Render::UniformBlockValueBuilder around as a copy,
  so every C++ Qt3DRender::Render::UniformBlockValueBuilder behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::UniformBlockValueBuilder that
  has a ritual and that Python can call so far, 2 names in all:
  'buildActiveUniformNameValueMapHelper',
  'buildActiveUniformNameValueMapStructHelper'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DRender::Render::UniformBlockValueBuilder::UniformBlockValueBuilder(
    const std::vector<int> &uniformNamesIds, ShaderDataManager
    *shaderDataManager, TextureManager *textureManager, const Matrix4x4
    &matrix)': takes a type Python has no way to hand over yet.
  - Qt's
    'Qt3DRender::Render::UniformBlockValueBuilder::~UniformBlockValueBuilder(
    )': the destructor: Python removes its C++
    Qt3DRender::Render::UniformBlockValueBuilder by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::UniformBlockValueBuilder is created at the
    first use, not by 'Qt3DRender::Render::UniformBlockValueBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::UniformBlockValueBuilder back
    gives a copy the ritual made for Python, in a new cute
    Qt3DRender::Render::UniformBlockValueBuilder.
  - Each name of Qt's Qt3DRender::Render::UniformBlockValueBuilder that has
    no cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::UniformBlockValueBuilder'

  #  Qt's '~Qt3DRender::Render::UniformBlockValueBuilder()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DRender::Render::UniformBlockValueBuilder behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender6Render24UniformBlockValueBuilderD1Ev')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'Qt3DRender::Render::UniformBlockValueBuilder::UniformBlockValueBuilder(
    const std::vector<int> &uniformNamesIds, ShaderDataManager
    *shaderDataManager, TextureManager *textureManager, const Matrix4x4
    &matrix)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.UniformBlockValueBuilder.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DRender::Render::UniformBlockValueBuilder::UniformBlockValueBui"
        "lder(const std::vector<int> &uniformNamesIds, ShaderDataManager "
        "*shaderDataManager, TextureManager *textureManager, const "
        "Matrix4x4 &matrix)': takes a type Python has no way to hand over "
        "yet.")

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

  @overload(
      WAIT['Qt3DRender.Render.ShaderData'], str, int, int,
      Qt3DRender.Render.ShaderData.PropertyValue,
  )
  @overload(WAIT['Qt3DRender.Render.ShaderData'], str, int, int, NoneType)
  @overload(
      NoneType, str, int, int, Qt3DRender.Render.ShaderData.PropertyValue,
  )
  @overload(NoneType, str, int, int, NoneType)
  def buildActiveUniformNameValueMapHelper(
      self,
      currentShaderData: Optional[Qt3DRender.Render.ShaderData],
      blockName: str,
      propertyInBlockNameId: int,
      propertyNameId: int,
      value: Optional[Qt3DRender.Render.ShaderData.PropertyValue],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::UniformBlockValueBuilder::
    buildActiveUniformNameValueMapHelper(const ShaderData *currentShaderData,
    const QString &blockName, const int propertyInBlockNameId, const int
    propertyNameId, const ShaderData::PropertyValue *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformblockvaluebuilder.html

    Parameters
    ----------

    currentShaderData : Optional[Qt3DRender.Render.ShaderData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    blockName : str
      Passed on as it is: a QString is made of it for the call.

    propertyInBlockNameId : int
      Passed on as it is.

    propertyNameId : int
      Passed on as it is.

    value : Optional[Qt3DRender.Render.ShaderData.PropertyValue]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::UniformBlockValueBuilder::
    #      buildActiveUniformNameValueMapHelper(const ShaderData
    #      *currentShaderData, const QString &blockName, const int
    #      propertyInBlockNameId, const int propertyNameId, const
    #      ShaderData::PropertyValue *value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render24UniformBlockValueBuilder36buildActiv'
        'eUniformNameValueMapHelperEPKNS0_10ShaderDataERK7QStringiiPKNS2_13'
        'PropertyValueE',
        self._addressOf(currentShaderData), blockName, propertyInBlockNameId,
        propertyNameId, self._addressOf(value),
    )

  @overload(WAIT['Qt3DRender.Render.ShaderData'], str)
  @overload(NoneType, str)
  @overload(WAIT['Qt3DRender.Render.ShaderData'], str, str)
  @overload(NoneType, str, str)
  def buildActiveUniformNameValueMapStructHelper(
      self,
      rShaderData: Optional[Qt3DRender.Render.ShaderData],
      blockName: str,
      qmlPropertyName: str = '',
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::UniformBlockValueBuilder::
    buildActiveUniformNameValueMapStructHelper(ShaderData *rShaderData, const
    QString &blockName, const QString &qmlPropertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-uniformblockvaluebuilder.html

    Parameters
    ----------

    rShaderData : Optional[Qt3DRender.Render.ShaderData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    blockName : str
      Passed on as it is: a QString is made of it for the call.

    qmlPropertyName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void Qt3DRender::Render::UniformBlockValueBuilder::
    #      buildActiveUniformNameValueMapStructHelper(ShaderData
    #      *rShaderData, const QString &blockName, const QString
    #      &qmlPropertyName)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render24UniformBlockValueBuilder42buildActiv'
        'eUniformNameValueMapStructHelperEPNS0_10ShaderDataERK7QStringS6_',
        self._addressOf(rShaderData), blockName, qmlPropertyName,
    )
