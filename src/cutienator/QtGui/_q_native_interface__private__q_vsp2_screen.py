"""
QNativeInterface::Private::QVsp2Screen binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformscreen_p.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QPoint, QSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']


class QVsp2Screen(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNativeInterface::Private::QVsp2Screen: a plain
  Python object standing in front of one C++
  QNativeInterface::Private::QVsp2Screen.

  What exists
  -----------

  Every function of Qt's QNativeInterface::Private::QVsp2Screen that has a
  ritual and that Python can call so far, 5 names in all: 'addLayer',
  'setLayerBuffer', 'setLayerPosition', 'setLayerAlpha', 'removeLayer'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeInterface::Private::QVsp2Screen::~QVsp2Screen()': the
    destructor: Python never removes a C++
    QNativeInterface::Private::QVsp2Screen.
  - Qt's 'void QNativeInterface::Private::QVsp2Screen::addBlendListener(void
    (*)() callback)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 12 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QNativeInterface::Private::QVsp2Screen is created at the first
    use, not by 'QNativeInterface::Private::QVsp2Screen(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeInterface::Private::QVsp2Screen.
  - Each name of Qt's QNativeInterface::Private::QVsp2Screen that has no cute
    function yet, '__init__', 'addBlendListener', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeInterface::Private::QVsp2Screen'

  #  A C++ QNativeInterface::Private::QVsp2Screen Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNativeInterface_Private_QVsp2Screen'

  #  The functions Qt calls itself that
  #  QNativeInterface::Private::QVsp2Screen is the first to declare and that
  #  cannot be handed to Python yet, each as Qt declares it. A class of a
  #  program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'addBlendListener': (
          'void '
          'QNativeInterface::Private::QVsp2Screen::addBlendListener(void '
          '(*)())',
      ),
  }

  #  The functions Qt calls itself that
  #  QNativeInterface::Private::QVsp2Screen is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'addLayer': (
          ('_ZN16QNativeInterface7Private11QVsp2Screen8addLayerEiRK5QSizeRK'
           '6QPointjj',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QSize'),
               ('address', 'value', 'QtCore:QPoint'),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
           )),
      ),
      'setLayerBuffer': (
          ('_ZN16QNativeInterface7Private11QVsp2Screen14setLayerBufferEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'setLayerPosition': (
          ('_ZN16QNativeInterface7Private11QVsp2Screen16setLayerPositionEiR'
           'K6QPoint',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'setLayerAlpha': (
          ('_ZN16QNativeInterface7Private11QVsp2Screen13setLayerAlphaEid',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'removeLayer': (
          ('_ZN16QNativeInterface7Private11QVsp2Screen11removeLayerEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def setLayerBuffer(self, id: int, dmabufFd: int) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QVsp2Screen::setLayerBuffer(int id, int
    dmabufFd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qvsp2screen.html

    Parameters
    ----------

    id : int
      Passed on as it is.

    dmabufFd : int
      Passed on as it is.
    """
    #  void QNativeInterface::Private::QVsp2Screen::setLayerBuffer(int id,
    #      int dmabufFd)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private11QVsp2Screen14setLayerBufferEi'
        'i',
        id, dmabufFd,
    )

  @overload(int, QPoint)
  def setLayerPosition(self, id: int, position: QPoint) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QVsp2Screen::setLayerPosition(int id, const
    QPoint &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qvsp2screen.html

    Parameters
    ----------

    id : int
      Passed on as it is.

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QNativeInterface::Private::QVsp2Screen::setLayerPosition(int id,
    #      const QPoint &position)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private11QVsp2Screen16setLayerPosition'
        'EiRK6QPoint',
        id, self._valueOf(position),
    )

  @overload(int, float)
  def setLayerAlpha(self, id: int, alpha: float) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QVsp2Screen::setLayerAlpha(int id, qreal
    alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qvsp2screen.html

    Parameters
    ----------

    id : int
      Passed on as it is.

    alpha : float
      Passed on as it is.
    """
    #  void QNativeInterface::Private::QVsp2Screen::setLayerAlpha(int id,
    #      qreal alpha)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private11QVsp2Screen13setLayerAlphaEid',
        id, alpha,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNativeInterface::Private::QVsp2Screen::QVsp2Screen()': the class
    is abstract, so C++ cannot make one, and the C++ class of ours does not
    fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QNativeInterface.Private.QVsp2Screen.__init__' has no cute "
        "function yet. Qt's "
        "'QNativeInterface::Private::QVsp2Screen::QVsp2Screen()': the class "
        "is abstract, so C++ cannot make one, and the C++ class of ours "
        "does not fill in every function it leaves open.")

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

  @overload(int, QSize, QPoint, int, int)
  def addLayer(
      self,
      dmabufFd: int,
      size: QSize,
      position: QPoint,
      drmPixelFormat: int,
      bytesPerLine: int,
  ) -> int:
    """
    Calls Qt's 'int QNativeInterface::Private::QVsp2Screen::addLayer(int
    dmabufFd, const QSize &size, const QPoint &position, uint drmPixelFormat,
    uint bytesPerLine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qvsp2screen.html#addLayer

    Parameters
    ----------

    dmabufFd : int
      Passed on as it is.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    drmPixelFormat : int
      Passed on as it is.

    bytesPerLine : int
      Passed on as it is.
    """
    #  int QNativeInterface::Private::QVsp2Screen::addLayer(int dmabufFd,
    #      const QSize &size, const QPoint &position, uint drmPixelFormat,
    #      uint bytesPerLine)
    return self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private11QVsp2Screen8addLayerEiRK5QSiz'
        'eRK6QPointjj',
        dmabufFd, self._valueOf(size), self._valueOf(position),
        drmPixelFormat, bytesPerLine,
    )

  @overload(int)
  def removeLayer(self, id: int) -> bool:
    """
    Calls Qt's 'bool QNativeInterface::Private::QVsp2Screen::removeLayer(int
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qvsp2screen.html

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  bool QNativeInterface::Private::QVsp2Screen::removeLayer(int id)
    return self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private11QVsp2Screen11removeLayerEi',
        id,
    )

  @staticmethod
  def addBlendListener(*__, **_) -> Never:
    """
    Qt's 'void QNativeInterface::Private::QVsp2Screen::addBlendListener(void
    (*)() callback)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.Private.QVsp2Screen.addBlendListener' has no "
        "cute function yet. Qt's 'void "
        "QNativeInterface::Private::QVsp2Screen::addBlendListener(void "
        "(*)() callback)': takes a type Python has no way to hand over yet.")
