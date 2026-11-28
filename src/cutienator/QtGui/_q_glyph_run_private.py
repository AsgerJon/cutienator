"""
QGlyphRunPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qglyphrun_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QGlyphRunPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGlyphRun
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGlyphRun = WAIT['QGlyphRun']


class QGlyphRunPrivate(QSharedData):
  """
  The cute side of Qt's QGlyphRunPrivate: a plain Python object standing in
  front of one C++ QGlyphRunPrivate.

  It is built on the cute 'QSharedData', as Qt's QGlyphRunPrivate is built on
  Qt's QSharedData, and has everything that class has.

  C++ hands a QGlyphRunPrivate around as a copy, so every C++
  QGlyphRunPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGlyphRunPrivate that has a ritual and that Python
  can call so far, 1 name in all: 'get'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGlyphRunPrivate::~QGlyphRunPrivate()': the destructor: Python
    removes its C++ QGlyphRunPrivate by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QGlyphRunPrivate is created at the first use, not by
    'QGlyphRunPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGlyphRunPrivate back gives a copy the ritual made
    for Python, in a new cute QGlyphRunPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGlyphRun)
  def get(glyphRun: QGlyphRun) -> Optional[QGlyphRunPrivate]:
    """
    Calls Qt's 'QGlyphRunPrivate *QGlyphRunPrivate::get(const QGlyphRun
    &glyphRun)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrunprivate.html#get

    Parameters
    ----------

    glyphRun : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.

    Returns
    -------

    Optional[QGlyphRunPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGlyphRunPrivate *QGlyphRunPrivate::get(const QGlyphRun &glyphRun)
    address = Rituals.call(
        'ritual_ZN16QGlyphRunPrivate3getERK9QGlyphRun',
        CuteMixin._valueOf(glyphRun),
    )
    return QGlyphRunPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGlyphRunPrivate'

  #  Qt's '~QGlyphRunPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QGlyphRunPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QGlyphRunPrivateD1Ev'

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
    Notes what was given, for Qt's 'QGlyphRunPrivate::QGlyphRunPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qglyphrunprivate.html#QGlyphRunPrivate
    """
    #  QGlyphRunPrivate::QGlyphRunPrivate()
    self._noteCreation(QGlyphRunPrivate, lambda: Rituals.call(
        'ritual_ZN16QGlyphRunPrivateC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGlyphRunPrivate) -> None:
    """
    Notes what was given, for Qt's 'QGlyphRunPrivate::QGlyphRunPrivate(const
    QGlyphRunPrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qglyphrunprivate.html#QGlyphRunPrivate

    Parameters
    ----------

    other : QGlyphRunPrivate
      Passed on as a value: Qt reads the C++ QGlyphRunPrivate, which stays
      Python's own.
    """
    #  QGlyphRunPrivate::QGlyphRunPrivate(const QGlyphRunPrivate &other)
    self._noteCreation(QGlyphRunPrivate, lambda: Rituals.call(
        'ritual_ZN16QGlyphRunPrivateC1ERKS_', self._valueOf(other),
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
