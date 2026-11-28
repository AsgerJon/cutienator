"""
QPlatformVideoSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideosource_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformVideoSource to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QPlatformMediaCaptureSession, QVideoFrame, QVideoFrameFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformMediaCaptureSession = WAIT['QPlatformMediaCaptureSession']
  QVideoFrame = WAIT['QVideoFrame']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformVideoSource(QObject):
  """
  The cute side of Qt's QPlatformVideoSource: a plain Python object standing
  in front of one C++ QPlatformVideoSource.

  It is built on the cute 'QObject', as Qt's QPlatformVideoSource is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformVideoSource that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'setActive',
  'isActive', 'frameFormat', 'setCaptureSession', 'errorString', 'hasError',
  'newVideoFrame', 'activeChanged', 'errorChanged'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformVideoSource::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformVideoSource::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'std::optional<int> QPlatformVideoSource::ffmpegHWPixelFormat()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformVideoSource is created at the first use, not by
    'QPlatformVideoSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformVideoSource.
  - Qt tells when it has removed the C++ QPlatformVideoSource. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformVideoSource that has no cute function yet,
    'ffmpegHWPixelFormat', holds a function that raises
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
    Calls Qt's 'QString QPlatformVideoSource::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosource.html#tr

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
    #  QString QPlatformVideoSource::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QPlatformVideoSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformVideoSource'

  #  A C++ QPlatformVideoSource Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformVideoSource'

  #  The functions Qt calls itself that QPlatformVideoSource is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'ffmpegHWPixelFormat': (
          'std::optional<int> QPlatformVideoSource::ffmpegHWPixelFormat() '
          'const',
      ),
  }

  #  The functions Qt calls itself that QPlatformVideoSource is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setActive': (
          ('_ZN20QPlatformVideoSource9setActiveEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'isActive': (
          ('_ZNK20QPlatformVideoSource8isActiveEv',
           ('bool', 'number', ''),
           ()),
      ),
      'frameFormat': (
          ('_ZNK20QPlatformVideoSource11frameFormatEv',
           ('address', 'value', 'QtMultimedia:QVideoFrameFormat'),
           ()),
      ),
      'setCaptureSession': (
          ('_ZN20QPlatformVideoSource17setCaptureSessionEP28QPlatformMediaC'
           'aptureSession',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtMultimedia:QPlatformMediaCaptureSession'),
           )),
      ),
      'errorString': (
          ('_ZNK20QPlatformVideoSource11errorStringEv',
           ('address', 'text', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QPlatformVideoSource::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformVideoSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformVideoSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QPlatformVideoSource::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosource.html#isActive
    """
    #  bool QPlatformVideoSource::isActive() const
    return self.uglySide.call('ritual_ZNK20QPlatformVideoSource8isActiveEv')

  def frameFormat(self) -> QVideoFrameFormat:
    """
    Calls Qt's 'QVideoFrameFormat QPlatformVideoSource::frameFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosource.html#frameFormat

    Returns
    -------

    QVideoFrameFormat
      A new cute QVideoFrameFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QVideoFrameFormat QPlatformVideoSource::frameFormat() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformVideoSource11frameFormatEv',
    )
    from . import QVideoFrameFormat
    return QVideoFrameFormat._cuteOwning(address)

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QPlatformVideoSource::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosource.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlatformVideoSource::errorString() const
    return self.uglySide.call(
        'ritual_ZNK20QPlatformVideoSource11errorStringEv',
    )

  def hasError(self) -> bool:
    """
    Calls Qt's 'bool QPlatformVideoSource::hasError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformvideosource.html#hasError
    """
    #  bool QPlatformVideoSource::hasError() const
    return self.uglySide.call('ritual_ZNK20QPlatformVideoSource8hasErrorEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QPlatformVideoSource::setActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosource.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QPlatformVideoSource::setActive(bool active)
    self.uglySide.call('ritual_ZN20QPlatformVideoSource9setActiveEb', active)

  @overload(QPlatformMediaCaptureSession)
  @overload(NoneType)
  def setCaptureSession(
      self,
      a0: Optional[QPlatformMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformVideoSource::setCaptureSession(QPlatformMediaCaptureSession
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosource.html#setCaptureSession

    Parameters
    ----------

    a0 : Optional[QPlatformMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformVideoSource::setCaptureSession(
    #      QPlatformMediaCaptureSession *a0)
    ritual = (
        'ritual_ZN20QPlatformVideoSource17setCaptureSessionEP28QPlatformMed'
        'iaCaptureSession')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QPlatformVideoSource17setCaptureSessionEP28QPlatf'
          'ormMediaCaptureSession')
    self.uglySide.call(ritual, self._addressOf(a0))

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

  @overload(QVideoFrame)
  def newVideoFrame(self, a0: QVideoFrame) -> None:
    """
    Calls Qt's 'void QPlatformVideoSource::newVideoFrame(const QVideoFrame
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosource.html#newVideoFrame

    Parameters
    ----------

    a0 : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QPlatformVideoSource::newVideoFrame(const QVideoFrame &a0)
    self.uglySide.call(
        'ritual_ZN20QPlatformVideoSource13newVideoFrameERK11QVideoFrame',
        self._valueOf(a0),
    )

  @overload(bool)
  def activeChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPlatformVideoSource::activeChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosource.html#activeChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPlatformVideoSource::activeChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN20QPlatformVideoSource13activeChangedEb', a0,
    )

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformVideoSource::errorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformvideosource.html#errorChanged
    """
    #  void QPlatformVideoSource::errorChanged()
    self.uglySide.call('ritual_ZN20QPlatformVideoSource12errorChangedEv')

  @staticmethod
  def ffmpegHWPixelFormat(*__, **_) -> Never:
    """
    Qt's 'std::optional<int> QPlatformVideoSource::ffmpegHWPixelFormat()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformVideoSource.ffmpegHWPixelFormat' has no cute function "
        "yet. Qt's 'std::optional<int> "
        "QPlatformVideoSource::ffmpegHWPixelFormat() const': gives a type "
        "Python has no way to take yet.")
