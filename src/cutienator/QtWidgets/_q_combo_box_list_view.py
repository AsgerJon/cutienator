"""
QComboBoxListView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QComboBoxListView to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QListView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPaintEvent, QResizeEvent
  from . import QStyleOptionViewItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QComboBoxListView(QListView):
  """
  The cute side of Qt's QComboBoxListView: a plain Python object standing in
  front of one C++ QComboBoxListView.

  It is built on the cute 'QListView', as Qt's QComboBoxListView is built on
  Qt's QListView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QComboBoxListView that has a ritual and that Python
  can call so far, 4 names in all: 'metaObject', 'resizeEvent',
  'initViewItemOption', 'paintEvent'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QComboBoxListView::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QComboBoxListView::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QComboBoxListView::~QComboBoxListView()': the destructor: Python
    never removes a C++ QComboBoxListView.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 2 leans on
  'QComboBoxListView.

  What to expect
  --------------

  - The C++ QComboBoxListView is created at the first use, not by
    'QComboBoxListView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QComboBoxListView.
  - Qt tells when it has removed the C++ QComboBoxListView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QComboBoxListView that has no cute function yet,
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
  __qt_class__ = 'QComboBoxListView'

  #  A C++ QComboBoxListView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QComboBoxListView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QComboBoxListView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxlistview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QComboBoxListView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QComboBoxListView10metaObjectEv',
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
    Qt's 'QComboBoxListView::QComboBoxListView(QComboBox *cmb)': leans on
    'QComboBoxListView::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxListView.__init__' has no cute function yet. Qt's "
        "'QComboBoxListView::QComboBoxListView(QComboBox *cmb)': leans on "
        "'QComboBoxListView::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxListView::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxlistview.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxListView::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN17QComboBoxListView11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QComboBoxListView11resizeEventEP12QResizeEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QStyleOptionViewItem)
  @overload(NoneType)
  def initViewItemOption(
      self,
      option: Optional[QStyleOptionViewItem],
  ) -> None:
    """
    Calls Qt's 'void
    QComboBoxListView::initViewItemOption(QStyleOptionViewItem *option)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxlistview.html#initViewItemOption

    Parameters
    ----------

    option : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxListView::initViewItemOption(QStyleOptionViewItem
    #      *option) const
    ritual = (
        'ritual_ZNK17QComboBoxListView18initViewItemOptionEP20QStyleOptionV'
        'iewItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QComboBoxListView18initViewItemOptionEP20QStyleO'
          'ptionViewItem')
    self.uglySide.call(ritual, self._addressOf(option))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxListView::paintEvent(QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcomboboxlistview.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxListView::paintEvent(QPaintEvent *e)
    ritual = 'ritual_ZN17QComboBoxListView10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QComboBoxListView10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(e))
