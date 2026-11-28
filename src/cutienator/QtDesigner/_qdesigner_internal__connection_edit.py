"""
qdesigner_internal::ConnectionEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ConnectionEdit to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtWidgets import QWidget
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QRect
  from ..QtGui import QContextMenuEvent, QKeyEvent, QMouseEvent, QPaintEvent
  from ..QtGui import QPainter, QResizeEvent, QShowEvent, QUndoStack
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QResizeEvent = WAIT['QResizeEvent']
  QShowEvent = WAIT['QShowEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ConnectionEdit(QWidget, qdesigner_internal.CETypes):
  """
  The cute side of Qt's qdesigner_internal::ConnectionEdit: a plain Python
  object standing in front of one C++ qdesigner_internal::ConnectionEdit.

  It is built on the cute 'QWidget', as Qt's
  qdesigner_internal::ConnectionEdit is built on Qt's QWidget, and has
  everything that class has. It is built on the cute
  'qdesigner_internal::CETypes' as well, as Qt's
  qdesigner_internal::ConnectionEdit is built on Qt's
  qdesigner_internal::CETypes too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ConnectionEdit that has a ritual
  and that Python can call so far, 56 names in all: 'metaObject', 'tr',
  'setSelected', 'selected', 'connectionCount', 'connection',
  'indexOfConnection', 'setSource', 'setTarget', 'undoStack', 'clear',
  'showEvent', 'aboutToAddConnection', 'connectionAdded',
  'aboutToRemoveConnection', 'connectionRemoved', 'connectionSelected',
  'widgetActivated', 'connectionChanged', 'selectNone', 'selectAll',
  'deleteSelected', 'setBackground', 'updateBackground', 'widgetRemoved',
  'objectRemoved', 'updateLines', 'enableUpdateBackground', 'paintEvent',
  'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent', 'keyPressEvent',
  'mouseDoubleClickEvent', 'resizeEvent', 'contextMenuEvent',
  'createConnection', 'modifyConnection', 'widgetAt', 'addConnection',
  'widgetRect', 'endConnection', 'takeConnection', 'newlyAddedConnection',
  'clearNewlyAddedConnection', 'findObjectsUnderMouse', 'startConnection',
  'continueConnection', 'abortConnection', 'startDrag', 'continueDrag',
  'endDrag', 'adjustHotSopt', 'connectionAt', 'endPointAt', 'paintLabel'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::ConnectionEdit::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::ConnectionEdit::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::ConnectionEdit::~ConnectionEdit()': the
    destructor: Python never removes a C++
    qdesigner_internal::ConnectionEdit.
  - Qt's 'const QPointer<QWidget>
    &qdesigner_internal::ConnectionEdit::background() const': gives a type
    Python has no way to take yet.
  - Qt's 'void qdesigner_internal::ConnectionEdit::createContextMenu(QMenu
    &menu)': takes a type Python has no way to hand over yet.
  - Qt's 'State qdesigner_internal::ConnectionEdit::state() const': gives the
    enum 'qdesigner_internal::ConnectionEdit::State', whose class cannot be
    named here.
  - Qt's 'const ConnectionList
    &qdesigner_internal::ConnectionEdit::connectionList() const': gives a
    type Python has no way to take yet.
  - Qt's 'const ConnectionSet
    &qdesigner_internal::ConnectionEdit::selection() const': gives a type
    Python has no way to take yet.
  - Qt's 'void qdesigner_internal::ConnectionEdit::paintConnection(QPainter
    *p, Connection *con, WidgetSet *heavy_highlight_set, WidgetSet
    *light_highlight_set) const': names
    'qdesigner_internal::CETypes::WidgetSet', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 68 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::ConnectionEdit is created at the first use,
    not by 'qdesigner_internal::ConnectionEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ConnectionEdit.
  - Qt tells when it has removed the C++ qdesigner_internal::ConnectionEdit.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::ConnectionEdit that has no cute
    function yet, 'background', 'connectionList', 'createContextMenu',
    'paintConnection', 'selection', 'state', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString qdesigner_internal::ConnectionEdit::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#tr

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
    #  QString qdesigner_internal::ConnectionEdit::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ConnectionEdit'

  #  Qt's qdesigner_internal::ConnectionEdit is built on more than one class.
  #  The part of a C++ qdesigner_internal::ConnectionEdit that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'qdesigner_internal::CETypes':
          'ritual_cast_qdesigner_internal_ConnectionEdit_qdesigner_internal_CETypes',
  }

  #  A C++ qdesigner_internal::ConnectionEdit Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_ConnectionEdit'

  #  The functions Qt calls itself that qdesigner_internal::ConnectionEdit is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createContextMenu': (
          'void '
          'qdesigner_internal::ConnectionEdit::createContextMenu(QMenu &)',
      ),
  }

  #  The functions Qt calls itself that qdesigner_internal::ConnectionEdit is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setSource': (
          ('_ZN18qdesigner_internal14ConnectionEdit9setSourceEPNS_10Connect'
           'ionERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:qdesigner_internal.Connection'),
               ('address', 'text', ''),
           )),
      ),
      'setTarget': (
          ('_ZN18qdesigner_internal14ConnectionEdit9setTargetEPNS_10Connect'
           'ionERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:qdesigner_internal.Connection'),
               ('address', 'text', ''),
           )),
      ),
      'deleteSelected': (
          ('_ZN18qdesigner_internal14ConnectionEdit14deleteSelectedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setBackground': (
          ('_ZN18qdesigner_internal14ConnectionEdit13setBackgroundEP7QWidge'
           't',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'updateBackground': (
          ('_ZN18qdesigner_internal14ConnectionEdit16updateBackgroundEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'widgetRemoved': (
          ('_ZN18qdesigner_internal14ConnectionEdit13widgetRemovedEP7QWidge'
           't',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'objectRemoved': (
          ('_ZN18qdesigner_internal14ConnectionEdit13objectRemovedEP7QObjec'
           't',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'createConnection': (
          ('_ZN18qdesigner_internal14ConnectionEdit16createConnectionEP7QWi'
           'dgetS2_',
           ('address', 'address',
            'QtDesigner:qdesigner_internal.Connection'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'modifyConnection': (
          ('_ZN18qdesigner_internal14ConnectionEdit16modifyConnectionEPNS_1'
           '0ConnectionE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:qdesigner_internal.Connection'),
           )),
      ),
      'widgetAt': (
          ('_ZNK18qdesigner_internal14ConnectionEdit8widgetAtERK6QPoint',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'endConnection': (
          ('_ZN18qdesigner_internal14ConnectionEdit13endConnectionEP7QWidge'
           'tRK6QPoint',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'value', 'QtCore:QPoint'),
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
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::ConnectionEdit::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::ConnectionEdit::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ConnectionEdit10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(WAIT['qdesigner_internal.Connection'])
  @overload(NoneType)
  def selected(self, con: Optional[qdesigner_internal.Connection]) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::ConnectionEdit::selected(const
    Connection *con) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#selected

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::ConnectionEdit::selected(const Connection
    #      *con) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ConnectionEdit8selectedEPKNS_10Con'
        'nectionE',
        self._addressOf(con),
    )

  def connectionCount(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::ConnectionEdit::connectionCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html
    """
    #  int qdesigner_internal::ConnectionEdit::connectionCount() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ConnectionEdit15connectionCountEv',
    )

  @overload(int)
  def connection(self, i: int) -> Optional[qdesigner_internal.Connection]:
    """
    Calls Qt's 'Connection
    *qdesigner_internal::ConnectionEdit::connection(int i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#connection

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[qdesigner_internal.Connection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Connection *qdesigner_internal::ConnectionEdit::connection(int i)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ConnectionEdit10connectionEi', i,
    )
    return qdesigner_internal.Connection._cuteAt(address)

  @overload(WAIT['qdesigner_internal.Connection'])
  @overload(NoneType)
  def indexOfConnection(
      self,
      con: Optional[qdesigner_internal.Connection],
  ) -> int:
    """
    Calls Qt's 'int
    qdesigner_internal::ConnectionEdit::indexOfConnection(Connection *con)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int qdesigner_internal::ConnectionEdit::indexOfConnection(Connection
    #      *con) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ConnectionEdit17indexOfConnectionE'
        'PNS_10ConnectionE',
        self._addressOf(con),
    )

  def undoStack(self) -> Optional[QUndoStack]:
    """
    Calls Qt's 'QUndoStack *qdesigner_internal::ConnectionEdit::undoStack()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#undoStack

    Returns
    -------

    Optional[QUndoStack]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUndoStack *qdesigner_internal::ConnectionEdit::undoStack() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ConnectionEdit9undoStackEv',
    )
    from ..QtGui import QUndoStack
    return QUndoStack._cuteAt(address)

  @overload(QPoint)
  def widgetAt(self, pos: QPoint) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::ConnectionEdit::widgetAt(const
    QPoint &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#widgetAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::ConnectionEdit::widgetAt(const QPoint
    #      &pos) const
    ritual = (
        'ritual_ZNK18qdesigner_internal14ConnectionEdit8widgetAtERK6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14ConnectionEdit8widgetAtERK6Q'
          'Point')
    address = self.uglySide.call(ritual, self._valueOf(pos))
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def widgetRect(self, w: Optional[QWidget]) -> QRect:
    """
    Calls Qt's 'QRect qdesigner_internal::ConnectionEdit::widgetRect(QWidget
    *w) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#widgetRect

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect qdesigner_internal::ConnectionEdit::widgetRect(QWidget *w) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ConnectionEdit10widgetRectEP7QWidg'
        'et',
        self._addressOf(w),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def connectionAt(
      self,
      pos: QPoint,
  ) -> Optional[qdesigner_internal.Connection]:
    """
    Calls Qt's 'Connection
    *qdesigner_internal::ConnectionEdit::connectionAt(const QPoint &pos)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[qdesigner_internal.Connection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Connection *qdesigner_internal::ConnectionEdit::connectionAt(const
    #      QPoint &pos) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ConnectionEdit12connectionAtERK6QP'
        'oint',
        self._valueOf(pos),
    )
    return qdesigner_internal.Connection._cuteAt(address)

  @overload(QPoint)
  def endPointAt(self, pos: QPoint) -> qdesigner_internal.CETypes.EndPoint:
    """
    Calls Qt's 'EndPoint qdesigner_internal::ConnectionEdit::endPointAt(const
    QPoint &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#endPointAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    qdesigner_internal.CETypes.EndPoint
      A new cute qdesigner_internal::CETypes::EndPoint around the copy Qt
      gave back. Python owns it.
    """
    #  EndPoint qdesigner_internal::ConnectionEdit::endPointAt(const QPoint
    #      &pos) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ConnectionEdit10endPointAtERK6QPoi'
        'nt',
        self._valueOf(pos),
    )
    return qdesigner_internal.CETypes.EndPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['qdesigner_internal.Connection'], bool)
  @overload(NoneType, bool)
  def setSelected(
      self,
      con: Optional[qdesigner_internal.Connection],
      sel: bool,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::setSelected(Connection *con, bool
    sel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#setSelected

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sel : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::ConnectionEdit::setSelected(Connection *con,
    #      bool sel)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit11setSelectedEPNS_10C'
        'onnectionEb',
        self._addressOf(con), sel,
    )

  @overload(WAIT['qdesigner_internal.Connection'], str)
  @overload(NoneType, str)
  def setSource(
      self,
      con: Optional[qdesigner_internal.Connection],
      obj_name: str,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::setSource(Connection
    *con, const QString &obj_name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#setSource

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    obj_name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::ConnectionEdit::setSource(Connection *con,
    #      const QString &obj_name)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit9setSourceEPNS_10Conn'
        'ectionERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit9setSourceEPNS_'
          '10ConnectionERK7QString')
    self.uglySide.call(ritual, self._addressOf(con), obj_name)

  @overload(WAIT['qdesigner_internal.Connection'], str)
  @overload(NoneType, str)
  def setTarget(
      self,
      con: Optional[qdesigner_internal.Connection],
      obj_name: str,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::setTarget(Connection
    *con, const QString &obj_name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#setTarget

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    obj_name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::ConnectionEdit::setTarget(Connection *con,
    #      const QString &obj_name)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit9setTargetEPNS_10Conn'
        'ectionERK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit9setTargetEPNS_'
          '10ConnectionERK7QString')
    self.uglySide.call(ritual, self._addressOf(con), obj_name)

  @overload(QWidget)
  @overload(NoneType)
  def setBackground(self, background: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::setBackground(QWidget *background)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    background : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::setBackground(QWidget
    #      *background)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit13setBackgroundEP7QWi'
        'dget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit13setBackground'
          'EP7QWidget')
    self.uglySide.call(ritual, self._addressOf(background))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget, QDesignerFormWindowInterface)
  @overload(QWidget, NoneType)
  @overload(NoneType, QDesignerFormWindowInterface)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      parent: Optional[QWidget],
      form: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ConnectionEdit::ConnectionEdit(QWidget *parent,
    QDesignerFormWindowInterface *form)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    form : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::ConnectionEdit::ConnectionEdit(QWidget *parent,
    #      QDesignerFormWindowInterface *form)
    self._noteCreation(ConnectionEdit, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal14ConnectionEditC1EP7QWidgetP28QDesig'
        'nerFormWindowInterface',
        self._addressOf(parent), self._addressOf(form),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#clear
    """
    #  void qdesigner_internal::ConnectionEdit::clear()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit5clearEv',
    )

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, a0: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::showEvent(QShowEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#showEvent

    Parameters
    ----------

    a0 : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::showEvent(QShowEvent *a0)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit9showEventEP10QShowEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit9showEventEP10Q'
          'ShowEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(int)
  def aboutToAddConnection(self, idx: int) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::aboutToAddConnection(int idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ConnectionEdit::aboutToAddConnection(int idx)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit20aboutToAddConnectio'
        'nEi',
        idx,
    )

  @overload(WAIT['qdesigner_internal.Connection'])
  @overload(NoneType)
  def connectionAdded(
      self,
      con: Optional[qdesigner_internal.Connection],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::connectionAdded(qdesigner_internal::
    Connection *con)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::connectionAdded(
    #      qdesigner_internal::Connection *con)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit15connectionAddedEPNS'
        '_10ConnectionE',
        self._addressOf(con),
    )

  @overload(WAIT['qdesigner_internal.Connection'])
  @overload(NoneType)
  def aboutToRemoveConnection(
      self,
      con: Optional[qdesigner_internal.Connection],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::aboutToRemoveConnection(
    qdesigner_internal::Connection *con)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::aboutToRemoveConnection(
    #      qdesigner_internal::Connection *con)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit23aboutToRemoveConnec'
        'tionEPNS_10ConnectionE',
        self._addressOf(con),
    )

  @overload(int)
  def connectionRemoved(self, idx: int) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::connectionRemoved(int idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ConnectionEdit::connectionRemoved(int idx)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit17connectionRemovedEi',
        idx,
    )

  @overload(WAIT['qdesigner_internal.Connection'])
  @overload(NoneType)
  def connectionSelected(
      self,
      con: Optional[qdesigner_internal.Connection],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::connectionSelected(
    qdesigner_internal::Connection *con)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::connectionSelected(
    #      qdesigner_internal::Connection *con)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit18connectionSelectedE'
        'PNS_10ConnectionE',
        self._addressOf(con),
    )

  @overload(QWidget)
  @overload(NoneType)
  def widgetActivated(self, wgt: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::widgetActivated(QWidget *wgt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    wgt : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::widgetActivated(QWidget *wgt)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit15widgetActivatedEP7Q'
        'Widget',
        self._addressOf(wgt),
    )

  @overload(WAIT['qdesigner_internal.Connection'])
  @overload(NoneType)
  def connectionChanged(
      self,
      con: Optional[qdesigner_internal.Connection],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::connectionChanged(
    qdesigner_internal::Connection *con)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::connectionChanged(
    #      qdesigner_internal::Connection *con)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit17connectionChangedEP'
        'NS_10ConnectionE',
        self._addressOf(con),
    )

  def selectNone(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::selectNone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#selectNone
    """
    #  void qdesigner_internal::ConnectionEdit::selectNone()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit10selectNoneEv',
    )

  def selectAll(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::selectAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#selectAll
    """
    #  void qdesigner_internal::ConnectionEdit::selectAll()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit9selectAllEv',
    )

  def deleteSelected(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::deleteSelected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html
    """
    #  void qdesigner_internal::ConnectionEdit::deleteSelected()
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit14deleteSelectedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit14deleteSelecte'
          'dEv')
    self.uglySide.call(ritual)

  def updateBackground(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::updateBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html
    """
    #  void qdesigner_internal::ConnectionEdit::updateBackground()
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit16updateBackgroundEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit16updateBackgro'
          'undEv')
    self.uglySide.call(ritual)

  @overload(QWidget)
  @overload(NoneType)
  def widgetRemoved(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::widgetRemoved(QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::widgetRemoved(QWidget *w)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit13widgetRemovedEP7QWi'
        'dget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit13widgetRemoved'
          'EP7QWidget')
    self.uglySide.call(ritual, self._addressOf(w))

  @overload(QObject)
  @overload(NoneType)
  def objectRemoved(self, o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::objectRemoved(QObject *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::objectRemoved(QObject *o)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit13objectRemovedEP7QOb'
        'ject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit13objectRemoved'
          'EP7QObject')
    self.uglySide.call(ritual, self._addressOf(o, 'QObject'))

  def updateLines(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::updateLines()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#updateLines
    """
    #  void qdesigner_internal::ConnectionEdit::updateLines()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit11updateLinesEv',
    )

  @overload(bool)
  def enableUpdateBackground(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::enableUpdateBackground(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::ConnectionEdit::enableUpdateBackground(bool
    #      enable)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit22enableUpdateBackgro'
        'undEb',
        enable,
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::paintEvent(QPaintEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::paintEvent(QPaintEvent *e)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit10paintEventEP11QPain'
        'tEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit10paintEventEP1'
          '1QPaintEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::mouseMoveEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::mouseMoveEvent(QMouseEvent
    #      *e)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit14mouseMoveEventEP11Q'
        'MouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit14mouseMoveEven'
          'tEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::mousePressEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::mousePressEvent(QMouseEvent
    #      *e)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit15mousePressEventEP11'
        'QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit15mousePressEve'
          'ntEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::mouseReleaseEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::mouseReleaseEvent(QMouseEvent
    #      *e)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit17mouseReleaseEventEP'
        '11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit17mouseReleaseE'
          'ventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::keyPressEvent(QKeyEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::keyPressEvent(QKeyEvent *e)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit13keyPressEventEP9QKe'
        'yEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit13keyPressEvent'
          'EP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::mouseDoubleClickEvent(QMouseEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::mouseDoubleClickEvent(
    #      QMouseEvent *e)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit21mouseDoubleClickEve'
        'ntEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit21mouseDoubleCl'
          'ickEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, e: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::resizeEvent(QResizeEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#resizeEvent

    Parameters
    ----------

    e : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::resizeEvent(QResizeEvent *e)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit11resizeEventEP12QRes'
        'izeEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit11resizeEventEP'
          '12QResizeEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, event: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::contextMenuEvent(QContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::contextMenuEvent(
    #      QContextMenuEvent *event)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit16contextMenuEventEP1'
        '7QContextMenuEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit16contextMenuEv'
          'entEP17QContextMenuEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QWidget, QWidget)
  @overload(QWidget, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def createConnection(
      self,
      source: Optional[QWidget],
      target: Optional[QWidget],
  ) -> Optional[qdesigner_internal.Connection]:
    """
    Calls Qt's 'Connection
    *qdesigner_internal::ConnectionEdit::createConnection(QWidget *source,
    QWidget *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    source : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[qdesigner_internal.Connection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Connection
    #      *qdesigner_internal::ConnectionEdit::createConnection(QWidget
    #      *source, QWidget *target)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit16createConnectionEP7'
        'QWidgetS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit16createConnect'
          'ionEP7QWidgetS2_')
    address = self.uglySide.call(
        ritual, self._addressOf(source), self._addressOf(target),
    )
    return qdesigner_internal.Connection._cuteAt(address)

  @overload(WAIT['qdesigner_internal.Connection'])
  @overload(NoneType)
  def modifyConnection(
      self,
      con: Optional[qdesigner_internal.Connection],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::modifyConnection(Connection *con)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::modifyConnection(Connection
    #      *con)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit16modifyConnectionEPN'
        'S_10ConnectionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit16modifyConnect'
          'ionEPNS_10ConnectionE')
    self.uglySide.call(ritual, self._addressOf(con))

  @overload(WAIT['qdesigner_internal.Connection'])
  @overload(NoneType)
  def addConnection(
      self,
      con: Optional[qdesigner_internal.Connection],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::addConnection(Connection *con)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::addConnection(Connection
    #      *con)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit13addConnectionEPNS_1'
        '0ConnectionE',
        self._addressOf(con),
    )

  @overload(QWidget, QPoint)
  @overload(NoneType, QPoint)
  def endConnection(self, target: Optional[QWidget], pos: QPoint) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::endConnection(QWidget *target, const
    QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    target : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ConnectionEdit::endConnection(QWidget
    #      *target, const QPoint &pos)
    ritual = (
        'ritual_ZN18qdesigner_internal14ConnectionEdit13endConnectionEP7QWi'
        'dgetRK6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ConnectionEdit13endConnection'
          'EP7QWidgetRK6QPoint')
    self.uglySide.call(ritual, self._addressOf(target), self._valueOf(pos))

  @overload(WAIT['qdesigner_internal.Connection'])
  @overload(NoneType)
  def takeConnection(
      self,
      con: Optional[qdesigner_internal.Connection],
  ) -> Optional[qdesigner_internal.Connection]:
    """
    Calls Qt's 'Connection
    *qdesigner_internal::ConnectionEdit::takeConnection(Connection *con)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[qdesigner_internal.Connection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Connection
    #      *qdesigner_internal::ConnectionEdit::takeConnection(Connection
    #      *con)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit14takeConnectionEPNS_'
        '10ConnectionE',
        self._addressOf(con),
    )
    return qdesigner_internal.Connection._cuteAt(address)

  def newlyAddedConnection(self) -> Optional[qdesigner_internal.Connection]:
    """
    Calls Qt's 'Connection
    *qdesigner_internal::ConnectionEdit::newlyAddedConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Returns
    -------

    Optional[qdesigner_internal.Connection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Connection *qdesigner_internal::ConnectionEdit::newlyAddedConnection()
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit20newlyAddedConnectio'
        'nEv',
    )
    return qdesigner_internal.Connection._cuteAt(address)

  def clearNewlyAddedConnection(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::clearNewlyAddedConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html
    """
    #  void qdesigner_internal::ConnectionEdit::clearNewlyAddedConnection()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit25clearNewlyAddedConn'
        'ectionEv',
    )

  @overload(QPoint)
  def findObjectsUnderMouse(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::findObjectsUnderMouse(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ConnectionEdit::findObjectsUnderMouse(const
    #      QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit21findObjectsUnderMou'
        'seERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QWidget, QPoint)
  @overload(NoneType, QPoint)
  def startConnection(self, source: Optional[QWidget], pos: QPoint) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::startConnection(QWidget *source,
    const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    source : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ConnectionEdit::startConnection(QWidget
    #      *source, const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit15startConnectionEP7Q'
        'WidgetRK6QPoint',
        self._addressOf(source), self._valueOf(pos),
    )

  @overload(QWidget, QPoint)
  @overload(NoneType, QPoint)
  def continueConnection(
      self,
      target: Optional[QWidget],
      pos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ConnectionEdit::continueConnection(QWidget *target,
    const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    target : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ConnectionEdit::continueConnection(QWidget
    #      *target, const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit18continueConnectionE'
        'P7QWidgetRK6QPoint',
        self._addressOf(target), self._valueOf(pos),
    )

  def abortConnection(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::abortConnection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html
    """
    #  void qdesigner_internal::ConnectionEdit::abortConnection()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit15abortConnectionEv',
    )

  @overload(qdesigner_internal.CETypes.EndPoint, QPoint)
  def startDrag(
      self,
      end_point: qdesigner_internal.CETypes.EndPoint,
      pos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::startDrag(const
    EndPoint &end_point, const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#startDrag

    Parameters
    ----------

    end_point : qdesigner_internal.CETypes.EndPoint
      Passed on as a value: Qt reads the C++
      qdesigner_internal::CETypes::EndPoint, which stays Python's own.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ConnectionEdit::startDrag(const EndPoint
    #      &end_point, const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit9startDragERKNS_7CETy'
        'pes8EndPointERK6QPoint',
        self._valueOf(end_point), self._valueOf(pos),
    )

  @overload(QPoint)
  def continueDrag(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::continueDrag(const
    QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ConnectionEdit::continueDrag(const QPoint
    #      &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit12continueDragERK6QPo'
        'int',
        self._valueOf(pos),
    )

  @overload(QPoint)
  def endDrag(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::endDrag(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#endDrag

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ConnectionEdit::endDrag(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit7endDragERK6QPoint',
        self._valueOf(pos),
    )

  @overload(qdesigner_internal.CETypes.EndPoint, QPoint)
  def adjustHotSopt(
      self,
      end_point: qdesigner_internal.CETypes.EndPoint,
      pos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::adjustHotSopt(const
    EndPoint &end_point, const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html

    Parameters
    ----------

    end_point : qdesigner_internal.CETypes.EndPoint
      Passed on as a value: Qt reads the C++
      qdesigner_internal::CETypes::EndPoint, which stays Python's own.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ConnectionEdit::adjustHotSopt(const EndPoint
    #      &end_point, const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit13adjustHotSoptERKNS_'
        '7CETypes8EndPointERK6QPoint',
        self._valueOf(end_point), self._valueOf(pos),
    )

  @overload(
      QPainter, qdesigner_internal.CETypes.EndPoint.Type,
      WAIT['qdesigner_internal.Connection'],
  )
  @overload(QPainter, qdesigner_internal.CETypes.EndPoint.Type, NoneType)
  @overload(
      NoneType, qdesigner_internal.CETypes.EndPoint.Type,
      WAIT['qdesigner_internal.Connection'],
  )
  @overload(NoneType, qdesigner_internal.CETypes.EndPoint.Type, NoneType)
  def paintLabel(
      self,
      p: Optional[QPainter],
      type: qdesigner_internal.CETypes.EndPoint.Type,
      con: Optional[qdesigner_internal.Connection],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ConnectionEdit::paintLabel(QPainter
    *p, EndPoint::Type type, Connection *con)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connectionedit.html#paintLabel

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    con : Optional[qdesigner_internal.Connection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ConnectionEdit::paintLabel(QPainter *p,
    #      EndPoint::Type type, Connection *con)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ConnectionEdit10paintLabelEP8QPaint'
        'erNS_7CETypes8EndPoint4TypeEPNS_10ConnectionE',
        self._addressOf(p), type.value, self._addressOf(con),
    )

  @staticmethod
  def background(*__, **_) -> Never:
    """
    Qt's 'const QPointer<QWidget>
    &qdesigner_internal::ConnectionEdit::background() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ConnectionEdit.background' has no cute "
        "function yet. Qt's 'const QPointer<QWidget> "
        "&qdesigner_internal::ConnectionEdit::background() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def connectionList(*__, **_) -> Never:
    """
    Qt's 'const ConnectionList
    &qdesigner_internal::ConnectionEdit::connectionList() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ConnectionEdit.connectionList' has no cute "
        "function yet. Qt's 'const ConnectionList "
        "&qdesigner_internal::ConnectionEdit::connectionList() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def createContextMenu(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::ConnectionEdit::createContextMenu(QMenu
    &menu)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ConnectionEdit.createContextMenu' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::ConnectionEdit::createContextMenu(QMenu "
        "&menu)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def paintConnection(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::ConnectionEdit::paintConnection(QPainter
    *p, Connection *con, WidgetSet *heavy_highlight_set, WidgetSet
    *light_highlight_set) const': names
    'qdesigner_internal::CETypes::WidgetSet', which has no cute class yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ConnectionEdit.paintConnection' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::ConnectionEdit::paintConnection(QPainter *p, "
        "Connection *con, WidgetSet *heavy_highlight_set, WidgetSet "
        "*light_highlight_set) const': names "
        "'qdesigner_internal::CETypes::WidgetSet', which has no cute class "
        "yet.")

  @staticmethod
  def selection(*__, **_) -> Never:
    """
    Qt's 'const ConnectionSet
    &qdesigner_internal::ConnectionEdit::selection() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ConnectionEdit.selection' has no cute function "
        "yet. Qt's 'const ConnectionSet "
        "&qdesigner_internal::ConnectionEdit::selection() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def state(*__, **_) -> Never:
    """
    Qt's 'State qdesigner_internal::ConnectionEdit::state() const': gives the
    enum 'qdesigner_internal::ConnectionEdit::State', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ConnectionEdit.state' has no cute function "
        "yet. Qt's 'State qdesigner_internal::ConnectionEdit::state() "
        "const': gives the enum "
        "'qdesigner_internal::ConnectionEdit::State', whose class cannot be "
        "named here.")
