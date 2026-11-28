"""
QPaintEngineEx binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpaintengineex_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPaintEngineEx to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..QtCore import Qt
from . import QPaintEngine, QPainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLine, QLineF, QPoint, QPointF, QRect, QRectF
  from . import QBrush, QColor, QFontEngine, QImage, QPaintEngineExPrivate
  from . import QPaintEngineState, QPainterPath, QPainterState, QPixmap
  from . import QRegion, QStaticTextItem, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']
  QFontEngine = WAIT['QFontEngine']
  QImage = WAIT['QImage']
  QLine = WAIT['QLine']
  QLineF = WAIT['QLineF']
  QPaintEngineState = WAIT['QPaintEngineState']
  QPainterPath = WAIT['QPainterPath']
  QPainterState = WAIT['QPainterState']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QRegion = WAIT['QRegion']
  QStaticTextItem = WAIT['QStaticTextItem']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPaintEngineEx(QPaintEngine):
  """
  The cute side of Qt's QPaintEngineEx: a plain Python object standing in
  front of one C++ QPaintEngineEx.

  It is built on the cute 'QPaintEngine', as Qt's QPaintEngineEx is built on
  Qt's QPaintEngine, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPaintEngineEx that has a ritual and that Python can
  call so far, 33 names in all: 'd_func', 'createState', 'clip',
  'clipEnabledChanged', 'penChanged', 'brushChanged', 'brushOriginChanged',
  'opacityChanged', 'compositionModeChanged', 'renderHintsChanged',
  'transformChanged', 'fillRect', 'drawRoundedRect', 'drawRects',
  'drawLines', 'drawEllipse', 'drawPath', 'drawPoints', 'drawPolygon',
  'drawPixmap', 'drawImage', 'drawTiledPixmap', 'drawPixmapFragments',
  'updateState', 'drawStaticTextItem', 'setState', 'state', 'sync',
  'beginNativePainting', 'endNativePainting', 'flags',
  'requiresPretransformedGlyphPositions', 'shouldDrawCachedGlyphs'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPaintEngineExPrivate *QPaintEngineEx::d_func() const': takes
    in Python what 'QPaintEngineExPrivate *QPaintEngineEx::d_func()' takes.
  - Qt's 'void QPaintEngineEx::draw(const QVectorPath &path)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QPaintEngineEx::fill(const QVectorPath &path, const QBrush
    &brush)': takes a type Python has no way to hand over yet.
  - Qt's 'void QPaintEngineEx::stroke(const QVectorPath &path, const QPen
    &pen)': takes a type Python has no way to hand over yet.
  - Qt's 'void QPaintEngineEx::clip(const QVectorPath &path,
    Qt::ClipOperation op)': takes a type Python has no way to hand over yet.
  - Qt's 'const QPainterState *QPaintEngineEx::state() const': takes in
    Python what 'QPainterState *QPaintEngineEx::state()' takes.

  What has no ritual
  ------------------

  2 of the 51 functions Qt declares: 2 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QPaintEngineEx is created at the first use, not by
    'QPaintEngineEx(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPaintEngineEx.
  - Each name of Qt's QPaintEngineEx that has no cute function yet,
    '__init__', 'draw', 'fill', 'stroke', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPaintEngineEx, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flags(CuteNum):
    """
    The enum 'QPaintEngineEx::Flags' of Qt, with the 2 names Qt gives in it.
    """

    DoNotEmulate = Kee[int](1)
    IsEmulationEngine = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPaintEngineEx'

  #  A C++ QPaintEngineEx Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPaintEngineEx'

  #  The functions Qt calls itself that QPaintEngineEx is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'draw': (
          'void QPaintEngineEx::draw(const QVectorPath &)',
      ),
      'fill': (
          'void QPaintEngineEx::fill(const QVectorPath &, const QBrush &)',
      ),
      'stroke': (
          'void QPaintEngineEx::stroke(const QVectorPath &, const QPen &)',
      ),
  }

  #  The functions Qt calls itself that QPaintEngineEx is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createState': (
          ('_ZNK14QPaintEngineEx11createStateEP13QPainterState',
           ('address', 'address', 'QtGui:QPainterState'),
           (
               ('address', 'address', 'QtGui:QPainterState'),
           )),
      ),
      'clip': (
          ('_ZN14QPaintEngineEx4clipERK5QRectN2Qt13ClipOperationE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
               ('int', 'enum', 'QtCore:Qt.ClipOperation'),
           )),
          ('_ZN14QPaintEngineEx4clipERK7QRegionN2Qt13ClipOperationE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QRegion'),
               ('int', 'enum', 'QtCore:Qt.ClipOperation'),
           )),
          ('_ZN14QPaintEngineEx4clipERK12QPainterPathN2Qt13ClipOperationE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPainterPath'),
               ('int', 'enum', 'QtCore:Qt.ClipOperation'),
           )),
      ),
      'clipEnabledChanged': (
          ('_ZN14QPaintEngineEx18clipEnabledChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'penChanged': (
          ('_ZN14QPaintEngineEx10penChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'brushChanged': (
          ('_ZN14QPaintEngineEx12brushChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'brushOriginChanged': (
          ('_ZN14QPaintEngineEx18brushOriginChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'opacityChanged': (
          ('_ZN14QPaintEngineEx14opacityChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'compositionModeChanged': (
          ('_ZN14QPaintEngineEx22compositionModeChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'renderHintsChanged': (
          ('_ZN14QPaintEngineEx18renderHintsChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'transformChanged': (
          ('_ZN14QPaintEngineEx16transformChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'fillRect': (
          ('_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QBrush',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QBrush'),
           )),
          ('_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'drawRoundedRect': (
          ('_ZN14QPaintEngineEx15drawRoundedRectERK6QRectFddN2Qt8SizeModeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
               ('double', 'number', ''),
               ('double', 'number', ''),
               ('int', 'enum', 'QtCore:Qt.SizeMode'),
           )),
      ),
      'drawPixmap': (
          ('_ZN14QPaintEngineEx10drawPixmapERK7QPointFRK7QPixmap',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('address', 'value', 'QtGui:QPixmap'),
           )),
      ),
      'drawImage': (
          ('_ZN14QPaintEngineEx9drawImageERK7QPointFRK6QImage',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
               ('address', 'value', 'QtGui:QImage'),
           )),
      ),
      'drawPixmapFragments': (
          ('_ZN14QPaintEngineEx19drawPixmapFragmentsEPKN8QPainter14PixmapFr'
           'agmentEiRK7QPixmap6QFlagsINS0_18PixmapFragmentHintEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter.PixmapFragment'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QPixmap'),
               ('int', 'flags', 'QtGui:QPainter.PixmapFragmentHint'),
           )),
      ),
      'drawStaticTextItem': (
          ('_ZN14QPaintEngineEx18drawStaticTextItemEP15QStaticTextItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QStaticTextItem'),
           )),
      ),
      'setState': (
          ('_ZN14QPaintEngineEx8setStateEP13QPainterState',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainterState'),
           )),
      ),
      'sync': (
          ('_ZN14QPaintEngineEx4syncEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'beginNativePainting': (
          ('_ZN14QPaintEngineEx19beginNativePaintingEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endNativePainting': (
          ('_ZN14QPaintEngineEx17endNativePaintingEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'flags': (
          ('_ZNK14QPaintEngineEx5flagsEv',
           ('unsigned int', 'number', ''),
           ()),
      ),
      'requiresPretransformedGlyphPositions': (
          ('_ZNK14QPaintEngineEx36requiresPretransformedGlyphPositionsEP11Q'
           'FontEngineRK10QTransform',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QFontEngine'),
               ('address', 'value', 'QtGui:QTransform'),
           )),
      ),
      'shouldDrawCachedGlyphs': (
          ('_ZNK14QPaintEngineEx22shouldDrawCachedGlyphsEP11QFontEngineRK10'
           'QTransform',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QFontEngine'),
               ('address', 'value', 'QtGui:QTransform'),
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

  @overload(QPainterState)
  @overload(NoneType)
  def createState(
      self,
      orig: Optional[QPainterState],
  ) -> Optional[QPainterState]:
    """
    Calls Qt's 'QPainterState *QPaintEngineEx::createState(QPainterState
    *orig) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#createState

    Parameters
    ----------

    orig : Optional[QPainterState]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPainterState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainterState *QPaintEngineEx::createState(QPainterState *orig) const
    ritual = 'ritual_ZNK14QPaintEngineEx11createStateEP13QPainterState'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPaintEngineEx11createStateEP13QPainterState'
    address = self.uglySide.call(ritual, self._addressOf(orig))
    from . import QPainterState
    return QPainterState._cuteAt(address)

  def flags(self) -> int:
    """
    Calls Qt's 'uint QPaintEngineEx::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#flags
    """
    #  uint QPaintEngineEx::flags() const
    ritual = 'ritual_ZNK14QPaintEngineEx5flagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QPaintEngineEx5flagsEv'
    return self.uglySide.call(ritual)

  @overload(QFontEngine, QTransform)
  @overload(NoneType, QTransform)
  def requiresPretransformedGlyphPositions(
      self,
      fontEngine: Optional[QFontEngine],
      m: QTransform,
  ) -> bool:
    """
    Calls Qt's 'bool
    QPaintEngineEx::requiresPretransformedGlyphPositions(QFontEngine
    *fontEngine, const QTransform &m) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html

    Parameters
    ----------

    fontEngine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    m : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  bool QPaintEngineEx::requiresPretransformedGlyphPositions(QFontEngine
    #      *fontEngine, const QTransform &m) const
    ritual = (
        'ritual_ZNK14QPaintEngineEx36requiresPretransformedGlyphPositionsEP'
        '11QFontEngineRK10QTransform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QPaintEngineEx36requiresPretransformedGlyphPosit'
          'ionsEP11QFontEngineRK10QTransform')
    return self.uglySide.call(
        ritual, self._addressOf(fontEngine), self._valueOf(m),
    )

  @overload(QFontEngine, QTransform)
  @overload(NoneType, QTransform)
  def shouldDrawCachedGlyphs(
      self,
      fontEngine: Optional[QFontEngine],
      m: QTransform,
  ) -> bool:
    """
    Calls Qt's 'bool QPaintEngineEx::shouldDrawCachedGlyphs(QFontEngine
    *fontEngine, const QTransform &m) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#shouldDrawCachedGlyphs

    Parameters
    ----------

    fontEngine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    m : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  bool QPaintEngineEx::shouldDrawCachedGlyphs(QFontEngine *fontEngine,
    #      const QTransform &m) const
    ritual = (
        'ritual_ZNK14QPaintEngineEx22shouldDrawCachedGlyphsEP11QFontEngineR'
        'K10QTransform')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QPaintEngineEx22shouldDrawCachedGlyphsEP11QFontE'
          'ngineRK10QTransform')
    return self.uglySide.call(
        ritual, self._addressOf(fontEngine), self._valueOf(m),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPainterState)
  @overload(NoneType)
  def setState(self, s: Optional[QPainterState]) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::setState(QPainterState *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#setState

    Parameters
    ----------

    s : Optional[QPainterState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPaintEngineEx::setState(QPainterState *s)
    ritual = 'ritual_ZN14QPaintEngineEx8setStateEP13QPainterState'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx8setStateEP13QPainterState'
    self.uglySide.call(ritual, self._addressOf(s))

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
    - Qt's 'QPaintEngineEx::QPaintEngineEx()': the class is abstract, so C++
      cannot make one, and the C++ class of ours does not fill in every
      function it leaves open.
    - Qt's 'QPaintEngineEx::QPaintEngineEx(QPaintEngineExPrivate &data)': the
      class is abstract, so C++ cannot make one, and the C++ class of ours
      does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QPaintEngineEx.__init__' has no cute function yet. Qt's "
        "'QPaintEngineEx::QPaintEngineEx()': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open. Qt's "
        "'QPaintEngineEx::QPaintEngineEx(QPaintEngineExPrivate &data)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  def d_func(self) -> Optional[QPaintEngineExPrivate]:
    """
    Calls Qt's 'QPaintEngineExPrivate *QPaintEngineEx::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#d_func

    Returns
    -------

    Optional[QPaintEngineExPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngineExPrivate *QPaintEngineEx::d_func()
    address = self.uglySide.call('ritual_ZN14QPaintEngineEx6d_funcEv')
    from . import QPaintEngineExPrivate
    return QPaintEngineExPrivate._cuteAt(address)

  @overload(QRect, Qt.ClipOperation)
  def clip(self, rect: QRect, op: Qt.ClipOperation) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::clip(const QRect &rect,
    Qt::ClipOperation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#clip

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    op : Qt.ClipOperation
      Passed on as its number.
    """
    #  void QPaintEngineEx::clip(const QRect &rect, Qt::ClipOperation op)
    ritual = 'ritual_ZN14QPaintEngineEx4clipERK5QRectN2Qt13ClipOperationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx4clipERK5QRectN2Qt13ClipOperationE')
    self.uglySide.call(ritual, self._valueOf(rect), op.value)

  @overload(QRegion, Qt.ClipOperation)
  def clip(self, region: QRegion, op: Qt.ClipOperation) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::clip(const QRegion &region,
    Qt::ClipOperation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#clip

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    op : Qt.ClipOperation
      Passed on as its number.
    """
    #  void QPaintEngineEx::clip(const QRegion &region, Qt::ClipOperation op)
    ritual = 'ritual_ZN14QPaintEngineEx4clipERK7QRegionN2Qt13ClipOperationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx4clipERK7QRegionN2Qt13ClipOperation'
          'E')
    self.uglySide.call(ritual, self._valueOf(region), op.value)

  @overload(QPainterPath, Qt.ClipOperation)
  def clip(self, path: QPainterPath, op: Qt.ClipOperation) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::clip(const QPainterPath &path,
    Qt::ClipOperation op)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#clip

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    op : Qt.ClipOperation
      Passed on as its number.
    """
    #  void QPaintEngineEx::clip(const QPainterPath &path, Qt::ClipOperation
    #      op)
    ritual = (
        'ritual_ZN14QPaintEngineEx4clipERK12QPainterPathN2Qt13ClipOperation'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx4clipERK12QPainterPathN2Qt13ClipOpe'
          'rationE')
    self.uglySide.call(ritual, self._valueOf(path), op.value)

  def clipEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::clipEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#clipEnabledChanged
    """
    #  void QPaintEngineEx::clipEnabledChanged()
    self.uglySide.call('ritual_ZN14QPaintEngineEx18clipEnabledChangedEv')

  def penChanged(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::penChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#penChanged
    """
    #  void QPaintEngineEx::penChanged()
    self.uglySide.call('ritual_ZN14QPaintEngineEx10penChangedEv')

  def brushChanged(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::brushChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#brushChanged
    """
    #  void QPaintEngineEx::brushChanged()
    self.uglySide.call('ritual_ZN14QPaintEngineEx12brushChangedEv')

  def brushOriginChanged(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::brushOriginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#brushOriginChanged
    """
    #  void QPaintEngineEx::brushOriginChanged()
    self.uglySide.call('ritual_ZN14QPaintEngineEx18brushOriginChangedEv')

  def opacityChanged(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::opacityChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#opacityChanged
    """
    #  void QPaintEngineEx::opacityChanged()
    self.uglySide.call('ritual_ZN14QPaintEngineEx14opacityChangedEv')

  def compositionModeChanged(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::compositionModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#compositionModeChanged
    """
    #  void QPaintEngineEx::compositionModeChanged()
    self.uglySide.call('ritual_ZN14QPaintEngineEx22compositionModeChangedEv')

  def renderHintsChanged(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::renderHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#renderHintsChanged
    """
    #  void QPaintEngineEx::renderHintsChanged()
    self.uglySide.call('ritual_ZN14QPaintEngineEx18renderHintsChangedEv')

  def transformChanged(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::transformChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#transformChanged
    """
    #  void QPaintEngineEx::transformChanged()
    self.uglySide.call('ritual_ZN14QPaintEngineEx16transformChangedEv')

  @overload(QRectF, QBrush)
  def fillRect(self, rect: QRectF, brush: QBrush) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::fillRect(const QRectF &rect, const
    QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#fillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPaintEngineEx::fillRect(const QRectF &rect, const QBrush &brush)
    ritual = 'ritual_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QBrush'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QBrush'
    self.uglySide.call(ritual, self._valueOf(rect), self._valueOf(brush))

  @overload(QRectF, QColor)
  def fillRect(self, rect: QRectF, color: QColor) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::fillRect(const QRectF &rect, const
    QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#fillRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPaintEngineEx::fillRect(const QRectF &rect, const QColor &color)
    ritual = 'ritual_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx8fillRectERK6QRectFRK6QColor'
    self.uglySide.call(ritual, self._valueOf(rect), self._valueOf(color))

  @overload(QRectF, float, float, Qt.SizeMode)
  def drawRoundedRect(
      self,
      rect: QRectF,
      xrad: float,
      yrad: float,
      mode: Qt.SizeMode,
  ) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawRoundedRect(const QRectF &rect,
    qreal xrad, qreal yrad, Qt::SizeMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#drawRoundedRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    xrad : float
      Passed on as it is.

    yrad : float
      Passed on as it is.

    mode : Qt.SizeMode
      Passed on as its number.
    """
    #  void QPaintEngineEx::drawRoundedRect(const QRectF &rect, qreal xrad,
    #      qreal yrad, Qt::SizeMode mode)
    ritual = (
        'ritual_ZN14QPaintEngineEx15drawRoundedRectERK6QRectFddN2Qt8SizeMod'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx15drawRoundedRectERK6QRectFddN2Qt8S'
          'izeModeE')
    self.uglySide.call(ritual, self._valueOf(rect), xrad, yrad, mode.value)

  @overload(QRect, int)
  @overload(NoneType, int)
  def drawRects(self, rects: Optional[QRect], rectCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawRects(const QRect *rects, int
    rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawRects

    Parameters
    ----------

    rects : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QPaintEngineEx::drawRects(const QRect *rects, int rectCount)
    ritual = 'ritual_ZN14QPaintEngineEx9drawRectsEPK5QRecti'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx9drawRectsEPK5QRecti'
    self.uglySide.call(ritual, self._addressOf(rects), rectCount)

  @overload(QRectF, int)
  def drawRects(self, rects: Optional[QRectF], rectCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawRects(const QRectF *rects, int
    rectCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawRects

    Parameters
    ----------

    rects : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rectCount : int
      Passed on as it is.
    """
    #  void QPaintEngineEx::drawRects(const QRectF *rects, int rectCount)
    ritual = 'ritual_ZN14QPaintEngineEx9drawRectsEPK6QRectFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx9drawRectsEPK6QRectFi'
    self.uglySide.call(ritual, self._addressOf(rects), rectCount)

  @overload(QLine, int)
  @overload(NoneType, int)
  def drawLines(self, lines: Optional[QLine], lineCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawLines(const QLine *lines, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawLines

    Parameters
    ----------

    lines : Optional[QLine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QPaintEngineEx::drawLines(const QLine *lines, int lineCount)
    ritual = 'ritual_ZN14QPaintEngineEx9drawLinesEPK5QLinei'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx9drawLinesEPK5QLinei'
    self.uglySide.call(ritual, self._addressOf(lines), lineCount)

  @overload(QLineF, int)
  def drawLines(self, lines: Optional[QLineF], lineCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawLines(const QLineF *lines, int
    lineCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawLines

    Parameters
    ----------

    lines : Optional[QLineF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lineCount : int
      Passed on as it is.
    """
    #  void QPaintEngineEx::drawLines(const QLineF *lines, int lineCount)
    ritual = 'ritual_ZN14QPaintEngineEx9drawLinesEPK6QLineFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx9drawLinesEPK6QLineFi'
    self.uglySide.call(ritual, self._addressOf(lines), lineCount)

  @overload(QRectF)
  def drawEllipse(self, r: QRectF) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawEllipse(const QRectF &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawEllipse

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPaintEngineEx::drawEllipse(const QRectF &r)
    ritual = 'ritual_ZN14QPaintEngineEx11drawEllipseERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx11drawEllipseERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(r))

  @overload(QRect)
  def drawEllipse(self, r: QRect) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawEllipse(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawEllipse

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QPaintEngineEx::drawEllipse(const QRect &r)
    ritual = 'ritual_ZN14QPaintEngineEx11drawEllipseERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx11drawEllipseERK5QRect'
    self.uglySide.call(ritual, self._valueOf(r))

  @overload(QPainterPath)
  def drawPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QPaintEngineEx::drawPath(const QPainterPath &path)
    ritual = 'ritual_ZN14QPaintEngineEx8drawPathERK12QPainterPath'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx8drawPathERK12QPainterPath'
    self.uglySide.call(ritual, self._valueOf(path))

  @overload(QPointF, int)
  @overload(NoneType, int)
  def drawPoints(self, points: Optional[QPointF], pointCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawPoints(const QPointF *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawPoints

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPaintEngineEx::drawPoints(const QPointF *points, int pointCount)
    ritual = 'ritual_ZN14QPaintEngineEx10drawPointsEPK7QPointFi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx10drawPointsEPK7QPointFi'
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount,
    )

  @overload(QPoint, int)
  def drawPoints(self, points: Optional[QPoint], pointCount: int) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawPoints(const QPoint *points, int
    pointCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawPoints

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.
    """
    #  void QPaintEngineEx::drawPoints(const QPoint *points, int pointCount)
    ritual = 'ritual_ZN14QPaintEngineEx10drawPointsEPK6QPointi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx10drawPointsEPK6QPointi'
    self.uglySide.call(ritual, self._addressOf(points), pointCount)

  @overload(QPointF, int, QPaintEngine.PolygonDrawMode)
  @overload(NoneType, int, QPaintEngine.PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPointF],
      pointCount: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawPolygon(const QPointF *points, int
    pointCount, PolygonDrawMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPointF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    mode : QPaintEngine.PolygonDrawMode
      Passed on as its number.
    """
    #  void QPaintEngineEx::drawPolygon(const QPointF *points, int
    #      pointCount, PolygonDrawMode mode)
    ritual = (
        'ritual_ZN14QPaintEngineEx11drawPolygonEPK7QPointFiN12QPaintEngine1'
        '5PolygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx11drawPolygonEPK7QPointFiN12QPaintE'
          'ngine15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points, 'QPointF'), pointCount, mode.value,
    )

  @overload(QPoint, int, QPaintEngine.PolygonDrawMode)
  def drawPolygon(
      self,
      points: Optional[QPoint],
      pointCount: int,
      mode: QPaintEngine.PolygonDrawMode,
  ) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawPolygon(const QPoint *points, int
    pointCount, PolygonDrawMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawPolygon

    Parameters
    ----------

    points : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pointCount : int
      Passed on as it is.

    mode : QPaintEngine.PolygonDrawMode
      Passed on as its number.
    """
    #  void QPaintEngineEx::drawPolygon(const QPoint *points, int pointCount,
    #      PolygonDrawMode mode)
    ritual = (
        'ritual_ZN14QPaintEngineEx11drawPolygonEPK6QPointiN12QPaintEngine15'
        'PolygonDrawModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx11drawPolygonEPK6QPointiN12QPaintEn'
          'gine15PolygonDrawModeE')
    self.uglySide.call(
        ritual, self._addressOf(points), pointCount, mode.value,
    )

  @overload(QRectF, QPixmap, QRectF)
  def drawPixmap(self, r: QRectF, pm: QPixmap, sr: QRectF) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawPixmap(const QRectF &r, const
    QPixmap &pm, const QRectF &sr)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawPixmap

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPaintEngineEx::drawPixmap(const QRectF &r, const QPixmap &pm,
    #      const QRectF &sr)
    self.uglySide.call(
        'ritual_ZN14QPaintEngineEx10drawPixmapERK6QRectFRK7QPixmapS2_',
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr),
    )

  @overload(QPointF, QPixmap)
  def drawPixmap(self, pos: QPointF, pm: QPixmap) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawPixmap(const QPointF &pos, const
    QPixmap &pm)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawPixmap

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pm : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QPaintEngineEx::drawPixmap(const QPointF &pos, const QPixmap &pm)
    ritual = 'ritual_ZN14QPaintEngineEx10drawPixmapERK7QPointFRK7QPixmap'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx10drawPixmapERK7QPointFRK7QPixmap')
    self.uglySide.call(
        ritual, self._valueOf(pos, 'QPointF'), self._valueOf(pm),
    )

  @overload(QRectF, QImage, QRectF)
  @overload(QRectF, QImage, QRectF, Qt.ImageConversionFlags)
  def drawImage(
      self,
      r: QRectF,
      pm: QImage,
      sr: QRectF,
      flags: Qt.ImageConversionFlags = Qt.ImageConversionFlags.AutoColor,
  ) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawImage(const QRectF &r, const QImage
    &pm, const QRectF &sr, Qt::ImageConversionFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawImage

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pm : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    sr : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    flags : Qt.ImageConversionFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ImageConversionFlags.AutoColor.
    """
    #  void QPaintEngineEx::drawImage(const QRectF &r, const QImage &pm,
    #      const QRectF &sr, Qt::ImageConversionFlags flags)
    self.uglySide.call(
        'ritual_ZN14QPaintEngineEx9drawImageERK6QRectFRK6QImageS2_6QFlagsIN'
        '2Qt19ImageConversionFlagEE',
        self._valueOf(r), self._valueOf(pm), self._valueOf(sr), flags.value,
    )

  @overload(QPointF, QImage)
  def drawImage(self, pos: QPointF, image: QImage) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawImage(const QPointF &pos, const
    QImage &image)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#drawImage

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QPaintEngineEx::drawImage(const QPointF &pos, const QImage
    #      &image)
    ritual = 'ritual_ZN14QPaintEngineEx9drawImageERK7QPointFRK6QImage'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx9drawImageERK7QPointFRK6QImage'
    self.uglySide.call(
        ritual, self._valueOf(pos, 'QPointF'), self._valueOf(image),
    )

  @overload(QRectF, QPixmap, QPointF)
  def drawTiledPixmap(self, r: QRectF, pixmap: QPixmap, s: QPointF) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawTiledPixmap(const QRectF &r, const
    QPixmap &pixmap, const QPointF &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#drawTiledPixmap

    Parameters
    ----------

    r : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    s : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPaintEngineEx::drawTiledPixmap(const QRectF &r, const QPixmap
    #      &pixmap, const QPointF &s)
    ritual = (
        'ritual_ZN14QPaintEngineEx15drawTiledPixmapERK6QRectFRK7QPixmapRK7Q'
        'PointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx15drawTiledPixmapERK6QRectFRK7QPixm'
          'apRK7QPointF')
    self.uglySide.call(
        ritual,
        self._valueOf(r), self._valueOf(pixmap), self._valueOf(s, 'QPointF'),
    )

  @overload(
      QPainter.PixmapFragment, int, QPixmap, QPainter.PixmapFragmentHints,
  )
  @overload(NoneType, int, QPixmap, QPainter.PixmapFragmentHints)
  def drawPixmapFragments(
      self,
      fragments: Optional[QPainter.PixmapFragment],
      fragmentCount: int,
      pixmap: QPixmap,
      hints: QPainter.PixmapFragmentHints,
  ) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawPixmapFragments(const
    QPainter::PixmapFragment *fragments, int fragmentCount, const QPixmap
    &pixmap, QFlags<QPainter::PixmapFragmentHint> hints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#drawPixmapFragments

    Parameters
    ----------

    fragments : Optional[QPainter.PixmapFragment]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fragmentCount : int
      Passed on as it is.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    hints : QPainter.PixmapFragmentHints
      Passed on as its number.
    """
    #  void QPaintEngineEx::drawPixmapFragments(const
    #      QPainter::PixmapFragment *fragments, int fragmentCount, const
    #      QPixmap &pixmap, QFlags<QPainter::PixmapFragmentHint> hints)
    ritual = (
        'ritual_ZN14QPaintEngineEx19drawPixmapFragmentsEPKN8QPainter14Pixma'
        'pFragmentEiRK7QPixmap6QFlagsINS0_18PixmapFragmentHintEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx19drawPixmapFragmentsEPKN8QPainter1'
          '4PixmapFragmentEiRK7QPixmap6QFlagsINS0_18PixmapFragmentHintEE')
    self.uglySide.call(
        ritual,
        self._addressOf(fragments), fragmentCount, self._valueOf(pixmap),
        hints.value,
    )

  @overload(QPaintEngineState)
  def updateState(self, state: QPaintEngineState) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::updateState(const QPaintEngineState
    &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#updateState

    Parameters
    ----------

    state : QPaintEngineState
      Passed on as a value: Qt reads the C++ QPaintEngineState, which stays
      Python's own.
    """
    #  void QPaintEngineEx::updateState(const QPaintEngineState &state)
    ritual = 'ritual_ZN14QPaintEngineEx11updateStateERK17QPaintEngineState'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx11updateStateERK17QPaintEngineState')
    self.uglySide.call(ritual, self._valueOf(state))

  @overload(QStaticTextItem)
  @overload(NoneType)
  def drawStaticTextItem(self, a0: Optional[QStaticTextItem]) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::drawStaticTextItem(QStaticTextItem
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#drawStaticTextItem

    Parameters
    ----------

    a0 : Optional[QStaticTextItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPaintEngineEx::drawStaticTextItem(QStaticTextItem *a0)
    ritual = (
        'ritual_ZN14QPaintEngineEx18drawStaticTextItemEP15QStaticTextItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QPaintEngineEx18drawStaticTextItemEP15QStaticText'
          'Item')
    self.uglySide.call(ritual, self._addressOf(a0))

  def state(self) -> Optional[QPainterState]:
    """
    Calls Qt's 'QPainterState *QPaintEngineEx::state()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#state

    Returns
    -------

    Optional[QPainterState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainterState *QPaintEngineEx::state()
    address = self.uglySide.call('ritual_ZN14QPaintEngineEx5stateEv')
    from . import QPainterState
    return QPainterState._cuteAt(address)

  def sync(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineex.html#sync
    """
    #  void QPaintEngineEx::sync()
    ritual = 'ritual_ZN14QPaintEngineEx4syncEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx4syncEv'
    self.uglySide.call(ritual)

  def beginNativePainting(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::beginNativePainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#beginNativePainting
    """
    #  void QPaintEngineEx::beginNativePainting()
    ritual = 'ritual_ZN14QPaintEngineEx19beginNativePaintingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx19beginNativePaintingEv'
    self.uglySide.call(ritual)

  def endNativePainting(self) -> None:
    """
    Calls Qt's 'void QPaintEngineEx::endNativePainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineex.html#endNativePainting
    """
    #  void QPaintEngineEx::endNativePainting()
    ritual = 'ritual_ZN14QPaintEngineEx17endNativePaintingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QPaintEngineEx17endNativePaintingEv'
    self.uglySide.call(ritual)

  @staticmethod
  def draw(*__, **_) -> Never:
    """
    Qt's 'void QPaintEngineEx::draw(const QVectorPath &path)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPaintEngineEx.draw' has no cute function yet. Qt's 'void "
        "QPaintEngineEx::draw(const QVectorPath &path)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def fill(*__, **_) -> Never:
    """
    Qt's 'void QPaintEngineEx::fill(const QVectorPath &path, const QBrush
    &brush)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPaintEngineEx.fill' has no cute function yet. Qt's 'void "
        "QPaintEngineEx::fill(const QVectorPath &path, const QBrush "
        "&brush)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def stroke(*__, **_) -> Never:
    """
    Qt's 'void QPaintEngineEx::stroke(const QVectorPath &path, const QPen
    &pen)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPaintEngineEx.stroke' has no cute function yet. Qt's 'void "
        "QPaintEngineEx::stroke(const QVectorPath &path, const QPen &pen)': "
        "takes a type Python has no way to hand over yet.")
