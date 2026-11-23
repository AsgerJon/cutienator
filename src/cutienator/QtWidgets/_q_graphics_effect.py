"""
QGraphicsEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRectF
  from ..QtGui import QPainter, QPixmap
  from . import QGraphicsEffectSource
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsEffect(QObject):
  """
  The cute side of Qt's QGraphicsEffect: a plain Python object standing in
  front of one C++ QGraphicsEffect.

  It is built on the cute 'QObject', as Qt's QGraphicsEffect is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsEffect that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'boundingRectFor',
  'boundingRect', 'isEnabled', 'setEnabled', 'update', 'draw',
  'sourceChanged', 'updateBoundingRect', 'sourceIsPixmap',
  'sourceBoundingRect', 'drawSource', 'sourcePixmap', 'source'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsEffect::~QGraphicsEffect()': the destructor: Python never
    removes a C++ QGraphicsEffect.

  What has no ritual
  ------------------

  11 of the 27 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 the class is abstract, so C++ cannot make one; 2 forbidden; 1
  a template; 1 declared and nowhere to be found; 1 a signal.

  What to expect
  --------------

  - The C++ QGraphicsEffect is created at the first use, not by
    'QGraphicsEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsEffect.
  - Qt tells when it has removed the C++ QGraphicsEffect. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QGraphicsEffect, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ChangeFlag(CuteFlags):
    """
    The flags enum 'QGraphicsEffect::ChangeFlag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QGraphicsEffect::ChangeFlags'.
    """

    SourceAttached = 0x1
    SourceDetached = 0x2
    SourceBoundingRectChanged = 0x4
    SourceInvalidated = 0x8

  ChangeFlags = ChangeFlag

  class PixmapPadMode(CuteNum):
    """
    The enum 'QGraphicsEffect::PixmapPadMode' of Qt, with the 3 names Qt
    gives in it.
    """

    NoPad = Kee[int](0)
    PadToTransparentBorder = Kee[int](1)
    PadToEffectiveBoundingRect = Kee[int](2)

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
    Calls Qt's 'QString QGraphicsEffect::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#tr

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
    #  QString QGraphicsEffect::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QGraphicsEffect2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsEffect'

  #  A C++ QGraphicsEffect Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsEffect'

  #  The functions Qt calls itself that QGraphicsEffect is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'boundingRectFor': (
          ('_ZNK15QGraphicsEffect15boundingRectForERK6QRectF',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'draw': (
          ('_ZN15QGraphicsEffect4drawEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'sourceChanged': (
          ('_ZN15QGraphicsEffect13sourceChangedE6QFlagsINS_10ChangeFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtWidgets:QGraphicsEffect.ChangeFlag'),
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
    Calls Qt's 'const QMetaObject *QGraphicsEffect::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsEffect::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsEffect10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QRectF)
  def boundingRectFor(self, sourceRect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsEffect::boundingRectFor(const QRectF
    &sourceRect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffect.html#boundingRectFor

    Parameters
    ----------

    sourceRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsEffect::boundingRectFor(const QRectF &sourceRect)
    #      const
    ritual = 'ritual_ZNK15QGraphicsEffect15boundingRectForERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QGraphicsEffect15boundingRectForERK6QRectF'
    address = self.uglySide.call(ritual, self._valueOf(sourceRect))
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsEffect::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsEffect::boundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK15QGraphicsEffect12boundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsEffect::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#isEnabled
    """
    #  bool QGraphicsEffect::isEnabled() const
    return self.uglySide.call('ritual_ZNK15QGraphicsEffect9isEnabledEv')

  def sourceIsPixmap(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsEffect::sourceIsPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffect.html#sourceIsPixmap
    """
    #  bool QGraphicsEffect::sourceIsPixmap() const
    return self.uglySide.call(
        'ritual_ZNK15QGraphicsEffect14sourceIsPixmapEv',
    )

  @overload()
  @overload(Qt.CoordinateSystem)
  def sourceBoundingRect(
      self,
      system: Qt.CoordinateSystem = Qt.CoordinateSystem.LogicalCoordinates,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF
    QGraphicsEffect::sourceBoundingRect(Qt::CoordinateSystem system) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffect.html#sourceBoundingRect

    Parameters
    ----------

    system : Qt.CoordinateSystem
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CoordinateSystem.LogicalCoordinates.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsEffect::sourceBoundingRect(Qt::CoordinateSystem
    #      system) const
    address = self.uglySide.call(
        'ritual_ZNK15QGraphicsEffect18sourceBoundingRectEN2Qt16CoordinateSy'
        'stemE',
        system.value,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload()
  @overload(Qt.CoordinateSystem)
  @overload(Qt.CoordinateSystem, QPoint)
  @overload(Qt.CoordinateSystem, NoneType)
  @overload(Qt.CoordinateSystem, QPoint, PixmapPadMode)
  @overload(Qt.CoordinateSystem, NoneType, PixmapPadMode)
  def sourcePixmap(
      self,
      system: Qt.CoordinateSystem = Qt.CoordinateSystem.LogicalCoordinates,
      offset: Optional[QPoint] = None,
      mode: PixmapPadMode = PixmapPadMode.PadToEffectiveBoundingRect,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QGraphicsEffect::sourcePixmap(Qt::CoordinateSystem
    system, QPoint *offset, PixmapPadMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#sourcePixmap

    Parameters
    ----------

    system : Qt.CoordinateSystem
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CoordinateSystem.LogicalCoordinates.

    offset : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    mode : PixmapPadMode
      Passed on as its number. May be left out, as in Qt: it is then
      PixmapPadMode.PadToEffectiveBoundingRect.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QGraphicsEffect::sourcePixmap(Qt::CoordinateSystem system,
    #      QPoint *offset, PixmapPadMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK15QGraphicsEffect12sourcePixmapEN2Qt16CoordinateSystemEP'
        '6QPointNS_13PixmapPadModeE',
        system.value, self._addressOf(offset), mode.value,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def source(self) -> Optional[QGraphicsEffectSource]:
    """
    Calls Qt's 'QGraphicsEffectSource *QGraphicsEffect::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#source

    Returns
    -------

    Optional[QGraphicsEffectSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsEffectSource *QGraphicsEffect::source() const
    address = self.uglySide.call('ritual_ZNK15QGraphicsEffect6sourceEv')
    from . import QGraphicsEffectSource
    return QGraphicsEffectSource._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QGraphicsEffect::setEnabled(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#setEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QGraphicsEffect::setEnabled(bool enable)
    self.uglySide.call('ritual_ZN15QGraphicsEffect10setEnabledEb', enable)

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

  def update(self) -> None:
    """
    Calls Qt's 'void QGraphicsEffect::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#update
    """
    #  void QGraphicsEffect::update()
    self.uglySide.call('ritual_ZN15QGraphicsEffect6updateEv')

  @overload(QPainter)
  @overload(NoneType)
  def draw(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QGraphicsEffect::draw(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#draw

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsEffect::draw(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN15QGraphicsEffect4drawEP8QPainter',
        self._addressOf(painter),
    )

  @overload(ChangeFlags)
  def sourceChanged(self, flags: ChangeFlags) -> None:
    """
    Calls Qt's 'void QGraphicsEffect::sourceChanged(ChangeFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#sourceChanged

    Parameters
    ----------

    flags : ChangeFlags
      Passed on as its number.
    """
    #  void QGraphicsEffect::sourceChanged(ChangeFlags flags)
    ritual = (
        'ritual_ZN15QGraphicsEffect13sourceChangedE6QFlagsINS_10ChangeFlagE'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QGraphicsEffect13sourceChangedE6QFlagsINS_10Chang'
          'eFlagEE')
    self.uglySide.call(ritual, flags.value)

  def updateBoundingRect(self) -> None:
    """
    Calls Qt's 'void QGraphicsEffect::updateBoundingRect()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffect.html#updateBoundingRect
    """
    #  void QGraphicsEffect::updateBoundingRect()
    self.uglySide.call('ritual_ZN15QGraphicsEffect18updateBoundingRectEv')

  @overload(QPainter)
  @overload(NoneType)
  def drawSource(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QGraphicsEffect::drawSource(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffect.html#drawSource

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsEffect::drawSource(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN15QGraphicsEffect10drawSourceEP8QPainter',
        self._addressOf(painter),
    )
