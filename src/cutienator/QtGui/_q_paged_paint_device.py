"""
QPagedPaintDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpagedpaintdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from . import QPageLayout, QPaintDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QMarginsF
  from . import QPageRanges, QPageSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMarginsF = WAIT['QMarginsF']
  QPageRanges = WAIT['QPageRanges']
  QPageSize = WAIT['QPageSize']


class QPagedPaintDevice(QPaintDevice):
  """
  The cute side of Qt's QPagedPaintDevice: a plain Python object standing in
  front of one C++ QPagedPaintDevice.

  It is built on the cute 'QPaintDevice', as Qt's QPagedPaintDevice is built
  on Qt's QPaintDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPagedPaintDevice that has a ritual and that Python
  can call so far, 8 names in all: 'newPage', 'setPageLayout', 'setPageSize',
  'setPageOrientation', 'setPageMargins', 'pageLayout', 'setPageRanges',
  'pageRanges'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPagedPaintDevice::~QPagedPaintDevice()': the destructor: Python
    never removes a C++ QPagedPaintDevice.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 protected.

  What to expect
  --------------

  - The C++ QPagedPaintDevice is created at the first use, not by
    'QPagedPaintDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPagedPaintDevice.
  """

  #  The enums Qt writes inside QPagedPaintDevice, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PdfVersion(CuteNum):
    """
    The enum 'QPagedPaintDevice::PdfVersion' of Qt, with the 4 names Qt gives
    in it.
    """

    PdfVersion_1_4 = Kee[int](0)
    PdfVersion_A1b = Kee[int](1)
    PdfVersion_1_6 = Kee[int](2)
    PdfVersion_X4 = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPagedPaintDevice'

  #  A C++ QPagedPaintDevice Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPagedPaintDevice'

  #  The functions Qt calls itself that QPagedPaintDevice is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'newPage': (
          ('_ZN17QPagedPaintDevice7newPageEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setPageLayout': (
          ('_ZN17QPagedPaintDevice13setPageLayoutERK11QPageLayout',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QPageLayout'),
           )),
      ),
      'setPageSize': (
          ('_ZN17QPagedPaintDevice11setPageSizeERK9QPageSize',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtGui:QPageSize'),
           )),
      ),
      'setPageOrientation': (
          ('_ZN17QPagedPaintDevice18setPageOrientationEN11QPageLayout11Orie'
           'ntationE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtGui:QPageLayout.Orientation'),
           )),
      ),
      'setPageMargins': (
          ('_ZN17QPagedPaintDevice14setPageMarginsERK9QMarginsFN11QPageLayo'
           'ut4UnitE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QMarginsF'),
               ('int', 'enum', 'QtGui:QPageLayout.Unit'),
           )),
      ),
      'setPageRanges': (
          ('_ZN17QPagedPaintDevice13setPageRangesERK11QPageRanges',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QPageRanges'),
           )),
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
    Calls Qt's 'QPageLayout QPagedPaintDevice::pageLayout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagedpaintdevice.html#pageLayout

    Returns
    -------

    QPageLayout
      A new cute QPageLayout around the copy Qt gave back. Python owns it.
    """
    #  QPageLayout QPagedPaintDevice::pageLayout() const
    address = self._callAs(
        'QPagedPaintDevice', 'ritual_ZNK17QPagedPaintDevice10pageLayoutEv',
    )
    return QPageLayout._cuteOwning(address)

  def pageRanges(self) -> QPageRanges:
    """
    Calls Qt's 'QPageRanges QPagedPaintDevice::pageRanges() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagedpaintdevice.html#pageRanges

    Returns
    -------

    QPageRanges
      A new cute QPageRanges around the copy Qt gave back. Python owns it.
    """
    #  QPageRanges QPagedPaintDevice::pageRanges() const
    address = self._callAs(
        'QPagedPaintDevice', 'ritual_ZNK17QPagedPaintDevice10pageRangesEv',
    )
    from . import QPageRanges
    return QPageRanges._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPageLayout)
  def setPageLayout(self, pageLayout: QPageLayout) -> bool:
    """
    Calls Qt's 'bool QPagedPaintDevice::setPageLayout(const QPageLayout
    &pageLayout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagedpaintdevice.html#setPageLayout

    Parameters
    ----------

    pageLayout : QPageLayout
      Passed on as a value: Qt reads the C++ QPageLayout, which stays
      Python's own.
    """
    #  bool QPagedPaintDevice::setPageLayout(const QPageLayout &pageLayout)
    ritual = 'ritual_ZN17QPagedPaintDevice13setPageLayoutERK11QPageLayout'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPagedPaintDevice13setPageLayoutERK11QPageLayout')
    return self._callAs(
        'QPagedPaintDevice', ritual, self._valueOf(pageLayout),
    )

  @overload(QPageSize)
  def setPageSize(self, pageSize: QPageSize) -> bool:
    """
    Calls Qt's 'bool QPagedPaintDevice::setPageSize(const QPageSize
    &pageSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagedpaintdevice.html#setPageSize

    Parameters
    ----------

    pageSize : QPageSize
      Passed on as a value: Qt reads the C++ QPageSize, which stays Python's
      own.
    """
    #  bool QPagedPaintDevice::setPageSize(const QPageSize &pageSize)
    ritual = 'ritual_ZN17QPagedPaintDevice11setPageSizeERK9QPageSize'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QPagedPaintDevice11setPageSizeERK9QPageSize'
    return self._callAs('QPagedPaintDevice', ritual, self._valueOf(pageSize))

  @overload(QPageLayout.Orientation)
  def setPageOrientation(self, orientation: QPageLayout.Orientation) -> bool:
    """
    Calls Qt's 'bool
    QPagedPaintDevice::setPageOrientation(QPageLayout::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagedpaintdevice.html#setPageOrientation

    Parameters
    ----------

    orientation : QPageLayout.Orientation
      Passed on as its number.
    """
    #  bool QPagedPaintDevice::setPageOrientation(QPageLayout::Orientation
    #      orientation)
    ritual = (
        'ritual_ZN17QPagedPaintDevice18setPageOrientationEN11QPageLayout11O'
        'rientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPagedPaintDevice18setPageOrientationEN11QPageLay'
          'out11OrientationE')
    return self._callAs('QPagedPaintDevice', ritual, orientation.value)

  @overload(QMarginsF)
  @overload(QMarginsF, QPageLayout.Unit)
  def setPageMargins(
      self,
      margins: QMarginsF,
      units: QPageLayout.Unit = QPageLayout.Unit.Millimeter,
  ) -> bool:
    """
    Calls Qt's 'bool QPagedPaintDevice::setPageMargins(const QMarginsF
    &margins, QPageLayout::Unit units)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagedpaintdevice.html#setPageMargins

    Parameters
    ----------

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    units : QPageLayout.Unit
      Passed on as its number. May be left out, as in Qt: it is then
      QPageLayout.Unit.Millimeter.
    """
    #  bool QPagedPaintDevice::setPageMargins(const QMarginsF &margins,
    #      QPageLayout::Unit units)
    ritual = (
        'ritual_ZN17QPagedPaintDevice14setPageMarginsERK9QMarginsFN11QPageL'
        'ayout4UnitE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPagedPaintDevice14setPageMarginsERK9QMarginsFN11'
          'QPageLayout4UnitE')
    return self._callAs(
        'QPagedPaintDevice', ritual, self._valueOf(margins), units.value,
    )

  @overload(QPageRanges)
  def setPageRanges(self, ranges: QPageRanges) -> None:
    """
    Calls Qt's 'void QPagedPaintDevice::setPageRanges(const QPageRanges
    &ranges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagedpaintdevice.html#setPageRanges

    Parameters
    ----------

    ranges : QPageRanges
      Passed on as a value: Qt reads the C++ QPageRanges, which stays
      Python's own.
    """
    #  void QPagedPaintDevice::setPageRanges(const QPageRanges &ranges)
    ritual = 'ritual_ZN17QPagedPaintDevice13setPageRangesERK11QPageRanges'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QPagedPaintDevice13setPageRangesERK11QPageRanges')
    self._callAs('QPagedPaintDevice', ritual, self._valueOf(ranges))

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

  def newPage(self) -> bool:
    """
    Calls Qt's 'bool QPagedPaintDevice::newPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qpagedpaintdevice.html#newPage
    """
    #  bool QPagedPaintDevice::newPage()
    return self._callAs(
        'QPagedPaintDevice', 'ritual_ZN17QPagedPaintDevice7newPageEv',
    )
