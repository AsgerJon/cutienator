"""
QmlSensorOutputRange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensorrange_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QmlSensorOutputRange to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlSensorOutputRange(QObject):
  """
  The cute side of Qt's QmlSensorOutputRange: a plain Python object standing
  in front of one C++ QmlSensorOutputRange.

  It is built on the cute 'QObject', as Qt's QmlSensorOutputRange is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlSensorOutputRange that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'minimum',
  'setMinimum', 'maximum', 'setMaximum', 'accuracy', 'setAccuracy'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlSensorOutputRange::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QmlSensorOutputRange::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlSensorOutputRange::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QmlSensorOutputRange::~QmlSensorOutputRange()': the destructor:
    Python never removes a C++ QmlSensorOutputRange.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlSensorOutputRange is created at the first use, not by
    'QmlSensorOutputRange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlSensorOutputRange.
  - Qt tells when it has removed the C++ QmlSensorOutputRange. Every call on
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
    Calls Qt's 'QString QmlSensorOutputRange::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensoroutputrange.html#tr

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
    #  QString QmlSensorOutputRange::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QmlSensorOutputRange2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlSensorOutputRange'

  #  A C++ QmlSensorOutputRange Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlSensorOutputRange'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlSensorOutputRange::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensoroutputrange.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlSensorOutputRange::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QmlSensorOutputRange10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def minimum(self) -> float:
    """
    Calls Qt's 'qreal QmlSensorOutputRange::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensoroutputrange.html#minimum
    """
    #  qreal QmlSensorOutputRange::minimum() const
    return self.uglySide.call('ritual_ZNK20QmlSensorOutputRange7minimumEv')

  def maximum(self) -> float:
    """
    Calls Qt's 'qreal QmlSensorOutputRange::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensoroutputrange.html#maximum
    """
    #  qreal QmlSensorOutputRange::maximum() const
    return self.uglySide.call('ritual_ZNK20QmlSensorOutputRange7maximumEv')

  def accuracy(self) -> float:
    """
    Calls Qt's 'qreal QmlSensorOutputRange::accuracy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensoroutputrange.html#accuracy
    """
    #  qreal QmlSensorOutputRange::accuracy() const
    return self.uglySide.call('ritual_ZNK20QmlSensorOutputRange8accuracyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMinimum(self, mini: float) -> None:
    """
    Calls Qt's 'void QmlSensorOutputRange::setMinimum(qreal mini)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensoroutputrange.html#setMinimum

    Parameters
    ----------

    mini : float
      Passed on as it is.
    """
    #  void QmlSensorOutputRange::setMinimum(qreal mini)
    self.uglySide.call('ritual_ZN20QmlSensorOutputRange10setMinimumEd', mini)

  @overload(float)
  def setMaximum(self, maxi: float) -> None:
    """
    Calls Qt's 'void QmlSensorOutputRange::setMaximum(qreal maxi)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensoroutputrange.html#setMaximum

    Parameters
    ----------

    maxi : float
      Passed on as it is.
    """
    #  void QmlSensorOutputRange::setMaximum(qreal maxi)
    self.uglySide.call('ritual_ZN20QmlSensorOutputRange10setMaximumEd', maxi)

  @overload(float)
  def setAccuracy(self, accu: float) -> None:
    """
    Calls Qt's 'void QmlSensorOutputRange::setAccuracy(qreal accu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensoroutputrange.html#setAccuracy

    Parameters
    ----------

    accu : float
      Passed on as it is.
    """
    #  void QmlSensorOutputRange::setAccuracy(qreal accu)
    self.uglySide.call(
        'ritual_ZN20QmlSensorOutputRange11setAccuracyEd', accu,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QmlSensorOutputRange::QmlSensorOutputRange(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensoroutputrange.html#QmlSensorOutputRange

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QmlSensorOutputRange::QmlSensorOutputRange(QObject *parent)
    self._noteCreation(QmlSensorOutputRange, lambda: Rituals.call(
        'ritual_ZN20QmlSensorOutputRangeC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
