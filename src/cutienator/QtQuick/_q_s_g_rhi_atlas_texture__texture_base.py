"""
QSGRhiAtlasTexture::TextureBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGRhiAtlasTexture::TextureBase to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect
  from ..QtGui import QRhi, QRhiResourceUpdateBatch, QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class TextureBase(QSGTexture):
  """
  The cute side of Qt's QSGRhiAtlasTexture::TextureBase: a plain Python
  object standing in front of one C++ QSGRhiAtlasTexture::TextureBase.

  It is built on the cute 'QSGTexture', as Qt's
  QSGRhiAtlasTexture::TextureBase is built on Qt's QSGTexture, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRhiAtlasTexture::TextureBase that has a ritual
  and that Python can call so far, 6 names in all: 'metaObject',
  'comparisonKey', 'rhiTexture', 'commitTextureOperations', 'isAtlasTexture',
  'atlasSubRect'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGRhiAtlasTexture::TextureBase::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QSGRhiAtlasTexture::TextureBase::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGRhiAtlasTexture::TextureBase::~TextureBase()': the destructor:
    Python never removes a C++ QSGRhiAtlasTexture::TextureBase.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 2 leans on
  'QSGRhiAtlasTexture.

  What to expect
  --------------

  - The C++ QSGRhiAtlasTexture::TextureBase is created at the first use, not
    by 'QSGRhiAtlasTexture::TextureBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRhiAtlasTexture::TextureBase.
  - Qt tells when it has removed the C++ QSGRhiAtlasTexture::TextureBase.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGRhiAtlasTexture::TextureBase that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QSGRhiAtlasTexture::TextureBase'

  #  A C++ QSGRhiAtlasTexture::TextureBase Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRhiAtlasTexture_TextureBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QSGRhiAtlasTexture::TextureBase::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texturebase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGRhiAtlasTexture::TextureBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture11TextureBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def comparisonKey(self) -> int:
    """
    Calls Qt's 'qint64 QSGRhiAtlasTexture::TextureBase::comparisonKey()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texturebase.html#comparisonKey
    """
    #  qint64 QSGRhiAtlasTexture::TextureBase::comparisonKey() const
    ritual = 'ritual_ZNK18QSGRhiAtlasTexture11TextureBase13comparisonKeyEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QSGRhiAtlasTexture11TextureBase13comparisonKeyEv')
    return self.uglySide.call(ritual)

  def rhiTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSGRhiAtlasTexture::TextureBase::rhiTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texturebase.html#rhiTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSGRhiAtlasTexture::TextureBase::rhiTexture() const
    ritual = 'ritual_ZNK18QSGRhiAtlasTexture11TextureBase10rhiTextureEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QSGRhiAtlasTexture11TextureBase10rhiTextureEv')
    address = self.uglySide.call(ritual)
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def isAtlasTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texturebase.html#isAtlasTexture
    """
    #  bool QSGRhiAtlasTexture::TextureBase::isAtlasTexture() const
    ritual = 'ritual_ZNK18QSGRhiAtlasTexture11TextureBase14isAtlasTextureEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QSGRhiAtlasTexture11TextureBase14isAtlasTextureE'
          'v')
    return self.uglySide.call(ritual)

  def atlasSubRect(self) -> QRect:
    """
    Calls Qt's 'QRect QSGRhiAtlasTexture::TextureBase::atlasSubRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texturebase.html#atlasSubRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QSGRhiAtlasTexture::TextureBase::atlasSubRect() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture11TextureBase12atlasSubRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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
    Qt's 'QSGRhiAtlasTexture::TextureBase::TextureBase(AtlasBase *atlas,
    const QRect &textureRect)': leans on
    'QSGRhiAtlasTexture::TextureBase::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGRhiAtlasTexture.TextureBase.__init__' has no cute function "
        "yet. Qt's 'QSGRhiAtlasTexture::TextureBase::TextureBase(AtlasBase "
        "*atlas, const QRect &textureRect)': leans on "
        "'QSGRhiAtlasTexture::TextureBase::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  @overload(QRhi, QRhiResourceUpdateBatch)
  @overload(QRhi, NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def commitTextureOperations(
      self,
      rhi: Optional[QRhi],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void
    QSGRhiAtlasTexture::TextureBase::commitTextureOperations(QRhi *rhi,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-texturebase.html

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiAtlasTexture::TextureBase::commitTextureOperations(QRhi
    #      *rhi, QRhiResourceUpdateBatch *resourceUpdates)
    ritual = (
        'ritual_ZN18QSGRhiAtlasTexture11TextureBase23commitTextureOperation'
        'sEP4QRhiP23QRhiResourceUpdateBatch')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QSGRhiAtlasTexture11TextureBase23commitTextureOpe'
          'rationsEP4QRhiP23QRhiResourceUpdateBatch')
    self.uglySide.call(
        ritual, self._addressOf(rhi), self._addressOf(resourceUpdates),
    )
