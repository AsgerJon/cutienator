"""
UserRenderPass binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means UserRenderPass to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QSSGRenderPass

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class UserRenderPass(QSSGRenderPass):
  """
  The cute side of Qt's UserRenderPass: a plain Python object standing in
  front of one C++ UserRenderPass.

  It is built on the cute 'QSSGRenderPass', as Qt's UserRenderPass is built
  on Qt's QSSGRenderPass, and has everything that class has.

  C++ hands a UserRenderPass around as a copy, so every C++ UserRenderPass
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's UserRenderPass that has a ritual and that Python can
  call so far, 2 names in all: 'passType', 'hasData'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'UserRenderPass::~UserRenderPass()': the destructor: Python removes
    its C++ UserRenderPass by it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 9 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'UserRenderPass.

  What to expect
  --------------

  - The C++ UserRenderPass is created at the first use, not by
    'UserRenderPass(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a UserRenderPass back gives a copy the ritual made for
    Python, in a new cute UserRenderPass.
  - Each name of Qt's UserRenderPass that has no cute function yet,
    'preparePassImpl', 'prepareSubPass', 'prepareTopLevelPass', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'UserRenderPass'

  #  Qt's '~UserRenderPass()'. Naming it makes this a value class: Python
  #  owns every C++ UserRenderPass behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14UserRenderPassD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def passType(self) -> QSSGRenderPass.Type:
    """
    Calls Qt's 'Type UserRenderPass::passType() const'.

    Qt's own words: https://doc.qt.io/qt-6/userrenderpass.html#passType

    Returns
    -------

    QSSGRenderPass.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderPass.Type(number)' gives.
    """
    #  Type UserRenderPass::passType() const
    return QSSGRenderPass.Type(self.uglySide.call(
        'ritual_ZNK14UserRenderPass8passTypeEv',
    ))

  def hasData(self) -> bool:
    """
    Calls Qt's 'bool UserRenderPass::hasData() const'.

    Qt's own words: https://doc.qt.io/qt-6/userrenderpass.html#hasData
    """
    #  bool UserRenderPass::hasData() const
    return self.uglySide.call('ritual_ZNK14UserRenderPass7hasDataEv')

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
  def preparePassImpl(*__, **_) -> Never:
    """
    Qt's 'void UserRenderPass::preparePassImpl(QSSGRenderer &renderer,
    QSSGLayerRenderData &data, QSSGRenderUserPass *passNode,
    std::vector<UserPassData> &outData, QSSGRhiRenderableTextureV2Ptr
    renderableTexture)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'QSSGRenderContextInterface'.
    """
    raise NotImplementedError(
        "'UserRenderPass.preparePassImpl' has no cute function yet. Qt's "
        "'void UserRenderPass::preparePassImpl(QSSGRenderer &renderer, "
        "QSSGLayerRenderData &data, QSSGRenderUserPass *passNode, "
        "std::vector<UserPassData> &outData, QSSGRhiRenderableTextureV2Ptr "
        "renderableTexture)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QSSGRenderContextInterface'.")

  @staticmethod
  def prepareSubPass(*__, **_) -> Never:
    """
    Qt's 'void UserRenderPass::prepareSubPass(QSSGRenderer &renderer,
    QSSGLayerRenderData &data, QSSGRenderUserPass *subPassNode,
    std::vector<UserPassData> &subPassData, const
    QSSGRhiRenderableTextureV2Ptr &renderableTexture)': leans on
    'UserRenderPass::preparePassImpl(QSSGRenderer&, QSSGLayerRenderData&,
    QSSGRenderUserPass*, std::vector<UserRenderPass::UserPassData,
    std::allocator<UserRenderPass::UserPassData> >&,
    std::shared_ptr<QSSGRhiRenderableTextureV2>)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'UserRenderPass.prepareSubPass' has no cute function yet. Qt's "
        "'void UserRenderPass::prepareSubPass(QSSGRenderer &renderer, "
        "QSSGLayerRenderData &data, QSSGRenderUserPass *subPassNode, "
        "std::vector<UserPassData> &subPassData, const "
        "QSSGRhiRenderableTextureV2Ptr &renderableTexture)': leans on "
        "'UserRenderPass::preparePassImpl(QSSGRenderer&, "
        "QSSGLayerRenderData&, QSSGRenderUserPass*, "
        "std::vector<UserRenderPass::UserPassData, "
        "std::allocator<UserRenderPass::UserPassData> >&, "
        "std::shared_ptr<QSSGRhiRenderableTextureV2>)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def prepareTopLevelPass(*__, **_) -> Never:
    """
    Qt's 'void UserRenderPass::prepareTopLevelPass(QSSGRenderer &renderer,
    QSSGLayerRenderData &data, QSSGRenderUserPass *passNode)': leans on
    'UserRenderPass::preparePassImpl(QSSGRenderer&, QSSGLayerRenderData&,
    QSSGRenderUserPass*, std::vector<UserRenderPass::UserPassData,
    std::allocator<UserRenderPass::UserPassData> >&,
    std::shared_ptr<QSSGRhiRenderableTextureV2>)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'UserRenderPass.prepareTopLevelPass' has no cute function yet. "
        "Qt's 'void UserRenderPass::prepareTopLevelPass(QSSGRenderer "
        "&renderer, QSSGLayerRenderData &data, QSSGRenderUserPass "
        "*passNode)': leans on "
        "'UserRenderPass::preparePassImpl(QSSGRenderer&, "
        "QSSGLayerRenderData&, QSSGRenderUserPass*, "
        "std::vector<UserRenderPass::UserPassData, "
        "std::allocator<UserRenderPass::UserPassData> >&, "
        "std::shared_ptr<QSSGRhiRenderableTextureV2>)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
