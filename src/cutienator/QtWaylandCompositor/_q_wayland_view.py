"""
QWaylandView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QRegion
  from . import QWaylandBufferRef, QWaylandOutput, QWaylandSurface
  from . import QWaylandViewPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRegion = WAIT['QRegion']
  QWaylandBufferRef = WAIT['QWaylandBufferRef']
  QWaylandOutput = WAIT['QWaylandOutput']
  QWaylandSurface = WAIT['QWaylandSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandView(QObject):
  """
  The cute side of Qt's QWaylandView: a plain Python object standing in front
  of one C++ QWaylandView.

  It is built on the cute 'QObject', as Qt's QWaylandView is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandView that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'd_func', 'renderObject',
  'surface', 'setSurface', 'output', 'setOutput', 'bufferCommitted',
  'advance', 'discardCurrentBuffer', 'currentBuffer', 'currentDamage',
  'isBufferLocked', 'setBufferLocked', 'allowDiscardFrontBuffer',
  'setAllowDiscardFrontBuffer', 'setPrimary', 'isPrimary', 'surfaceChanged',
  'surfaceDestroyed', 'outputChanged', 'bufferLockedChanged',
  'allowDiscardFrontBufferChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandView::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWaylandView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QWaylandViewPrivate *QWaylandView::d_func() const': takes in
    Python what 'QWaylandViewPrivate *QWaylandView::d_func()' takes.
  - Qt's 'QWaylandView::~QWaylandView()': the destructor: Python never
    removes a C++ QWaylandView.
  - Qt's 'struct wl_resource *QWaylandView::surfaceResource() const': gives
    'struct wl_resource', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 32 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandView is created at the first use, not by
    'QWaylandView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandView.
  - Qt tells when it has removed the C++ QWaylandView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QWaylandView that has no cute function yet,
    'surfaceResource', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QWaylandView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#tr

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
    #  QString QWaylandView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QWaylandView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandView'

  #  A C++ QWaylandView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandView'

  #  The functions Qt calls itself that QWaylandView is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'bufferCommitted': (
          ('_ZN12QWaylandView15bufferCommittedERK17QWaylandBufferRefRK7QReg'
           'ion',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtWaylandCompositor:QWaylandBufferRef'),
               ('address', 'value', 'QtGui:QRegion'),
           )),
      ),
      'advance': (
          ('_ZN12QWaylandView7advanceEv',
           ('bool', 'number', ''),
           ()),
      ),
      'discardCurrentBuffer': (
          ('_ZN12QWaylandView20discardCurrentBufferEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'currentBuffer': (
          ('_ZN12QWaylandView13currentBufferEv',
           ('address', 'value', 'QtWaylandCompositor:QWaylandBufferRef'),
           ()),
      ),
      'currentDamage': (
          ('_ZN12QWaylandView13currentDamageEv',
           ('address', 'value', 'QtGui:QRegion'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandView::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QWaylandView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def renderObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QWaylandView::renderObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#renderObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QWaylandView::renderObject() const
    address = self.uglySide.call('ritual_ZNK12QWaylandView12renderObjectEv')
    return QObject._cuteAt(address)

  def surface(self) -> Optional[QWaylandSurface]:
    """
    Calls Qt's 'QWaylandSurface *QWaylandView::surface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#surface

    Returns
    -------

    Optional[QWaylandSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurface *QWaylandView::surface() const
    address = self.uglySide.call('ritual_ZNK12QWaylandView7surfaceEv')
    from . import QWaylandSurface
    return QWaylandSurface._cuteAt(address)

  def output(self) -> Optional[QWaylandOutput]:
    """
    Calls Qt's 'QWaylandOutput *QWaylandView::output() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#output

    Returns
    -------

    Optional[QWaylandOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandOutput *QWaylandView::output() const
    address = self.uglySide.call('ritual_ZNK12QWaylandView6outputEv')
    from . import QWaylandOutput
    return QWaylandOutput._cuteAt(address)

  def isBufferLocked(self) -> bool:
    """
    Calls Qt's 'bool QWaylandView::isBufferLocked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#isBufferLocked
    """
    #  bool QWaylandView::isBufferLocked() const
    return self.uglySide.call('ritual_ZNK12QWaylandView14isBufferLockedEv')

  def allowDiscardFrontBuffer(self) -> bool:
    """
    Calls Qt's 'bool QWaylandView::allowDiscardFrontBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandview.html#allowDiscardFrontBuffer
    """
    #  bool QWaylandView::allowDiscardFrontBuffer() const
    return self.uglySide.call(
        'ritual_ZNK12QWaylandView23allowDiscardFrontBufferEv',
    )

  def isPrimary(self) -> bool:
    """
    Calls Qt's 'bool QWaylandView::isPrimary() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#isPrimary
    """
    #  bool QWaylandView::isPrimary() const
    return self.uglySide.call('ritual_ZNK12QWaylandView9isPrimaryEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandSurface)
  @overload(NoneType)
  def setSurface(self, surface: Optional[QWaylandSurface]) -> None:
    """
    Calls Qt's 'void QWaylandView::setSurface(QWaylandSurface *surface)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#setSurface

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandView::setSurface(QWaylandSurface *surface)
    self.uglySide.call(
        'ritual_ZN12QWaylandView10setSurfaceEP15QWaylandSurface',
        self._addressOf(surface),
    )

  @overload(QWaylandOutput)
  @overload(NoneType)
  def setOutput(self, output: Optional[QWaylandOutput]) -> None:
    """
    Calls Qt's 'void QWaylandView::setOutput(QWaylandOutput *output)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#setOutput

    Parameters
    ----------

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandView::setOutput(QWaylandOutput *output)
    self.uglySide.call(
        'ritual_ZN12QWaylandView9setOutputEP14QWaylandOutput',
        self._addressOf(output),
    )

  @overload(bool)
  def setBufferLocked(self, locked: bool) -> None:
    """
    Calls Qt's 'void QWaylandView::setBufferLocked(bool locked)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#setBufferLocked

    Parameters
    ----------

    locked : bool
      Passed on as it is.
    """
    #  void QWaylandView::setBufferLocked(bool locked)
    self.uglySide.call('ritual_ZN12QWaylandView15setBufferLockedEb', locked)

  @overload(bool)
  def setAllowDiscardFrontBuffer(self, discard: bool) -> None:
    """
    Calls Qt's 'void QWaylandView::setAllowDiscardFrontBuffer(bool discard)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandview.html#setAllowDiscardFrontBuffer

    Parameters
    ----------

    discard : bool
      Passed on as it is.
    """
    #  void QWaylandView::setAllowDiscardFrontBuffer(bool discard)
    self.uglySide.call(
        'ritual_ZN12QWaylandView26setAllowDiscardFrontBufferEb', discard,
    )

  def setPrimary(self) -> None:
    """
    Calls Qt's 'void QWaylandView::setPrimary()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#setPrimary
    """
    #  void QWaylandView::setPrimary()
    self.uglySide.call('ritual_ZN12QWaylandView10setPrimaryEv')

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
  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      renderObject: Optional[QObject] = None,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QWaylandView::QWaylandView(QObject
    *renderObject, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#QWaylandView

    Parameters
    ----------

    renderObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandView::QWaylandView(QObject *renderObject, QObject *parent)
    self._noteCreation(QWaylandView, lambda: Rituals.call(
        'ritual_ZN12QWaylandViewC1EP7QObjectS1_',
        self._addressOf(renderObject, 'QObject'), self._addressOf(parent,
        'QObject'),
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

  def d_func(self) -> Optional[QWaylandViewPrivate]:
    """
    Calls Qt's 'QWaylandViewPrivate *QWaylandView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#d_func

    Returns
    -------

    Optional[QWaylandViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandViewPrivate *QWaylandView::d_func()
    address = self.uglySide.call('ritual_ZN12QWaylandView6d_funcEv')
    from . import QWaylandViewPrivate
    return QWaylandViewPrivate._cuteAt(address)

  @overload(QWaylandBufferRef, QRegion)
  def bufferCommitted(
      self,
      buffer: QWaylandBufferRef,
      damage: QRegion,
  ) -> None:
    """
    Calls Qt's 'void QWaylandView::bufferCommitted(const QWaylandBufferRef
    &buffer, const QRegion &damage)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#bufferCommitted

    Parameters
    ----------

    buffer : QWaylandBufferRef
      Passed on as a value: Qt reads the C++ QWaylandBufferRef, which stays
      Python's own.

    damage : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWaylandView::bufferCommitted(const QWaylandBufferRef &buffer,
    #      const QRegion &damage)
    ritual = (
        'ritual_ZN12QWaylandView15bufferCommittedERK17QWaylandBufferRefRK7Q'
        'Region')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QWaylandView15bufferCommittedERK17QWaylandBufferR'
          'efRK7QRegion')
    self.uglySide.call(ritual, self._valueOf(buffer), self._valueOf(damage))

  def advance(self) -> bool:
    """
    Calls Qt's 'bool QWaylandView::advance()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#advance
    """
    #  bool QWaylandView::advance()
    ritual = 'ritual_ZN12QWaylandView7advanceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QWaylandView7advanceEv'
    return self.uglySide.call(ritual)

  def discardCurrentBuffer(self) -> None:
    """
    Calls Qt's 'void QWaylandView::discardCurrentBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandview.html#discardCurrentBuffer
    """
    #  void QWaylandView::discardCurrentBuffer()
    ritual = 'ritual_ZN12QWaylandView20discardCurrentBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QWaylandView20discardCurrentBufferEv'
    self.uglySide.call(ritual)

  def currentBuffer(self) -> QWaylandBufferRef:
    """
    Calls Qt's 'QWaylandBufferRef QWaylandView::currentBuffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#currentBuffer

    Returns
    -------

    QWaylandBufferRef
      A new cute QWaylandBufferRef around the copy Qt gave back. Python owns
      it.
    """
    #  QWaylandBufferRef QWaylandView::currentBuffer()
    ritual = 'ritual_ZN12QWaylandView13currentBufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QWaylandView13currentBufferEv'
    address = self.uglySide.call(ritual)
    from . import QWaylandBufferRef
    return QWaylandBufferRef._cuteOwning(address)

  def currentDamage(self) -> QRegion:
    """
    Calls Qt's 'QRegion QWaylandView::currentDamage()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#currentDamage

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QWaylandView::currentDamage()
    ritual = 'ritual_ZN12QWaylandView13currentDamageEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QWaylandView13currentDamageEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def surfaceChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandView::surfaceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#surfaceChanged
    """
    #  void QWaylandView::surfaceChanged()
    self.uglySide.call('ritual_ZN12QWaylandView14surfaceChangedEv')

  def surfaceDestroyed(self) -> None:
    """
    Calls Qt's 'void QWaylandView::surfaceDestroyed()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#surfaceDestroyed
    """
    #  void QWaylandView::surfaceDestroyed()
    self.uglySide.call('ritual_ZN12QWaylandView16surfaceDestroyedEv')

  def outputChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandView::outputChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandview.html#outputChanged
    """
    #  void QWaylandView::outputChanged()
    self.uglySide.call('ritual_ZN12QWaylandView13outputChangedEv')

  def bufferLockedChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandView::bufferLockedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandview.html#bufferLockedChanged
    """
    #  void QWaylandView::bufferLockedChanged()
    self.uglySide.call('ritual_ZN12QWaylandView19bufferLockedChangedEv')

  def allowDiscardFrontBufferChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandView::allowDiscardFrontBufferChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandview.html#allowDiscardFrontBufferChanged
    """
    #  void QWaylandView::allowDiscardFrontBufferChanged()
    self.uglySide.call(
        'ritual_ZN12QWaylandView30allowDiscardFrontBufferChangedEv',
    )

  @staticmethod
  def surfaceResource(*__, **_) -> Never:
    """
    Qt's 'struct wl_resource *QWaylandView::surfaceResource() const': gives
    'struct wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandView.surfaceResource' has no cute function yet. Qt's "
        "'struct wl_resource *QWaylandView::surfaceResource() const': gives "
        "'struct wl_resource', which has no cute class yet.")


#  Qt's 'QList<QWaylandView *>': the list of QWaylandView, which
#  'QList[QWaylandView]' gives. It is made here, so that there is one as soon
#  as there can be a QWaylandView.
QList.createKind(
    QWaylandView, 'address',
    make='ritual_list_make_QWaylandView_ptr',
    add='ritual_list_add_QWaylandView_ptr',
    size='ritual_list_size_QWaylandView_ptr',
    at='ritual_list_at_QWaylandView_ptr',
    drop='ritual_list_drop_QWaylandView_ptr',
)
