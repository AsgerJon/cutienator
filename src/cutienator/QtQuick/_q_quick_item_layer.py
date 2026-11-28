"""
QQuickItemLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickItemLayer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickShaderEffectSource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QRectF, QSize
  from ..QtQml import QQmlComponent
  from . import QQuickGeometryChange, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemLayer(QObject):
  """
  The cute side of Qt's QQuickItemLayer: a plain Python object standing in
  front of one C++ QQuickItemLayer.

  It is built on the cute 'QObject', as Qt's QQuickItemLayer is built on Qt's
  QObject, and has everything that class has. Qt's QQuickItemLayer is built
  on Qt's QSafeQuickItemChangeListener<QQuickItemLayer> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickItemLayer that has a ritual and that Python
  can call so far, 54 names in all: 'metaObject', 'tr', 'classBegin',
  'componentComplete', 'enabled', 'setEnabled', 'mipmap', 'setMipmap',
  'smooth', 'setSmooth', 'live', 'setLive', 'size', 'setSize', 'format',
  'setFormat', 'sourceRect', 'setSourceRect', 'wrapMode', 'setWrapMode',
  'name', 'setName', 'effect', 'setEffect', 'textureMirroring',
  'setTextureMirroring', 'samples', 'setSamples', 'effectSource',
  'itemGeometryChanged', 'itemOpacityChanged', 'itemParentChanged',
  'itemSiblingOrderChanged', 'itemVisibilityChanged', 'updateMatrix',
  'updateGeometry', 'updateOpacity', 'updateZ', 'enabledChanged',
  'sizeChanged', 'mipmapChanged', 'wrapModeChanged', 'nameChanged',
  'effectChanged', 'smoothChanged', 'liveChanged', 'formatChanged',
  'sourceRectChanged', 'textureMirroringChanged', 'samplesChanged',
  'activate', 'deactivate', 'activateEffect', 'deactivateEffect'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickItemLayer::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickItemLayer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickItemLayer::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQuickItemLayer::~QQuickItemLayer()': the destructor: Python never
    removes a C++ QQuickItemLayer.

  What has no ritual
  ------------------

  2 of the 61 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickItemLayer is created at the first use, not by
    'QQuickItemLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemLayer.
  - Qt tells when it has removed the C++ QQuickItemLayer. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickItemLayer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#tr

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
    #  QString QQuickItemLayer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickItemLayer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemLayer'

  #  A C++ QQuickItemLayer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemLayer'

  #  The functions Qt calls itself that QQuickItemLayer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN15QQuickItemLayer19itemGeometryChangedEP10QQuickItem20QQuick'
           'GeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemOpacityChanged': (
          ('_ZN15QQuickItemLayer18itemOpacityChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemParentChanged': (
          ('_ZN15QQuickItemLayer17itemParentChangedEP10QQuickItemS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemSiblingOrderChanged': (
          ('_ZN15QQuickItemLayer23itemSiblingOrderChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemVisibilityChanged': (
          ('_ZN15QQuickItemLayer21itemVisibilityChangedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
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
    Calls Qt's 'const QMetaObject *QQuickItemLayer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickItemLayer::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickItemLayer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemLayer::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#enabled
    """
    #  bool QQuickItemLayer::enabled() const
    return self.uglySide.call('ritual_ZNK15QQuickItemLayer7enabledEv')

  def mipmap(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemLayer::mipmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#mipmap
    """
    #  bool QQuickItemLayer::mipmap() const
    return self.uglySide.call('ritual_ZNK15QQuickItemLayer6mipmapEv')

  def smooth(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemLayer::smooth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#smooth
    """
    #  bool QQuickItemLayer::smooth() const
    return self.uglySide.call('ritual_ZNK15QQuickItemLayer6smoothEv')

  def live(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemLayer::live() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#live
    """
    #  bool QQuickItemLayer::live() const
    return self.uglySide.call('ritual_ZNK15QQuickItemLayer4liveEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickItemLayer::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickItemLayer::size() const
    address = self.uglySide.call('ritual_ZNK15QQuickItemLayer4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def format(self) -> QQuickShaderEffectSource.Format:
    """
    Calls Qt's 'QQuickShaderEffectSource::Format QQuickItemLayer::format()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#format

    Returns
    -------

    QQuickShaderEffectSource.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShaderEffectSource.Format(number)' gives.
    """
    #  QQuickShaderEffectSource::Format QQuickItemLayer::format() const
    return QQuickShaderEffectSource.Format(self.uglySide.call(
        'ritual_ZNK15QQuickItemLayer6formatEv',
    ))

  def sourceRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItemLayer::sourceRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#sourceRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickItemLayer::sourceRect() const
    address = self.uglySide.call('ritual_ZNK15QQuickItemLayer10sourceRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def wrapMode(self) -> QQuickShaderEffectSource.WrapMode:
    """
    Calls Qt's 'QQuickShaderEffectSource::WrapMode
    QQuickItemLayer::wrapMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#wrapMode

    Returns
    -------

    QQuickShaderEffectSource.WrapMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShaderEffectSource.WrapMode(number)' gives.
    """
    #  QQuickShaderEffectSource::WrapMode QQuickItemLayer::wrapMode() const
    return QQuickShaderEffectSource.WrapMode(self.uglySide.call(
        'ritual_ZNK15QQuickItemLayer8wrapModeEv',
    ))

  def name(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQuickItemLayer::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#name

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQuickItemLayer::name() const
    address = self.uglySide.call('ritual_ZNK15QQuickItemLayer4nameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def effect(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickItemLayer::effect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#effect

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickItemLayer::effect() const
    address = self.uglySide.call('ritual_ZNK15QQuickItemLayer6effectEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def textureMirroring(self) -> QQuickShaderEffectSource.TextureMirroring:
    """
    Calls Qt's 'QQuickShaderEffectSource::TextureMirroring
    QQuickItemLayer::textureMirroring() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#textureMirroring

    Returns
    -------

    QQuickShaderEffectSource.TextureMirroring
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShaderEffectSource.TextureMirroring(number)' gives.
    """
    #  QQuickShaderEffectSource::TextureMirroring
    #      QQuickItemLayer::textureMirroring() const
    return QQuickShaderEffectSource.TextureMirroring(self.uglySide.call(
        'ritual_ZNK15QQuickItemLayer16textureMirroringEv',
    ))

  def samples(self) -> int:
    """
    Calls Qt's 'int QQuickItemLayer::samples() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#samples
    """
    #  int QQuickItemLayer::samples() const
    return self.uglySide.call('ritual_ZNK15QQuickItemLayer7samplesEv')

  def effectSource(self) -> Optional[QQuickShaderEffectSource]:
    """
    Calls Qt's 'QQuickShaderEffectSource *QQuickItemLayer::effectSource()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#effectSource

    Returns
    -------

    Optional[QQuickShaderEffectSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShaderEffectSource *QQuickItemLayer::effectSource() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickItemLayer12effectSourceEv',
    )
    return QQuickShaderEffectSource._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickItemLayer::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN15QQuickItemLayer10setEnabledEb', enabled)

  @overload(bool)
  def setMipmap(self, mipmap: bool) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::setMipmap(bool mipmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setMipmap

    Parameters
    ----------

    mipmap : bool
      Passed on as it is.
    """
    #  void QQuickItemLayer::setMipmap(bool mipmap)
    self.uglySide.call('ritual_ZN15QQuickItemLayer9setMipmapEb', mipmap)

  @overload(bool)
  def setSmooth(self, s: bool) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::setSmooth(bool s)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setSmooth

    Parameters
    ----------

    s : bool
      Passed on as it is.
    """
    #  void QQuickItemLayer::setSmooth(bool s)
    self.uglySide.call('ritual_ZN15QQuickItemLayer9setSmoothEb', s)

  @overload(bool)
  def setLive(self, live: bool) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::setLive(bool live)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setLive

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QQuickItemLayer::setLive(bool live)
    self.uglySide.call('ritual_ZN15QQuickItemLayer7setLiveEb', live)

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickItemLayer::setSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer7setSizeERK5QSize', self._valueOf(size),
    )

  @overload(QQuickShaderEffectSource.Format)
  def setFormat(self, f: QQuickShaderEffectSource.Format) -> None:
    """
    Calls Qt's 'void
    QQuickItemLayer::setFormat(QQuickShaderEffectSource::Format f)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setFormat

    Parameters
    ----------

    f : QQuickShaderEffectSource.Format
      Passed on as its number.
    """
    #  void QQuickItemLayer::setFormat(QQuickShaderEffectSource::Format f)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer9setFormatEN24QQuickShaderEffectSource6F'
        'ormatE',
        f.value,
    )

  @overload(QRectF)
  def setSourceRect(self, sourceRect: QRectF) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::setSourceRect(const QRectF
    &sourceRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setSourceRect

    Parameters
    ----------

    sourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItemLayer::setSourceRect(const QRectF &sourceRect)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer13setSourceRectERK6QRectF',
        self._valueOf(sourceRect),
    )

  @overload(QQuickShaderEffectSource.WrapMode)
  def setWrapMode(self, mode: QQuickShaderEffectSource.WrapMode) -> None:
    """
    Calls Qt's 'void
    QQuickItemLayer::setWrapMode(QQuickShaderEffectSource::WrapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setWrapMode

    Parameters
    ----------

    mode : QQuickShaderEffectSource.WrapMode
      Passed on as its number.
    """
    #  void QQuickItemLayer::setWrapMode(QQuickShaderEffectSource::WrapMode
    #      mode)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer11setWrapModeEN24QQuickShaderEffectSourc'
        'e8WrapModeE',
        mode.value,
    )

  @overload(QByteArray)
  def setName(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::setName(const QByteArray &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setName

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuickItemLayer::setName(const QByteArray &name)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer7setNameERK10QByteArray',
        self._valueOf(name),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setEffect(self, effect: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::setEffect(QQmlComponent *effect)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setEffect

    Parameters
    ----------

    effect : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemLayer::setEffect(QQmlComponent *effect)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer9setEffectEP13QQmlComponent',
        self._addressOf(effect),
    )

  @overload(QQuickShaderEffectSource.TextureMirroring)
  def setTextureMirroring(
      self,
      mirroring: QQuickShaderEffectSource.TextureMirroring,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemLayer::setTextureMirroring(QQuickShaderEffectSource::
    TextureMirroring mirroring)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#setTextureMirroring

    Parameters
    ----------

    mirroring : QQuickShaderEffectSource.TextureMirroring
      Passed on as its number.
    """
    #  void QQuickItemLayer::setTextureMirroring(QQuickShaderEffectSource::
    #      TextureMirroring mirroring)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer19setTextureMirroringEN24QQuickShaderEff'
        'ectSource16TextureMirroringE',
        mirroring.value,
    )

  @overload(int)
  def setSamples(self, count: int) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::setSamples(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#setSamples

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuickItemLayer::setSamples(int count)
    self.uglySide.call('ritual_ZN15QQuickItemLayer10setSamplesEi', count)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, item: Optional[QQuickItem]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickItemLayer::QQuickItemLayer(QQuickItem *item)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#QQuickItemLayer

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickItemLayer::QQuickItemLayer(QQuickItem *item)
    self._noteCreation(QQuickItemLayer, lambda: Rituals.call(
        'ritual_ZN15QQuickItemLayerC1EP10QQuickItem', self._addressOf(item),
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#classBegin
    """
    #  void QQuickItemLayer::classBegin()
    self.uglySide.call('ritual_ZN15QQuickItemLayer10classBeginEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#componentComplete
    """
    #  void QQuickItemLayer::componentComplete()
    self.uglySide.call('ritual_ZN15QQuickItemLayer17componentCompleteEv')

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      a0: Optional[QQuickItem],
      a1: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::itemGeometryChanged(QQuickItem *a0,
    QQuickGeometryChange a1, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#itemGeometryChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItemLayer::itemGeometryChanged(QQuickItem *a0,
    #      QQuickGeometryChange a1, const QRectF &a2)
    ritual = (
        'ritual_ZN15QQuickItemLayer19itemGeometryChangedEP10QQuickItem20QQu'
        'ickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickItemLayer19itemGeometryChangedEP10QQuickIte'
          'm20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual, self._addressOf(a0), self._valueOf(a1), self._valueOf(a2),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemOpacityChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::itemOpacityChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#itemOpacityChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemLayer::itemOpacityChanged(QQuickItem *a0)
    ritual = 'ritual_ZN15QQuickItemLayer18itemOpacityChangedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickItemLayer18itemOpacityChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemParentChanged(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::itemParentChanged(QQuickItem *a0,
    QQuickItem *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#itemParentChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemLayer::itemParentChanged(QQuickItem *a0, QQuickItem
    #      *a1)
    ritual = 'ritual_ZN15QQuickItemLayer17itemParentChangedEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickItemLayer17itemParentChangedEP10QQuickItemS'
          '1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemSiblingOrderChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::itemSiblingOrderChanged(QQuickItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#itemSiblingOrderChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemLayer::itemSiblingOrderChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN15QQuickItemLayer23itemSiblingOrderChangedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickItemLayer23itemSiblingOrderChangedEP10QQuic'
          'kItem')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemVisibilityChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::itemVisibilityChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#itemVisibilityChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemLayer::itemVisibilityChanged(QQuickItem *a0)
    ritual = (
        'ritual_ZN15QQuickItemLayer21itemVisibilityChangedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickItemLayer21itemVisibilityChangedEP10QQuickI'
          'tem')
    self.uglySide.call(ritual, self._addressOf(a0))

  def updateMatrix(self) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::updateMatrix()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#updateMatrix
    """
    #  void QQuickItemLayer::updateMatrix()
    self.uglySide.call('ritual_ZN15QQuickItemLayer12updateMatrixEv')

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#updateGeometry
    """
    #  void QQuickItemLayer::updateGeometry()
    self.uglySide.call('ritual_ZN15QQuickItemLayer14updateGeometryEv')

  def updateOpacity(self) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::updateOpacity()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#updateOpacity
    """
    #  void QQuickItemLayer::updateOpacity()
    self.uglySide.call('ritual_ZN15QQuickItemLayer13updateOpacityEv')

  def updateZ(self) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::updateZ()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#updateZ
    """
    #  void QQuickItemLayer::updateZ()
    self.uglySide.call('ritual_ZN15QQuickItemLayer7updateZEv')

  @overload(bool)
  def enabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::enabledChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#enabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickItemLayer::enabledChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer14enabledChangedEb', enabled,
    )

  @overload(QSize)
  def sizeChanged(self, size: QSize) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::sizeChanged(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#sizeChanged

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickItemLayer::sizeChanged(const QSize &size)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer11sizeChangedERK5QSize',
        self._valueOf(size),
    )

  @overload(bool)
  def mipmapChanged(self, mipmap: bool) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::mipmapChanged(bool mipmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#mipmapChanged

    Parameters
    ----------

    mipmap : bool
      Passed on as it is.
    """
    #  void QQuickItemLayer::mipmapChanged(bool mipmap)
    self.uglySide.call('ritual_ZN15QQuickItemLayer13mipmapChangedEb', mipmap)

  @overload(QQuickShaderEffectSource.WrapMode)
  def wrapModeChanged(self, mode: QQuickShaderEffectSource.WrapMode) -> None:
    """
    Calls Qt's 'void
    QQuickItemLayer::wrapModeChanged(QQuickShaderEffectSource::WrapMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#wrapModeChanged

    Parameters
    ----------

    mode : QQuickShaderEffectSource.WrapMode
      Passed on as its number.
    """
    #  void QQuickItemLayer::wrapModeChanged(QQuickShaderEffectSource::
    #      WrapMode mode)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer15wrapModeChangedEN24QQuickShaderEffectS'
        'ource8WrapModeE',
        mode.value,
    )

  @overload(QByteArray)
  def nameChanged(self, name: QByteArray) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::nameChanged(const QByteArray &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#nameChanged

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuickItemLayer::nameChanged(const QByteArray &name)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer11nameChangedERK10QByteArray',
        self._valueOf(name),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def effectChanged(self, component: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::effectChanged(QQmlComponent
    *component)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#effectChanged

    Parameters
    ----------

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemLayer::effectChanged(QQmlComponent *component)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer13effectChangedEP13QQmlComponent',
        self._addressOf(component),
    )

  @overload(bool)
  def smoothChanged(self, smooth: bool) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::smoothChanged(bool smooth)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#smoothChanged

    Parameters
    ----------

    smooth : bool
      Passed on as it is.
    """
    #  void QQuickItemLayer::smoothChanged(bool smooth)
    self.uglySide.call('ritual_ZN15QQuickItemLayer13smoothChangedEb', smooth)

  @overload(bool)
  def liveChanged(self, live: bool) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::liveChanged(bool live)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#liveChanged

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QQuickItemLayer::liveChanged(bool live)
    self.uglySide.call('ritual_ZN15QQuickItemLayer11liveChangedEb', live)

  @overload(QQuickShaderEffectSource.Format)
  def formatChanged(self, format: QQuickShaderEffectSource.Format) -> None:
    """
    Calls Qt's 'void
    QQuickItemLayer::formatChanged(QQuickShaderEffectSource::Format format)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#formatChanged

    Parameters
    ----------

    format : QQuickShaderEffectSource.Format
      Passed on as its number.
    """
    #  void QQuickItemLayer::formatChanged(QQuickShaderEffectSource::Format
    #      format)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer13formatChangedEN24QQuickShaderEffectSou'
        'rce6FormatE',
        format.value,
    )

  @overload(QRectF)
  def sourceRectChanged(self, sourceRect: QRectF) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::sourceRectChanged(const QRectF
    &sourceRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#sourceRectChanged

    Parameters
    ----------

    sourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItemLayer::sourceRectChanged(const QRectF &sourceRect)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer17sourceRectChangedERK6QRectF',
        self._valueOf(sourceRect),
    )

  @overload(QQuickShaderEffectSource.TextureMirroring)
  def textureMirroringChanged(
      self,
      mirroring: QQuickShaderEffectSource.TextureMirroring,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemLayer::textureMirroringChanged(QQuickShaderEffectSource::
    TextureMirroring mirroring)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#textureMirroringChanged

    Parameters
    ----------

    mirroring : QQuickShaderEffectSource.TextureMirroring
      Passed on as its number.
    """
    #  void QQuickItemLayer::textureMirroringChanged(
    #      QQuickShaderEffectSource::TextureMirroring mirroring)
    self.uglySide.call(
        'ritual_ZN15QQuickItemLayer23textureMirroringChangedEN24QQuickShade'
        'rEffectSource16TextureMirroringE',
        mirroring.value,
    )

  @overload(int)
  def samplesChanged(self, count: int) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::samplesChanged(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#samplesChanged

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuickItemLayer::samplesChanged(int count)
    self.uglySide.call('ritual_ZN15QQuickItemLayer14samplesChangedEi', count)

  def activate(self) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::activate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#activate
    """
    #  void QQuickItemLayer::activate()
    self.uglySide.call('ritual_ZN15QQuickItemLayer8activateEv')

  def deactivate(self) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::deactivate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemlayer.html#deactivate
    """
    #  void QQuickItemLayer::deactivate()
    self.uglySide.call('ritual_ZN15QQuickItemLayer10deactivateEv')

  def activateEffect(self) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::activateEffect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#activateEffect
    """
    #  void QQuickItemLayer::activateEffect()
    self.uglySide.call('ritual_ZN15QQuickItemLayer14activateEffectEv')

  def deactivateEffect(self) -> None:
    """
    Calls Qt's 'void QQuickItemLayer::deactivateEffect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemlayer.html#deactivateEffect
    """
    #  void QQuickItemLayer::deactivateEffect()
    self.uglySide.call('ritual_ZN15QQuickItemLayer16deactivateEffectEv')
