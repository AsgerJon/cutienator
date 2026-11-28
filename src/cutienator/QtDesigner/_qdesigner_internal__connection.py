"""
qdesigner_internal::Connection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/connectionedit_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::Connection to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QPoint, QRect
  from ..QtGui import QPainter, QPixmap, QRegion
  from ..QtWidgets import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Connection(qdesigner_internal.CETypes):
  """
  The cute side of Qt's qdesigner_internal::Connection: a plain Python object
  standing in front of one C++ qdesigner_internal::Connection.

  It is built on the cute 'qdesigner_internal::CETypes', as Qt's
  qdesigner_internal::Connection is built on Qt's
  qdesigner_internal::CETypes, and has everything that class has.

  C++ hands a qdesigner_internal::Connection around as a copy, so every C++
  qdesigner_internal::Connection behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::Connection that has a ritual and
  that Python can call so far, 28 names in all: 'object', 'widget',
  'endPointPos', 'endPointRect', 'setEndPoint', 'isVisible',
  'updateVisibility', 'setVisible', 'region', 'contains', 'paint', 'update',
  'checkWidgets', 'label', 'setLabel', 'labelRect', 'labelPixmap', 'edit',
  'inserted', 'removed', 'setSource', 'setTarget', 'updateKneeList',
  'trimLine', 'updatePixmap', 'labelDir', 'ground', 'groundRect'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::Connection::~Connection()': the destructor:
    Python removes its C++ qdesigner_internal::Connection by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::Connection is created at the first use, not
    by 'qdesigner_internal::Connection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::Connection back gives a copy the
    ritual made for Python, in a new cute qdesigner_internal::Connection.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::Connection'

  #  A C++ qdesigner_internal::Connection Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_Connection'

  #  The functions Qt calls itself that qdesigner_internal::Connection is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'updateVisibility': (
          ('_ZN18qdesigner_internal10Connection16updateVisibilityEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'region': (
          ('_ZNK18qdesigner_internal10Connection6regionEv',
           ('address', 'value', 'QtGui:QRegion'),
           ()),
      ),
      'paint': (
          ('_ZNK18qdesigner_internal10Connection5paintEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'inserted': (
          ('_ZN18qdesigner_internal10Connection8insertedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'removed': (
          ('_ZN18qdesigner_internal10Connection7removedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Qt's '~qdesigner_internal::Connection()'. Naming it makes this a value
  #  class: Python owns every C++ qdesigner_internal::Connection behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal10ConnectionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(qdesigner_internal.CETypes.EndPoint.Type)
  def object(
      self,
      type: qdesigner_internal.CETypes.EndPoint.Type,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *qdesigner_internal::Connection::object(EndPoint::Type type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#object

    Parameters
    ----------

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *qdesigner_internal::Connection::object(EndPoint::Type type)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection6objectENS_7CETypes8EndP'
        'oint4TypeE',
        type.value,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(qdesigner_internal.CETypes.EndPoint.Type)
  def widget(
      self,
      type: qdesigner_internal.CETypes.EndPoint.Type,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::Connection::widget(EndPoint::Type type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#widget

    Parameters
    ----------

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::Connection::widget(EndPoint::Type type)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection6widgetENS_7CETypes8EndP'
        'oint4TypeE',
        type.value,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(qdesigner_internal.CETypes.EndPoint.Type)
  def endPointPos(
      self,
      type: qdesigner_internal.CETypes.EndPoint.Type,
  ) -> QPoint:
    """
    Calls Qt's 'QPoint
    qdesigner_internal::Connection::endPointPos(EndPoint::Type type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#endPointPos

    Parameters
    ----------

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint qdesigner_internal::Connection::endPointPos(EndPoint::Type
    #      type) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection11endPointPosENS_7CEType'
        's8EndPoint4TypeE',
        type.value,
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(qdesigner_internal.CETypes.EndPoint.Type)
  def endPointRect(
      self,
      a0: qdesigner_internal.CETypes.EndPoint.Type,
  ) -> QRect:
    """
    Calls Qt's 'QRect
    qdesigner_internal::Connection::endPointRect(EndPoint::Type a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#endPointRect

    Parameters
    ----------

    a0 : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect qdesigner_internal::Connection::endPointRect(EndPoint::Type a0)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection12endPointRectENS_7CETyp'
        'es8EndPoint4TypeE',
        a0.value,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::Connection::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#isVisible
    """
    #  bool qdesigner_internal::Connection::isVisible() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection9isVisibleEv',
    )

  def region(self) -> QRegion:
    """
    Calls Qt's 'QRegion qdesigner_internal::Connection::region() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#region

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion qdesigner_internal::Connection::region() const
    ritual = 'ritual_ZNK18qdesigner_internal10Connection6regionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18qdesigner_internal10Connection6regionEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  @overload(QPoint)
  def contains(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::Connection::contains(const QPoint
    &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#contains

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool qdesigner_internal::Connection::contains(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection8containsERK6QPoint',
        self._valueOf(pos),
    )

  @overload(qdesigner_internal.CETypes.EndPoint.Type)
  def label(self, type: qdesigner_internal.CETypes.EndPoint.Type) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::Connection::label(EndPoint::Type
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#label

    Parameters
    ----------

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::Connection::label(EndPoint::Type type)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection5labelENS_7CETypes8EndPo'
        'int4TypeE',
        type.value,
    )

  @overload(qdesigner_internal.CETypes.EndPoint.Type)
  def labelRect(
      self,
      type: qdesigner_internal.CETypes.EndPoint.Type,
  ) -> QRect:
    """
    Calls Qt's 'QRect
    qdesigner_internal::Connection::labelRect(EndPoint::Type type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#labelRect

    Parameters
    ----------

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect qdesigner_internal::Connection::labelRect(EndPoint::Type type)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection9labelRectENS_7CETypes8E'
        'ndPoint4TypeE',
        type.value,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(qdesigner_internal.CETypes.EndPoint.Type)
  def labelPixmap(
      self,
      type: qdesigner_internal.CETypes.EndPoint.Type,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    qdesigner_internal::Connection::labelPixmap(EndPoint::Type type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#labelPixmap

    Parameters
    ----------

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap qdesigner_internal::Connection::labelPixmap(EndPoint::Type
    #      type) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection11labelPixmapENS_7CEType'
        's8EndPoint4TypeE',
        type.value,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def edit(self) -> Optional[qdesigner_internal.ConnectionEdit]:
    """
    Calls Qt's 'ConnectionEdit *qdesigner_internal::Connection::edit()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#edit

    Returns
    -------

    Optional[qdesigner_internal.ConnectionEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ConnectionEdit *qdesigner_internal::Connection::edit() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection4editEv',
    )
    return qdesigner_internal.ConnectionEdit._cuteAt(address)

  @overload(qdesigner_internal.CETypes.EndPoint.Type)
  def labelDir(
      self,
      type: qdesigner_internal.CETypes.EndPoint.Type,
  ) -> qdesigner_internal.CETypes.LineDir:
    """
    Calls Qt's 'LineDir
    qdesigner_internal::Connection::labelDir(EndPoint::Type type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#labelDir

    Parameters
    ----------

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    Returns
    -------

    qdesigner_internal.CETypes.LineDir
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'qdesigner_internal.CETypes.LineDir(number)' gives.
    """
    #  LineDir qdesigner_internal::Connection::labelDir(EndPoint::Type type)
    #      const
    return qdesigner_internal.CETypes.LineDir(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection8labelDirENS_7CETypes8En'
        'dPoint4TypeE',
        type.value,
    ))

  def ground(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::Connection::ground() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#ground
    """
    #  bool qdesigner_internal::Connection::ground() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection6groundEv',
    )

  def groundRect(self) -> QRect:
    """
    Calls Qt's 'QRect qdesigner_internal::Connection::groundRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#groundRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect qdesigner_internal::Connection::groundRect() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection10groundRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(qdesigner_internal.CETypes.EndPoint.Type, QObject, QPoint)
  @overload(qdesigner_internal.CETypes.EndPoint.Type, NoneType, QPoint)
  def setEndPoint(
      self,
      type: qdesigner_internal.CETypes.EndPoint.Type,
      w: Optional[QObject],
      pos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::Connection::setEndPoint(EndPoint::Type type, QObject
    *w, const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#setEndPoint

    Parameters
    ----------

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    w : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::Connection::setEndPoint(EndPoint::Type type,
    #      QObject *w, const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10Connection11setEndPointENS_7CETypes'
        '8EndPoint4TypeEP7QObjectRK6QPoint',
        type.value, self._addressOf(w, 'QObject'), self._valueOf(pos),
    )

  @overload(bool)
  def setVisible(self, b: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::setVisible(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#setVisible

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::Connection::setVisible(bool b)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10Connection10setVisibleEb', b,
    )

  @overload(qdesigner_internal.CETypes.EndPoint.Type, str)
  def setLabel(
      self,
      type: qdesigner_internal.CETypes.EndPoint.Type,
      text: str,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::setLabel(EndPoint::Type
    type, const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#setLabel

    Parameters
    ----------

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::Connection::setLabel(EndPoint::Type type,
    #      const QString &text)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10Connection8setLabelENS_7CETypes8End'
        'Point4TypeERK7QString',
        type.value, text,
    )

  @overload(QObject, QPoint)
  @overload(NoneType, QPoint)
  def setSource(self, source: Optional[QObject], pos: QPoint) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::setSource(QObject
    *source, const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#setSource

    Parameters
    ----------

    source : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::Connection::setSource(QObject *source, const
    #      QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10Connection9setSourceEP7QObjectRK6QP'
        'oint',
        self._addressOf(source, 'QObject'), self._valueOf(pos),
    )

  @overload(QObject, QPoint)
  @overload(NoneType, QPoint)
  def setTarget(self, target: Optional[QObject], pos: QPoint) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::setTarget(QObject
    *target, const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#setTarget

    Parameters
    ----------

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::Connection::setTarget(QObject *target, const
    #      QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10Connection9setTargetEP7QObjectRK6QP'
        'oint',
        self._addressOf(target, 'QObject'), self._valueOf(pos),
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

  @overload(WAIT['qdesigner_internal.ConnectionEdit'])
  @overload(NoneType)
  def __init__(
      self,
      edit: Optional[qdesigner_internal.ConnectionEdit],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::Connection::Connection(ConnectionEdit *edit)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#Connection

    Parameters
    ----------

    edit : Optional[qdesigner_internal.ConnectionEdit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::Connection::Connection(ConnectionEdit *edit)
    self._noteCreation(Connection, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal10ConnectionC1EPNS_14ConnectionEditE',
        self._addressOf(edit),
    ))

  @overload(WAIT['qdesigner_internal.ConnectionEdit'], QObject, QObject)
  @overload(WAIT['qdesigner_internal.ConnectionEdit'], QObject, NoneType)
  @overload(WAIT['qdesigner_internal.ConnectionEdit'], NoneType, QObject)
  @overload(WAIT['qdesigner_internal.ConnectionEdit'], NoneType, NoneType)
  @overload(NoneType, QObject, QObject)
  @overload(NoneType, QObject, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      edit: Optional[qdesigner_internal.ConnectionEdit],
      source: Optional[QObject],
      target: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::Connection::Connection(ConnectionEdit *edit, QObject
    *source, QObject *target)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#Connection

    Parameters
    ----------

    edit : Optional[qdesigner_internal.ConnectionEdit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    source : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::Connection::Connection(ConnectionEdit *edit,
    #      QObject *source, QObject *target)
    self._noteCreation(Connection, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal10ConnectionC1EPNS_14ConnectionEditEP'
        '7QObjectS4_',
        self._addressOf(edit), self._addressOf(source, 'QObject'),
        self._addressOf(target, 'QObject'),
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

  def updateVisibility(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::updateVisibility()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html
    """
    #  void qdesigner_internal::Connection::updateVisibility()
    ritual = 'ritual_ZN18qdesigner_internal10Connection16updateVisibilityEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal10Connection16updateVisibilityE'
          'v')
    self.uglySide.call(ritual)

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, p: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::paint(QPainter *p)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#paint

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::Connection::paint(QPainter *p) const
    ritual = 'ritual_ZNK18qdesigner_internal10Connection5paintEP8QPainter'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal10Connection5paintEP8QPainter')
    self.uglySide.call(ritual, self._addressOf(p))

  @overload()
  @overload(bool)
  def update(self, update_widgets: bool = True) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::update(bool
    update_widgets) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#update

    Parameters
    ----------

    update_widgets : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void qdesigner_internal::Connection::update(bool update_widgets) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10Connection6updateEb',
        update_widgets,
    )

  def checkWidgets(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::checkWidgets()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#checkWidgets
    """
    #  void qdesigner_internal::Connection::checkWidgets()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10Connection12checkWidgetsEv',
    )

  def inserted(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::inserted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#inserted
    """
    #  void qdesigner_internal::Connection::inserted()
    ritual = 'ritual_ZN18qdesigner_internal10Connection8insertedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal10Connection8insertedEv'
    self.uglySide.call(ritual)

  def removed(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::removed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#removed
    """
    #  void qdesigner_internal::Connection::removed()
    ritual = 'ritual_ZN18qdesigner_internal10Connection7removedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal10Connection7removedEv'
    self.uglySide.call(ritual)

  def updateKneeList(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::updateKneeList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#updateKneeList
    """
    #  void qdesigner_internal::Connection::updateKneeList()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10Connection14updateKneeListEv',
    )

  def trimLine(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Connection::trimLine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#trimLine
    """
    #  void qdesigner_internal::Connection::trimLine()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10Connection8trimLineEv',
    )

  @overload(qdesigner_internal.CETypes.EndPoint.Type)
  def updatePixmap(
      self,
      type: qdesigner_internal.CETypes.EndPoint.Type,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::Connection::updatePixmap(EndPoint::Type type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-connection.html#updatePixmap

    Parameters
    ----------

    type : qdesigner_internal.CETypes.EndPoint.Type
      Passed on as its number.
    """
    #  void qdesigner_internal::Connection::updatePixmap(EndPoint::Type type)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10Connection12updatePixmapENS_7CEType'
        's8EndPoint4TypeE',
        type.value,
    )
