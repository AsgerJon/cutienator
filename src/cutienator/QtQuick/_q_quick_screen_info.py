"""
QQuickScreenInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickscreen_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickScreenInfo to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QScreen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScreen = WAIT['QScreen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickScreenInfo(QObject):
  """
  The cute side of Qt's QQuickScreenInfo: a plain Python object standing in
  front of one C++ QQuickScreenInfo.

  It is built on the cute 'QObject', as Qt's QQuickScreenInfo is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScreenInfo that has a ritual and that Python
  can call so far, 33 names in all: 'metaObject', 'tr', 'name',
  'manufacturer', 'model', 'serialNumber', 'width', 'height',
  'desktopAvailableWidth', 'desktopAvailableHeight', 'logicalPixelDensity',
  'pixelDensity', 'devicePixelRatio', 'primaryOrientation', 'orientation',
  'virtualX', 'virtualY', 'setWrappedScreen', 'wrappedScreen', 'nameChanged',
  'manufacturerChanged', 'modelChanged', 'serialNumberChanged',
  'widthChanged', 'heightChanged', 'desktopGeometryChanged',
  'logicalPixelDensityChanged', 'pixelDensityChanged',
  'devicePixelRatioChanged', 'primaryOrientationChanged',
  'orientationChanged', 'virtualXChanged', 'virtualYChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickScreenInfo::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickScreenInfo::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickScreenInfo::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 39 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickScreenInfo is created at the first use, not by
    'QQuickScreenInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScreenInfo.
  - Qt tells when it has removed the C++ QQuickScreenInfo. Every call on the
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
    Calls Qt's 'QString QQuickScreenInfo::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#tr

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
    #  QString QQuickScreenInfo::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickScreenInfo2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScreenInfo'

  #  A C++ QQuickScreenInfo Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickScreenInfo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickScreenInfo::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickScreenInfo::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickScreenInfo10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickScreenInfo::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickScreenInfo::name() const
    return self.uglySide.call('ritual_ZNK16QQuickScreenInfo4nameEv')

  def manufacturer(self) -> str:
    """
    Calls Qt's 'QString QQuickScreenInfo::manufacturer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#manufacturer

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickScreenInfo::manufacturer() const
    return self.uglySide.call('ritual_ZNK16QQuickScreenInfo12manufacturerEv')

  def model(self) -> str:
    """
    Calls Qt's 'QString QQuickScreenInfo::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#model

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickScreenInfo::model() const
    return self.uglySide.call('ritual_ZNK16QQuickScreenInfo5modelEv')

  def serialNumber(self) -> str:
    """
    Calls Qt's 'QString QQuickScreenInfo::serialNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#serialNumber

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickScreenInfo::serialNumber() const
    return self.uglySide.call('ritual_ZNK16QQuickScreenInfo12serialNumberEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QQuickScreenInfo::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#width
    """
    #  int QQuickScreenInfo::width() const
    return self.uglySide.call('ritual_ZNK16QQuickScreenInfo5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QQuickScreenInfo::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#height
    """
    #  int QQuickScreenInfo::height() const
    return self.uglySide.call('ritual_ZNK16QQuickScreenInfo6heightEv')

  def desktopAvailableWidth(self) -> int:
    """
    Calls Qt's 'int QQuickScreenInfo::desktopAvailableWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#desktopAvailableWidth
    """
    #  int QQuickScreenInfo::desktopAvailableWidth() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickScreenInfo21desktopAvailableWidthEv',
    )

  def desktopAvailableHeight(self) -> int:
    """
    Calls Qt's 'int QQuickScreenInfo::desktopAvailableHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#desktopAvailableHeight
    """
    #  int QQuickScreenInfo::desktopAvailableHeight() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickScreenInfo22desktopAvailableHeightEv',
    )

  def logicalPixelDensity(self) -> float:
    """
    Calls Qt's 'qreal QQuickScreenInfo::logicalPixelDensity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#logicalPixelDensity
    """
    #  qreal QQuickScreenInfo::logicalPixelDensity() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickScreenInfo19logicalPixelDensityEv',
    )

  def pixelDensity(self) -> float:
    """
    Calls Qt's 'qreal QQuickScreenInfo::pixelDensity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#pixelDensity
    """
    #  qreal QQuickScreenInfo::pixelDensity() const
    return self.uglySide.call('ritual_ZNK16QQuickScreenInfo12pixelDensityEv')

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickScreenInfo::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#devicePixelRatio
    """
    #  qreal QQuickScreenInfo::devicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK16QQuickScreenInfo16devicePixelRatioEv',
    )

  def primaryOrientation(self) -> Qt.ScreenOrientation:
    """
    Calls Qt's 'Qt::ScreenOrientation QQuickScreenInfo::primaryOrientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#primaryOrientation

    Returns
    -------

    Qt.ScreenOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScreenOrientation(number)' gives.
    """
    #  Qt::ScreenOrientation QQuickScreenInfo::primaryOrientation() const
    return Qt.ScreenOrientation(self.uglySide.call(
        'ritual_ZNK16QQuickScreenInfo18primaryOrientationEv',
    ))

  def orientation(self) -> Qt.ScreenOrientation:
    """
    Calls Qt's 'Qt::ScreenOrientation QQuickScreenInfo::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#orientation

    Returns
    -------

    Qt.ScreenOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScreenOrientation(number)' gives.
    """
    #  Qt::ScreenOrientation QQuickScreenInfo::orientation() const
    return Qt.ScreenOrientation(self.uglySide.call(
        'ritual_ZNK16QQuickScreenInfo11orientationEv',
    ))

  def virtualX(self) -> int:
    """
    Calls Qt's 'int QQuickScreenInfo::virtualX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#virtualX
    """
    #  int QQuickScreenInfo::virtualX() const
    return self.uglySide.call('ritual_ZNK16QQuickScreenInfo8virtualXEv')

  def virtualY(self) -> int:
    """
    Calls Qt's 'int QQuickScreenInfo::virtualY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#virtualY
    """
    #  int QQuickScreenInfo::virtualY() const
    return self.uglySide.call('ritual_ZNK16QQuickScreenInfo8virtualYEv')

  def wrappedScreen(self) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QQuickScreenInfo::wrappedScreen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#wrappedScreen

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QQuickScreenInfo::wrappedScreen() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickScreenInfo13wrappedScreenEv',
    )
    from ..QtGui import QScreen
    return QScreen._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScreen)
  @overload(NoneType)
  def setWrappedScreen(self, screen: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::setWrappedScreen(QScreen *screen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#setWrappedScreen

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScreenInfo::setWrappedScreen(QScreen *screen)
    self.uglySide.call(
        'ritual_ZN16QQuickScreenInfo16setWrappedScreenEP7QScreen',
        self._addressOf(screen),
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
  @overload(QObject, QScreen)
  @overload(QObject, NoneType)
  @overload(NoneType, QScreen)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      parent: Optional[QObject] = None,
      wrappedScreen: Optional[QScreen] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickScreenInfo::QQuickScreenInfo(QObject *parent, QScreen
    *wrappedScreen)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#QQuickScreenInfo

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    wrappedScreen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickScreenInfo::QQuickScreenInfo(QObject *parent, QScreen
    #      *wrappedScreen)
    self._noteCreation(QQuickScreenInfo, lambda: Rituals.call(
        'ritual_ZN16QQuickScreenInfoC1EP7QObjectP7QScreen',
        self._addressOf(parent, 'QObject'), self._addressOf(wrappedScreen),
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

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::nameChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#nameChanged
    """
    #  void QQuickScreenInfo::nameChanged()
    self.uglySide.call('ritual_ZN16QQuickScreenInfo11nameChangedEv')

  def manufacturerChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::manufacturerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#manufacturerChanged
    """
    #  void QQuickScreenInfo::manufacturerChanged()
    self.uglySide.call('ritual_ZN16QQuickScreenInfo19manufacturerChangedEv')

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#modelChanged
    """
    #  void QQuickScreenInfo::modelChanged()
    self.uglySide.call('ritual_ZN16QQuickScreenInfo12modelChangedEv')

  def serialNumberChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::serialNumberChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#serialNumberChanged
    """
    #  void QQuickScreenInfo::serialNumberChanged()
    self.uglySide.call('ritual_ZN16QQuickScreenInfo19serialNumberChangedEv')

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::widthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscreeninfo.html#widthChanged
    """
    #  void QQuickScreenInfo::widthChanged()
    self.uglySide.call('ritual_ZN16QQuickScreenInfo12widthChangedEv')

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::heightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#heightChanged
    """
    #  void QQuickScreenInfo::heightChanged()
    self.uglySide.call('ritual_ZN16QQuickScreenInfo13heightChangedEv')

  def desktopGeometryChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::desktopGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#desktopGeometryChanged
    """
    #  void QQuickScreenInfo::desktopGeometryChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickScreenInfo22desktopGeometryChangedEv',
    )

  def logicalPixelDensityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::logicalPixelDensityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#logicalPixelDensityChanged
    """
    #  void QQuickScreenInfo::logicalPixelDensityChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickScreenInfo26logicalPixelDensityChangedEv',
    )

  def pixelDensityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::pixelDensityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#pixelDensityChanged
    """
    #  void QQuickScreenInfo::pixelDensityChanged()
    self.uglySide.call('ritual_ZN16QQuickScreenInfo19pixelDensityChangedEv')

  def devicePixelRatioChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::devicePixelRatioChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#devicePixelRatioChanged
    """
    #  void QQuickScreenInfo::devicePixelRatioChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickScreenInfo23devicePixelRatioChangedEv',
    )

  def primaryOrientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::primaryOrientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#primaryOrientationChanged
    """
    #  void QQuickScreenInfo::primaryOrientationChanged()
    self.uglySide.call(
        'ritual_ZN16QQuickScreenInfo25primaryOrientationChangedEv',
    )

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#orientationChanged
    """
    #  void QQuickScreenInfo::orientationChanged()
    self.uglySide.call('ritual_ZN16QQuickScreenInfo18orientationChangedEv')

  def virtualXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::virtualXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#virtualXChanged
    """
    #  void QQuickScreenInfo::virtualXChanged()
    self.uglySide.call('ritual_ZN16QQuickScreenInfo15virtualXChangedEv')

  def virtualYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScreenInfo::virtualYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscreeninfo.html#virtualYChanged
    """
    #  void QQuickScreenInfo::virtualYChanged()
    self.uglySide.call('ritual_ZN16QQuickScreenInfo15virtualYChangedEv')
