"""
QDesignerFormWindowManagerInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractformwindowmanager.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QAction, QActionGroup, QPixmap
  from ..QtWidgets import QWidget
  from . import QDesignerDnDItemInterface, QDesignerFormEditorInterface
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerDnDItemInterface = WAIT['QDesignerDnDItemInterface']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerFormWindowManagerInterface(QObject):
  """
  The cute side of Qt's QDesignerFormWindowManagerInterface: a plain Python
  object standing in front of one C++ QDesignerFormWindowManagerInterface.

  It is built on the cute 'QObject', as Qt's
  QDesignerFormWindowManagerInterface is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerFormWindowManagerInterface that has a
  ritual and that Python can call so far, 39 names in all: 'metaObject',
  'tr', 'action', 'actionGroup', 'actionCut', 'actionCopy', 'actionPaste',
  'actionDelete', 'actionSelectAll', 'actionLower', 'actionRaise',
  'actionUndo', 'actionRedo', 'actionHorizontalLayout',
  'actionVerticalLayout', 'actionSplitHorizontal', 'actionSplitVertical',
  'actionGridLayout', 'actionFormLayout', 'actionBreakLayout',
  'actionAdjustSize', 'actionSimplifyLayout', 'activeFormWindow',
  'formWindowCount', 'formWindow', 'createFormWindow', 'core', 'dragItems',
  'createPreviewPixmap', 'formWindowAdded', 'formWindowRemoved',
  'activeFormWindowChanged', 'formWindowSettingsChanged', 'addFormWindow',
  'removeFormWindow', 'setActiveFormWindow', 'showPreview',
  'closeAllPreviews', 'showPluginDialog'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerFormWindowManagerInterface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QDesignerFormWindowManagerInterface::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerFormWindowManagerInterface::
    ~QDesignerFormWindowManagerInterface()': the destructor: Python never
    removes a C++ QDesignerFormWindowManagerInterface.

  What has no ritual
  ------------------

  3 of the 45 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerFormWindowManagerInterface is created at the first use,
    not by 'QDesignerFormWindowManagerInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerFormWindowManagerInterface.
  - Qt tells when it has removed the C++ QDesignerFormWindowManagerInterface.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDesignerFormWindowManagerInterface that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDesignerFormWindowManagerInterface, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Action(CuteNum):
    """
    The enum 'QDesignerFormWindowManagerInterface::Action' of Qt, with the 20
    names Qt gives in it.
    """

    CutAction = Kee[int](100)
    CopyAction = Kee[int](101)
    PasteAction = Kee[int](102)
    DeleteAction = Kee[int](103)
    SelectAllAction = Kee[int](104)
    LowerAction = Kee[int](200)
    RaiseAction = Kee[int](201)
    UndoAction = Kee[int](300)
    RedoAction = Kee[int](301)
    HorizontalLayoutAction = Kee[int](400)
    VerticalLayoutAction = Kee[int](401)
    SplitHorizontalAction = Kee[int](402)
    SplitVerticalAction = Kee[int](403)
    GridLayoutAction = Kee[int](404)
    FormLayoutAction = Kee[int](405)
    BreakLayoutAction = Kee[int](406)
    AdjustSizeAction = Kee[int](407)
    SimplifyLayoutAction = Kee[int](408)
    DefaultPreviewAction = Kee[int](500)
    FormWindowSettingsDialogAction = Kee[int](600)

  class ActionGroup(CuteNum):
    """
    The enum 'QDesignerFormWindowManagerInterface::ActionGroup' of Qt, with
    the 1 names Qt gives in it.
    """

    StyledPreviewActionGroup = Kee[int](100)

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
    Calls Qt's 'QString QDesignerFormWindowManagerInterface::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html#tr

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
    #  QString QDesignerFormWindowManagerInterface::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerFormWindowManagerInterface'

  #  A C++ QDesignerFormWindowManagerInterface Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerFormWindowManagerInterface'

  #  The functions Qt calls itself that QDesignerFormWindowManagerInterface
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dragItems': (
          'void QDesignerFormWindowManagerInterface::dragItems(const '
          'QList<QDesignerDnDItemInterface *> &)',
      ),
  }

  #  The functions Qt calls itself that QDesignerFormWindowManagerInterface
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'action': (
          ('_ZNK35QDesignerFormWindowManagerInterface6actionENS_6ActionE',
           ('address', 'address', 'QtGui:QAction'),
           (
               ('int', 'enum',
                'QtDesigner:QDesignerFormWindowManagerInterface.Action'),
           )),
      ),
      'actionGroup': (
          ('_ZNK35QDesignerFormWindowManagerInterface11actionGroupENS_11Act'
           'ionGroupE',
           ('address', 'address', 'QtGui:QActionGroup'),
           (
               ('int', 'enum',
                'QtDesigner:QDesignerFormWindowManagerInterface.ActionGroup'),
           )),
      ),
      'activeFormWindow': (
          ('_ZNK35QDesignerFormWindowManagerInterface16activeFormWindowEv',
           ('address', 'address', 'QtDesigner:QDesignerFormWindowInterface'),
           ()),
      ),
      'formWindowCount': (
          ('_ZNK35QDesignerFormWindowManagerInterface15formWindowCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'formWindow': (
          ('_ZNK35QDesignerFormWindowManagerInterface10formWindowEi',
           ('address', 'address', 'QtDesigner:QDesignerFormWindowInterface'),
           (
               ('int', 'number', ''),
           )),
      ),
      'createFormWindow': (
          ('_ZN35QDesignerFormWindowManagerInterface16createFormWindowEP7QW'
           'idget6QFlagsIN2Qt10WindowTypeEE',
           ('address', 'address', 'QtDesigner:QDesignerFormWindowInterface'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('int', 'flags', 'QtCore:Qt.WindowType'),
           )),
      ),
      'core': (
          ('_ZNK35QDesignerFormWindowManagerInterface4coreEv',
           ('address', 'address', 'QtDesigner:QDesignerFormEditorInterface'),
           ()),
      ),
      'createPreviewPixmap': (
          ('_ZNK35QDesignerFormWindowManagerInterface19createPreviewPixmapE'
           'v',
           ('address', 'value', 'QtGui:QPixmap'),
           ()),
      ),
      'addFormWindow': (
          ('_ZN35QDesignerFormWindowManagerInterface13addFormWindowEP28QDes'
           'ignerFormWindowInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormWindowInterface'),
           )),
      ),
      'removeFormWindow': (
          ('_ZN35QDesignerFormWindowManagerInterface16removeFormWindowEP28Q'
           'DesignerFormWindowInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormWindowInterface'),
           )),
      ),
      'setActiveFormWindow': (
          ('_ZN35QDesignerFormWindowManagerInterface19setActiveFormWindowEP'
           '28QDesignerFormWindowInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormWindowInterface'),
           )),
      ),
      'showPreview': (
          ('_ZN35QDesignerFormWindowManagerInterface11showPreviewEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'closeAllPreviews': (
          ('_ZN35QDesignerFormWindowManagerInterface16closeAllPreviewsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'showPluginDialog': (
          ('_ZN35QDesignerFormWindowManagerInterface16showPluginDialogEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject
    *QDesignerFormWindowManagerInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerFormWindowManagerInterface::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(Action)
  def action(self, action: Action) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormWindowManagerInterface::action(Action
    action) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html#action

    Parameters
    ----------

    action : Action
      Passed on as its number.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::action(Action action)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface6actionENS_6ActionE',
        action.value,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(ActionGroup)
  def actionGroup(self, actionGroup: ActionGroup) -> Optional[QActionGroup]:
    """
    Calls Qt's 'QActionGroup
    *QDesignerFormWindowManagerInterface::actionGroup(ActionGroup
    actionGroup) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Parameters
    ----------

    actionGroup : ActionGroup
      Passed on as its number.

    Returns
    -------

    Optional[QActionGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionGroup
    #      *QDesignerFormWindowManagerInterface::actionGroup(ActionGroup
    #      actionGroup) const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface11actionGroupENS_11'
        'ActionGroupE',
        actionGroup.value,
    )
    from ..QtGui import QActionGroup
    return QActionGroup._cuteAt(address)

  def actionCut(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormWindowManagerInterface::actionCut()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html#actionCut

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionCut() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface9actionCutEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionCopy(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormWindowManagerInterface::actionCopy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionCopy() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface10actionCopyEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionPaste(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormWindowManagerInterface::actionPaste()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionPaste() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface11actionPasteEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionDelete(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormWindowManagerInterface::actionDelete()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionDelete() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface12actionDeleteEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionSelectAll(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *QDesignerFormWindowManagerInterface::actionSelectAll() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionSelectAll() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface15actionSelectAllEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionLower(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormWindowManagerInterface::actionLower()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionLower() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface11actionLowerEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionRaise(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormWindowManagerInterface::actionRaise()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionRaise() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface11actionRaiseEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionUndo(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormWindowManagerInterface::actionUndo()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionUndo() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface10actionUndoEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionRedo(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormWindowManagerInterface::actionRedo()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionRedo() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface10actionRedoEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionHorizontalLayout(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *QDesignerFormWindowManagerInterface::actionHorizontalLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionHorizontalLayout()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface22actionHorizontalL'
        'ayoutEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionVerticalLayout(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *QDesignerFormWindowManagerInterface::actionVerticalLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionVerticalLayout()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface20actionVerticalLay'
        'outEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionSplitHorizontal(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *QDesignerFormWindowManagerInterface::actionSplitHorizontal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionSplitHorizontal()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface21actionSplitHorizo'
        'ntalEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionSplitVertical(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *QDesignerFormWindowManagerInterface::actionSplitVertical() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionSplitVertical()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface19actionSplitVertic'
        'alEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionGridLayout(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *QDesignerFormWindowManagerInterface::actionGridLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionGridLayout() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface16actionGridLayoutE'
        'v',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionFormLayout(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *QDesignerFormWindowManagerInterface::actionFormLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionFormLayout() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface16actionFormLayoutE'
        'v',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionBreakLayout(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *QDesignerFormWindowManagerInterface::actionBreakLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionBreakLayout()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface17actionBreakLayout'
        'Ev',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionAdjustSize(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *QDesignerFormWindowManagerInterface::actionAdjustSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionAdjustSize() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface16actionAdjustSizeE'
        'v',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionSimplifyLayout(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *QDesignerFormWindowManagerInterface::actionSimplifyLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowManagerInterface::actionSimplifyLayout()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface20actionSimplifyLay'
        'outEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def activeFormWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *QDesignerFormWindowManagerInterface::activeFormWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *QDesignerFormWindowManagerInterface::activeFormWindow() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface16activeFormWindowE'
        'v',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def formWindowCount(self) -> int:
    """
    Calls Qt's 'int QDesignerFormWindowManagerInterface::formWindowCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html
    """
    #  int QDesignerFormWindowManagerInterface::formWindowCount() const
    return self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface15formWindowCountEv',
    )

  @overload(int)
  def formWindow(self, index: int) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *QDesignerFormWindowManagerInterface::formWindow(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *QDesignerFormWindowManagerInterface::formWindow(int index) const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface10formWindowEi',
        index,
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerFormWindowManagerInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface
    #      *QDesignerFormWindowManagerInterface::core() const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface4coreEv',
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  def createPreviewPixmap(self) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    QDesignerFormWindowManagerInterface::createPreviewPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QDesignerFormWindowManagerInterface::createPreviewPixmap()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK35QDesignerFormWindowManagerInterface19createPreviewPixm'
        'apEv',
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def setActiveFormWindow(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowManagerInterface::setActiveFormWindow(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowManagerInterface::setActiveFormWindow(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface19setActiveFormWindo'
        'wEP28QDesignerFormWindowInterface',
        self._addressOf(formWindow),
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
    Qt's 'QDesignerFormWindowManagerInterface::
    QDesignerFormWindowManagerInterface(QObject *parent)': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QDesignerFormWindowManagerInterface.__init__' has no cute "
        "function yet. Qt's "
        "'QDesignerFormWindowManagerInterface::QDesignerFormWindowManagerInt"
        "erface(QObject *parent)': the class is abstract, so C++ cannot "
        "make one, and the C++ class of ours does not fill in every "
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

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def createFormWindow(
      self,
      parentWidget: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *QDesignerFormWindowManagerInterface::createFormWindow(QWidget
    *parentWidget, Qt::WindowFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Parameters
    ----------

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *QDesignerFormWindowManagerInterface::createFormWindow(QWidget
    #      *parentWidget, Qt::WindowFlags flags)
    address = self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface16createFormWindowEP'
        '7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parentWidget), flags.value,
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  @overload(QList[QDesignerDnDItemInterface])
  def dragItems(self, item_list: QList[QDesignerDnDItemInterface]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowManagerInterface::dragItems(const
    QList<QDesignerDnDItemInterface *> &item_list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html#dragItems

    Parameters
    ----------

    item_list : QList[QDesignerDnDItemInterface]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDesignerFormWindowManagerInterface::dragItems(const
    #      QList<QDesignerDnDItemInterface *> &item_list)
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface9dragItemsERK5QListI'
        'P25QDesignerDnDItemInterfaceE',
        self._valueOf(item_list),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def formWindowAdded(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowManagerInterface::formWindowAdded(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowManagerInterface::formWindowAdded(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface15formWindowAddedEP2'
        '8QDesignerFormWindowInterface',
        self._addressOf(formWindow),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def formWindowRemoved(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowManagerInterface::formWindowRemoved(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowManagerInterface::formWindowRemoved(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface17formWindowRemovedE'
        'P28QDesignerFormWindowInterface',
        self._addressOf(formWindow),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def activeFormWindowChanged(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowManagerInterface::activeFormWindowChanged(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowManagerInterface::activeFormWindowChanged(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface23activeFormWindowCh'
        'angedEP28QDesignerFormWindowInterface',
        self._addressOf(formWindow),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def formWindowSettingsChanged(
      self,
      fw: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowManagerInterface::formWindowSettingsChanged(
    QDesignerFormWindowInterface *fw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowManagerInterface::formWindowSettingsChanged(
    #      QDesignerFormWindowInterface *fw)
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface25formWindowSettings'
        'ChangedEP28QDesignerFormWindowInterface',
        self._addressOf(fw),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def addFormWindow(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowManagerInterface::addFormWindow(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowManagerInterface::addFormWindow(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface13addFormWindowEP28Q'
        'DesignerFormWindowInterface',
        self._addressOf(formWindow),
    )

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def removeFormWindow(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowManagerInterface::removeFormWindow(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowManagerInterface::removeFormWindow(
    #      QDesignerFormWindowInterface *formWindow)
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface16removeFormWindowEP'
        '28QDesignerFormWindowInterface',
        self._addressOf(formWindow),
    )

  def showPreview(self) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowManagerInterface::showPreview()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html
    """
    #  void QDesignerFormWindowManagerInterface::showPreview()
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface11showPreviewEv',
    )

  def closeAllPreviews(self) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowManagerInterface::closeAllPreviews()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html
    """
    #  void QDesignerFormWindowManagerInterface::closeAllPreviews()
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface16closeAllPreviewsEv',
    )

  def showPluginDialog(self) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowManagerInterface::showPluginDialog()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowmanagerinterface.html
    """
    #  void QDesignerFormWindowManagerInterface::showPluginDialog()
    self.uglySide.call(
        'ritual_ZN35QDesignerFormWindowManagerInterface16showPluginDialogEv',
    )
