"""
QScreen binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qscreen.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize, QSizeF
  from . import QPixmap, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScreen(QObject):
  """
  The cute side of Qt's QScreen: a plain Python object standing in front of
  one C++ QScreen.

  It is built on the cute 'QObject', as Qt's QScreen is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScreen that has a ritual and that Python can call
  so far, 35 names in all: 'metaObject', 'tr', 'name', 'manufacturer',
  'model', 'serialNumber', 'depth', 'size', 'geometry', 'physicalSize',
  'physicalDotsPerInchX', 'physicalDotsPerInchY', 'physicalDotsPerInch',
  'logicalDotsPerInchX', 'logicalDotsPerInchY', 'logicalDotsPerInch',
  'devicePixelRatio', 'availableSize', 'availableGeometry',
  'virtualSiblings', 'virtualSiblingAt', 'virtualSize', 'virtualGeometry',
  'availableVirtualSize', 'availableVirtualGeometry', 'primaryOrientation',
  'orientation', 'nativeOrientation', 'angleBetween', 'transformBetween',
  'mapBetween', 'isPortrait', 'isLandscape', 'grabWindow', 'refreshRate'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScreen::~QScreen()': the destructor: Python never removes a C++
    QScreen.

  What has no ritual
  ------------------

  21 of the 57 functions Qt declares: 9 a signal; 7 takes or gives a type
  that cannot be passed yet; 2 a template; 2 forbidden; 1 declared and
  nowhere to be found.

  What to expect
  --------------

  - The C++ QScreen is created at the first use, not by 'QScreen(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScreen.
  - Qt tells when it has removed the C++ QScreen. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QScreen::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#tr

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
    #  QString QScreen::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QScreen2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScreen'

  #  A C++ QScreen Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScreen'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScreen::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScreen::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QScreen10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QScreen::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScreen::name() const
    return self.uglySide.call('ritual_ZNK7QScreen4nameEv')

  def manufacturer(self) -> str:
    """
    Calls Qt's 'QString QScreen::manufacturer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#manufacturer

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScreen::manufacturer() const
    return self.uglySide.call('ritual_ZNK7QScreen12manufacturerEv')

  def model(self) -> str:
    """
    Calls Qt's 'QString QScreen::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#model

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScreen::model() const
    return self.uglySide.call('ritual_ZNK7QScreen5modelEv')

  def serialNumber(self) -> str:
    """
    Calls Qt's 'QString QScreen::serialNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#serialNumber

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScreen::serialNumber() const
    return self.uglySide.call('ritual_ZNK7QScreen12serialNumberEv')

  def depth(self) -> int:
    """
    Calls Qt's 'int QScreen::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#depth
    """
    #  int QScreen::depth() const
    return self.uglySide.call('ritual_ZNK7QScreen5depthEv')

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QScreen::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QScreen::size() const
    address = self.uglySide.call('ritual_ZNK7QScreen4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QScreen::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QScreen::geometry() const
    address = self.uglySide.call('ritual_ZNK7QScreen8geometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def physicalSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QScreen::physicalSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#physicalSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QScreen::physicalSize() const
    address = self.uglySide.call('ritual_ZNK7QScreen12physicalSizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def physicalDotsPerInchX(self) -> float:
    """
    Calls Qt's 'qreal QScreen::physicalDotsPerInchX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#physicalDotsPerInchX
    """
    #  qreal QScreen::physicalDotsPerInchX() const
    return self.uglySide.call('ritual_ZNK7QScreen20physicalDotsPerInchXEv')

  def physicalDotsPerInchY(self) -> float:
    """
    Calls Qt's 'qreal QScreen::physicalDotsPerInchY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#physicalDotsPerInchY
    """
    #  qreal QScreen::physicalDotsPerInchY() const
    return self.uglySide.call('ritual_ZNK7QScreen20physicalDotsPerInchYEv')

  def physicalDotsPerInch(self) -> float:
    """
    Calls Qt's 'qreal QScreen::physicalDotsPerInch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#physicalDotsPerInch
    """
    #  qreal QScreen::physicalDotsPerInch() const
    return self.uglySide.call('ritual_ZNK7QScreen19physicalDotsPerInchEv')

  def logicalDotsPerInchX(self) -> float:
    """
    Calls Qt's 'qreal QScreen::logicalDotsPerInchX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#logicalDotsPerInchX
    """
    #  qreal QScreen::logicalDotsPerInchX() const
    return self.uglySide.call('ritual_ZNK7QScreen19logicalDotsPerInchXEv')

  def logicalDotsPerInchY(self) -> float:
    """
    Calls Qt's 'qreal QScreen::logicalDotsPerInchY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#logicalDotsPerInchY
    """
    #  qreal QScreen::logicalDotsPerInchY() const
    return self.uglySide.call('ritual_ZNK7QScreen19logicalDotsPerInchYEv')

  def logicalDotsPerInch(self) -> float:
    """
    Calls Qt's 'qreal QScreen::logicalDotsPerInch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#logicalDotsPerInch
    """
    #  qreal QScreen::logicalDotsPerInch() const
    return self.uglySide.call('ritual_ZNK7QScreen18logicalDotsPerInchEv')

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QScreen::devicePixelRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#devicePixelRatio
    """
    #  qreal QScreen::devicePixelRatio() const
    return self.uglySide.call('ritual_ZNK7QScreen16devicePixelRatioEv')

  def availableSize(self) -> QSize:
    """
    Calls Qt's 'QSize QScreen::availableSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#availableSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QScreen::availableSize() const
    address = self.uglySide.call('ritual_ZNK7QScreen13availableSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def availableGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QScreen::availableGeometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#availableGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QScreen::availableGeometry() const
    address = self.uglySide.call('ritual_ZNK7QScreen17availableGeometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def virtualSiblings(self) -> QList[QScreen]:
    """
    Calls Qt's 'QList<QScreen *> QScreen::virtualSiblings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#virtualSiblings

    Returns
    -------

    QList[QScreen]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScreen *> QScreen::virtualSiblings() const
    address = self.uglySide.call('ritual_ZNK7QScreen15virtualSiblingsEv')
    return QList[QScreen]._cuteOwning(address)

  def virtualSize(self) -> QSize:
    """
    Calls Qt's 'QSize QScreen::virtualSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#virtualSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QScreen::virtualSize() const
    address = self.uglySide.call('ritual_ZNK7QScreen11virtualSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def virtualGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QScreen::virtualGeometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#virtualGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QScreen::virtualGeometry() const
    address = self.uglySide.call('ritual_ZNK7QScreen15virtualGeometryEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def availableVirtualSize(self) -> QSize:
    """
    Calls Qt's 'QSize QScreen::availableVirtualSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#availableVirtualSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QScreen::availableVirtualSize() const
    address = self.uglySide.call(
        'ritual_ZNK7QScreen20availableVirtualSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def availableVirtualGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QScreen::availableVirtualGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscreen.html#availableVirtualGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QScreen::availableVirtualGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK7QScreen24availableVirtualGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def primaryOrientation(self) -> Qt.ScreenOrientation:
    """
    Calls Qt's 'Qt::ScreenOrientation QScreen::primaryOrientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#primaryOrientation

    Returns
    -------

    Qt.ScreenOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScreenOrientation(number)' gives.
    """
    #  Qt::ScreenOrientation QScreen::primaryOrientation() const
    return Qt.ScreenOrientation(self.uglySide.call(
        'ritual_ZNK7QScreen18primaryOrientationEv',
    ))

  def orientation(self) -> Qt.ScreenOrientation:
    """
    Calls Qt's 'Qt::ScreenOrientation QScreen::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#orientation

    Returns
    -------

    Qt.ScreenOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScreenOrientation(number)' gives.
    """
    #  Qt::ScreenOrientation QScreen::orientation() const
    return Qt.ScreenOrientation(self.uglySide.call(
        'ritual_ZNK7QScreen11orientationEv',
    ))

  def nativeOrientation(self) -> Qt.ScreenOrientation:
    """
    Calls Qt's 'Qt::ScreenOrientation QScreen::nativeOrientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#nativeOrientation

    Returns
    -------

    Qt.ScreenOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScreenOrientation(number)' gives.
    """
    #  Qt::ScreenOrientation QScreen::nativeOrientation() const
    return Qt.ScreenOrientation(self.uglySide.call(
        'ritual_ZNK7QScreen17nativeOrientationEv',
    ))

  @overload(Qt.ScreenOrientation, Qt.ScreenOrientation)
  def angleBetween(
      self,
      a: Qt.ScreenOrientation,
      b: Qt.ScreenOrientation,
  ) -> int:
    """
    Calls Qt's 'int QScreen::angleBetween(Qt::ScreenOrientation a,
    Qt::ScreenOrientation b) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#angleBetween

    Parameters
    ----------

    a : Qt.ScreenOrientation
      Passed on as its number.

    b : Qt.ScreenOrientation
      Passed on as its number.
    """
    #  int QScreen::angleBetween(Qt::ScreenOrientation a,
    #      Qt::ScreenOrientation b) const
    return self.uglySide.call(
        'ritual_ZNK7QScreen12angleBetweenEN2Qt17ScreenOrientationES1_',
        a.value, b.value,
    )

  @overload(Qt.ScreenOrientation, Qt.ScreenOrientation, QRect)
  def transformBetween(
      self,
      a: Qt.ScreenOrientation,
      b: Qt.ScreenOrientation,
      target: QRect,
  ) -> QTransform:
    """
    Calls Qt's 'QTransform QScreen::transformBetween(Qt::ScreenOrientation a,
    Qt::ScreenOrientation b, const QRect &target) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#transformBetween

    Parameters
    ----------

    a : Qt.ScreenOrientation
      Passed on as its number.

    b : Qt.ScreenOrientation
      Passed on as its number.

    target : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QScreen::transformBetween(Qt::ScreenOrientation a,
    #      Qt::ScreenOrientation b, const QRect &target) const
    address = self.uglySide.call(
        'ritual_ZNK7QScreen16transformBetweenEN2Qt17ScreenOrientationES1_RK'
        '5QRect',
        a.value, b.value, self._valueOf(target),
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

  @overload(Qt.ScreenOrientation, Qt.ScreenOrientation, QRect)
  def mapBetween(
      self,
      a: Qt.ScreenOrientation,
      b: Qt.ScreenOrientation,
      rect: QRect,
  ) -> QRect:
    """
    Calls Qt's 'QRect QScreen::mapBetween(Qt::ScreenOrientation a,
    Qt::ScreenOrientation b, const QRect &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#mapBetween

    Parameters
    ----------

    a : Qt.ScreenOrientation
      Passed on as its number.

    b : Qt.ScreenOrientation
      Passed on as its number.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QScreen::mapBetween(Qt::ScreenOrientation a,
    #      Qt::ScreenOrientation b, const QRect &rect) const
    address = self.uglySide.call(
        'ritual_ZNK7QScreen10mapBetweenEN2Qt17ScreenOrientationES1_RK5QRect',
        a.value, b.value, self._valueOf(rect),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(Qt.ScreenOrientation)
  def isPortrait(self, orientation: Qt.ScreenOrientation) -> bool:
    """
    Calls Qt's 'bool QScreen::isPortrait(Qt::ScreenOrientation orientation)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#isPortrait

    Parameters
    ----------

    orientation : Qt.ScreenOrientation
      Passed on as its number.
    """
    #  bool QScreen::isPortrait(Qt::ScreenOrientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK7QScreen10isPortraitEN2Qt17ScreenOrientationE',
        orientation.value,
    )

  @overload(Qt.ScreenOrientation)
  def isLandscape(self, orientation: Qt.ScreenOrientation) -> bool:
    """
    Calls Qt's 'bool QScreen::isLandscape(Qt::ScreenOrientation orientation)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#isLandscape

    Parameters
    ----------

    orientation : Qt.ScreenOrientation
      Passed on as its number.
    """
    #  bool QScreen::isLandscape(Qt::ScreenOrientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK7QScreen11isLandscapeEN2Qt17ScreenOrientationE',
        orientation.value,
    )

  def refreshRate(self) -> float:
    """
    Calls Qt's 'qreal QScreen::refreshRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#refreshRate
    """
    #  qreal QScreen::refreshRate() const
    return self.uglySide.call('ritual_ZNK7QScreen11refreshRateEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QPoint)
  def virtualSiblingAt(self, point: QPoint) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QScreen::virtualSiblingAt(QPoint point)'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#virtualSiblingAt

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QScreen::virtualSiblingAt(QPoint point)
    address = self.uglySide.call(
        'ritual_ZN7QScreen16virtualSiblingAtE6QPoint', self._valueOf(point),
    )
    return QScreen._cuteAt(address)

  @overload()
  @overload(int)
  @overload(int, int)
  @overload(int, int, int)
  @overload(int, int, int, int)
  @overload(int, int, int, int, int)
  def grabWindow(
      self,
      window: int = 0,
      x: int = 0,
      y: int = 0,
      w: int = -1,
      h: int = -1,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QScreen::grabWindow(WId window, int x, int y, int w,
    int h)'.

    Qt's own words: https://doc.qt.io/qt-6/qscreen.html#grabWindow

    Parameters
    ----------

    window : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    x : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    y : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    w : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    h : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QScreen::grabWindow(WId window, int x, int y, int w, int h)
    address = self.uglySide.call(
        'ritual_ZN7QScreen10grabWindowEyiiii', window, x, y, w, h,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)


#  Qt's 'QList<QScreen *>': the list of QScreen, which 'QList[QScreen]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QScreen.
QList.createKind(
    QScreen, 'address',
    make='ritual_list_make_QScreen_ptr',
    add='ritual_list_add_QScreen_ptr',
    size='ritual_list_size_QScreen_ptr',
    at='ritual_list_at_QScreen_ptr',
    drop='ritual_list_drop_QScreen_ptr',
)
