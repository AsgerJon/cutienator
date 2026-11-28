"""
Qt3DRender::QTextureImageDataPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qtextureimagedata_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QTextureImageDataPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextureImageDataPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::QTextureImageDataPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QTextureImageDataPrivate.

  C++ hands a Qt3DRender::QTextureImageDataPrivate around as a copy, so every
  C++ Qt3DRender::QTextureImageDataPrivate behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QTextureImageDataPrivate that has a
  ritual and that Python can call so far, 7 names in all: 'setData', 'data',
  'get', 'ddsLayerSize', 'ddsFaceSize', 'mipmapLevelSize', 'ktxData'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void Qt3DRender::QTextureImageDataPrivate::setData(const QByteArray
    &data, std::function<QByteArray (QByteArray, int, int, int)>
    dataExtractor, bool isCompressed)': takes a type Python has no way to
    hand over yet.
  - Qt's 'Qt3DRender::QTextureImageDataPrivate::~QTextureImageDataPrivate()':
    the destructor: Python removes its C++
    Qt3DRender::QTextureImageDataPrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 11 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ Qt3DRender::QTextureImageDataPrivate is created at the first use,
    not by 'Qt3DRender::QTextureImageDataPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::QTextureImageDataPrivate back gives a
    copy the ritual made for Python, in a new cute
    Qt3DRender::QTextureImageDataPrivate.
  - Each name of Qt's Qt3DRender::QTextureImageDataPrivate that has no cute
    function yet, 'setCompressedFile', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DRender.QTextureImageData'])
  @overload(NoneType)
  def get(
      imageData: Optional[Qt3DRender.QTextureImageData],
  ) -> Optional[QTextureImageDataPrivate]:
    """
    Calls Qt's 'QTextureImageDataPrivate
    *Qt3DRender::QTextureImageDataPrivate::get(QTextureImageData
    *imageData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedataprivate.html#get

    Parameters
    ----------

    imageData : Optional[Qt3DRender.QTextureImageData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTextureImageDataPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextureImageDataPrivate
    #      *Qt3DRender::QTextureImageDataPrivate::get(QTextureImageData
    #      *imageData)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender24QTextureImageDataPrivate3getEPNS_17QTexture'
        'ImageDataE',
        CuteMixin._addressOf(imageData),
    )
    return QTextureImageDataPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QTextureImageDataPrivate'

  #  Qt's '~Qt3DRender::QTextureImageDataPrivate()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::QTextureImageDataPrivate
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender24QTextureImageDataPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, int)
  def data(self, layer: int, face: int, mipmapLevel: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::QTextureImageDataPrivate::data(int
    layer, int face, int mipmapLevel) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedataprivate.html#data

    Parameters
    ----------

    layer : int
      Passed on as it is.

    face : int
      Passed on as it is.

    mipmapLevel : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QTextureImageDataPrivate::data(int layer, int
    #      face, int mipmapLevel) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender24QTextureImageDataPrivate4dataEiii',
        layer, face, mipmapLevel,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def ddsLayerSize(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureImageDataPrivate::ddsLayerSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedataprivate.html
    """
    #  int Qt3DRender::QTextureImageDataPrivate::ddsLayerSize() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender24QTextureImageDataPrivate12ddsLayerSizeEv',
    )

  def ddsFaceSize(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureImageDataPrivate::ddsFaceSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedataprivate.html
    """
    #  int Qt3DRender::QTextureImageDataPrivate::ddsFaceSize() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender24QTextureImageDataPrivate11ddsFaceSizeEv',
    )

  @overload(int)
  def mipmapLevelSize(self, level: int) -> int:
    """
    Calls Qt's 'int Qt3DRender::QTextureImageDataPrivate::mipmapLevelSize(int
    level) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedataprivate.html

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  int Qt3DRender::QTextureImageDataPrivate::mipmapLevelSize(int level)
    #      const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender24QTextureImageDataPrivate15mipmapLevelSizeE'
        'i',
        level,
    )

  @overload(int, int, int)
  def ktxData(self, layer: int, face: int, mipmapLevel: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::QTextureImageDataPrivate::ktxData(int
    layer, int face, int mipmapLevel) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedataprivate.html#ktxData

    Parameters
    ----------

    layer : int
      Passed on as it is.

    face : int
      Passed on as it is.

    mipmapLevel : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::QTextureImageDataPrivate::ktxData(int layer,
    #      int face, int mipmapLevel) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender24QTextureImageDataPrivate7ktxDataEiii',
        layer, face, mipmapLevel,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray, int, bool)
  def setData(
      self,
      data: QByteArray,
      blockSize: int,
      isCompressed: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImageDataPrivate::setData(const
    QByteArray &data, int blockSize, bool isCompressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedataprivate.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    blockSize : int
      Passed on as it is.

    isCompressed : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureImageDataPrivate::setData(const QByteArray
    #      &data, int blockSize, bool isCompressed)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender24QTextureImageDataPrivate7setDataERK10QByteA'
        'rrayib',
        self._valueOf(data), blockSize, isCompressed,
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
    'Qt3DRender::QTextureImageDataPrivate::QTextureImageDataPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimagedataprivate.html
    """
    #  Qt3DRender::QTextureImageDataPrivate::QTextureImageDataPrivate()
    self._noteCreation(QTextureImageDataPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender24QTextureImageDataPrivateC1Ev',
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
  def setCompressedFile(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DRender::QTextureImageDataPrivate::setCompressedFile(const
    QString &source)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'Qt3DRender.QTextureImageDataPrivate.setCompressedFile' has no "
        "cute function yet. Qt's 'bool "
        "Qt3DRender::QTextureImageDataPrivate::setCompressedFile(const "
        "QString &source)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
