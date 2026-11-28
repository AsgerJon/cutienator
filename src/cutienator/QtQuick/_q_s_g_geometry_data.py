"""
QSGGeometryData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsggeometry_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSGGeometryData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGGeometry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGGeometry = WAIT['QSGGeometry']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGGeometryData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGGeometryData: a plain Python object standing in
  front of one C++ QSGGeometryData.

  C++ hands a QSGGeometryData around as a copy, so every C++ QSGGeometryData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSGGeometryData that has a ritual and that Python
  can call so far, 6 names in all: 'data', 'install', 'hasDirtyVertexData',
  'clearDirtyVertexData', 'hasDirtyIndexData', 'clearDirtyIndexData'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGGeometryData::~QSGGeometryData()': the destructor: Python
    removes its C++ QSGGeometryData by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSGGeometryData is created at the first use, not by
    'QSGGeometryData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSGGeometryData back gives a copy the ritual made for
    Python, in a new cute QSGGeometryData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSGGeometry)
  @overload(NoneType)
  def data(g: Optional[QSGGeometry]) -> Optional[QSGGeometryData]:
    """
    Calls Qt's 'QSGGeometryData *QSGGeometryData::data(const QSGGeometry
    *g)'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometrydata.html#data

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGGeometryData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGGeometryData *QSGGeometryData::data(const QSGGeometry *g)
    address = Rituals.call(
        'ritual_ZN15QSGGeometryData4dataEPK11QSGGeometry',
        CuteMixin._addressOf(g),
    )
    return QSGGeometryData._cuteAt(address)

  @staticmethod
  @overload(QSGGeometry, THIS)
  @overload(QSGGeometry, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def install(
      g: Optional[QSGGeometry],
      data: Optional[QSGGeometryData],
  ) -> None:
    """
    Calls Qt's 'void QSGGeometryData::install(const QSGGeometry *g,
    QSGGeometryData *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometrydata.html#install

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[QSGGeometryData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGGeometryData::install(const QSGGeometry *g, QSGGeometryData
    #      *data)
    Rituals.call(
        'ritual_ZN15QSGGeometryData7installEPK11QSGGeometryPS_',
        CuteMixin._addressOf(g), CuteMixin._addressOf(data),
    )

  @staticmethod
  @overload(QSGGeometry)
  @overload(NoneType)
  def hasDirtyVertexData(g: Optional[QSGGeometry]) -> bool:
    """
    Calls Qt's 'bool QSGGeometryData::hasDirtyVertexData(const QSGGeometry
    *g)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrydata.html#hasDirtyVertexData

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGGeometryData::hasDirtyVertexData(const QSGGeometry *g)
    return Rituals.call(
        'ritual_ZN15QSGGeometryData18hasDirtyVertexDataEPK11QSGGeometry',
        CuteMixin._addressOf(g),
    )

  @staticmethod
  @overload(QSGGeometry)
  @overload(NoneType)
  def clearDirtyVertexData(g: Optional[QSGGeometry]) -> None:
    """
    Calls Qt's 'void QSGGeometryData::clearDirtyVertexData(const QSGGeometry
    *g)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrydata.html#clearDirtyVertexData

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGGeometryData::clearDirtyVertexData(const QSGGeometry *g)
    Rituals.call(
        'ritual_ZN15QSGGeometryData20clearDirtyVertexDataEPK11QSGGeometry',
        CuteMixin._addressOf(g),
    )

  @staticmethod
  @overload(QSGGeometry)
  @overload(NoneType)
  def hasDirtyIndexData(g: Optional[QSGGeometry]) -> bool:
    """
    Calls Qt's 'bool QSGGeometryData::hasDirtyIndexData(const QSGGeometry
    *g)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrydata.html#hasDirtyIndexData

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSGGeometryData::hasDirtyIndexData(const QSGGeometry *g)
    return Rituals.call(
        'ritual_ZN15QSGGeometryData17hasDirtyIndexDataEPK11QSGGeometry',
        CuteMixin._addressOf(g),
    )

  @staticmethod
  @overload(QSGGeometry)
  @overload(NoneType)
  def clearDirtyIndexData(g: Optional[QSGGeometry]) -> None:
    """
    Calls Qt's 'void QSGGeometryData::clearDirtyIndexData(const QSGGeometry
    *g)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrydata.html#clearDirtyIndexData

    Parameters
    ----------

    g : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGGeometryData::clearDirtyIndexData(const QSGGeometry *g)
    Rituals.call(
        'ritual_ZN15QSGGeometryData19clearDirtyIndexDataEPK11QSGGeometry',
        CuteMixin._addressOf(g),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGGeometryData'

  #  Qt's '~QSGGeometryData()'. Naming it makes this a value class: Python
  #  owns every C++ QSGGeometryData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QSGGeometryDataD1Ev'

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
