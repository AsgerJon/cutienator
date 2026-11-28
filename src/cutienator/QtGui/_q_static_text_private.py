"""
QStaticTextPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qstatictext_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QStaticTextPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from . import QColor, QPainter, QStaticText
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainter = WAIT['QPainter']
  QPointF = WAIT['QPointF']
  QStaticText = WAIT['QStaticText']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStaticTextPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStaticTextPrivate: a plain Python object standing in
  front of one C++ QStaticTextPrivate.

  C++ hands a QStaticTextPrivate around as a copy, so every C++
  QStaticTextPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStaticTextPrivate that has a ritual and that Python
  can call so far, 3 names in all: 'paintText', 'invalidate', 'get'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStaticTextPrivate::~QStaticTextPrivate()': the destructor: Python
    removes its C++ QStaticTextPrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QStaticTextPrivate is created at the first use, not by
    'QStaticTextPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStaticTextPrivate back gives a copy the ritual made
    for Python, in a new cute QStaticTextPrivate.
  - Each name of Qt's QStaticTextPrivate that has no cute function yet,
    'init', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QStaticText)
  @overload(NoneType)
  def get(q: Optional[QStaticText]) -> Optional[QStaticTextPrivate]:
    """
    Calls Qt's 'QStaticTextPrivate *QStaticTextPrivate::get(const QStaticText
    *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictextprivate.html#get

    Parameters
    ----------

    q : Optional[QStaticText]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QStaticTextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStaticTextPrivate *QStaticTextPrivate::get(const QStaticText *q)
    address = Rituals.call(
        'ritual_ZN18QStaticTextPrivate3getEPK11QStaticText',
        CuteMixin._addressOf(q),
    )
    return QStaticTextPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStaticTextPrivate'

  #  Qt's '~QStaticTextPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QStaticTextPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QStaticTextPrivateD1Ev'

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
    'QStaticTextPrivate::QStaticTextPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatictextprivate.html#QStaticTextPrivate
    """
    #  QStaticTextPrivate::QStaticTextPrivate()
    self._noteCreation(QStaticTextPrivate, lambda: Rituals.call(
        'ritual_ZN18QStaticTextPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QStaticTextPrivate) -> None:
    """
    Notes what was given, for Qt's
    'QStaticTextPrivate::QStaticTextPrivate(const QStaticTextPrivate
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatictextprivate.html#QStaticTextPrivate

    Parameters
    ----------

    other : QStaticTextPrivate
      Passed on as a value: Qt reads the C++ QStaticTextPrivate, which stays
      Python's own.
    """
    #  QStaticTextPrivate::QStaticTextPrivate(const QStaticTextPrivate
    #      &other)
    self._noteCreation(QStaticTextPrivate, lambda: Rituals.call(
        'ritual_ZN18QStaticTextPrivateC1ERKS_', self._valueOf(other),
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

  @overload(QPointF, QPainter, QColor)
  @overload(QPointF, NoneType, QColor)
  def paintText(
      self,
      pos: QPointF,
      p: Optional[QPainter],
      pen: QColor,
  ) -> None:
    """
    Calls Qt's 'void QStaticTextPrivate::paintText(const QPointF &pos,
    QPainter *p, const QColor &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictextprivate.html#paintText

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pen : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QStaticTextPrivate::paintText(const QPointF &pos, QPainter *p,
    #      const QColor &pen)
    self.uglySide.call(
        'ritual_ZN18QStaticTextPrivate9paintTextERK7QPointFP8QPainterRK6QCo'
        'lor',
        self._valueOf(pos, 'QPointF'), self._addressOf(p),
        self._valueOf(pen),
    )

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QStaticTextPrivate::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qstatictextprivate.html#invalidate
    """
    #  void QStaticTextPrivate::invalidate()
    self.uglySide.call('ritual_ZN18QStaticTextPrivate10invalidateEv')

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QStaticTextPrivate::init()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: unknown
    type name 'DrawTextItemDevice'; did you mean 'DrawTextItemRecorder'?.
    """
    raise NotImplementedError(
        "'QStaticTextPrivate.init' has no cute function yet. Qt's 'void "
        "QStaticTextPrivate::init()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "unknown type name 'DrawTextItemDevice'; did you mean "
        "'DrawTextItemRecorder'?.")
