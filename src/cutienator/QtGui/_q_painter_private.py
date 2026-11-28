"""
QPainterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpainter_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPainterPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QPaintDevice, QPaintEngine, QPainter, QPainterDummyState
  from . import QPainterPath, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintDevice = WAIT['QPaintDevice']
  QPainter = WAIT['QPainter']
  QPainterPath = WAIT['QPainterPath']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPainterPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPainterPrivate: a plain Python object standing in
  front of one C++ QPainterPrivate.

  What exists
  -----------

  Every function of Qt's QPainterPrivate that has a ritual and that Python
  can call so far, 12 names in all: 'q_func', 'fakeState',
  'drawOpaqueBackground', 'updateMatrix', 'updateInvMatrix', 'get',
  'viewTransform', 'effectiveDevicePixelRatio', 'hidpiScaleTransform',
  'attachPainterPrivate', 'detachPainterPrivate', 'initFrom'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPainter *QPainterPrivate::q_func() const': takes in Python
    what 'QPainter *QPainterPrivate::q_func()' takes.
  - Qt's 'QPainterPrivate::~QPainterPrivate()': the destructor: Python never
    removes a C++ QPainterPrivate.
  - Qt's 'void QPainterPrivate::setEngineDirtyFlags(QSpan<const
    QPaintEngine::DirtyFlags> a0)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  9 of the 25 functions Qt declares: 5 leans on 'QPainterPrivate; 4 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file.

  What to expect
  --------------

  - The C++ QPainterPrivate is created at the first use, not by
    'QPainterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPainterPrivate.
  - Each name of Qt's QPainterPrivate that has no cute function yet,
    'checkEmulation', 'drawGlyphs', 'drawStretchedGradient', 'drawTextItem',
    'draw_helper', 'setEngineDirtyFlags', 'updateEmulationSpecifier',
    'updateState', 'updateStateImpl', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPainterPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DrawOperation(CuteNum):
    """
    The enum 'QPainterPrivate::DrawOperation' of Qt, with the 3 names Qt
    gives in it.
    """

    StrokeDraw = Kee[int](1)
    FillDraw = Kee[int](2)
    StrokeAndFillDraw = Kee[int](3)

  #  The classes Qt writes inside QPainterPrivate, each a class in here as in
  #  C++.

  class QPaintEngineDestructor(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QPainterPrivate::QPaintEngineDestructor: a plain
    Python object standing in front of one C++
    QPainterPrivate::QPaintEngineDestructor.

    C++ hands a QPainterPrivate::QPaintEngineDestructor around as a copy, so
    every C++ QPainterPrivate::QPaintEngineDestructor behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QPainterPrivate::QPaintEngineDestructor that has a
    ritual and that Python can call so far, 1 name in all: '__call__'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QPainterPrivate::QPaintEngineDestructor::~QPaintEngineDestructor()':
      the destructor: Python removes its C++
      QPainterPrivate::QPaintEngineDestructor by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QPainterPrivate::QPaintEngineDestructor is created at the first
      use, not by 'QPainterPrivate::QPaintEngineDestructor(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QPainterPrivate::QPaintEngineDestructor back gives
      a copy the ritual made for Python, in a new cute
      QPainterPrivate::QPaintEngineDestructor.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPaintEngine = WAIT['QPaintEngine']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QPainterPrivate::QPaintEngineDestructor'

    #  Qt's '~QPainterPrivate::QPaintEngineDestructor()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QPainterPrivate::QPaintEngineDestructor behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN15QPainterPrivate22QPaintEngineDestructorD1Ev')

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

    @overload(QPaintEngine)
    @overload(NoneType)
    def __call__(self, pe: Optional[QPaintEngine]) -> None:
      """
      Calls Qt's 'void
      QPainterPrivate::QPaintEngineDestructor::operator()(QPaintEngine *pe)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qpainterprivate-qpaintenginedestructor.html

      Parameters
      ----------

      pe : Optional[QPaintEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void
      #      QPainterPrivate::QPaintEngineDestructor::operator()(QPaintEngine
      #      *pe) const
      self.uglySide.call(
          'ritual_ZNK15QPainterPrivate22QPaintEngineDestructorclEP12QPaintE'
          'ngine',
          self._addressOf(pe),
      )

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
  @overload(QPainter)
  @overload(NoneType)
  def get(painter: Optional[QPainter]) -> Optional[QPainterPrivate]:
    """
    Calls Qt's 'QPainterPrivate *QPainterPrivate::get(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterprivate.html#get

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPainterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainterPrivate *QPainterPrivate::get(QPainter *painter)
    address = Rituals.call(
        'ritual_ZN15QPainterPrivate3getEP8QPainter',
        CuteMixin._addressOf(painter),
    )
    return QPainterPrivate._cuteAt(address)

  @staticmethod
  @overload(QPainter, QPaintDevice)
  @overload(QPainter, NoneType)
  @overload(NoneType, QPaintDevice)
  @overload(NoneType, NoneType)
  def attachPainterPrivate(
      q: Optional[QPainter],
      pdev: Optional[QPaintDevice],
  ) -> bool:
    """
    Calls Qt's 'bool QPainterPrivate::attachPainterPrivate(QPainter *q,
    QPaintDevice *pdev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterprivate.html#attachPainterPrivate

    Parameters
    ----------

    q : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pdev : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPainterPrivate::attachPainterPrivate(QPainter *q, QPaintDevice
    #      *pdev)
    return Rituals.call(
        'ritual_ZN15QPainterPrivate20attachPainterPrivateEP8QPainterP12QPai'
        'ntDevice',
        CuteMixin._addressOf(q), CuteMixin._addressOf(pdev, 'QPaintDevice'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPainterPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fakeState(self) -> Optional[QPainterDummyState]:
    """
    Calls Qt's 'QPainterDummyState *QPainterPrivate::fakeState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterprivate.html#fakeState

    Returns
    -------

    Optional[QPainterDummyState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainterDummyState *QPainterPrivate::fakeState() const
    address = self.uglySide.call('ritual_ZNK15QPainterPrivate9fakeStateEv')
    from . import QPainterDummyState
    return QPainterDummyState._cuteAt(address)

  def viewTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QPainterPrivate::viewTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterprivate.html#viewTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QPainterPrivate::viewTransform() const
    address = self.uglySide.call(
        'ritual_ZNK15QPainterPrivate13viewTransformEv',
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

  def effectiveDevicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal QPainterPrivate::effectiveDevicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterprivate.html#effectiveDevicePixelRatio
    """
    #  qreal QPainterPrivate::effectiveDevicePixelRatio() const
    return self.uglySide.call(
        'ritual_ZNK15QPainterPrivate25effectiveDevicePixelRatioEv',
    )

  def hidpiScaleTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QPainterPrivate::hidpiScaleTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterprivate.html#hidpiScaleTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QPainterPrivate::hidpiScaleTransform() const
    address = self.uglySide.call(
        'ritual_ZNK15QPainterPrivate19hidpiScaleTransformEv',
    )
    from . import QTransform
    return QTransform._cuteOwning(address)

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

  @overload(QPainter)
  @overload(NoneType)
  def __init__(self, painter: Optional[QPainter]) -> None:
    """
    Notes what was given, for Qt's 'QPainterPrivate::QPainterPrivate(QPainter
    *painter)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterprivate.html#QPainterPrivate

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPainterPrivate::QPainterPrivate(QPainter *painter)
    self._noteCreation(QPainterPrivate, lambda: Rituals.call(
        'ritual_ZN15QPainterPrivateC1EP8QPainter', self._addressOf(painter),
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

  def q_func(self) -> Optional[QPainter]:
    """
    Calls Qt's 'QPainter *QPainterPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterprivate.html#q_func

    Returns
    -------

    Optional[QPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPainter *QPainterPrivate::q_func()
    address = self.uglySide.call('ritual_ZN15QPainterPrivate6q_funcEv')
    from . import QPainter
    return QPainter._cuteAt(address)

  @overload(QPainterPath, DrawOperation)
  def drawOpaqueBackground(
      self,
      path: QPainterPath,
      operation: DrawOperation,
  ) -> None:
    """
    Calls Qt's 'void QPainterPrivate::drawOpaqueBackground(const QPainterPath
    &path, DrawOperation operation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterprivate.html#drawOpaqueBackground

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    operation : DrawOperation
      Passed on as its number.
    """
    #  void QPainterPrivate::drawOpaqueBackground(const QPainterPath &path,
    #      DrawOperation operation)
    self.uglySide.call(
        'ritual_ZN15QPainterPrivate20drawOpaqueBackgroundERK12QPainterPathN'
        'S_13DrawOperationE',
        self._valueOf(path), operation.value,
    )

  def updateMatrix(self) -> None:
    """
    Calls Qt's 'void QPainterPrivate::updateMatrix()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterprivate.html#updateMatrix
    """
    #  void QPainterPrivate::updateMatrix()
    self.uglySide.call('ritual_ZN15QPainterPrivate12updateMatrixEv')

  def updateInvMatrix(self) -> None:
    """
    Calls Qt's 'void QPainterPrivate::updateInvMatrix()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterprivate.html#updateInvMatrix
    """
    #  void QPainterPrivate::updateInvMatrix()
    self.uglySide.call('ritual_ZN15QPainterPrivate15updateInvMatrixEv')

  @overload(QPainter)
  @overload(NoneType)
  def detachPainterPrivate(self, q: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QPainterPrivate::detachPainterPrivate(QPainter *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterprivate.html#detachPainterPrivate

    Parameters
    ----------

    q : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPainterPrivate::detachPainterPrivate(QPainter *q)
    self.uglySide.call(
        'ritual_ZN15QPainterPrivate20detachPainterPrivateEP8QPainter',
        self._addressOf(q),
    )

  @overload(QPaintDevice)
  @overload(NoneType)
  def initFrom(self, device: Optional[QPaintDevice]) -> None:
    """
    Calls Qt's 'void QPainterPrivate::initFrom(const QPaintDevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterprivate.html#initFrom

    Parameters
    ----------

    device : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPainterPrivate::initFrom(const QPaintDevice *device)
    self.uglySide.call(
        'ritual_ZN15QPainterPrivate8initFromEPK12QPaintDevice',
        self._addressOf(device, 'QPaintDevice'),
    )

  @staticmethod
  def checkEmulation(*__, **_) -> Never:
    """
    Qt's 'void QPainterPrivate::checkEmulation()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'needsEmulation'.
    """
    raise NotImplementedError(
        "'QPainterPrivate.checkEmulation' has no cute function yet. Qt's "
        "'void QPainterPrivate::checkEmulation()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'needsEmulation'.")

  @staticmethod
  def drawGlyphs(*__, **_) -> Never:
    """
    Qt's 'void QPainterPrivate::drawGlyphs(const QPointF &decorationPosition,
    const quint32 *glyphArray, QFixedPoint *positionArray, int glyphCount,
    QFontEngine *fontEngine, bool overline, bool underline, bool strikeOut)':
    leans on 'QPainterPrivate::updateEmulationSpecifier(QPainterState*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QPainterPrivate.drawGlyphs' has no cute function yet. Qt's 'void "
        "QPainterPrivate::drawGlyphs(const QPointF &decorationPosition, "
        "const quint32 *glyphArray, QFixedPoint *positionArray, int "
        "glyphCount, QFontEngine *fontEngine, bool overline, bool "
        "underline, bool strikeOut)': leans on "
        "'QPainterPrivate::updateEmulationSpecifier(QPainterState*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def drawStretchedGradient(*__, **_) -> Never:
    """
    Qt's 'void QPainterPrivate::drawStretchedGradient(const QPainterPath
    &path, DrawOperation operation)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'coordinateMode'.
    """
    raise NotImplementedError(
        "'QPainterPrivate.drawStretchedGradient' has no cute function yet. "
        "Qt's 'void QPainterPrivate::drawStretchedGradient(const "
        "QPainterPath &path, DrawOperation operation)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'coordinateMode'.")

  @staticmethod
  def drawTextItem(*__, **_) -> Never:
    """
    Qt's 'void QPainterPrivate::drawTextItem(const QPointF &p, const
    QTextItem &_ti, QTextEngine *textEngine)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'drawTextItemDecoration'.
    """
    raise NotImplementedError(
        "'QPainterPrivate.drawTextItem' has no cute function yet. Qt's "
        "'void QPainterPrivate::drawTextItem(const QPointF &p, const "
        "QTextItem &_ti, QTextEngine *textEngine)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'drawTextItemDecoration'.")

  @staticmethod
  def draw_helper(*__, **_) -> Never:
    """
    Qt's 'void QPainterPrivate::draw_helper(const QPainterPath &path,
    DrawOperation operation)': leans on
    'QPainterPrivate::drawStretchedGradient(QPainterPath const&,
    QPainterPrivate::DrawOperation)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QPainterPrivate.draw_helper' has no cute function yet. Qt's 'void "
        "QPainterPrivate::draw_helper(const QPainterPath &path, "
        "DrawOperation operation)': leans on "
        "'QPainterPrivate::drawStretchedGradient(QPainterPath const&, "
        "QPainterPrivate::DrawOperation)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setEngineDirtyFlags(*__, **_) -> Never:
    """
    Qt's 'void QPainterPrivate::setEngineDirtyFlags(QSpan<const
    QPaintEngine::DirtyFlags> a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QPainterPrivate.setEngineDirtyFlags' has no cute function yet. "
        "Qt's 'void QPainterPrivate::setEngineDirtyFlags(QSpan<const "
        "QPaintEngine::DirtyFlags> a0)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def updateEmulationSpecifier(*__, **_) -> Never:
    """
    Qt's 'void QPainterPrivate::updateEmulationSpecifier(QPainterState *s)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'qt_isExtendedRadialGradient'.
    """
    raise NotImplementedError(
        "'QPainterPrivate.updateEmulationSpecifier' has no cute function "
        "yet. Qt's 'void "
        "QPainterPrivate::updateEmulationSpecifier(QPainterState *s)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qt_isExtendedRadialGradient'.")

  @staticmethod
  def updateState(*__, **_) -> Never:
    """
    - Qt's 'void QPainterPrivate::updateState(QPainterState *state)': leans
      on 'QPainterPrivate::updateEmulationSpecifier(QPainterState*)', which
      Qt's source does not mark for use from outside Qt and has no code for
      that could be taken.
    - Qt's 'void QPainterPrivate::updateState(std::unique_ptr<QPainterState>
      &state)': leans on
      'QPainterPrivate::updateEmulationSpecifier(QPainterState*)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QPainterPrivate.updateState' has no cute function yet. Qt's 'void "
        "QPainterPrivate::updateState(QPainterState *state)': leans on "
        "'QPainterPrivate::updateEmulationSpecifier(QPainterState*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's 'void "
        "QPainterPrivate::updateState(std::unique_ptr<QPainterState> "
        "&state)': leans on "
        "'QPainterPrivate::updateEmulationSpecifier(QPainterState*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def updateStateImpl(*__, **_) -> Never:
    """
    Qt's 'void QPainterPrivate::updateStateImpl(QPainterState *state)': leans
    on 'QPainterPrivate::updateEmulationSpecifier(QPainterState*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QPainterPrivate.updateStateImpl' has no cute function yet. Qt's "
        "'void QPainterPrivate::updateStateImpl(QPainterState *state)': "
        "leans on "
        "'QPainterPrivate::updateEmulationSpecifier(QPainterState*)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
