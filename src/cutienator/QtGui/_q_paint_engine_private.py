"""
QPaintEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpaintengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QPaintEnginePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from . import QPaintEngine, QRegion, QTextItemInt, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintEngine = WAIT['QPaintEngine']
  QPointF = WAIT['QPointF']
  QRegion = WAIT['QRegion']
  QTextItemInt = WAIT['QTextItemInt']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPaintEnginePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPaintEnginePrivate: a plain Python object standing
  in front of one C++ QPaintEnginePrivate.

  C++ hands a QPaintEnginePrivate around as a copy, so every C++
  QPaintEnginePrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPaintEnginePrivate that has a ritual and that
  Python can call so far, 9 names in all: 'q_func', 'updateSystemClip',
  'setSystemTransform', 'setSystemViewport', 'setSystemTransformAndViewport',
  'systemStateChanged', 'drawBoxTextItem', 'get', 'aggregateEngine'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPaintEngine *QPaintEnginePrivate::q_func() const': takes in
    Python what 'QPaintEngine *QPaintEnginePrivate::q_func()' takes.
  - Qt's 'QPaintEnginePrivate::~QPaintEnginePrivate()': the destructor:
    Python removes its C++ QPaintEnginePrivate by it, and has no other use
    for it.
  - Qt's 'Qt::HANDLE QPaintEnginePrivate::nativeHandle()': gives 'void',
    which has no cute class yet.

  What to expect
  --------------

  - The C++ QPaintEnginePrivate is created at the first use, not by
    'QPaintEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPaintEnginePrivate back gives a copy the ritual made
    for Python, in a new cute QPaintEnginePrivate.
  - Each name of Qt's QPaintEnginePrivate that has no cute function yet,
    'nativeHandle', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPaintEngine)
  @overload(NoneType)
  def get(
      paintEngine: Optional[QPaintEngine],
  ) -> Optional[QPaintEnginePrivate]:
    """
    Calls Qt's 'QPaintEnginePrivate *QPaintEnginePrivate::get(QPaintEngine
    *paintEngine)'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineprivate.html#get

    Parameters
    ----------

    paintEngine : Optional[QPaintEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPaintEnginePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEnginePrivate *QPaintEnginePrivate::get(QPaintEngine
    #      *paintEngine)
    address = Rituals.call(
        'ritual_ZN19QPaintEnginePrivate3getEP12QPaintEngine',
        CuteMixin._addressOf(paintEngine),
    )
    return QPaintEnginePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPaintEnginePrivate'

  #  A C++ QPaintEnginePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPaintEnginePrivate'

  #  The functions Qt calls itself that QPaintEnginePrivate is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'nativeHandle': (
          'Qt::HANDLE QPaintEnginePrivate::nativeHandle()',
      ),
  }

  #  The functions Qt calls itself that QPaintEnginePrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'systemStateChanged': (
          ('_ZN19QPaintEnginePrivate18systemStateChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'aggregateEngine': (
          ('_ZN19QPaintEnginePrivate15aggregateEngineEv',
           ('address', 'address', 'QtGui:QPaintEngine'),
           ()),
      ),
  }

  #  Qt's '~QPaintEnginePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QPaintEnginePrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QPaintEnginePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTransform)
  def setSystemTransform(self, xform: QTransform) -> None:
    """
    Calls Qt's 'void QPaintEnginePrivate::setSystemTransform(const QTransform
    &xform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineprivate.html#setSystemTransform

    Parameters
    ----------

    xform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QPaintEnginePrivate::setSystemTransform(const QTransform &xform)
    self.uglySide.call(
        'ritual_ZN19QPaintEnginePrivate18setSystemTransformERK10QTransform',
        self._valueOf(xform),
    )

  @overload(QRegion)
  def setSystemViewport(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QPaintEnginePrivate::setSystemViewport(const QRegion
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineprivate.html#setSystemViewport

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPaintEnginePrivate::setSystemViewport(const QRegion &region)
    self.uglySide.call(
        'ritual_ZN19QPaintEnginePrivate17setSystemViewportERK7QRegion',
        self._valueOf(region),
    )

  @overload(QTransform, QRegion)
  def setSystemTransformAndViewport(
      self,
      xform: QTransform,
      region: QRegion,
  ) -> None:
    """
    Calls Qt's 'void QPaintEnginePrivate::setSystemTransformAndViewport(const
    QTransform &xform, const QRegion &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineprivate.html

    Parameters
    ----------

    xform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPaintEnginePrivate::setSystemTransformAndViewport(const
    #      QTransform &xform, const QRegion &region)
    self.uglySide.call(
        'ritual_ZN19QPaintEnginePrivate29setSystemTransformAndViewportERK10'
        'QTransformRK7QRegion',
        self._valueOf(xform), self._valueOf(region),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPaintEnginePrivate::QPaintEnginePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineprivate.html#QPaintEnginePrivate
    """
    #  QPaintEnginePrivate::QPaintEnginePrivate()
    self._noteCreation(QPaintEnginePrivate, lambda: Rituals.call(
        'ritual_ZN19QPaintEnginePrivateC1Ev',
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

  def q_func(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QPaintEnginePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpaintengineprivate.html#q_func

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QPaintEnginePrivate::q_func()
    address = self.uglySide.call('ritual_ZN19QPaintEnginePrivate6q_funcEv')
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

  def updateSystemClip(self) -> None:
    """
    Calls Qt's 'void QPaintEnginePrivate::updateSystemClip()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineprivate.html#updateSystemClip
    """
    #  void QPaintEnginePrivate::updateSystemClip()
    self.uglySide.call('ritual_ZN19QPaintEnginePrivate16updateSystemClipEv')

  def systemStateChanged(self) -> None:
    """
    Calls Qt's 'void QPaintEnginePrivate::systemStateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineprivate.html#systemStateChanged
    """
    #  void QPaintEnginePrivate::systemStateChanged()
    ritual = 'ritual_ZN19QPaintEnginePrivate18systemStateChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPaintEnginePrivate18systemStateChangedEv'
    self.uglySide.call(ritual)

  @overload(QPointF, QTextItemInt)
  def drawBoxTextItem(self, p: QPointF, ti: QTextItemInt) -> None:
    """
    Calls Qt's 'void QPaintEnginePrivate::drawBoxTextItem(const QPointF &p,
    const QTextItemInt &ti)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineprivate.html#drawBoxTextItem

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    ti : QTextItemInt
      Passed on as a value: Qt reads the C++ QTextItemInt, which stays
      Python's own.
    """
    #  void QPaintEnginePrivate::drawBoxTextItem(const QPointF &p, const
    #      QTextItemInt &ti)
    self.uglySide.call(
        'ritual_ZN19QPaintEnginePrivate15drawBoxTextItemERK7QPointFRK12QTex'
        'tItemInt',
        self._valueOf(p, 'QPointF'), self._valueOf(ti),
    )

  def aggregateEngine(self) -> Optional[QPaintEngine]:
    """
    Calls Qt's 'QPaintEngine *QPaintEnginePrivate::aggregateEngine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpaintengineprivate.html#aggregateEngine

    Returns
    -------

    Optional[QPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintEngine *QPaintEnginePrivate::aggregateEngine()
    ritual = 'ritual_ZN19QPaintEnginePrivate15aggregateEngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPaintEnginePrivate15aggregateEngineEv'
    address = self.uglySide.call(ritual)
    from . import QPaintEngine
    return QPaintEngine._cuteAt(address)

  @staticmethod
  def nativeHandle(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QPaintEnginePrivate::nativeHandle()': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPaintEnginePrivate.nativeHandle' has no cute function yet. Qt's "
        "'Qt::HANDLE QPaintEnginePrivate::nativeHandle()': gives 'void', "
        "which has no cute class yet.")
