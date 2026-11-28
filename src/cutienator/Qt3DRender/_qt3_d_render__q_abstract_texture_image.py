"""
Qt3DRender::QAbstractTextureImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qabstracttextureimage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractTextureImage(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DRender::QAbstractTextureImage: a plain Python
  object standing in front of one C++ Qt3DRender::QAbstractTextureImage.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DRender::QAbstractTextureImage is built on Qt's Qt3DCore::QNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QAbstractTextureImage that has a ritual
  and that Python can call so far, 13 names in all: 'metaObject', 'tr',
  'mipLevel', 'layer', 'face', 'setMipLevel', 'setLayer', 'setFace',
  'mipLevelChanged', 'layerChanged', 'faceChanged',
  'notifyDataGeneratorChanged', 'd_func'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QAbstractTextureImage::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DRender::QAbstractTextureImage::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QAbstractTextureImage::~QAbstractTextureImage()': the
    destructor: Python never removes a C++ Qt3DRender::QAbstractTextureImage.
  - Qt's 'QTextureImageDataGeneratorPtr
    Qt3DRender::QAbstractTextureImage::dataGenerator() const': gives a type
    Python has no way to take yet.
  - Qt's 'const QAbstractTextureImagePrivate
    *Qt3DRender::QAbstractTextureImage::d_func() const': takes in Python what
    'QAbstractTextureImagePrivate
    *Qt3DRender::QAbstractTextureImage::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ Qt3DRender::QAbstractTextureImage is created at the first use,
    not by 'Qt3DRender::QAbstractTextureImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QAbstractTextureImage.
  - Qt tells when it has removed the C++ Qt3DRender::QAbstractTextureImage.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QAbstractTextureImage that has no cute
    function yet, '__init__', 'dataGenerator', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QAbstractTextureImage::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QAbstractTextureImage::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender21QAbstractTextureImage2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QAbstractTextureImage'

  #  A C++ Qt3DRender::QAbstractTextureImage Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QAbstractTextureImage'

  #  The functions Qt calls itself that Qt3DRender::QAbstractTextureImage is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dataGenerator': (
          'QTextureImageDataGeneratorPtr '
          'Qt3DRender::QAbstractTextureImage::dataGenerator() const',
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
    *Qt3DRender::QAbstractTextureImage::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QAbstractTextureImage::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QAbstractTextureImage10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mipLevel(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QAbstractTextureImage::mipLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#mipLevel
    """
    #  int Qt3DRender::QAbstractTextureImage::mipLevel() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QAbstractTextureImage8mipLevelEv',
    )

  def layer(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QAbstractTextureImage::layer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#layer
    """
    #  int Qt3DRender::QAbstractTextureImage::layer() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QAbstractTextureImage5layerEv',
    )

  def face(self) -> Qt3DRender.QAbstractTexture.CubeMapFace:
    """
    Calls Qt's 'QAbstractTexture::CubeMapFace
    Qt3DRender::QAbstractTextureImage::face() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#face

    Returns
    -------

    Qt3DRender.QAbstractTexture.CubeMapFace
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QAbstractTexture.CubeMapFace(number)' gives.
    """
    #  QAbstractTexture::CubeMapFace
    #      Qt3DRender::QAbstractTextureImage::face() const
    return Qt3DRender.QAbstractTexture.CubeMapFace(self.uglySide.call(
        'ritual_ZNK10Qt3DRender21QAbstractTextureImage4faceEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMipLevel(self, level: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTextureImage::setMipLevel(int
    level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#setMipLevel

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTextureImage::setMipLevel(int level)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QAbstractTextureImage11setMipLevelEi', level,
    )

  @overload(int)
  def setLayer(self, layer: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTextureImage::setLayer(int layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#setLayer

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTextureImage::setLayer(int layer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QAbstractTextureImage8setLayerEi', layer,
    )

  @overload(Qt3DRender.QAbstractTexture.CubeMapFace)
  def setFace(self, face: Qt3DRender.QAbstractTexture.CubeMapFace) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTextureImage::setFace(QAbstractTexture::CubeMapFace
    face)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#setFace

    Parameters
    ----------

    face : Qt3DRender.QAbstractTexture.CubeMapFace
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTextureImage::setFace(QAbstractTexture::
    #      CubeMapFace face)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QAbstractTextureImage7setFaceENS_16QAbstrac'
        'tTexture11CubeMapFaceE',
        face.value,
    )

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
    - Qt's
      'Qt3DRender::QAbstractTextureImage::QAbstractTextureImage(Qt3DCore::
      QNode *parent)': the class is abstract, so C++ cannot make one, and the
      C++ class of ours does not fill in every function it leaves open.
    - Qt's 'Qt3DRender::QAbstractTextureImage::QAbstractTextureImage(
      QAbstractTextureImagePrivate &dd, Qt3DCore::QNode *parent)': the class
      is abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractTextureImage.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DRender::QAbstractTextureImage::QAbstractTextureImage(Qt3DCore:"
        ":QNode *parent)': the class is abstract, so C++ cannot make one, "
        "and the C++ class of ours does not fill in every function it "
        "leaves open. Qt's "
        "'Qt3DRender::QAbstractTextureImage::QAbstractTextureImage(QAbstract"
        "TextureImagePrivate &dd, Qt3DCore::QNode *parent)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  @overload(int)
  def mipLevelChanged(self, mipLevel: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTextureImage::mipLevelChanged(int
    mipLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html

    Parameters
    ----------

    mipLevel : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTextureImage::mipLevelChanged(int mipLevel)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QAbstractTextureImage15mipLevelChangedEi',
        mipLevel,
    )

  @overload(int)
  def layerChanged(self, layer: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QAbstractTextureImage::layerChanged(int
    layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#layerChanged

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void Qt3DRender::QAbstractTextureImage::layerChanged(int layer)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QAbstractTextureImage12layerChangedEi',
        layer,
    )

  @overload(Qt3DRender.QAbstractTexture.CubeMapFace)
  def faceChanged(
      self,
      face: Qt3DRender.QAbstractTexture.CubeMapFace,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTextureImage::faceChanged(QAbstractTexture::
    CubeMapFace face)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#faceChanged

    Parameters
    ----------

    face : Qt3DRender.QAbstractTexture.CubeMapFace
      Passed on as its number.
    """
    #  void Qt3DRender::QAbstractTextureImage::faceChanged(QAbstractTexture::
    #      CubeMapFace face)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QAbstractTextureImage11faceChangedENS_16QAb'
        'stractTexture11CubeMapFaceE',
        face.value,
    )

  def notifyDataGeneratorChanged(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QAbstractTextureImage::notifyDataGeneratorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html
    """
    #  void Qt3DRender::QAbstractTextureImage::notifyDataGeneratorChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender21QAbstractTextureImage26notifyDataGeneratorC'
        'hangedEv',
    )

  def d_func(self) -> Optional[Qt3DRender.QAbstractTextureImagePrivate]:
    """
    Calls Qt's 'QAbstractTextureImagePrivate
    *Qt3DRender::QAbstractTextureImage::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstracttextureimage.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QAbstractTextureImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTextureImagePrivate
    #      *Qt3DRender::QAbstractTextureImage::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender21QAbstractTextureImage6d_funcEv',
    )
    return Qt3DRender.QAbstractTextureImagePrivate._cuteAt(address)

  @staticmethod
  def dataGenerator(*__, **_) -> Never:
    """
    Qt's 'QTextureImageDataGeneratorPtr
    Qt3DRender::QAbstractTextureImage::dataGenerator() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractTextureImage.dataGenerator' has no cute "
        "function yet. Qt's 'QTextureImageDataGeneratorPtr "
        "Qt3DRender::QAbstractTextureImage::dataGenerator() const': gives a "
        "type Python has no way to take yet.")
