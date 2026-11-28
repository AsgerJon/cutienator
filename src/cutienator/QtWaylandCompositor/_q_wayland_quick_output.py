"""
QWaylandQuickOutput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandquickoutput.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QWaylandOutput

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QWindow
  from . import QWaylandCompositor
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QWaylandCompositor = WAIT['QWaylandCompositor']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickOutput(QWaylandOutput):
  """
  The cute side of Qt's QWaylandQuickOutput: a plain Python object standing
  in front of one C++ QWaylandQuickOutput.

  It is built on the cute 'QWaylandOutput', as Qt's QWaylandQuickOutput is
  built on Qt's QWaylandOutput, and has everything that class has. Qt's
  QWaylandQuickOutput is built on Qt's QQmlParserStatus as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QWaylandQuickOutput that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'update',
  'automaticFrameCallback', 'setAutomaticFrameCallback', 'pickClickableItem',
  'updateStarted', 'automaticFrameCallbackChanged', 'initialize',
  'classBegin', 'componentComplete', 'doFrameCallbacks'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandQuickOutput::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandQuickOutput::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject> QWaylandQuickOutput::data()': gives a
    type Python has no way to take yet.
  - Qt's 'void QWaylandQuickOutput::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'qsizetype
    QWaylandQuickOutput::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QWaylandQuickOutput::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'void QWaylandQuickOutput::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandQuickOutput is created at the first use, not by
    'QWaylandQuickOutput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQuickOutput.
  - Qt tells when it has removed the C++ QWaylandQuickOutput. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandQuickOutput that has no cute function yet,
    'appendFunction', 'atFunction', 'clearFunction', 'countFunction', 'data',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

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
    Calls Qt's 'QString QWaylandQuickOutput::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickoutput.html#tr

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
    #  QString QWaylandQuickOutput::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QWaylandQuickOutput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickOutput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandQuickOutput::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandQuickOutput::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QWaylandQuickOutput10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def automaticFrameCallback(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickOutput::automaticFrameCallback() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#automaticFrameCallback
    """
    #  bool QWaylandQuickOutput::automaticFrameCallback() const
    return self.uglySide.call(
        'ritual_ZNK19QWaylandQuickOutput22automaticFrameCallbackEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAutomaticFrameCallback(self, automatic: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickOutput::setAutomaticFrameCallback(bool
    automatic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#setAutomaticFrameCallback

    Parameters
    ----------

    automatic : bool
      Passed on as it is.
    """
    #  void QWaylandQuickOutput::setAutomaticFrameCallback(bool automatic)
    self.uglySide.call(
        'ritual_ZN19QWaylandQuickOutput25setAutomaticFrameCallbackEb',
        automatic,
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
    'QWaylandQuickOutput::QWaylandQuickOutput()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#QWaylandQuickOutput
    """
    #  QWaylandQuickOutput::QWaylandQuickOutput()
    self._noteCreation(QWaylandQuickOutput, lambda: Rituals.call(
        'ritual_ZN19QWaylandQuickOutputC1Ev',
    ))

  @overload(QWaylandCompositor, QWindow)
  @overload(QWaylandCompositor, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      compositor: Optional[QWaylandCompositor],
      window: Optional[QWindow],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandQuickOutput::QWaylandQuickOutput(QWaylandCompositor *compositor,
    QWindow *window)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#QWaylandQuickOutput

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandQuickOutput::QWaylandQuickOutput(QWaylandCompositor
    #      *compositor, QWindow *window)
    self._noteCreation(QWaylandQuickOutput, lambda: Rituals.call(
        'ritual_ZN19QWaylandQuickOutputC1EP18QWaylandCompositorP7QWindow',
        self._addressOf(compositor), self._addressOf(window),
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

  def update(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickOutput::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickoutput.html#update
    """
    #  void QWaylandQuickOutput::update()
    ritual = 'ritual_ZN19QWaylandQuickOutput6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QWaylandQuickOutput6updateEv'
    self.uglySide.call(ritual)

  @overload(QPointF)
  def pickClickableItem(self, position: QPointF) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QWaylandQuickOutput::pickClickableItem(const
    QPointF &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#pickClickableItem

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QWaylandQuickOutput::pickClickableItem(const QPointF
    #      &position)
    address = self.uglySide.call(
        'ritual_ZN19QWaylandQuickOutput17pickClickableItemERK7QPointF',
        self._valueOf(position, 'QPointF'),
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def updateStarted(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickOutput::updateStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#updateStarted
    """
    #  void QWaylandQuickOutput::updateStarted()
    self.uglySide.call('ritual_ZN19QWaylandQuickOutput13updateStartedEv')

  def automaticFrameCallbackChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickOutput::automaticFrameCallbackChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html
    """
    #  void QWaylandQuickOutput::automaticFrameCallbackChanged()
    self.uglySide.call(
        'ritual_ZN19QWaylandQuickOutput29automaticFrameCallbackChangedEv',
    )

  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickOutput::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#initialize
    """
    #  void QWaylandQuickOutput::initialize()
    ritual = 'ritual_ZN19QWaylandQuickOutput10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QWaylandQuickOutput10initializeEv'
    self.uglySide.call(ritual)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickOutput::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#classBegin
    """
    #  void QWaylandQuickOutput::classBegin()
    ritual = 'ritual_ZN19QWaylandQuickOutput10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QWaylandQuickOutput10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickOutput::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#componentComplete
    """
    #  void QWaylandQuickOutput::componentComplete()
    ritual = 'ritual_ZN19QWaylandQuickOutput17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QWaylandQuickOutput17componentCompleteEv'
    self.uglySide.call(ritual)

  def doFrameCallbacks(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickOutput::doFrameCallbacks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickoutput.html#doFrameCallbacks
    """
    #  void QWaylandQuickOutput::doFrameCallbacks()
    self.uglySide.call('ritual_ZN19QWaylandQuickOutput16doFrameCallbacksEv')

  @staticmethod
  def appendFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQuickOutput::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickOutput.appendFunction' has no cute function yet. "
        "Qt's 'void "
        "QWaylandQuickOutput::appendFunction(QQmlListProperty<QObject> "
        "*list, QObject *object)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def atFunction(*__, **_) -> Never:
    """
    Qt's 'QObject *QWaylandQuickOutput::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickOutput.atFunction' has no cute function yet. Qt's "
        "'QObject "
        "*QWaylandQuickOutput::atFunction(QQmlListProperty<QObject> *list, "
        "qsizetype index)': names 'QQmlListProperty<QObject>', which has no "
        "cute class yet.")

  @staticmethod
  def clearFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQuickOutput::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickOutput.clearFunction' has no cute function yet. Qt's "
        "'void QWaylandQuickOutput::clearFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def countFunction(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QWaylandQuickOutput::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickOutput.countFunction' has no cute function yet. Qt's "
        "'qsizetype "
        "QWaylandQuickOutput::countFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QWaylandQuickOutput::data()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickOutput.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QWaylandQuickOutput::data()': gives a "
        "type Python has no way to take yet.")
