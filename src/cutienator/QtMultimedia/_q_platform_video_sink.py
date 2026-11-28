"""
QPlatformVideoSink binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideosink_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformVideoSink to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect, QSize
  from ..QtGui import QRhi
  from . import QVideoFrame, QVideoSink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QRhi = WAIT['QRhi']
  QSize = WAIT['QSize']
  QVideoFrame = WAIT['QVideoFrame']
  QVideoSink = WAIT['QVideoSink']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformVideoSink(QObject):
  """
  The cute side of Qt's QPlatformVideoSink: a plain Python object standing in
  front of one C++ QPlatformVideoSink.

  It is built on the cute 'QObject', as Qt's QPlatformVideoSink is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformVideoSink that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'setRhi', 'setWinId',
  'setDisplayRect', 'setFullScreen', 'setAspectRatioMode', 'nativeSize',
  'setBrightness', 'setContrast', 'setHue', 'setSaturation', 'videoSink',
  'setNativeSize', 'setVideoFrame', 'currentVideoFrame', 'setSubtitleText',
  'subtitleText', 'onVideoFrameChanged', 'rhiChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformVideoSink::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPlatformVideoSink::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformVideoSink::~QPlatformVideoSink()': the destructor: Python
    never removes a C++ QPlatformVideoSink.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformVideoSink is created at the first use, not by
    'QPlatformVideoSink(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformVideoSink.
  - Qt tells when it has removed the C++ QPlatformVideoSink. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QPlatformVideoSink::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosink.html#tr

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
    #  QString QPlatformVideoSink::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QPlatformVideoSink2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformVideoSink'

  #  A C++ QPlatformVideoSink Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformVideoSink'

  #  The functions Qt calls itself that QPlatformVideoSink is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setRhi': (
          ('_ZN18QPlatformVideoSink6setRhiEP4QRhi',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhi'),
           )),
      ),
      'setWinId': (
          ('_ZN18QPlatformVideoSink8setWinIdEy',
           ('nothing', 'nothing', ''),
           (
               ('unsigned long long', 'number', ''),
           )),
      ),
      'setDisplayRect': (
          ('_ZN18QPlatformVideoSink14setDisplayRectERK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'setFullScreen': (
          ('_ZN18QPlatformVideoSink13setFullScreenEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setAspectRatioMode': (
          ('_ZN18QPlatformVideoSink18setAspectRatioModeEN2Qt15AspectRatioMo'
           'deE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtCore:Qt.AspectRatioMode'),
           )),
      ),
      'setBrightness': (
          ('_ZN18QPlatformVideoSink13setBrightnessEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'setContrast': (
          ('_ZN18QPlatformVideoSink11setContrastEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'setHue': (
          ('_ZN18QPlatformVideoSink6setHueEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'setSaturation': (
          ('_ZN18QPlatformVideoSink13setSaturationEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
      'onVideoFrameChanged': (
          ('_ZN18QPlatformVideoSink19onVideoFrameChangedERK11QVideoFrame',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtMultimedia:QVideoFrame'),
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
    Calls Qt's 'const QMetaObject *QPlatformVideoSink::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosink.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformVideoSink::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QPlatformVideoSink10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def nativeSize(self) -> QSize:
    """
    Calls Qt's 'QSize QPlatformVideoSink::nativeSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosink.html#nativeSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QPlatformVideoSink::nativeSize() const
    address = self.uglySide.call(
        'ritual_ZNK18QPlatformVideoSink10nativeSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def currentVideoFrame(self) -> QVideoFrame:
    """
    Calls Qt's 'QVideoFrame QPlatformVideoSink::currentVideoFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#currentVideoFrame

    Returns
    -------

    QVideoFrame
      A new cute QVideoFrame around the copy Qt gave back. Python owns it.
    """
    #  QVideoFrame QPlatformVideoSink::currentVideoFrame() const
    address = self.uglySide.call(
        'ritual_ZNK18QPlatformVideoSink17currentVideoFrameEv',
    )
    from . import QVideoFrame
    return QVideoFrame._cuteOwning(address)

  def subtitleText(self) -> str:
    """
    Calls Qt's 'QString QPlatformVideoSink::subtitleText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#subtitleText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformVideoSink::subtitleText() const
    return self.uglySide.call(
        'ritual_ZNK18QPlatformVideoSink12subtitleTextEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhi)
  @overload(NoneType)
  def setRhi(self, a0: Optional[QRhi]) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setRhi(QRhi *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosink.html#setRhi

    Parameters
    ----------

    a0 : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformVideoSink::setRhi(QRhi *a0)
    ritual = 'ritual_ZN18QPlatformVideoSink6setRhiEP4QRhi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPlatformVideoSink6setRhiEP4QRhi'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(int)
  def setWinId(self, a0: int) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setWinId(WId a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosink.html#setWinId

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QPlatformVideoSink::setWinId(WId a0)
    ritual = 'ritual_ZN18QPlatformVideoSink8setWinIdEy'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPlatformVideoSink8setWinIdEy'
    self.uglySide.call(ritual, a0)

  @overload(QRect)
  def setDisplayRect(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setDisplayRect(const QRect &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#setDisplayRect

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPlatformVideoSink::setDisplayRect(const QRect &a0)
    ritual = 'ritual_ZN18QPlatformVideoSink14setDisplayRectERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPlatformVideoSink14setDisplayRectERK5QRect'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(bool)
  def setFullScreen(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setFullScreen(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#setFullScreen

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPlatformVideoSink::setFullScreen(bool a0)
    ritual = 'ritual_ZN18QPlatformVideoSink13setFullScreenEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPlatformVideoSink13setFullScreenEb'
    self.uglySide.call(ritual, a0)

  @overload(Qt.AspectRatioMode)
  def setAspectRatioMode(self, a0: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void
    QPlatformVideoSink::setAspectRatioMode(Qt::AspectRatioMode a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#setAspectRatioMode

    Parameters
    ----------

    a0 : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QPlatformVideoSink::setAspectRatioMode(Qt::AspectRatioMode a0)
    ritual = (
        'ritual_ZN18QPlatformVideoSink18setAspectRatioModeEN2Qt15AspectRati'
        'oModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QPlatformVideoSink18setAspectRatioModeEN2Qt15Aspe'
          'ctRatioModeE')
    self.uglySide.call(ritual, a0.value)

  @overload(float)
  def setBrightness(self, a0: float) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setBrightness(float a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#setBrightness

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QPlatformVideoSink::setBrightness(float a0)
    ritual = 'ritual_ZN18QPlatformVideoSink13setBrightnessEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPlatformVideoSink13setBrightnessEf'
    self.uglySide.call(ritual, a0)

  @overload(float)
  def setContrast(self, a0: float) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setContrast(float a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#setContrast

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QPlatformVideoSink::setContrast(float a0)
    ritual = 'ritual_ZN18QPlatformVideoSink11setContrastEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPlatformVideoSink11setContrastEf'
    self.uglySide.call(ritual, a0)

  @overload(float)
  def setHue(self, a0: float) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setHue(float a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosink.html#setHue

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QPlatformVideoSink::setHue(float a0)
    ritual = 'ritual_ZN18QPlatformVideoSink6setHueEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPlatformVideoSink6setHueEf'
    self.uglySide.call(ritual, a0)

  @overload(float)
  def setSaturation(self, a0: float) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setSaturation(float a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#setSaturation

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QPlatformVideoSink::setSaturation(float a0)
    ritual = 'ritual_ZN18QPlatformVideoSink13setSaturationEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPlatformVideoSink13setSaturationEf'
    self.uglySide.call(ritual, a0)

  @overload(QSize)
  def setNativeSize(self, s: QSize) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setNativeSize(QSize s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#setNativeSize

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QPlatformVideoSink::setNativeSize(QSize s)
    self.uglySide.call(
        'ritual_ZN18QPlatformVideoSink13setNativeSizeE5QSize',
        self._valueOf(s),
    )

  @overload(QVideoFrame)
  def setVideoFrame(self, frame: QVideoFrame) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setVideoFrame(const QVideoFrame
    &frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#setVideoFrame

    Parameters
    ----------

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QPlatformVideoSink::setVideoFrame(const QVideoFrame &frame)
    self.uglySide.call(
        'ritual_ZN18QPlatformVideoSink13setVideoFrameERK11QVideoFrame',
        self._valueOf(frame),
    )

  @overload(str)
  def setSubtitleText(self, subtitleText: str) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::setSubtitleText(const QString
    &subtitleText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#setSubtitleText

    Parameters
    ----------

    subtitleText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlatformVideoSink::setSubtitleText(const QString &subtitleText)
    self.uglySide.call(
        'ritual_ZN18QPlatformVideoSink15setSubtitleTextERK7QString',
        subtitleText,
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

  @overload(QVideoSink)
  @overload(NoneType)
  def __init__(self, parent: Optional[QVideoSink]) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformVideoSink::QPlatformVideoSink(QVideoSink *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#QPlatformVideoSink

    Parameters
    ----------

    parent : Optional[QVideoSink]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlatformVideoSink::QPlatformVideoSink(QVideoSink *parent)
    self._noteCreation(QPlatformVideoSink, lambda: Rituals.call(
        'ritual_ZN18QPlatformVideoSinkC1EP10QVideoSink',
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

  def videoSink(self) -> Optional[QVideoSink]:
    """
    Calls Qt's 'QVideoSink *QPlatformVideoSink::videoSink()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosink.html#videoSink

    Returns
    -------

    Optional[QVideoSink]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVideoSink *QPlatformVideoSink::videoSink()
    address = self.uglySide.call('ritual_ZN18QPlatformVideoSink9videoSinkEv')
    from . import QVideoSink
    return QVideoSink._cuteAt(address)

  @overload(QVideoFrame)
  def onVideoFrameChanged(self, a0: QVideoFrame) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::onVideoFrameChanged(const
    QVideoFrame &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosink.html#onVideoFrameChanged

    Parameters
    ----------

    a0 : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QPlatformVideoSink::onVideoFrameChanged(const QVideoFrame &a0)
    ritual = (
        'ritual_ZN18QPlatformVideoSink19onVideoFrameChangedERK11QVideoFrame')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QPlatformVideoSink19onVideoFrameChangedERK11QVide'
          'oFrame')
    self.uglySide.call(ritual, self._valueOf(a0))

  def rhiChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformVideoSink::rhiChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosink.html#rhiChanged
    """
    #  void QPlatformVideoSink::rhiChanged()
    self.uglySide.call('ritual_ZN18QPlatformVideoSink10rhiChangedEv')
