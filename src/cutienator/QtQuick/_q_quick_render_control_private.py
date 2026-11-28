"""
QQuickRenderControlPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickrendercontrol_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickRenderControlPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QImage, QWindow
  from . import QQuickGraphicsConfiguration, QQuickRenderControl
  from . import QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGraphicsConfiguration = WAIT['QQuickGraphicsConfiguration']
  QQuickRenderControl = WAIT['QQuickRenderControl']
  QQuickWindow = WAIT['QQuickWindow']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRenderControlPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickRenderControlPrivate: a plain Python object
  standing in front of one C++ QQuickRenderControlPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickRenderControlPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRenderControlPrivate that has a ritual and
  that Python can call so far, 12 names in all: 'q_func', 'get',
  'isRenderWindowFor', 'isFocusWindowFor', 'isRenderWindow', 'cleanup',
  'windowDestroyed', 'update', 'maybeUpdate', 'initRhi', 'resetRhi', 'grab'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickRenderControl *QQuickRenderControlPrivate::q_func()
    const': takes in Python what 'QQuickRenderControl
    *QQuickRenderControlPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickRenderControlPrivate is created at the first use, not by
    'QQuickRenderControlPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRenderControlPrivate.
  """

  #  The enums Qt writes inside QQuickRenderControlPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FrameStatus(CuteNum):
    """
    The enum 'QQuickRenderControlPrivate::FrameStatus' of Qt, with the 4
    names Qt gives in it.
    """

    NotRecordingFrame = Kee[int](0)
    RecordingFrame = Kee[int](1)
    DeviceLostInBeginFrame = Kee[int](2)
    ErrorInBeginFrame = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickRenderControl)
  @overload(NoneType)
  def get(
      renderControl: Optional[QQuickRenderControl],
  ) -> Optional[QQuickRenderControlPrivate]:
    """
    Calls Qt's 'QQuickRenderControlPrivate
    *QQuickRenderControlPrivate::get(QQuickRenderControl *renderControl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#get

    Parameters
    ----------

    renderControl : Optional[QQuickRenderControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickRenderControlPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRenderControlPrivate
    #      *QQuickRenderControlPrivate::get(QQuickRenderControl
    #      *renderControl)
    address = Rituals.call(
        'ritual_ZN26QQuickRenderControlPrivate3getEP19QQuickRenderControl',
        CuteMixin._addressOf(renderControl),
    )
    return QQuickRenderControlPrivate._cuteAt(address)

  @staticmethod
  @overload(QQuickWindow, QWindow)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def isRenderWindowFor(
      quickWin: Optional[QQuickWindow],
      renderWin: Optional[QWindow],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickRenderControlPrivate::isRenderWindowFor(QQuickWindow *quickWin,
    const QWindow *renderWin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#isRenderWindowFor

    Parameters
    ----------

    quickWin : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    renderWin : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickRenderControlPrivate::isRenderWindowFor(QQuickWindow
    #      *quickWin, const QWindow *renderWin)
    return Rituals.call(
        'ritual_ZN26QQuickRenderControlPrivate17isRenderWindowForEP12QQuick'
        'WindowPK7QWindow',
        CuteMixin._addressOf(quickWin), CuteMixin._addressOf(renderWin),
    )

  @staticmethod
  @overload(QQuickWindow, QWindow)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def isFocusWindowFor(
      quickWindow: Optional[QQuickWindow],
      focusWindow: Optional[QWindow],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickRenderControlPrivate::isFocusWindowFor(QQuickWindow *quickWindow,
    const QWindow *focusWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#isFocusWindowFor

    Parameters
    ----------

    quickWindow : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    focusWindow : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickRenderControlPrivate::isFocusWindowFor(QQuickWindow
    #      *quickWindow, const QWindow *focusWindow)
    return Rituals.call(
        'ritual_ZN26QQuickRenderControlPrivate16isFocusWindowForEP12QQuickW'
        'indowPK7QWindow',
        CuteMixin._addressOf(quickWindow), CuteMixin._addressOf(focusWindow),
    )

  @staticmethod
  def cleanup() -> None:
    """
    Calls Qt's 'void QQuickRenderControlPrivate::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#cleanup
    """
    #  void QQuickRenderControlPrivate::cleanup()
    Rituals.call('ritual_ZN26QQuickRenderControlPrivate7cleanupEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRenderControlPrivate'

  #  A C++ QQuickRenderControlPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRenderControlPrivate'

  #  The functions Qt calls itself that QQuickRenderControlPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isRenderWindow': (
          ('_ZN26QQuickRenderControlPrivate14isRenderWindowEPK7QWindow',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QWindow'),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickRenderControl)
  @overload(NoneType)
  def __init__(self, renderControl: Optional[QQuickRenderControl]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickRenderControlPrivate::QQuickRenderControlPrivate(
    QQuickRenderControl *renderControl)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html

    Parameters
    ----------

    renderControl : Optional[QQuickRenderControl]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickRenderControlPrivate::QQuickRenderControlPrivate(
    #      QQuickRenderControl *renderControl)
    self._noteCreation(QQuickRenderControlPrivate, lambda: Rituals.call(
        'ritual_ZN26QQuickRenderControlPrivateC1EP19QQuickRenderControl',
        self._addressOf(renderControl),
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

  def q_func(self) -> Optional[QQuickRenderControl]:
    """
    Calls Qt's 'QQuickRenderControl *QQuickRenderControlPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#q_func

    Returns
    -------

    Optional[QQuickRenderControl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRenderControl *QQuickRenderControlPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QQuickRenderControlPrivate6q_funcEv',
    )
    from . import QQuickRenderControl
    return QQuickRenderControl._cuteAt(address)

  @overload(QWindow)
  @overload(NoneType)
  def isRenderWindow(self, w: Optional[QWindow]) -> bool:
    """
    Calls Qt's 'bool QQuickRenderControlPrivate::isRenderWindow(const QWindow
    *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#isRenderWindow

    Parameters
    ----------

    w : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickRenderControlPrivate::isRenderWindow(const QWindow *w)
    ritual = (
        'ritual_ZN26QQuickRenderControlPrivate14isRenderWindowEPK7QWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickRenderControlPrivate14isRenderWindowEPK7QWi'
          'ndow')
    return self.uglySide.call(ritual, self._addressOf(w))

  def windowDestroyed(self) -> None:
    """
    Calls Qt's 'void QQuickRenderControlPrivate::windowDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#windowDestroyed
    """
    #  void QQuickRenderControlPrivate::windowDestroyed()
    self.uglySide.call(
        'ritual_ZN26QQuickRenderControlPrivate15windowDestroyedEv',
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QQuickRenderControlPrivate::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#update
    """
    #  void QQuickRenderControlPrivate::update()
    self.uglySide.call('ritual_ZN26QQuickRenderControlPrivate6updateEv')

  def maybeUpdate(self) -> None:
    """
    Calls Qt's 'void QQuickRenderControlPrivate::maybeUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#maybeUpdate
    """
    #  void QQuickRenderControlPrivate::maybeUpdate()
    self.uglySide.call(
        'ritual_ZN26QQuickRenderControlPrivate11maybeUpdateEv',
    )

  def initRhi(self) -> bool:
    """
    Calls Qt's 'bool QQuickRenderControlPrivate::initRhi()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#initRhi
    """
    #  bool QQuickRenderControlPrivate::initRhi()
    return self.uglySide.call(
        'ritual_ZN26QQuickRenderControlPrivate7initRhiEv',
    )

  @overload(QQuickGraphicsConfiguration)
  def resetRhi(self, config: QQuickGraphicsConfiguration) -> None:
    """
    Calls Qt's 'void QQuickRenderControlPrivate::resetRhi(const
    QQuickGraphicsConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#resetRhi

    Parameters
    ----------

    config : QQuickGraphicsConfiguration
      Passed on as a value: Qt reads the C++ QQuickGraphicsConfiguration,
      which stays Python's own.
    """
    #  void QQuickRenderControlPrivate::resetRhi(const
    #      QQuickGraphicsConfiguration &config)
    self.uglySide.call(
        'ritual_ZN26QQuickRenderControlPrivate8resetRhiERK27QQuickGraphicsC'
        'onfiguration',
        self._valueOf(config),
    )

  def grab(self) -> QImage:
    """
    Calls Qt's 'QImage QQuickRenderControlPrivate::grab()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrolprivate.html#grab

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickRenderControlPrivate::grab()
    address = self.uglySide.call(
        'ritual_ZN26QQuickRenderControlPrivate4grabEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)
