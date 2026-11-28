"""
Qt3DRender::QViewport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qviewport.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QViewport(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QViewport: a plain Python object standing
  in front of one C++ Qt3DRender::QViewport.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QViewport is built on Qt's Qt3DRender::QFrameGraphNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QViewport that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr',
  'normalizedRect', 'gamma', 'setNormalizedRect', 'setGamma',
  'normalizedRectChanged', 'gammaChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QViewport::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QViewport::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QViewport::~QViewport()': the destructor: Python never
    removes a C++ Qt3DRender::QViewport.
  - Qt's 'Qt3DRender::QViewport::QViewport(QViewportPrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QViewportPrivate *Qt3DRender::QViewport::d_func() const':
    takes in Python what 'QViewportPrivate *Qt3DRender::QViewport::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QViewport is created at the first use, not by
    'Qt3DRender::QViewport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QViewport.
  - Qt tells when it has removed the C++ Qt3DRender::QViewport. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DRender::QViewport::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qviewport.html#tr

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
    #  QString Qt3DRender::QViewport::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender9QViewport2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QViewport'

  #  A C++ Qt3DRender::QViewport Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QViewport'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QViewport::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qviewport.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QViewport::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender9QViewport10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def normalizedRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF Qt3DRender::QViewport::normalizedRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qviewport.html#normalizedRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF Qt3DRender::QViewport::normalizedRect() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender9QViewport14normalizedRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def gamma(self) -> float:
    """
    Calls Qt's 'float Qt3DRender::QViewport::gamma() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qviewport.html#gamma
    """
    #  float Qt3DRender::QViewport::gamma() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender9QViewport5gammaEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setNormalizedRect(self, normalizedRect: QRectF) -> None:
    """
    Calls Qt's 'void Qt3DRender::QViewport::setNormalizedRect(const QRectF
    &normalizedRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qviewport.html#setNormalizedRect

    Parameters
    ----------

    normalizedRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void Qt3DRender::QViewport::setNormalizedRect(const QRectF
    #      &normalizedRect)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QViewport17setNormalizedRectERK6QRectF',
        self._valueOf(normalizedRect),
    )

  @overload(float)
  def setGamma(self, gamma: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QViewport::setGamma(float gamma)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qviewport.html#setGamma

    Parameters
    ----------

    gamma : float
      Passed on as it is.
    """
    #  void Qt3DRender::QViewport::setGamma(float gamma)
    self.uglySide.call('ritual_ZN10Qt3DRender9QViewport8setGammaEf', gamma)

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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QViewport::QViewport(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qviewport.html#QViewport

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QViewport::QViewport(Qt3DCore::QNode *parent)
    self._noteCreation(QViewport, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender9QViewportC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(QRectF)
  def normalizedRectChanged(self, normalizedRect: QRectF) -> None:
    """
    Calls Qt's 'void Qt3DRender::QViewport::normalizedRectChanged(const
    QRectF &normalizedRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qviewport.html#normalizedRectChanged

    Parameters
    ----------

    normalizedRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void Qt3DRender::QViewport::normalizedRectChanged(const QRectF
    #      &normalizedRect)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QViewport21normalizedRectChangedERK6QRectF',
        self._valueOf(normalizedRect),
    )

  @overload(float)
  def gammaChanged(self, gamma: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QViewport::gammaChanged(float gamma)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qviewport.html#gammaChanged

    Parameters
    ----------

    gamma : float
      Passed on as it is.
    """
    #  void Qt3DRender::QViewport::gammaChanged(float gamma)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QViewport12gammaChangedEf', gamma,
    )

  def d_func(self) -> Optional[Qt3DRender.QViewportPrivate]:
    """
    Calls Qt's 'QViewportPrivate *Qt3DRender::QViewport::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qviewport.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QViewportPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QViewportPrivate *Qt3DRender::QViewport::d_func()
    address = self.uglySide.call('ritual_ZN10Qt3DRender9QViewport6d_funcEv')
    return Qt3DRender.QViewportPrivate._cuteAt(address)
