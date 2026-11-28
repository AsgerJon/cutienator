"""
QQuick3DShaderUtilsBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DShaderUtilsBuffer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtQuick3DUtils import QSSGRenderTextureFormat
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGCommand

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DShaderUtilsBuffer(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DShaderUtilsBuffer: a plain Python object
  standing in front of one C++ QQuick3DShaderUtilsBuffer.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DShaderUtilsBuffer
  is built on Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DShaderUtilsBuffer that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr',
  'textureFilterOperation', 'setTextureFilterOperation',
  'textureCoordOperation', 'setTextureCoordOperation', 'cloneCommand',
  'format', 'setFormat', 'bufferFlags', 'setBufferFlags', 'mapTextureFormat',
  'mapRenderTextureFormat', 'changed'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DShaderUtilsBuffer::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DShaderUtilsBuffer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DShaderUtilsBuffer::~QQuick3DShaderUtilsBuffer()': the
    destructor: Python never removes a C++ QQuick3DShaderUtilsBuffer.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DShaderUtilsBuffer is created at the first use, not by
    'QQuick3DShaderUtilsBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DShaderUtilsBuffer.
  - Qt tells when it has removed the C++ QQuick3DShaderUtilsBuffer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DShaderUtilsBuffer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class AllocateBufferFlagValues(CuteNum, scoped=True):
    """
    The enum 'QQuick3DShaderUtilsBuffer::AllocateBufferFlagValues' of Qt,
    with the 2 names Qt gives in it. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    NULL = Kee[int](0)
    SceneLifetime = Kee[int](1)

  class TextureCoordOperation(CuteNum, scoped=True):
    """
    The enum 'QQuick3DShaderUtilsBuffer::TextureCoordOperation' of Qt, with
    the 4 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    ClampToEdge = Kee[int](1)
    MirroredRepeat = Kee[int](2)
    Repeat = Kee[int](3)

  class TextureFilterOperation(CuteNum, scoped=True):
    """
    The enum 'QQuick3DShaderUtilsBuffer::TextureFilterOperation' of Qt, with
    the 3 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    Nearest = Kee[int](1)
    Linear = Kee[int](2)

  class TextureFormat(CuteNum, scoped=True):
    """
    The enum 'QQuick3DShaderUtilsBuffer::TextureFormat' of Qt, with the 8
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Unknown = Kee[int](0)
    RGBA8 = Kee[int](1)
    RGBA16F = Kee[int](2)
    RGBA32F = Kee[int](3)
    R8 = Kee[int](4)
    R16 = Kee[int](5)
    R16F = Kee[int](6)
    R32F = Kee[int](7)

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
    Calls Qt's 'QString QQuick3DShaderUtilsBuffer::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html#tr

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
    #  QString QQuick3DShaderUtilsBuffer::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuick3DShaderUtilsBuffer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(TextureFormat)
  def mapTextureFormat(fmt: TextureFormat) -> QSSGRenderTextureFormat.Format:
    """
    Calls Qt's 'QSSGRenderTextureFormat::Format
    QQuick3DShaderUtilsBuffer::mapTextureFormat(QQuick3DShaderUtilsBuffer::
    TextureFormat fmt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html#mapTextureFormat

    Parameters
    ----------

    fmt : TextureFormat
      Passed on as its number.

    Returns
    -------

    QSSGRenderTextureFormat.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSSGRenderTextureFormat.Format(number)' gives.
    """
    #  QSSGRenderTextureFormat::Format
    #      QQuick3DShaderUtilsBuffer::mapTextureFormat(
    #      QQuick3DShaderUtilsBuffer::TextureFormat fmt)
    return QSSGRenderTextureFormat.Format(Rituals.call(
        'ritual_ZN25QQuick3DShaderUtilsBuffer16mapTextureFormatENS_13Textur'
        'eFormatE',
        fmt.value,
    ))

  @staticmethod
  @overload(QSSGRenderTextureFormat.Format)
  def mapRenderTextureFormat(
      fmt: QSSGRenderTextureFormat.Format,
  ) -> TextureFormat:
    """
    Calls Qt's 'QQuick3DShaderUtilsBuffer::TextureFormat
    QQuick3DShaderUtilsBuffer::mapRenderTextureFormat(
    QSSGRenderTextureFormat::Format fmt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html

    Parameters
    ----------

    fmt : QSSGRenderTextureFormat.Format
      Passed on as its number.

    Returns
    -------

    TextureFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureFormat(number)'
      gives.
    """
    #  QQuick3DShaderUtilsBuffer::TextureFormat
    #      QQuick3DShaderUtilsBuffer::mapRenderTextureFormat(
    #      QSSGRenderTextureFormat::Format fmt)
    return QQuick3DShaderUtilsBuffer.TextureFormat(Rituals.call(
        'ritual_ZN25QQuick3DShaderUtilsBuffer22mapRenderTextureFormatEN23QS'
        'SGRenderTextureFormat6FormatE',
        fmt.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DShaderUtilsBuffer'

  #  A C++ QQuick3DShaderUtilsBuffer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DShaderUtilsBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DShaderUtilsBuffer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DShaderUtilsBuffer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuick3DShaderUtilsBuffer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureFilterOperation(self) -> TextureFilterOperation:
    """
    Calls Qt's 'TextureFilterOperation
    QQuick3DShaderUtilsBuffer::textureFilterOperation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html

    Returns
    -------

    TextureFilterOperation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'TextureFilterOperation(number)' gives.
    """
    #  TextureFilterOperation
    #      QQuick3DShaderUtilsBuffer::textureFilterOperation() const
    return QQuick3DShaderUtilsBuffer.TextureFilterOperation(
        self.uglySide.call(
            'ritual_ZNK25QQuick3DShaderUtilsBuffer22textureFilterOperationE'
            'v',
        ))

  def textureCoordOperation(self) -> TextureCoordOperation:
    """
    Calls Qt's 'TextureCoordOperation
    QQuick3DShaderUtilsBuffer::textureCoordOperation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html

    Returns
    -------

    TextureCoordOperation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'TextureCoordOperation(number)' gives.
    """
    #  TextureCoordOperation
    #      QQuick3DShaderUtilsBuffer::textureCoordOperation() const
    return QQuick3DShaderUtilsBuffer.TextureCoordOperation(
        self.uglySide.call(
            'ritual_ZNK25QQuick3DShaderUtilsBuffer21textureCoordOperationEv',
        ))

  def format(self) -> TextureFormat:
    """
    Calls Qt's 'TextureFormat QQuick3DShaderUtilsBuffer::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html#format

    Returns
    -------

    TextureFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TextureFormat(number)'
      gives.
    """
    #  TextureFormat QQuick3DShaderUtilsBuffer::format() const
    return QQuick3DShaderUtilsBuffer.TextureFormat(self.uglySide.call(
        'ritual_ZNK25QQuick3DShaderUtilsBuffer6formatEv',
    ))

  def bufferFlags(self) -> AllocateBufferFlagValues:
    """
    Calls Qt's 'AllocateBufferFlagValues
    QQuick3DShaderUtilsBuffer::bufferFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html#bufferFlags

    Returns
    -------

    AllocateBufferFlagValues
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AllocateBufferFlagValues(number)' gives.
    """
    #  AllocateBufferFlagValues QQuick3DShaderUtilsBuffer::bufferFlags()
    #      const
    return QQuick3DShaderUtilsBuffer.AllocateBufferFlagValues(
        self.uglySide.call(
            'ritual_ZNK25QQuick3DShaderUtilsBuffer11bufferFlagsEv',
        ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TextureFilterOperation)
  def setTextureFilterOperation(self, op: TextureFilterOperation) -> None:
    """
    Calls Qt's 'void QQuick3DShaderUtilsBuffer::setTextureFilterOperation(
    TextureFilterOperation op)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html

    Parameters
    ----------

    op : TextureFilterOperation
      Passed on as its number.
    """
    #  void QQuick3DShaderUtilsBuffer::setTextureFilterOperation(
    #      TextureFilterOperation op)
    self.uglySide.call(
        'ritual_ZN25QQuick3DShaderUtilsBuffer25setTextureFilterOperationENS'
        '_22TextureFilterOperationE',
        op.value,
    )

  @overload(TextureCoordOperation)
  def setTextureCoordOperation(
      self,
      texCoordOp: TextureCoordOperation,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsBuffer::setTextureCoordOperation(TextureCoordOperation
    texCoordOp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html

    Parameters
    ----------

    texCoordOp : TextureCoordOperation
      Passed on as its number.
    """
    #  void QQuick3DShaderUtilsBuffer::setTextureCoordOperation(
    #      TextureCoordOperation texCoordOp)
    self.uglySide.call(
        'ritual_ZN25QQuick3DShaderUtilsBuffer24setTextureCoordOperationENS_'
        '21TextureCoordOperationE',
        texCoordOp.value,
    )

  @overload(TextureFormat)
  def setFormat(self, format: TextureFormat) -> None:
    """
    Calls Qt's 'void QQuick3DShaderUtilsBuffer::setFormat(TextureFormat
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html#setFormat

    Parameters
    ----------

    format : TextureFormat
      Passed on as its number.
    """
    #  void QQuick3DShaderUtilsBuffer::setFormat(TextureFormat format)
    self.uglySide.call(
        'ritual_ZN25QQuick3DShaderUtilsBuffer9setFormatENS_13TextureFormatE',
        format.value,
    )

  @overload(AllocateBufferFlagValues)
  def setBufferFlags(self, flag: AllocateBufferFlagValues) -> None:
    """
    Calls Qt's 'void
    QQuick3DShaderUtilsBuffer::setBufferFlags(AllocateBufferFlagValues
    flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html#setBufferFlags

    Parameters
    ----------

    flag : AllocateBufferFlagValues
      Passed on as its number.
    """
    #  void
    #      QQuick3DShaderUtilsBuffer::setBufferFlags(AllocateBufferFlagValues
    #      flag)
    self.uglySide.call(
        'ritual_ZN25QQuick3DShaderUtilsBuffer14setBufferFlagsENS_24Allocate'
        'BufferFlagValuesE',
        flag.value,
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
    Notes what was given, for Qt's
    'QQuick3DShaderUtilsBuffer::QQuick3DShaderUtilsBuffer()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html
    """
    #  QQuick3DShaderUtilsBuffer::QQuick3DShaderUtilsBuffer()
    self._noteCreation(QQuick3DShaderUtilsBuffer, lambda: Rituals.call(
        'ritual_ZN25QQuick3DShaderUtilsBufferC1Ev',
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

  def cloneCommand(self) -> Optional[QSSGCommand]:
    """
    Calls Qt's 'QSSGCommand *QQuick3DShaderUtilsBuffer::cloneCommand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html#cloneCommand

    Returns
    -------

    Optional[QSSGCommand]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGCommand *QQuick3DShaderUtilsBuffer::cloneCommand()
    address = self.uglySide.call(
        'ritual_ZN25QQuick3DShaderUtilsBuffer12cloneCommandEv',
    )
    from ..QtQuick3DRuntimeRender import QSSGCommand
    return QSSGCommand._cuteAt(address)

  def changed(self) -> None:
    """
    Calls Qt's 'void QQuick3DShaderUtilsBuffer::changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dshaderutilsbuffer.html#changed
    """
    #  void QQuick3DShaderUtilsBuffer::changed()
    self.uglySide.call('ritual_ZN25QQuick3DShaderUtilsBuffer7changedEv')
