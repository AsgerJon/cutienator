"""
QSplitterLayoutStruct binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsplitter_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSplitterLayoutStruct to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']


class QSplitterLayoutStruct(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSplitterLayoutStruct: a plain Python object standing
  in front of one C++ QSplitterLayoutStruct.

  C++ hands a QSplitterLayoutStruct around as a copy, so every C++
  QSplitterLayoutStruct behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSplitterLayoutStruct that has a ritual and that
  Python can call so far, 3 names in all: 'getWidgetSize', 'getHandleSize',
  'pick'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSplitterLayoutStruct::~QSplitterLayoutStruct()': the destructor:
    Python removes its C++ QSplitterLayoutStruct by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSplitterLayoutStruct is created at the first use, not by
    'QSplitterLayoutStruct(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSplitterLayoutStruct back gives a copy the ritual
    made for Python, in a new cute QSplitterLayoutStruct.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSplitterLayoutStruct'

  #  Qt's '~QSplitterLayoutStruct()'. Naming it makes this a value class:
  #  Python owns every C++ QSplitterLayoutStruct behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QSplitterLayoutStructD1Ev'

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
    'QSplitterLayoutStruct::QSplitterLayoutStruct()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterlayoutstruct.html#QSplitterLayoutStruct
    """
    #  QSplitterLayoutStruct::QSplitterLayoutStruct()
    self._noteCreation(QSplitterLayoutStruct, lambda: Rituals.call(
        'ritual_ZN21QSplitterLayoutStructC1Ev',
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

  @overload(Qt.Orientation)
  def getWidgetSize(self, orient: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QSplitterLayoutStruct::getWidgetSize(Qt::Orientation
    orient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterlayoutstruct.html#getWidgetSize

    Parameters
    ----------

    orient : Qt.Orientation
      Passed on as its number.
    """
    #  int QSplitterLayoutStruct::getWidgetSize(Qt::Orientation orient)
    return self.uglySide.call(
        'ritual_ZN21QSplitterLayoutStruct13getWidgetSizeEN2Qt11OrientationE',
        orient.value,
    )

  @overload(Qt.Orientation)
  def getHandleSize(self, orient: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QSplitterLayoutStruct::getHandleSize(Qt::Orientation
    orient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterlayoutstruct.html#getHandleSize

    Parameters
    ----------

    orient : Qt.Orientation
      Passed on as its number.
    """
    #  int QSplitterLayoutStruct::getHandleSize(Qt::Orientation orient)
    return self.uglySide.call(
        'ritual_ZN21QSplitterLayoutStruct13getHandleSizeEN2Qt11OrientationE',
        orient.value,
    )

  @overload(QSize, Qt.Orientation)
  def pick(self, size: QSize, orient: Qt.Orientation) -> int:
    """
    Calls Qt's 'int QSplitterLayoutStruct::pick(const QSize &size,
    Qt::Orientation orient)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterlayoutstruct.html#pick

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    orient : Qt.Orientation
      Passed on as its number.
    """
    #  int QSplitterLayoutStruct::pick(const QSize &size, Qt::Orientation
    #      orient)
    return self.uglySide.call(
        'ritual_ZN21QSplitterLayoutStruct4pickERK5QSizeN2Qt11OrientationE',
        self._valueOf(size), orient.value,
    )
