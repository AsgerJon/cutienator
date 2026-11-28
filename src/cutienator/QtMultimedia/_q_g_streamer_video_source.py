"""
QGStreamerVideoSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/spi/qgstreamervideosource.h, Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QGStreamerVideoSourcePrivate, QMediaCaptureSession
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMediaCaptureSession = WAIT['QMediaCaptureSession']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGStreamerVideoSource(QObject):
  """
  The cute side of Qt's QGStreamerVideoSource: a plain Python object standing
  in front of one C++ QGStreamerVideoSource.

  It is built on the cute 'QObject', as Qt's QGStreamerVideoSource is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGStreamerVideoSource that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'isActive',
  'gstBinDescription', 'captureSession', 'setActive', 'start', 'stop',
  'activeChanged', 'setCaptureSession', 'd_func'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGStreamerVideoSource::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QGStreamerVideoSource::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGStreamerVideoSource::QGStreamerVideoSource(GstElement
    *gstElement, QObject *parent)': names 'GstElement', which has no cute
    class yet.
  - Qt's 'QGStreamerVideoSource::~QGStreamerVideoSource()': the destructor:
    Python never removes a C++ QGStreamerVideoSource.
  - Qt's 'GstElement *QGStreamerVideoSource::gstElement() const': gives
    'struct _GstElement', which has no cute class yet.
  - Qt's 'QPlatformCamera *QGStreamerVideoSource::platformVideoSource()
    const': gives 'QPlatformCamera', which has no cute class yet.
  - Qt's 'const QGStreamerVideoSourcePrivate *QGStreamerVideoSource::d_func()
    const': takes in Python what 'QGStreamerVideoSourcePrivate
    *QGStreamerVideoSource::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 26 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QGStreamerVideoSource is created at the first use, not by
    'QGStreamerVideoSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGStreamerVideoSource.
  - Qt tells when it has removed the C++ QGStreamerVideoSource. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGStreamerVideoSource that has no cute function yet,
    'gstElement', 'platformVideoSource', holds a function that raises
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
    Calls Qt's 'QString QGStreamerVideoSource::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgstreamervideosource.html#tr

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
    #  QString QGStreamerVideoSource::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QGStreamerVideoSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGStreamerVideoSource'

  #  A C++ QGStreamerVideoSource Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGStreamerVideoSource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGStreamerVideoSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGStreamerVideoSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QGStreamerVideoSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QGStreamerVideoSource::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosource.html#isActive
    """
    #  bool QGStreamerVideoSource::isActive() const
    return self.uglySide.call('ritual_ZNK21QGStreamerVideoSource8isActiveEv')

  def gstBinDescription(self) -> str:
    """
    Calls Qt's 'QString QGStreamerVideoSource::gstBinDescription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosource.html#gstBinDescription

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGStreamerVideoSource::gstBinDescription() const
    return self.uglySide.call(
        'ritual_ZNK21QGStreamerVideoSource17gstBinDescriptionEv',
    )

  def captureSession(self) -> Optional[QMediaCaptureSession]:
    """
    Calls Qt's 'QMediaCaptureSession *QGStreamerVideoSource::captureSession()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosource.html#captureSession

    Returns
    -------

    Optional[QMediaCaptureSession]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMediaCaptureSession *QGStreamerVideoSource::captureSession() const
    address = self.uglySide.call(
        'ritual_ZNK21QGStreamerVideoSource14captureSessionEv',
    )
    from . import QMediaCaptureSession
    return QMediaCaptureSession._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QGStreamerVideoSource::setActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosource.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QGStreamerVideoSource::setActive(bool active)
    self.uglySide.call(
        'ritual_ZN21QGStreamerVideoSource9setActiveEb', active,
    )

  @overload(QMediaCaptureSession)
  @overload(NoneType)
  def setCaptureSession(
      self,
      session: Optional[QMediaCaptureSession],
  ) -> None:
    """
    Calls Qt's 'void
    QGStreamerVideoSource::setCaptureSession(QMediaCaptureSession *session)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosource.html#setCaptureSession

    Parameters
    ----------

    session : Optional[QMediaCaptureSession]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGStreamerVideoSource::setCaptureSession(QMediaCaptureSession
    #      *session)
    self.uglySide.call(
        'ritual_ZN21QGStreamerVideoSource17setCaptureSessionEP20QMediaCaptu'
        'reSession',
        self._addressOf(session),
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

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      gstBinDescription: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGStreamerVideoSource::QGStreamerVideoSource(const QString
    &gstBinDescription, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosource.html#QGStreamerVideoSource

    Parameters
    ----------

    gstBinDescription : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGStreamerVideoSource::QGStreamerVideoSource(const QString
    #      &gstBinDescription, QObject *parent)
    self._noteCreation(QGStreamerVideoSource, lambda: Rituals.call(
        'ritual_ZN21QGStreamerVideoSourceC1ERK7QStringP7QObject',
        gstBinDescription, self._addressOf(parent, 'QObject'),
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QGStreamerVideoSource::QGStreamerVideoSource(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosource.html#QGStreamerVideoSource

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGStreamerVideoSource::QGStreamerVideoSource(QObject *parent)
    self._noteCreation(QGStreamerVideoSource, lambda: Rituals.call(
        'ritual_ZN21QGStreamerVideoSourceC1EP7QObject',
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

  def start(self) -> None:
    """
    Calls Qt's 'void QGStreamerVideoSource::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qgstreamervideosource.html#start
    """
    #  void QGStreamerVideoSource::start()
    self.uglySide.call('ritual_ZN21QGStreamerVideoSource5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QGStreamerVideoSource::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qgstreamervideosource.html#stop
    """
    #  void QGStreamerVideoSource::stop()
    self.uglySide.call('ritual_ZN21QGStreamerVideoSource4stopEv')

  @overload(bool)
  def activeChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QGStreamerVideoSource::activeChanged(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgstreamervideosource.html#activeChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QGStreamerVideoSource::activeChanged(bool active)
    self.uglySide.call(
        'ritual_ZN21QGStreamerVideoSource13activeChangedEb', active,
    )

  def d_func(self) -> Optional[QGStreamerVideoSourcePrivate]:
    """
    Calls Qt's 'QGStreamerVideoSourcePrivate
    *QGStreamerVideoSource::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgstreamervideosource.html#d_func

    Returns
    -------

    Optional[QGStreamerVideoSourcePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGStreamerVideoSourcePrivate *QGStreamerVideoSource::d_func()
    address = self.uglySide.call('ritual_ZN21QGStreamerVideoSource6d_funcEv')
    from . import QGStreamerVideoSourcePrivate
    return QGStreamerVideoSourcePrivate._cuteAt(address)

  @staticmethod
  def gstElement(*__, **_) -> Never:
    """
    Qt's 'GstElement *QGStreamerVideoSource::gstElement() const': gives
    'struct _GstElement', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGStreamerVideoSource.gstElement' has no cute function yet. Qt's "
        "'GstElement *QGStreamerVideoSource::gstElement() const': gives "
        "'struct _GstElement', which has no cute class yet.")

  @staticmethod
  def platformVideoSource(*__, **_) -> Never:
    """
    Qt's 'QPlatformCamera *QGStreamerVideoSource::platformVideoSource()
    const': gives 'QPlatformCamera', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGStreamerVideoSource.platformVideoSource' has no cute function "
        "yet. Qt's 'QPlatformCamera "
        "*QGStreamerVideoSource::platformVideoSource() const': gives "
        "'QPlatformCamera', which has no cute class yet.")
