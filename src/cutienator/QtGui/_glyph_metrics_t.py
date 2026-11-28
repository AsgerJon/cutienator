"""
glyph_metrics_t binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means glyph_metrics_t to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QFixed, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFixed = WAIT['QFixed']
  QTransform = WAIT['QTransform']


class glyph_metrics_t(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's glyph_metrics_t: a plain Python object standing in
  front of one C++ glyph_metrics_t.

  C++ hands a glyph_metrics_t around as a copy, so every C++ glyph_metrics_t
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's glyph_metrics_t that has a ritual and that Python
  can call so far, 4 names in all: 'transformed', 'isValid', 'leftBearing',
  'rightBearing'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'glyph_metrics_t::~glyph_metrics_t()': the destructor: Python
    removes its C++ glyph_metrics_t by it, and has no other use for it.

  What to expect
  --------------

  - The C++ glyph_metrics_t is created at the first use, not by
    'glyph_metrics_t(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a glyph_metrics_t back gives a copy the ritual made for
    Python, in a new cute glyph_metrics_t.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'glyph_metrics_t'

  #  Qt's '~glyph_metrics_t()'. Naming it makes this a value class: Python
  #  owns every C++ glyph_metrics_t behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15glyph_metrics_tD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTransform)
  def transformed(self, xform: QTransform) -> glyph_metrics_t:
    """
    Calls Qt's 'glyph_metrics_t glyph_metrics_t::transformed(const QTransform
    &xform) const'.

    Qt's own words: https://doc.qt.io/qt-6/glyph_metrics_t.html#transformed

    Parameters
    ----------

    xform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    Returns
    -------

    glyph_metrics_t
      A new cute glyph_metrics_t around the copy Qt gave back. Python owns
      it.
    """
    #  glyph_metrics_t glyph_metrics_t::transformed(const QTransform &xform)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15glyph_metrics_t11transformedERK10QTransform',
        self._valueOf(xform),
    )
    return glyph_metrics_t._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool glyph_metrics_t::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/glyph_metrics_t.html#isValid
    """
    #  bool glyph_metrics_t::isValid() const
    return self.uglySide.call('ritual_ZNK15glyph_metrics_t7isValidEv')

  def leftBearing(self) -> QFixed:
    """
    Calls Qt's 'QFixed glyph_metrics_t::leftBearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/glyph_metrics_t.html#leftBearing

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed glyph_metrics_t::leftBearing() const
    address = self.uglySide.call(
        'ritual_ZNK15glyph_metrics_t11leftBearingEv',
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

  def rightBearing(self) -> QFixed:
    """
    Calls Qt's 'QFixed glyph_metrics_t::rightBearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/glyph_metrics_t.html#rightBearing

    Returns
    -------

    QFixed
      A new cute QFixed around the copy Qt gave back. Python owns it.
    """
    #  QFixed glyph_metrics_t::rightBearing() const
    address = self.uglySide.call(
        'ritual_ZNK15glyph_metrics_t12rightBearingEv',
    )
    from . import QFixed
    return QFixed._cuteOwning(address)

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
    Notes what was given, for Qt's 'glyph_metrics_t::glyph_metrics_t()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/glyph_metrics_t.html#glyph_metrics_t
    """
    #  glyph_metrics_t::glyph_metrics_t()
    self._noteCreation(glyph_metrics_t, lambda: Rituals.call(
        'ritual_ZN15glyph_metrics_tC1Ev',
    ))

  @overload(QFixed, QFixed, QFixed, QFixed, QFixed, QFixed)
  def __init__(
      self,
      _x: QFixed,
      _y: QFixed,
      _width: QFixed,
      _height: QFixed,
      _xoff: QFixed,
      _yoff: QFixed,
  ) -> None:
    """
    Notes what was given, for Qt's 'glyph_metrics_t::glyph_metrics_t(QFixed
    _x, QFixed _y, QFixed _width, QFixed _height, QFixed _xoff, QFixed
    _yoff)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/glyph_metrics_t.html#glyph_metrics_t

    Parameters
    ----------

    _x : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    _y : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    _width : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    _height : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    _xoff : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.

    _yoff : QFixed
      Passed on as a value: Qt reads the C++ QFixed, which stays Python's
      own.
    """
    #  glyph_metrics_t::glyph_metrics_t(QFixed _x, QFixed _y, QFixed _width,
    #      QFixed _height, QFixed _xoff, QFixed _yoff)
    self._noteCreation(glyph_metrics_t, lambda: Rituals.call(
        'ritual_ZN15glyph_metrics_tC1E6QFixedS0_S0_S0_S0_S0_',
        self._valueOf(_x), self._valueOf(_y), self._valueOf(_width),
        self._valueOf(_height), self._valueOf(_xoff), self._valueOf(_yoff),
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
