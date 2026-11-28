"""
QRhiResourceUpdateBatchPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhi_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QRhiResourceUpdateBatchPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QRhiBuffer, QRhiReadbackDescription, QRhiReadbackResult
  from . import QRhiResourceUpdateBatch, QRhiTexture
  from . import QRhiTextureCopyDescription, QRhiTextureUploadDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiResourceUpdateBatchPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiResourceUpdateBatchPrivate: a plain Python object
  standing in front of one C++ QRhiResourceUpdateBatchPrivate.

  C++ hands a QRhiResourceUpdateBatchPrivate around as a copy, so every C++
  QRhiResourceUpdateBatchPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QRhiResourceUpdateBatchPrivate that has a ritual and
  that Python can call so far, 5 names in all: 'free', 'merge',
  'hasOptimalCapacity', 'trimOpLists', 'get'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiResourceUpdateBatchPrivate::~QRhiResourceUpdateBatchPrivate()':
    the destructor: Python removes its C++ QRhiResourceUpdateBatchPrivate by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QRhiResourceUpdateBatchPrivate is created at the first use, not
    by 'QRhiResourceUpdateBatchPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiResourceUpdateBatchPrivate back gives a copy the
    ritual made for Python, in a new cute QRhiResourceUpdateBatchPrivate.
  """

  #  The classes Qt writes inside QRhiResourceUpdateBatchPrivate, each a
  #  class in here as in C++.

  class BufferOp(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiResourceUpdateBatchPrivate::BufferOp: a plain
    Python object standing in front of one C++
    QRhiResourceUpdateBatchPrivate::BufferOp.

    C++ hands a QRhiResourceUpdateBatchPrivate::BufferOp around as a copy, so
    every C++ QRhiResourceUpdateBatchPrivate::BufferOp behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QRhiResourceUpdateBatchPrivate::BufferOp that has
    a ritual and that Python can call so far, 5 names in all:
    'dynamicUpdate', 'changeToDynamicUpdate', 'staticUpload',
    'changeToStaticUpload', 'read'. None can be made from Python: one comes
    out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'BufferOp
      QRhiResourceUpdateBatchPrivate::BufferOp::dynamicUpdate(QRhiBuffer
      *buf, quint32 offset, quint32 size, const void *data)': names 'void',
      which has no cute class yet.
    - Qt's 'void
      QRhiResourceUpdateBatchPrivate::BufferOp::changeToDynamicUpdate(
      BufferOp *op, QRhiBuffer *buf, quint32 offset, quint32 size, const void
      *data)': names 'void', which has no cute class yet.
    - Qt's 'BufferOp
      QRhiResourceUpdateBatchPrivate::BufferOp::staticUpload(QRhiBuffer *buf,
      quint32 offset, quint32 size, const void *data)': names 'void', which
      has no cute class yet.
    - Qt's 'void
      QRhiResourceUpdateBatchPrivate::BufferOp::changeToStaticUpload(BufferOp
      *op, QRhiBuffer *buf, quint32 offset, quint32 size, const void *data)':
      names 'void', which has no cute class yet.
    - Qt's 'QRhiResourceUpdateBatchPrivate::BufferOp::~BufferOp()': the
      destructor: Python removes its C++
      QRhiResourceUpdateBatchPrivate::BufferOp by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QRhiResourceUpdateBatchPrivate::BufferOp is created at the
      first use, not by 'QRhiResourceUpdateBatchPrivate::BufferOp(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiResourceUpdateBatchPrivate::BufferOp back gives
      a copy the ritual made for Python, in a new cute
      QRhiResourceUpdateBatchPrivate::BufferOp.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QByteArray = WAIT['QByteArray']
      QRhiBuffer = WAIT['QRhiBuffer']
      QRhiReadbackResult = WAIT['QRhiReadbackResult']

    #  The enums Qt writes inside QRhiResourceUpdateBatchPrivate::BufferOp,
    #  each a class in here as in C++, and the names Qt has for the
    #  combinations of its flags enums.

    class Type(CuteNum):
      """
      The enum 'QRhiResourceUpdateBatchPrivate::BufferOp::Type' of Qt, with
      the 3 names Qt gives in it.
      """

      DynamicUpdate = Kee[int](0)
      StaticUpload = Kee[int](1)
      Read = Kee[int](2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(QRhiBuffer, int, QByteArray)
    @overload(NoneType, int, QByteArray)
    def dynamicUpdate(
        buf: Optional[QRhiBuffer],
        offset: int,
        data: QByteArray,
    ) -> QRhiResourceUpdateBatchPrivate.BufferOp:
      """
      Calls Qt's 'BufferOp
      QRhiResourceUpdateBatchPrivate::BufferOp::dynamicUpdate(QRhiBuffer
      *buf, quint32 offset, QByteArray data)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate-bufferop.html

      Parameters
      ----------

      buf : Optional[QRhiBuffer]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      offset : int
        Passed on as it is.

      data : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.

      Returns
      -------

      QRhiResourceUpdateBatchPrivate.BufferOp
        A new cute QRhiResourceUpdateBatchPrivate::BufferOp around the copy
        Qt gave back. Python owns it.
      """
      #  BufferOp QRhiResourceUpdateBatchPrivate::BufferOp::dynamicUpdate(
      #      QRhiBuffer *buf, quint32 offset, QByteArray data)
      address = Rituals.call(
          'ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp13dynamicUpdat'
          'eEP10QRhiBufferj10QByteArray',
          CuteMixin._addressOf(buf), offset, CuteMixin._valueOf(data),
      )
      return QRhiResourceUpdateBatchPrivate.BufferOp._cuteOwning(address)

    @staticmethod
    @overload(THIS, QRhiBuffer, int, QByteArray)
    @overload(THIS, NoneType, int, QByteArray)
    @overload(NoneType, QRhiBuffer, int, QByteArray)
    @overload(NoneType, NoneType, int, QByteArray)
    def changeToDynamicUpdate(
        op: Optional[QRhiResourceUpdateBatchPrivate.BufferOp],
        buf: Optional[QRhiBuffer],
        offset: int,
        data: QByteArray,
    ) -> None:
      """
      Calls Qt's 'void
      QRhiResourceUpdateBatchPrivate::BufferOp::changeToDynamicUpdate(
      BufferOp *op, QRhiBuffer *buf, quint32 offset, QByteArray data)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate-bufferop.html

      Parameters
      ----------

      op : Optional[QRhiResourceUpdateBatchPrivate.BufferOp]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      buf : Optional[QRhiBuffer]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      offset : int
        Passed on as it is.

      data : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.
      """
      #  void
      #      QRhiResourceUpdateBatchPrivate::BufferOp::changeToDynamicUpdate(
      #      BufferOp *op, QRhiBuffer *buf, quint32 offset, QByteArray data)
      Rituals.call(
          'ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp21changeToDyna'
          'micUpdateEPS0_P10QRhiBufferj10QByteArray',
          CuteMixin._addressOf(op), CuteMixin._addressOf(buf), offset,
          CuteMixin._valueOf(data),
      )

    @staticmethod
    @overload(QRhiBuffer, int, QByteArray)
    @overload(NoneType, int, QByteArray)
    def staticUpload(
        buf: Optional[QRhiBuffer],
        offset: int,
        data: QByteArray,
    ) -> QRhiResourceUpdateBatchPrivate.BufferOp:
      """
      Calls Qt's 'BufferOp
      QRhiResourceUpdateBatchPrivate::BufferOp::staticUpload(QRhiBuffer *buf,
      quint32 offset, QByteArray data)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate-bufferop.html

      Parameters
      ----------

      buf : Optional[QRhiBuffer]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      offset : int
        Passed on as it is.

      data : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.

      Returns
      -------

      QRhiResourceUpdateBatchPrivate.BufferOp
        A new cute QRhiResourceUpdateBatchPrivate::BufferOp around the copy
        Qt gave back. Python owns it.
      """
      #  BufferOp QRhiResourceUpdateBatchPrivate::BufferOp::staticUpload(
      #      QRhiBuffer *buf, quint32 offset, QByteArray data)
      address = Rituals.call(
          'ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp12staticUpload'
          'EP10QRhiBufferj10QByteArray',
          CuteMixin._addressOf(buf), offset, CuteMixin._valueOf(data),
      )
      return QRhiResourceUpdateBatchPrivate.BufferOp._cuteOwning(address)

    @staticmethod
    @overload(THIS, QRhiBuffer, int, QByteArray)
    @overload(THIS, NoneType, int, QByteArray)
    @overload(NoneType, QRhiBuffer, int, QByteArray)
    @overload(NoneType, NoneType, int, QByteArray)
    def changeToStaticUpload(
        op: Optional[QRhiResourceUpdateBatchPrivate.BufferOp],
        buf: Optional[QRhiBuffer],
        offset: int,
        data: QByteArray,
    ) -> None:
      """
      Calls Qt's 'void
      QRhiResourceUpdateBatchPrivate::BufferOp::changeToStaticUpload(BufferOp
      *op, QRhiBuffer *buf, quint32 offset, QByteArray data)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate-bufferop.html

      Parameters
      ----------

      op : Optional[QRhiResourceUpdateBatchPrivate.BufferOp]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      buf : Optional[QRhiBuffer]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      offset : int
        Passed on as it is.

      data : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.
      """
      #  void QRhiResourceUpdateBatchPrivate::BufferOp::changeToStaticUpload(
      #      BufferOp *op, QRhiBuffer *buf, quint32 offset, QByteArray data)
      Rituals.call(
          'ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp20changeToStat'
          'icUploadEPS0_P10QRhiBufferj10QByteArray',
          CuteMixin._addressOf(op), CuteMixin._addressOf(buf), offset,
          CuteMixin._valueOf(data),
      )

    @staticmethod
    @overload(QRhiBuffer, int, int, QRhiReadbackResult)
    @overload(QRhiBuffer, int, int, NoneType)
    @overload(NoneType, int, int, QRhiReadbackResult)
    @overload(NoneType, int, int, NoneType)
    def read(
        buf: Optional[QRhiBuffer],
        offset: int,
        size: int,
        result: Optional[QRhiReadbackResult],
    ) -> QRhiResourceUpdateBatchPrivate.BufferOp:
      """
      Calls Qt's 'BufferOp
      QRhiResourceUpdateBatchPrivate::BufferOp::read(QRhiBuffer *buf, quint32
      offset, quint32 size, QRhiReadbackResult *result)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate-bufferop.html

      Parameters
      ----------

      buf : Optional[QRhiBuffer]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      offset : int
        Passed on as it is.

      size : int
        Passed on as it is.

      result : Optional[QRhiReadbackResult]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      Returns
      -------

      QRhiResourceUpdateBatchPrivate.BufferOp
        A new cute QRhiResourceUpdateBatchPrivate::BufferOp around the copy
        Qt gave back. Python owns it.
      """
      #  BufferOp QRhiResourceUpdateBatchPrivate::BufferOp::read(QRhiBuffer
      #      *buf, quint32 offset, quint32 size, QRhiReadbackResult *result)
      address = Rituals.call(
          'ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOp4readEP10QRhiB'
          'ufferjjP18QRhiReadbackResult',
          CuteMixin._addressOf(buf), offset, size,
          CuteMixin._addressOf(result),
      )
      return QRhiResourceUpdateBatchPrivate.BufferOp._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiResourceUpdateBatchPrivate::BufferOp'

    #  Qt's '~QRhiResourceUpdateBatchPrivate::BufferOp()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QRhiResourceUpdateBatchPrivate::BufferOp behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN30QRhiResourceUpdateBatchPrivate8BufferOpD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class TextureOp(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiResourceUpdateBatchPrivate::TextureOp: a plain
    Python object standing in front of one C++
    QRhiResourceUpdateBatchPrivate::TextureOp.

    C++ hands a QRhiResourceUpdateBatchPrivate::TextureOp around as a copy,
    so every C++ QRhiResourceUpdateBatchPrivate::TextureOp behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QRhiResourceUpdateBatchPrivate::TextureOp that has
    a ritual and that Python can call so far, 4 names in all: 'upload',
    'copy', 'read', 'genMips'. None can be made from Python: one comes out of
    a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QRhiResourceUpdateBatchPrivate::TextureOp::~TextureOp()': the
      destructor: Python removes its C++
      QRhiResourceUpdateBatchPrivate::TextureOp by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QRhiResourceUpdateBatchPrivate::TextureOp is created at the
      first use, not by 'QRhiResourceUpdateBatchPrivate::TextureOp(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiResourceUpdateBatchPrivate::TextureOp back
      gives a copy the ritual made for Python, in a new cute
      QRhiResourceUpdateBatchPrivate::TextureOp.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QRhiReadbackDescription = WAIT['QRhiReadbackDescription']
      QRhiReadbackResult = WAIT['QRhiReadbackResult']
      QRhiTexture = WAIT['QRhiTexture']
      QRhiTextureCopyDescription = WAIT['QRhiTextureCopyDescription']
      QRhiTextureUploadDescription = WAIT['QRhiTextureUploadDescription']

    #  The enums Qt writes inside QRhiResourceUpdateBatchPrivate::TextureOp,
    #  each a class in here as in C++, and the names Qt has for the
    #  combinations of its flags enums.

    class Type(CuteNum):
      """
      The enum 'QRhiResourceUpdateBatchPrivate::TextureOp::Type' of Qt, with
      the 4 names Qt gives in it.
      """

      Upload = Kee[int](0)
      Copy = Kee[int](1)
      Read = Kee[int](2)
      GenMips = Kee[int](3)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(QRhiTexture, QRhiTextureUploadDescription)
    @overload(NoneType, QRhiTextureUploadDescription)
    def upload(
        tex: Optional[QRhiTexture],
        desc: QRhiTextureUploadDescription,
    ) -> QRhiResourceUpdateBatchPrivate.TextureOp:
      """
      Calls Qt's 'TextureOp
      QRhiResourceUpdateBatchPrivate::TextureOp::upload(QRhiTexture *tex,
      const QRhiTextureUploadDescription &desc)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate-textureop.html

      Parameters
      ----------

      tex : Optional[QRhiTexture]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      desc : QRhiTextureUploadDescription
        Passed on as a value: Qt reads the C++ QRhiTextureUploadDescription,
        which stays Python's own.

      Returns
      -------

      QRhiResourceUpdateBatchPrivate.TextureOp
        A new cute QRhiResourceUpdateBatchPrivate::TextureOp around the copy
        Qt gave back. Python owns it.
      """
      #  TextureOp
      #      QRhiResourceUpdateBatchPrivate::TextureOp::upload(QRhiTexture
      #      *tex, const QRhiTextureUploadDescription &desc)
      address = Rituals.call(
          'ritual_ZN30QRhiResourceUpdateBatchPrivate9TextureOp6uploadEP11QR'
          'hiTextureRK28QRhiTextureUploadDescription',
          CuteMixin._addressOf(tex), CuteMixin._valueOf(desc),
      )
      return QRhiResourceUpdateBatchPrivate.TextureOp._cuteOwning(address)

    @staticmethod
    @overload(QRhiTexture, QRhiTexture, QRhiTextureCopyDescription)
    @overload(QRhiTexture, NoneType, QRhiTextureCopyDescription)
    @overload(NoneType, QRhiTexture, QRhiTextureCopyDescription)
    @overload(NoneType, NoneType, QRhiTextureCopyDescription)
    def copy(
        dst: Optional[QRhiTexture],
        src: Optional[QRhiTexture],
        desc: QRhiTextureCopyDescription,
    ) -> QRhiResourceUpdateBatchPrivate.TextureOp:
      """
      Calls Qt's 'TextureOp
      QRhiResourceUpdateBatchPrivate::TextureOp::copy(QRhiTexture *dst,
      QRhiTexture *src, const QRhiTextureCopyDescription &desc)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate-textureop.html

      Parameters
      ----------

      dst : Optional[QRhiTexture]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      src : Optional[QRhiTexture]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      desc : QRhiTextureCopyDescription
        Passed on as a value: Qt reads the C++ QRhiTextureCopyDescription,
        which stays Python's own.

      Returns
      -------

      QRhiResourceUpdateBatchPrivate.TextureOp
        A new cute QRhiResourceUpdateBatchPrivate::TextureOp around the copy
        Qt gave back. Python owns it.
      """
      #  TextureOp
      #      QRhiResourceUpdateBatchPrivate::TextureOp::copy(QRhiTexture
      #      *dst, QRhiTexture *src, const QRhiTextureCopyDescription &desc)
      address = Rituals.call(
          'ritual_ZN30QRhiResourceUpdateBatchPrivate9TextureOp4copyEP11QRhi'
          'TextureS2_RK26QRhiTextureCopyDescription',
          CuteMixin._addressOf(dst), CuteMixin._addressOf(src),
          CuteMixin._valueOf(desc),
      )
      return QRhiResourceUpdateBatchPrivate.TextureOp._cuteOwning(address)

    @staticmethod
    @overload(QRhiReadbackDescription, QRhiReadbackResult)
    @overload(QRhiReadbackDescription, NoneType)
    def read(
        rb: QRhiReadbackDescription,
        result: Optional[QRhiReadbackResult],
    ) -> QRhiResourceUpdateBatchPrivate.TextureOp:
      """
      Calls Qt's 'TextureOp
      QRhiResourceUpdateBatchPrivate::TextureOp::read(const
      QRhiReadbackDescription &rb, QRhiReadbackResult *result)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate-textureop.html

      Parameters
      ----------

      rb : QRhiReadbackDescription
        Passed on as a value: Qt reads the C++ QRhiReadbackDescription, which
        stays Python's own.

      result : Optional[QRhiReadbackResult]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      Returns
      -------

      QRhiResourceUpdateBatchPrivate.TextureOp
        A new cute QRhiResourceUpdateBatchPrivate::TextureOp around the copy
        Qt gave back. Python owns it.
      """
      #  TextureOp QRhiResourceUpdateBatchPrivate::TextureOp::read(const
      #      QRhiReadbackDescription &rb, QRhiReadbackResult *result)
      address = Rituals.call(
          'ritual_ZN30QRhiResourceUpdateBatchPrivate9TextureOp4readERK23QRh'
          'iReadbackDescriptionP18QRhiReadbackResult',
          CuteMixin._valueOf(rb), CuteMixin._addressOf(result),
      )
      return QRhiResourceUpdateBatchPrivate.TextureOp._cuteOwning(address)

    @staticmethod
    @overload(QRhiTexture)
    @overload(NoneType)
    def genMips(
        tex: Optional[QRhiTexture],
    ) -> QRhiResourceUpdateBatchPrivate.TextureOp:
      """
      Calls Qt's 'TextureOp
      QRhiResourceUpdateBatchPrivate::TextureOp::genMips(QRhiTexture *tex)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate-textureop.html

      Parameters
      ----------

      tex : Optional[QRhiTexture]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      Returns
      -------

      QRhiResourceUpdateBatchPrivate.TextureOp
        A new cute QRhiResourceUpdateBatchPrivate::TextureOp around the copy
        Qt gave back. Python owns it.
      """
      #  TextureOp
      #      QRhiResourceUpdateBatchPrivate::TextureOp::genMips(QRhiTexture
      #      *tex)
      address = Rituals.call(
          'ritual_ZN30QRhiResourceUpdateBatchPrivate9TextureOp7genMipsEP11Q'
          'RhiTexture',
          CuteMixin._addressOf(tex),
      )
      return QRhiResourceUpdateBatchPrivate.TextureOp._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiResourceUpdateBatchPrivate::TextureOp'

    #  Qt's '~QRhiResourceUpdateBatchPrivate::TextureOp()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QRhiResourceUpdateBatchPrivate::TextureOp behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN30QRhiResourceUpdateBatchPrivate9TextureOpD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def get(
      b: Optional[QRhiResourceUpdateBatch],
  ) -> Optional[QRhiResourceUpdateBatchPrivate]:
    """
    Calls Qt's 'QRhiResourceUpdateBatchPrivate
    *QRhiResourceUpdateBatchPrivate::get(QRhiResourceUpdateBatch *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate.html#get

    Parameters
    ----------

    b : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRhiResourceUpdateBatchPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiResourceUpdateBatchPrivate
    #      *QRhiResourceUpdateBatchPrivate::get(QRhiResourceUpdateBatch *b)
    address = Rituals.call(
        'ritual_ZN30QRhiResourceUpdateBatchPrivate3getEP23QRhiResourceUpdat'
        'eBatch',
        CuteMixin._addressOf(b),
    )
    return QRhiResourceUpdateBatchPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiResourceUpdateBatchPrivate'

  #  Qt's '~QRhiResourceUpdateBatchPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QRhiResourceUpdateBatchPrivate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QRhiResourceUpdateBatchPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasOptimalCapacity(self) -> bool:
    """
    Calls Qt's 'bool QRhiResourceUpdateBatchPrivate::hasOptimalCapacity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate.html
    """
    #  bool QRhiResourceUpdateBatchPrivate::hasOptimalCapacity() const
    return self.uglySide.call(
        'ritual_ZNK30QRhiResourceUpdateBatchPrivate18hasOptimalCapacityEv',
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

  def free(self) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatchPrivate::free()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate.html#free
    """
    #  void QRhiResourceUpdateBatchPrivate::free()
    self.uglySide.call('ritual_ZN30QRhiResourceUpdateBatchPrivate4freeEv')

  @overload(THIS)
  @overload(NoneType)
  def merge(self, other: Optional[QRhiResourceUpdateBatchPrivate]) -> None:
    """
    Calls Qt's 'void
    QRhiResourceUpdateBatchPrivate::merge(QRhiResourceUpdateBatchPrivate
    *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate.html#merge

    Parameters
    ----------

    other : Optional[QRhiResourceUpdateBatchPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiResourceUpdateBatchPrivate::merge(
    #      QRhiResourceUpdateBatchPrivate *other)
    self.uglySide.call(
        'ritual_ZN30QRhiResourceUpdateBatchPrivate5mergeEPS_',
        self._addressOf(other),
    )

  def trimOpLists(self) -> None:
    """
    Calls Qt's 'void QRhiResourceUpdateBatchPrivate::trimOpLists()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiresourceupdatebatchprivate.html#trimOpLists
    """
    #  void QRhiResourceUpdateBatchPrivate::trimOpLists()
    self.uglySide.call(
        'ritual_ZN30QRhiResourceUpdateBatchPrivate11trimOpListsEv',
    )
