"""
QDockWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qdockwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QAction, QCloseEvent, QPaintEvent
  from . import QStyleOptionDockWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCloseEvent = WAIT['QCloseEvent']
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QStyleOptionDockWidget = WAIT['QStyleOptionDockWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDockWidget(QWidget):
  """
  The cute side of Qt's QDockWidget: a plain Python object standing in front
  of one C++ QDockWidget.

  It is built on the cute 'QWidget', as Qt's QDockWidget is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDockWidget that has a ritual and that Python can
  call so far, 21 names in all: 'metaObject', 'tr', 'widget', 'setWidget',
  'setFeatures', 'features', 'setFloating', 'isFloating', 'setAllowedAreas',
  'allowedAreas', 'setTitleBarWidget', 'titleBarWidget', 'setDockLocation',
  'dockLocation', 'isAreaAllowed', 'toggleViewAction', 'changeEvent',
  'closeEvent', 'paintEvent', 'event', 'initStyleOption'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDockWidget::~QDockWidget()': the destructor: Python never removes
    a C++ QDockWidget.
  - Qt's 'QDebug operator<<(QDebug dbg, const QDockWidget *dockWidget)': an
    operator between other classes, written inside this one.

  What has no ritual
  ------------------

  13 of the 38 functions Qt declares: 5 a signal; 4 takes or gives a type
  that cannot be passed yet; 2 forbidden; 1 a template; 1 declared and
  nowhere to be found.

  What to expect
  --------------

  - The C++ QDockWidget is created at the first use, not by
    'QDockWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDockWidget.
  - Qt tells when it has removed the C++ QDockWidget. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QDockWidget, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class DockWidgetFeature(CuteFlags):
    """
    The flags enum 'QDockWidget::DockWidgetFeature' of Qt, with the 7 names
    Qt gives in it. Qt names the type of its combinations
    'QDockWidget::DockWidgetFeatures'.
    """

    DockWidgetClosable = 0x1
    DockWidgetMovable = 0x2
    DockWidgetFloatable = 0x4
    DockWidgetVerticalTitleBar = 0x8
    DockWidgetFeatureMask = 0xf
    NoDockWidgetFeatures = 0x0
    Reserved = 0xff

  DockWidgetFeatures = DockWidgetFeature

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
    Calls Qt's 'QString QDockWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#tr

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
    #  QString QDockWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QDockWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDockWidget'

  #  A C++ QDockWidget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDockWidget'

  #  The functions Qt calls itself that QDockWidget is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK11QDockWidget15initStyleOptionEP22QStyleOptionDockWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionDockWidget'),
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
    Calls Qt's 'const QMetaObject *QDockWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDockWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QDockWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDockWidget::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDockWidget::widget() const
    address = self.uglySide.call('ritual_ZNK11QDockWidget6widgetEv')
    return QWidget._cuteAt(address)

  def features(self) -> DockWidgetFeatures:
    """
    Calls Qt's 'DockWidgetFeatures QDockWidget::features() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#features

    Returns
    -------

    DockWidgetFeatures
      The value standing for the combination Qt gave back.
    """
    #  DockWidgetFeatures QDockWidget::features() const
    return QDockWidget.DockWidgetFeatures(self.uglySide.call(
        'ritual_ZNK11QDockWidget8featuresEv',
    ))

  def isFloating(self) -> bool:
    """
    Calls Qt's 'bool QDockWidget::isFloating() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#isFloating
    """
    #  bool QDockWidget::isFloating() const
    return self.uglySide.call('ritual_ZNK11QDockWidget10isFloatingEv')

  def allowedAreas(self) -> Qt.DockWidgetAreas:
    """
    Calls Qt's 'Qt::DockWidgetAreas QDockWidget::allowedAreas() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#allowedAreas

    Returns
    -------

    Qt.DockWidgetAreas
      The value standing for the combination Qt gave back.
    """
    #  Qt::DockWidgetAreas QDockWidget::allowedAreas() const
    return Qt.DockWidgetAreas(self.uglySide.call(
        'ritual_ZNK11QDockWidget12allowedAreasEv',
    ))

  def titleBarWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDockWidget::titleBarWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#titleBarWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDockWidget::titleBarWidget() const
    address = self.uglySide.call('ritual_ZNK11QDockWidget14titleBarWidgetEv')
    return QWidget._cuteAt(address)

  def dockLocation(self) -> Qt.DockWidgetArea:
    """
    Calls Qt's 'Qt::DockWidgetArea QDockWidget::dockLocation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#dockLocation

    Returns
    -------

    Qt.DockWidgetArea
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.DockWidgetArea(number)' gives.
    """
    #  Qt::DockWidgetArea QDockWidget::dockLocation() const
    return Qt.DockWidgetArea(self.uglySide.call(
        'ritual_ZNK11QDockWidget12dockLocationEv',
    ))

  @overload(Qt.DockWidgetArea)
  def isAreaAllowed(self, area: Qt.DockWidgetArea) -> bool:
    """
    Calls Qt's 'bool QDockWidget::isAreaAllowed(Qt::DockWidgetArea area)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#isAreaAllowed

    Parameters
    ----------

    area : Qt.DockWidgetArea
      Passed on as its number.
    """
    #  bool QDockWidget::isAreaAllowed(Qt::DockWidgetArea area) const
    return self.uglySide.call(
        'ritual_ZNK11QDockWidget13isAreaAllowedEN2Qt14DockWidgetAreaE',
        area.value,
    )

  def toggleViewAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDockWidget::toggleViewAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#toggleViewAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDockWidget::toggleViewAction() const
    address = self.uglySide.call(
        'ritual_ZNK11QDockWidget16toggleViewActionEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDockWidget::setWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#setWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidget::setWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QDockWidget9setWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(DockWidgetFeatures)
  def setFeatures(self, features: DockWidgetFeatures) -> None:
    """
    Calls Qt's 'void QDockWidget::setFeatures(DockWidgetFeatures features)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#setFeatures

    Parameters
    ----------

    features : DockWidgetFeatures
      Passed on as its number.
    """
    #  void QDockWidget::setFeatures(DockWidgetFeatures features)
    self.uglySide.call(
        'ritual_ZN11QDockWidget11setFeaturesE6QFlagsINS_17DockWidgetFeature'
        'EE',
        features.value,
    )

  @overload(bool)
  def setFloating(self, floating: bool) -> None:
    """
    Calls Qt's 'void QDockWidget::setFloating(bool floating)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#setFloating

    Parameters
    ----------

    floating : bool
      Passed on as it is.
    """
    #  void QDockWidget::setFloating(bool floating)
    self.uglySide.call('ritual_ZN11QDockWidget11setFloatingEb', floating)

  @overload(Qt.DockWidgetAreas)
  def setAllowedAreas(self, areas: Qt.DockWidgetAreas) -> None:
    """
    Calls Qt's 'void QDockWidget::setAllowedAreas(Qt::DockWidgetAreas
    areas)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#setAllowedAreas

    Parameters
    ----------

    areas : Qt.DockWidgetAreas
      Passed on as its number.
    """
    #  void QDockWidget::setAllowedAreas(Qt::DockWidgetAreas areas)
    self.uglySide.call(
        'ritual_ZN11QDockWidget15setAllowedAreasE6QFlagsIN2Qt14DockWidgetAr'
        'eaEE',
        areas.value,
    )

  @overload(QWidget)
  @overload(NoneType)
  def setTitleBarWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDockWidget::setTitleBarWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#setTitleBarWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidget::setTitleBarWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN11QDockWidget17setTitleBarWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(Qt.DockWidgetArea)
  def setDockLocation(self, area: Qt.DockWidgetArea) -> None:
    """
    Calls Qt's 'void QDockWidget::setDockLocation(Qt::DockWidgetArea area)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#setDockLocation

    Parameters
    ----------

    area : Qt.DockWidgetArea
      Passed on as its number.
    """
    #  void QDockWidget::setDockLocation(Qt::DockWidgetArea area)
    self.uglySide.call(
        'ritual_ZN11QDockWidget15setDockLocationEN2Qt14DockWidgetAreaE',
        area.value,
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

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  @overload(str, QWidget, Qt.WindowFlags)
  @overload(str, NoneType, Qt.WindowFlags)
  def __init__(
      self,
      title: str,
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QDockWidget::QDockWidget(const QString
    &title, QWidget *parent, Qt::WindowFlags flags)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#QDockWidget

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QDockWidget::QDockWidget(const QString &title, QWidget *parent,
    #      Qt::WindowFlags flags)
    self._noteCreation(QDockWidget, lambda: Rituals.call(
        'ritual_ZN11QDockWidgetC1ERK7QStringP7QWidget6QFlagsIN2Qt10WindowTy'
        'peEE',
        title, self._addressOf(parent), flags.value,
    ))

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QDockWidget::QDockWidget(QWidget *parent,
    Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#QDockWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QDockWidget::QDockWidget(QWidget *parent, Qt::WindowFlags flags)
    self._noteCreation(QDockWidget, lambda: Rituals.call(
        'ritual_ZN11QDockWidgetC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), flags.value,
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

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QDockWidget::changeEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#changeEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidget::changeEvent(QEvent *event)
    ritual = 'ritual_ZN11QDockWidget11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QDockWidget11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QCloseEvent)
  @overload(NoneType)
  def closeEvent(self, event: Optional[QCloseEvent]) -> None:
    """
    Calls Qt's 'void QDockWidget::closeEvent(QCloseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#closeEvent

    Parameters
    ----------

    event : Optional[QCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidget::closeEvent(QCloseEvent *event)
    ritual = 'ritual_ZN11QDockWidget10closeEventEP11QCloseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QDockWidget10closeEventEP11QCloseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QDockWidget::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidget::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN11QDockWidget10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QDockWidget10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QDockWidget::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDockWidget::event(QEvent *event)
    ritual = 'ritual_ZN11QDockWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QDockWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QStyleOptionDockWidget)
  @overload(NoneType)
  def initStyleOption(
      self,
      option: Optional[QStyleOptionDockWidget],
  ) -> None:
    """
    Calls Qt's 'void QDockWidget::initStyleOption(QStyleOptionDockWidget
    *option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdockwidget.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionDockWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDockWidget::initStyleOption(QStyleOptionDockWidget *option)
    #      const
    ritual = (
        'ritual_ZNK11QDockWidget15initStyleOptionEP22QStyleOptionDockWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK11QDockWidget15initStyleOptionEP22QStyleOptionDock'
          'Widget')
    self.uglySide.call(ritual, self._addressOf(option))


#  Qt's 'QList<QDockWidget *>': the list of QDockWidget, which
#  'QList[QDockWidget]' gives. It is made here, so that there is one as soon
#  as there can be a QDockWidget.
QList.createKind(
    QDockWidget, 'address',
    make='ritual_list_make_QDockWidget_ptr',
    add='ritual_list_add_QDockWidget_ptr',
    size='ritual_list_size_QDockWidget_ptr',
    at='ritual_list_at_QDockWidget_ptr',
    drop='ritual_list_drop_QDockWidget_ptr',
)
