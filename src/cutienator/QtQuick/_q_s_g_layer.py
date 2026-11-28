"""
QSGLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGLayer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QSGDynamicTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from ..QtGui import QImage
  from . import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGLayer(QSGDynamicTexture):
  """
  The cute side of Qt's QSGLayer: a plain Python object standing in front of
  one C++ QSGLayer.

  It is built on the cute 'QSGDynamicTexture', as Qt's QSGLayer is built on
  Qt's QSGDynamicTexture, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGLayer that has a ritual and that Python can call
  so far, 19 names in all: 'metaObject', 'tr', 'setItem', 'setRect',
  'setSize', 'scheduleUpdate', 'toImage', 'setLive', 'setRecursive',
  'setFormat', 'setHasMipmaps', 'setDevicePixelRatio', 'setMirrorHorizontal',
  'setMirrorVertical', 'setSamples', 'markDirtyTexture', 'invalidated',
  'updateRequested', 'scheduledUpdateCompleted'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSGLayer::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QSGLayer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSGLayer::~QSGLayer()': the destructor: Python never removes a C++
    QSGLayer.
  - Qt's 'QSGLayer::QSGLayer(QSGTexturePrivate &dd)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSGLayer is created at the first use, not by 'QSGLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGLayer.
  - Qt tells when it has removed the C++ QSGLayer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QSGLayer that has no cute function yet, '__init__',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QSGLayer, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Format(CuteNum):
    """The enum 'QSGLayer::Format' of Qt, with the 3 names Qt gives in it."""

    RGBA8 = Kee[int](1)
    RGBA16F = Kee[int](2)
    RGBA32F = Kee[int](3)

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
    Calls Qt's 'QString QSGLayer::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#tr

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
    #  QString QSGLayer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QSGLayer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGLayer'

  #  A C++ QSGLayer Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGLayer'

  #  The functions Qt calls itself that QSGLayer is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setItem': (
          ('_ZN8QSGLayer7setItemEP7QSGNode',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
           )),
      ),
      'setRect': (
          ('_ZN8QSGLayer7setRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'setSize': (
          ('_ZN8QSGLayer7setSizeERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'scheduleUpdate': (
          ('_ZN8QSGLayer14scheduleUpdateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'toImage': (
          ('_ZNK8QSGLayer7toImageEv',
           ('address', 'value', 'QtGui:QImage'),
           ()),
      ),
      'setLive': (
          ('_ZN8QSGLayer7setLiveEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setRecursive': (
          ('_ZN8QSGLayer12setRecursiveEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setFormat': (
          ('_ZN8QSGLayer9setFormatENS_6FormatE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGLayer.Format'),
           )),
      ),
      'setHasMipmaps': (
          ('_ZN8QSGLayer13setHasMipmapsEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setDevicePixelRatio': (
          ('_ZN8QSGLayer19setDevicePixelRatioEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'setMirrorHorizontal': (
          ('_ZN8QSGLayer19setMirrorHorizontalEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setMirrorVertical': (
          ('_ZN8QSGLayer17setMirrorVerticalEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setSamples': (
          ('_ZN8QSGLayer10setSamplesEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'markDirtyTexture': (
          ('_ZN8QSGLayer16markDirtyTextureEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'invalidated': (
          ('_ZN8QSGLayer11invalidatedEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject *QSGLayer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSGLayer::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QSGLayer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def toImage(self) -> QImage:
    """
    Calls Qt's 'QImage QSGLayer::toImage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#toImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSGLayer::toImage() const
    address = self.uglySide.call('ritual_ZNK8QSGLayer7toImageEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGNode)
  @overload(NoneType)
  def setItem(self, item: Optional[QSGNode]) -> None:
    """
    Calls Qt's 'void QSGLayer::setItem(QSGNode *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setItem

    Parameters
    ----------

    item : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGLayer::setItem(QSGNode *item)
    self.uglySide.call(
        'ritual_ZN8QSGLayer7setItemEP7QSGNode',
        self._addressOf(item, 'QSGNode'),
    )

  @overload(QRectF)
  def setRect(self, logicalRect: QRectF) -> None:
    """
    Calls Qt's 'void QSGLayer::setRect(const QRectF &logicalRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setRect

    Parameters
    ----------

    logicalRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGLayer::setRect(const QRectF &logicalRect)
    self.uglySide.call(
        'ritual_ZN8QSGLayer7setRectERK6QRectF', self._valueOf(logicalRect),
    )

  @overload(QSize)
  def setSize(self, pixelSize: QSize) -> None:
    """
    Calls Qt's 'void QSGLayer::setSize(const QSize &pixelSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setSize

    Parameters
    ----------

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSGLayer::setSize(const QSize &pixelSize)
    self.uglySide.call(
        'ritual_ZN8QSGLayer7setSizeERK5QSize', self._valueOf(pixelSize),
    )

  @overload(bool)
  def setLive(self, live: bool) -> None:
    """
    Calls Qt's 'void QSGLayer::setLive(bool live)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setLive

    Parameters
    ----------

    live : bool
      Passed on as it is.
    """
    #  void QSGLayer::setLive(bool live)
    self.uglySide.call('ritual_ZN8QSGLayer7setLiveEb', live)

  @overload(bool)
  def setRecursive(self, recursive: bool) -> None:
    """
    Calls Qt's 'void QSGLayer::setRecursive(bool recursive)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setRecursive

    Parameters
    ----------

    recursive : bool
      Passed on as it is.
    """
    #  void QSGLayer::setRecursive(bool recursive)
    self.uglySide.call('ritual_ZN8QSGLayer12setRecursiveEb', recursive)

  @overload(Format)
  def setFormat(self, format: Format) -> None:
    """
    Calls Qt's 'void QSGLayer::setFormat(Format format)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setFormat

    Parameters
    ----------

    format : Format
      Passed on as its number.
    """
    #  void QSGLayer::setFormat(Format format)
    self.uglySide.call(
        'ritual_ZN8QSGLayer9setFormatENS_6FormatE', format.value,
    )

  @overload(bool)
  def setHasMipmaps(self, mipmap: bool) -> None:
    """
    Calls Qt's 'void QSGLayer::setHasMipmaps(bool mipmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setHasMipmaps

    Parameters
    ----------

    mipmap : bool
      Passed on as it is.
    """
    #  void QSGLayer::setHasMipmaps(bool mipmap)
    self.uglySide.call('ritual_ZN8QSGLayer13setHasMipmapsEb', mipmap)

  @overload(float)
  def setDevicePixelRatio(self, ratio: float) -> None:
    """
    Calls Qt's 'void QSGLayer::setDevicePixelRatio(qreal ratio)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setDevicePixelRatio

    Parameters
    ----------

    ratio : float
      Passed on as it is.
    """
    #  void QSGLayer::setDevicePixelRatio(qreal ratio)
    self.uglySide.call('ritual_ZN8QSGLayer19setDevicePixelRatioEd', ratio)

  @overload(bool)
  def setMirrorHorizontal(self, mirror: bool) -> None:
    """
    Calls Qt's 'void QSGLayer::setMirrorHorizontal(bool mirror)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setMirrorHorizontal

    Parameters
    ----------

    mirror : bool
      Passed on as it is.
    """
    #  void QSGLayer::setMirrorHorizontal(bool mirror)
    self.uglySide.call('ritual_ZN8QSGLayer19setMirrorHorizontalEb', mirror)

  @overload(bool)
  def setMirrorVertical(self, mirror: bool) -> None:
    """
    Calls Qt's 'void QSGLayer::setMirrorVertical(bool mirror)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setMirrorVertical

    Parameters
    ----------

    mirror : bool
      Passed on as it is.
    """
    #  void QSGLayer::setMirrorVertical(bool mirror)
    self.uglySide.call('ritual_ZN8QSGLayer17setMirrorVerticalEb', mirror)

  @overload(int)
  def setSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void QSGLayer::setSamples(int samples)'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#setSamples

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QSGLayer::setSamples(int samples)
    self.uglySide.call('ritual_ZN8QSGLayer10setSamplesEi', samples)

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
    Qt's 'QSGLayer::QSGLayer(QSGTexturePrivate &dd)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGLayer.__init__' has no cute function yet. Qt's "
        "'QSGLayer::QSGLayer(QSGTexturePrivate &dd)': takes a type Python "
        "has no way to hand over yet.")

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

  def scheduleUpdate(self) -> None:
    """
    Calls Qt's 'void QSGLayer::scheduleUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#scheduleUpdate
    """
    #  void QSGLayer::scheduleUpdate()
    self.uglySide.call('ritual_ZN8QSGLayer14scheduleUpdateEv')

  def markDirtyTexture(self) -> None:
    """
    Calls Qt's 'void QSGLayer::markDirtyTexture()'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#markDirtyTexture
    """
    #  void QSGLayer::markDirtyTexture()
    self.uglySide.call('ritual_ZN8QSGLayer16markDirtyTextureEv')

  def invalidated(self) -> None:
    """
    Calls Qt's 'void QSGLayer::invalidated()'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#invalidated
    """
    #  void QSGLayer::invalidated()
    self.uglySide.call('ritual_ZN8QSGLayer11invalidatedEv')

  def updateRequested(self) -> None:
    """
    Calls Qt's 'void QSGLayer::updateRequested()'.

    Qt's own words: https://doc.qt.io/qt-6/qsglayer.html#updateRequested
    """
    #  void QSGLayer::updateRequested()
    self.uglySide.call('ritual_ZN8QSGLayer15updateRequestedEv')

  def scheduledUpdateCompleted(self) -> None:
    """
    Calls Qt's 'void QSGLayer::scheduledUpdateCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsglayer.html#scheduledUpdateCompleted
    """
    #  void QSGLayer::scheduledUpdateCompleted()
    self.uglySide.call('ritual_ZN8QSGLayer24scheduledUpdateCompletedEv')
