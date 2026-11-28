"""
QQuickWidgetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickWidgets/6.12.0/QtQuickWidgets/private/qquickwidget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickWidgetPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QPlatformTextureList
from ..QtWidgets import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QRectF, QSize
  from ..QtGui import QImage, QPlatformBackingStoreRhiConfig, QSurfaceFormat
  from ..QtQuick import QQuickGeometryChange, QQuickItem
  from . import QQuickWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickWidget = WAIT['QQuickWidget']
  QRectF = WAIT['QRectF']
  QSurfaceFormat = WAIT['QSurfaceFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWidgetPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QQuickWidgetPrivate: a plain Python object standing
  in front of one C++ QQuickWidgetPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QQuickWidgetPrivate is
  built on Qt's QWidgetPrivate, and has everything that class has. Qt's
  QQuickWidgetPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickWidgetPrivate> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickWidgetPrivate that has a ritual and that
  Python can call so far, 19 names in all: 'q_func', 'get', 'executeHelper',
  'destroy', 'execute', 'itemGeometryChanged', 'initResize', 'updateSize',
  'updatePosition', 'setRootObject', 'handleContextCreationFailure',
  'rhiConfig', 'texture', 'textureListFlags', 'grabFramebuffer',
  'ensureEngine', 'handleWindowAboutToChange', 'invalidateRenderControl',
  'rootObjectSize'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickWidget *QQuickWidgetPrivate::q_func() const': takes in
    Python what 'QQuickWidget *QQuickWidgetPrivate::q_func()' takes.
  - Qt's 'const QQuickWidgetPrivate *QQuickWidgetPrivate::get(const
    QQuickWidget *view)': takes in Python what 'QQuickWidgetPrivate
    *QQuickWidgetPrivate::get(QQuickWidget *view)' takes.

  What has no ritual
  ------------------

  9 of the 31 functions Qt declares: 5 leans on 'QQuickWidgetRenderControl; 2
  leans on 'qAccessibleQuickWidgetFactory(QString const&, QObject*)', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken; 1 cannot be called and cannot be called through the
  meta-object and cannot be copied; 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickWidgetPrivate is created at the first use, not by
    'QQuickWidgetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWidgetPrivate.
  - Each name of Qt's QQuickWidgetPrivate that has no cute function yet,
    '__init__', 'ensureBackingScene', 'handleWindowChange',
    'initOffscreenWindow', 'initializeWithRhi', 'renderSceneGraph',
    'updateFrambufferObjectSize', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickWidget)
  @overload(NoneType)
  def get(view: Optional[QQuickWidget]) -> Optional[QQuickWidgetPrivate]:
    """
    Calls Qt's 'QQuickWidgetPrivate *QQuickWidgetPrivate::get(QQuickWidget
    *view)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidgetprivate.html#get

    Parameters
    ----------

    view : Optional[QQuickWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickWidgetPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWidgetPrivate *QQuickWidgetPrivate::get(QQuickWidget *view)
    address = Rituals.call(
        'ritual_ZN19QQuickWidgetPrivate3getEP12QQuickWidget',
        CuteMixin._addressOf(view),
    )
    return QQuickWidgetPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWidgetPrivate'

  #  A C++ QQuickWidgetPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWidgetPrivate'

  #  The functions Qt calls itself that QQuickWidgetPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN19QQuickWidgetPrivate19itemGeometryChangedEP10QQuickItem20QQ'
           'uickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
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

  def rhiConfig(self) -> QPlatformBackingStoreRhiConfig:
    """
    Calls Qt's 'QPlatformBackingStoreRhiConfig
    QQuickWidgetPrivate::rhiConfig() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidgetprivate.html#rhiConfig

    Returns
    -------

    QPlatformBackingStoreRhiConfig
      A new cute QPlatformBackingStoreRhiConfig around the copy Qt gave back.
      Python owns it.
    """
    #  QPlatformBackingStoreRhiConfig QQuickWidgetPrivate::rhiConfig() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWidgetPrivate9rhiConfigEv',
    )
    from ..QtGui import QPlatformBackingStoreRhiConfig
    return QPlatformBackingStoreRhiConfig._cuteOwning(address)

  def texture(self) -> QWidgetPrivate.TextureData:
    """
    Calls Qt's 'TextureData QQuickWidgetPrivate::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidgetprivate.html#texture

    Returns
    -------

    QWidgetPrivate.TextureData
      A new cute QWidgetPrivate::TextureData around the copy Qt gave back.
      Python owns it.
    """
    #  TextureData QQuickWidgetPrivate::texture() const
    ritual = 'ritual_ZNK19QQuickWidgetPrivate7textureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickWidgetPrivate7textureEv'
    address = self.uglySide.call(ritual)
    return QWidgetPrivate.TextureData._cuteOwning(address)

  def rootObjectSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickWidgetPrivate::rootObjectSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#rootObjectSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickWidgetPrivate::rootObjectSize() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWidgetPrivate14rootObjectSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setRootObject(self, a0: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QQuickWidgetPrivate::setRootObject(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#setRootObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickWidgetPrivate::setRootObject(QObject *a0)
    return self.uglySide.call(
        'ritual_ZN19QQuickWidgetPrivate13setRootObjectEP7QObject',
        self._addressOf(a0, 'QObject'),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickWidgetPrivate::QQuickWidgetPrivate()': leans on
    'QQuickWidgetRenderControl::QQuickWidgetRenderControl(QQuickWidget*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickWidgetPrivate.__init__' has no cute function yet. Qt's "
        "'QQuickWidgetPrivate::QQuickWidgetPrivate()': leans on "
        "'QQuickWidgetRenderControl::QQuickWidgetRenderControl(QQuickWidget*"
        ")', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

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

  def q_func(self) -> Optional[QQuickWidget]:
    """
    Calls Qt's 'QQuickWidget *QQuickWidgetPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidgetprivate.html#q_func

    Returns
    -------

    Optional[QQuickWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWidget *QQuickWidgetPrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QQuickWidgetPrivate6q_funcEv')
    from . import QQuickWidget
    return QQuickWidget._cuteAt(address)

  def executeHelper(self) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::executeHelper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#executeHelper
    """
    #  void QQuickWidgetPrivate::executeHelper()
    self.uglySide.call('ritual_ZN19QQuickWidgetPrivate13executeHelperEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidgetprivate.html#destroy
    """
    #  void QQuickWidgetPrivate::destroy()
    self.uglySide.call('ritual_ZN19QQuickWidgetPrivate7destroyEv')

  @overload()
  def execute(self) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::execute()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidgetprivate.html#execute
    """
    #  void QQuickWidgetPrivate::execute()
    self.uglySide.call('ritual_ZN19QQuickWidgetPrivate7executeEv')

  @overload(str, str)
  def execute(self, uri: str, typeName: str) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::execute(QAnyStringView uri,
    QAnyStringView typeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwidgetprivate.html#execute

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickWidgetPrivate::execute(QAnyStringView uri, QAnyStringView
    #      typeName)
    self.uglySide.call(
        'ritual_ZN19QQuickWidgetPrivate7executeE14QAnyStringViewS0_',
        uri, typeName,
    )

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      oldGeometry: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickWidgetPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &oldGeometry)
    ritual = (
        'ritual_ZN19QQuickWidgetPrivate19itemGeometryChangedEP10QQuickItem2'
        '0QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickWidgetPrivate19itemGeometryChangedEP10QQuic'
          'kItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change),
        self._valueOf(oldGeometry),
    )

  def initResize(self) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::initResize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#initResize
    """
    #  void QQuickWidgetPrivate::initResize()
    self.uglySide.call('ritual_ZN19QQuickWidgetPrivate10initResizeEv')

  def updateSize(self) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::updateSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#updateSize
    """
    #  void QQuickWidgetPrivate::updateSize()
    self.uglySide.call('ritual_ZN19QQuickWidgetPrivate10updateSizeEv')

  def updatePosition(self) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::updatePosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#updatePosition
    """
    #  void QQuickWidgetPrivate::updatePosition()
    self.uglySide.call('ritual_ZN19QQuickWidgetPrivate14updatePositionEv')

  @overload(QSurfaceFormat)
  def handleContextCreationFailure(self, format: QSurfaceFormat) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::handleContextCreationFailure(const
    QSurfaceFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html

    Parameters
    ----------

    format : QSurfaceFormat
      Passed on as a value: Qt reads the C++ QSurfaceFormat, which stays
      Python's own.
    """
    #  void QQuickWidgetPrivate::handleContextCreationFailure(const
    #      QSurfaceFormat &format)
    self.uglySide.call(
        'ritual_ZN19QQuickWidgetPrivate28handleContextCreationFailureERK14Q'
        'SurfaceFormat',
        self._valueOf(format),
    )

  def textureListFlags(self) -> QPlatformTextureList.Flags:
    """
    Calls Qt's 'QPlatformTextureList::Flags
    QQuickWidgetPrivate::textureListFlags()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#textureListFlags

    Returns
    -------

    QPlatformTextureList.Flags
      The value standing for the combination Qt gave back.
    """
    #  QPlatformTextureList::Flags QQuickWidgetPrivate::textureListFlags()
    ritual = 'ritual_ZN19QQuickWidgetPrivate16textureListFlagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickWidgetPrivate16textureListFlagsEv'
    return QPlatformTextureList.Flags(self.uglySide.call(ritual))

  def grabFramebuffer(self) -> QImage:
    """
    Calls Qt's 'QImage QQuickWidgetPrivate::grabFramebuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#grabFramebuffer

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickWidgetPrivate::grabFramebuffer()
    address = self.uglySide.call(
        'ritual_ZN19QQuickWidgetPrivate15grabFramebufferEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def ensureEngine(self) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::ensureEngine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#ensureEngine
    """
    #  void QQuickWidgetPrivate::ensureEngine() const
    self.uglySide.call('ritual_ZNK19QQuickWidgetPrivate12ensureEngineEv')

  def handleWindowAboutToChange(self) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::handleWindowAboutToChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#handleWindowAboutToChange
    """
    #  void QQuickWidgetPrivate::handleWindowAboutToChange()
    self.uglySide.call(
        'ritual_ZN19QQuickWidgetPrivate25handleWindowAboutToChangeEv',
    )

  def invalidateRenderControl(self) -> None:
    """
    Calls Qt's 'void QQuickWidgetPrivate::invalidateRenderControl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwidgetprivate.html#invalidateRenderControl
    """
    #  void QQuickWidgetPrivate::invalidateRenderControl()
    self.uglySide.call(
        'ritual_ZN19QQuickWidgetPrivate23invalidateRenderControlEv',
    )

  @staticmethod
  def ensureBackingScene(*__, **_) -> Never:
    """
    Qt's 'void QQuickWidgetPrivate::ensureBackingScene()': leans on
    'QQuickWidgetRenderControl::QQuickWidgetRenderControl(QQuickWidget*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickWidgetPrivate.ensureBackingScene' has no cute function yet. "
        "Qt's 'void QQuickWidgetPrivate::ensureBackingScene()': leans on "
        "'QQuickWidgetRenderControl::QQuickWidgetRenderControl(QQuickWidget*"
        ")', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

  @staticmethod
  def handleWindowChange(*__, **_) -> Never:
    """
    Qt's 'void QQuickWidgetPrivate::handleWindowChange()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: unknown type name 'QQuickWidgetRenderControl'; did you mean
    'QQuickRenderControl'?.
    """
    raise NotImplementedError(
        "'QQuickWidgetPrivate.handleWindowChange' has no cute function yet. "
        "Qt's 'void QQuickWidgetPrivate::handleWindowChange()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name "
        "'QQuickWidgetRenderControl'; did you mean 'QQuickRenderControl'?.")

  @staticmethod
  def initOffscreenWindow(*__, **_) -> Never:
    """
    Qt's 'void QQuickWidgetPrivate::initOffscreenWindow()': leans on
    'qAccessibleQuickWidgetFactory(QString const&, QObject*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickWidgetPrivate.initOffscreenWindow' has no cute function "
        "yet. Qt's 'void QQuickWidgetPrivate::initOffscreenWindow()': leans "
        "on 'qAccessibleQuickWidgetFactory(QString const&, QObject*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def initializeWithRhi(*__, **_) -> Never:
    """
    Qt's 'void QQuickWidgetPrivate::initializeWithRhi()': leans on
    'QQuickWidgetRenderControl::QQuickWidgetRenderControl(QQuickWidget*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickWidgetPrivate.initializeWithRhi' has no cute function yet. "
        "Qt's 'void QQuickWidgetPrivate::initializeWithRhi()': leans on "
        "'QQuickWidgetRenderControl::QQuickWidgetRenderControl(QQuickWidget*"
        ")', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

  @staticmethod
  def renderSceneGraph(*__, **_) -> Never:
    """
    Qt's 'void QQuickWidgetPrivate::renderSceneGraph()': leans on
    'QQuickWidgetRenderControl::QQuickWidgetRenderControl(QQuickWidget*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickWidgetPrivate.renderSceneGraph' has no cute function yet. "
        "Qt's 'void QQuickWidgetPrivate::renderSceneGraph()': leans on "
        "'QQuickWidgetRenderControl::QQuickWidgetRenderControl(QQuickWidget*"
        ")', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

  @staticmethod
  def updateFrambufferObjectSize(*__, **_) -> Never:
    """
    Qt's 'void QQuickWidgetPrivate::updateFrambufferObjectSize()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickWidgetPrivate.updateFrambufferObjectSize' has no cute "
        "function yet. Qt's 'void "
        "QQuickWidgetPrivate::updateFrambufferObjectSize()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
