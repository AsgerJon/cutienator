"""
DeclarativeCandlestickSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativecandlestickseries_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeCandlestickSet to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtCharts import QCandlestickSet

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeCandlestickSet(QCandlestickSet):
  """
  The cute side of Qt's DeclarativeCandlestickSet: a plain Python object
  standing in front of one C++ DeclarativeCandlestickSet.

  It is built on the cute 'QCandlestickSet', as Qt's
  DeclarativeCandlestickSet is built on Qt's QCandlestickSet, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeCandlestickSet that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'setBrushFilename', 'brushFilename', 'brushFilenameChanged',
  'handleBrushChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeCandlestickSet::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int DeclarativeCandlestickSet::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DeclarativeCandlestickSet is created at the first use, not by
    'DeclarativeCandlestickSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeCandlestickSet.
  - Qt tells when it has removed the C++ DeclarativeCandlestickSet. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString DeclarativeCandlestickSet::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/declarativecandlestickset.html#tr

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
    #  QString DeclarativeCandlestickSet::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25DeclarativeCandlestickSet2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DeclarativeCandlestickSet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeCandlestickSet::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickset.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeCandlestickSet::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25DeclarativeCandlestickSet10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def brushFilename(self) -> str:
    """
    Calls Qt's 'QString DeclarativeCandlestickSet::brushFilename() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickset.html#brushFilename

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DeclarativeCandlestickSet::brushFilename() const
    return self.uglySide.call(
        'ritual_ZNK25DeclarativeCandlestickSet13brushFilenameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setBrushFilename(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSet::setBrushFilename(const
    QString &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickset.html#setBrushFilename

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeCandlestickSet::setBrushFilename(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN25DeclarativeCandlestickSet16setBrushFilenameERK7QString',
        brushFilename,
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
  @overload(float)
  @overload(float, QObject)
  @overload(float, NoneType)
  def __init__(
      self,
      timestamp: float = 0.0,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'DeclarativeCandlestickSet::DeclarativeCandlestickSet(qreal timestamp,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickset.html

    Parameters
    ----------

    timestamp : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DeclarativeCandlestickSet::DeclarativeCandlestickSet(qreal timestamp,
    #      QObject *parent)
    self._noteCreation(DeclarativeCandlestickSet, lambda: Rituals.call(
        'ritual_ZN25DeclarativeCandlestickSetC1EdP7QObject',
        timestamp, self._addressOf(parent, 'QObject'),
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

  @overload(str)
  def brushFilenameChanged(self, brushFilename: str) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSet::brushFilenameChanged(const
    QString &brushFilename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickset.html

    Parameters
    ----------

    brushFilename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DeclarativeCandlestickSet::brushFilenameChanged(const QString
    #      &brushFilename)
    self.uglySide.call(
        'ritual_ZN25DeclarativeCandlestickSet20brushFilenameChangedERK7QStr'
        'ing',
        brushFilename,
    )

  def handleBrushChanged(self) -> None:
    """
    Calls Qt's 'void DeclarativeCandlestickSet::handleBrushChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativecandlestickset.html#handleBrushChanged
    """
    #  void DeclarativeCandlestickSet::handleBrushChanged()
    self.uglySide.call(
        'ritual_ZN25DeclarativeCandlestickSet18handleBrushChangedEv',
    )
