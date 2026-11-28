"""
QDesignerWidgetBoxInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractwidgetbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from . import QDesignerDnDItemInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerDnDItemInterface = WAIT['QDesignerDnDItemInterface']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerWidgetBoxInterface(QWidget):
  """
  The cute side of Qt's QDesignerWidgetBoxInterface: a plain Python object
  standing in front of one C++ QDesignerWidgetBoxInterface.

  It is built on the cute 'QWidget', as Qt's QDesignerWidgetBoxInterface is
  built on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerWidgetBoxInterface that has a ritual and
  that Python can call so far, 16 names in all: 'metaObject', 'tr',
  'categoryCount', 'category', 'addCategory', 'removeCategory',
  'widgetCount', 'widget', 'addWidget', 'removeWidget',
  'findOrInsertCategory', 'dropWidgets', 'setFileName', 'fileName', 'load',
  'save'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerWidgetBoxInterface::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDesignerWidgetBoxInterface::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerWidgetBoxInterface::~QDesignerWidgetBoxInterface()': the
    destructor: Python never removes a C++ QDesignerWidgetBoxInterface.

  What has no ritual
  ------------------

  3 of the 22 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerWidgetBoxInterface is created at the first use, not by
    'QDesignerWidgetBoxInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerWidgetBoxInterface.
  - Qt tells when it has removed the C++ QDesignerWidgetBoxInterface. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDesignerWidgetBoxInterface that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QDesignerWidgetBoxInterface, each a class
  #  in here as in C++.

  class Category(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDesignerWidgetBoxInterface::Category: a plain
    Python object standing in front of one C++
    QDesignerWidgetBoxInterface::Category.

    C++ hands a QDesignerWidgetBoxInterface::Category around as a copy, so
    every C++ QDesignerWidgetBoxInterface::Category behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QDesignerWidgetBoxInterface::Category that has a
    ritual and that Python can call so far, 7 names in all: 'name',
    'setName', 'widgetCount', 'removeWidget', 'type', 'setType', 'isNull'. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Widget QDesignerWidgetBoxInterface::Category::widget(int idx)
      const': gives 'QDesignerWidgetBoxInterface::Widget', which stands
      beside this class inside 'QDesignerWidgetBoxInterface' and cannot be
      named from here.
    - Qt's 'void QDesignerWidgetBoxInterface::Category::addWidget(const
      Widget &awidget)': names 'QDesignerWidgetBoxInterface::Widget', which
      stands beside this class inside 'QDesignerWidgetBoxInterface' and
      cannot be named from here.
    - Qt's 'QDesignerWidgetBoxInterface::Category::~Category()': the
      destructor: Python removes its C++
      QDesignerWidgetBoxInterface::Category by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QDesignerWidgetBoxInterface::Category is created at the first
      use, not by 'QDesignerWidgetBoxInterface::Category(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDesignerWidgetBoxInterface::Category back gives a
      copy the ritual made for Python, in a new cute
      QDesignerWidgetBoxInterface::Category.
    - Each name of Qt's QDesignerWidgetBoxInterface::Category that has no
      cute function yet, 'addWidget', 'widget', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The enums Qt writes inside QDesignerWidgetBoxInterface::Category, each
    #  a class in here as in C++, and the names Qt has for the combinations
    #  of its flags enums.

    class Type(CuteNum):
      """
      The enum 'QDesignerWidgetBoxInterface::Category::Type' of Qt, with the
      2 names Qt gives in it.
      """

      Default = Kee[int](0)
      Scratchpad = Kee[int](1)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDesignerWidgetBoxInterface::Category'

    #  Qt's '~QDesignerWidgetBoxInterface::Category()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QDesignerWidgetBoxInterface::Category behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN27QDesignerWidgetBoxInterface8CategoryD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def name(self) -> str:
      """
      Calls Qt's 'QString QDesignerWidgetBoxInterface::Category::name()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-category.html#name

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDesignerWidgetBoxInterface::Category::name() const
      return self.uglySide.call(
          'ritual_ZNK27QDesignerWidgetBoxInterface8Category4nameEv',
      )

    def widgetCount(self) -> int:
      """
      Calls Qt's 'int QDesignerWidgetBoxInterface::Category::widgetCount()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-category.html
      """
      #  int QDesignerWidgetBoxInterface::Category::widgetCount() const
      return self.uglySide.call(
          'ritual_ZNK27QDesignerWidgetBoxInterface8Category11widgetCountEv',
      )

    def type(self) -> Type:
      """
      Calls Qt's 'Type QDesignerWidgetBoxInterface::Category::type() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-category.html#type

      Returns
      -------

      Type
        The member standing for the number Qt gave back. For a number Qt
        gives no name it is the member without a name that 'Type(number)'
        gives.
      """
      #  Type QDesignerWidgetBoxInterface::Category::type() const
      return QDesignerWidgetBoxInterface.Category.Type(self.uglySide.call(
          'ritual_ZNK27QDesignerWidgetBoxInterface8Category4typeEv',
      ))

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool QDesignerWidgetBoxInterface::Category::isNull()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-category.html#isNull
      """
      #  bool QDesignerWidgetBoxInterface::Category::isNull() const
      return self.uglySide.call(
          'ritual_ZNK27QDesignerWidgetBoxInterface8Category6isNullEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str)
    def setName(self, aname: str) -> None:
      """
      Calls Qt's 'void QDesignerWidgetBoxInterface::Category::setName(const
      QString &aname)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-category.html

      Parameters
      ----------

      aname : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  void QDesignerWidgetBoxInterface::Category::setName(const QString
      #      &aname)
      self.uglySide.call(
          'ritual_ZN27QDesignerWidgetBoxInterface8Category7setNameERK7QStri'
          'ng',
          aname,
      )

    @overload(Type)
    def setType(self, atype: Type) -> None:
      """
      Calls Qt's 'void QDesignerWidgetBoxInterface::Category::setType(Type
      atype)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-category.html

      Parameters
      ----------

      atype : Type
        Passed on as its number.
      """
      #  void QDesignerWidgetBoxInterface::Category::setType(Type atype)
      self.uglySide.call(
          'ritual_ZN27QDesignerWidgetBoxInterface8Category7setTypeENS0_4Typ'
          'eE',
          atype.value,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    @overload(str)
    @overload(str, Type)
    def __init__(self, aname: str = '', atype: Type = Type.Default) -> None:
      """
      Notes what was given, for Qt's
      'QDesignerWidgetBoxInterface::Category::Category(const QString &aname,
      Type atype)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-category.html

      Parameters
      ----------

      aname : str
        Passed on as it is: a QString is made of it for the call. May be left
        out, as in Qt: it is then ''.

      atype : Type
        Passed on as its number. May be left out, as in Qt: it is then
        Type.Default.
      """
      #  QDesignerWidgetBoxInterface::Category::Category(const QString
      #      &aname, Type atype)
      self._noteCreation(
          QDesignerWidgetBoxInterface.Category, lambda: Rituals.call(
              'ritual_ZN27QDesignerWidgetBoxInterface8CategoryC1ERK7QString'
              'NS0_4TypeE',
              aname, atype.value,
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    def removeWidget(self, idx: int) -> None:
      """
      Calls Qt's 'void
      QDesignerWidgetBoxInterface::Category::removeWidget(int idx)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-category.html

      Parameters
      ----------

      idx : int
        Passed on as it is.
      """
      #  void QDesignerWidgetBoxInterface::Category::removeWidget(int idx)
      self.uglySide.call(
          'ritual_ZN27QDesignerWidgetBoxInterface8Category12removeWidgetEi',
          idx,
      )

    @staticmethod
    def addWidget(*__, **_) -> Never:
      """
      Qt's 'void QDesignerWidgetBoxInterface::Category::addWidget(const
      Widget &awidget)': names 'QDesignerWidgetBoxInterface::Widget', which
      stands beside this class inside 'QDesignerWidgetBoxInterface' and
      cannot be named from here.
      """
      raise NotImplementedError(
          "'QDesignerWidgetBoxInterface.Category.addWidget' has no cute "
          "function yet. Qt's 'void "
          "QDesignerWidgetBoxInterface::Category::addWidget(const Widget "
          "&awidget)': names 'QDesignerWidgetBoxInterface::Widget', which "
          "stands beside this class inside 'QDesignerWidgetBoxInterface' "
          "and cannot be named from here.")

    @staticmethod
    def widget(*__, **_) -> Never:
      """
      Qt's 'Widget QDesignerWidgetBoxInterface::Category::widget(int idx)
      const': gives 'QDesignerWidgetBoxInterface::Widget', which stands
      beside this class inside 'QDesignerWidgetBoxInterface' and cannot be
      named from here.
      """
      raise NotImplementedError(
          "'QDesignerWidgetBoxInterface.Category.widget' has no cute "
          "function yet. Qt's 'Widget "
          "QDesignerWidgetBoxInterface::Category::widget(int idx) const': "
          "gives 'QDesignerWidgetBoxInterface::Widget', which stands beside "
          "this class inside 'QDesignerWidgetBoxInterface' and cannot be "
          "named from here.")

  class Widget(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDesignerWidgetBoxInterface::Widget: a plain Python
    object standing in front of one C++ QDesignerWidgetBoxInterface::Widget.

    C++ hands a QDesignerWidgetBoxInterface::Widget around as a copy, so
    every C++ QDesignerWidgetBoxInterface::Widget behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QDesignerWidgetBoxInterface::Widget that has a
    ritual and that Python can call so far, 9 names in all: 'name',
    'setName', 'domXml', 'setDomXml', 'iconName', 'setIconName', 'type',
    'setType', 'isNull'. It can be made from Python, in 2 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDesignerWidgetBoxInterface::Widget::~Widget()': the destructor:
      Python removes its C++ QDesignerWidgetBoxInterface::Widget by it, and
      has no other use for it.
    - Qt's 'Widget &QDesignerWidgetBoxInterface::Widget::operator=(const
      Widget &w)': assignment: Python binds a name and has no operator for
      it.

    What to expect
    --------------

    - The C++ QDesignerWidgetBoxInterface::Widget is created at the first
      use, not by 'QDesignerWidgetBoxInterface::Widget(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDesignerWidgetBoxInterface::Widget back gives a
      copy the ritual made for Python, in a new cute
      QDesignerWidgetBoxInterface::Widget.
    """

    #  The enums Qt writes inside QDesignerWidgetBoxInterface::Widget, each a
    #  class in here as in C++, and the names Qt has for the combinations of
    #  its flags enums.

    class Type(CuteNum):
      """
      The enum 'QDesignerWidgetBoxInterface::Widget::Type' of Qt, with the 2
      names Qt gives in it.
      """

      Default = Kee[int](0)
      Custom = Kee[int](1)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDesignerWidgetBoxInterface::Widget'

    #  Qt's '~QDesignerWidgetBoxInterface::Widget()'. Naming it makes this a
    #  value class: Python owns every C++ QDesignerWidgetBoxInterface::Widget
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN27QDesignerWidgetBoxInterface6WidgetD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def name(self) -> str:
      """
      Calls Qt's 'QString QDesignerWidgetBoxInterface::Widget::name() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html#name

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDesignerWidgetBoxInterface::Widget::name() const
      return self.uglySide.call(
          'ritual_ZNK27QDesignerWidgetBoxInterface6Widget4nameEv',
      )

    def domXml(self) -> str:
      """
      Calls Qt's 'QString QDesignerWidgetBoxInterface::Widget::domXml()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html#domXml

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDesignerWidgetBoxInterface::Widget::domXml() const
      return self.uglySide.call(
          'ritual_ZNK27QDesignerWidgetBoxInterface6Widget6domXmlEv',
      )

    def iconName(self) -> str:
      """
      Calls Qt's 'QString QDesignerWidgetBoxInterface::Widget::iconName()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html#iconName

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QDesignerWidgetBoxInterface::Widget::iconName() const
      return self.uglySide.call(
          'ritual_ZNK27QDesignerWidgetBoxInterface6Widget8iconNameEv',
      )

    def type(self) -> Type:
      """
      Calls Qt's 'Type QDesignerWidgetBoxInterface::Widget::type() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html#type

      Returns
      -------

      Type
        The member standing for the number Qt gave back. For a number Qt
        gives no name it is the member without a name that 'Type(number)'
        gives.
      """
      #  Type QDesignerWidgetBoxInterface::Widget::type() const
      return QDesignerWidgetBoxInterface.Widget.Type(self.uglySide.call(
          'ritual_ZNK27QDesignerWidgetBoxInterface6Widget4typeEv',
      ))

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool QDesignerWidgetBoxInterface::Widget::isNull() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html#isNull
      """
      #  bool QDesignerWidgetBoxInterface::Widget::isNull() const
      return self.uglySide.call(
          'ritual_ZNK27QDesignerWidgetBoxInterface6Widget6isNullEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str)
    def setName(self, aname: str) -> None:
      """
      Calls Qt's 'void QDesignerWidgetBoxInterface::Widget::setName(const
      QString &aname)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html#setName

      Parameters
      ----------

      aname : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  void QDesignerWidgetBoxInterface::Widget::setName(const QString
      #      &aname)
      self.uglySide.call(
          'ritual_ZN27QDesignerWidgetBoxInterface6Widget7setNameERK7QString',
          aname,
      )

    @overload(str)
    def setDomXml(self, xml: str) -> None:
      """
      Calls Qt's 'void QDesignerWidgetBoxInterface::Widget::setDomXml(const
      QString &xml)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html

      Parameters
      ----------

      xml : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  void QDesignerWidgetBoxInterface::Widget::setDomXml(const QString
      #      &xml)
      self.uglySide.call(
          'ritual_ZN27QDesignerWidgetBoxInterface6Widget9setDomXmlERK7QStri'
          'ng',
          xml,
      )

    @overload(str)
    def setIconName(self, icon_name: str) -> None:
      """
      Calls Qt's 'void QDesignerWidgetBoxInterface::Widget::setIconName(const
      QString &icon_name)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html

      Parameters
      ----------

      icon_name : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  void QDesignerWidgetBoxInterface::Widget::setIconName(const QString
      #      &icon_name)
      self.uglySide.call(
          'ritual_ZN27QDesignerWidgetBoxInterface6Widget11setIconNameERK7QS'
          'tring',
          icon_name,
      )

    @overload(Type)
    def setType(self, atype: Type) -> None:
      """
      Calls Qt's 'void QDesignerWidgetBoxInterface::Widget::setType(Type
      atype)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html#setType

      Parameters
      ----------

      atype : Type
        Passed on as its number.
      """
      #  void QDesignerWidgetBoxInterface::Widget::setType(Type atype)
      self.uglySide.call(
          'ritual_ZN27QDesignerWidgetBoxInterface6Widget7setTypeENS0_4TypeE',
          atype.value,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    @overload(str)
    @overload(str, str)
    @overload(str, str, str)
    @overload(str, str, str, Type)
    def __init__(
        self,
        aname: str = '',
        xml: str = '',
        icon_name: str = '',
        atype: Type = Type.Default,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QDesignerWidgetBoxInterface::Widget::Widget(const QString &aname,
      const QString &xml, const QString &icon_name, Type atype)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html#Widget

      Parameters
      ----------

      aname : str
        Passed on as it is: a QString is made of it for the call. May be left
        out, as in Qt: it is then ''.

      xml : str
        Passed on as it is: a QString is made of it for the call. May be left
        out, as in Qt: it is then ''.

      icon_name : str
        Passed on as it is: a QString is made of it for the call. May be left
        out, as in Qt: it is then ''.

      atype : Type
        Passed on as its number. May be left out, as in Qt: it is then
        Type.Default.
      """
      #  QDesignerWidgetBoxInterface::Widget::Widget(const QString &aname,
      #      const QString &xml, const QString &icon_name, Type atype)
      self._noteCreation(
          QDesignerWidgetBoxInterface.Widget, lambda: Rituals.call(
              'ritual_ZN27QDesignerWidgetBoxInterface6WidgetC1ERK7QStringS3'
              '_S3_NS0_4TypeE',
              aname, xml, icon_name, atype.value,
          ))

    @overload(THIS)
    def __init__(self, w: QDesignerWidgetBoxInterface.Widget) -> None:
      """
      Notes what was given, for Qt's
      'QDesignerWidgetBoxInterface::Widget::Widget(const Widget &w)', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesignerwidgetboxinterface-widget.html#Widget

      Parameters
      ----------

      w : QDesignerWidgetBoxInterface.Widget
        Passed on as a value: Qt reads the C++
        QDesignerWidgetBoxInterface::Widget, which stays Python's own.
      """
      #  QDesignerWidgetBoxInterface::Widget::Widget(const Widget &w)
      self._noteCreation(
          QDesignerWidgetBoxInterface.Widget, lambda: Rituals.call(
              'ritual_ZN27QDesignerWidgetBoxInterface6WidgetC1ERKS0_',
              self._valueOf(w),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QDesignerWidgetBoxInterface::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#tr

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
    #  QString QDesignerWidgetBoxInterface::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QDesignerWidgetBoxInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerWidgetBoxInterface'

  #  A C++ QDesignerWidgetBoxInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerWidgetBoxInterface'

  #  The functions Qt calls itself that QDesignerWidgetBoxInterface is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dropWidgets': (
          'void QDesignerWidgetBoxInterface::dropWidgets(const '
          'QList<QDesignerDnDItemInterface *> &, const QPoint &)',
      ),
  }

  #  The functions Qt calls itself that QDesignerWidgetBoxInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'categoryCount': (
          ('_ZNK27QDesignerWidgetBoxInterface13categoryCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'category': (
          ('_ZNK27QDesignerWidgetBoxInterface8categoryEi',
           ('address', 'value',
            'QtDesigner:QDesignerWidgetBoxInterface.Category'),
           (
               ('int', 'number', ''),
           )),
      ),
      'addCategory': (
          ('_ZN27QDesignerWidgetBoxInterface11addCategoryERKNS_8CategoryE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value',
                'QtDesigner:QDesignerWidgetBoxInterface.Category'),
           )),
      ),
      'removeCategory': (
          ('_ZN27QDesignerWidgetBoxInterface14removeCategoryEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'widgetCount': (
          ('_ZNK27QDesignerWidgetBoxInterface11widgetCountEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'widget': (
          ('_ZNK27QDesignerWidgetBoxInterface6widgetEii',
           ('address', 'value',
            'QtDesigner:QDesignerWidgetBoxInterface.Widget'),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'addWidget': (
          ('_ZN27QDesignerWidgetBoxInterface9addWidgetEiRKNS_6WidgetE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value',
                'QtDesigner:QDesignerWidgetBoxInterface.Widget'),
           )),
      ),
      'removeWidget': (
          ('_ZN27QDesignerWidgetBoxInterface12removeWidgetEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'setFileName': (
          ('_ZN27QDesignerWidgetBoxInterface11setFileNameERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'fileName': (
          ('_ZNK27QDesignerWidgetBoxInterface8fileNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'load': (
          ('_ZN27QDesignerWidgetBoxInterface4loadEv',
           ('bool', 'number', ''),
           ()),
      ),
      'save': (
          ('_ZN27QDesignerWidgetBoxInterface4saveEv',
           ('bool', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QDesignerWidgetBoxInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerWidgetBoxInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QDesignerWidgetBoxInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def categoryCount(self) -> int:
    """
    Calls Qt's 'int QDesignerWidgetBoxInterface::categoryCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#categoryCount
    """
    #  int QDesignerWidgetBoxInterface::categoryCount() const
    return self.uglySide.call(
        'ritual_ZNK27QDesignerWidgetBoxInterface13categoryCountEv',
    )

  @overload(int)
  def category(self, cat_idx: int) -> Category:
    """
    Calls Qt's 'Category QDesignerWidgetBoxInterface::category(int cat_idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#category

    Parameters
    ----------

    cat_idx : int
      Passed on as it is.

    Returns
    -------

    Category
      A new cute QDesignerWidgetBoxInterface::Category around the copy Qt
      gave back. Python owns it.
    """
    #  Category QDesignerWidgetBoxInterface::category(int cat_idx) const
    address = self.uglySide.call(
        'ritual_ZNK27QDesignerWidgetBoxInterface8categoryEi', cat_idx,
    )
    return QDesignerWidgetBoxInterface.Category._cuteOwning(address)

  @overload(int)
  def widgetCount(self, cat_idx: int) -> int:
    """
    Calls Qt's 'int QDesignerWidgetBoxInterface::widgetCount(int cat_idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#widgetCount

    Parameters
    ----------

    cat_idx : int
      Passed on as it is.
    """
    #  int QDesignerWidgetBoxInterface::widgetCount(int cat_idx) const
    return self.uglySide.call(
        'ritual_ZNK27QDesignerWidgetBoxInterface11widgetCountEi', cat_idx,
    )

  @overload(int, int)
  def widget(self, cat_idx: int, wgt_idx: int) -> Widget:
    """
    Calls Qt's 'Widget QDesignerWidgetBoxInterface::widget(int cat_idx, int
    wgt_idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#widget

    Parameters
    ----------

    cat_idx : int
      Passed on as it is.

    wgt_idx : int
      Passed on as it is.

    Returns
    -------

    Widget
      A new cute QDesignerWidgetBoxInterface::Widget around the copy Qt gave
      back. Python owns it.
    """
    #  Widget QDesignerWidgetBoxInterface::widget(int cat_idx, int wgt_idx)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QDesignerWidgetBoxInterface6widgetEii',
        cat_idx, wgt_idx,
    )
    return QDesignerWidgetBoxInterface.Widget._cuteOwning(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QDesignerWidgetBoxInterface::fileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerWidgetBoxInterface::fileName() const
    return self.uglySide.call(
        'ritual_ZNK27QDesignerWidgetBoxInterface8fileNameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, file_name: str) -> None:
    """
    Calls Qt's 'void QDesignerWidgetBoxInterface::setFileName(const QString
    &file_name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#setFileName

    Parameters
    ----------

    file_name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerWidgetBoxInterface::setFileName(const QString
    #      &file_name)
    self.uglySide.call(
        'ritual_ZN27QDesignerWidgetBoxInterface11setFileNameERK7QString',
        file_name,
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
    Qt's 'QDesignerWidgetBoxInterface::QDesignerWidgetBoxInterface(QWidget
    *parent, Qt::WindowFlags flags)': the class is abstract, so C++ cannot
    make one, and the C++ class of ours does not fill in every function it
    leaves open.
    """
    raise NotImplementedError(
        "'QDesignerWidgetBoxInterface.__init__' has no cute function yet. "
        "Qt's "
        "'QDesignerWidgetBoxInterface::QDesignerWidgetBoxInterface(QWidget "
        "*parent, Qt::WindowFlags flags)': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  @overload(Category)
  def addCategory(self, cat: Category) -> None:
    """
    Calls Qt's 'void QDesignerWidgetBoxInterface::addCategory(const Category
    &cat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#addCategory

    Parameters
    ----------

    cat : Category
      Passed on as a value: Qt reads the C++
      QDesignerWidgetBoxInterface::Category, which stays Python's own.
    """
    #  void QDesignerWidgetBoxInterface::addCategory(const Category &cat)
    self.uglySide.call(
        'ritual_ZN27QDesignerWidgetBoxInterface11addCategoryERKNS_8Category'
        'E',
        self._valueOf(cat),
    )

  @overload(int)
  def removeCategory(self, cat_idx: int) -> None:
    """
    Calls Qt's 'void QDesignerWidgetBoxInterface::removeCategory(int
    cat_idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#removeCategory

    Parameters
    ----------

    cat_idx : int
      Passed on as it is.
    """
    #  void QDesignerWidgetBoxInterface::removeCategory(int cat_idx)
    self.uglySide.call(
        'ritual_ZN27QDesignerWidgetBoxInterface14removeCategoryEi', cat_idx,
    )

  @overload(int, Widget)
  def addWidget(self, cat_idx: int, wgt: Widget) -> None:
    """
    Calls Qt's 'void QDesignerWidgetBoxInterface::addWidget(int cat_idx,
    const Widget &wgt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#addWidget

    Parameters
    ----------

    cat_idx : int
      Passed on as it is.

    wgt : Widget
      Passed on as a value: Qt reads the C++
      QDesignerWidgetBoxInterface::Widget, which stays Python's own.
    """
    #  void QDesignerWidgetBoxInterface::addWidget(int cat_idx, const Widget
    #      &wgt)
    self.uglySide.call(
        'ritual_ZN27QDesignerWidgetBoxInterface9addWidgetEiRKNS_6WidgetE',
        cat_idx, self._valueOf(wgt),
    )

  @overload(int, int)
  def removeWidget(self, cat_idx: int, wgt_idx: int) -> None:
    """
    Calls Qt's 'void QDesignerWidgetBoxInterface::removeWidget(int cat_idx,
    int wgt_idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#removeWidget

    Parameters
    ----------

    cat_idx : int
      Passed on as it is.

    wgt_idx : int
      Passed on as it is.
    """
    #  void QDesignerWidgetBoxInterface::removeWidget(int cat_idx, int
    #      wgt_idx)
    self.uglySide.call(
        'ritual_ZN27QDesignerWidgetBoxInterface12removeWidgetEii',
        cat_idx, wgt_idx,
    )

  @overload(str)
  def findOrInsertCategory(self, categoryName: str) -> int:
    """
    Calls Qt's 'int QDesignerWidgetBoxInterface::findOrInsertCategory(const
    QString &categoryName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html

    Parameters
    ----------

    categoryName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QDesignerWidgetBoxInterface::findOrInsertCategory(const QString
    #      &categoryName)
    return self.uglySide.call(
        'ritual_ZN27QDesignerWidgetBoxInterface20findOrInsertCategoryERK7QS'
        'tring',
        categoryName,
    )

  @overload(QList[QDesignerDnDItemInterface], QPoint)
  def dropWidgets(
      self,
      item_list: QList[QDesignerDnDItemInterface],
      global_mouse_pos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QDesignerWidgetBoxInterface::dropWidgets(const
    QList<QDesignerDnDItemInterface *> &item_list, const QPoint
    &global_mouse_pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#dropWidgets

    Parameters
    ----------

    item_list : QList[QDesignerDnDItemInterface]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    global_mouse_pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QDesignerWidgetBoxInterface::dropWidgets(const
    #      QList<QDesignerDnDItemInterface *> &item_list, const QPoint
    #      &global_mouse_pos)
    self.uglySide.call(
        'ritual_ZN27QDesignerWidgetBoxInterface11dropWidgetsERK5QListIP25QD'
        'esignerDnDItemInterfaceERK6QPoint',
        self._valueOf(item_list), self._valueOf(global_mouse_pos),
    )

  def load(self) -> bool:
    """
    Calls Qt's 'bool QDesignerWidgetBoxInterface::load()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#load
    """
    #  bool QDesignerWidgetBoxInterface::load()
    return self.uglySide.call(
        'ritual_ZN27QDesignerWidgetBoxInterface4loadEv',
    )

  def save(self) -> bool:
    """
    Calls Qt's 'bool QDesignerWidgetBoxInterface::save()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerwidgetboxinterface.html#save
    """
    #  bool QDesignerWidgetBoxInterface::save()
    return self.uglySide.call(
        'ritual_ZN27QDesignerWidgetBoxInterface4saveEv',
    )
