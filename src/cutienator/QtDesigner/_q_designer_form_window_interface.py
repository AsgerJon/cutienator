"""
QDesignerFormWindowInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractformwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDir, QIODevice, QMetaObject, QPoint, QString
  from ..QtGui import QUndoStack
  from . import QDesignerFormEditorInterface
  from . import QDesignerFormWindowCursorInterface
  from . import QDesignerFormWindowToolInterface, QtResourceSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowToolInterface = WAIT['QDesignerFormWindowToolInterface']
  QIODevice = WAIT['QIODevice']
  QPoint = WAIT['QPoint']
  QString = WAIT['QString']
  QtResourceSet = WAIT['QtResourceSet']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerFormWindowInterface(QWidget):
  """
  The cute side of Qt's QDesignerFormWindowInterface: a plain Python object
  standing in front of one C++ QDesignerFormWindowInterface.

  It is built on the cute 'QWidget', as Qt's QDesignerFormWindowInterface is
  built on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerFormWindowInterface that has a ritual and
  that Python can call so far, 72 names in all: 'metaObject', 'tr',
  'fileName', 'absoluteDir', 'contents', 'checkContents', 'setContents',
  'features', 'hasFeature', 'author', 'setAuthor', 'comment', 'setComment',
  'setLayoutDefault', 'layoutFunction', 'setLayoutFunction',
  'pixmapFunction', 'setPixmapFunction', 'exportMacro', 'setExportMacro',
  'includeHints', 'setIncludeHints', 'resourceFileSaveMode',
  'setResourceFileSaveMode', 'resourceSet', 'setResourceSet',
  'activeResourceFilePaths', 'core', 'cursor', 'toolCount', 'currentTool',
  'setCurrentTool', 'tool', 'registerTool', 'grid', 'mainContainer',
  'setMainContainer', 'formContainer', 'isManaged', 'isDirty',
  'findFormWindow', 'commandHistory', 'beginCommand', 'endCommand',
  'emitSelectionChanged', 'resourceFiles', 'addResourceFile',
  'removeResourceFile', 'ensureUniqueObjectName', 'manageWidget',
  'unmanageWidget', 'setFeatures', 'setDirty', 'clearSelection',
  'selectWidget', 'setGrid', 'setFileName', 'editWidgets',
  'mainContainerChanged', 'toolChanged', 'fileNameChanged', 'featureChanged',
  'selectionChanged', 'geometryChanged', 'resourceFilesChanged',
  'widgetManaged', 'widgetUnmanaged', 'aboutToUnmanageWidget', 'activated',
  'changed', 'widgetRemoved', 'objectRemoved'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerFormWindowInterface::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDesignerFormWindowInterface::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerFormWindowInterface::~QDesignerFormWindowInterface()': the
    destructor: Python never removes a C++ QDesignerFormWindowInterface.
  - Qt's 'void QDesignerFormWindowInterface::layoutDefault(int *margin, int
    *spacing)': takes a number to change where it is.
  - Qt's 'void QDesignerFormWindowInterface::simplifySelection(QList<QWidget
    *> *widgets) const': names 'QList<QWidget *>', which has no cute class
    yet.
  - Qt's 'void QDesignerFormWindowInterface::activateResourceFilePaths(const
    QStringList &paths, int *errorCount, QString *errorMessages)': takes a
    number to change where it is.

  What has no ritual
  ------------------

  3 of the 83 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QDesignerFormWindowInterface is created at the first use, not by
    'QDesignerFormWindowInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerFormWindowInterface.
  - Qt tells when it has removed the C++ QDesignerFormWindowInterface. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDesignerFormWindowInterface that has no cute function
    yet, '__init__', 'activateResourceFilePaths', 'layoutDefault',
    'simplifySelection', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QDesignerFormWindowInterface, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FeatureFlag(CuteFlags):
    """
    The flags enum 'QDesignerFormWindowInterface::FeatureFlag' of Qt, with
    the 4 names Qt gives in it. Qt names the type of its combinations
    'QDesignerFormWindowInterface::Feature'.
    """

    EditFeature = 0x1
    GridFeature = 0x2
    TabOrderFeature = 0x4
    DefaultFeature = 0x3

  Feature = FeatureFlag

  class ResourceFileSaveMode(CuteNum):
    """
    The enum 'QDesignerFormWindowInterface::ResourceFileSaveMode' of Qt, with
    the 3 names Qt gives in it.
    """

    SaveAllResourceFiles = Kee[int](0)
    SaveOnlyUsedResourceFiles = Kee[int](1)
    DontSaveResourceFiles = Kee[int](2)

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
    Calls Qt's 'QString QDesignerFormWindowInterface::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#tr

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
    #  QString QDesignerFormWindowInterface::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QDesignerFormWindowInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def findFormWindow(
      w: Optional[QWidget],
  ) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *QDesignerFormWindowInterface::findFormWindow(QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#findFormWindow

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *QDesignerFormWindowInterface::findFormWindow(QWidget *w)
    address = Rituals.call(
        'ritual_ZN28QDesignerFormWindowInterface14findFormWindowEP7QWidget',
        CuteMixin._addressOf(w),
    )
    return QDesignerFormWindowInterface._cuteAt(address)

  @staticmethod
  @overload(QObject)
  def findFormWindow(
      obj: Optional[QObject],
  ) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *QDesignerFormWindowInterface::findFormWindow(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#findFormWindow

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *QDesignerFormWindowInterface::findFormWindow(QObject *obj)
    address = Rituals.call(
        'ritual_ZN28QDesignerFormWindowInterface14findFormWindowEP7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    return QDesignerFormWindowInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerFormWindowInterface'

  #  A C++ QDesignerFormWindowInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerFormWindowInterface'

  #  The functions Qt calls itself that QDesignerFormWindowInterface is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'checkContents': (
          'QStringList QDesignerFormWindowInterface::checkContents() const',
      ),
      'layoutDefault': (
          'void QDesignerFormWindowInterface::layoutDefault(int *, int *)',
      ),
      'includeHints': (
          'QStringList QDesignerFormWindowInterface::includeHints() const',
      ),
      'setIncludeHints': (
          'void QDesignerFormWindowInterface::setIncludeHints(const '
          'QStringList &)',
      ),
      'simplifySelection': (
          'void '
          'QDesignerFormWindowInterface::simplifySelection(QList<QWidget '
          '*> *) const',
      ),
      'resourceFiles': (
          'QStringList QDesignerFormWindowInterface::resourceFiles() const',
      ),
  }

  #  The functions Qt calls itself that QDesignerFormWindowInterface is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'fileName': (
          ('_ZNK28QDesignerFormWindowInterface8fileNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'absoluteDir': (
          ('_ZNK28QDesignerFormWindowInterface11absoluteDirEv',
           ('address', 'value', 'QtCore:QDir'),
           ()),
      ),
      'contents': (
          ('_ZNK28QDesignerFormWindowInterface8contentsEv',
           ('address', 'text', ''),
           ()),
      ),
      'setContents': (
          ('_ZN28QDesignerFormWindowInterface11setContentsEP9QIODeviceP7QSt'
           'ring',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QIODevice'),
               ('address', 'address', 'QtCore:QString'),
           )),
          ('_ZN28QDesignerFormWindowInterface11setContentsERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'features': (
          ('_ZNK28QDesignerFormWindowInterface8featuresEv',
           ('int', 'flags',
            'QtDesigner:QDesignerFormWindowInterface.FeatureFlag'),
           ()),
      ),
      'hasFeature': (
          ('_ZNK28QDesignerFormWindowInterface10hasFeatureE6QFlagsINS_11Fea'
           'tureFlagEE',
           ('bool', 'number', ''),
           (
               ('int', 'flags',
                'QtDesigner:QDesignerFormWindowInterface.FeatureFlag'),
           )),
      ),
      'author': (
          ('_ZNK28QDesignerFormWindowInterface6authorEv',
           ('address', 'text', ''),
           ()),
      ),
      'setAuthor': (
          ('_ZN28QDesignerFormWindowInterface9setAuthorERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'comment': (
          ('_ZNK28QDesignerFormWindowInterface7commentEv',
           ('address', 'text', ''),
           ()),
      ),
      'setComment': (
          ('_ZN28QDesignerFormWindowInterface10setCommentERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setLayoutDefault': (
          ('_ZN28QDesignerFormWindowInterface16setLayoutDefaultEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'layoutFunction': (
          ('_ZN28QDesignerFormWindowInterface14layoutFunctionEP7QStringS1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QString'),
               ('address', 'address', 'QtCore:QString'),
           )),
      ),
      'setLayoutFunction': (
          ('_ZN28QDesignerFormWindowInterface17setLayoutFunctionERK7QString'
           'S2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'pixmapFunction': (
          ('_ZNK28QDesignerFormWindowInterface14pixmapFunctionEv',
           ('address', 'text', ''),
           ()),
      ),
      'setPixmapFunction': (
          ('_ZN28QDesignerFormWindowInterface17setPixmapFunctionERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'exportMacro': (
          ('_ZNK28QDesignerFormWindowInterface11exportMacroEv',
           ('address', 'text', ''),
           ()),
      ),
      'setExportMacro': (
          ('_ZN28QDesignerFormWindowInterface14setExportMacroERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'resourceFileSaveMode': (
          ('_ZNK28QDesignerFormWindowInterface20resourceFileSaveModeEv',
           ('int', 'enum',
            'QtDesigner:QDesignerFormWindowInterface.ResourceFileSaveMode'),
           ()),
      ),
      'setResourceFileSaveMode': (
          ('_ZN28QDesignerFormWindowInterface23setResourceFileSaveModeENS_2'
           '0ResourceFileSaveModeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtDesigner:QDesignerFormWindowInterface.ResourceFileSaveMode'),
           )),
      ),
      'resourceSet': (
          ('_ZNK28QDesignerFormWindowInterface11resourceSetEv',
           ('address', 'address', 'QtDesigner:QtResourceSet'),
           ()),
      ),
      'setResourceSet': (
          ('_ZN28QDesignerFormWindowInterface14setResourceSetEP13QtResource'
           'Set',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDesigner:QtResourceSet'),
           )),
      ),
      'core': (
          ('_ZNK28QDesignerFormWindowInterface4coreEv',
           ('address', 'address', 'QtDesigner:QDesignerFormEditorInterface'),
           ()),
      ),
      'toolCount': (
          ('_ZNK28QDesignerFormWindowInterface9toolCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'currentTool': (
          ('_ZNK28QDesignerFormWindowInterface11currentToolEv',
           ('int', 'number', ''),
           ()),
      ),
      'setCurrentTool': (
          ('_ZN28QDesignerFormWindowInterface14setCurrentToolEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'tool': (
          ('_ZNK28QDesignerFormWindowInterface4toolEi',
           ('address', 'address',
            'QtDesigner:QDesignerFormWindowToolInterface'),
           (
               ('int', 'number', ''),
           )),
      ),
      'registerTool': (
          ('_ZN28QDesignerFormWindowInterface12registerToolEP32QDesignerFor'
           'mWindowToolInterface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormWindowToolInterface'),
           )),
      ),
      'grid': (
          ('_ZNK28QDesignerFormWindowInterface4gridEv',
           ('address', 'value', 'QtCore:QPoint'),
           ()),
      ),
      'mainContainer': (
          ('_ZNK28QDesignerFormWindowInterface13mainContainerEv',
           ('address', 'address', 'QtWidgets:QWidget'),
           ()),
      ),
      'setMainContainer': (
          ('_ZN28QDesignerFormWindowInterface16setMainContainerEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'formContainer': (
          ('_ZNK28QDesignerFormWindowInterface13formContainerEv',
           ('address', 'address', 'QtWidgets:QWidget'),
           ()),
      ),
      'isManaged': (
          ('_ZNK28QDesignerFormWindowInterface9isManagedEP7QWidget',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'isDirty': (
          ('_ZNK28QDesignerFormWindowInterface7isDirtyEv',
           ('bool', 'number', ''),
           ()),
      ),
      'commandHistory': (
          ('_ZNK28QDesignerFormWindowInterface14commandHistoryEv',
           ('address', 'address', 'QtGui:QUndoStack'),
           ()),
      ),
      'beginCommand': (
          ('_ZN28QDesignerFormWindowInterface12beginCommandERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'endCommand': (
          ('_ZN28QDesignerFormWindowInterface10endCommandEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'emitSelectionChanged': (
          ('_ZN28QDesignerFormWindowInterface20emitSelectionChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'addResourceFile': (
          ('_ZN28QDesignerFormWindowInterface15addResourceFileERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'removeResourceFile': (
          ('_ZN28QDesignerFormWindowInterface18removeResourceFileERK7QStrin'
           'g',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'ensureUniqueObjectName': (
          ('_ZN28QDesignerFormWindowInterface22ensureUniqueObjectNameEP7QOb'
           'ject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'manageWidget': (
          ('_ZN28QDesignerFormWindowInterface12manageWidgetEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'unmanageWidget': (
          ('_ZN28QDesignerFormWindowInterface14unmanageWidgetEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'setFeatures': (
          ('_ZN28QDesignerFormWindowInterface11setFeaturesE6QFlagsINS_11Fea'
           'tureFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags',
                'QtDesigner:QDesignerFormWindowInterface.FeatureFlag'),
           )),
      ),
      'setDirty': (
          ('_ZN28QDesignerFormWindowInterface8setDirtyEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'clearSelection': (
          ('_ZN28QDesignerFormWindowInterface14clearSelectionEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'selectWidget': (
          ('_ZN28QDesignerFormWindowInterface12selectWidgetEP7QWidgetb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('bool', 'number', ''),
           )),
      ),
      'setGrid': (
          ('_ZN28QDesignerFormWindowInterface7setGridERK6QPoint',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'setFileName': (
          ('_ZN28QDesignerFormWindowInterface11setFileNameERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'editWidgets': (
          ('_ZN28QDesignerFormWindowInterface11editWidgetsEv',
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
    Calls Qt's 'const QMetaObject *QDesignerFormWindowInterface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerFormWindowInterface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QDesignerFormWindowInterface::fileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerFormWindowInterface::fileName() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface8fileNameEv',
    )

  def absoluteDir(self) -> QDir:
    """
    Calls Qt's 'QDir QDesignerFormWindowInterface::absoluteDir() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#absoluteDir

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QDesignerFormWindowInterface::absoluteDir() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface11absoluteDirEv',
    )
    from ..QtCore import QDir
    return QDir._cuteOwning(address)

  def contents(self) -> str:
    """
    Calls Qt's 'QString QDesignerFormWindowInterface::contents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#contents

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerFormWindowInterface::contents() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface8contentsEv',
    )

  def checkContents(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerFormWindowInterface::checkContents()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#checkContents

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerFormWindowInterface::checkContents() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface13checkContentsEv',
    )
    return QStringList._cuteOwning(address)

  def features(self) -> Feature:
    """
    Calls Qt's 'Feature QDesignerFormWindowInterface::features() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#features

    Returns
    -------

    Feature
      The value standing for the combination Qt gave back.
    """
    #  Feature QDesignerFormWindowInterface::features() const
    return QDesignerFormWindowInterface.Feature(self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface8featuresEv',
    ))

  @overload(Feature)
  def hasFeature(self, f: Feature) -> bool:
    """
    Calls Qt's 'bool QDesignerFormWindowInterface::hasFeature(Feature f)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#hasFeature

    Parameters
    ----------

    f : Feature
      Passed on as its number.
    """
    #  bool QDesignerFormWindowInterface::hasFeature(Feature f) const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface10hasFeatureE6QFlagsINS_11'
        'FeatureFlagEE',
        f.value,
    )

  def author(self) -> str:
    """
    Calls Qt's 'QString QDesignerFormWindowInterface::author() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#author

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerFormWindowInterface::author() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface6authorEv',
    )

  def comment(self) -> str:
    """
    Calls Qt's 'QString QDesignerFormWindowInterface::comment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#comment

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerFormWindowInterface::comment() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface7commentEv',
    )

  def pixmapFunction(self) -> str:
    """
    Calls Qt's 'QString QDesignerFormWindowInterface::pixmapFunction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#pixmapFunction

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerFormWindowInterface::pixmapFunction() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface14pixmapFunctionEv',
    )

  def exportMacro(self) -> str:
    """
    Calls Qt's 'QString QDesignerFormWindowInterface::exportMacro() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#exportMacro

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerFormWindowInterface::exportMacro() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface11exportMacroEv',
    )

  def includeHints(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerFormWindowInterface::includeHints()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#includeHints

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerFormWindowInterface::includeHints() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface12includeHintsEv',
    )
    return QStringList._cuteOwning(address)

  def resourceFileSaveMode(self) -> ResourceFileSaveMode:
    """
    Calls Qt's 'ResourceFileSaveMode
    QDesignerFormWindowInterface::resourceFileSaveMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html

    Returns
    -------

    ResourceFileSaveMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ResourceFileSaveMode(number)' gives.
    """
    #  ResourceFileSaveMode
    #      QDesignerFormWindowInterface::resourceFileSaveMode() const
    return QDesignerFormWindowInterface.ResourceFileSaveMode(
        self.uglySide.call(
            'ritual_ZNK28QDesignerFormWindowInterface20resourceFileSaveMode'
            'Ev',
        ))

  def resourceSet(self) -> Optional[QtResourceSet]:
    """
    Calls Qt's 'QtResourceSet *QDesignerFormWindowInterface::resourceSet()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#resourceSet

    Returns
    -------

    Optional[QtResourceSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtResourceSet *QDesignerFormWindowInterface::resourceSet() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface11resourceSetEv',
    )
    from . import QtResourceSet
    return QtResourceSet._cuteAt(address)

  def activeResourceFilePaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QDesignerFormWindowInterface::activeResourceFilePaths() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerFormWindowInterface::activeResourceFilePaths()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface23activeResourceFilePathsE'
        'v',
    )
    return QStringList._cuteOwning(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerFormWindowInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerFormWindowInterface::core()
    #      const
    ritual = 'ritual_ZNK28QDesignerFormWindowInterface4coreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QDesignerFormWindowInterface4coreEv'
    address = self.uglySide.call(ritual)
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  def cursor(self) -> Optional[QDesignerFormWindowCursorInterface]:
    """
    Calls Qt's 'QDesignerFormWindowCursorInterface
    *QDesignerFormWindowInterface::cursor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#cursor

    Returns
    -------

    Optional[QDesignerFormWindowCursorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowCursorInterface
    #      *QDesignerFormWindowInterface::cursor() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface6cursorEv',
    )
    from . import QDesignerFormWindowCursorInterface
    return QDesignerFormWindowCursorInterface._cuteAt(address)

  def toolCount(self) -> int:
    """
    Calls Qt's 'int QDesignerFormWindowInterface::toolCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#toolCount
    """
    #  int QDesignerFormWindowInterface::toolCount() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface9toolCountEv',
    )

  def currentTool(self) -> int:
    """
    Calls Qt's 'int QDesignerFormWindowInterface::currentTool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#currentTool
    """
    #  int QDesignerFormWindowInterface::currentTool() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface11currentToolEv',
    )

  @overload(int)
  def tool(self, index: int) -> Optional[QDesignerFormWindowToolInterface]:
    """
    Calls Qt's 'QDesignerFormWindowToolInterface
    *QDesignerFormWindowInterface::tool(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#tool

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QDesignerFormWindowToolInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowToolInterface
    #      *QDesignerFormWindowInterface::tool(int index) const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface4toolEi', index,
    )
    from . import QDesignerFormWindowToolInterface
    return QDesignerFormWindowToolInterface._cuteAt(address)

  def grid(self) -> QPoint:
    """
    Calls Qt's 'QPoint QDesignerFormWindowInterface::grid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#grid

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QDesignerFormWindowInterface::grid() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface4gridEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def mainContainer(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerFormWindowInterface::mainContainer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#mainContainer

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerFormWindowInterface::mainContainer() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface13mainContainerEv',
    )
    return QWidget._cuteAt(address)

  def formContainer(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerFormWindowInterface::formContainer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#formContainer

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerFormWindowInterface::formContainer() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface13formContainerEv',
    )
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def isManaged(self, widget: Optional[QWidget]) -> bool:
    """
    Calls Qt's 'bool QDesignerFormWindowInterface::isManaged(QWidget *widget)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#isManaged

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerFormWindowInterface::isManaged(QWidget *widget) const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface9isManagedEP7QWidget',
        self._addressOf(widget),
    )

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool QDesignerFormWindowInterface::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#isDirty
    """
    #  bool QDesignerFormWindowInterface::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface7isDirtyEv',
    )

  def commandHistory(self) -> Optional[QUndoStack]:
    """
    Calls Qt's 'QUndoStack *QDesignerFormWindowInterface::commandHistory()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#commandHistory

    Returns
    -------

    Optional[QUndoStack]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUndoStack *QDesignerFormWindowInterface::commandHistory() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface14commandHistoryEv',
    )
    from ..QtGui import QUndoStack
    return QUndoStack._cuteAt(address)

  def resourceFiles(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDesignerFormWindowInterface::resourceFiles()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#resourceFiles

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDesignerFormWindowInterface::resourceFiles() const
    address = self.uglySide.call(
        'ritual_ZNK28QDesignerFormWindowInterface13resourceFilesEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, QString)
  @overload(QIODevice, NoneType)
  @overload(NoneType, QString)
  @overload(NoneType, NoneType)
  def setContents(
      self,
      dev: Optional[QIODevice],
      errorMessage: Optional[QString] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QDesignerFormWindowInterface::setContents(QIODevice
    *dev, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setContents

    Parameters
    ----------

    dev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QDesignerFormWindowInterface::setContents(QIODevice *dev, QString
    #      *errorMessage)
    return self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface11setContentsEP9QIODeviceP7'
        'QString',
        self._addressOf(dev), self._addressOf(errorMessage),
    )

  @overload(str)
  def setContents(self, contents: str) -> bool:
    """
    Calls Qt's 'bool QDesignerFormWindowInterface::setContents(const QString
    &contents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setContents

    Parameters
    ----------

    contents : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDesignerFormWindowInterface::setContents(const QString
    #      &contents)
    return self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface11setContentsERK7QString',
        contents,
    )

  @overload(str)
  def setAuthor(self, author: str) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setAuthor(const QString
    &author)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setAuthor

    Parameters
    ----------

    author : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowInterface::setAuthor(const QString &author)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface9setAuthorERK7QString',
        author,
    )

  @overload(str)
  def setComment(self, comment: str) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setComment(const QString
    &comment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setComment

    Parameters
    ----------

    comment : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowInterface::setComment(const QString &comment)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface10setCommentERK7QString',
        comment,
    )

  @overload(int, int)
  def setLayoutDefault(self, margin: int, spacing: int) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setLayoutDefault(int
    margin, int spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setLayoutDefault

    Parameters
    ----------

    margin : int
      Passed on as it is.

    spacing : int
      Passed on as it is.
    """
    #  void QDesignerFormWindowInterface::setLayoutDefault(int margin, int
    #      spacing)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface16setLayoutDefaultEii',
        margin, spacing,
    )

  @overload(str, str)
  def setLayoutFunction(self, margin: str, spacing: str) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setLayoutFunction(const
    QString &margin, const QString &spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html

    Parameters
    ----------

    margin : str
      Passed on as it is: a QString is made of it for the call.

    spacing : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowInterface::setLayoutFunction(const QString
    #      &margin, const QString &spacing)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface17setLayoutFunctionERK7QStr'
        'ingS2_',
        margin, spacing,
    )

  @overload(str)
  def setPixmapFunction(self, pixmapFunction: str) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setPixmapFunction(const
    QString &pixmapFunction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html

    Parameters
    ----------

    pixmapFunction : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowInterface::setPixmapFunction(const QString
    #      &pixmapFunction)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface17setPixmapFunctionERK7QStr'
        'ing',
        pixmapFunction,
    )

  @overload(str)
  def setExportMacro(self, exportMacro: str) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setExportMacro(const
    QString &exportMacro)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setExportMacro

    Parameters
    ----------

    exportMacro : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowInterface::setExportMacro(const QString
    #      &exportMacro)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface14setExportMacroERK7QString',
        exportMacro,
    )

  @overload(QStringList)
  def setIncludeHints(self, includeHints: QStringList) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setIncludeHints(const
    QStringList &includeHints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setIncludeHints

    Parameters
    ----------

    includeHints : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDesignerFormWindowInterface::setIncludeHints(const QStringList
    #      &includeHints)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface15setIncludeHintsERK5QListI'
        '7QStringE',
        self._valueOf(includeHints),
    )

  @overload(ResourceFileSaveMode)
  def setResourceFileSaveMode(self, behaviour: ResourceFileSaveMode) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setResourceFileSaveMode(
    ResourceFileSaveMode behaviour)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html

    Parameters
    ----------

    behaviour : ResourceFileSaveMode
      Passed on as its number.
    """
    #  void QDesignerFormWindowInterface::setResourceFileSaveMode(
    #      ResourceFileSaveMode behaviour)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface23setResourceFileSaveModeEN'
        'S_20ResourceFileSaveModeE',
        behaviour.value,
    )

  @overload(QtResourceSet)
  @overload(NoneType)
  def setResourceSet(self, resourceSet: Optional[QtResourceSet]) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowInterface::setResourceSet(QtResourceSet
    *resourceSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setResourceSet

    Parameters
    ----------

    resourceSet : Optional[QtResourceSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::setResourceSet(QtResourceSet
    #      *resourceSet)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface14setResourceSetEP13QtResou'
        'rceSet',
        self._addressOf(resourceSet),
    )

  @overload(int)
  def setCurrentTool(self, index: int) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setCurrentTool(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setCurrentTool

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QDesignerFormWindowInterface::setCurrentTool(int index)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface14setCurrentToolEi', index,
    )

  @overload(QWidget)
  @overload(NoneType)
  def setMainContainer(self, mainContainer: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setMainContainer(QWidget
    *mainContainer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setMainContainer

    Parameters
    ----------

    mainContainer : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::setMainContainer(QWidget
    #      *mainContainer)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface16setMainContainerEP7QWidge'
        't',
        self._addressOf(mainContainer),
    )

  @overload(Feature)
  def setFeatures(self, f: Feature) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setFeatures(Feature f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setFeatures

    Parameters
    ----------

    f : Feature
      Passed on as its number.
    """
    #  void QDesignerFormWindowInterface::setFeatures(Feature f)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface11setFeaturesE6QFlagsINS_11'
        'FeatureFlagEE',
        f.value,
    )

  @overload(bool)
  def setDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QDesignerFormWindowInterface::setDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface8setDirtyEb', dirty,
    )

  @overload(QPoint)
  def setGrid(self, grid: QPoint) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setGrid(const QPoint
    &grid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setGrid

    Parameters
    ----------

    grid : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QDesignerFormWindowInterface::setGrid(const QPoint &grid)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface7setGridERK6QPoint',
        self._valueOf(grid),
    )

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::setFileName(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowInterface::setFileName(const QString
    #      &fileName)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface11setFileNameERK7QString',
        fileName,
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
    Qt's 'QDesignerFormWindowInterface::QDesignerFormWindowInterface(QWidget
    *parent, Qt::WindowFlags flags)': the class is abstract, so C++ cannot
    make one, and the C++ class of ours does not fill in every function it
    leaves open.
    """
    raise NotImplementedError(
        "'QDesignerFormWindowInterface.__init__' has no cute function yet. "
        "Qt's "
        "'QDesignerFormWindowInterface::QDesignerFormWindowInterface(QWidget"
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

  @overload(QString, QString)
  @overload(QString, NoneType)
  @overload(NoneType, QString)
  @overload(NoneType, NoneType)
  def layoutFunction(
      self,
      margin: Optional[QString],
      spacing: Optional[QString],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::layoutFunction(QString
    *margin, QString *spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#layoutFunction

    Parameters
    ----------

    margin : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    spacing : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::layoutFunction(QString *margin,
    #      QString *spacing)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface14layoutFunctionEP7QStringS'
        '1_',
        self._addressOf(margin), self._addressOf(spacing),
    )

  @overload(QDesignerFormWindowToolInterface)
  @overload(NoneType)
  def registerTool(
      self,
      tool: Optional[QDesignerFormWindowToolInterface],
  ) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::registerTool(
    QDesignerFormWindowToolInterface *tool)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#registerTool

    Parameters
    ----------

    tool : Optional[QDesignerFormWindowToolInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::registerTool(
    #      QDesignerFormWindowToolInterface *tool)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface12registerToolEP32QDesigner'
        'FormWindowToolInterface',
        self._addressOf(tool),
    )

  @overload(str)
  def beginCommand(self, description: str) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::beginCommand(const QString
    &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#beginCommand

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowInterface::beginCommand(const QString
    #      &description)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface12beginCommandERK7QString',
        description,
    )

  def endCommand(self) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::endCommand()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#endCommand
    """
    #  void QDesignerFormWindowInterface::endCommand()
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface10endCommandEv',
    )

  def emitSelectionChanged(self) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::emitSelectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html
    """
    #  void QDesignerFormWindowInterface::emitSelectionChanged()
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface20emitSelectionChangedEv',
    )

  @overload(str)
  def addResourceFile(self, path: str) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::addResourceFile(const
    QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#addResourceFile

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowInterface::addResourceFile(const QString
    #      &path)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface15addResourceFileERK7QStrin'
        'g',
        path,
    )

  @overload(str)
  def removeResourceFile(self, path: str) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::removeResourceFile(const
    QString &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowInterface::removeResourceFile(const QString
    #      &path)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface18removeResourceFileERK7QSt'
        'ring',
        path,
    )

  @overload(QObject)
  @overload(NoneType)
  def ensureUniqueObjectName(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowInterface::ensureUniqueObjectName(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::ensureUniqueObjectName(QObject
    #      *object)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface22ensureUniqueObjectNameEP7'
        'QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QWidget)
  @overload(NoneType)
  def manageWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::manageWidget(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#manageWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::manageWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface12manageWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def unmanageWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::unmanageWidget(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#unmanageWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::unmanageWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface14unmanageWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload()
  @overload(bool)
  def clearSelection(self, changePropertyDisplay: bool = True) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::clearSelection(bool
    changePropertyDisplay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#clearSelection

    Parameters
    ----------

    changePropertyDisplay : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDesignerFormWindowInterface::clearSelection(bool
    #      changePropertyDisplay)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface14clearSelectionEb',
        changePropertyDisplay,
    )

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, bool)
  @overload(NoneType, bool)
  def selectWidget(self, w: Optional[QWidget], select: bool = True) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::selectWidget(QWidget *w,
    bool select)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#selectWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    select : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDesignerFormWindowInterface::selectWidget(QWidget *w, bool
    #      select)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface12selectWidgetEP7QWidgetb',
        self._addressOf(w), select,
    )

  def editWidgets(self) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::editWidgets()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#editWidgets
    """
    #  void QDesignerFormWindowInterface::editWidgets()
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface11editWidgetsEv',
    )

  @overload(QWidget)
  @overload(NoneType)
  def mainContainerChanged(self, mainContainer: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowInterface::mainContainerChanged(QWidget
    *mainContainer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html

    Parameters
    ----------

    mainContainer : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::mainContainerChanged(QWidget
    #      *mainContainer)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface20mainContainerChangedEP7QW'
        'idget',
        self._addressOf(mainContainer),
    )

  @overload(int)
  def toolChanged(self, toolIndex: int) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::toolChanged(int
    toolIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#toolChanged

    Parameters
    ----------

    toolIndex : int
      Passed on as it is.
    """
    #  void QDesignerFormWindowInterface::toolChanged(int toolIndex)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface11toolChangedEi', toolIndex,
    )

  @overload(str)
  def fileNameChanged(self, fileName: str) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::fileNameChanged(const
    QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#fileNameChanged

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerFormWindowInterface::fileNameChanged(const QString
    #      &fileName)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface15fileNameChangedERK7QStrin'
        'g',
        fileName,
    )

  @overload(Feature)
  def featureChanged(self, f: Feature) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::featureChanged(Feature
    f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#featureChanged

    Parameters
    ----------

    f : Feature
      Passed on as its number.
    """
    #  void QDesignerFormWindowInterface::featureChanged(Feature f)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface14featureChangedE6QFlagsINS'
        '_11FeatureFlagEE',
        f.value,
    )

  def selectionChanged(self) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::selectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#selectionChanged
    """
    #  void QDesignerFormWindowInterface::selectionChanged()
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface16selectionChangedEv',
    )

  def geometryChanged(self) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::geometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#geometryChanged
    """
    #  void QDesignerFormWindowInterface::geometryChanged()
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface15geometryChangedEv',
    )

  def resourceFilesChanged(self) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::resourceFilesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html
    """
    #  void QDesignerFormWindowInterface::resourceFilesChanged()
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface20resourceFilesChangedEv',
    )

  @overload(QWidget)
  @overload(NoneType)
  def widgetManaged(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::widgetManaged(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#widgetManaged

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::widgetManaged(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface13widgetManagedEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def widgetUnmanaged(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::widgetUnmanaged(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#widgetUnmanaged

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::widgetUnmanaged(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface15widgetUnmanagedEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def aboutToUnmanageWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    QDesignerFormWindowInterface::aboutToUnmanageWidget(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::aboutToUnmanageWidget(QWidget
    #      *widget)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface21aboutToUnmanageWidgetEP7Q'
        'Widget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def activated(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::activated(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#activated

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::activated(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface9activatedEP7QWidget',
        self._addressOf(widget),
    )

  def changed(self) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::changed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#changed
    """
    #  void QDesignerFormWindowInterface::changed()
    self.uglySide.call('ritual_ZN28QDesignerFormWindowInterface7changedEv')

  @overload(QWidget)
  @overload(NoneType)
  def widgetRemoved(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::widgetRemoved(QWidget
    *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#widgetRemoved

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::widgetRemoved(QWidget *w)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface13widgetRemovedEP7QWidget',
        self._addressOf(w),
    )

  @overload(QObject)
  @overload(NoneType)
  def objectRemoved(self, o: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowInterface::objectRemoved(QObject
    *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowinterface.html#objectRemoved

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowInterface::objectRemoved(QObject *o)
    self.uglySide.call(
        'ritual_ZN28QDesignerFormWindowInterface13objectRemovedEP7QObject',
        self._addressOf(o, 'QObject'),
    )

  @staticmethod
  def activateResourceFilePaths(*__, **_) -> Never:
    """
    Qt's 'void QDesignerFormWindowInterface::activateResourceFilePaths(const
    QStringList &paths, int *errorCount, QString *errorMessages)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QDesignerFormWindowInterface.activateResourceFilePaths' has no "
        "cute function yet. Qt's 'void "
        "QDesignerFormWindowInterface::activateResourceFilePaths(const "
        "QStringList &paths, int *errorCount, QString *errorMessages)': "
        "takes a number to change where it is.")

  @staticmethod
  def layoutDefault(*__, **_) -> Never:
    """
    Qt's 'void QDesignerFormWindowInterface::layoutDefault(int *margin, int
    *spacing)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QDesignerFormWindowInterface.layoutDefault' has no cute function "
        "yet. Qt's 'void QDesignerFormWindowInterface::layoutDefault(int "
        "*margin, int *spacing)': takes a number to change where it is.")

  @staticmethod
  def simplifySelection(*__, **_) -> Never:
    """
    Qt's 'void QDesignerFormWindowInterface::simplifySelection(QList<QWidget
    *> *widgets) const': names 'QList<QWidget *>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QDesignerFormWindowInterface.simplifySelection' has no cute "
        "function yet. Qt's 'void "
        "QDesignerFormWindowInterface::simplifySelection(QList<QWidget *> "
        "*widgets) const': names 'QList<QWidget *>', which has no cute "
        "class yet.")
