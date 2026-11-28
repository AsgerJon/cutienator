"""
QmlSensorRange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensorrange_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QmlSensorRange to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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


class QmlSensorRange(QObject):
  """
  The cute side of Qt's QmlSensorRange: a plain Python object standing in
  front of one C++ QmlSensorRange.

  It is built on the cute 'QObject', as Qt's QmlSensorRange is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlSensorRange that has a ritual and that Python can
  call so far, 6 names in all: 'metaObject', 'tr', 'minimum', 'setMinumum',
  'maximum', 'setMaximum'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlSensorRange::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QmlSensorRange::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlSensorRange::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QmlSensorRange::~QmlSensorRange()': the destructor: Python never
    removes a C++ QmlSensorRange.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlSensorRange is created at the first use, not by
    'QmlSensorRange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlSensorRange.
  - Qt tells when it has removed the C++ QmlSensorRange. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QmlSensorRange::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorrange.html#tr

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
    #  QString QmlSensorRange::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QmlSensorRange2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlSensorRange'

  #  A C++ QmlSensorRange Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlSensorRange'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlSensorRange::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorrange.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlSensorRange::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QmlSensorRange10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def minimum(self) -> int:
    """
    Calls Qt's 'int QmlSensorRange::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorrange.html#minimum
    """
    #  int QmlSensorRange::minimum() const
    return self.uglySide.call('ritual_ZNK14QmlSensorRange7minimumEv')

  def maximum(self) -> int:
    """
    Calls Qt's 'int QmlSensorRange::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorrange.html#maximum
    """
    #  int QmlSensorRange::maximum() const
    return self.uglySide.call('ritual_ZNK14QmlSensorRange7maximumEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMinumum(self, mini: int) -> None:
    """
    Calls Qt's 'void QmlSensorRange::setMinumum(int mini)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorrange.html#setMinumum

    Parameters
    ----------

    mini : int
      Passed on as it is.
    """
    #  void QmlSensorRange::setMinumum(int mini)
    self.uglySide.call('ritual_ZN14QmlSensorRange10setMinumumEi', mini)

  @overload(int)
  def setMaximum(self, maxi: int) -> None:
    """
    Calls Qt's 'void QmlSensorRange::setMaximum(int maxi)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorrange.html#setMaximum

    Parameters
    ----------

    maxi : int
      Passed on as it is.
    """
    #  void QmlSensorRange::setMaximum(int maxi)
    self.uglySide.call('ritual_ZN14QmlSensorRange10setMaximumEi', maxi)

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
    Notes what was given, for Qt's 'QmlSensorRange::QmlSensorRange(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensorrange.html#QmlSensorRange

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QmlSensorRange::QmlSensorRange(QObject *parent)
    self._noteCreation(QmlSensorRange, lambda: Rituals.call(
        'ritual_ZN14QmlSensorRangeC1EP7QObject',
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
