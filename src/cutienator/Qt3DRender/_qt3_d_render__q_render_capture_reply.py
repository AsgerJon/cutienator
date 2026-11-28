"""
Qt3DRender::QRenderCaptureReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qrendercapture.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderCaptureReply(QObject):
  """
  The cute side of Qt's Qt3DRender::QRenderCaptureReply: a plain Python
  object standing in front of one C++ Qt3DRender::QRenderCaptureReply.

  It is built on the cute 'QObject', as Qt's Qt3DRender::QRenderCaptureReply
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderCaptureReply that has a ritual
  and that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'image', 'captureId', 'isComplete', 'saveImage', 'completed', 'd_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QRenderCaptureReply::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QRenderCaptureReply::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QRenderCaptureReplyPrivate
    *Qt3DRender::QRenderCaptureReply::d_func() const': takes in Python what
    'QRenderCaptureReplyPrivate *Qt3DRender::QRenderCaptureReply::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderCaptureReply is created at the first use, not
    by 'Qt3DRender::QRenderCaptureReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderCaptureReply.
  - Qt tells when it has removed the C++ Qt3DRender::QRenderCaptureReply.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DRender::QRenderCaptureReply::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapturereply.html#tr

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
    #  QString Qt3DRender::QRenderCaptureReply::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender19QRenderCaptureReply2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderCaptureReply'

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
    *Qt3DRender::QRenderCaptureReply::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapturereply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QRenderCaptureReply::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCaptureReply10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def image(self) -> QImage:
    """
    Calls Qt's 'QImage Qt3DRender::QRenderCaptureReply::image() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapturereply.html#image

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage Qt3DRender::QRenderCaptureReply::image() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCaptureReply5imageEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def captureId(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QRenderCaptureReply::captureId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapturereply.html#captureId
    """
    #  int Qt3DRender::QRenderCaptureReply::captureId() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCaptureReply9captureIdEv',
    )

  def isComplete(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QRenderCaptureReply::isComplete() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapturereply.html#isComplete
    """
    #  bool Qt3DRender::QRenderCaptureReply::isComplete() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCaptureReply10isCompleteEv',
    )

  @overload(str)
  def saveImage(self, fileName: str) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QRenderCaptureReply::saveImage(const QString
    &fileName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapturereply.html#saveImage

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool Qt3DRender::QRenderCaptureReply::saveImage(const QString
    #      &fileName) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender19QRenderCaptureReply9saveImageERK7QString',
        fileName,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRenderCaptureReply::QRenderCaptureReply(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapturereply.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QRenderCaptureReply::QRenderCaptureReply(QObject *parent)
    self._noteCreation(QRenderCaptureReply, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender19QRenderCaptureReplyC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def completed(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderCaptureReply::completed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapturereply.html#completed
    """
    #  void Qt3DRender::QRenderCaptureReply::completed()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderCaptureReply9completedEv',
    )

  def d_func(self) -> Optional[Qt3DRender.QRenderCaptureReplyPrivate]:
    """
    Calls Qt's 'QRenderCaptureReplyPrivate
    *Qt3DRender::QRenderCaptureReply::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrendercapturereply.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QRenderCaptureReplyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderCaptureReplyPrivate *Qt3DRender::QRenderCaptureReply::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderCaptureReply6d_funcEv',
    )
    return Qt3DRender.QRenderCaptureReplyPrivate._cuteAt(address)
