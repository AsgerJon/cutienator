"""
QMdi::MinOverlapPlacer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMdi::MinOverlapPlacer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QMdi

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QPoint, QRect, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']


class MinOverlapPlacer(QMdi.Placer):
  """
  The cute side of Qt's QMdi::MinOverlapPlacer: a plain Python object
  standing in front of one C++ QMdi::MinOverlapPlacer.

  It is built on the cute 'QMdi::Placer', as Qt's QMdi::MinOverlapPlacer is
  built on Qt's QMdi::Placer, and has everything that class has.

  C++ hands a QMdi::MinOverlapPlacer around as a copy, so every C++
  QMdi::MinOverlapPlacer behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMdi::MinOverlapPlacer that has a ritual and that
  Python can call so far, 5 names in all: 'place', 'accumulatedOverlap',
  'findMinOverlapRect', 'getCandidatePlacements', 'findMaxOverlappers'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPoint QMdi::MinOverlapPlacer::findBestPlacement(const QRect
    &domain, const QList<QRect> &rects, QList<QRect> &source)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QList<QRect> QMdi::MinOverlapPlacer::findNonInsiders(const QRect
    &domain, QList<QRect> &source)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QMdi::MinOverlapPlacer::~MinOverlapPlacer()': the destructor:
    Python removes its C++ QMdi::MinOverlapPlacer by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QMdi::MinOverlapPlacer is created at the first use, not by
    'QMdi::MinOverlapPlacer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMdi::MinOverlapPlacer back gives a copy the ritual
    made for Python, in a new cute QMdi::MinOverlapPlacer.
  - Each name of Qt's QMdi::MinOverlapPlacer that has no cute function yet,
    'findBestPlacement', 'findNonInsiders', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QRect, QList[QRect])
  def accumulatedOverlap(source: QRect, rects: QList[QRect]) -> int:
    """
    Calls Qt's 'int QMdi::MinOverlapPlacer::accumulatedOverlap(const QRect
    &source, const QList<QRect> &rects)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdi-minoverlapplacer.html#accumulatedOverlap

    Parameters
    ----------

    source : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    rects : QList[QRect]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  int QMdi::MinOverlapPlacer::accumulatedOverlap(const QRect &source,
    #      const QList<QRect> &rects)
    return Rituals.call(
        'ritual_ZN4QMdi16MinOverlapPlacer18accumulatedOverlapERK5QRectRK5QL'
        'istIS1_E',
        CuteMixin._valueOf(source), CuteMixin._valueOf(rects),
    )

  @staticmethod
  @overload(QList[QRect], QList[QRect])
  def findMinOverlapRect(source: QList[QRect], rects: QList[QRect]) -> QRect:
    """
    Calls Qt's 'QRect QMdi::MinOverlapPlacer::findMinOverlapRect(const
    QList<QRect> &source, const QList<QRect> &rects)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdi-minoverlapplacer.html#findMinOverlapRect

    Parameters
    ----------

    source : QList[QRect]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    rects : QList[QRect]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QMdi::MinOverlapPlacer::findMinOverlapRect(const QList<QRect>
    #      &source, const QList<QRect> &rects)
    address = Rituals.call(
        'ritual_ZN4QMdi16MinOverlapPlacer18findMinOverlapRectERK5QListI5QRe'
        'ctES5_',
        CuteMixin._valueOf(source), CuteMixin._valueOf(rects),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  @overload(QSize, QList[QRect], QRect)
  def getCandidatePlacements(
      size: QSize,
      rects: QList[QRect],
      domain: QRect,
  ) -> QList[QRect]:
    """
    Calls Qt's 'QList<QRect>
    QMdi::MinOverlapPlacer::getCandidatePlacements(const QSize &size, const
    QList<QRect> &rects, const QRect &domain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdi-minoverlapplacer.html#getCandidatePlacements

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    rects : QList[QRect]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    domain : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QList[QRect]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QRect> QMdi::MinOverlapPlacer::getCandidatePlacements(const
    #      QSize &size, const QList<QRect> &rects, const QRect &domain)
    address = Rituals.call(
        'ritual_ZN4QMdi16MinOverlapPlacer22getCandidatePlacementsERK5QSizeR'
        'K5QListI5QRectERKS5_',
        CuteMixin._valueOf(size), CuteMixin._valueOf(rects),
        CuteMixin._valueOf(domain),
    )
    from ..QtCore import QRect
    return QList[QRect]._cuteOwning(address)

  @staticmethod
  @overload(QRect, QList[QRect])
  def findMaxOverlappers(
      domain: QRect,
      source: QList[QRect],
  ) -> QList[QRect]:
    """
    Calls Qt's 'QList<QRect> QMdi::MinOverlapPlacer::findMaxOverlappers(const
    QRect &domain, const QList<QRect> &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmdi-minoverlapplacer.html#findMaxOverlappers

    Parameters
    ----------

    domain : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    source : QList[QRect]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QRect]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QRect> QMdi::MinOverlapPlacer::findMaxOverlappers(const QRect
    #      &domain, const QList<QRect> &source)
    address = Rituals.call(
        'ritual_ZN4QMdi16MinOverlapPlacer18findMaxOverlappersERK5QRectRK5QL'
        'istIS1_E',
        CuteMixin._valueOf(domain), CuteMixin._valueOf(source),
    )
    from ..QtCore import QRect
    return QList[QRect]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMdi::MinOverlapPlacer'

  #  Qt's '~QMdi::MinOverlapPlacer()'. Naming it makes this a value class:
  #  Python owns every C++ QMdi::MinOverlapPlacer behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QMdi16MinOverlapPlacerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize, QList[QRect], QRect)
  def place(self, size: QSize, rects: QList[QRect], domain: QRect) -> QPoint:
    """
    Calls Qt's 'QPoint QMdi::MinOverlapPlacer::place(const QSize &size, const
    QList<QRect> &rects, const QRect &domain) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmdi-minoverlapplacer.html#place

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    rects : QList[QRect]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    domain : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QMdi::MinOverlapPlacer::place(const QSize &size, const
    #      QList<QRect> &rects, const QRect &domain) const
    address = self.uglySide.call(
        'ritual_ZNK4QMdi16MinOverlapPlacer5placeERK5QSizeRK5QListI5QRectERK'
        'S5_',
        self._valueOf(size), self._valueOf(rects), self._valueOf(domain),
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

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

  @staticmethod
  def findBestPlacement(*__, **_) -> Never:
    """
    Qt's 'QPoint QMdi::MinOverlapPlacer::findBestPlacement(const QRect
    &domain, const QList<QRect> &rects, QList<QRect> &source)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMdi.MinOverlapPlacer.findBestPlacement' has no cute function "
        "yet. Qt's 'QPoint QMdi::MinOverlapPlacer::findBestPlacement(const "
        "QRect &domain, const QList<QRect> &rects, QList<QRect> &source)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def findNonInsiders(*__, **_) -> Never:
    """
    Qt's 'QList<QRect> QMdi::MinOverlapPlacer::findNonInsiders(const QRect
    &domain, QList<QRect> &source)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QMdi.MinOverlapPlacer.findNonInsiders' has no cute function yet. "
        "Qt's 'QList<QRect> QMdi::MinOverlapPlacer::findNonInsiders(const "
        "QRect &domain, QList<QRect> &source)': takes a type Python has no "
        "way to hand over yet.")
