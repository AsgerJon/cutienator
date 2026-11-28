"""
qdesigner_internal::QDesignerMimeData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_dnditem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerMimeData to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QMimeData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QDrag, QDropEvent
  from ..QtWidgets import QWidget
  from . import QDesignerDnDItemInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerDnDItemInterface = WAIT['QDesignerDnDItemInterface']
  QDrag = WAIT['QDrag']
  QDropEvent = WAIT['QDropEvent']
  QPoint = WAIT['QPoint']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerMimeData(QMimeData):
  """
  The cute side of Qt's qdesigner_internal::QDesignerMimeData: a plain Python
  object standing in front of one C++ qdesigner_internal::QDesignerMimeData.

  It is built on the cute 'QMimeData', as Qt's
  qdesigner_internal::QDesignerMimeData is built on Qt's QMimeData, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerMimeData that has a
  ritual and that Python can call so far, 10 names in all: 'metaObject',
  'tr', 'items', 'execDrag', 'hotSpot', 'moveDecoration',
  'removeMovedWidgetsFromSourceForm', 'acceptEvent', 'acceptEventWithAction',
  'proposedDropAction'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::QDesignerMimeData::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::QDesignerMimeData::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::QDesignerMimeData::~QDesignerMimeData()': the
    destructor: Python never removes a C++
    qdesigner_internal::QDesignerMimeData.
  - Qt's 'void
    qdesigner_internal::QDesignerMimeData::setImageTransparency(QImage
    &image, int alpha)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerMimeData is created at the first
    use, not by 'qdesigner_internal::QDesignerMimeData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QDesignerMimeData.
  - Qt tells when it has removed the C++
    qdesigner_internal::QDesignerMimeData. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's qdesigner_internal::QDesignerMimeData that has no cute
    function yet, 'setImageTransparency', holds a function that raises
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
    Calls Qt's 'QString qdesigner_internal::QDesignerMimeData::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html#tr

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
    #  QString qdesigner_internal::QDesignerMimeData::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal17QDesignerMimeData2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QList[QDesignerDnDItemInterface], QWidget)
  @overload(QList[QDesignerDnDItemInterface], NoneType)
  def execDrag(
      items: QList[QDesignerDnDItemInterface],
      dragSource: Optional[QWidget],
  ) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction
    qdesigner_internal::QDesignerMimeData::execDrag(const QDesignerDnDItems
    &items, QWidget *dragSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html#execDrag

    Parameters
    ----------

    items : QList[QDesignerDnDItemInterface]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    dragSource : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction qdesigner_internal::QDesignerMimeData::execDrag(const
    #      QDesignerDnDItems &items, QWidget *dragSource)
    return Qt.DropAction(Rituals.call(
        'ritual_ZN18qdesigner_internal17QDesignerMimeData8execDragERK5QList'
        'IP25QDesignerDnDItemInterfaceEP7QWidget',
        CuteMixin._valueOf(items), CuteMixin._addressOf(dragSource),
    ))

  @staticmethod
  @overload(QList[QDesignerDnDItemInterface])
  def removeMovedWidgetsFromSourceForm(
      items: QList[QDesignerDnDItemInterface],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerMimeData::removeMovedWidgetsFromSourceForm(
    const QDesignerDnDItems &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html

    Parameters
    ----------

    items : QList[QDesignerDnDItemInterface]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::QDesignerMimeData::
    #      removeMovedWidgetsFromSourceForm(const QDesignerDnDItems &items)
    Rituals.call(
        'ritual_ZN18qdesigner_internal17QDesignerMimeData32removeMovedWidge'
        'tsFromSourceFormERK5QListIP25QDesignerDnDItemInterfaceE',
        CuteMixin._valueOf(items),
    )

  @staticmethod
  @overload(Qt.DropAction, QDropEvent)
  @overload(Qt.DropAction, NoneType)
  def acceptEventWithAction(
      desiredAction: Qt.DropAction,
      e: Optional[QDropEvent],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerMimeData::acceptEventWithAction(Qt::
    DropAction desiredAction, QDropEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html

    Parameters
    ----------

    desiredAction : Qt.DropAction
      Passed on as its number.

    e : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QDesignerMimeData::acceptEventWithAction(Qt::
    #      DropAction desiredAction, QDropEvent *e)
    Rituals.call(
        'ritual_ZN18qdesigner_internal17QDesignerMimeData21acceptEventWithA'
        'ctionEN2Qt10DropActionEP10QDropEvent',
        desiredAction.value, CuteMixin._addressOf(e),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerMimeData'

  #  A C++ qdesigner_internal::QDesignerMimeData Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_QDesignerMimeData'

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
    *qdesigner_internal::QDesignerMimeData::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::QDesignerMimeData::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerMimeData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def items(self) -> QList[QDesignerDnDItemInterface]:
    """
    Calls Qt's 'const QDesignerDnDItems
    &qdesigner_internal::QDesignerMimeData::items() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html#items

    Returns
    -------

    QList[QDesignerDnDItemInterface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QDesignerDnDItems
    #      &qdesigner_internal::QDesignerMimeData::items() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerMimeData5itemsEv',
    )
    from . import QDesignerDnDItemInterface
    return QList[QDesignerDnDItemInterface]._cuteOwning(address)

  def hotSpot(self) -> QPoint:
    """
    Calls Qt's 'QPoint qdesigner_internal::QDesignerMimeData::hotSpot()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html#hotSpot

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint qdesigner_internal::QDesignerMimeData::hotSpot() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerMimeData7hotSpotEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def proposedDropAction(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction
    qdesigner_internal::QDesignerMimeData::proposedDropAction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction
    #      qdesigner_internal::QDesignerMimeData::proposedDropAction() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerMimeData18proposedDropAct'
        'ionEv',
    ))

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

  @overload(QList[QDesignerDnDItemInterface], QDrag)
  @overload(QList[QDesignerDnDItemInterface], NoneType)
  def __init__(
      self,
      items: QList[QDesignerDnDItemInterface],
      drag: Optional[QDrag],
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::QDesignerMimeData::QDesignerMimeData(const
    QDesignerDnDItems &items, QDrag *drag)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html

    Parameters
    ----------

    items : QList[QDesignerDnDItemInterface]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    drag : Optional[QDrag]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::QDesignerMimeData::QDesignerMimeData(const
    #      QDesignerDnDItems &items, QDrag *drag)
    self._noteCreation(QDesignerMimeData, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal17QDesignerMimeDataC1ERK5QListIP25QDe'
        'signerDnDItemInterfaceEP5QDrag',
        self._valueOf(items), self._addressOf(drag),
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

  @overload(QPoint)
  def moveDecoration(self, globalPos: QPoint) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerMimeData::moveDecoration(const QPoint
    &globalPos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html

    Parameters
    ----------

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::QDesignerMimeData::moveDecoration(const
    #      QPoint &globalPos) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerMimeData14moveDecorationE'
        'RK6QPoint',
        self._valueOf(globalPos),
    )

  @overload(QDropEvent)
  @overload(NoneType)
  def acceptEvent(self, e: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerMimeData::acceptEvent(QDropEvent *e) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignermimedata.html

    Parameters
    ----------

    e : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QDesignerMimeData::acceptEvent(QDropEvent *e)
    #      const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17QDesignerMimeData11acceptEventEP10'
        'QDropEvent',
        self._addressOf(e),
    )

  @staticmethod
  def setImageTransparency(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::QDesignerMimeData::setImageTransparency(QImage
    &image, int alpha)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerMimeData.setImageTransparency' has no "
        "cute function yet. Qt's 'void "
        "qdesigner_internal::QDesignerMimeData::setImageTransparency(QImage "
        "&image, int alpha)': takes a type Python has no way to hand over "
        "yet.")
