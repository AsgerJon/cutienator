"""
Qt3DRender::QDepthRange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qdepthrange.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDepthRange(Qt3DRender.QRenderState):
  """
  The cute side of Qt's Qt3DRender::QDepthRange: a plain Python object
  standing in front of one C++ Qt3DRender::QDepthRange.

  It is built on the cute 'Qt3DRender::QRenderState', as Qt's
  Qt3DRender::QDepthRange is built on Qt's Qt3DRender::QRenderState, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QDepthRange that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'nearValue',
  'farValue', 'setNearValue', 'setFarValue', 'nearValueChanged',
  'farValueChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QDepthRange::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QDepthRange::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QDepthRange::~QDepthRange()': the destructor: Python
    never removes a C++ Qt3DRender::QDepthRange.
  - Qt's 'const QDepthRangePrivate *Qt3DRender::QDepthRange::d_func() const':
    takes in Python what 'QDepthRangePrivate
    *Qt3DRender::QDepthRange::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QDepthRange is created at the first use, not by
    'Qt3DRender::QDepthRange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QDepthRange.
  - Qt tells when it has removed the C++ Qt3DRender::QDepthRange. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DRender::QDepthRange::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qdepthrange.html#tr

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
    #  QString Qt3DRender::QDepthRange::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender11QDepthRange2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QDepthRange'

  #  A C++ Qt3DRender::QDepthRange Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QDepthRange'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QDepthRange::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthrange.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QDepthRange::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QDepthRange10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def nearValue(self) -> float:
    """
    Calls Qt's 'double Qt3DRender::QDepthRange::nearValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthrange.html#nearValue
    """
    #  double Qt3DRender::QDepthRange::nearValue() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QDepthRange9nearValueEv',
    )

  def farValue(self) -> float:
    """
    Calls Qt's 'double Qt3DRender::QDepthRange::farValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthrange.html#farValue
    """
    #  double Qt3DRender::QDepthRange::farValue() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender11QDepthRange8farValueEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setNearValue(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDepthRange::setNearValue(double value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthrange.html#setNearValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DRender::QDepthRange::setNearValue(double value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QDepthRange12setNearValueEd', value,
    )

  @overload(float)
  def setFarValue(self, value: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDepthRange::setFarValue(double value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthrange.html#setFarValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void Qt3DRender::QDepthRange::setFarValue(double value)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QDepthRange11setFarValueEd', value,
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QDepthRange::QDepthRange(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthrange.html#QDepthRange

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QDepthRange::QDepthRange(Qt3DCore::QNode *parent)
    self._noteCreation(QDepthRange, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender11QDepthRangeC1EPN8Qt3DCore5QNodeE',
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

  @overload(float)
  def nearValueChanged(self, nearValue: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDepthRange::nearValueChanged(double
    nearValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthrange.html#nearValueChanged

    Parameters
    ----------

    nearValue : float
      Passed on as it is.
    """
    #  void Qt3DRender::QDepthRange::nearValueChanged(double nearValue)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QDepthRange16nearValueChangedEd', nearValue,
    )

  @overload(float)
  def farValueChanged(self, farValue: float) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDepthRange::farValueChanged(double
    farValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdepthrange.html#farValueChanged

    Parameters
    ----------

    farValue : float
      Passed on as it is.
    """
    #  void Qt3DRender::QDepthRange::farValueChanged(double farValue)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender11QDepthRange15farValueChangedEd', farValue,
    )

  def d_func(self) -> Optional[Qt3DRender.QDepthRangePrivate]:
    """
    Calls Qt's 'QDepthRangePrivate *Qt3DRender::QDepthRange::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qdepthrange.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QDepthRangePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDepthRangePrivate *Qt3DRender::QDepthRange::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender11QDepthRange6d_funcEv',
    )
    return Qt3DRender.QDepthRangePrivate._cuteAt(address)
