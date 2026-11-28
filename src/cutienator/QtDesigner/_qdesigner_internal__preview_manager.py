"""
qdesigner_internal::PreviewManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/previewmanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PreviewManager to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QString
  from ..QtGui import QPixmap
  from ..QtWidgets import QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QEvent = WAIT['QEvent']
  QString = WAIT['QString']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PreviewManager(QObject):
  """
  The cute side of Qt's qdesigner_internal::PreviewManager: a plain Python
  object standing in front of one C++ qdesigner_internal::PreviewManager.

  It is built on the cute 'QObject', as Qt's
  qdesigner_internal::PreviewManager is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PreviewManager that has a ritual
  and that Python can call so far, 15 names in all: 'metaObject', 'tr',
  'showPreview', 'previewCount', 'createPreviewPixmap', 'eventFilter',
  'closeAllPreviews', 'firstPreviewOpened', 'lastPreviewClosed',
  'slotZoomChanged', 'previewWindowFlags', 'createDeviceSkinContainer',
  'raise_', 'createPreview', 'updatePreviewClosed'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::PreviewManager::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::PreviewManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::PreviewManager::~PreviewManager()': the
    destructor: Python never removes a C++
    qdesigner_internal::PreviewManager.
  - Qt's 'qdesigner_internal::PreviewManager::PreviewManager(const
    PreviewManager &other)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 27 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::PreviewManager is created at the first use,
    not by 'qdesigner_internal::PreviewManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::PreviewManager.
  - Qt tells when it has removed the C++ qdesigner_internal::PreviewManager.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside qdesigner_internal::PreviewManager, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class PreviewMode(CuteNum):
    """
    The enum 'qdesigner_internal::PreviewManager::PreviewMode' of Qt, with
    the 3 names Qt gives in it.
    """

    ApplicationModalPreview = Kee[int](0)
    SingleFormNonModalPreview = Kee[int](1)
    MultipleFormNonModalPreview = Kee[int](2)

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
    Calls Qt's 'QString qdesigner_internal::PreviewManager::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html#tr

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
    #  QString qdesigner_internal::PreviewManager::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14PreviewManager2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PreviewManager'

  #  A C++ qdesigner_internal::PreviewManager Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_PreviewManager'

  #  The functions Qt calls itself that qdesigner_internal::PreviewManager is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'previewWindowFlags': (
          ('_ZNK18qdesigner_internal14PreviewManager18previewWindowFlagsEPK'
           '7QWidget',
           ('int', 'flags', 'QtCore:Qt.WindowType'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'createDeviceSkinContainer': (
          ('_ZNK18qdesigner_internal14PreviewManager25createDeviceSkinConta'
           'inerEPK28QDesignerFormWindowInterface',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address',
                'QtDesigner:QDesignerFormWindowInterface'),
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
    *qdesigner_internal::PreviewManager::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::PreviewManager::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14PreviewManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def previewCount(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::PreviewManager::previewCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html
    """
    #  int qdesigner_internal::PreviewManager::previewCount() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14PreviewManager12previewCountEv',
    )

  @overload(QWidget)
  @overload(NoneType)
  def previewWindowFlags(self, widget: Optional[QWidget]) -> Qt.WindowFlags:
    """
    Calls Qt's 'Qt::WindowFlags
    qdesigner_internal::PreviewManager::previewWindowFlags(const QWidget
    *widget) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.WindowFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::WindowFlags
    #      qdesigner_internal::PreviewManager::previewWindowFlags(const
    #      QWidget *widget) const
    ritual = (
        'ritual_ZNK18qdesigner_internal14PreviewManager18previewWindowFlags'
        'EPK7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14PreviewManager18previewWindo'
          'wFlagsEPK7QWidget')
    return Qt.WindowFlags(self.uglySide.call(
        ritual, self._addressOf(widget),
    ))

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def createDeviceSkinContainer(
      self,
      a0: Optional[QDesignerFormWindowInterface],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::PreviewManager::createDeviceSkinContainer(const
    QDesignerFormWindowInterface *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html

    Parameters
    ----------

    a0 : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget
    #      *qdesigner_internal::PreviewManager::createDeviceSkinContainer(
    #      const QDesignerFormWindowInterface *a0) const
    ritual = (
        'ritual_ZNK18qdesigner_internal14PreviewManager25createDeviceSkinCo'
        'ntainerEPK28QDesignerFormWindowInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18qdesigner_internal14PreviewManager25createDevice'
          'SkinContainerEPK28QDesignerFormWindowInterface')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

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

  @overload(PreviewMode, QObject)
  @overload(PreviewMode, NoneType)
  def __init__(self, mode: PreviewMode, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PreviewManager::PreviewManager(PreviewMode mode,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html

    Parameters
    ----------

    mode : PreviewMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::PreviewManager::PreviewManager(PreviewMode mode,
    #      QObject *parent)
    self._noteCreation(PreviewManager, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal14PreviewManagerC1ENS0_11PreviewModeE'
        'P7QObject',
        mode.value, self._addressOf(parent, 'QObject'),
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

  @overload(
      QDesignerFormWindowInterface,
      WAIT['qdesigner_internal.PreviewConfiguration'], int, QString,
  )
  @overload(
      QDesignerFormWindowInterface,
      WAIT['qdesigner_internal.PreviewConfiguration'], int, NoneType,
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.PreviewConfiguration'], int,
      QString,
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.PreviewConfiguration'], int,
      NoneType,
  )
  def showPreview(
      self,
      a0: Optional[QDesignerFormWindowInterface],
      pc: qdesigner_internal.PreviewConfiguration,
      deviceProfileIndex: int,
      errorMessage: Optional[QString],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::PreviewManager::showPreview(const
    QDesignerFormWindowInterface *a0, const PreviewConfiguration &pc, int
    deviceProfileIndex, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html#showPreview

    Parameters
    ----------

    a0 : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pc : qdesigner_internal.PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.

    deviceProfileIndex : int
      Passed on as it is.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::PreviewManager::showPreview(const
    #      QDesignerFormWindowInterface *a0, const PreviewConfiguration &pc,
    #      int deviceProfileIndex, QString *errorMessage)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager11showPreviewEPK28QDe'
        'signerFormWindowInterfaceRKNS_20PreviewConfigurationEiP7QString',
        self._addressOf(a0), self._valueOf(pc), deviceProfileIndex,
        self._addressOf(errorMessage),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(QDesignerFormWindowInterface, str, int, QString)
  @overload(QDesignerFormWindowInterface, str, int, NoneType)
  @overload(NoneType, str, int, QString)
  @overload(NoneType, str, int, NoneType)
  def showPreview(
      self,
      a0: Optional[QDesignerFormWindowInterface],
      style: str,
      deviceProfileIndex: int,
      errorMessage: Optional[QString],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::PreviewManager::showPreview(const
    QDesignerFormWindowInterface *a0, const QString &style, int
    deviceProfileIndex, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html#showPreview

    Parameters
    ----------

    a0 : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    style : str
      Passed on as it is: a QString is made of it for the call.

    deviceProfileIndex : int
      Passed on as it is.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::PreviewManager::showPreview(const
    #      QDesignerFormWindowInterface *a0, const QString &style, int
    #      deviceProfileIndex, QString *errorMessage)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager11showPreviewEPK28QDe'
        'signerFormWindowInterfaceRK7QStringiPS4_',
        self._addressOf(a0), style, deviceProfileIndex,
        self._addressOf(errorMessage),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(QDesignerFormWindowInterface, str, QString)
  @overload(QDesignerFormWindowInterface, str, NoneType)
  @overload(NoneType, str, QString)
  @overload(NoneType, str, NoneType)
  def showPreview(
      self,
      a0: Optional[QDesignerFormWindowInterface],
      style: str,
      errorMessage: Optional[QString],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::PreviewManager::showPreview(const
    QDesignerFormWindowInterface *a0, const QString &style, QString
    *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html#showPreview

    Parameters
    ----------

    a0 : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    style : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::PreviewManager::showPreview(const
    #      QDesignerFormWindowInterface *a0, const QString &style, QString
    #      *errorMessage)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager11showPreviewEPK28QDe'
        'signerFormWindowInterfaceRK7QStringPS4_',
        self._addressOf(a0), style, self._addressOf(errorMessage),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(
      QDesignerFormWindowInterface,
      WAIT['qdesigner_internal.PreviewConfiguration'], int, QString,
  )
  @overload(
      QDesignerFormWindowInterface,
      WAIT['qdesigner_internal.PreviewConfiguration'], int, NoneType,
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.PreviewConfiguration'], int,
      QString,
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.PreviewConfiguration'], int,
      NoneType,
  )
  def createPreviewPixmap(
      self,
      fw: Optional[QDesignerFormWindowInterface],
      pc: qdesigner_internal.PreviewConfiguration,
      deviceProfileIndex: int,
      errorMessage: Optional[QString],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    qdesigner_internal::PreviewManager::createPreviewPixmap(const
    QDesignerFormWindowInterface *fw, const PreviewConfiguration &pc, int
    deviceProfileIndex, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pc : qdesigner_internal.PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.

    deviceProfileIndex : int
      Passed on as it is.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap qdesigner_internal::PreviewManager::createPreviewPixmap(const
    #      QDesignerFormWindowInterface *fw, const PreviewConfiguration &pc,
    #      int deviceProfileIndex, QString *errorMessage)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager19createPreviewPixmap'
        'EPK28QDesignerFormWindowInterfaceRKNS_20PreviewConfigurationEiP7QS'
        'tring',
        self._addressOf(fw), self._valueOf(pc), deviceProfileIndex,
        self._addressOf(errorMessage),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QDesignerFormWindowInterface, str, int, QString)
  @overload(QDesignerFormWindowInterface, str, int, NoneType)
  @overload(NoneType, str, int, QString)
  @overload(NoneType, str, int, NoneType)
  def createPreviewPixmap(
      self,
      fw: Optional[QDesignerFormWindowInterface],
      style: str,
      deviceProfileIndex: int,
      errorMessage: Optional[QString],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    qdesigner_internal::PreviewManager::createPreviewPixmap(const
    QDesignerFormWindowInterface *fw, const QString &style, int
    deviceProfileIndex, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    style : str
      Passed on as it is: a QString is made of it for the call.

    deviceProfileIndex : int
      Passed on as it is.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap qdesigner_internal::PreviewManager::createPreviewPixmap(const
    #      QDesignerFormWindowInterface *fw, const QString &style, int
    #      deviceProfileIndex, QString *errorMessage)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager19createPreviewPixmap'
        'EPK28QDesignerFormWindowInterfaceRK7QStringiPS4_',
        self._addressOf(fw), style, deviceProfileIndex,
        self._addressOf(errorMessage),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QDesignerFormWindowInterface, str, QString)
  @overload(QDesignerFormWindowInterface, str, NoneType)
  @overload(NoneType, str, QString)
  @overload(NoneType, str, NoneType)
  def createPreviewPixmap(
      self,
      fw: Optional[QDesignerFormWindowInterface],
      style: str,
      errorMessage: Optional[QString],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    qdesigner_internal::PreviewManager::createPreviewPixmap(const
    QDesignerFormWindowInterface *fw, const QString &style, QString
    *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    style : str
      Passed on as it is: a QString is made of it for the call.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap qdesigner_internal::PreviewManager::createPreviewPixmap(const
    #      QDesignerFormWindowInterface *fw, const QString &style, QString
    #      *errorMessage)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager19createPreviewPixmap'
        'EPK28QDesignerFormWindowInterfaceRK7QStringPS4_',
        self._addressOf(fw), style, self._addressOf(errorMessage),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::PreviewManager::eventFilter(QObject
    *watched, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html#eventFilter

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::PreviewManager::eventFilter(QObject *watched,
    #      QEvent *event)
    ritual = (
        'ritual_ZN18qdesigner_internal14PreviewManager11eventFilterEP7QObje'
        'ctP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14PreviewManager11eventFilterEP'
          '7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  def closeAllPreviews(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PreviewManager::closeAllPreviews()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html
    """
    #  void qdesigner_internal::PreviewManager::closeAllPreviews()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager16closeAllPreviewsEv',
    )

  def firstPreviewOpened(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PreviewManager::firstPreviewOpened()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html
    """
    #  void qdesigner_internal::PreviewManager::firstPreviewOpened()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager18firstPreviewOpenedE'
        'v',
    )

  def lastPreviewClosed(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PreviewManager::lastPreviewClosed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html
    """
    #  void qdesigner_internal::PreviewManager::lastPreviewClosed()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager17lastPreviewClosedEv',
    )

  @overload(int)
  def slotZoomChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PreviewManager::slotZoomChanged(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void qdesigner_internal::PreviewManager::slotZoomChanged(int a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager15slotZoomChangedEi',
        a0,
    )

  @overload(
      QDesignerFormWindowInterface,
      WAIT['qdesigner_internal.PreviewConfiguration'],
  )
  @overload(NoneType, WAIT['qdesigner_internal.PreviewConfiguration'])
  def raise_(
      self,
      a0: Optional[QDesignerFormWindowInterface],
      pc: qdesigner_internal.PreviewConfiguration,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *qdesigner_internal::PreviewManager::raise(const
    QDesignerFormWindowInterface *a0, const PreviewConfiguration &pc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html#raise

    Parameters
    ----------

    a0 : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pc : qdesigner_internal.PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::PreviewManager::raise(const
    #      QDesignerFormWindowInterface *a0, const PreviewConfiguration &pc)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager5raiseEPK28QDesignerF'
        'ormWindowInterfaceRKNS_20PreviewConfigurationE',
        self._addressOf(a0), self._valueOf(pc),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(
      QDesignerFormWindowInterface,
      WAIT['qdesigner_internal.PreviewConfiguration'], int, QString,
  )
  @overload(
      QDesignerFormWindowInterface,
      WAIT['qdesigner_internal.PreviewConfiguration'], int, NoneType,
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.PreviewConfiguration'], int,
      QString,
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.PreviewConfiguration'], int,
      NoneType,
  )
  @overload(
      QDesignerFormWindowInterface,
      WAIT['qdesigner_internal.PreviewConfiguration'], int, QString, int,
  )
  @overload(
      QDesignerFormWindowInterface,
      WAIT['qdesigner_internal.PreviewConfiguration'], int, NoneType, int,
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.PreviewConfiguration'], int,
      QString, int,
  )
  @overload(
      NoneType, WAIT['qdesigner_internal.PreviewConfiguration'], int,
      NoneType, int,
  )
  def createPreview(
      self,
      a0: Optional[QDesignerFormWindowInterface],
      pc: qdesigner_internal.PreviewConfiguration,
      deviceProfileIndex: int,
      errorMessage: Optional[QString],
      initialZoom: int = -1,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::PreviewManager::createPreview(const
    QDesignerFormWindowInterface *a0, const PreviewConfiguration &pc, int
    deviceProfileIndex, QString *errorMessage, int initialZoom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html

    Parameters
    ----------

    a0 : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pc : qdesigner_internal.PreviewConfiguration
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PreviewConfiguration, which stays Python's own.

    deviceProfileIndex : int
      Passed on as it is.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    initialZoom : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::PreviewManager::createPreview(const
    #      QDesignerFormWindowInterface *a0, const PreviewConfiguration &pc,
    #      int deviceProfileIndex, QString *errorMessage, int initialZoom)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager13createPreviewEPK28Q'
        'DesignerFormWindowInterfaceRKNS_20PreviewConfigurationEiP7QStringi',
        self._addressOf(a0), self._valueOf(pc), deviceProfileIndex,
        self._addressOf(errorMessage), initialZoom,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def updatePreviewClosed(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PreviewManager::updatePreviewClosed(QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-previewmanager.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::PreviewManager::updatePreviewClosed(QWidget
    #      *w)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14PreviewManager19updatePreviewClosed'
        'EP7QWidget',
        self._addressOf(w),
    )
