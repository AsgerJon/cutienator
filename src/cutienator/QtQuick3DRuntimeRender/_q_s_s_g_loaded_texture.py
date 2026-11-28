"""
QSSGLoadedTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderloadedtexture_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGLoadedTexture to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQuick3DUtils import QSSGRenderTextureFormat
  from . import QSSGRenderTextureData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderTextureData = WAIT['QSSGRenderTextureData']
  QSSGRenderTextureFormat = WAIT['QSSGRenderTextureFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGLoadedTexture(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGLoadedTexture: a plain Python object standing in
  front of one C++ QSSGLoadedTexture.

  C++ hands a QSSGLoadedTexture around as a copy, so every C++
  QSSGLoadedTexture behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGLoadedTexture that has a ritual and that Python
  can call so far, 7 names in all: 'setFormatFromComponents',
  'scanForTransparency', 'load', 'loadQImage', 'loadCompressedImage',
  'loadTextureData', 'loadLightmapImage'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGLoadedTexture::~QSSGLoadedTexture()': the destructor: Python
    removes its C++ QSSGLoadedTexture by it, and has no other use for it.
  - Qt's 'QSSGLoadedTexture *QSSGLoadedTexture::loadHdrImage(const
    QSharedPointer<QIODevice> &source, const QSSGRenderTextureFormat
    &inFormat)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSSGLoadedTexture is created at the first use, not by
    'QSSGLoadedTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGLoadedTexture back gives a copy the ritual made
    for Python, in a new cute QSSGLoadedTexture.
  - Each name of Qt's QSSGLoadedTexture that has no cute function yet,
    'loadHdrImage', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str, QSSGRenderTextureFormat)
  @overload(str, QSSGRenderTextureFormat, bool)
  def load(
      inPath: str,
      inFormat: QSSGRenderTextureFormat,
      inFlipY: bool = True,
  ) -> Optional[QSSGLoadedTexture]:
    """
    Calls Qt's 'QSSGLoadedTexture *QSSGLoadedTexture::load(const QString
    &inPath, const QSSGRenderTextureFormat &inFormat, bool inFlipY)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgloadedtexture.html#load

    Parameters
    ----------

    inPath : str
      Passed on as it is: a QString is made of it for the call.

    inFormat : QSSGRenderTextureFormat
      Passed on as a value: Qt reads the C++ QSSGRenderTextureFormat, which
      stays Python's own.

    inFlipY : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[QSSGLoadedTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGLoadedTexture *QSSGLoadedTexture::load(const QString &inPath,
    #      const QSSGRenderTextureFormat &inFormat, bool inFlipY)
    address = Rituals.call(
        'ritual_ZN17QSSGLoadedTexture4loadERK7QStringRK23QSSGRenderTextureF'
        'ormatb',
        inPath, CuteMixin._valueOf(inFormat), inFlipY,
    )
    return QSSGLoadedTexture._cuteAt(address)

  @staticmethod
  @overload(str, int)
  def loadQImage(
      inPath: str,
      flipVertical: int,
  ) -> Optional[QSSGLoadedTexture]:
    """
    Calls Qt's 'QSSGLoadedTexture *QSSGLoadedTexture::loadQImage(const
    QString &inPath, qint32 flipVertical)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgloadedtexture.html#loadQImage

    Parameters
    ----------

    inPath : str
      Passed on as it is: a QString is made of it for the call.

    flipVertical : int
      Passed on as it is.

    Returns
    -------

    Optional[QSSGLoadedTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGLoadedTexture *QSSGLoadedTexture::loadQImage(const QString
    #      &inPath, qint32 flipVertical)
    address = Rituals.call(
        'ritual_ZN17QSSGLoadedTexture10loadQImageERK7QStringi',
        inPath, flipVertical,
    )
    return QSSGLoadedTexture._cuteAt(address)

  @staticmethod
  @overload(str)
  def loadCompressedImage(inPath: str) -> Optional[QSSGLoadedTexture]:
    """
    Calls Qt's 'QSSGLoadedTexture
    *QSSGLoadedTexture::loadCompressedImage(const QString &inPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgloadedtexture.html#loadCompressedImage

    Parameters
    ----------

    inPath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QSSGLoadedTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGLoadedTexture *QSSGLoadedTexture::loadCompressedImage(const
    #      QString &inPath)
    address = Rituals.call(
        'ritual_ZN17QSSGLoadedTexture19loadCompressedImageERK7QString',
        inPath,
    )
    return QSSGLoadedTexture._cuteAt(address)

  @staticmethod
  @overload(QSSGRenderTextureData)
  @overload(NoneType)
  def loadTextureData(
      textureData: Optional[QSSGRenderTextureData],
  ) -> Optional[QSSGLoadedTexture]:
    """
    Calls Qt's 'QSSGLoadedTexture
    *QSSGLoadedTexture::loadTextureData(QSSGRenderTextureData *textureData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgloadedtexture.html#loadTextureData

    Parameters
    ----------

    textureData : Optional[QSSGRenderTextureData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGLoadedTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGLoadedTexture
    #      *QSSGLoadedTexture::loadTextureData(QSSGRenderTextureData
    #      *textureData)
    address = Rituals.call(
        'ritual_ZN17QSSGLoadedTexture15loadTextureDataEP21QSSGRenderTexture'
        'Data',
        CuteMixin._addressOf(textureData),
    )
    return QSSGLoadedTexture._cuteAt(address)

  @staticmethod
  @overload(str, QSSGRenderTextureFormat, str)
  def loadLightmapImage(
      inPath: str,
      inFormat: QSSGRenderTextureFormat,
      key: str,
  ) -> Optional[QSSGLoadedTexture]:
    """
    Calls Qt's 'QSSGLoadedTexture *QSSGLoadedTexture::loadLightmapImage(const
    QString &inPath, const QSSGRenderTextureFormat &inFormat, const QString
    &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgloadedtexture.html#loadLightmapImage

    Parameters
    ----------

    inPath : str
      Passed on as it is: a QString is made of it for the call.

    inFormat : QSSGRenderTextureFormat
      Passed on as a value: Qt reads the C++ QSSGRenderTextureFormat, which
      stays Python's own.

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QSSGLoadedTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGLoadedTexture *QSSGLoadedTexture::loadLightmapImage(const QString
    #      &inPath, const QSSGRenderTextureFormat &inFormat, const QString
    #      &key)
    address = Rituals.call(
        'ritual_ZN17QSSGLoadedTexture17loadLightmapImageERK7QStringRK23QSSG'
        'RenderTextureFormatS2_',
        inPath, CuteMixin._valueOf(inFormat), key,
    )
    return QSSGLoadedTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGLoadedTexture'

  #  Qt's '~QSSGLoadedTexture()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGLoadedTexture behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QSSGLoadedTextureD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scanForTransparency(self) -> bool:
    """
    Calls Qt's 'bool QSSGLoadedTexture::scanForTransparency() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgloadedtexture.html#scanForTransparency
    """
    #  bool QSSGLoadedTexture::scanForTransparency() const
    return self.uglySide.call(
        'ritual_ZNK17QSSGLoadedTexture19scanForTransparencyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setFormatFromComponents(self) -> None:
    """
    Calls Qt's 'void QSSGLoadedTexture::setFormatFromComponents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgloadedtexture.html#setFormatFromComponents
    """
    #  void QSSGLoadedTexture::setFormatFromComponents()
    self.uglySide.call(
        'ritual_ZN17QSSGLoadedTexture23setFormatFromComponentsEv',
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
  def loadHdrImage(*__, **_) -> Never:
    """
    Qt's 'QSSGLoadedTexture *QSSGLoadedTexture::loadHdrImage(const
    QSharedPointer<QIODevice> &source, const QSSGRenderTextureFormat
    &inFormat)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGLoadedTexture.loadHdrImage' has no cute function yet. Qt's "
        "'QSSGLoadedTexture *QSSGLoadedTexture::loadHdrImage(const "
        "QSharedPointer<QIODevice> &source, const QSSGRenderTextureFormat "
        "&inFormat)': takes a type Python has no way to hand over yet.")
