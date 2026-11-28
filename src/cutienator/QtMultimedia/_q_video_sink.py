"""
QVideoSink binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qvideosink.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QRhi
  from . import QPlatformVideoSink, QVideoFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']
  QVideoFrame = WAIT['QVideoFrame']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVideoSink(QObject):
  """
  The cute side of Qt's QVideoSink: a plain Python object standing in front
  of one C++ QVideoSink.

  It is built on the cute 'QObject', as Qt's QVideoSink is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVideoSink that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'rhi', 'setRhi',
  'videoSize', 'subtitleText', 'setSubtitleText', 'setVideoFrame',
  'videoFrame', 'platformVideoSink', 'videoFrameChanged',
  'subtitleTextChanged', 'videoSizeChanged', 'setSource'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVideoSink::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QVideoSink::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QVideoSink::~QVideoSink()': the destructor: Python never removes a
    C++ QVideoSink.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVideoSink is created at the first use, not by 'QVideoSink(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVideoSink.
  - Qt tells when it has removed the C++ QVideoSink. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QVideoSink::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#tr

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
    #  QString QVideoSink::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QVideoSink2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoSink'

  #  A C++ QVideoSink Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVideoSink'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVideoSink::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVideoSink::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QVideoSink10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QVideoSink::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QVideoSink::rhi() const
    address = self.uglySide.call('ritual_ZNK10QVideoSink3rhiEv')
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  def videoSize(self) -> QSize:
    """
    Calls Qt's 'QSize QVideoSink::videoSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#videoSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVideoSink::videoSize() const
    address = self.uglySide.call('ritual_ZNK10QVideoSink9videoSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def subtitleText(self) -> str:
    """
    Calls Qt's 'QString QVideoSink::subtitleText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#subtitleText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVideoSink::subtitleText() const
    return self.uglySide.call('ritual_ZNK10QVideoSink12subtitleTextEv')

  def videoFrame(self) -> QVideoFrame:
    """
    Calls Qt's 'QVideoFrame QVideoSink::videoFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#videoFrame

    Returns
    -------

    QVideoFrame
      A new cute QVideoFrame around the copy Qt gave back. Python owns it.
    """
    #  QVideoFrame QVideoSink::videoFrame() const
    address = self.uglySide.call('ritual_ZNK10QVideoSink10videoFrameEv')
    from . import QVideoFrame
    return QVideoFrame._cuteOwning(address)

  def platformVideoSink(self) -> Optional[QPlatformVideoSink]:
    """
    Calls Qt's 'QPlatformVideoSink *QVideoSink::platformVideoSink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#platformVideoSink

    Returns
    -------

    Optional[QPlatformVideoSink]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformVideoSink *QVideoSink::platformVideoSink() const
    address = self.uglySide.call(
        'ritual_ZNK10QVideoSink17platformVideoSinkEv',
    )
    from . import QPlatformVideoSink
    return QPlatformVideoSink._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhi)
  @overload(NoneType)
  def setRhi(self, rhi: Optional[QRhi]) -> None:
    """
    Calls Qt's 'void QVideoSink::setRhi(QRhi *rhi)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#setRhi

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVideoSink::setRhi(QRhi *rhi)
    self.uglySide.call(
        'ritual_ZN10QVideoSink6setRhiEP4QRhi', self._addressOf(rhi),
    )

  @overload(str)
  def setSubtitleText(self, subtitle: str) -> None:
    """
    Calls Qt's 'void QVideoSink::setSubtitleText(const QString &subtitle)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#setSubtitleText

    Parameters
    ----------

    subtitle : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QVideoSink::setSubtitleText(const QString &subtitle)
    self.uglySide.call(
        'ritual_ZN10QVideoSink15setSubtitleTextERK7QString', subtitle,
    )

  @overload(QVideoFrame)
  def setVideoFrame(self, frame: QVideoFrame) -> None:
    """
    Calls Qt's 'void QVideoSink::setVideoFrame(const QVideoFrame &frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#setVideoFrame

    Parameters
    ----------

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QVideoSink::setVideoFrame(const QVideoFrame &frame)
    self.uglySide.call(
        'ritual_ZN10QVideoSink13setVideoFrameERK11QVideoFrame',
        self._valueOf(frame),
    )

  @overload(QObject)
  @overload(NoneType)
  def setSource(self, source: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QVideoSink::setSource(QObject *source)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#setSource

    Parameters
    ----------

    source : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVideoSink::setSource(QObject *source)
    self.uglySide.call(
        'ritual_ZN10QVideoSink9setSourceEP7QObject',
        self._addressOf(source, 'QObject'),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QVideoSink::QVideoSink(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#QVideoSink

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVideoSink::QVideoSink(QObject *parent)
    self._noteCreation(QVideoSink, lambda: Rituals.call(
        'ritual_ZN10QVideoSinkC1EP7QObject',
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

  @overload(QVideoFrame)
  def videoFrameChanged(self, frame: QVideoFrame) -> None:
    """
    Calls Qt's 'void QVideoSink::videoFrameChanged(const QVideoFrame &frame)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#videoFrameChanged

    Parameters
    ----------

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QVideoSink::videoFrameChanged(const QVideoFrame &frame) const
    self.uglySide.call(
        'ritual_ZNK10QVideoSink17videoFrameChangedERK11QVideoFrame',
        self._valueOf(frame),
    )

  @overload(str)
  def subtitleTextChanged(self, subtitleText: str) -> None:
    """
    Calls Qt's 'void QVideoSink::subtitleTextChanged(const QString
    &subtitleText) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideosink.html#subtitleTextChanged

    Parameters
    ----------

    subtitleText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QVideoSink::subtitleTextChanged(const QString &subtitleText)
    #      const
    self.uglySide.call(
        'ritual_ZNK10QVideoSink19subtitleTextChangedERK7QString',
        subtitleText,
    )

  def videoSizeChanged(self) -> None:
    """
    Calls Qt's 'void QVideoSink::videoSizeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qvideosink.html#videoSizeChanged
    """
    #  void QVideoSink::videoSizeChanged()
    self.uglySide.call('ritual_ZN10QVideoSink16videoSizeChangedEv')
