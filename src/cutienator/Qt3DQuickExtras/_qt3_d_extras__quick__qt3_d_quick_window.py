"""
Qt3DExtras::Quick::Qt3DQuickWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickExtras/qt3dquickwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QWindow
from ..Qt3DCore import Qt3DCore
from ..Qt3DQuick import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QShowEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QShowEvent = WAIT['QShowEvent']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Qt3DQuickWindow(QWindow):
  """
  The cute side of Qt's Qt3DExtras::Quick::Qt3DQuickWindow: a plain Python
  object standing in front of one C++ Qt3DExtras::Quick::Qt3DQuickWindow.

  It is built on the cute 'QWindow', as Qt's
  Qt3DExtras::Quick::Qt3DQuickWindow is built on Qt's QWindow, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::Quick::Qt3DQuickWindow that has a ritual
  and that Python can call so far, 13 names in all: 'metaObject', 'tr',
  'registerAspect', 'setSource', 'engine', 'setCameraAspectRatioMode',
  'cameraAspectRatioMode', 'cameraAspectRatioModeChanged', 'showEvent',
  'onSceneCreated', 'setWindowSurface', 'setCameraAspectModeHelper',
  'updateCameraAspectRatio'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DExtras::Quick::Qt3DQuickWindow::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DExtras::Quick::Qt3DQuickWindow::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DExtras::Quick::Qt3DQuickWindow::~Qt3DQuickWindow()': the
    destructor: Python never removes a C++
    Qt3DExtras::Quick::Qt3DQuickWindow.
  - Qt's 'Qt3DQuickWindowPrivate
    *Qt3DExtras::Quick::Qt3DQuickWindow::d_func()': gives
    'Qt3DExtras::Quick::Qt3DQuickWindowPrivate', which has no cute class yet.
  - Qt's 'const Qt3DQuickWindowPrivate
    *Qt3DExtras::Quick::Qt3DQuickWindow::d_func() const': gives
    'Qt3DExtras::Quick::Qt3DQuickWindowPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DExtras::Quick::Qt3DQuickWindow is created at the first use,
    not by 'Qt3DExtras::Quick::Qt3DQuickWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::Quick::Qt3DQuickWindow.
  - Qt tells when it has removed the C++ Qt3DExtras::Quick::Qt3DQuickWindow.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DExtras::Quick::Qt3DQuickWindow, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class CameraAspectRatioMode(CuteNum):
    """
    The enum 'Qt3DExtras::Quick::Qt3DQuickWindow::CameraAspectRatioMode' of
    Qt, with the 2 names Qt gives in it.
    """

    AutomaticAspectRatio = Kee[int](0)
    UserAspectRatio = Kee[int](1)

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
    Calls Qt's 'QString Qt3DExtras::Quick::Qt3DQuickWindow::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html#tr

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
    #  QString Qt3DExtras::Quick::Qt3DQuickWindow::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::Quick::Qt3DQuickWindow'

  #  A C++ Qt3DExtras::Quick::Qt3DQuickWindow Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_Quick_Qt3DQuickWindow'

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
    *Qt3DExtras::Quick::Qt3DQuickWindow::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DExtras::Quick::Qt3DQuickWindow::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras5Quick15Qt3DQuickWindow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def engine(self) -> Optional[Qt3DCore.Quick.QQmlAspectEngine]:
    """
    Calls Qt's 'Qt3DCore::Quick::QQmlAspectEngine
    *Qt3DExtras::Quick::Qt3DQuickWindow::engine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html#engine

    Returns
    -------

    Optional[Qt3DCore.Quick.QQmlAspectEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::Quick::QQmlAspectEngine
    #      *Qt3DExtras::Quick::Qt3DQuickWindow::engine() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras5Quick15Qt3DQuickWindow6engineEv',
    )
    return Qt3DCore.Quick.QQmlAspectEngine._cuteAt(address)

  def cameraAspectRatioMode(self) -> CameraAspectRatioMode:
    """
    Calls Qt's 'CameraAspectRatioMode
    Qt3DExtras::Quick::Qt3DQuickWindow::cameraAspectRatioMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html

    Returns
    -------

    CameraAspectRatioMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'CameraAspectRatioMode(number)' gives.
    """
    #  CameraAspectRatioMode
    #      Qt3DExtras::Quick::Qt3DQuickWindow::cameraAspectRatioMode() const
    return Qt3DQuickWindow.CameraAspectRatioMode(self.uglySide.call(
        'ritual_ZNK10Qt3DExtras5Quick15Qt3DQuickWindow21cameraAspectRatioMo'
        'deEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DExtras::Quick::Qt3DQuickWindow::setSource(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DExtras::Quick::Qt3DQuickWindow::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(CameraAspectRatioMode)
  def setCameraAspectRatioMode(self, mode: CameraAspectRatioMode) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Quick::Qt3DQuickWindow::setCameraAspectRatioMode(
    CameraAspectRatioMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html

    Parameters
    ----------

    mode : CameraAspectRatioMode
      Passed on as its number.
    """
    #  void Qt3DExtras::Quick::Qt3DQuickWindow::setCameraAspectRatioMode(
    #      CameraAspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow24setCameraAspectRatio'
        'ModeENS1_21CameraAspectRatioModeE',
        mode.value,
    )

  @overload(QObject)
  @overload(NoneType)
  def setWindowSurface(self, rootObject: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Quick::Qt3DQuickWindow::setWindowSurface(QObject
    *rootObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html

    Parameters
    ----------

    rootObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::Quick::Qt3DQuickWindow::setWindowSurface(QObject
    #      *rootObject)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow16setWindowSurfaceEP7Q'
        'Object',
        self._addressOf(rootObject, 'QObject'),
    )

  def setCameraAspectModeHelper(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Quick::Qt3DQuickWindow::setCameraAspectModeHelper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html
    """
    #  void Qt3DExtras::Quick::Qt3DQuickWindow::setCameraAspectModeHelper()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow25setCameraAspectModeH'
        'elperEv',
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
  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWindow] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DExtras::Quick::Qt3DQuickWindow::Qt3DQuickWindow(QWindow *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DExtras::Quick::Qt3DQuickWindow::Qt3DQuickWindow(QWindow *parent)
    self._noteCreation(Qt3DQuickWindow, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindowC1EP7QWindow',
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

  @overload(WAIT['Qt3DCore.QAbstractAspect'])
  @overload(NoneType)
  def registerAspect(
      self,
      aspect: Optional[Qt3DCore.QAbstractAspect],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Quick::Qt3DQuickWindow::registerAspect(Qt3DCore::
    QAbstractAspect *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html

    Parameters
    ----------

    aspect : Optional[Qt3DCore.QAbstractAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::Quick::Qt3DQuickWindow::registerAspect(Qt3DCore::
    #      QAbstractAspect *aspect)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow14registerAspectEPN8Qt'
        '3DCore15QAbstractAspectE',
        self._addressOf(aspect),
    )

  @overload(str)
  def registerAspect(self, name: str) -> None:
    """
    Calls Qt's 'void Qt3DExtras::Quick::Qt3DQuickWindow::registerAspect(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DExtras::Quick::Qt3DQuickWindow::registerAspect(const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow14registerAspectERK7QS'
        'tring',
        name,
    )

  @overload(CameraAspectRatioMode)
  def cameraAspectRatioModeChanged(
      self,
      mode: CameraAspectRatioMode,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Quick::Qt3DQuickWindow::cameraAspectRatioModeChanged(
    CameraAspectRatioMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html

    Parameters
    ----------

    mode : CameraAspectRatioMode
      Passed on as its number.
    """
    #  void Qt3DExtras::Quick::Qt3DQuickWindow::cameraAspectRatioModeChanged(
    #      CameraAspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow28cameraAspectRatioMod'
        'eChangedENS1_21CameraAspectRatioModeE',
        mode.value,
    )

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, e: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void Qt3DExtras::Quick::Qt3DQuickWindow::showEvent(QShowEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html#showEvent

    Parameters
    ----------

    e : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::Quick::Qt3DQuickWindow::showEvent(QShowEvent *e)
    ritual = (
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow9showEventEP10QShowEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DExtras5Quick15Qt3DQuickWindow9showEventEP10QS'
          'howEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QObject)
  @overload(NoneType)
  def onSceneCreated(self, rootObject: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Quick::Qt3DQuickWindow::onSceneCreated(QObject *rootObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html

    Parameters
    ----------

    rootObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::Quick::Qt3DQuickWindow::onSceneCreated(QObject
    #      *rootObject)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow14onSceneCreatedEP7QOb'
        'ject',
        self._addressOf(rootObject, 'QObject'),
    )

  def updateCameraAspectRatio(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::Quick::Qt3DQuickWindow::updateCameraAspectRatio()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-quick-qt3dquickwindow.html
    """
    #  void Qt3DExtras::Quick::Qt3DQuickWindow::updateCameraAspectRatio()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras5Quick15Qt3DQuickWindow23updateCameraAspectRa'
        'tioEv',
    )
