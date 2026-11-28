"""
Qt3DRender::QTextureImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qtextureimage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextureImage(Qt3DRender.QAbstractTextureImage):
  """
  The cute side of Qt's Qt3DRender::QTextureImage: a plain Python object
  standing in front of one C++ Qt3DRender::QTextureImage.

  It is built on the cute 'Qt3DRender::QAbstractTextureImage', as Qt's
  Qt3DRender::QTextureImage is built on Qt's
  Qt3DRender::QAbstractTextureImage, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QTextureImage that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'source',
  'status', 'isMirrored', 'setSource', 'setMirrored', 'sourceChanged',
  'statusChanged', 'mirroredChanged', 'setStatus', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QTextureImage::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QTextureImage::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QTextureImage::~QTextureImage()': the destructor:
    Python never removes a C++ Qt3DRender::QTextureImage.
  - Qt's 'QTextureImageDataGeneratorPtr
    Qt3DRender::QTextureImage::dataGenerator() const': gives a type Python
    has no way to take yet.
  - Qt's 'const QTextureImagePrivate *Qt3DRender::QTextureImage::d_func()
    const': takes in Python what 'QTextureImagePrivate
    *Qt3DRender::QTextureImage::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QTextureImage is created at the first use, not by
    'Qt3DRender::QTextureImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QTextureImage.
  - Qt tells when it has removed the C++ Qt3DRender::QTextureImage. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QTextureImage, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Status(CuteNum):
    """
    The enum 'Qt3DRender::QTextureImage::Status' of Qt, with the 4 names Qt
    gives in it.
    """

    NULL = Kee[int](0)
    Loading = Kee[int](1)
    Ready = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString Qt3DRender::QTextureImage::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#tr

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
    #  QString Qt3DRender::QTextureImage::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender13QTextureImage2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QTextureImage'

  #  A C++ Qt3DRender::QTextureImage Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QTextureImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QTextureImage::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QTextureImage::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QTextureImage10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::QTextureImage::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::QTextureImage::source() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QTextureImage6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status Qt3DRender::QTextureImage::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status Qt3DRender::QTextureImage::status() const
    return QTextureImage.Status(self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QTextureImage6statusEv',
    ))

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QTextureImage::isMirrored() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#isMirrored
    """
    #  bool Qt3DRender::QTextureImage::isMirrored() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender13QTextureImage10isMirroredEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImage::setSource(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QTextureImage::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QTextureImage9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(bool)
  def setMirrored(self, mirrored: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImage::setMirrored(bool mirrored)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#setMirrored

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureImage::setMirrored(bool mirrored)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QTextureImage11setMirroredEb', mirrored,
    )

  @overload(Status)
  def setStatus(self, status: Status) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImage::setStatus(Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureImage::setStatus(Status status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QTextureImage9setStatusENS0_6StatusE',
        status.value,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QTextureImage::QTextureImage(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#QTextureImage

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QTextureImage::QTextureImage(Qt3DCore::QNode *parent)
    self._noteCreation(QTextureImage, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender13QTextureImageC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(QUrl)
  def sourceChanged(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImage::sourceChanged(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#sourceChanged

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QTextureImage::sourceChanged(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QTextureImage13sourceChangedERK4QUrl',
        self._valueOf(source),
    )

  @overload(Status)
  def statusChanged(self, status: Status) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImage::statusChanged(Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#statusChanged

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void Qt3DRender::QTextureImage::statusChanged(Status status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QTextureImage13statusChangedENS0_6StatusE',
        status.value,
    )

  @overload(bool)
  def mirroredChanged(self, mirrored: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QTextureImage::mirroredChanged(bool
    mirrored)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#mirroredChanged

    Parameters
    ----------

    mirrored : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QTextureImage::mirroredChanged(bool mirrored)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender13QTextureImage15mirroredChangedEb', mirrored,
    )

  def d_func(self) -> Optional[Qt3DRender.QTextureImagePrivate]:
    """
    Calls Qt's 'QTextureImagePrivate *Qt3DRender::QTextureImage::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qtextureimage.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QTextureImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextureImagePrivate *Qt3DRender::QTextureImage::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender13QTextureImage6d_funcEv',
    )
    return Qt3DRender.QTextureImagePrivate._cuteAt(address)
