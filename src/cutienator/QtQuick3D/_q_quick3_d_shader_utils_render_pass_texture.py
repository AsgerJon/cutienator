"""
QQuick3DShaderUtilsRenderPassTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DShaderUtilsRenderPassTexture to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DUtils import QSSGRenderTextureFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderTextureFormat = WAIT['QSSGRenderTextureFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DShaderUtilsRenderPassTexture(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DShaderUtilsRenderPassTexture: a plain Python
  object standing in front of one C++ QQuick3DShaderUtilsRenderPassTexture.

  It is built on the cute 'QQuick3DObject', as Qt's
  QQuick3DShaderUtilsRenderPassTexture is built on Qt's QQuick3DObject, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DShaderUtilsRenderPassTexture that has a
  ritual and that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'format', 'setFormat', 'asRenderTextureFormat', 'fromRenderTextureFormat'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DShaderUtilsRenderPassTexture::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuick3DShaderUtilsRenderPassTexture::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DShaderUtilsRenderPassTexture::
    ~QQuick3DShaderUtilsRenderPassTexture()': the destructor: Python never
    removes a C++ QQuick3DShaderUtilsRenderPassTexture.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DShaderUtilsRenderPassTexture is created at the first use,
    not by 'QQuick3DShaderUtilsRenderPassTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DShaderUtilsRenderPassTexture.
  - Qt tells when it has removed the C++
    QQuick3DShaderUtilsRenderPassTexture. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  #  The enums Qt writes inside QQuick3DShaderUtilsRenderPassTexture, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class TextureFormat(CuteNum, scoped=True):
    """
    The enum 'QQuick3DShaderUtilsRenderPassTexture::TextureFormat' of Qt,
    with the 12 names Qt gives in it. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    RGBA8 = Kee[int](1)
    RGBA16F = Kee[int](2)
    RGBA32F = Kee[int](3)
    R8 = Kee[int](4)
    R16 = Kee[int](5)
    R16F = Kee[int](6)
    R32F = Kee[int](7)
    Depth16 = Kee[int](8)
    Depth24 = Kee[int](9)
    Depth32 = Kee[int](10)
    Depth24Stencil8 = Kee[int](11)

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
    Calls Qt's 'QString QQuick3DShaderUtilsRenderPassTexture::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpasstexture.html#tr

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
    #  QString QQuick3DShaderUtilsRenderPassTexture::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN36QQuick3DShaderUtilsRenderPassTexture2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(TextureFormat)
  def asRenderTextureFormat(fmt: TextureFormat) -> QSSGRenderTextureFormat:
    """
    Calls Qt's 'QSSGRenderTextureFormat
    QQuick3DShaderUtilsRenderPassTexture::asRenderTextureFormat(
    QQuick3DShaderUtilsRenderPassTexture::TextureFormat fmt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpasstexture.html

    Parameters
    ----------

    fmt : TextureFormat
      Passed on as its number.

    Returns
    -------

    QSSGRenderTextureFormat
      A new cute QSSGRenderTextureFormat around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGRenderTextureFormat
    #      QQuick3DShaderUtilsRenderPassTexture::asRenderTextureFormat(
    #      QQuick3DShaderUtilsRenderPassTexture::TextureFormat fmt)
    address = Rituals.call(
        'ritual_ZN36QQuick3DShaderUtilsRenderPassTexture21asRenderTextureFo'
        'rmatENS_13TextureFormatE',
        fmt.value,
    )
    from ..QtQuick3DUtils import QSSGRenderTextureFormat
    return QSSGRenderTextureFormat._cuteOwning(address)

  @staticmethod
  @overload(QSSGRenderTextureFormat)
  def fromRenderTextureFormat(fmt: QSSGRenderTextureFormat) -> TextureFormat:
    """
    Calls Qt's 'QQuick3DShaderUtilsRenderPassTexture::TextureFormat
    QQuick3DShaderUtilsRenderPassTexture::fromRenderTextureFormat(
    QSSGRenderTextureFormat fmt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpasstexture.html

    Parameters
    ----------

    fmt : QSSGRenderTextureFormat
      Passed on as a value: Qt reads the C++ QSSGRenderTextureFormat, which
      stays Python's own.

    Returns
    -------

    TextureFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureFormat(number)'
      gives.
    """
    #  QQuick3DShaderUtilsRenderPassTexture::TextureFormat
    #      QQuick3DShaderUtilsRenderPassTexture::fromRenderTextureFormat(
    #      QSSGRenderTextureFormat fmt)
    return QQuick3DShaderUtilsRenderPassTexture.TextureFormat(Rituals.call(
        'ritual_ZN36QQuick3DShaderUtilsRenderPassTexture23fromRenderTexture'
        'FormatE23QSSGRenderTextureFormat',
        CuteMixin._valueOf(fmt),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DShaderUtilsRenderPassTexture'

  #  A C++ QQuick3DShaderUtilsRenderPassTexture Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DShaderUtilsRenderPassTexture'

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
    *QQuick3DShaderUtilsRenderPassTexture::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpasstexture.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DShaderUtilsRenderPassTexture::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK36QQuick3DShaderUtilsRenderPassTexture10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def format(self) -> TextureFormat:
    """
    Calls Qt's 'TextureFormat QQuick3DShaderUtilsRenderPassTexture::format()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpasstexture.html#format

    Returns
    -------

    TextureFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureFormat(number)'
      gives.
    """
    #  TextureFormat QQuick3DShaderUtilsRenderPassTexture::format() const
    return QQuick3DShaderUtilsRenderPassTexture.TextureFormat(
        self.uglySide.call(
            'ritual_ZNK36QQuick3DShaderUtilsRenderPassTexture6formatEv',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TextureFormat)
  def setFormat(self, newFormat: TextureFormat) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsRenderPassTexture::setFormat(TextureFormat
    newFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpasstexture.html

    Parameters
    ----------

    newFormat : TextureFormat
      Passed on as its number.
    """
    #  void QQuick3DShaderUtilsRenderPassTexture::setFormat(TextureFormat
    #      newFormat)
    self.uglySide.call(
        'ritual_ZN36QQuick3DShaderUtilsRenderPassTexture9setFormatENS_13Tex'
        'tureFormatE',
        newFormat.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQuick3DShaderUtilsRenderPassTexture::
    QQuick3DShaderUtilsRenderPassTexture()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsrenderpasstexture.html
    """
    #  QQuick3DShaderUtilsRenderPassTexture::
    #      QQuick3DShaderUtilsRenderPassTexture()
    self._noteCreation(
        QQuick3DShaderUtilsRenderPassTexture, lambda: Rituals.call(
            'ritual_ZN36QQuick3DShaderUtilsRenderPassTextureC1Ev',
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
