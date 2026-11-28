"""
qdesigner_internal::Layout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/layout_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means qdesigner_internal::Layout to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QLayout, QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QLayout = WAIT['QLayout']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Layout(QObject):
  """
  The cute side of Qt's qdesigner_internal::Layout: a plain Python object
  standing in front of one C++ qdesigner_internal::Layout.

  It is built on the cute 'QObject', as Qt's qdesigner_internal::Layout is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::Layout that has a ritual and
  that Python can call so far, 17 names in all: 'metaObject', 'tr',
  'createLayout', 'sort', 'doLayout', 'setup', 'undoLayout', 'breakLayout',
  'widgets', 'parentWidget', 'layoutBaseWidget', 'reparentLayoutWidget',
  'setReparentLayoutWidget', 'finishLayout', 'setWidgets',
  'reparentToLayoutBase', 'widgetDestroyed'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::Layout::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::Layout::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::Layout::~Layout()': the destructor: Python
    never removes a C++ qdesigner_internal::Layout.
  - Qt's 'bool qdesigner_internal::Layout::prepareLayout(bool &needMove, bool
    &needReparent)': takes a number to change where it is.

  What has no ritual
  ------------------

  6 of the 29 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::Layout is created at the first use, not by
    'qdesigner_internal::Layout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::Layout.
  - Qt tells when it has removed the C++ qdesigner_internal::Layout. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::Layout that has no cute function
    yet, 'prepareLayout', holds a function that raises 'NotImplementedError',
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
    Calls Qt's 'QString qdesigner_internal::Layout::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesigner_internal-layout.html#tr

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
    #  QString qdesigner_internal::Layout::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal6Layout2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(
      QList[QWidget], QWidget, QDesignerFormWindowInterface, QWidget,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], QWidget, QDesignerFormWindowInterface, NoneType,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], QWidget, NoneType, QWidget,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], QWidget, NoneType, NoneType,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], NoneType, QDesignerFormWindowInterface, QWidget,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], NoneType, QDesignerFormWindowInterface, NoneType,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], NoneType, NoneType, QWidget,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], NoneType, NoneType, NoneType,
      qdesigner_internal.LayoutInfo.Type,
  )
  def createLayout(
      widgets: QList[QWidget],
      parentWidget: Optional[QWidget],
      fw: Optional[QDesignerFormWindowInterface],
      layoutBase: Optional[QWidget],
      layoutType: qdesigner_internal.LayoutInfo.Type,
  ) -> Optional[Layout]:
    """
    Calls Qt's 'Layout *qdesigner_internal::Layout::createLayout(const
    QWidgetList &widgets, QWidget *parentWidget, QDesignerFormWindowInterface
    *fw, QWidget *layoutBase, LayoutInfo::Type layoutType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#createLayout

    Parameters
    ----------

    widgets : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layoutBase : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layoutType : qdesigner_internal.LayoutInfo.Type
      Passed on as its number.

    Returns
    -------

    Optional[Layout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Layout *qdesigner_internal::Layout::createLayout(const QWidgetList
    #      &widgets, QWidget *parentWidget, QDesignerFormWindowInterface *fw,
    #      QWidget *layoutBase, LayoutInfo::Type layoutType)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal6Layout12createLayoutERK5QListIP7QWid'
        'getES3_P28QDesignerFormWindowInterfaceS3_NS_10LayoutInfo4TypeE',
        CuteMixin._valueOf(widgets), CuteMixin._addressOf(parentWidget),
        CuteMixin._addressOf(fw), CuteMixin._addressOf(layoutBase),
        layoutType.value,
    )
    return Layout._cuteAt(address)

  @overload(int)
  def createLayout(self, type: int) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout *qdesigner_internal::Layout::createLayout(int type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#createLayout

    Parameters
    ----------

    type : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *qdesigner_internal::Layout::createLayout(int type)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal6Layout12createLayoutEi', type,
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::Layout'

  #  A C++ qdesigner_internal::Layout Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_Layout'

  #  The functions Qt calls itself that qdesigner_internal::Layout is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'prepareLayout': (
          'bool qdesigner_internal::Layout::prepareLayout(bool &, bool &)',
      ),
  }

  #  The functions Qt calls itself that qdesigner_internal::Layout is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'sort': (
          ('_ZN18qdesigner_internal6Layout4sortEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'doLayout': (
          ('_ZN18qdesigner_internal6Layout8doLayoutEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setup': (
          ('_ZN18qdesigner_internal6Layout5setupEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'undoLayout': (
          ('_ZN18qdesigner_internal6Layout10undoLayoutEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'breakLayout': (
          ('_ZN18qdesigner_internal6Layout11breakLayoutEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'finishLayout': (
          ('_ZN18qdesigner_internal6Layout12finishLayoutEbP7QLayout',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
               ('address', 'address', 'QtWidgets:QLayout'),
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
    Calls Qt's 'const QMetaObject *qdesigner_internal::Layout::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::Layout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal6Layout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def widgets(self) -> QList[QWidget]:
    """
    Calls Qt's 'const QWidgetList &qdesigner_internal::Layout::widgets()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#widgets

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QWidgetList &qdesigner_internal::Layout::widgets() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal6Layout7widgetsEv',
    )
    from ..QtWidgets import QWidget
    return QList[QWidget]._cuteOwning(address)

  def parentWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::Layout::parentWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#parentWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::Layout::parentWidget() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal6Layout12parentWidgetEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def layoutBaseWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::Layout::layoutBaseWidget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#layoutBaseWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::Layout::layoutBaseWidget() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal6Layout16layoutBaseWidgetEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def reparentLayoutWidget(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::Layout::reparentLayoutWidget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html
    """
    #  bool qdesigner_internal::Layout::reparentLayoutWidget() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal6Layout20reparentLayoutWidgetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setReparentLayoutWidget(self, v: bool) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Layout::setReparentLayoutWidget(bool
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::Layout::setReparentLayoutWidget(bool v)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal6Layout23setReparentLayoutWidgetEb', v,
    )

  @overload(QList[QWidget])
  def setWidgets(self, widgets: QList[QWidget]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Layout::setWidgets(const QWidgetList
    &widgets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#setWidgets

    Parameters
    ----------

    widgets : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::Layout::setWidgets(const QWidgetList
    #      &widgets)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal6Layout10setWidgetsERK5QListIP7QWidge'
        'tE',
        self._valueOf(widgets),
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

  @overload(
      QList[QWidget], QWidget, QDesignerFormWindowInterface, QWidget,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], QWidget, QDesignerFormWindowInterface, NoneType,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], QWidget, NoneType, QWidget,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], QWidget, NoneType, NoneType,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], NoneType, QDesignerFormWindowInterface, QWidget,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], NoneType, QDesignerFormWindowInterface, NoneType,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], NoneType, NoneType, QWidget,
      qdesigner_internal.LayoutInfo.Type,
  )
  @overload(
      QList[QWidget], NoneType, NoneType, NoneType,
      qdesigner_internal.LayoutInfo.Type,
  )
  def __init__(
      self,
      wl: QList[QWidget],
      p: Optional[QWidget],
      fw: Optional[QDesignerFormWindowInterface],
      lb: Optional[QWidget],
      layoutType: qdesigner_internal.LayoutInfo.Type,
  ) -> None:
    """
    Notes what was given, for Qt's 'qdesigner_internal::Layout::Layout(const
    QWidgetList &wl, QWidget *p, QDesignerFormWindowInterface *fw, QWidget
    *lb, LayoutInfo::Type layoutType)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#Layout

    Parameters
    ----------

    wl : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    p : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    lb : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layoutType : qdesigner_internal.LayoutInfo.Type
      Passed on as its number.
    """
    #  qdesigner_internal::Layout::Layout(const QWidgetList &wl, QWidget *p,
    #      QDesignerFormWindowInterface *fw, QWidget *lb, LayoutInfo::Type
    #      layoutType)
    self._noteCreation(Layout, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal6LayoutC1ERK5QListIP7QWidgetES3_P28QD'
        'esignerFormWindowInterfaceS3_NS_10LayoutInfo4TypeE',
        self._valueOf(wl), self._addressOf(p), self._addressOf(fw),
        self._addressOf(lb), layoutType.value,
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

  def sort(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Layout::sort()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#sort
    """
    #  void qdesigner_internal::Layout::sort()
    self.uglySide.call('ritual_ZN18qdesigner_internal6Layout4sortEv')

  def doLayout(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Layout::doLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#doLayout
    """
    #  void qdesigner_internal::Layout::doLayout()
    self.uglySide.call('ritual_ZN18qdesigner_internal6Layout8doLayoutEv')

  def setup(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Layout::setup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#setup
    """
    #  void qdesigner_internal::Layout::setup()
    ritual = 'ritual_ZN18qdesigner_internal6Layout5setupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal6Layout5setupEv'
    self.uglySide.call(ritual)

  def undoLayout(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Layout::undoLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#undoLayout
    """
    #  void qdesigner_internal::Layout::undoLayout()
    ritual = 'ritual_ZN18qdesigner_internal6Layout10undoLayoutEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal6Layout10undoLayoutEv'
    self.uglySide.call(ritual)

  def breakLayout(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Layout::breakLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#breakLayout
    """
    #  void qdesigner_internal::Layout::breakLayout()
    ritual = 'ritual_ZN18qdesigner_internal6Layout11breakLayoutEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal6Layout11breakLayoutEv'
    self.uglySide.call(ritual)

  @overload(bool)
  @overload(bool, QLayout)
  @overload(bool, NoneType)
  def finishLayout(
      self,
      needMove: bool,
      layout: Optional[QLayout] = None,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Layout::finishLayout(bool needMove,
    QLayout *layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#finishLayout

    Parameters
    ----------

    needMove : bool
      Passed on as it is.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void qdesigner_internal::Layout::finishLayout(bool needMove, QLayout
    #      *layout)
    ritual = 'ritual_ZN18qdesigner_internal6Layout12finishLayoutEbP7QLayout'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal6Layout12finishLayoutEbP7QLayou'
          't')
    self.uglySide.call(ritual, needMove, self._addressOf(layout))

  @overload(QWidget)
  @overload(NoneType)
  def reparentToLayoutBase(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Layout::reparentToLayoutBase(QWidget
    *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::Layout::reparentToLayoutBase(QWidget *w)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal6Layout20reparentToLayoutBaseEP7QWidg'
        'et',
        self._addressOf(w),
    )

  def widgetDestroyed(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::Layout::widgetDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layout.html#widgetDestroyed
    """
    #  void qdesigner_internal::Layout::widgetDestroyed()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal6Layout15widgetDestroyedEv',
    )

  @staticmethod
  def prepareLayout(*__, **_) -> Never:
    """
    Qt's 'bool qdesigner_internal::Layout::prepareLayout(bool &needMove, bool
    &needReparent)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.Layout.prepareLayout' has no cute function "
        "yet. Qt's 'bool qdesigner_internal::Layout::prepareLayout(bool "
        "&needMove, bool &needReparent)': takes a number to change where it "
        "is.")
