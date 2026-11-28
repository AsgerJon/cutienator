"""
QAlphaPaintEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_alpha_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QAlphaPaintEnginePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QPaintEnginePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QPainter, QPainterPath
  from . import QAlphaPaintEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPainterPath = WAIT['QPainterPath']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAlphaPaintEnginePrivate(QPaintEnginePrivate):
  """
  The cute side of Qt's QAlphaPaintEnginePrivate: a plain Python object
  standing in front of one C++ QAlphaPaintEnginePrivate.

  It is built on the cute 'QPaintEnginePrivate', as Qt's
  QAlphaPaintEnginePrivate is built on Qt's QPaintEnginePrivate, and has
  everything that class has.

  C++ hands a QAlphaPaintEnginePrivate around as a copy, so every C++
  QAlphaPaintEnginePrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QAlphaPaintEnginePrivate that has a ritual and that
  Python can call so far, 8 names in all: 'q_func', 'addAlphaRect',
  'addDirtyRect', 'canSeeTroughBackground', 'addPenWidth', 'drawAlphaImage',
  'fullyContained', 'resetState'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAlphaPaintEngine *QAlphaPaintEnginePrivate::q_func() const':
    takes in Python what 'QAlphaPaintEngine
    *QAlphaPaintEnginePrivate::q_func()' takes.
  - Qt's 'QAlphaPaintEnginePrivate::~QAlphaPaintEnginePrivate()': the
    destructor: Python removes its C++ QAlphaPaintEnginePrivate by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 12 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QAlphaPaintEnginePrivate is created at the first use, not by
    'QAlphaPaintEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAlphaPaintEnginePrivate back gives a copy the ritual
    made for Python, in a new cute QAlphaPaintEnginePrivate.
  - Each name of Qt's QAlphaPaintEnginePrivate that has no cute function yet,
    'toRect', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAlphaPaintEnginePrivate'

  #  A C++ QAlphaPaintEnginePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAlphaPaintEnginePrivate'

  #  Qt's '~QAlphaPaintEnginePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QAlphaPaintEnginePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QAlphaPaintEnginePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool, QRectF)
  def canSeeTroughBackground(
      self,
      somethingInRectHasAlpha: bool,
      rect: QRectF,
  ) -> bool:
    """
    Calls Qt's 'bool QAlphaPaintEnginePrivate::canSeeTroughBackground(bool
    somethingInRectHasAlpha, const QRectF &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengineprivate.html

    Parameters
    ----------

    somethingInRectHasAlpha : bool
      Passed on as it is.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QAlphaPaintEnginePrivate::canSeeTroughBackground(bool
    #      somethingInRectHasAlpha, const QRectF &rect) const
    return self.uglySide.call(
        'ritual_ZNK24QAlphaPaintEnginePrivate22canSeeTroughBackgroundEbRK6Q'
        'RectF',
        somethingInRectHasAlpha, self._valueOf(rect),
    )

  @overload(QRectF)
  def fullyContained(self, rect: QRectF) -> bool:
    """
    Calls Qt's 'bool QAlphaPaintEnginePrivate::fullyContained(const QRectF
    &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengineprivate.html#fullyContained

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QAlphaPaintEnginePrivate::fullyContained(const QRectF &rect)
    #      const
    return self.uglySide.call(
        'ritual_ZNK24QAlphaPaintEnginePrivate14fullyContainedERK6QRectF',
        self._valueOf(rect),
    )

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
    'QAlphaPaintEnginePrivate::QAlphaPaintEnginePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengineprivate.html
    """
    #  QAlphaPaintEnginePrivate::QAlphaPaintEnginePrivate()
    self._noteCreation(QAlphaPaintEnginePrivate, lambda: Rituals.call(
        'ritual_ZN24QAlphaPaintEnginePrivateC1Ev',
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

  def q_func(self) -> Optional[QAlphaPaintEngine]:
    """
    Calls Qt's 'QAlphaPaintEngine *QAlphaPaintEnginePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengineprivate.html#q_func

    Returns
    -------

    Optional[QAlphaPaintEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAlphaPaintEngine *QAlphaPaintEnginePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QAlphaPaintEnginePrivate6q_funcEv',
    )
    from . import QAlphaPaintEngine
    return QAlphaPaintEngine._cuteAt(address)

  @overload(QRectF)
  def addAlphaRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QAlphaPaintEnginePrivate::addAlphaRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengineprivate.html#addAlphaRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QAlphaPaintEnginePrivate::addAlphaRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN24QAlphaPaintEnginePrivate12addAlphaRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QRectF)
  def addDirtyRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QAlphaPaintEnginePrivate::addDirtyRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengineprivate.html#addDirtyRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QAlphaPaintEnginePrivate::addDirtyRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN24QAlphaPaintEnginePrivate12addDirtyRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QPainterPath)
  def addPenWidth(self, path: QPainterPath) -> QRectF:
    """
    Calls Qt's 'QRectF QAlphaPaintEnginePrivate::addPenWidth(const
    QPainterPath &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengineprivate.html#addPenWidth

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QAlphaPaintEnginePrivate::addPenWidth(const QPainterPath &path)
    address = self.uglySide.call(
        'ritual_ZN24QAlphaPaintEnginePrivate11addPenWidthERK12QPainterPath',
        self._valueOf(path),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def drawAlphaImage(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QAlphaPaintEnginePrivate::drawAlphaImage(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengineprivate.html#drawAlphaImage

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QAlphaPaintEnginePrivate::drawAlphaImage(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN24QAlphaPaintEnginePrivate14drawAlphaImageERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QPainter)
  @overload(NoneType)
  def resetState(self, p: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QAlphaPaintEnginePrivate::resetState(QPainter *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qalphapaintengineprivate.html#resetState

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAlphaPaintEnginePrivate::resetState(QPainter *p)
    self.uglySide.call(
        'ritual_ZN24QAlphaPaintEnginePrivate10resetStateEP8QPainter',
        self._addressOf(p),
    )

  @staticmethod
  def toRect(*__, **_) -> Never:
    """
    Qt's 'QRect QAlphaPaintEnginePrivate::toRect(const QRectF &rect) const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QAlphaPaintEnginePrivate.toRect' has no cute function yet. Qt's "
        "'QRect QAlphaPaintEnginePrivate::toRect(const QRectF &rect) "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
