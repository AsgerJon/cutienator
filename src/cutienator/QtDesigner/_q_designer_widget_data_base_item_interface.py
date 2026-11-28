"""
QDesignerWidgetDataBaseItemInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractwidgetdatabase.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from ..QtGui import QIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIcon = WAIT['QIcon']
  QVariant = WAIT['QVariant']


class QDesignerWidgetDataBaseItemInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerWidgetDataBaseItemInterface: a plain Python
  object standing in front of one C++ QDesignerWidgetDataBaseItemInterface.

  What exists
  -----------

  Every function of Qt's QDesignerWidgetDataBaseItemInterface that has a
  ritual and that Python can call so far, 26 names in all: 'name', 'setName',
  'group', 'setGroup', 'toolTip', 'setToolTip', 'whatsThis', 'setWhatsThis',
  'includeFile', 'setIncludeFile', 'icon', 'setIcon', 'isCompat',
  'setCompat', 'isContainer', 'setContainer', 'isCustom', 'setCustom',
  'pluginPath', 'setPluginPath', 'isPromoted', 'setPromoted', 'extends',
  'setExtends', 'setDefaultPropertyValues', 'defaultPropertyValues'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDesignerWidgetDataBaseItemInterface::
    ~QDesignerWidgetDataBaseItemInterface()': the destructor: Python never
    removes a C++ QDesignerWidgetDataBaseItemInterface.

  What has no ritual
  ------------------

  5 of the 32 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerWidgetDataBaseItemInterface is created at the first use,
    not by 'QDesignerWidgetDataBaseItemInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerWidgetDataBaseItemInterface.
  - Each name of Qt's QDesignerWidgetDataBaseItemInterface that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerWidgetDataBaseItemInterface'

  #  A C++ QDesignerWidgetDataBaseItemInterface Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerWidgetDataBaseItemInterface'

  #  The functions Qt calls itself that QDesignerWidgetDataBaseItemInterface
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setDefaultPropertyValues': (
          'void '
          'QDesignerWidgetDataBaseItemInterface::setDefaultPropertyValues(c'
          'onst QList<QVariant> &)',
      ),
      'defaultPropertyValues': (
          'QList<QVariant> '
          'QDesignerWidgetDataBaseItemInterface::defaultPropertyValues() '
          'const',
      ),
  }

  #  The functions Qt calls itself that QDesignerWidgetDataBaseItemInterface
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'setName': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface7setNameERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'group': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface5groupEv',
           ('address', 'text', ''),
           ()),
      ),
      'setGroup': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface8setGroupERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'toolTip': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface7toolTipEv',
           ('address', 'text', ''),
           ()),
      ),
      'setToolTip': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface10setToolTipERK7QStrin'
           'g',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'whatsThis': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface9whatsThisEv',
           ('address', 'text', ''),
           ()),
      ),
      'setWhatsThis': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface12setWhatsThisERK7QStr'
           'ing',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'includeFile': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface11includeFileEv',
           ('address', 'text', ''),
           ()),
      ),
      'setIncludeFile': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface14setIncludeFileERK7QS'
           'tring',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'icon': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface4iconEv',
           ('address', 'value', 'QtGui:QIcon'),
           ()),
      ),
      'setIcon': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface7setIconERK5QIcon',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QIcon'),
           )),
      ),
      'isCompat': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface8isCompatEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setCompat': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface9setCompatEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'isContainer': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface11isContainerEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setContainer': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface12setContainerEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'isCustom': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface8isCustomEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setCustom': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface9setCustomEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'pluginPath': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface10pluginPathEv',
           ('address', 'text', ''),
           ()),
      ),
      'setPluginPath': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface13setPluginPathERK7QSt'
           'ring',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'isPromoted': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface10isPromotedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setPromoted': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface11setPromotedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'extends': (
          ('_ZNK36QDesignerWidgetDataBaseItemInterface7extendsEv',
           ('address', 'text', ''),
           ()),
      ),
      'setExtends': (
          ('_ZN36QDesignerWidgetDataBaseItemInterface10setExtendsERK7QStrin'
           'g',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
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

  def name(self) -> str:
    """
    Calls Qt's 'QString QDesignerWidgetDataBaseItemInterface::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerWidgetDataBaseItemInterface::name() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface4nameEv',
    )

  def group(self) -> str:
    """
    Calls Qt's 'QString QDesignerWidgetDataBaseItemInterface::group() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html#group

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerWidgetDataBaseItemInterface::group() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface5groupEv',
    )

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString QDesignerWidgetDataBaseItemInterface::toolTip()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerWidgetDataBaseItemInterface::toolTip() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface7toolTipEv',
    )

  def whatsThis(self) -> str:
    """
    Calls Qt's 'QString QDesignerWidgetDataBaseItemInterface::whatsThis()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerWidgetDataBaseItemInterface::whatsThis() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface9whatsThisEv',
    )

  def includeFile(self) -> str:
    """
    Calls Qt's 'QString QDesignerWidgetDataBaseItemInterface::includeFile()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerWidgetDataBaseItemInterface::includeFile() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface11includeFileEv',
    )

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QDesignerWidgetDataBaseItemInterface::icon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QDesignerWidgetDataBaseItemInterface::icon() const
    address = self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface4iconEv',
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def isCompat(self) -> bool:
    """
    Calls Qt's 'bool QDesignerWidgetDataBaseItemInterface::isCompat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html#isCompat
    """
    #  bool QDesignerWidgetDataBaseItemInterface::isCompat() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface8isCompatEv',
    )

  def isContainer(self) -> bool:
    """
    Calls Qt's 'bool QDesignerWidgetDataBaseItemInterface::isContainer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html
    """
    #  bool QDesignerWidgetDataBaseItemInterface::isContainer() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface11isContainerEv',
    )

  def isCustom(self) -> bool:
    """
    Calls Qt's 'bool QDesignerWidgetDataBaseItemInterface::isCustom() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html#isCustom
    """
    #  bool QDesignerWidgetDataBaseItemInterface::isCustom() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface8isCustomEv',
    )

  def pluginPath(self) -> str:
    """
    Calls Qt's 'QString QDesignerWidgetDataBaseItemInterface::pluginPath()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerWidgetDataBaseItemInterface::pluginPath() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface10pluginPathEv',
    )

  def isPromoted(self) -> bool:
    """
    Calls Qt's 'bool QDesignerWidgetDataBaseItemInterface::isPromoted()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html
    """
    #  bool QDesignerWidgetDataBaseItemInterface::isPromoted() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface10isPromotedEv',
    )

  def extends(self) -> str:
    """
    Calls Qt's 'QString QDesignerWidgetDataBaseItemInterface::extends()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html#extends

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerWidgetDataBaseItemInterface::extends() const
    return self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface7extendsEv',
    )

  def defaultPropertyValues(self) -> QList[QVariant]:
    """
    Calls Qt's 'QList<QVariant>
    QDesignerWidgetDataBaseItemInterface::defaultPropertyValues() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVariant>
    #      QDesignerWidgetDataBaseItemInterface::defaultPropertyValues()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK36QDesignerWidgetDataBaseItemInterface21defaultPropertyV'
        'aluesEv',
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseItemInterface::setName(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setName(const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface7setNameERK7QString',
        name,
    )

  @overload(str)
  def setGroup(self, group: str) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseItemInterface::setGroup(const
    QString &group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html#setGroup

    Parameters
    ----------

    group : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setGroup(const QString
    #      &group)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface8setGroupERK7QStrin'
        'g',
        group,
    )

  @overload(str)
  def setToolTip(self, toolTip: str) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseItemInterface::setToolTip(const
    QString &toolTip)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Parameters
    ----------

    toolTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setToolTip(const QString
    #      &toolTip)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface10setToolTipERK7QSt'
        'ring',
        toolTip,
    )

  @overload(str)
  def setWhatsThis(self, whatsThis: str) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseItemInterface::setWhatsThis(const
    QString &whatsThis)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Parameters
    ----------

    whatsThis : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setWhatsThis(const QString
    #      &whatsThis)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface12setWhatsThisERK7Q'
        'String',
        whatsThis,
    )

  @overload(str)
  def setIncludeFile(self, includeFile: str) -> None:
    """
    Calls Qt's 'void
    QDesignerWidgetDataBaseItemInterface::setIncludeFile(const QString
    &includeFile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Parameters
    ----------

    includeFile : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setIncludeFile(const
    #      QString &includeFile)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface14setIncludeFileERK'
        '7QString',
        includeFile,
    )

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseItemInterface::setIcon(const
    QIcon &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface7setIconERK5QIcon',
        self._valueOf(icon),
    )

  @overload(bool)
  def setCompat(self, compat: bool) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseItemInterface::setCompat(bool
    compat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Parameters
    ----------

    compat : bool
      Passed on as it is.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setCompat(bool compat)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface9setCompatEb',
        compat,
    )

  @overload(bool)
  def setContainer(self, container: bool) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseItemInterface::setContainer(bool
    container)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Parameters
    ----------

    container : bool
      Passed on as it is.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setContainer(bool
    #      container)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface12setContainerEb',
        container,
    )

  @overload(bool)
  def setCustom(self, custom: bool) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseItemInterface::setCustom(bool
    custom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Parameters
    ----------

    custom : bool
      Passed on as it is.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setCustom(bool custom)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface9setCustomEb',
        custom,
    )

  @overload(str)
  def setPluginPath(self, path: str) -> None:
    """
    Calls Qt's 'void
    QDesignerWidgetDataBaseItemInterface::setPluginPath(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setPluginPath(const QString
    #      &path)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface13setPluginPathERK7'
        'QString',
        path,
    )

  @overload(bool)
  def setPromoted(self, b: bool) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseItemInterface::setPromoted(bool
    b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setPromoted(bool b)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface11setPromotedEb', b,
    )

  @overload(str)
  def setExtends(self, s: str) -> None:
    """
    Calls Qt's 'void QDesignerWidgetDataBaseItemInterface::setExtends(const
    QString &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setExtends(const QString
    #      &s)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface10setExtendsERK7QSt'
        'ring',
        s,
    )

  @overload(QList[QVariant])
  def setDefaultPropertyValues(self, list: QList[QVariant]) -> None:
    """
    Calls Qt's 'void
    QDesignerWidgetDataBaseItemInterface::setDefaultPropertyValues(const
    QList<QVariant> &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetdatabaseiteminterface.html

    Parameters
    ----------

    list : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDesignerWidgetDataBaseItemInterface::setDefaultPropertyValues(
    #      const QList<QVariant> &list)
    self.uglySide.call(
        'ritual_ZN36QDesignerWidgetDataBaseItemInterface24setDefaultPropert'
        'yValuesERK5QListI8QVariantE',
        self._valueOf(list),
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
    Qt's 'QDesignerWidgetDataBaseItemInterface::
    QDesignerWidgetDataBaseItemInterface()': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QDesignerWidgetDataBaseItemInterface.__init__' has no cute "
        "function yet. Qt's "
        "'QDesignerWidgetDataBaseItemInterface::QDesignerWidgetDataBaseItemI"
        "nterface()': the class is abstract, so C++ cannot make one, and "
        "the C++ class of ours does not fill in every function it leaves "
        "open.")

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


#  Qt's 'QList<QDesignerWidgetDataBaseItemInterface *>': the list of
#  QDesignerWidgetDataBaseItemInterface, which
#  'QList[QDesignerWidgetDataBaseItemInterface]' gives. It is made here, so
#  that there is one as soon as there can be a
#  QDesignerWidgetDataBaseItemInterface.
QList.createKind(
    QDesignerWidgetDataBaseItemInterface, 'address',
    make='ritual_list_make_QDesignerWidgetDataBaseItemInterface_ptr',
    add='ritual_list_add_QDesignerWidgetDataBaseItemInterface_ptr',
    size='ritual_list_size_QDesignerWidgetDataBaseItemInterface_ptr',
    at='ritual_list_at_QDesignerWidgetDataBaseItemInterface_ptr',
    drop='ritual_list_drop_QDesignerWidgetDataBaseItemInterface_ptr',
)
