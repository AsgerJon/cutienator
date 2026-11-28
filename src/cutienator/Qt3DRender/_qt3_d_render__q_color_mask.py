"""
Qt3DRender::QColorMask binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qcolormask.h, Qt 6.12.0. Changes made here are lost.
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


class QColorMask(Qt3DRender.QRenderState):
  """
  The cute side of Qt's Qt3DRender::QColorMask: a plain Python object
  standing in front of one C++ Qt3DRender::QColorMask.

  It is built on the cute 'Qt3DRender::QRenderState', as Qt's
  Qt3DRender::QColorMask is built on Qt's Qt3DRender::QRenderState, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QColorMask that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'isRedMasked',
  'isGreenMasked', 'isBlueMasked', 'isAlphaMasked', 'setRedMasked',
  'setGreenMasked', 'setBlueMasked', 'setAlphaMasked', 'redMaskedChanged',
  'greenMaskedChanged', 'blueMaskedChanged', 'alphaMaskedChanged', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QColorMask::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QColorMask::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QColorMask::~QColorMask()': the destructor: Python
    never removes a C++ Qt3DRender::QColorMask.
  - Qt's 'const QColorMaskPrivate *Qt3DRender::QColorMask::d_func() const':
    takes in Python what 'QColorMaskPrivate
    *Qt3DRender::QColorMask::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QColorMask is created at the first use, not by
    'Qt3DRender::QColorMask(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QColorMask.
  - Qt tells when it has removed the C++ Qt3DRender::QColorMask. Every call
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
    Calls Qt's 'QString Qt3DRender::QColorMask::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcolormask.html#tr

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
    #  QString Qt3DRender::QColorMask::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10QColorMask2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QColorMask'

  #  A C++ Qt3DRender::QColorMask Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QColorMask'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QColorMask::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QColorMask::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QColorMask10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRedMasked(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QColorMask::isRedMasked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#isRedMasked
    """
    #  bool Qt3DRender::QColorMask::isRedMasked() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QColorMask11isRedMaskedEv',
    )

  def isGreenMasked(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QColorMask::isGreenMasked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#isGreenMasked
    """
    #  bool Qt3DRender::QColorMask::isGreenMasked() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QColorMask13isGreenMaskedEv',
    )

  def isBlueMasked(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QColorMask::isBlueMasked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#isBlueMasked
    """
    #  bool Qt3DRender::QColorMask::isBlueMasked() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QColorMask12isBlueMaskedEv',
    )

  def isAlphaMasked(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QColorMask::isAlphaMasked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#isAlphaMasked
    """
    #  bool Qt3DRender::QColorMask::isAlphaMasked() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QColorMask13isAlphaMaskedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRedMasked(self, redMasked: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QColorMask::setRedMasked(bool redMasked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#setRedMasked

    Parameters
    ----------

    redMasked : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QColorMask::setRedMasked(bool redMasked)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QColorMask12setRedMaskedEb', redMasked,
    )

  @overload(bool)
  def setGreenMasked(self, greenMasked: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QColorMask::setGreenMasked(bool
    greenMasked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#setGreenMasked

    Parameters
    ----------

    greenMasked : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QColorMask::setGreenMasked(bool greenMasked)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QColorMask14setGreenMaskedEb', greenMasked,
    )

  @overload(bool)
  def setBlueMasked(self, blueMasked: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QColorMask::setBlueMasked(bool blueMasked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#setBlueMasked

    Parameters
    ----------

    blueMasked : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QColorMask::setBlueMasked(bool blueMasked)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QColorMask13setBlueMaskedEb', blueMasked,
    )

  @overload(bool)
  def setAlphaMasked(self, alphaMasked: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QColorMask::setAlphaMasked(bool
    alphaMasked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#setAlphaMasked

    Parameters
    ----------

    alphaMasked : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QColorMask::setAlphaMasked(bool alphaMasked)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QColorMask14setAlphaMaskedEb', alphaMasked,
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
    'Qt3DRender::QColorMask::QColorMask(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#QColorMask

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QColorMask::QColorMask(Qt3DCore::QNode *parent)
    self._noteCreation(QColorMask, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QColorMaskC1EPN8Qt3DCore5QNodeE',
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

  @overload(bool)
  def redMaskedChanged(self, redMasked: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QColorMask::redMaskedChanged(bool
    redMasked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#redMaskedChanged

    Parameters
    ----------

    redMasked : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QColorMask::redMaskedChanged(bool redMasked)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QColorMask16redMaskedChangedEb', redMasked,
    )

  @overload(bool)
  def greenMaskedChanged(self, greenMasked: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QColorMask::greenMaskedChanged(bool
    greenMasked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#greenMaskedChanged

    Parameters
    ----------

    greenMasked : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QColorMask::greenMaskedChanged(bool greenMasked)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QColorMask18greenMaskedChangedEb',
        greenMasked,
    )

  @overload(bool)
  def blueMaskedChanged(self, blueMasked: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QColorMask::blueMaskedChanged(bool
    blueMasked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#blueMaskedChanged

    Parameters
    ----------

    blueMasked : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QColorMask::blueMaskedChanged(bool blueMasked)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QColorMask17blueMaskedChangedEb', blueMasked,
    )

  @overload(bool)
  def alphaMaskedChanged(self, alphaMasked: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QColorMask::alphaMaskedChanged(bool
    alphaMasked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcolormask.html#alphaMaskedChanged

    Parameters
    ----------

    alphaMasked : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QColorMask::alphaMaskedChanged(bool alphaMasked)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QColorMask18alphaMaskedChangedEb',
        alphaMasked,
    )

  def d_func(self) -> Optional[Qt3DRender.QColorMaskPrivate]:
    """
    Calls Qt's 'QColorMaskPrivate *Qt3DRender::QColorMask::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcolormask.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QColorMaskPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QColorMaskPrivate *Qt3DRender::QColorMask::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10QColorMask6d_funcEv',
    )
    return Qt3DRender.QColorMaskPrivate._cuteAt(address)
