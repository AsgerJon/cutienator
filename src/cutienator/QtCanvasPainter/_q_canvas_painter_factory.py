"""
QCanvasPainterFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvaspainterfactory.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhi
  from . import QCanvasPainter, QCanvasRhiPaintDriver
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhi = WAIT['QRhi']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasPainterFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasPainterFactory: a plain Python object standing
  in front of one C++ QCanvasPainterFactory.

  What exists
  -----------

  Every function of Qt's QCanvasPainterFactory that has a ritual and that
  Python can call so far, 6 names in all: 'sharedInstance', 'isValid',
  'create', 'destroy', 'painter', 'paintDriver'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasPainterFactory::~QCanvasPainterFactory()': the destructor:
    Python never removes a C++ QCanvasPainterFactory.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QCanvasPainterFactory is created at the first use, not by
    'QCanvasPainterFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanvasPainterFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRhi)
  @overload(NoneType)
  def sharedInstance(rhi: Optional[QRhi]) -> Optional[QCanvasPainterFactory]:
    """
    Calls Qt's 'QCanvasPainterFactory
    *QCanvasPainterFactory::sharedInstance(QRhi *rhi)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterfactory.html#sharedInstance

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCanvasPainterFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasPainterFactory *QCanvasPainterFactory::sharedInstance(QRhi
    #      *rhi)
    address = Rituals.call(
        'ritual_ZN21QCanvasPainterFactory14sharedInstanceEP4QRhi',
        CuteMixin._addressOf(rhi),
    )
    return QCanvasPainterFactory._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasPainterFactory'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCanvasPainterFactory::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterfactory.html#isValid
    """
    #  bool QCanvasPainterFactory::isValid() const
    return self.uglySide.call('ritual_ZNK21QCanvasPainterFactory7isValidEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasPainterFactory::QCanvasPainterFactory()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterfactory.html#QCanvasPainterFactory
    """
    #  QCanvasPainterFactory::QCanvasPainterFactory()
    self._noteCreation(QCanvasPainterFactory, lambda: Rituals.call(
        'ritual_ZN21QCanvasPainterFactoryC1Ev',
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

  @overload(QRhi)
  @overload(NoneType)
  def create(self, rhi: Optional[QRhi]) -> Optional[QCanvasPainter]:
    """
    Calls Qt's 'QCanvasPainter *QCanvasPainterFactory::create(QRhi *rhi)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterfactory.html#create

    Parameters
    ----------

    rhi : Optional[QRhi]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QCanvasPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasPainter *QCanvasPainterFactory::create(QRhi *rhi)
    address = self.uglySide.call(
        'ritual_ZN21QCanvasPainterFactory6createEP4QRhi',
        self._addressOf(rhi),
    )
    from . import QCanvasPainter
    return QCanvasPainter._cuteAt(address)

  def destroy(self) -> None:
    """
    Calls Qt's 'void QCanvasPainterFactory::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterfactory.html#destroy
    """
    #  void QCanvasPainterFactory::destroy()
    self.uglySide.call('ritual_ZN21QCanvasPainterFactory7destroyEv')

  def painter(self) -> Optional[QCanvasPainter]:
    """
    Calls Qt's 'QCanvasPainter *QCanvasPainterFactory::painter()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterfactory.html#painter

    Returns
    -------

    Optional[QCanvasPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasPainter *QCanvasPainterFactory::painter()
    address = self.uglySide.call(
        'ritual_ZN21QCanvasPainterFactory7painterEv',
    )
    from . import QCanvasPainter
    return QCanvasPainter._cuteAt(address)

  def paintDriver(self) -> Optional[QCanvasRhiPaintDriver]:
    """
    Calls Qt's 'QCanvasRhiPaintDriver *QCanvasPainterFactory::paintDriver()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterfactory.html#paintDriver

    Returns
    -------

    Optional[QCanvasRhiPaintDriver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasRhiPaintDriver *QCanvasPainterFactory::paintDriver()
    address = self.uglySide.call(
        'ritual_ZN21QCanvasPainterFactory11paintDriverEv',
    )
    from . import QCanvasRhiPaintDriver
    return QCanvasRhiPaintDriver._cuteAt(address)
