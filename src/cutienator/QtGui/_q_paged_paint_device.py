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

from ._q_page_size import QPageSize
from ._q_paint_device import QPaintDevice
from ._q_paged_paint_device_pdf_version import PdfVersion


class QPagedPaintDevice(QPaintDevice):
  """
  The cute side of Qt's QPagedPaintDevice: a plain Python object standing in
  front of one C++ QPagedPaintDevice.

  It is built on the cute 'QPaintDevice', as Qt's QPagedPaintDevice is built
  on Qt's QPaintDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPagedPaintDevice that has a ritual and that Python
  can call so far, 2 names in all: 'newPage', 'setPageSize'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPagedPaintDevice::~QPagedPaintDevice()': the destructor: Python
    never removes a C++ QPagedPaintDevice.
  - Qt's 'bool QPagedPaintDevice::setPageLayout(const QPageLayout
    &pageLayout)': names 'QPageLayout', which has no cute class yet.
  - Qt's 'bool QPagedPaintDevice::setPageOrientation(QPageLayout::Orientation
    orientation)': names the enum 'QPageLayout::Orientation', whose class
    cannot be named here.
  - Qt's 'bool QPagedPaintDevice::setPageMargins(const QMarginsF &margins,
    QPageLayout::Unit units)': names the enum 'QPageLayout::Unit', whose
    class cannot be named here.
  - Qt's 'QPageLayout QPagedPaintDevice::pageLayout() const': gives
    'QPageLayout', which has no cute class yet.
  - Qt's 'void QPagedPaintDevice::setPageRanges(const QPageRanges &ranges)':
    names 'QPageRanges', which has no cute class yet.
  - Qt's 'QPageRanges QPagedPaintDevice::pageRanges() const': gives
    'QPageRanges', which has no cute class yet.

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

  #  The enums Qt writes inside QPagedPaintDevice, and the names Qt has for
  #  the combinations of its flags enums.
  PdfVersion = PdfVersion

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPagedPaintDevice'

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
    return self.uglySide.call(
        'ritual_ZN17QPagedPaintDevice11setPageSizeERK9QPageSize',
        self._valueOf(pageSize),
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
    return self.uglySide.call('ritual_ZN17QPagedPaintDevice7newPageEv')
