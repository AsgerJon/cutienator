"""
QWaylandCompositor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandcompositor.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from . import QWaylandObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QMimeData
  from ..QtGui import QInputEvent, QWindow
  from . import QWaylandBufferRef, QWaylandClient, QWaylandKeyboard
  from . import QWaylandOutput, QWaylandPointer, QWaylandSeat
  from . import QWaylandSurface, QWaylandSurfaceGrabber, QWaylandTouch
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QInputEvent = WAIT['QInputEvent']
  QMimeData = WAIT['QMimeData']
  QWaylandBufferRef = WAIT['QWaylandBufferRef']
  QWaylandClient = WAIT['QWaylandClient']
  QWaylandOutput = WAIT['QWaylandOutput']
  QWaylandSeat = WAIT['QWaylandSeat']
  QWaylandSurface = WAIT['QWaylandSurface']
  QWaylandSurfaceGrabber = WAIT['QWaylandSurfaceGrabber']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandCompositor(QWaylandObject):
  """
  The cute side of Qt's QWaylandCompositor: a plain Python object standing in
  front of one C++ QWaylandCompositor.

  It is built on the cute 'QWaylandObject', as Qt's QWaylandCompositor is
  built on Qt's QWaylandObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandCompositor that has a ritual and that Python
  can call so far, 46 names in all: 'metaObject', 'tr', 'create',
  'isCreated', 'setSocketName', 'socketName', 'addSocketDescriptor',
  'nextSerial', 'clients', 'destroyClientForSurface', 'destroyClient',
  'surfaces', 'surfacesForClient', 'outputFor', 'defaultOutput',
  'setDefaultOutput', 'outputs', 'currentTimeMsecs',
  'setRetainedSelectionEnabled', 'retainedSelectionEnabled',
  'overrideSelection', 'defaultSeat', 'seatFor',
  'useHardwareIntegrationExtension', 'setUseHardwareIntegrationExtension',
  'grabSurface', 'processWaylandEvents', 'applicationStateChanged',
  'createdChanged', 'socketNameChanged', 'retainedSelectionChanged',
  'surfaceRequested', 'surfaceCreated', 'surfaceAboutToBeDestroyed',
  'subsurfaceChanged', 'defaultOutputChanged', 'defaultSeatChanged',
  'useHardwareIntegrationExtensionChanged', 'outputAdded', 'outputRemoved',
  'additionalShmFormatsChanged', 'retainedSelectionReceived', 'createSeat',
  'createPointerDevice', 'createKeyboardDevice', 'createTouchDevice'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandCompositor::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandCompositor::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandCompositorPrivate *QWaylandCompositor::d_func()': gives
    'QWaylandCompositorPrivate', which has no cute class yet.
  - Qt's 'const QWaylandCompositorPrivate *QWaylandCompositor::d_func()
    const': gives 'QWaylandCompositorPrivate', which has no cute class yet.
  - Qt's 'void QWaylandCompositor::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QWaylandCompositor::~QWaylandCompositor()': the destructor: Python
    never removes a C++ QWaylandCompositor.
  - Qt's '::wl_display *QWaylandCompositor::display() const': gives
    '::wl_display', which has no cute class yet.
  - Qt's 'QVector<ShmFormat> QWaylandCompositor::additionalShmFormats()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QWaylandCompositor::setAdditionalShmFormats(const
    QVector<ShmFormat> &additionalShmFormats)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QWaylandCompositor::QWaylandCompositor(QWaylandCompositorPrivate
    &dptr, QObject *parent)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 59 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandCompositor is created at the first use, not by
    'QWaylandCompositor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandCompositor.
  - Qt tells when it has removed the C++ QWaylandCompositor. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandCompositor that has no cute function yet,
    'additionalShmFormats', 'display', 'setAdditionalShmFormats', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWaylandCompositor, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ShmFormat(CuteNum):
    """
    The enum 'QWaylandCompositor::ShmFormat' of Qt, with the 15 names Qt
    gives in it.
    """

    ShmFormat_ARGB8888 = Kee[int](0)
    ShmFormat_XRGB8888 = Kee[int](1)
    ShmFormat_C8 = Kee[int](538982467)
    ShmFormat_XRGB4444 = Kee[int](842093144)
    ShmFormat_ARGB4444 = Kee[int](842093121)
    ShmFormat_XRGB1555 = Kee[int](892424792)
    ShmFormat_RGB565 = Kee[int](909199186)
    ShmFormat_RGB888 = Kee[int](875710290)
    ShmFormat_XBGR8888 = Kee[int](875709016)
    ShmFormat_ABGR8888 = Kee[int](875708993)
    ShmFormat_BGR888 = Kee[int](875710274)
    ShmFormat_XRGB2101010 = Kee[int](808669784)
    ShmFormat_XBGR2101010 = Kee[int](808665688)
    ShmFormat_ARGB2101010 = Kee[int](808669761)
    ShmFormat_ABGR2101010 = Kee[int](808665665)

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
    Calls Qt's 'QString QWaylandCompositor::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#tr

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
    #  QString QWaylandCompositor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QWaylandCompositor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandCompositor'

  #  A C++ QWaylandCompositor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandCompositor'

  #  The functions Qt calls itself that QWaylandCompositor is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'create': (
          ('_ZN18QWaylandCompositor6createEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'grabSurface': (
          ('_ZN18QWaylandCompositor11grabSurfaceEP22QWaylandSurfaceGrabberR'
           'K17QWaylandBufferRef',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtWaylandCompositor:QWaylandSurfaceGrabber'),
               ('address', 'value', 'QtWaylandCompositor:QWaylandBufferRef'),
           )),
      ),
      'retainedSelectionReceived': (
          ('_ZN18QWaylandCompositor25retainedSelectionReceivedEP9QMimeData',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QMimeData'),
           )),
      ),
      'createSeat': (
          ('_ZN18QWaylandCompositor10createSeatEv',
           ('address', 'address', 'QtWaylandCompositor:QWaylandSeat'),
           ()),
      ),
      'createPointerDevice': (
          ('_ZN18QWaylandCompositor19createPointerDeviceEP12QWaylandSeat',
           ('address', 'address', 'QtWaylandCompositor:QWaylandPointer'),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandSeat'),
           )),
      ),
      'createKeyboardDevice': (
          ('_ZN18QWaylandCompositor20createKeyboardDeviceEP12QWaylandSeat',
           ('address', 'address', 'QtWaylandCompositor:QWaylandKeyboard'),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandSeat'),
           )),
      ),
      'createTouchDevice': (
          ('_ZN18QWaylandCompositor17createTouchDeviceEP12QWaylandSeat',
           ('address', 'address', 'QtWaylandCompositor:QWaylandTouch'),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandSeat'),
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
    Calls Qt's 'const QMetaObject *QWaylandCompositor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandCompositor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QWaylandCompositor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isCreated(self) -> bool:
    """
    Calls Qt's 'bool QWaylandCompositor::isCreated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#isCreated
    """
    #  bool QWaylandCompositor::isCreated() const
    return self.uglySide.call('ritual_ZNK18QWaylandCompositor9isCreatedEv')

  def socketName(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QWaylandCompositor::socketName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#socketName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWaylandCompositor::socketName() const
    address = self.uglySide.call(
        'ritual_ZNK18QWaylandCompositor10socketNameEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def clients(self) -> QList[QWaylandClient]:
    """
    Calls Qt's 'QList<QWaylandClient *> QWaylandCompositor::clients() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#clients

    Returns
    -------

    QList[QWaylandClient]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWaylandClient *> QWaylandCompositor::clients() const
    address = self.uglySide.call('ritual_ZNK18QWaylandCompositor7clientsEv')
    from . import QWaylandClient
    return QList[QWaylandClient]._cuteOwning(address)

  def surfaces(self) -> QList[QWaylandSurface]:
    """
    Calls Qt's 'QList<QWaylandSurface *> QWaylandCompositor::surfaces()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#surfaces

    Returns
    -------

    QList[QWaylandSurface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWaylandSurface *> QWaylandCompositor::surfaces() const
    address = self.uglySide.call('ritual_ZNK18QWaylandCompositor8surfacesEv')
    from . import QWaylandSurface
    return QList[QWaylandSurface]._cuteOwning(address)

  @overload(QWaylandClient)
  @overload(NoneType)
  def surfacesForClient(
      self,
      client: Optional[QWaylandClient],
  ) -> QList[QWaylandSurface]:
    """
    Calls Qt's 'QList<QWaylandSurface *>
    QWaylandCompositor::surfacesForClient(QWaylandClient *client) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#surfacesForClient

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QWaylandSurface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWaylandSurface *>
    #      QWaylandCompositor::surfacesForClient(QWaylandClient *client)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QWaylandCompositor17surfacesForClientEP14QWaylandClien'
        't',
        self._addressOf(client),
    )
    from . import QWaylandSurface
    return QList[QWaylandSurface]._cuteOwning(address)

  @overload(QWindow)
  @overload(NoneType)
  def outputFor(self, window: Optional[QWindow]) -> Optional[QWaylandOutput]:
    """
    Calls Qt's 'QWaylandOutput *QWaylandCompositor::outputFor(QWindow
    *window) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#outputFor

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandOutput *QWaylandCompositor::outputFor(QWindow *window) const
    address = self.uglySide.call(
        'ritual_ZNK18QWaylandCompositor9outputForEP7QWindow',
        self._addressOf(window),
    )
    from . import QWaylandOutput
    return QWaylandOutput._cuteAt(address)

  def defaultOutput(self) -> Optional[QWaylandOutput]:
    """
    Calls Qt's 'QWaylandOutput *QWaylandCompositor::defaultOutput() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#defaultOutput

    Returns
    -------

    Optional[QWaylandOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandOutput *QWaylandCompositor::defaultOutput() const
    address = self.uglySide.call(
        'ritual_ZNK18QWaylandCompositor13defaultOutputEv',
    )
    from . import QWaylandOutput
    return QWaylandOutput._cuteAt(address)

  def outputs(self) -> QList[QWaylandOutput]:
    """
    Calls Qt's 'QList<QWaylandOutput *> QWaylandCompositor::outputs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#outputs

    Returns
    -------

    QList[QWaylandOutput]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWaylandOutput *> QWaylandCompositor::outputs() const
    address = self.uglySide.call('ritual_ZNK18QWaylandCompositor7outputsEv')
    from . import QWaylandOutput
    return QList[QWaylandOutput]._cuteOwning(address)

  def currentTimeMsecs(self) -> int:
    """
    Calls Qt's 'uint QWaylandCompositor::currentTimeMsecs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#currentTimeMsecs
    """
    #  uint QWaylandCompositor::currentTimeMsecs() const
    return self.uglySide.call(
        'ritual_ZNK18QWaylandCompositor16currentTimeMsecsEv',
    )

  def retainedSelectionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QWaylandCompositor::retainedSelectionEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#retainedSelectionEnabled
    """
    #  bool QWaylandCompositor::retainedSelectionEnabled() const
    return self.uglySide.call(
        'ritual_ZNK18QWaylandCompositor24retainedSelectionEnabledEv',
    )

  def defaultSeat(self) -> Optional[QWaylandSeat]:
    """
    Calls Qt's 'QWaylandSeat *QWaylandCompositor::defaultSeat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#defaultSeat

    Returns
    -------

    Optional[QWaylandSeat]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSeat *QWaylandCompositor::defaultSeat() const
    address = self.uglySide.call(
        'ritual_ZNK18QWaylandCompositor11defaultSeatEv',
    )
    from . import QWaylandSeat
    return QWaylandSeat._cuteAt(address)

  def useHardwareIntegrationExtension(self) -> bool:
    """
    Calls Qt's 'bool QWaylandCompositor::useHardwareIntegrationExtension()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html
    """
    #  bool QWaylandCompositor::useHardwareIntegrationExtension() const
    return self.uglySide.call(
        'ritual_ZNK18QWaylandCompositor31useHardwareIntegrationExtensionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setSocketName(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::setSocketName(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#setSocketName

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWaylandCompositor::setSocketName(const QByteArray &name)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor13setSocketNameERK10QByteArray',
        self._valueOf(name),
    )

  @overload(QWaylandOutput)
  @overload(NoneType)
  def setDefaultOutput(self, output: Optional[QWaylandOutput]) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::setDefaultOutput(QWaylandOutput
    *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#setDefaultOutput

    Parameters
    ----------

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::setDefaultOutput(QWaylandOutput *output)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor16setDefaultOutputEP14QWaylandOutput',
        self._addressOf(output),
    )

  @overload(bool)
  def setRetainedSelectionEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::setRetainedSelectionEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWaylandCompositor::setRetainedSelectionEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor27setRetainedSelectionEnabledEb',
        enabled,
    )

  @overload(bool)
  def setUseHardwareIntegrationExtension(self, use: bool) -> None:
    """
    Calls Qt's 'void
    QWaylandCompositor::setUseHardwareIntegrationExtension(bool use)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html

    Parameters
    ----------

    use : bool
      Passed on as it is.
    """
    #  void QWaylandCompositor::setUseHardwareIntegrationExtension(bool use)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor34setUseHardwareIntegrationExtensionE'
        'b',
        use,
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
    Notes what was given, for Qt's
    'QWaylandCompositor::QWaylandCompositor(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#QWaylandCompositor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandCompositor::QWaylandCompositor(QObject *parent)
    self._noteCreation(QWaylandCompositor, lambda: Rituals.call(
        'ritual_ZN18QWaylandCompositorC1EP7QObject',
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

  def create(self) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#create
    """
    #  void QWaylandCompositor::create()
    ritual = 'ritual_ZN18QWaylandCompositor6createEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QWaylandCompositor6createEv'
    self.uglySide.call(ritual)

  @overload(int)
  def addSocketDescriptor(self, fd: int) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::addSocketDescriptor(int fd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#addSocketDescriptor

    Parameters
    ----------

    fd : int
      Passed on as it is.
    """
    #  void QWaylandCompositor::addSocketDescriptor(int fd)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor19addSocketDescriptorEi', fd,
    )

  def nextSerial(self) -> int:
    """
    Calls Qt's 'uint32_t QWaylandCompositor::nextSerial()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#nextSerial
    """
    #  uint32_t QWaylandCompositor::nextSerial()
    return self.uglySide.call('ritual_ZN18QWaylandCompositor10nextSerialEv')

  @overload(QWaylandSurface)
  @overload(NoneType)
  def destroyClientForSurface(
      self,
      surface: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void
    QWaylandCompositor::destroyClientForSurface(QWaylandSurface *surface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#destroyClientForSurface

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::destroyClientForSurface(QWaylandSurface
    #      *surface)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor23destroyClientForSurfaceEP15QWayland'
        'Surface',
        self._addressOf(surface),
    )

  @overload(QWaylandClient)
  @overload(NoneType)
  def destroyClient(self, client: Optional[QWaylandClient]) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::destroyClient(QWaylandClient
    *client)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#destroyClient

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::destroyClient(QWaylandClient *client)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor13destroyClientEP14QWaylandClient',
        self._addressOf(client),
    )

  @overload(QMimeData)
  @overload(NoneType)
  def overrideSelection(self, data: Optional[QMimeData]) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::overrideSelection(const QMimeData
    *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#overrideSelection

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::overrideSelection(const QMimeData *data)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor17overrideSelectionEPK9QMimeData',
        self._addressOf(data),
    )

  @overload(QInputEvent)
  @overload(NoneType)
  def seatFor(
      self,
      inputEvent: Optional[QInputEvent],
  ) -> Optional[QWaylandSeat]:
    """
    Calls Qt's 'QWaylandSeat *QWaylandCompositor::seatFor(QInputEvent
    *inputEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#seatFor

    Parameters
    ----------

    inputEvent : Optional[QInputEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandSeat]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSeat *QWaylandCompositor::seatFor(QInputEvent *inputEvent)
    address = self.uglySide.call(
        'ritual_ZN18QWaylandCompositor7seatForEP11QInputEvent',
        self._addressOf(inputEvent),
    )
    from . import QWaylandSeat
    return QWaylandSeat._cuteAt(address)

  @overload(QWaylandSurfaceGrabber, QWaylandBufferRef)
  @overload(NoneType, QWaylandBufferRef)
  def grabSurface(
      self,
      grabber: Optional[QWaylandSurfaceGrabber],
      buffer: QWaylandBufferRef,
  ) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::grabSurface(QWaylandSurfaceGrabber
    *grabber, const QWaylandBufferRef &buffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#grabSurface

    Parameters
    ----------

    grabber : Optional[QWaylandSurfaceGrabber]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    buffer : QWaylandBufferRef
      Passed on as a value: Qt reads the C++ QWaylandBufferRef, which stays
      Python's own.
    """
    #  void QWaylandCompositor::grabSurface(QWaylandSurfaceGrabber *grabber,
    #      const QWaylandBufferRef &buffer)
    ritual = (
        'ritual_ZN18QWaylandCompositor11grabSurfaceEP22QWaylandSurfaceGrabb'
        'erRK17QWaylandBufferRef')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QWaylandCompositor11grabSurfaceEP22QWaylandSurfac'
          'eGrabberRK17QWaylandBufferRef')
    self.uglySide.call(
        ritual, self._addressOf(grabber), self._valueOf(buffer),
    )

  def processWaylandEvents(self) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::processWaylandEvents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#processWaylandEvents
    """
    #  void QWaylandCompositor::processWaylandEvents()
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor20processWaylandEventsEv',
    )

  @overload(Qt.ApplicationState)
  def applicationStateChanged(self, state: Qt.ApplicationState) -> None:
    """
    Calls Qt's 'void
    QWaylandCompositor::applicationStateChanged(Qt::ApplicationState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#applicationStateChanged

    Parameters
    ----------

    state : Qt.ApplicationState
      Passed on as its number.
    """
    #  void QWaylandCompositor::applicationStateChanged(Qt::ApplicationState
    #      state)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor23applicationStateChangedEN2Qt16Appli'
        'cationStateE',
        state.value,
    )

  def createdChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::createdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#createdChanged
    """
    #  void QWaylandCompositor::createdChanged()
    self.uglySide.call('ritual_ZN18QWaylandCompositor14createdChangedEv')

  @overload(QByteArray)
  def socketNameChanged(self, socketName: QByteArray) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::socketNameChanged(const QByteArray
    &socketName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#socketNameChanged

    Parameters
    ----------

    socketName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QWaylandCompositor::socketNameChanged(const QByteArray
    #      &socketName)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor17socketNameChangedERK10QByteArray',
        self._valueOf(socketName),
    )

  @overload(bool)
  def retainedSelectionChanged(self, retainedSelection: bool) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::retainedSelectionChanged(bool
    retainedSelection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#retainedSelectionChanged

    Parameters
    ----------

    retainedSelection : bool
      Passed on as it is.
    """
    #  void QWaylandCompositor::retainedSelectionChanged(bool
    #      retainedSelection)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor24retainedSelectionChangedEb',
        retainedSelection,
    )

  @overload(QWaylandClient, int, int)
  @overload(NoneType, int, int)
  def surfaceRequested(
      self,
      client: Optional[QWaylandClient],
      id: int,
      version: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::surfaceRequested(QWaylandClient
    *client, uint id, int version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#surfaceRequested

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    version : int
      Passed on as it is.
    """
    #  void QWaylandCompositor::surfaceRequested(QWaylandClient *client, uint
    #      id, int version)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor16surfaceRequestedEP14QWaylandClientj'
        'i',
        self._addressOf(client), id, version,
    )

  @overload(QWaylandSurface)
  @overload(NoneType)
  def surfaceCreated(self, surface: Optional[QWaylandSurface]) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::surfaceCreated(QWaylandSurface
    *surface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#surfaceCreated

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::surfaceCreated(QWaylandSurface *surface)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor14surfaceCreatedEP15QWaylandSurface',
        self._addressOf(surface),
    )

  @overload(QWaylandSurface)
  @overload(NoneType)
  def surfaceAboutToBeDestroyed(
      self,
      surface: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void
    QWaylandCompositor::surfaceAboutToBeDestroyed(QWaylandSurface *surface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#surfaceAboutToBeDestroyed

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::surfaceAboutToBeDestroyed(QWaylandSurface
    #      *surface)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor25surfaceAboutToBeDestroyedEP15QWayla'
        'ndSurface',
        self._addressOf(surface),
    )

  @overload(QWaylandSurface, QWaylandSurface)
  @overload(QWaylandSurface, NoneType)
  @overload(NoneType, QWaylandSurface)
  @overload(NoneType, NoneType)
  def subsurfaceChanged(
      self,
      child: Optional[QWaylandSurface],
      parent: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::subsurfaceChanged(QWaylandSurface
    *child, QWaylandSurface *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#subsurfaceChanged

    Parameters
    ----------

    child : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::subsurfaceChanged(QWaylandSurface *child,
    #      QWaylandSurface *parent)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor17subsurfaceChangedEP15QWaylandSurfac'
        'eS1_',
        self._addressOf(child), self._addressOf(parent),
    )

  def defaultOutputChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::defaultOutputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#defaultOutputChanged
    """
    #  void QWaylandCompositor::defaultOutputChanged()
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor20defaultOutputChangedEv',
    )

  @overload(QWaylandSeat, QWaylandSeat)
  @overload(QWaylandSeat, NoneType)
  @overload(NoneType, QWaylandSeat)
  @overload(NoneType, NoneType)
  def defaultSeatChanged(
      self,
      newDevice: Optional[QWaylandSeat],
      oldDevice: Optional[QWaylandSeat],
  ) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::defaultSeatChanged(QWaylandSeat
    *newDevice, QWaylandSeat *oldDevice)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#defaultSeatChanged

    Parameters
    ----------

    newDevice : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldDevice : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::defaultSeatChanged(QWaylandSeat *newDevice,
    #      QWaylandSeat *oldDevice)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor18defaultSeatChangedEP12QWaylandSeatS'
        '1_',
        self._addressOf(newDevice), self._addressOf(oldDevice),
    )

  def useHardwareIntegrationExtensionChanged(self) -> None:
    """
    Calls Qt's 'void
    QWaylandCompositor::useHardwareIntegrationExtensionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html
    """
    #  void QWaylandCompositor::useHardwareIntegrationExtensionChanged()
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor38useHardwareIntegrationExtensionChan'
        'gedEv',
    )

  @overload(QWaylandOutput)
  @overload(NoneType)
  def outputAdded(self, output: Optional[QWaylandOutput]) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::outputAdded(QWaylandOutput
    *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#outputAdded

    Parameters
    ----------

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::outputAdded(QWaylandOutput *output)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor11outputAddedEP14QWaylandOutput',
        self._addressOf(output),
    )

  @overload(QWaylandOutput)
  @overload(NoneType)
  def outputRemoved(self, output: Optional[QWaylandOutput]) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::outputRemoved(QWaylandOutput
    *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#outputRemoved

    Parameters
    ----------

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::outputRemoved(QWaylandOutput *output)
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor13outputRemovedEP14QWaylandOutput',
        self._addressOf(output),
    )

  def additionalShmFormatsChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::additionalShmFormatsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html
    """
    #  void QWaylandCompositor::additionalShmFormatsChanged()
    self.uglySide.call(
        'ritual_ZN18QWaylandCompositor27additionalShmFormatsChangedEv',
    )

  @overload(QMimeData)
  @overload(NoneType)
  def retainedSelectionReceived(self, mimeData: Optional[QMimeData]) -> None:
    """
    Calls Qt's 'void QWaylandCompositor::retainedSelectionReceived(QMimeData
    *mimeData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#retainedSelectionReceived

    Parameters
    ----------

    mimeData : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandCompositor::retainedSelectionReceived(QMimeData
    #      *mimeData)
    ritual = (
        'ritual_ZN18QWaylandCompositor25retainedSelectionReceivedEP9QMimeDa'
        'ta')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QWaylandCompositor25retainedSelectionReceivedEP9Q'
          'MimeData')
    self.uglySide.call(ritual, self._addressOf(mimeData))

  def createSeat(self) -> Optional[QWaylandSeat]:
    """
    Calls Qt's 'QWaylandSeat *QWaylandCompositor::createSeat()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandcompositor.html#createSeat

    Returns
    -------

    Optional[QWaylandSeat]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSeat *QWaylandCompositor::createSeat()
    ritual = 'ritual_ZN18QWaylandCompositor10createSeatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QWaylandCompositor10createSeatEv'
    address = self.uglySide.call(ritual)
    from . import QWaylandSeat
    return QWaylandSeat._cuteAt(address)

  @overload(QWaylandSeat)
  @overload(NoneType)
  def createPointerDevice(
      self,
      seat: Optional[QWaylandSeat],
  ) -> Optional[QWaylandPointer]:
    """
    Calls Qt's 'QWaylandPointer
    *QWaylandCompositor::createPointerDevice(QWaylandSeat *seat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#createPointerDevice

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandPointer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandPointer *QWaylandCompositor::createPointerDevice(QWaylandSeat
    #      *seat)
    ritual = (
        'ritual_ZN18QWaylandCompositor19createPointerDeviceEP12QWaylandSeat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QWaylandCompositor19createPointerDeviceEP12QWayla'
          'ndSeat')
    address = self.uglySide.call(ritual, self._addressOf(seat))
    from . import QWaylandPointer
    return QWaylandPointer._cuteAt(address)

  @overload(QWaylandSeat)
  @overload(NoneType)
  def createKeyboardDevice(
      self,
      seat: Optional[QWaylandSeat],
  ) -> Optional[QWaylandKeyboard]:
    """
    Calls Qt's 'QWaylandKeyboard
    *QWaylandCompositor::createKeyboardDevice(QWaylandSeat *seat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#createKeyboardDevice

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandKeyboard]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandKeyboard
    #      *QWaylandCompositor::createKeyboardDevice(QWaylandSeat *seat)
    ritual = (
        'ritual_ZN18QWaylandCompositor20createKeyboardDeviceEP12QWaylandSea'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QWaylandCompositor20createKeyboardDeviceEP12QWayl'
          'andSeat')
    address = self.uglySide.call(ritual, self._addressOf(seat))
    from . import QWaylandKeyboard
    return QWaylandKeyboard._cuteAt(address)

  @overload(QWaylandSeat)
  @overload(NoneType)
  def createTouchDevice(
      self,
      seat: Optional[QWaylandSeat],
  ) -> Optional[QWaylandTouch]:
    """
    Calls Qt's 'QWaylandTouch
    *QWaylandCompositor::createTouchDevice(QWaylandSeat *seat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandcompositor.html#createTouchDevice

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandTouch]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandTouch *QWaylandCompositor::createTouchDevice(QWaylandSeat
    #      *seat)
    ritual = (
        'ritual_ZN18QWaylandCompositor17createTouchDeviceEP12QWaylandSeat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QWaylandCompositor17createTouchDeviceEP12QWayland'
          'Seat')
    address = self.uglySide.call(ritual, self._addressOf(seat))
    from . import QWaylandTouch
    return QWaylandTouch._cuteAt(address)

  @staticmethod
  def additionalShmFormats(*__, **_) -> Never:
    """
    Qt's 'QVector<ShmFormat> QWaylandCompositor::additionalShmFormats()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandCompositor.additionalShmFormats' has no cute function "
        "yet. Qt's 'QVector<ShmFormat> "
        "QWaylandCompositor::additionalShmFormats() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def display(*__, **_) -> Never:
    """
    Qt's '::wl_display *QWaylandCompositor::display() const': gives
    '::wl_display', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandCompositor.display' has no cute function yet. Qt's "
        "'::wl_display *QWaylandCompositor::display() const': gives "
        "'::wl_display', which has no cute class yet.")

  @staticmethod
  def setAdditionalShmFormats(*__, **_) -> Never:
    """
    Qt's 'void QWaylandCompositor::setAdditionalShmFormats(const
    QVector<ShmFormat> &additionalShmFormats)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QWaylandCompositor.setAdditionalShmFormats' has no cute function "
        "yet. Qt's 'void QWaylandCompositor::setAdditionalShmFormats(const "
        "QVector<ShmFormat> &additionalShmFormats)': takes a type Python "
        "has no way to hand over yet.")
