"""
QBackingStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qbackingstore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QSize
  from . import QPaintDevice, QPlatformBackingStore, QRegion, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QRegion = WAIT['QRegion']
  QSize = WAIT['QSize']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBackingStore(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBackingStore: a plain Python object standing in
  front of one C++ QBackingStore.

  What exists
  -----------

  Every function of Qt's QBackingStore that has a ritual and that Python can
  call so far, 12 names in all: 'window', 'paintDevice', 'flush', 'resize',
  'size', 'scroll', 'beginPaint', 'endPaint', 'setStaticContents',
  'staticContents', 'hasStaticContents', 'handle'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBackingStore::~QBackingStore()': the destructor: Python never
    removes a C++ QBackingStore.

  What to expect
  --------------

  - The C++ QBackingStore is created at the first use, not by
    'QBackingStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBackingStore.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBackingStore'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def window(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QBackingStore::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#window

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QBackingStore::window() const
    address = self.uglySide.call('ritual_ZNK13QBackingStore6windowEv')
    from . import QWindow
    return QWindow._cuteAt(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QBackingStore::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QBackingStore::size() const
    address = self.uglySide.call('ritual_ZNK13QBackingStore4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def staticContents(self) -> QRegion:
    """
    Calls Qt's 'QRegion QBackingStore::staticContents() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#staticContents

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QBackingStore::staticContents() const
    address = self.uglySide.call(
        'ritual_ZNK13QBackingStore14staticContentsEv',
    )
    from . import QRegion
    return QRegion._cuteOwning(address)

  def hasStaticContents(self) -> bool:
    """
    Calls Qt's 'bool QBackingStore::hasStaticContents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstore.html#hasStaticContents
    """
    #  bool QBackingStore::hasStaticContents() const
    return self.uglySide.call(
        'ritual_ZNK13QBackingStore17hasStaticContentsEv',
    )

  def handle(self) -> Optional[QPlatformBackingStore]:
    """
    Calls Qt's 'QPlatformBackingStore *QBackingStore::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#handle

    Returns
    -------

    Optional[QPlatformBackingStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformBackingStore *QBackingStore::handle() const
    address = self.uglySide.call('ritual_ZNK13QBackingStore6handleEv')
    from . import QPlatformBackingStore
    return QPlatformBackingStore._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRegion)
  def setStaticContents(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QBackingStore::setStaticContents(const QRegion
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbackingstore.html#setStaticContents

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QBackingStore::setStaticContents(const QRegion &region)
    self.uglySide.call(
        'ritual_ZN13QBackingStore17setStaticContentsERK7QRegion',
        self._valueOf(region),
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

  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, window: Optional[QWindow]) -> None:
    """
    Notes what was given, for Qt's 'QBackingStore::QBackingStore(QWindow
    *window)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#QBackingStore

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBackingStore::QBackingStore(QWindow *window)
    self._noteCreation(QBackingStore, lambda: Rituals.call(
        'ritual_ZN13QBackingStoreC1EP7QWindow', self._addressOf(window),
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

  def paintDevice(self) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QBackingStore::paintDevice()'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#paintDevice

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QBackingStore::paintDevice()
    address = self.uglySide.call('ritual_ZN13QBackingStore11paintDeviceEv')
    from . import QPaintDevice
    return QPaintDevice._cuteAt(address)

  @overload(QRegion)
  @overload(QRegion, QWindow)
  @overload(QRegion, NoneType)
  @overload(QRegion, QWindow, QPoint)
  @overload(QRegion, NoneType, QPoint)
  def flush(
      self,
      region: QRegion,
      window: Optional[QWindow] = None,
      offset: Optional[QPoint] = None,
  ) -> None:
    """
    Calls Qt's 'void QBackingStore::flush(const QRegion &region, QWindow
    *window, const QPoint &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#flush

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    offset : Optional[QPoint]
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own. May be left out, as in Qt: a new 'QPoint()' is then passed on.
    """
    #  void QBackingStore::flush(const QRegion &region, QWindow *window,
    #      const QPoint &offset)
    if offset is None:
      from ..QtCore import QPoint
      offset = QPoint()
    self.uglySide.call(
        'ritual_ZN13QBackingStore5flushERK7QRegionP7QWindowRK6QPoint',
        self._valueOf(region), self._addressOf(window),
        self._valueOf(offset),
    )

  @overload(QSize)
  def resize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QBackingStore::resize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#resize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QBackingStore::resize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN13QBackingStore6resizeERK5QSize', self._valueOf(size),
    )

  @overload(QRegion, int, int)
  def scroll(self, area: QRegion, dx: int, dy: int) -> bool:
    """
    Calls Qt's 'bool QBackingStore::scroll(const QRegion &area, int dx, int
    dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#scroll

    Parameters
    ----------

    area : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  bool QBackingStore::scroll(const QRegion &area, int dx, int dy)
    return self.uglySide.call(
        'ritual_ZN13QBackingStore6scrollERK7QRegionii',
        self._valueOf(area), dx, dy,
    )

  @overload(QRegion)
  def beginPaint(self, a0: QRegion) -> None:
    """
    Calls Qt's 'void QBackingStore::beginPaint(const QRegion &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#beginPaint

    Parameters
    ----------

    a0 : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QBackingStore::beginPaint(const QRegion &a0)
    self.uglySide.call(
        'ritual_ZN13QBackingStore10beginPaintERK7QRegion', self._valueOf(a0),
    )

  def endPaint(self) -> None:
    """
    Calls Qt's 'void QBackingStore::endPaint()'.

    Qt's own words: https://doc.qt.io/qt-6/qbackingstore.html#endPaint
    """
    #  void QBackingStore::endPaint()
    self.uglySide.call('ritual_ZN13QBackingStore8endPaintEv')
