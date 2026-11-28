"""
QAbstract3DGraphPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qabstract3dgraph_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAbstract3DGraphPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAbstract3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DAxis = WAIT['QtDataVisualization:QAbstract3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstract3DGraphPrivate(QObject):
  """
  The cute side of Qt's QAbstract3DGraphPrivate: a plain Python object
  standing in front of one C++ QAbstract3DGraphPrivate.

  It is built on the cute 'QObject', as Qt's QAbstract3DGraphPrivate is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstract3DGraphPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject',
  'handleDevicePixelRatioChange', 'render', 'renderLater', 'renderNow',
  'handleAxisXChanged', 'handleAxisYChanged', 'handleAxisZChanged'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstract3DGraphPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstract3DGraphPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstract3DGraphPrivate::~QAbstract3DGraphPrivate()': the
    destructor: Python never removes a C++ QAbstract3DGraphPrivate.

  What has no ritual
  ------------------

  6 of the 17 functions Qt declares: 3 leans on 'QAbstract3DGraphPrivate; 2
  not a gap; 1 leans on 'Utils.

  What to expect
  --------------

  - The C++ QAbstract3DGraphPrivate is created at the first use, not by
    'QAbstract3DGraphPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstract3DGraphPrivate.
  - Qt tells when it has removed the C++ QAbstract3DGraphPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstract3DGraphPrivate that has no cute function yet,
    '__init__', 'renderToImage', 'setVisualController', holds a function that
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
  __qt_class__ = 'QAbstract3DGraphPrivate'

  #  A C++ QAbstract3DGraphPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstract3DGraphPrivate'

  #  The functions Qt calls itself that QAbstract3DGraphPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'handleAxisXChanged': (
          ('_ZN23QAbstract3DGraphPrivate18handleAxisXChangedEP15QAbstract3D'
           'Axis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           )),
      ),
      'handleAxisYChanged': (
          ('_ZN23QAbstract3DGraphPrivate18handleAxisYChangedEP15QAbstract3D'
           'Axis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
           )),
      ),
      'handleAxisZChanged': (
          ('_ZN23QAbstract3DGraphPrivate18handleAxisZChangedEP15QAbstract3D'
           'Axis',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDataVisualization:QAbstract3DAxis'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstract3DGraphPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraphprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstract3DGraphPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QAbstract3DGraphPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QAbstract3DGraphPrivate::QAbstract3DGraphPrivate(QAbstract3DGraph
    *q)': leans on 'QAbstract3DGraphPrivate::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstract3DGraphPrivate.__init__' has no cute function yet. Qt's "
        "'QAbstract3DGraphPrivate::QAbstract3DGraphPrivate(QAbstract3DGraph "
        "*q)': leans on "
        "'QAbstract3DGraphPrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def handleDevicePixelRatioChange(self) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraphPrivate::handleDevicePixelRatioChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraphprivate.html
    """
    #  void QAbstract3DGraphPrivate::handleDevicePixelRatioChange()
    self.uglySide.call(
        'ritual_ZN23QAbstract3DGraphPrivate28handleDevicePixelRatioChangeEv',
    )

  def render(self) -> None:
    """
    Calls Qt's 'void QAbstract3DGraphPrivate::render()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraphprivate.html#render
    """
    #  void QAbstract3DGraphPrivate::render()
    self.uglySide.call('ritual_ZN23QAbstract3DGraphPrivate6renderEv')

  def renderLater(self) -> None:
    """
    Calls Qt's 'void QAbstract3DGraphPrivate::renderLater()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraphprivate.html#renderLater
    """
    #  void QAbstract3DGraphPrivate::renderLater()
    self.uglySide.call('ritual_ZN23QAbstract3DGraphPrivate11renderLaterEv')

  def renderNow(self) -> None:
    """
    Calls Qt's 'void QAbstract3DGraphPrivate::renderNow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraphprivate.html#renderNow
    """
    #  void QAbstract3DGraphPrivate::renderNow()
    self.uglySide.call('ritual_ZN23QAbstract3DGraphPrivate9renderNowEv')

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisXChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraphPrivate::handleAxisXChanged(QAbstract3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraphprivate.html#handleAxisXChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraphPrivate::handleAxisXChanged(QAbstract3DAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DGraphPrivate18handleAxisXChangedEP15QAbstrac'
        't3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisYChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraphPrivate::handleAxisYChanged(QAbstract3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraphprivate.html#handleAxisYChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraphPrivate::handleAxisYChanged(QAbstract3DAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DGraphPrivate18handleAxisYChangedEP15QAbstrac'
        't3DAxis',
        self._addressOf(axis),
    )

  @overload(QAbstract3DAxis)
  @overload(NoneType)
  def handleAxisZChanged(self, axis: Optional[QAbstract3DAxis]) -> None:
    """
    Calls Qt's 'void
    QAbstract3DGraphPrivate::handleAxisZChanged(QAbstract3DAxis *axis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dgraphprivate.html#handleAxisZChanged

    Parameters
    ----------

    axis : Optional[QAbstract3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DGraphPrivate::handleAxisZChanged(QAbstract3DAxis
    #      *axis)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DGraphPrivate18handleAxisZChangedEP15QAbstrac'
        't3DAxis',
        self._addressOf(axis),
    )

  @staticmethod
  def renderToImage(*__, **_) -> Never:
    """
    Qt's 'QImage QAbstract3DGraphPrivate::renderToImage(int msaaSamples,
    const QSize &imageSize)': leans on 'Utils::isOpenGLES()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QAbstract3DGraphPrivate.renderToImage' has no cute function yet. "
        "Qt's 'QImage QAbstract3DGraphPrivate::renderToImage(int "
        "msaaSamples, const QSize &imageSize)': leans on "
        "'Utils::isOpenGLES()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setVisualController(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstract3DGraphPrivate::setVisualController(Abstract3DController
    *controller)': leans on 'QAbstract3DGraphPrivate::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstract3DGraphPrivate.setVisualController' has no cute function "
        "yet. Qt's 'void "
        "QAbstract3DGraphPrivate::setVisualController(Abstract3DController "
        "*controller)': leans on "
        "'QAbstract3DGraphPrivate::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
