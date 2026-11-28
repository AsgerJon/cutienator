"""
QLayoutPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlayout_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLayoutPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QSizePolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLayout, QLayoutItem, QSpacerItem, QWidget, QWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLayout = WAIT['QLayout']
  QLayoutItem = WAIT['QLayoutItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLayoutPrivate(QObjectPrivate):
  """
  The cute side of Qt's QLayoutPrivate: a plain Python object standing in
  front of one C++ QLayoutPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QLayoutPrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLayoutPrivate that has a ritual and that Python can
  call so far, 8 names in all: 'q_func', 'doResize', 'reparentChildWidgets',
  'checkWidget', 'checkLayout', 'createWidgetItem', 'createSpacerItem',
  'replaceAt'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QLayout *QLayoutPrivate::q_func() const': takes in Python
    what 'QLayout *QLayoutPrivate::q_func()' takes.
  - Qt's 'void QLayoutPrivate::getMargin(int *result, int userMargin,
    QStyle::PixelMetric pm) const': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QLayoutPrivate is created at the first use, not by
    'QLayoutPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLayoutPrivate.
  - Each name of Qt's QLayoutPrivate that has no cute function yet,
    'getMargin', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QLayout, QWidget)
  @overload(QLayout, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def createWidgetItem(
      layout: Optional[QLayout],
      widget: Optional[QWidget],
  ) -> Optional[QWidgetItem]:
    """
    Calls Qt's 'QWidgetItem *QLayoutPrivate::createWidgetItem(const QLayout
    *layout, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutprivate.html#createWidgetItem

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidgetItem *QLayoutPrivate::createWidgetItem(const QLayout *layout,
    #      QWidget *widget)
    address = Rituals.call(
        'ritual_ZN14QLayoutPrivate16createWidgetItemEPK7QLayoutP7QWidget',
        CuteMixin._addressOf(layout), CuteMixin._addressOf(widget),
    )
    from . import QWidgetItem
    return QWidgetItem._cuteAt(address)

  @staticmethod
  @overload(QLayout, int, int)
  @overload(NoneType, int, int)
  @overload(QLayout, int, int, QSizePolicy.Policy)
  @overload(NoneType, int, int, QSizePolicy.Policy)
  @overload(QLayout, int, int, QSizePolicy.Policy, QSizePolicy.Policy)
  @overload(NoneType, int, int, QSizePolicy.Policy, QSizePolicy.Policy)
  def createSpacerItem(
      layout: Optional[QLayout],
      w: int,
      h: int,
      hPolicy: QSizePolicy.Policy = QSizePolicy.Policy.Minimum,
      vPolicy: QSizePolicy.Policy = QSizePolicy.Policy.Minimum,
  ) -> Optional[QSpacerItem]:
    """
    Calls Qt's 'QSpacerItem *QLayoutPrivate::createSpacerItem(const QLayout
    *layout, int w, int h, QSizePolicy::Policy hPolicy, QSizePolicy::Policy
    vPolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutprivate.html#createSpacerItem

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    w : int
      Passed on as it is.

    h : int
      Passed on as it is.

    hPolicy : QSizePolicy.Policy
      Passed on as its number. May be left out, as in Qt: it is then
      QSizePolicy.Policy.Minimum.

    vPolicy : QSizePolicy.Policy
      Passed on as its number. May be left out, as in Qt: it is then
      QSizePolicy.Policy.Minimum.

    Returns
    -------

    Optional[QSpacerItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSpacerItem *QLayoutPrivate::createSpacerItem(const QLayout *layout,
    #      int w, int h, QSizePolicy::Policy hPolicy, QSizePolicy::Policy
    #      vPolicy)
    address = Rituals.call(
        'ritual_ZN14QLayoutPrivate16createSpacerItemEPK7QLayoutiiN11QSizePo'
        'licy6PolicyES4_',
        CuteMixin._addressOf(layout), w, h, hPolicy.value, vPolicy.value,
    )
    from . import QSpacerItem
    return QSpacerItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLayoutPrivate'

  #  A C++ QLayoutPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLayoutPrivate'

  #  The functions Qt calls itself that QLayoutPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'replaceAt': (
          ('_ZN14QLayoutPrivate9replaceAtEiP11QLayoutItem',
           ('address', 'address', 'QtWidgets:QLayoutItem'),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtWidgets:QLayoutItem'),
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

  @overload(QWidget)
  @overload(NoneType)
  def checkWidget(self, widget: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QLayoutPrivate::checkWidget(QWidget *widget) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutprivate.html#checkWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QLayoutPrivate::checkWidget(QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK14QLayoutPrivate11checkWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QLayout)
  @overload(NoneType)
  def checkLayout(self, otherLayout: Optional[QLayout]) -> bool:
    """
    Calls Qt's 'bool QLayoutPrivate::checkLayout(QLayout *otherLayout)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutprivate.html#checkLayout

    Parameters
    ----------

    otherLayout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QLayoutPrivate::checkLayout(QLayout *otherLayout) const
    return self.uglySide.call(
        'ritual_ZNK14QLayoutPrivate11checkLayoutEP7QLayout',
        self._addressOf(otherLayout),
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QLayoutPrivate::QLayoutPrivate()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutprivate.html#QLayoutPrivate
    """
    #  QLayoutPrivate::QLayoutPrivate()
    self._noteCreation(QLayoutPrivate, lambda: Rituals.call(
        'ritual_ZN14QLayoutPrivateC1Ev',
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

  def q_func(self) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *QLayoutPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutprivate.html#q_func

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *QLayoutPrivate::q_func()
    address = self.uglySide.call('ritual_ZN14QLayoutPrivate6q_funcEv')
    from . import QLayout
    return QLayout._cuteAt(address)

  def doResize(self) -> None:
    """
    Calls Qt's 'void QLayoutPrivate::doResize()'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutprivate.html#doResize
    """
    #  void QLayoutPrivate::doResize()
    self.uglySide.call('ritual_ZN14QLayoutPrivate8doResizeEv')

  @overload(QWidget)
  @overload(NoneType)
  def reparentChildWidgets(self, mw: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QLayoutPrivate::reparentChildWidgets(QWidget *mw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlayoutprivate.html#reparentChildWidgets

    Parameters
    ----------

    mw : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLayoutPrivate::reparentChildWidgets(QWidget *mw)
    self.uglySide.call(
        'ritual_ZN14QLayoutPrivate20reparentChildWidgetsEP7QWidget',
        self._addressOf(mw),
    )

  @overload(int, QLayoutItem)
  @overload(int, NoneType)
  def replaceAt(
      self,
      a0: int,
      a1: Optional[QLayoutItem],
  ) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QLayoutPrivate::replaceAt(int a0, QLayoutItem
    *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qlayoutprivate.html#replaceAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QLayoutPrivate::replaceAt(int a0, QLayoutItem *a1)
    ritual = 'ritual_ZN14QLayoutPrivate9replaceAtEiP11QLayoutItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QLayoutPrivate9replaceAtEiP11QLayoutItem'
    address = self.uglySide.call(
        ritual, a0, self._addressOf(a1, 'QLayoutItem'),
    )
    from . import QLayoutItem
    return QLayoutItem._cuteAt(address)

  @staticmethod
  def getMargin(*__, **_) -> Never:
    """
    Qt's 'void QLayoutPrivate::getMargin(int *result, int userMargin,
    QStyle::PixelMetric pm) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QLayoutPrivate.getMargin' has no cute function yet. Qt's 'void "
        "QLayoutPrivate::getMargin(int *result, int userMargin, "
        "QStyle::PixelMetric pm) const': takes a number to change where it "
        "is.")
