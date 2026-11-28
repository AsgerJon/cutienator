"""
QSGRhiAtlasTexture::AtlasBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGRhiAtlasTexture::AtlasBase to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import QSGRhiAtlasTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QRhi, QRhiResourceUpdateBatch, QRhiTexture
  from . import QSGDefaultRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class AtlasBase(QObject):
  """
  The cute side of Qt's QSGRhiAtlasTexture::AtlasBase: a plain Python object
  standing in front of one C++ QSGRhiAtlasTexture::AtlasBase.

  It is built on the cute 'QObject', as Qt's QSGRhiAtlasTexture::AtlasBase is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRhiAtlasTexture::AtlasBase that has a ritual and
  that Python can call so far, 10 names in all: 'metaObject', 'invalidate',
  'commitTextureOperations', 'remove', 'renderContext', 'rhi', 'texture',
  'size', 'generateTexture', 'enqueueTextureUpload'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGRhiAtlasTexture::AtlasBase::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QSGRhiAtlasTexture::AtlasBase::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSGRhiAtlasTexture::AtlasBase::~AtlasBase()': the destructor:
    Python never removes a C++ QSGRhiAtlasTexture::AtlasBase.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 leans on
  'QSGRhiAtlasTexture.

  What to expect
  --------------

  - The C++ QSGRhiAtlasTexture::AtlasBase is created at the first use, not by
    'QSGRhiAtlasTexture::AtlasBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRhiAtlasTexture::AtlasBase.
  - Qt tells when it has removed the C++ QSGRhiAtlasTexture::AtlasBase. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSGRhiAtlasTexture::AtlasBase that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRhiAtlasTexture::AtlasBase'

  #  A C++ QSGRhiAtlasTexture::AtlasBase Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRhiAtlasTexture_AtlasBase'

  #  The functions Qt calls itself that QSGRhiAtlasTexture::AtlasBase is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'generateTexture': (
          ('_ZN18QSGRhiAtlasTexture9AtlasBase15generateTextureEv',
           ('bool', 'number', ''),
           ()),
      ),
      'enqueueTextureUpload': (
          ('_ZN18QSGRhiAtlasTexture9AtlasBase20enqueueTextureUploadEPNS_11T'
           'extureBaseEP23QRhiResourceUpdateBatch',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtQuick:QSGRhiAtlasTexture.TextureBase'),
               ('address', 'address', 'QtGui:QRhiResourceUpdateBatch'),
           )),
      ),
  }

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
    *QSGRhiAtlasTexture::AtlasBase::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-atlasbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGRhiAtlasTexture::AtlasBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture9AtlasBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def renderContext(self) -> Optional[QSGDefaultRenderContext]:
    """
    Calls Qt's 'QSGDefaultRenderContext
    *QSGRhiAtlasTexture::AtlasBase::renderContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-atlasbase.html#renderContext

    Returns
    -------

    Optional[QSGDefaultRenderContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGDefaultRenderContext
    #      *QSGRhiAtlasTexture::AtlasBase::renderContext() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture9AtlasBase13renderContextEv',
    )
    from . import QSGDefaultRenderContext
    return QSGDefaultRenderContext._cuteAt(address)

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QSGRhiAtlasTexture::AtlasBase::rhi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-atlasbase.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QSGRhiAtlasTexture::AtlasBase::rhi() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture9AtlasBase3rhiEv',
    )
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  def texture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QSGRhiAtlasTexture::AtlasBase::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-atlasbase.html#texture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QSGRhiAtlasTexture::AtlasBase::texture() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture9AtlasBase7textureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QSGRhiAtlasTexture::AtlasBase::size() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-atlasbase.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSGRhiAtlasTexture::AtlasBase::size() const
    address = self.uglySide.call(
        'ritual_ZNK18QSGRhiAtlasTexture9AtlasBase4sizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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
    Qt's 'QSGRhiAtlasTexture::AtlasBase::AtlasBase(QSGDefaultRenderContext
    *rc, const QSize &size)': leans on
    'QSGRhiAtlasTexture::AtlasBase::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSGRhiAtlasTexture.AtlasBase.__init__' has no cute function yet. "
        "Qt's "
        "'QSGRhiAtlasTexture::AtlasBase::AtlasBase(QSGDefaultRenderContext "
        "*rc, const QSize &size)': leans on "
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QSGRhiAtlasTexture::AtlasBase::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-atlasbase.html#invalidate
    """
    #  void QSGRhiAtlasTexture::AtlasBase::invalidate()
    self.uglySide.call(
        'ritual_ZN18QSGRhiAtlasTexture9AtlasBase10invalidateEv',
    )

  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def commitTextureOperations(
      self,
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void QSGRhiAtlasTexture::AtlasBase::commitTextureOperations(
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-atlasbase.html

    Parameters
    ----------

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiAtlasTexture::AtlasBase::commitTextureOperations(
    #      QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN18QSGRhiAtlasTexture9AtlasBase23commitTextureOperationsEP'
        '23QRhiResourceUpdateBatch',
        self._addressOf(resourceUpdates),
    )

  @overload(WAIT['QSGRhiAtlasTexture.TextureBase'])
  @overload(NoneType)
  def remove(self, t: Optional[QSGRhiAtlasTexture.TextureBase]) -> None:
    """
    Calls Qt's 'void QSGRhiAtlasTexture::AtlasBase::remove(TextureBase *t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-atlasbase.html#remove

    Parameters
    ----------

    t : Optional[QSGRhiAtlasTexture.TextureBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiAtlasTexture::AtlasBase::remove(TextureBase *t)
    self.uglySide.call(
        'ritual_ZN18QSGRhiAtlasTexture9AtlasBase6removeEPNS_11TextureBaseE',
        self._addressOf(t),
    )

  def generateTexture(self) -> bool:
    """
    Calls Qt's 'bool QSGRhiAtlasTexture::AtlasBase::generateTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-atlasbase.html#generateTexture
    """
    #  bool QSGRhiAtlasTexture::AtlasBase::generateTexture()
    return self.uglySide.call(
        'ritual_ZN18QSGRhiAtlasTexture9AtlasBase15generateTextureEv',
    )

  @overload(WAIT['QSGRhiAtlasTexture.TextureBase'], QRhiResourceUpdateBatch)
  @overload(WAIT['QSGRhiAtlasTexture.TextureBase'], NoneType)
  @overload(NoneType, QRhiResourceUpdateBatch)
  @overload(NoneType, NoneType)
  def enqueueTextureUpload(
      self,
      t: Optional[QSGRhiAtlasTexture.TextureBase],
      resourceUpdates: Optional[QRhiResourceUpdateBatch],
  ) -> None:
    """
    Calls Qt's 'void
    QSGRhiAtlasTexture::AtlasBase::enqueueTextureUpload(TextureBase *t,
    QRhiResourceUpdateBatch *resourceUpdates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiatlastexture-atlasbase.html

    Parameters
    ----------

    t : Optional[QSGRhiAtlasTexture.TextureBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourceUpdates : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiAtlasTexture::AtlasBase::enqueueTextureUpload(TextureBase
    #      *t, QRhiResourceUpdateBatch *resourceUpdates)
    self.uglySide.call(
        'ritual_ZN18QSGRhiAtlasTexture9AtlasBase20enqueueTextureUploadEPNS_'
        '11TextureBaseEP23QRhiResourceUpdateBatch',
        self._addressOf(t), self._addressOf(resourceUpdates),
    )
