"""
QQuickCanvasContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcanvascontext_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickCanvasContext to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QMap, QObject, QStringList
from ..QtQml import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect, QRectF, QSize, QVariant
  from ..QtGui import QImage
  from . import QQuickCanvasItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickCanvasItem = WAIT['QQuickCanvasItem']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickCanvasContext(QObject):
  """
  The cute side of Qt's QQuickCanvasContext: a plain Python object standing
  in front of one C++ QQuickCanvasContext.

  It is built on the cute 'QObject', as Qt's QQuickCanvasContext is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickCanvasContext that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'contextNames',
  'init', 'prepare', 'flush', 'v4Engine', 'setV4Engine', 'v4value',
  'toImage', 'textureChanged'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickCanvasContext::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickCanvasContext::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickCanvasContext::~QQuickCanvasContext()': the destructor:
    Python never removes a C++ QQuickCanvasContext.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 leans on 'QQuickCanvasContext.

  What to expect
  --------------

  - The C++ QQuickCanvasContext is created at the first use, not by
    'QQuickCanvasContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickCanvasContext.
  - Qt tells when it has removed the C++ QQuickCanvasContext. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickCanvasContext that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickCanvasContext'

  #  A C++ QQuickCanvasContext Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickCanvasContext'

  #  The functions Qt calls itself that QQuickCanvasContext is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'contextNames': (
          'QStringList QQuickCanvasContext::contextNames() const',
      ),
      'init': (
          'void QQuickCanvasContext::init(QQuickCanvasItem *, const '
          'QVariantMap &)',
      ),
  }

  #  The functions Qt calls itself that QQuickCanvasContext is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'prepare': (
          ('_ZN19QQuickCanvasContext7prepareERK5QSizeS2_RK5QRectS5_bb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
               ('address', 'value', 'QtCore:QSize'),
               ('address', 'value', 'QtCore:QRect'),
               ('address', 'value', 'QtCore:QRect'),
               ('bool', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'flush': (
          ('_ZN19QQuickCanvasContext5flushEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'v4Engine': (
          ('_ZNK19QQuickCanvasContext8v4EngineEv',
           ('address', 'address', 'QtQml:QV4.ExecutionEngine'),
           ()),
      ),
      'setV4Engine': (
          ('_ZN19QQuickCanvasContext11setV4EngineEPN3QV415ExecutionEngineE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QV4.ExecutionEngine'),
           )),
      ),
      'v4value': (
          ('_ZNK19QQuickCanvasContext7v4valueEv',
           ('unsigned long long', 'number', ''),
           ()),
      ),
      'toImage': (
          ('_ZN19QQuickCanvasContext7toImageERK6QRectF',
           ('address', 'value', 'QtGui:QImage'),
           (
               ('address', 'value', 'QtCore:QRectF'),
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
    Calls Qt's 'const QMetaObject *QQuickCanvasContext::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvascontext.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickCanvasContext::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickCanvasContext10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def contextNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickCanvasContext::contextNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvascontext.html#contextNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickCanvasContext::contextNames() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickCanvasContext12contextNamesEv',
    )
    return QStringList._cuteOwning(address)

  def v4Engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QQuickCanvasContext::v4Engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvascontext.html#v4Engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QQuickCanvasContext::v4Engine() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickCanvasContext8v4EngineEv',
    )
    return QV4.ExecutionEngine._cuteAt(address)

  def v4value(self) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQuickCanvasContext::v4value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvascontext.html#v4value
    """
    #  QV4::ReturnedValue QQuickCanvasContext::v4value() const
    return self.uglySide.call('ritual_ZNK19QQuickCanvasContext7v4valueEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def setV4Engine(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Calls Qt's 'void QQuickCanvasContext::setV4Engine(QV4::ExecutionEngine
    *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvascontext.html#setV4Engine

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickCanvasContext::setV4Engine(QV4::ExecutionEngine *engine)
    self.uglySide.call(
        'ritual_ZN19QQuickCanvasContext11setV4EngineEPN3QV415ExecutionEngin'
        'eE',
        self._addressOf(engine),
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
    Qt's 'QQuickCanvasContext::QQuickCanvasContext(QObject *parent)': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QQuickCanvasContext.__init__' has no cute function yet. Qt's "
        "'QQuickCanvasContext::QQuickCanvasContext(QObject *parent)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  @overload(QQuickCanvasItem, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  def init(
      self,
      canvasItem: Optional[QQuickCanvasItem],
      args: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QQuickCanvasContext::init(QQuickCanvasItem *canvasItem,
    const QVariantMap &args)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvascontext.html#init

    Parameters
    ----------

    canvasItem : Optional[QQuickCanvasItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    args : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQuickCanvasContext::init(QQuickCanvasItem *canvasItem, const
    #      QVariantMap &args)
    self.uglySide.call(
        'ritual_ZN19QQuickCanvasContext4initEP16QQuickCanvasItemRK4QMapI7QS'
        'tring8QVariantE',
        self._addressOf(canvasItem), self._valueOf(args),
    )

  @overload(QSize, QSize, QRect, QRect, bool, bool)
  def prepare(
      self,
      canvasSize: QSize,
      tileSize: QSize,
      canvasWindow: QRect,
      dirtyRect: QRect,
      smooth: bool,
      antialiasing: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickCanvasContext::prepare(const QSize &canvasSize,
    const QSize &tileSize, const QRect &canvasWindow, const QRect &dirtyRect,
    bool smooth, bool antialiasing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvascontext.html#prepare

    Parameters
    ----------

    canvasSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    tileSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    canvasWindow : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    dirtyRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    smooth : bool
      Passed on as it is.

    antialiasing : bool
      Passed on as it is.
    """
    #  void QQuickCanvasContext::prepare(const QSize &canvasSize, const QSize
    #      &tileSize, const QRect &canvasWindow, const QRect &dirtyRect, bool
    #      smooth, bool antialiasing)
    ritual = (
        'ritual_ZN19QQuickCanvasContext7prepareERK5QSizeS2_RK5QRectS5_bb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickCanvasContext7prepareERK5QSizeS2_RK5QRectS5'
          '_bb')
    self.uglySide.call(
        ritual,
        self._valueOf(canvasSize), self._valueOf(tileSize),
        self._valueOf(canvasWindow), self._valueOf(dirtyRect), smooth,
        antialiasing,
    )

  def flush(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasContext::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvascontext.html#flush
    """
    #  void QQuickCanvasContext::flush()
    ritual = 'ritual_ZN19QQuickCanvasContext5flushEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickCanvasContext5flushEv'
    self.uglySide.call(ritual)

  @overload(QRectF)
  def toImage(self, bounds: QRectF) -> QImage:
    """
    Calls Qt's 'QImage QQuickCanvasContext::toImage(const QRectF &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcanvascontext.html#toImage

    Parameters
    ----------

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickCanvasContext::toImage(const QRectF &bounds)
    address = self.uglySide.call(
        'ritual_ZN19QQuickCanvasContext7toImageERK6QRectF',
        self._valueOf(bounds),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def textureChanged(self) -> None:
    """
    Calls Qt's 'void QQuickCanvasContext::textureChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcanvascontext.html#textureChanged
    """
    #  void QQuickCanvasContext::textureChanged()
    self.uglySide.call('ritual_ZN19QQuickCanvasContext14textureChangedEv')
