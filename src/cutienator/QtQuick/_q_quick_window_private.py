"""
QQuickWindowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickwindow_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickWindowPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QWindowPrivate
from . import QQuickWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QSize, QString
  from ..QtGui import QMouseEvent, QOpenGLContext, QPalette
  from ..QtGui import QRhiCommandBuffer, QRhiRenderTarget
  from . import QQuickDeliveryAgentPrivate, QQuickItem, QQuickPalette
  from . import QQuickRenderControl, QSGNode, QSGTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QPalette = WAIT['QPalette']
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']
  QQuickPalette = WAIT['QQuickPalette']
  QQuickRenderControl = WAIT['QQuickRenderControl']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWindowPrivate(QWindowPrivate):
  """
  The cute side of Qt's QQuickWindowPrivate: a plain Python object standing
  in front of one C++ QQuickWindowPrivate.

  It is built on the cute 'QWindowPrivate', as Qt's QQuickWindowPrivate is
  built on Qt's QWindowPrivate, and has everything that class has. Qt's
  QQuickWindowPrivate is built on Qt's
  QQuickPaletteProviderPrivateBase<QQuickWindow, QQuickWindowPrivate> as
  well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickWindowPrivate that has a ritual and that
  Python can call so far, 34 names in all: 'q_func', 'get', 'setPalette',
  'updateWindowPalette', 'updateChildrenPalettes', 'init',
  'deliveryAgentPrivate', 'updateCursor', 'clearFocusObject',
  'setFocusToTarget', 'maybeSynthesizeContextMenuEvent', 'dirtyItem',
  'cleanup', 'ensureCustomRenderTarget', 'setCustomCommandBuffer',
  'polishItems', 'forcePolish', 'invalidateFontData', 'syncSceneGraph',
  'renderSceneGraph', 'isRenderable', 'emitError',
  'createTextureFromNativeTexture', 'updateDirtyNodes', 'cleanupNodes',
  'cleanupNodesOnShutdown', 'updateDirtyNode', 'fireFrameSwapped',
  'fireAboutToStop', 'updateChildWindowStackingOrder', 'multiViewCount',
  'activeCustomRhiRenderTarget', 'rhiCreationFailureMessage',
  'openglContext'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickWindow *QQuickWindowPrivate::q_func() const': takes in
    Python what 'QQuickWindow *QQuickWindowPrivate::q_func()' takes.
  - Qt's 'const QQuickWindowPrivate *QQuickWindowPrivate::get(const
    QQuickWindow *c)': takes in Python what 'QQuickWindowPrivate
    *QQuickWindowPrivate::get(QQuickWindow *c)' takes.
  - Qt's 'QQuickWindowPrivate::~QQuickWindowPrivate()': the destructor:
    Python never removes a C++ QQuickWindowPrivate.
  - Qt's 'QQmlListProperty<QObject> QQuickWindowPrivate::data()': gives a
    type Python has no way to take yet.
  - Qt's 'std::pair<QQuickItem *, QQuickPointerHandler *>
    QQuickWindowPrivate::findCursorItemAndHandler(QQuickItem *item, const
    QPointF &localPos, const QPointF &scenePos) const': gives a type Python
    has no way to take yet.
  - Qt's 'void QQuickWindowPrivate::data_append(QQmlListProperty<QObject>
    *a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'qsizetype QQuickWindowPrivate::data_count(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QQuickWindowPrivate::data_at(QQmlListProperty<QObject>
    *a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void QQuickWindowPrivate::data_clear(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void QQuickWindowPrivate::data_removeLast(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void QQuickWindowPrivate::emitBeforeRenderPassRecording(void *ud)':
    names 'void', which has no cute class yet.
  - Qt's 'void QQuickWindowPrivate::emitAfterRenderPassRecording(void *ud)':
    names 'void', which has no cute class yet.
  - Qt's 'void QQuickWindowPrivate::runAndClearJobs(QList<QRunnable *>
    *jobs)': names 'QList<QRunnable *>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 52 functions Qt declares: 2 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickWindowPrivate is created at the first use, not by
    'QQuickWindowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWindowPrivate.
  - Each name of Qt's QQuickWindowPrivate that has no cute function yet,
    'data', 'data_append', 'data_at', 'data_clear', 'data_count',
    'data_removeLast', 'emitAfterRenderPassRecording',
    'emitBeforeRenderPassRecording', 'findCursorItemAndHandler',
    'runAndClearJobs', 'updateEffectiveOpacity',
    'updateEffectiveOpacityRoot', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickWindowPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class CustomEvents(CuteNum):
    """
    The enum 'QQuickWindowPrivate::CustomEvents' of Qt, with the 2 names Qt
    gives in it.
    """

    FullUpdateRequest = Kee[int](1001)
    TriggerContextCreationFailure = Kee[int](1002)

  class TextureFromNativeTextureFlag(CuteFlags):
    """
    The flags enum 'QQuickWindowPrivate::TextureFromNativeTextureFlag' of Qt,
    with the 1 names Qt gives in it. Qt names the type of its combinations
    'QQuickWindowPrivate::TextureFromNativeTextureFlags'.
    """

    NativeTextureIsExternalOES = 0x1

  TextureFromNativeTextureFlags = TextureFromNativeTextureFlag

  #  The classes Qt writes inside QQuickWindowPrivate, each a class in here
  #  as in C++.

  class Redirect(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickWindowPrivate::Redirect: a plain Python
    object standing in front of one C++ QQuickWindowPrivate::Redirect.

    C++ hands a QQuickWindowPrivate::Redirect around as a copy, so every C++
    QQuickWindowPrivate::Redirect behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuickWindowPrivate::Redirect yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickWindowPrivate::Redirect::~Redirect()': the destructor:
      Python removes its C++ QQuickWindowPrivate::Redirect by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQuickWindowPrivate::Redirect is created at the first use, not
      by 'QQuickWindowPrivate::Redirect(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickWindowPrivate::Redirect back gives a copy the
      ritual made for Python, in a new cute QQuickWindowPrivate::Redirect.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickWindowPrivate::Redirect'

    #  Qt's '~QQuickWindowPrivate::Redirect()'. Naming it makes this a value
    #  class: Python owns every C++ QQuickWindowPrivate::Redirect behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QQuickWindowPrivate8RedirectD1Ev'

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
  @overload(QQuickWindow)
  @overload(NoneType)
  def get(c: Optional[QQuickWindow]) -> Optional[QQuickWindowPrivate]:
    """
    Calls Qt's 'QQuickWindowPrivate *QQuickWindowPrivate::get(QQuickWindow
    *c)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowprivate.html#get

    Parameters
    ----------

    c : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickWindowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindowPrivate *QQuickWindowPrivate::get(QQuickWindow *c)
    address = Rituals.call(
        'ritual_ZN19QQuickWindowPrivate3getEP12QQuickWindow',
        CuteMixin._addressOf(c),
    )
    return QQuickWindowPrivate._cuteAt(address)

  @staticmethod
  @overload(str, QString, QString)
  @overload(str, QString, NoneType)
  @overload(str, NoneType, QString)
  @overload(str, NoneType, NoneType)
  def rhiCreationFailureMessage(
      backendName: str,
      translatedMessage: Optional[QString],
      untranslatedMessage: Optional[QString],
  ) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::rhiCreationFailureMessage(const
    QString &backendName, QString *translatedMessage, QString
    *untranslatedMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#rhiCreationFailureMessage

    Parameters
    ----------

    backendName : str
      Passed on as it is: a QString is made of it for the call.

    translatedMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    untranslatedMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowPrivate::rhiCreationFailureMessage(const QString
    #      &backendName, QString *translatedMessage, QString
    #      *untranslatedMessage)
    Rituals.call(
        'ritual_ZN19QQuickWindowPrivate25rhiCreationFailureMessageERK7QStri'
        'ngPS0_S3_',
        backendName, CuteMixin._addressOf(translatedMessage),
        CuteMixin._addressOf(untranslatedMessage),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWindowPrivate'

  #  A C++ QQuickWindowPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWindowPrivate'

  #  The functions Qt calls itself that QQuickWindowPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setPalette': (
          ('_ZN19QQuickWindowPrivate10setPaletteEP13QQuickPalette',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickPalette'),
           )),
      ),
      'updateChildrenPalettes': (
          ('_ZN19QQuickWindowPrivate22updateChildrenPalettesERK8QPalette',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPalette'),
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

  def deliveryAgentPrivate(self) -> Optional[QQuickDeliveryAgentPrivate]:
    """
    Calls Qt's 'QQuickDeliveryAgentPrivate
    *QQuickWindowPrivate::deliveryAgentPrivate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#deliveryAgentPrivate

    Returns
    -------

    Optional[QQuickDeliveryAgentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDeliveryAgentPrivate
    #      *QQuickWindowPrivate::deliveryAgentPrivate() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWindowPrivate20deliveryAgentPrivateEv',
    )
    from . import QQuickDeliveryAgentPrivate
    return QQuickDeliveryAgentPrivate._cuteAt(address)

  def isRenderable(self) -> bool:
    """
    Calls Qt's 'bool QQuickWindowPrivate::isRenderable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#isRenderable
    """
    #  bool QQuickWindowPrivate::isRenderable() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickWindowPrivate12isRenderableEv',
    )

  @overload(int, int, int, QSize, QQuickWindow.CreateTextureOptions)
  @overload(
      int, int, int, QSize, QQuickWindow.CreateTextureOptions,
      TextureFromNativeTextureFlags,
  )
  def createTextureFromNativeTexture(
      self,
      nativeObjectHandle: int,
      nativeLayoutOrState: int,
      nativeFormat: int,
      size: QSize,
      options: QQuickWindow.CreateTextureOptions,
      flags: TextureFromNativeTextureFlags = TextureFromNativeTextureFlags(),
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QQuickWindowPrivate::createTextureFromNativeTexture(quint64
    nativeObjectHandle, int nativeLayoutOrState, uint nativeFormat, const
    QSize &size, QQuickWindow::CreateTextureOptions options,
    TextureFromNativeTextureFlags flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html

    Parameters
    ----------

    nativeObjectHandle : int
      Passed on as it is.

    nativeLayoutOrState : int
      Passed on as it is.

    nativeFormat : int
      Passed on as it is.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QQuickWindow.CreateTextureOptions
      Passed on as its number.

    flags : TextureFromNativeTextureFlags
      Passed on as its number. May be left out, as in Qt: it is then
      TextureFromNativeTextureFlags().

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture
    #      *QQuickWindowPrivate::createTextureFromNativeTexture(quint64
    #      nativeObjectHandle, int nativeLayoutOrState, uint nativeFormat,
    #      const QSize &size, QQuickWindow::CreateTextureOptions options,
    #      TextureFromNativeTextureFlags flags) const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWindowPrivate30createTextureFromNativeTextureEyi'
        'jRK5QSize6QFlagsIN12QQuickWindow19CreateTextureOptionEES3_INS_28Te'
        'xtureFromNativeTextureFlagEE',
        nativeObjectHandle, nativeLayoutOrState, nativeFormat,
        self._valueOf(size), options.value, flags.value,
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  @overload(int, int, QSize, QQuickWindow.CreateTextureOptions)
  @overload(
      int, int, QSize, QQuickWindow.CreateTextureOptions,
      TextureFromNativeTextureFlags,
  )
  def createTextureFromNativeTexture(
      self,
      nativeObjectHandle: int,
      nativeLayoutOrState: int,
      size: QSize,
      options: QQuickWindow.CreateTextureOptions,
      flags: TextureFromNativeTextureFlags = TextureFromNativeTextureFlags(),
  ) -> Optional[QSGTexture]:
    """
    Calls Qt's 'QSGTexture
    *QQuickWindowPrivate::createTextureFromNativeTexture(quint64
    nativeObjectHandle, int nativeLayoutOrState, const QSize &size,
    QQuickWindow::CreateTextureOptions options, TextureFromNativeTextureFlags
    flags) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html

    Parameters
    ----------

    nativeObjectHandle : int
      Passed on as it is.

    nativeLayoutOrState : int
      Passed on as it is.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    options : QQuickWindow.CreateTextureOptions
      Passed on as its number.

    flags : TextureFromNativeTextureFlags
      Passed on as its number. May be left out, as in Qt: it is then
      TextureFromNativeTextureFlags().

    Returns
    -------

    Optional[QSGTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGTexture
    #      *QQuickWindowPrivate::createTextureFromNativeTexture(quint64
    #      nativeObjectHandle, int nativeLayoutOrState, const QSize &size,
    #      QQuickWindow::CreateTextureOptions options,
    #      TextureFromNativeTextureFlags flags) const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWindowPrivate30createTextureFromNativeTextureEyi'
        'RK5QSize6QFlagsIN12QQuickWindow19CreateTextureOptionEES3_INS_28Tex'
        'tureFromNativeTextureFlagEE',
        nativeObjectHandle, nativeLayoutOrState, self._valueOf(size),
        options.value, flags.value,
    )
    from . import QSGTexture
    return QSGTexture._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickPalette)
  @overload(NoneType)
  def setPalette(self, p: Optional[QQuickPalette]) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::setPalette(QQuickPalette *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#setPalette

    Parameters
    ----------

    p : Optional[QQuickPalette]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowPrivate::setPalette(QQuickPalette *p)
    ritual = 'ritual_ZN19QQuickWindowPrivate10setPaletteEP13QQuickPalette'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickWindowPrivate10setPaletteEP13QQuickPalette')
    self.uglySide.call(ritual, self._addressOf(p))

  @overload(QWindowPrivate.FocusTarget, Qt.FocusReason)
  def setFocusToTarget(
      self,
      a0: QWindowPrivate.FocusTarget,
      a1: Qt.FocusReason,
  ) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::setFocusToTarget(FocusTarget a0,
    Qt::FocusReason a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#setFocusToTarget

    Parameters
    ----------

    a0 : QWindowPrivate.FocusTarget
      Passed on as its number.

    a1 : Qt.FocusReason
      Passed on as its number.
    """
    #  void QQuickWindowPrivate::setFocusToTarget(FocusTarget a0,
    #      Qt::FocusReason a1)
    ritual = (
        'ritual_ZN19QQuickWindowPrivate16setFocusToTargetEN14QWindowPrivate'
        '11FocusTargetEN2Qt11FocusReasonE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickWindowPrivate16setFocusToTargetEN14QWindowP'
          'rivate11FocusTargetEN2Qt11FocusReasonE')
    self.uglySide.call(ritual, a0.value, a1.value)

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def setCustomCommandBuffer(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void
    QQuickWindowPrivate::setCustomCommandBuffer(QRhiCommandBuffer *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#setCustomCommandBuffer

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowPrivate::setCustomCommandBuffer(QRhiCommandBuffer
    #      *cb)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate22setCustomCommandBufferEP17QRhiComm'
        'andBuffer',
        self._addressOf(cb),
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
    'QQuickWindowPrivate::QQuickWindowPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#QQuickWindowPrivate
    """
    #  QQuickWindowPrivate::QQuickWindowPrivate()
    self._noteCreation(QQuickWindowPrivate, lambda: Rituals.call(
        'ritual_ZN19QQuickWindowPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QQuickWindowPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowprivate.html#q_func

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QQuickWindowPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QQuickWindowPrivate6q_funcEv')
    return QQuickWindow._cuteAt(address)

  def updateWindowPalette(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::updateWindowPalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#updateWindowPalette
    """
    #  void QQuickWindowPrivate::updateWindowPalette()
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate19updateWindowPaletteEv',
    )

  @overload(QPalette)
  def updateChildrenPalettes(self, parentPalette: QPalette) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::updateChildrenPalettes(const
    QPalette &parentPalette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#updateChildrenPalettes

    Parameters
    ----------

    parentPalette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QQuickWindowPrivate::updateChildrenPalettes(const QPalette
    #      &parentPalette)
    ritual = (
        'ritual_ZN19QQuickWindowPrivate22updateChildrenPalettesERK8QPalette')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickWindowPrivate22updateChildrenPalettesERK8QP'
          'alette')
    self.uglySide.call(ritual, self._valueOf(parentPalette))

  @overload(QQuickWindow)
  @overload(NoneType)
  @overload(QQuickWindow, QQuickRenderControl)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QQuickRenderControl)
  @overload(NoneType, NoneType)
  def init(
      self,
      a0: Optional[QQuickWindow],
      control: Optional[QQuickRenderControl] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::init(QQuickWindow *a0,
    QQuickRenderControl *control)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowprivate.html#init

    Parameters
    ----------

    a0 : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    control : Optional[QQuickRenderControl]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickWindowPrivate::init(QQuickWindow *a0, QQuickRenderControl
    #      *control)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate4initEP12QQuickWindowP19QQuickRender'
        'Control',
        self._addressOf(a0), self._addressOf(control),
    )

  @overload(QPointF)
  @overload(QPointF, QQuickItem)
  @overload(QPointF, NoneType)
  def updateCursor(
      self,
      scenePos: QPointF,
      rootItem: Optional[QQuickItem] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::updateCursor(const QPointF
    &scenePos, QQuickItem *rootItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#updateCursor

    Parameters
    ----------

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    rootItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickWindowPrivate::updateCursor(const QPointF &scenePos,
    #      QQuickItem *rootItem)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate12updateCursorERK7QPointFP10QQuickIt'
        'em',
        self._valueOf(scenePos, 'QPointF'), self._addressOf(rootItem),
    )

  def clearFocusObject(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::clearFocusObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#clearFocusObject
    """
    #  void QQuickWindowPrivate::clearFocusObject()
    ritual = 'ritual_ZN19QQuickWindowPrivate16clearFocusObjectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickWindowPrivate16clearFocusObjectEv'
    self.uglySide.call(ritual)

  @overload(QMouseEvent)
  @overload(NoneType)
  def maybeSynthesizeContextMenuEvent(
      self,
      event: Optional[QMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN19QQuickWindowPrivate31maybeSynthesizeContextMenuEventEP1'
        '1QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickWindowPrivate31maybeSynthesizeContextMenuEv'
          'entEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem)
  @overload(NoneType)
  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  def dirtyItem(
      self,
      item: Optional[QQuickItem],
      maySkipUpdate: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::dirtyItem(QQuickItem *item, bool
    maySkipUpdate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowprivate.html#dirtyItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    maySkipUpdate : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickWindowPrivate::dirtyItem(QQuickItem *item, bool
    #      maySkipUpdate)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate9dirtyItemEP10QQuickItemb',
        self._addressOf(item), maySkipUpdate,
    )

  @overload(QSGNode)
  @overload(NoneType)
  def cleanup(self, a0: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::cleanup(QSGNode *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowprivate.html#cleanup

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowPrivate::cleanup(QSGNode *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate7cleanupEP7QSGNode',
        self._addressOf(a0, 'QSGNode'),
    )

  def ensureCustomRenderTarget(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::ensureCustomRenderTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#ensureCustomRenderTarget
    """
    #  void QQuickWindowPrivate::ensureCustomRenderTarget()
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate24ensureCustomRenderTargetEv',
    )

  def polishItems(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::polishItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#polishItems
    """
    #  void QQuickWindowPrivate::polishItems()
    self.uglySide.call('ritual_ZN19QQuickWindowPrivate11polishItemsEv')

  def forcePolish(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::forcePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#forcePolish
    """
    #  void QQuickWindowPrivate::forcePolish()
    self.uglySide.call('ritual_ZN19QQuickWindowPrivate11forcePolishEv')

  @overload(QQuickItem)
  @overload(NoneType)
  def invalidateFontData(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::invalidateFontData(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#invalidateFontData

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowPrivate::invalidateFontData(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate18invalidateFontDataEP10QQuickItem',
        self._addressOf(item),
    )

  def syncSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::syncSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#syncSceneGraph
    """
    #  void QQuickWindowPrivate::syncSceneGraph()
    self.uglySide.call('ritual_ZN19QQuickWindowPrivate14syncSceneGraphEv')

  def renderSceneGraph(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::renderSceneGraph()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#renderSceneGraph
    """
    #  void QQuickWindowPrivate::renderSceneGraph()
    self.uglySide.call('ritual_ZN19QQuickWindowPrivate16renderSceneGraphEv')

  @overload(QQuickWindow.SceneGraphError, str)
  def emitError(self, error: QQuickWindow.SceneGraphError, msg: str) -> bool:
    """
    Calls Qt's 'bool
    QQuickWindowPrivate::emitError(QQuickWindow::SceneGraphError error, const
    QString &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowprivate.html#emitError

    Parameters
    ----------

    error : QQuickWindow.SceneGraphError
      Passed on as its number.

    msg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickWindowPrivate::emitError(QQuickWindow::SceneGraphError
    #      error, const QString &msg)
    return self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate9emitErrorEN12QQuickWindow15SceneGra'
        'phErrorERK7QString',
        error.value, msg,
    )

  def updateDirtyNodes(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::updateDirtyNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#updateDirtyNodes
    """
    #  void QQuickWindowPrivate::updateDirtyNodes()
    self.uglySide.call('ritual_ZN19QQuickWindowPrivate16updateDirtyNodesEv')

  def cleanupNodes(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::cleanupNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#cleanupNodes
    """
    #  void QQuickWindowPrivate::cleanupNodes()
    self.uglySide.call('ritual_ZN19QQuickWindowPrivate12cleanupNodesEv')

  @overload()
  def cleanupNodesOnShutdown(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::cleanupNodesOnShutdown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#cleanupNodesOnShutdown
    """
    #  void QQuickWindowPrivate::cleanupNodesOnShutdown()
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate22cleanupNodesOnShutdownEv',
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def cleanupNodesOnShutdown(a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::cleanupNodesOnShutdown(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#cleanupNodesOnShutdown

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowPrivate::cleanupNodesOnShutdown(QQuickItem *a0)
    Rituals.call(
        'ritual_ZN19QQuickWindowPrivate22cleanupNodesOnShutdownEP10QQuickIt'
        'em',
        CuteMixin._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def updateDirtyNode(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::updateDirtyNode(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#updateDirtyNode

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowPrivate::updateDirtyNode(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate15updateDirtyNodeEP10QQuickItem',
        self._addressOf(a0),
    )

  def fireFrameSwapped(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::fireFrameSwapped()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#fireFrameSwapped
    """
    #  void QQuickWindowPrivate::fireFrameSwapped()
    self.uglySide.call('ritual_ZN19QQuickWindowPrivate16fireFrameSwappedEv')

  def fireAboutToStop(self) -> None:
    """
    Calls Qt's 'void QQuickWindowPrivate::fireAboutToStop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#fireAboutToStop
    """
    #  void QQuickWindowPrivate::fireAboutToStop()
    self.uglySide.call('ritual_ZN19QQuickWindowPrivate15fireAboutToStopEv')

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def updateChildWindowStackingOrder(
      self,
      item: Optional[QQuickItem] = None,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickWindowPrivate::updateChildWindowStackingOrder(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickWindowPrivate::updateChildWindowStackingOrder(QQuickItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate30updateChildWindowStackingOrderEP10'
        'QQuickItem',
        self._addressOf(item),
    )

  def multiViewCount(self) -> int:
    """
    Calls Qt's 'int QQuickWindowPrivate::multiViewCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#multiViewCount
    """
    #  int QQuickWindowPrivate::multiViewCount()
    return self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate14multiViewCountEv',
    )

  def activeCustomRhiRenderTarget(self) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget
    *QQuickWindowPrivate::activeCustomRhiRenderTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget *QQuickWindowPrivate::activeCustomRhiRenderTarget()
    address = self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate27activeCustomRhiRenderTargetEv',
    )
    from ..QtGui import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

  def openglContext(self) -> Optional[QOpenGLContext]:
    """
    Calls Qt's 'QOpenGLContext *QQuickWindowPrivate::openglContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowprivate.html#openglContext

    Returns
    -------

    Optional[QOpenGLContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContext *QQuickWindowPrivate::openglContext()
    address = self.uglySide.call(
        'ritual_ZN19QQuickWindowPrivate13openglContextEv',
    )
    from ..QtGui import QOpenGLContext
    return QOpenGLContext._cuteAt(address)

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickWindowPrivate::data()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickWindowPrivate::data()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def data_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickWindowPrivate::data_append(QQmlListProperty<QObject>
    *a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.data_append' has no cute function yet. Qt's "
        "'void QQuickWindowPrivate::data_append(QQmlListProperty<QObject> "
        "*a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def data_at(*__, **_) -> Never:
    """
    Qt's 'QObject *QQuickWindowPrivate::data_at(QQmlListProperty<QObject>
    *a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.data_at' has no cute function yet. Qt's "
        "'QObject *QQuickWindowPrivate::data_at(QQmlListProperty<QObject> "
        "*a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def data_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickWindowPrivate::data_clear(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.data_clear' has no cute function yet. Qt's "
        "'void QQuickWindowPrivate::data_clear(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def data_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickWindowPrivate::data_count(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.data_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuickWindowPrivate::data_count(QQmlListProperty<QObject> *a0)': "
        "names 'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def data_removeLast(*__, **_) -> Never:
    """
    Qt's 'void QQuickWindowPrivate::data_removeLast(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.data_removeLast' has no cute function yet. "
        "Qt's 'void "
        "QQuickWindowPrivate::data_removeLast(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def emitAfterRenderPassRecording(*__, **_) -> Never:
    """
    Qt's 'void QQuickWindowPrivate::emitAfterRenderPassRecording(void *ud)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.emitAfterRenderPassRecording' has no cute "
        "function yet. Qt's 'void "
        "QQuickWindowPrivate::emitAfterRenderPassRecording(void *ud)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def emitBeforeRenderPassRecording(*__, **_) -> Never:
    """
    Qt's 'void QQuickWindowPrivate::emitBeforeRenderPassRecording(void *ud)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.emitBeforeRenderPassRecording' has no cute "
        "function yet. Qt's 'void "
        "QQuickWindowPrivate::emitBeforeRenderPassRecording(void *ud)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def findCursorItemAndHandler(*__, **_) -> Never:
    """
    Qt's 'std::pair<QQuickItem *, QQuickPointerHandler *>
    QQuickWindowPrivate::findCursorItemAndHandler(QQuickItem *item, const
    QPointF &localPos, const QPointF &scenePos) const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.findCursorItemAndHandler' has no cute "
        "function yet. Qt's 'std::pair<QQuickItem *, QQuickPointerHandler "
        "*> QQuickWindowPrivate::findCursorItemAndHandler(QQuickItem *item, "
        "const QPointF &localPos, const QPointF &scenePos) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def runAndClearJobs(*__, **_) -> Never:
    """
    Qt's 'void QQuickWindowPrivate::runAndClearJobs(QList<QRunnable *>
    *jobs)': names 'QList<QRunnable *>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.runAndClearJobs' has no cute function yet. "
        "Qt's 'void QQuickWindowPrivate::runAndClearJobs(QList<QRunnable *> "
        "*jobs)': names 'QList<QRunnable *>', which has no cute class yet.")

  @staticmethod
  def updateEffectiveOpacity(*__, **_) -> Never:
    """
    Qt's 'bool QQuickWindowPrivate::updateEffectiveOpacity(QQuickItem *a0)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.updateEffectiveOpacity' has no cute function "
        "yet. Qt's 'bool "
        "QQuickWindowPrivate::updateEffectiveOpacity(QQuickItem *a0)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def updateEffectiveOpacityRoot(*__, **_) -> Never:
    """
    Qt's 'void QQuickWindowPrivate::updateEffectiveOpacityRoot(QQuickItem
    *a0, qreal a1)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickWindowPrivate.updateEffectiveOpacityRoot' has no cute "
        "function yet. Qt's 'void "
        "QQuickWindowPrivate::updateEffectiveOpacityRoot(QQuickItem *a0, "
        "qreal a1)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
