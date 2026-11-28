"""
qdesigner_internal::QDesignerWidgetBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_widgetbox_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerWidgetBox to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QDesignerWidgetBoxInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QString
  from ..QtGui import QIcon
  from . import DomUI
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerWidgetBox(QDesignerWidgetBoxInterface):
  """
  The cute side of Qt's qdesigner_internal::QDesignerWidgetBox: a plain
  Python object standing in front of one C++
  qdesigner_internal::QDesignerWidgetBox.

  It is built on the cute 'QDesignerWidgetBoxInterface', as Qt's
  qdesigner_internal::QDesignerWidgetBox is built on Qt's
  QDesignerWidgetBoxInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerWidgetBox that has a
  ritual and that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'loadMode', 'setLoadMode', 'loadContents', 'iconForWidget', 'findWidget',
  'xmlToUi'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::QDesignerWidgetBox::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::QDesignerWidgetBox::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerWidgetBox is created at the first
    use, not by 'qdesigner_internal::QDesignerWidgetBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QDesignerWidgetBox.
  - Qt tells when it has removed the C++
    qdesigner_internal::QDesignerWidgetBox. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's qdesigner_internal::QDesignerWidgetBox that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside qdesigner_internal::QDesignerWidgetBox, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class LoadMode(CuteNum):
    """
    The enum 'qdesigner_internal::QDesignerWidgetBox::LoadMode' of Qt, with
    the 3 names Qt gives in it.
    """

    LoadMerge = Kee[int](0)
    LoadReplace = Kee[int](1)
    LoadCustomWidgetsOnly = Kee[int](2)

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
    Calls Qt's 'QString qdesigner_internal::QDesignerWidgetBox::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetbox.html#tr

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
    #  QString qdesigner_internal::QDesignerWidgetBox::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal18QDesignerWidgetBox2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(
      QDesignerWidgetBoxInterface, str, str,
      QDesignerWidgetBoxInterface.Widget,
  )
  @overload(QDesignerWidgetBoxInterface, str, str, NoneType)
  @overload(NoneType, str, str, QDesignerWidgetBoxInterface.Widget)
  @overload(NoneType, str, str, NoneType)
  def findWidget(
      wbox: Optional[QDesignerWidgetBoxInterface],
      className: str,
      category: str,
      widgetData: Optional[QDesignerWidgetBoxInterface.Widget],
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::QDesignerWidgetBox::findWidget(const
    QDesignerWidgetBoxInterface *wbox, const QString &className, const
    QString &category, Widget *widgetData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetbox.html

    Parameters
    ----------

    wbox : Optional[QDesignerWidgetBoxInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    className : str
      Passed on as it is: a QString is made of it for the call.

    category : str
      Passed on as it is: a QString is made of it for the call.

    widgetData : Optional[QDesignerWidgetBoxInterface.Widget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerWidgetBox::findWidget(const
    #      QDesignerWidgetBoxInterface *wbox, const QString &className, const
    #      QString &category, Widget *widgetData)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal18QDesignerWidgetBox10findWidgetEPK27'
        'QDesignerWidgetBoxInterfaceRK7QStringS6_PNS1_6WidgetE',
        CuteMixin._addressOf(wbox), className, category,
        CuteMixin._addressOf(widgetData),
    )

  @staticmethod
  @overload(str, str, bool, QString)
  @overload(str, str, bool, NoneType)
  def xmlToUi(
      name: str,
      xml: str,
      insertFakeTopLevel: bool,
      errorMessage: Optional[QString],
  ) -> Optional[DomUI]:
    """
    Calls Qt's 'DomUI *qdesigner_internal::QDesignerWidgetBox::xmlToUi(const
    QString &name, const QString &xml, bool insertFakeTopLevel, QString
    *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetbox.html#xmlToUi

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    xml : str
      Passed on as it is: a QString is made of it for the call.

    insertFakeTopLevel : bool
      Passed on as it is.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[DomUI]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomUI *qdesigner_internal::QDesignerWidgetBox::xmlToUi(const QString
    #      &name, const QString &xml, bool insertFakeTopLevel, QString
    #      *errorMessage)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal18QDesignerWidgetBox7xmlToUiERK7QStri'
        'ngS3_bPS1_',
        name, xml, insertFakeTopLevel, CuteMixin._addressOf(errorMessage),
    )
    from . import DomUI
    return DomUI._cuteAt(address)

  @staticmethod
  @overload(str, str, bool)
  def xmlToUi(
      name: str,
      xml: str,
      insertFakeTopLevel: bool,
  ) -> Optional[DomUI]:
    """
    Calls Qt's 'DomUI *qdesigner_internal::QDesignerWidgetBox::xmlToUi(const
    QString &name, const QString &xml, bool insertFakeTopLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetbox.html#xmlToUi

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    xml : str
      Passed on as it is: a QString is made of it for the call.

    insertFakeTopLevel : bool
      Passed on as it is.

    Returns
    -------

    Optional[DomUI]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomUI *qdesigner_internal::QDesignerWidgetBox::xmlToUi(const QString
    #      &name, const QString &xml, bool insertFakeTopLevel)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal18QDesignerWidgetBox7xmlToUiERK7QStri'
        'ngS3_b',
        name, xml, insertFakeTopLevel,
    )
    from . import DomUI
    return DomUI._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerWidgetBox'

  #  The functions Qt calls itself that
  #  qdesigner_internal::QDesignerWidgetBox is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'loadContents': (
          ('_ZN18qdesigner_internal18QDesignerWidgetBox12loadContentsERK7QS'
           'tring',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'iconForWidget': (
          ('_ZNK18qdesigner_internal18QDesignerWidgetBox13iconForWidgetERK7'
           'QStringS3_',
           ('address', 'value', 'QtGui:QIcon'),
           (
               ('address', 'text', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::QDesignerWidgetBox::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetbox.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::QDesignerWidgetBox::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18QDesignerWidgetBox10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def loadMode(self) -> LoadMode:
    """
    Calls Qt's 'LoadMode qdesigner_internal::QDesignerWidgetBox::loadMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetbox.html

    Returns
    -------

    LoadMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LoadMode(number)' gives.
    """
    #  LoadMode qdesigner_internal::QDesignerWidgetBox::loadMode() const
    return QDesignerWidgetBox.LoadMode(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18QDesignerWidgetBox8loadModeEv',
    ))

  @overload(str)
  @overload(str, str)
  def iconForWidget(self, className: str, category: str = '') -> QIcon:
    """
    Calls Qt's 'QIcon
    qdesigner_internal::QDesignerWidgetBox::iconForWidget(const QString
    &className, const QString &category) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetbox.html

    Parameters
    ----------

    className : str
      Passed on as it is: a QString is made of it for the call.

    category : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon qdesigner_internal::QDesignerWidgetBox::iconForWidget(const
    #      QString &className, const QString &category) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18QDesignerWidgetBox13iconForWidgetE'
        'RK7QStringS3_',
        className, category,
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(LoadMode)
  def setLoadMode(self, lm: LoadMode) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerWidgetBox::setLoadMode(LoadMode lm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetbox.html

    Parameters
    ----------

    lm : LoadMode
      Passed on as its number.
    """
    #  void qdesigner_internal::QDesignerWidgetBox::setLoadMode(LoadMode lm)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18QDesignerWidgetBox11setLoadModeENS0'
        '_8LoadModeE',
        lm.value,
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
    Qt's 'qdesigner_internal::QDesignerWidgetBox::QDesignerWidgetBox(QWidget
    *parent, Qt::WindowFlags flags)': the class is abstract, so C++ cannot
    make one, and the C++ class of ours does not fill in every function it
    leaves open.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerWidgetBox.__init__' has no cute "
        "function yet. Qt's "
        "'qdesigner_internal::QDesignerWidgetBox::QDesignerWidgetBox(QWidget"
        " *parent, Qt::WindowFlags flags)': the class is abstract, so C++ "
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

  @overload(str)
  def loadContents(self, contents: str) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerWidgetBox::loadContents(const QString
    &contents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerwidgetbox.html

    Parameters
    ----------

    contents : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool qdesigner_internal::QDesignerWidgetBox::loadContents(const
    #      QString &contents)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal18QDesignerWidgetBox12loadContentsERK'
        '7QString',
        contents,
    )
