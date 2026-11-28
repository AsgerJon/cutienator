"""
qdesigner_internal::LayoutHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::LayoutHelper to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect
  from ..QtWidgets import QLayout, QWidget
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QLayout = WAIT['QLayout']
  QRect = WAIT['QRect']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LayoutHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::LayoutHelper: a plain Python
  object standing in front of one C++ qdesigner_internal::LayoutHelper.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::LayoutHelper that has a ritual
  and that Python can call so far, 9 names in all: 'indexOf', 'itemInfo',
  'insertWidget', 'removeWidget', 'replaceWidget', 'canSimplify', 'simplify',
  'pushState', 'popState'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::LayoutHelper::~LayoutHelper()': the destructor:
    Python never removes a C++ qdesigner_internal::LayoutHelper.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 2 forbidden; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ qdesigner_internal::LayoutHelper is created at the first use, not
    by 'qdesigner_internal::LayoutHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::LayoutHelper.
  - Each name of Qt's qdesigner_internal::LayoutHelper that has no cute
    function yet, 'createLayoutHelper', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QLayout, QWidget)
  @overload(QLayout, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def indexOf(lt: Optional[QLayout], widget: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int qdesigner_internal::LayoutHelper::indexOf(const QLayout
    *lt, const QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#indexOf

    Parameters
    ----------

    lt : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int qdesigner_internal::LayoutHelper::indexOf(const QLayout *lt, const
    #      QWidget *widget)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal12LayoutHelper7indexOfEPK7QLayoutPK7Q'
        'Widget',
        CuteMixin._addressOf(lt), CuteMixin._addressOf(widget),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::LayoutHelper'

  #  A C++ qdesigner_internal::LayoutHelper Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_LayoutHelper'

  #  The functions Qt calls itself that qdesigner_internal::LayoutHelper is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'itemInfo': (
          ('_ZNK18qdesigner_internal12LayoutHelper8itemInfoEP7QLayouti',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('address', 'address', 'QtWidgets:QLayout'),
               ('int', 'number', ''),
           )),
      ),
      'insertWidget': (
          ('_ZN18qdesigner_internal12LayoutHelper12insertWidgetEP7QLayoutRK'
           '5QRectP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QLayout'),
               ('address', 'value', 'QtCore:QRect'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'removeWidget': (
          ('_ZN18qdesigner_internal12LayoutHelper12removeWidgetEP7QLayoutP7'
           'QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QLayout'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'replaceWidget': (
          ('_ZN18qdesigner_internal12LayoutHelper13replaceWidgetEP7QLayoutP'
           '7QWidgetS4_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QLayout'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'canSimplify': (
          ('_ZNK18qdesigner_internal12LayoutHelper11canSimplifyEPK28QDesign'
           'erFormEditorInterfacePK7QWidgetRK5QRect',
           ('bool', 'number', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormEditorInterface'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'simplify': (
          ('_ZN18qdesigner_internal12LayoutHelper8simplifyEPK28QDesignerFor'
           'mEditorInterfaceP7QWidgetRK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormEditorInterface'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'pushState': (
          ('_ZN18qdesigner_internal12LayoutHelper9pushStateEPK28QDesignerFo'
           'rmEditorInterfacePK7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormEditorInterface'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'popState': (
          ('_ZN18qdesigner_internal12LayoutHelper8popStateEPK28QDesignerFor'
           'mEditorInterfaceP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormEditorInterface'),
               ('address', 'address', 'QtWidgets:QWidget'),
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

  @overload(QLayout, QWidget)
  @overload(QLayout, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def itemInfo(
      self,
      lt: Optional[QLayout],
      widget: Optional[QWidget],
  ) -> QRect:
    """
    Calls Qt's 'QRect qdesigner_internal::LayoutHelper::itemInfo(QLayout *lt,
    const QWidget *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#itemInfo

    Parameters
    ----------

    lt : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect qdesigner_internal::LayoutHelper::itemInfo(QLayout *lt, const
    #      QWidget *widget) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12LayoutHelper8itemInfoEP7QLayoutPK7'
        'QWidget',
        self._addressOf(lt), self._addressOf(widget),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QLayout, int)
  @overload(NoneType, int)
  def itemInfo(self, lt: Optional[QLayout], index: int) -> QRect:
    """
    Calls Qt's 'QRect qdesigner_internal::LayoutHelper::itemInfo(QLayout *lt,
    int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#itemInfo

    Parameters
    ----------

    lt : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect qdesigner_internal::LayoutHelper::itemInfo(QLayout *lt, int
    #      index) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12LayoutHelper8itemInfoEP7QLayouti',
        self._addressOf(lt), index,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QDesignerFormEditorInterface, QWidget, QRect)
  @overload(QDesignerFormEditorInterface, NoneType, QRect)
  @overload(NoneType, QWidget, QRect)
  @overload(NoneType, NoneType, QRect)
  def canSimplify(
      self,
      core: Optional[QDesignerFormEditorInterface],
      widgetWithManagedLayout: Optional[QWidget],
      restrictionArea: QRect,
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::LayoutHelper::canSimplify(const
    QDesignerFormEditorInterface *core, const QWidget
    *widgetWithManagedLayout, const QRect &restrictionArea) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#canSimplify

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widgetWithManagedLayout : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    restrictionArea : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  bool qdesigner_internal::LayoutHelper::canSimplify(const
    #      QDesignerFormEditorInterface *core, const QWidget
    #      *widgetWithManagedLayout, const QRect &restrictionArea) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12LayoutHelper11canSimplifyEPK28QDes'
        'ignerFormEditorInterfacePK7QWidgetRK5QRect',
        self._addressOf(core), self._addressOf(widgetWithManagedLayout),
        self._valueOf(restrictionArea),
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
    Notes what was given, for Qt's
    'qdesigner_internal::LayoutHelper::LayoutHelper()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#LayoutHelper
    """
    #  qdesigner_internal::LayoutHelper::LayoutHelper()
    self._noteCreation(LayoutHelper, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal12LayoutHelperC1Ev',
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

  @overload(QLayout, QRect, QWidget)
  @overload(QLayout, QRect, NoneType)
  @overload(NoneType, QRect, QWidget)
  @overload(NoneType, QRect, NoneType)
  def insertWidget(
      self,
      lt: Optional[QLayout],
      info: QRect,
      w: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutHelper::insertWidget(QLayout
    *lt, const QRect &info, QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#insertWidget

    Parameters
    ----------

    lt : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    info : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::LayoutHelper::insertWidget(QLayout *lt, const
    #      QRect &info, QWidget *w)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12LayoutHelper12insertWidgetEP7QLayou'
        'tRK5QRectP7QWidget',
        self._addressOf(lt), self._valueOf(info), self._addressOf(w),
    )

  @overload(QLayout, QWidget)
  @overload(QLayout, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def removeWidget(
      self,
      lt: Optional[QLayout],
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutHelper::removeWidget(QLayout
    *lt, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#removeWidget

    Parameters
    ----------

    lt : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::LayoutHelper::removeWidget(QLayout *lt,
    #      QWidget *widget)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12LayoutHelper12removeWidgetEP7QLayou'
        'tP7QWidget',
        self._addressOf(lt), self._addressOf(widget),
    )

  @overload(QLayout, QWidget, QWidget)
  @overload(QLayout, QWidget, NoneType)
  @overload(QLayout, NoneType, QWidget)
  @overload(QLayout, NoneType, NoneType)
  @overload(NoneType, QWidget, QWidget)
  @overload(NoneType, QWidget, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def replaceWidget(
      self,
      lt: Optional[QLayout],
      before: Optional[QWidget],
      after: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutHelper::replaceWidget(QLayout
    *lt, QWidget *before, QWidget *after)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#replaceWidget

    Parameters
    ----------

    lt : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    before : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    after : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::LayoutHelper::replaceWidget(QLayout *lt,
    #      QWidget *before, QWidget *after)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12LayoutHelper13replaceWidgetEP7QLayo'
        'utP7QWidgetS4_',
        self._addressOf(lt), self._addressOf(before), self._addressOf(after),
    )

  @overload(QDesignerFormEditorInterface, QWidget, QRect)
  @overload(QDesignerFormEditorInterface, NoneType, QRect)
  @overload(NoneType, QWidget, QRect)
  @overload(NoneType, NoneType, QRect)
  def simplify(
      self,
      core: Optional[QDesignerFormEditorInterface],
      widgetWithManagedLayout: Optional[QWidget],
      restrictionArea: QRect,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutHelper::simplify(const
    QDesignerFormEditorInterface *core, QWidget *widgetWithManagedLayout,
    const QRect &restrictionArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#simplify

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widgetWithManagedLayout : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    restrictionArea : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void qdesigner_internal::LayoutHelper::simplify(const
    #      QDesignerFormEditorInterface *core, QWidget
    #      *widgetWithManagedLayout, const QRect &restrictionArea)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12LayoutHelper8simplifyEPK28QDesigner'
        'FormEditorInterfaceP7QWidgetRK5QRect',
        self._addressOf(core), self._addressOf(widgetWithManagedLayout),
        self._valueOf(restrictionArea),
    )

  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def pushState(
      self,
      core: Optional[QDesignerFormEditorInterface],
      widgetWithManagedLayout: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutHelper::pushState(const
    QDesignerFormEditorInterface *core, const QWidget
    *widgetWithManagedLayout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#pushState

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widgetWithManagedLayout : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::LayoutHelper::pushState(const
    #      QDesignerFormEditorInterface *core, const QWidget
    #      *widgetWithManagedLayout)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12LayoutHelper9pushStateEPK28QDesigne'
        'rFormEditorInterfacePK7QWidget',
        self._addressOf(core), self._addressOf(widgetWithManagedLayout),
    )

  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def popState(
      self,
      core: Optional[QDesignerFormEditorInterface],
      widgetWithManagedLayout: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::LayoutHelper::popState(const
    QDesignerFormEditorInterface *core, QWidget *widgetWithManagedLayout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-layouthelper.html#popState

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widgetWithManagedLayout : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::LayoutHelper::popState(const
    #      QDesignerFormEditorInterface *core, QWidget
    #      *widgetWithManagedLayout)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12LayoutHelper8popStateEPK28QDesigner'
        'FormEditorInterfaceP7QWidget',
        self._addressOf(core), self._addressOf(widgetWithManagedLayout),
    )

  @staticmethod
  def createLayoutHelper(*__, **_) -> Never:
    """
    Qt's 'LayoutHelper
    *qdesigner_internal::LayoutHelper::createLayoutHelper(int type)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'BoxLayoutHelper'; did you mean
    'LayoutHelper'?.
    """
    raise NotImplementedError(
        "'qdesigner_internal.LayoutHelper.createLayoutHelper' has no cute "
        "function yet. Qt's 'LayoutHelper "
        "*qdesigner_internal::LayoutHelper::createLayoutHelper(int type)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: unknown type name "
        "'BoxLayoutHelper'; did you mean 'LayoutHelper'?.")
