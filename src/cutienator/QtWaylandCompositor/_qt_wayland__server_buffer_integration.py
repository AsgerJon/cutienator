"""
QtWayland::ServerBufferIntegration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlserverbufferintegration_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWayland::ServerBufferIntegration to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtWayland

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArrayView, QSize
  from ..QtGui import QImage
  from . import QWaylandCompositor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QImage = WAIT['QImage']
  QSize = WAIT['QSize']
  QWaylandCompositor = WAIT['QWaylandCompositor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ServerBufferIntegration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtWayland::ServerBufferIntegration: a plain Python
  object standing in front of one C++ QtWayland::ServerBufferIntegration.

  What exists
  -----------

  Every function of Qt's QtWayland::ServerBufferIntegration that has a ritual
  and that Python can call so far, 4 names in all: 'initializeHardware',
  'supportsFormat', 'createServerBufferFromImage',
  'createServerBufferFromData'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtWayland::ServerBufferIntegration::~ServerBufferIntegration()':
    the destructor: Python never removes a C++
    QtWayland::ServerBufferIntegration.

  What to expect
  --------------

  - The C++ QtWayland::ServerBufferIntegration is created at the first use,
    not by 'QtWayland::ServerBufferIntegration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtWayland::ServerBufferIntegration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtWayland::ServerBufferIntegration'

  #  A C++ QtWayland::ServerBufferIntegration Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtWayland_ServerBufferIntegration'

  #  The functions Qt calls itself that QtWayland::ServerBufferIntegration is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'initializeHardware': (
          ('_ZN9QtWayland23ServerBufferIntegration18initializeHardwareEP18Q'
           'WaylandCompositor',
           ('bool', 'number', ''),
           (
               ('address', 'address',
                'QtWaylandCompositor:QWaylandCompositor'),
           )),
      ),
      'supportsFormat': (
          ('_ZNK9QtWayland23ServerBufferIntegration14supportsFormatENS_12Se'
           'rverBuffer6FormatE',
           ('bool', 'number', ''),
           (
               ('int', 'enum',
                'QtWaylandCompositor:QtWayland.ServerBuffer.Format'),
           )),
      ),
      'createServerBufferFromImage': (
          ('_ZN9QtWayland23ServerBufferIntegration27createServerBufferFromI'
           'mageERK6QImageNS_12ServerBuffer6FormatE',
           ('address', 'address',
            'QtWaylandCompositor:QtWayland.ServerBuffer'),
           (
               ('address', 'value', 'QtGui:QImage'),
               ('int', 'enum',
                'QtWaylandCompositor:QtWayland.ServerBuffer.Format'),
           )),
      ),
      'createServerBufferFromData': (
          ('_ZN9QtWayland23ServerBufferIntegration26createServerBufferFromD'
           'ataE14QByteArrayViewRK5QSizej',
           ('address', 'address',
            'QtWaylandCompositor:QtWayland.ServerBuffer'),
           (
               ('address', 'value', 'QtCore:QByteArrayView'),
               ('address', 'value', 'QtCore:QSize'),
               ('unsigned int', 'number', ''),
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

  @overload(QtWayland.ServerBuffer.Format)
  def supportsFormat(self, format: QtWayland.ServerBuffer.Format) -> bool:
    """
    Calls Qt's 'bool
    QtWayland::ServerBufferIntegration::supportsFormat(ServerBuffer::Format
    format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-serverbufferintegration.html

    Parameters
    ----------

    format : QtWayland.ServerBuffer.Format
      Passed on as its number.
    """
    #  bool QtWayland::ServerBufferIntegration::supportsFormat(ServerBuffer::
    #      Format format) const
    return self.uglySide.call(
        'ritual_ZNK9QtWayland23ServerBufferIntegration14supportsFormatENS_1'
        '2ServerBuffer6FormatE',
        format.value,
    )

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
    'QtWayland::ServerBufferIntegration::ServerBufferIntegration()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-serverbufferintegration.html
    """
    #  QtWayland::ServerBufferIntegration::ServerBufferIntegration()
    self._noteCreation(ServerBufferIntegration, lambda: Rituals.call(
        'ritual_ZN9QtWayland23ServerBufferIntegrationC1Ev',
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

  @overload(QWaylandCompositor)
  @overload(NoneType)
  def initializeHardware(self, a0: Optional[QWaylandCompositor]) -> bool:
    """
    Calls Qt's 'bool
    QtWayland::ServerBufferIntegration::initializeHardware(QWaylandCompositor
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-serverbufferintegration.html

    Parameters
    ----------

    a0 : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QtWayland::ServerBufferIntegration::initializeHardware(
    #      QWaylandCompositor *a0)
    ritual = (
        'ritual_ZN9QtWayland23ServerBufferIntegration18initializeHardwareEP'
        '18QWaylandCompositor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QtWayland23ServerBufferIntegration18initializeHard'
          'wareEP18QWaylandCompositor')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QImage, QtWayland.ServerBuffer.Format)
  def createServerBufferFromImage(
      self,
      qimage: QImage,
      format: QtWayland.ServerBuffer.Format,
  ) -> Optional[QtWayland.ServerBuffer]:
    """
    Calls Qt's 'ServerBuffer
    *QtWayland::ServerBufferIntegration::createServerBufferFromImage(const
    QImage &qimage, ServerBuffer::Format format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-serverbufferintegration.html

    Parameters
    ----------

    qimage : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    format : QtWayland.ServerBuffer.Format
      Passed on as its number.

    Returns
    -------

    Optional[QtWayland.ServerBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ServerBuffer
    #      *QtWayland::ServerBufferIntegration::createServerBufferFromImage(
    #      const QImage &qimage, ServerBuffer::Format format)
    address = self.uglySide.call(
        'ritual_ZN9QtWayland23ServerBufferIntegration27createServerBufferFr'
        'omImageERK6QImageNS_12ServerBuffer6FormatE',
        self._valueOf(qimage), format.value,
    )
    return QtWayland.ServerBuffer._cuteAt(address)

  @overload(QByteArrayView, QSize, int)
  def createServerBufferFromData(
      self,
      view: QByteArrayView,
      size: QSize,
      glInternalFormat: int,
  ) -> Optional[QtWayland.ServerBuffer]:
    """
    Calls Qt's 'ServerBuffer
    *QtWayland::ServerBufferIntegration::createServerBufferFromData(
    QByteArrayView view, const QSize &size, uint glInternalFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtwayland-serverbufferintegration.html

    Parameters
    ----------

    view : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    glInternalFormat : int
      Passed on as it is.

    Returns
    -------

    Optional[QtWayland.ServerBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ServerBuffer
    #      *QtWayland::ServerBufferIntegration::createServerBufferFromData(
    #      QByteArrayView view, const QSize &size, uint glInternalFormat)
    ritual = (
        'ritual_ZN9QtWayland23ServerBufferIntegration26createServerBufferFr'
        'omDataE14QByteArrayViewRK5QSizej')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN9QtWayland23ServerBufferIntegration26createServerBu'
          'fferFromDataE14QByteArrayViewRK5QSizej')
    address = self.uglySide.call(
        ritual, self._valueOf(view), self._valueOf(size), glInternalFormat,
    )
    return QtWayland.ServerBuffer._cuteAt(address)
