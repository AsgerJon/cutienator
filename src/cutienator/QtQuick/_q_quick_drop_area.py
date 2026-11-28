"""
QQuickDropArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdroparea_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDropArea to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent
  from ..QtGui import QDropEvent
  from . import QQuickDragEvent, QQuickDropAreaDrag
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QQuickDragEvent = WAIT['QQuickDragEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDropArea(QQuickItem):
  """
  The cute side of Qt's QQuickDropArea: a plain Python object standing in
  front of one C++ QQuickDropArea.

  It is built on the cute 'QQuickItem', as Qt's QQuickDropArea is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDropArea that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'containsDrag', 'keys',
  'setKeys', 'drag', 'containsDragChanged', 'keysChanged', 'sourceChanged',
  'entered', 'exited', 'positionChanged', 'dropped', 'dragMoveEvent',
  'dragEnterEvent', 'dragLeaveEvent', 'dropEvent'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDropArea::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickDropArea::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickDropArea::~QQuickDropArea()': the destructor: Python never
    removes a C++ QQuickDropArea.
  - Qt's 'QQuickDropAreaPrivate *QQuickDropArea::d_func()': gives
    'QQuickDropAreaPrivate', which has no cute class yet.
  - Qt's 'const QQuickDropAreaPrivate *QQuickDropArea::d_func() const': gives
    'QQuickDropAreaPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 28 functions Qt declares: 2 not a gap; 2 forbidden; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickDropArea is created at the first use, not by
    'QQuickDropArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDropArea.
  - Qt tells when it has removed the C++ QQuickDropArea. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickDropArea that has no cute function yet,
    'setContainsDrag', holds a function that raises 'NotImplementedError',
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
    Calls Qt's 'QString QQuickDropArea::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#tr

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
    #  QString QQuickDropArea::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickDropArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDropArea'

  #  A C++ QQuickDropArea Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDropArea'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDropArea::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDropArea::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickDropArea10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def containsDrag(self) -> bool:
    """
    Calls Qt's 'bool QQuickDropArea::containsDrag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#containsDrag
    """
    #  bool QQuickDropArea::containsDrag() const
    return self.uglySide.call('ritual_ZNK14QQuickDropArea12containsDragEv')

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickDropArea::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickDropArea::keys() const
    address = self.uglySide.call('ritual_ZNK14QQuickDropArea4keysEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setKeys(self, keys: QStringList) -> None:
    """
    Calls Qt's 'void QQuickDropArea::setKeys(const QStringList &keys)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#setKeys

    Parameters
    ----------

    keys : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickDropArea::setKeys(const QStringList &keys)
    self.uglySide.call(
        'ritual_ZN14QQuickDropArea7setKeysERK5QListI7QStringE',
        self._valueOf(keys),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickDropArea::QQuickDropArea(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#QQuickDropArea

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickDropArea::QQuickDropArea(QQuickItem *parent)
    self._noteCreation(QQuickDropArea, lambda: Rituals.call(
        'ritual_ZN14QQuickDropAreaC1EP10QQuickItem', self._addressOf(parent),
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

  def drag(self) -> Optional[QQuickDropAreaDrag]:
    """
    Calls Qt's 'QQuickDropAreaDrag *QQuickDropArea::drag()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#drag

    Returns
    -------

    Optional[QQuickDropAreaDrag]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDropAreaDrag *QQuickDropArea::drag()
    address = self.uglySide.call('ritual_ZN14QQuickDropArea4dragEv')
    from . import QQuickDropAreaDrag
    return QQuickDropAreaDrag._cuteAt(address)

  def containsDragChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDropArea::containsDragChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdroparea.html#containsDragChanged
    """
    #  void QQuickDropArea::containsDragChanged()
    self.uglySide.call('ritual_ZN14QQuickDropArea19containsDragChangedEv')

  def keysChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDropArea::keysChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#keysChanged
    """
    #  void QQuickDropArea::keysChanged()
    self.uglySide.call('ritual_ZN14QQuickDropArea11keysChangedEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDropArea::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#sourceChanged
    """
    #  void QQuickDropArea::sourceChanged()
    self.uglySide.call('ritual_ZN14QQuickDropArea13sourceChangedEv')

  @overload(QQuickDragEvent)
  @overload(NoneType)
  def entered(self, drag: Optional[QQuickDragEvent]) -> None:
    """
    Calls Qt's 'void QQuickDropArea::entered(QQuickDragEvent *drag)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#entered

    Parameters
    ----------

    drag : Optional[QQuickDragEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDropArea::entered(QQuickDragEvent *drag)
    self.uglySide.call(
        'ritual_ZN14QQuickDropArea7enteredEP15QQuickDragEvent',
        self._addressOf(drag),
    )

  def exited(self) -> None:
    """
    Calls Qt's 'void QQuickDropArea::exited()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#exited
    """
    #  void QQuickDropArea::exited()
    self.uglySide.call('ritual_ZN14QQuickDropArea6exitedEv')

  @overload(QQuickDragEvent)
  @overload(NoneType)
  def positionChanged(self, drag: Optional[QQuickDragEvent]) -> None:
    """
    Calls Qt's 'void QQuickDropArea::positionChanged(QQuickDragEvent *drag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdroparea.html#positionChanged

    Parameters
    ----------

    drag : Optional[QQuickDragEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDropArea::positionChanged(QQuickDragEvent *drag)
    self.uglySide.call(
        'ritual_ZN14QQuickDropArea15positionChangedEP15QQuickDragEvent',
        self._addressOf(drag),
    )

  @overload(QQuickDragEvent)
  @overload(NoneType)
  def dropped(self, drop: Optional[QQuickDragEvent]) -> None:
    """
    Calls Qt's 'void QQuickDropArea::dropped(QQuickDragEvent *drop)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#dropped

    Parameters
    ----------

    drop : Optional[QQuickDragEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDropArea::dropped(QQuickDragEvent *drop)
    self.uglySide.call(
        'ritual_ZN14QQuickDropArea7droppedEP15QQuickDragEvent',
        self._addressOf(drop),
    )

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QQuickDropArea::dragMoveEvent(QDragMoveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDropArea::dragMoveEvent(QDragMoveEvent *event)
    ritual = 'ritual_ZN14QQuickDropArea13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickDropArea13dragMoveEventEP14QDragMoveEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QQuickDropArea::dragEnterEvent(QDragEnterEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDropArea::dragEnterEvent(QDragEnterEvent *event)
    ritual = 'ritual_ZN14QQuickDropArea14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickDropArea14dragEnterEventEP15QDragEnterEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, event: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QQuickDropArea::dragLeaveEvent(QDragLeaveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDropArea::dragLeaveEvent(QDragLeaveEvent *event)
    ritual = 'ritual_ZN14QQuickDropArea14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickDropArea14dragLeaveEventEP15QDragLeaveEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QQuickDropArea::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdroparea.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDropArea::dropEvent(QDropEvent *event)
    ritual = 'ritual_ZN14QQuickDropArea9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickDropArea9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def setContainsDrag(*__, **_) -> Never:
    """
    Qt's 'void QQuickDropArea::setContainsDrag(bool drag)': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickDropArea.setContainsDrag' has no cute function yet. Qt's "
        "'void QQuickDropArea::setContainsDrag(bool drag)': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
