"""
QQuick3DLightmapBaker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dlightmapbaker_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DLightmapBaker to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick import QQuickCloseEvent
  from . import QQuick3DViewport
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DViewport = WAIT['QQuick3DViewport']
  QQuickCloseEvent = WAIT['QQuickCloseEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DLightmapBaker(QObject):
  """
  The cute side of Qt's QQuick3DLightmapBaker: a plain Python object standing
  in front of one C++ QQuick3DLightmapBaker.

  It is built on the cute 'QObject', as Qt's QQuick3DLightmapBaker is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DLightmapBaker that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'bake',
  'denoise', 'onLmCancelButtonClicked', 'onLmWindowClosing', 'updateView'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DLightmapBaker::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DLightmapBaker::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DLightmapBaker::~QQuick3DLightmapBaker()': the destructor:
    Python never removes a C++ QQuick3DLightmapBaker.
  - Qt's 'void QQuick3DLightmapBaker::bake(Callback callback)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQuick3DLightmapBaker::denoise(Callback callback)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DLightmapBaker is created at the first use, not by
    'QQuick3DLightmapBaker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DLightmapBaker.
  - Qt tells when it has removed the C++ QQuick3DLightmapBaker. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DLightmapBaker, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BakingStatus(CuteNum, scoped=True):
    """
    The enum 'QQuick3DLightmapBaker::BakingStatus' of Qt, with the 7 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    Info = Kee[int](1)
    Warning = Kee[int](2)
    Error = Kee[int](3)
    Cancelled = Kee[int](4)
    Failed = Kee[int](5)
    Complete = Kee[int](6)

  #  The classes Qt writes inside QQuick3DLightmapBaker, each a class in here
  #  as in C++.

  class BakingControl(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DLightmapBaker::BakingControl: a plain
    Python object standing in front of one C++
    QQuick3DLightmapBaker::BakingControl.

    C++ hands a QQuick3DLightmapBaker::BakingControl around as a copy, so
    every C++ QQuick3DLightmapBaker::BakingControl behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuick3DLightmapBaker::BakingControl that has a
    ritual and that Python can call so far, 3 names in all: 'reset',
    'requestCancel', 'isCancelled'. None can be made from Python: one comes
    out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DLightmapBaker::BakingControl::~BakingControl()': the
      destructor: Python removes its C++ QQuick3DLightmapBaker::BakingControl
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuick3DLightmapBaker::BakingControl is created at the first
      use, not by 'QQuick3DLightmapBaker::BakingControl(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DLightmapBaker::BakingControl back gives a
      copy the ritual made for Python, in a new cute
      QQuick3DLightmapBaker::BakingControl.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DLightmapBaker::BakingControl'

    #  Qt's '~QQuick3DLightmapBaker::BakingControl()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QQuick3DLightmapBaker::BakingControl behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN21QQuick3DLightmapBaker13BakingControlD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isCancelled(self) -> bool:
      """
      Calls Qt's 'bool QQuick3DLightmapBaker::BakingControl::isCancelled()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dlightmapbaker-bakingcontrol.html
      """
      #  bool QQuick3DLightmapBaker::BakingControl::isCancelled() const
      return self.uglySide.call(
          'ritual_ZNK21QQuick3DLightmapBaker13BakingControl11isCancelledEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def reset(self) -> None:
      """
      Calls Qt's 'void QQuick3DLightmapBaker::BakingControl::reset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dlightmapbaker-bakingcontrol.html#reset
      """
      #  void QQuick3DLightmapBaker::BakingControl::reset()
      self.uglySide.call(
          'ritual_ZN21QQuick3DLightmapBaker13BakingControl5resetEv',
      )

    def requestCancel(self) -> None:
      """
      Calls Qt's 'void
      QQuick3DLightmapBaker::BakingControl::requestCancel()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dlightmapbaker-bakingcontrol.html
      """
      #  void QQuick3DLightmapBaker::BakingControl::requestCancel()
      self.uglySide.call(
          'ritual_ZN21QQuick3DLightmapBaker13BakingControl13requestCancelEv',
      )

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
    Calls Qt's 'QString QQuick3DLightmapBaker::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapbaker.html#tr

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
    #  QString QQuick3DLightmapBaker::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuick3DLightmapBaker2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DLightmapBaker'

  #  A C++ QQuick3DLightmapBaker Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DLightmapBaker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DLightmapBaker::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapbaker.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DLightmapBaker::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DLightmapBaker10metaObjectEv',
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

  @overload(QQuick3DViewport)
  @overload(NoneType)
  def __init__(self, view: Optional[QQuick3DViewport]) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DLightmapBaker::QQuick3DLightmapBaker(QQuick3DViewport *view)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapbaker.html#QQuick3DLightmapBaker

    Parameters
    ----------

    view : Optional[QQuick3DViewport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuick3DLightmapBaker::QQuick3DLightmapBaker(QQuick3DViewport *view)
    self._noteCreation(QQuick3DLightmapBaker, lambda: Rituals.call(
        'ritual_ZN21QQuick3DLightmapBakerC1EP16QQuick3DViewport',
        self._addressOf(view),
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

  def bake(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapBaker::bake()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapbaker.html#bake
    """
    #  void QQuick3DLightmapBaker::bake()
    self.uglySide.call('ritual_ZN21QQuick3DLightmapBaker4bakeEv')

  def denoise(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapBaker::denoise()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dlightmapbaker.html#denoise
    """
    #  void QQuick3DLightmapBaker::denoise()
    self.uglySide.call('ritual_ZN21QQuick3DLightmapBaker7denoiseEv')

  def onLmCancelButtonClicked(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapBaker::onLmCancelButtonClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapbaker.html#onLmCancelButtonClicked
    """
    #  void QQuick3DLightmapBaker::onLmCancelButtonClicked()
    self.uglySide.call(
        'ritual_ZN21QQuick3DLightmapBaker23onLmCancelButtonClickedEv',
    )

  @overload(QQuickCloseEvent)
  @overload(NoneType)
  def onLmWindowClosing(self, event: Optional[QQuickCloseEvent]) -> None:
    """
    Calls Qt's 'void
    QQuick3DLightmapBaker::onLmWindowClosing(QQuickCloseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapbaker.html#onLmWindowClosing

    Parameters
    ----------

    event : Optional[QQuickCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DLightmapBaker::onLmWindowClosing(QQuickCloseEvent *event)
    self.uglySide.call(
        'ritual_ZN21QQuick3DLightmapBaker17onLmWindowClosingEP16QQuickClose'
        'Event',
        self._addressOf(event),
    )

  def updateView(self) -> None:
    """
    Calls Qt's 'void QQuick3DLightmapBaker::updateView()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dlightmapbaker.html#updateView
    """
    #  void QQuick3DLightmapBaker::updateView()
    self.uglySide.call('ritual_ZN21QQuick3DLightmapBaker10updateViewEv')
