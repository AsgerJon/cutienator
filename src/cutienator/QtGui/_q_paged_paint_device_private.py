"""
QPagedPaintDevicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qpagedpaintdevice_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPagedPaintDevicePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QPageLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMarginsF
  from . import QPageSize, QPagedPaintDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMarginsF = WAIT['QMarginsF']
  QPageSize = WAIT['QPageSize']
  QPagedPaintDevice = WAIT['QPagedPaintDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPagedPaintDevicePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPagedPaintDevicePrivate: a plain Python object
  standing in front of one C++ QPagedPaintDevicePrivate.

  What exists
  -----------

  Every function of Qt's QPagedPaintDevicePrivate that has a ritual and that
  Python can call so far, 6 names in all: 'setPageLayout', 'setPageSize',
  'setPageOrientation', 'setPageMargins', 'pageLayout', 'get'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPagedPaintDevicePrivate::~QPagedPaintDevicePrivate()': the
    destructor: Python never removes a C++ QPagedPaintDevicePrivate.

  What to expect
  --------------

  - The C++ QPagedPaintDevicePrivate is created at the first use, not by
    'QPagedPaintDevicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPagedPaintDevicePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QPagedPaintDevice)
  @overload(NoneType)
  def get(
      pd: Optional[QPagedPaintDevice],
  ) -> Optional[QPagedPaintDevicePrivate]:
    """
    Calls Qt's 'QPagedPaintDevicePrivate
    *QPagedPaintDevicePrivate::get(QPagedPaintDevice *pd)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagedpaintdeviceprivate.html#get

    Parameters
    ----------

    pd : Optional[QPagedPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPagedPaintDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPagedPaintDevicePrivate
    #      *QPagedPaintDevicePrivate::get(QPagedPaintDevice *pd)
    address = Rituals.call(
        'ritual_ZN24QPagedPaintDevicePrivate3getEP17QPagedPaintDevice',
        CuteMixin._addressOf(pd, 'QPagedPaintDevice'),
    )
    return QPagedPaintDevicePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPagedPaintDevicePrivate'

  #  A C++ QPagedPaintDevicePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPagedPaintDevicePrivate'

  #  The functions Qt calls itself that QPagedPaintDevicePrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setPageLayout': (
          ('_ZN24QPagedPaintDevicePrivate13setPageLayoutERK11QPageLayout',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QPageLayout'),
           )),
      ),
      'setPageSize': (
          ('_ZN24QPagedPaintDevicePrivate11setPageSizeERK9QPageSize',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QPageSize'),
           )),
      ),
      'setPageOrientation': (
          ('_ZN24QPagedPaintDevicePrivate18setPageOrientationEN11QPageLayou'
           't11OrientationE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QPageLayout.Orientation'),
           )),
      ),
      'setPageMargins': (
          ('_ZN24QPagedPaintDevicePrivate14setPageMarginsERK9QMarginsFN11QP'
           'ageLayout4UnitE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QMarginsF'),
               ('int', 'enum', 'QtGui:QPageLayout.Unit'),
           )),
      ),
      'pageLayout': (
          ('_ZNK24QPagedPaintDevicePrivate10pageLayoutEv',
           ('address', 'value', 'QtGui:QPageLayout'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pageLayout(self) -> QPageLayout:
    """
    Calls Qt's 'QPageLayout QPagedPaintDevicePrivate::pageLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagedpaintdeviceprivate.html#pageLayout

    Returns
    -------

    QPageLayout
      A new cute QPageLayout around the copy Qt gave back. Python owns it.
    """
    #  QPageLayout QPagedPaintDevicePrivate::pageLayout() const
    address = self.uglySide.call(
        'ritual_ZNK24QPagedPaintDevicePrivate10pageLayoutEv',
    )
    return QPageLayout._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPageLayout)
  def setPageLayout(self, newPageLayout: QPageLayout) -> bool:
    """
    Calls Qt's 'bool QPagedPaintDevicePrivate::setPageLayout(const
    QPageLayout &newPageLayout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagedpaintdeviceprivate.html#setPageLayout

    Parameters
    ----------

    newPageLayout : QPageLayout
      Passed on as a value: Qt reads the C++ QPageLayout, which stays
      Python's own.
    """
    #  bool QPagedPaintDevicePrivate::setPageLayout(const QPageLayout
    #      &newPageLayout)
    return self.uglySide.call(
        'ritual_ZN24QPagedPaintDevicePrivate13setPageLayoutERK11QPageLayout',
        self._valueOf(newPageLayout),
    )

  @overload(QPageSize)
  def setPageSize(self, pageSize: QPageSize) -> bool:
    """
    Calls Qt's 'bool QPagedPaintDevicePrivate::setPageSize(const QPageSize
    &pageSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagedpaintdeviceprivate.html#setPageSize

    Parameters
    ----------

    pageSize : QPageSize
      Passed on as a value: Qt reads the C++ QPageSize, which stays Python's
      own.
    """
    #  bool QPagedPaintDevicePrivate::setPageSize(const QPageSize &pageSize)
    return self.uglySide.call(
        'ritual_ZN24QPagedPaintDevicePrivate11setPageSizeERK9QPageSize',
        self._valueOf(pageSize),
    )

  @overload(QPageLayout.Orientation)
  def setPageOrientation(self, orientation: QPageLayout.Orientation) -> bool:
    """
    Calls Qt's 'bool
    QPagedPaintDevicePrivate::setPageOrientation(QPageLayout::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagedpaintdeviceprivate.html#setPageOrientation

    Parameters
    ----------

    orientation : QPageLayout.Orientation
      Passed on as its number.
    """
    #  bool QPagedPaintDevicePrivate::setPageOrientation(QPageLayout::
    #      Orientation orientation)
    return self.uglySide.call(
        'ritual_ZN24QPagedPaintDevicePrivate18setPageOrientationEN11QPageLa'
        'yout11OrientationE',
        orientation.value,
    )

  @overload(QMarginsF, QPageLayout.Unit)
  def setPageMargins(
      self,
      margins: QMarginsF,
      units: QPageLayout.Unit,
  ) -> bool:
    """
    Calls Qt's 'bool QPagedPaintDevicePrivate::setPageMargins(const QMarginsF
    &margins, QPageLayout::Unit units)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagedpaintdeviceprivate.html#setPageMargins

    Parameters
    ----------

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    units : QPageLayout.Unit
      Passed on as its number.
    """
    #  bool QPagedPaintDevicePrivate::setPageMargins(const QMarginsF
    #      &margins, QPageLayout::Unit units)
    return self.uglySide.call(
        'ritual_ZN24QPagedPaintDevicePrivate14setPageMarginsERK9QMarginsFN1'
        '1QPageLayout4UnitE',
        self._valueOf(margins), units.value,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPagedPaintDevicePrivate::QPagedPaintDevicePrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagedpaintdeviceprivate.html
    """
    #  QPagedPaintDevicePrivate::QPagedPaintDevicePrivate()
    self._noteCreation(QPagedPaintDevicePrivate, lambda: Rituals.call(
        'ritual_ZN24QPagedPaintDevicePrivateC1Ev',
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
