"""
QHeightMapSurfaceDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qheightmapsurfacedataproxy.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QSurfaceDataProxy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage
  from . import QHeightMapSurfaceDataProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHeightMapSurfaceDataProxy(QSurfaceDataProxy):
  """
  The cute side of Qt's QHeightMapSurfaceDataProxy: a plain Python object
  standing in front of one C++ QHeightMapSurfaceDataProxy.

  It is built on the cute 'QSurfaceDataProxy', as Qt's
  QHeightMapSurfaceDataProxy is built on Qt's QSurfaceDataProxy, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QHeightMapSurfaceDataProxy that has a ritual and
  that Python can call so far, 32 names in all: 'metaObject', 'tr', 'd_func',
  'setHeightMap', 'heightMap', 'setHeightMapFile', 'heightMapFile',
  'setValueRanges', 'setMinXValue', 'minXValue', 'setMaxXValue', 'maxXValue',
  'setMinZValue', 'minZValue', 'setMaxZValue', 'maxZValue', 'setMinYValue',
  'minYValue', 'setMaxYValue', 'maxYValue', 'setAutoScaleY', 'autoScaleY',
  'heightMapChanged', 'heightMapFileChanged', 'minXValueChanged',
  'maxXValueChanged', 'minZValueChanged', 'maxZValueChanged',
  'minYValueChanged', 'maxYValueChanged', 'autoScaleYChanged',
  'handlePendingResolve'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHeightMapSurfaceDataProxy::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QHeightMapSurfaceDataProxy::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QHeightMapSurfaceDataProxyPrivate
    *QHeightMapSurfaceDataProxy::d_func() const': takes in Python what
    'QHeightMapSurfaceDataProxyPrivate *QHeightMapSurfaceDataProxy::d_func()'
    takes.
  - Qt's 'QHeightMapSurfaceDataProxy::~QHeightMapSurfaceDataProxy()': the
    destructor: Python never removes a C++ QHeightMapSurfaceDataProxy.
  - Qt's 'QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(
    QHeightMapSurfaceDataProxyPrivate &d, QObject *parent)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 44 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QHeightMapSurfaceDataProxy is created at the first use, not by
    'QHeightMapSurfaceDataProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHeightMapSurfaceDataProxy.
  - Qt tells when it has removed the C++ QHeightMapSurfaceDataProxy. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QHeightMapSurfaceDataProxy::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#tr

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
    #  QString QHeightMapSurfaceDataProxy::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHeightMapSurfaceDataProxy'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QHeightMapSurfaceDataProxy Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHeightMapSurfaceDataProxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHeightMapSurfaceDataProxy::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHeightMapSurfaceDataProxy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QHeightMapSurfaceDataProxy10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def heightMap(self) -> QImage:
    """
    Calls Qt's 'QImage QHeightMapSurfaceDataProxy::heightMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#heightMap

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QHeightMapSurfaceDataProxy::heightMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QHeightMapSurfaceDataProxy9heightMapEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def heightMapFile(self) -> str:
    """
    Calls Qt's 'QString QHeightMapSurfaceDataProxy::heightMapFile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#heightMapFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHeightMapSurfaceDataProxy::heightMapFile() const
    return self.uglySide.call(
        'ritual_ZNK26QHeightMapSurfaceDataProxy13heightMapFileEv',
    )

  def minXValue(self) -> float:
    """
    Calls Qt's 'float QHeightMapSurfaceDataProxy::minXValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#minXValue
    """
    #  float QHeightMapSurfaceDataProxy::minXValue() const
    return self.uglySide.call(
        'ritual_ZNK26QHeightMapSurfaceDataProxy9minXValueEv',
    )

  def maxXValue(self) -> float:
    """
    Calls Qt's 'float QHeightMapSurfaceDataProxy::maxXValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#maxXValue
    """
    #  float QHeightMapSurfaceDataProxy::maxXValue() const
    return self.uglySide.call(
        'ritual_ZNK26QHeightMapSurfaceDataProxy9maxXValueEv',
    )

  def minZValue(self) -> float:
    """
    Calls Qt's 'float QHeightMapSurfaceDataProxy::minZValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#minZValue
    """
    #  float QHeightMapSurfaceDataProxy::minZValue() const
    return self.uglySide.call(
        'ritual_ZNK26QHeightMapSurfaceDataProxy9minZValueEv',
    )

  def maxZValue(self) -> float:
    """
    Calls Qt's 'float QHeightMapSurfaceDataProxy::maxZValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#maxZValue
    """
    #  float QHeightMapSurfaceDataProxy::maxZValue() const
    return self.uglySide.call(
        'ritual_ZNK26QHeightMapSurfaceDataProxy9maxZValueEv',
    )

  def minYValue(self) -> float:
    """
    Calls Qt's 'float QHeightMapSurfaceDataProxy::minYValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#minYValue
    """
    #  float QHeightMapSurfaceDataProxy::minYValue() const
    return self.uglySide.call(
        'ritual_ZNK26QHeightMapSurfaceDataProxy9minYValueEv',
    )

  def maxYValue(self) -> float:
    """
    Calls Qt's 'float QHeightMapSurfaceDataProxy::maxYValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#maxYValue
    """
    #  float QHeightMapSurfaceDataProxy::maxYValue() const
    return self.uglySide.call(
        'ritual_ZNK26QHeightMapSurfaceDataProxy9maxYValueEv',
    )

  def autoScaleY(self) -> bool:
    """
    Calls Qt's 'bool QHeightMapSurfaceDataProxy::autoScaleY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#autoScaleY
    """
    #  bool QHeightMapSurfaceDataProxy::autoScaleY() const
    return self.uglySide.call(
        'ritual_ZNK26QHeightMapSurfaceDataProxy10autoScaleYEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QImage)
  def setHeightMap(self, image: QImage) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::setHeightMap(const QImage
    &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#setHeightMap

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QHeightMapSurfaceDataProxy::setHeightMap(const QImage &image)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy12setHeightMapERK6QImage',
        self._valueOf(image),
    )

  @overload(str)
  def setHeightMapFile(self, filename: str) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::setHeightMapFile(const
    QString &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#setHeightMapFile

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHeightMapSurfaceDataProxy::setHeightMapFile(const QString
    #      &filename)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy16setHeightMapFileERK7QString',
        filename,
    )

  @overload(float, float, float, float)
  def setValueRanges(
      self,
      minX: float,
      maxX: float,
      minZ: float,
      maxZ: float,
  ) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::setValueRanges(float minX,
    float maxX, float minZ, float maxZ)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#setValueRanges

    Parameters
    ----------

    minX : float
      Passed on as it is.

    maxX : float
      Passed on as it is.

    minZ : float
      Passed on as it is.

    maxZ : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::setValueRanges(float minX, float
    #      maxX, float minZ, float maxZ)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy14setValueRangesEffff',
        minX, maxX, minZ, maxZ,
    )

  @overload(float)
  def setMinXValue(self, min: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::setMinXValue(float min)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#setMinXValue

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::setMinXValue(float min)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy12setMinXValueEf', min,
    )

  @overload(float)
  def setMaxXValue(self, max: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::setMaxXValue(float max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#setMaxXValue

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::setMaxXValue(float max)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy12setMaxXValueEf', max,
    )

  @overload(float)
  def setMinZValue(self, min: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::setMinZValue(float min)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#setMinZValue

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::setMinZValue(float min)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy12setMinZValueEf', min,
    )

  @overload(float)
  def setMaxZValue(self, max: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::setMaxZValue(float max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#setMaxZValue

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::setMaxZValue(float max)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy12setMaxZValueEf', max,
    )

  @overload(float)
  def setMinYValue(self, min: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::setMinYValue(float min)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#setMinYValue

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::setMinYValue(float min)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy12setMinYValueEf', min,
    )

  @overload(float)
  def setMaxYValue(self, max: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::setMaxYValue(float max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#setMaxYValue

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::setMaxYValue(float max)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy12setMaxYValueEf', max,
    )

  @overload(bool)
  def setAutoScaleY(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::setAutoScaleY(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#setAutoScaleY

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::setAutoScaleY(bool enabled)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy13setAutoScaleYEb', enabled,
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
    'QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(QObject
    #      *parent)
    self._noteCreation(QHeightMapSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN26QHeightMapSurfaceDataProxyC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QImage)
  @overload(QImage, QObject)
  @overload(QImage, NoneType)
  def __init__(
      self,
      image: QImage,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(const QImage
    &image, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(const QImage
    #      &image, QObject *parent)
    self._noteCreation(QHeightMapSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN26QHeightMapSurfaceDataProxyC1ERK6QImageP7QObject',
        self._valueOf(image), self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(
      self,
      filename: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(const QString
    &filename, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHeightMapSurfaceDataProxy::QHeightMapSurfaceDataProxy(const QString
    #      &filename, QObject *parent)
    self._noteCreation(QHeightMapSurfaceDataProxy, lambda: Rituals.call(
        'ritual_ZN26QHeightMapSurfaceDataProxyC1ERK7QStringP7QObject',
        filename, self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QHeightMapSurfaceDataProxyPrivate]:
    """
    Calls Qt's 'QHeightMapSurfaceDataProxyPrivate
    *QHeightMapSurfaceDataProxy::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#d_func

    Returns
    -------

    Optional[QHeightMapSurfaceDataProxyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHeightMapSurfaceDataProxyPrivate
    #      *QHeightMapSurfaceDataProxy::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy6d_funcEv',
    )
    from . import QHeightMapSurfaceDataProxyPrivate
    return QHeightMapSurfaceDataProxyPrivate._cuteAt(address)

  @overload(QImage)
  def heightMapChanged(self, image: QImage) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::heightMapChanged(const
    QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#heightMapChanged

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QHeightMapSurfaceDataProxy::heightMapChanged(const QImage &image)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy16heightMapChangedERK6QImage',
        self._valueOf(image),
    )

  @overload(str)
  def heightMapFileChanged(self, filename: str) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::heightMapFileChanged(const
    QString &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QHeightMapSurfaceDataProxy::heightMapFileChanged(const QString
    #      &filename)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy20heightMapFileChangedERK7QSt'
        'ring',
        filename,
    )

  @overload(float)
  def minXValueChanged(self, value: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::minXValueChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#minXValueChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::minXValueChanged(float value)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy16minXValueChangedEf', value,
    )

  @overload(float)
  def maxXValueChanged(self, value: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::maxXValueChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#maxXValueChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::maxXValueChanged(float value)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy16maxXValueChangedEf', value,
    )

  @overload(float)
  def minZValueChanged(self, value: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::minZValueChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#minZValueChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::minZValueChanged(float value)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy16minZValueChangedEf', value,
    )

  @overload(float)
  def maxZValueChanged(self, value: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::maxZValueChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#maxZValueChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::maxZValueChanged(float value)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy16maxZValueChangedEf', value,
    )

  @overload(float)
  def minYValueChanged(self, value: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::minYValueChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#minYValueChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::minYValueChanged(float value)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy16minYValueChangedEf', value,
    )

  @overload(float)
  def maxYValueChanged(self, value: float) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::maxYValueChanged(float
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#maxYValueChanged

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::maxYValueChanged(float value)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy16maxYValueChangedEf', value,
    )

  @overload(bool)
  def autoScaleYChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::autoScaleYChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html#autoScaleYChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QHeightMapSurfaceDataProxy::autoScaleYChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy17autoScaleYChangedEb',
        enabled,
    )

  def handlePendingResolve(self) -> None:
    """
    Calls Qt's 'void QHeightMapSurfaceDataProxy::handlePendingResolve()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qheightmapsurfacedataproxy.html
    """
    #  void QHeightMapSurfaceDataProxy::handlePendingResolve()
    self.uglySide.call(
        'ritual_ZN26QHeightMapSurfaceDataProxy20handlePendingResolveEv',
    )
