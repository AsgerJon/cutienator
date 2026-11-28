"""
QSGCompressedAtlasTexture::Atlas binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgcompressedatlastexture_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGCompressedAtlasTexture::Atlas to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGRhiAtlasTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QRhiResourceUpdateBatch
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Atlas(QSGRhiAtlasTexture.AtlasBase):
  """
  The cute side of Qt's QSGCompressedAtlasTexture::Atlas: a plain Python
  object standing in front of one C++ QSGCompressedAtlasTexture::Atlas.

  It is built on the cute 'QSGRhiAtlasTexture::AtlasBase', as Qt's
  QSGCompressedAtlasTexture::Atlas is built on Qt's
  QSGRhiAtlasTexture::AtlasBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGCompressedAtlasTexture::Atlas that has a ritual
  and that Python can call so far, 3 names in all: 'generateTexture',
  'enqueueTextureUpload', 'format'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGCompressedAtlasTexture::Atlas::~Atlas()': the destructor: Python
    never removes a C++ QSGCompressedAtlasTexture::Atlas.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 1 leans on 'QSGRhiAtlasTexture; 1 leans
  on 'vtable for QSGCompressedAtlasTexture.

  What to expect
  --------------

  - The C++ QSGCompressedAtlasTexture::Atlas is created at the first use, not
    by 'QSGCompressedAtlasTexture::Atlas(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGCompressedAtlasTexture::Atlas.
  - Qt tells when it has removed the C++ QSGCompressedAtlasTexture::Atlas.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGCompressedAtlasTexture::Atlas that has no cute
    function yet, '__init__', 'create', holds a function that raises
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
  __qt_class__ = 'QSGCompressedAtlasTexture::Atlas'

  #  A C++ QSGCompressedAtlasTexture::Atlas Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGCompressedAtlasTexture_Atlas'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> int:
    """
    Calls Qt's 'uint QSGCompressedAtlasTexture::Atlas::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-atlas.html#format
    """
    #  uint QSGCompressedAtlasTexture::Atlas::format() const
    return self.uglySide.call(
        'ritual_ZNK25QSGCompressedAtlasTexture5Atlas6formatEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSGCompressedAtlasTexture::Atlas::Atlas(QSGDefaultRenderContext
    *rc, const QSize &size, uint format)': leans on
    'QSGRhiAtlasTexture::AtlasBase::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGCompressedAtlasTexture.Atlas.__init__' has no cute function "
        "yet. Qt's "
        "'QSGCompressedAtlasTexture::Atlas::Atlas(QSGDefaultRenderContext "
        "*rc, const QSize &size, uint format)': leans on "
        "'QSGRhiAtlasTexture::AtlasBase::qt_metacall(QMetaObject::Call, "
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

  def generateTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGCompressedAtlasTexture::Atlas::generateTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-atlas.html
    """
    #  bool QSGCompressedAtlasTexture::Atlas::generateTexture()
    return self.uglySide.call(
        'ritual_ZN25QSGCompressedAtlasTexture5Atlas15generateTextureEv',
    )

  @overload(WAIT['QSGRhiAtlasTexture.TextureBase'], QRhiResourceUpdateBatch)
  @overload(WAIT['QSGRhiAtlasTexture.TextureBase'], NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def enqueueTextureUpload(
      self,
      t: Optional[QSGRhiAtlasTexture.TextureBase],
      rcub: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QSGCompressedAtlasTexture::Atlas::enqueueTextureUpload(
    QSGRhiAtlasTexture::TextureBase *t, QRhiResourceUpdateBatch *rcub)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgcompressedatlastexture-atlas.html

    Parameters
    ----------

    t : Optional[QSGRhiAtlasTexture.TextureBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rcub : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGCompressedAtlasTexture::Atlas::enqueueTextureUpload(
    #      QSGRhiAtlasTexture::TextureBase *t, QRhiResourceUpdateBatch *rcub)
    self.uglySide.call(
        'ritual_ZN25QSGCompressedAtlasTexture5Atlas20enqueueTextureUploadEP'
        'N18QSGRhiAtlasTexture11TextureBaseEP23QRhiResourceUpdateBatch',
        self._addressOf(t), self._addressOf(rcub),
    )

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'Texture *QSGCompressedAtlasTexture::Atlas::create(QByteArrayView
    data, const QSize &size)': leans on 'vtable for
    QSGCompressedAtlasTexture::Texture', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGCompressedAtlasTexture.Atlas.create' has no cute function yet. "
        "Qt's 'Texture "
        "*QSGCompressedAtlasTexture::Atlas::create(QByteArrayView data, "
        "const QSize &size)': leans on 'vtable for "
        "QSGCompressedAtlasTexture::Texture', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
