"""
qdesigner_internal::QDesignerFormBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_formbuilder_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerFormBuilder to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QFormBuilder, qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QString
  from ..QtGui import QIcon, QPixmap
  from ..QtWidgets import QLayout, QLayoutItem, QWidget
  from . import DomLayout, DomLayoutItem, DomProperty, DomResources, DomUI
  from . import DomWidget, QDesignerFormEditorInterface
  from . import QDesignerFormWindowInterface, QtResourceSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomLayout = WAIT['DomLayout']
  DomLayoutItem = WAIT['DomLayoutItem']
  DomProperty = WAIT['DomProperty']
  DomResources = WAIT['DomResources']
  DomUI = WAIT['DomUI']
  DomWidget = WAIT['DomWidget']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QLayout = WAIT['QLayout']
  QLayoutItem = WAIT['QLayoutItem']
  QObject = WAIT['QObject']
  QString = WAIT['QString']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerFormBuilder(QFormBuilder):
  """
  The cute side of Qt's qdesigner_internal::QDesignerFormBuilder: a plain
  Python object standing in front of one C++
  qdesigner_internal::QDesignerFormBuilder.

  It is built on the cute 'QFormBuilder', as Qt's
  qdesigner_internal::QDesignerFormBuilder is built on Qt's QFormBuilder, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerFormBuilder that has a
  ritual and that Python can call so far, 15 names in all: 'createWidget',
  'core', 'systemStyle', 'createPreview', 'createPreviewPixmap', 'create',
  'createDom', 'createResources', 'addItem', 'nameToIcon', 'nameToPixmap',
  'applyProperties', 'loadExtraInfo', 'internalResourceSet', 'deviceProfile'.
  It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerFormBuilder is created at the first
    use, not by 'qdesigner_internal::QDesignerFormBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::QDesignerFormBuilder.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      QDesignerFormWindowInterface, str, str,
      WAIT['qdesigner_internal.DeviceProfile'], QString,
  )
  @overload(
      QDesignerFormWindowInterface, str, str,
      WAIT['qdesigner_internal.DeviceProfile'], NoneType,
  )
  @overload(
      NoneType, str, str, WAIT['qdesigner_internal.DeviceProfile'], QString,
  )
  @overload(
      NoneType, str, str, WAIT['qdesigner_internal.DeviceProfile'], NoneType,
  )
  def createPreview(
      fw: Optional[QDesignerFormWindowInterface],
      styleName: str,
      appStyleSheet: str,
      deviceProfile: qdesigner_internal.DeviceProfile,
      errorMessage: Optional[QString],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::QDesignerFormBuilder::createPreview(const
    QDesignerFormWindowInterface *fw, const QString &styleName, const QString
    &appStyleSheet, const DeviceProfile &deviceProfile, QString
    *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    styleName : str
      Passed on as it is: a QString is made of it for the call.

    appStyleSheet : str
      Passed on as it is: a QString is made of it for the call.

    deviceProfile : qdesigner_internal.DeviceProfile
      Passed on as a value: Qt reads the C++
      qdesigner_internal::DeviceProfile, which stays Python's own.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerFormBuilder::createPreview(const
    #      QDesignerFormWindowInterface *fw, const QString &styleName, const
    #      QString &appStyleSheet, const DeviceProfile &deviceProfile,
    #      QString *errorMessage)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder13createPreview'
        'EPK28QDesignerFormWindowInterfaceRK7QStringS6_RKNS_13DeviceProfile'
        'EPS4_',
        CuteMixin._addressOf(fw), styleName, appStyleSheet,
        CuteMixin._valueOf(deviceProfile),
        CuteMixin._addressOf(errorMessage),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  @overload(QDesignerFormWindowInterface, str)
  @overload(NoneType, str)
  def createPreview(
      fw: Optional[QDesignerFormWindowInterface],
      styleName: str = '',
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::QDesignerFormBuilder::createPreview(const
    QDesignerFormWindowInterface *fw, const QString &styleName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    styleName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerFormBuilder::createPreview(const
    #      QDesignerFormWindowInterface *fw, const QString &styleName)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder13createPreview'
        'EPK28QDesignerFormWindowInterfaceRK7QString',
        CuteMixin._addressOf(fw), styleName,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(QDesignerFormWindowInterface, str, str, QString)
  @overload(QDesignerFormWindowInterface, str, str, NoneType)
  @overload(NoneType, str, str, QString)
  @overload(NoneType, str, str, NoneType)
  def createPreview(
      fw: Optional[QDesignerFormWindowInterface],
      styleName: str,
      appStyleSheet: str,
      errorMessage: Optional[QString],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::QDesignerFormBuilder::createPreview(const
    QDesignerFormWindowInterface *fw, const QString &styleName, const QString
    &appStyleSheet, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    styleName : str
      Passed on as it is: a QString is made of it for the call.

    appStyleSheet : str
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
    #  QWidget *qdesigner_internal::QDesignerFormBuilder::createPreview(const
    #      QDesignerFormWindowInterface *fw, const QString &styleName, const
    #      QString &appStyleSheet, QString *errorMessage)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder13createPreview'
        'EPK28QDesignerFormWindowInterfaceRK7QStringS6_PS4_',
        CuteMixin._addressOf(fw), styleName, appStyleSheet,
        CuteMixin._addressOf(errorMessage),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(QDesignerFormWindowInterface, str, str)
  @overload(NoneType, str, str)
  def createPreview(
      fw: Optional[QDesignerFormWindowInterface],
      styleName: str,
      appStyleSheet: str,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::QDesignerFormBuilder::createPreview(const
    QDesignerFormWindowInterface *fw, const QString &styleName, const QString
    &appStyleSheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    styleName : str
      Passed on as it is: a QString is made of it for the call.

    appStyleSheet : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerFormBuilder::createPreview(const
    #      QDesignerFormWindowInterface *fw, const QString &styleName, const
    #      QString &appStyleSheet)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder13createPreview'
        'EPK28QDesignerFormWindowInterfaceRK7QStringS6_',
        CuteMixin._addressOf(fw), styleName, appStyleSheet,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @staticmethod
  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  @overload(QDesignerFormWindowInterface, str)
  @overload(NoneType, str)
  @overload(QDesignerFormWindowInterface, str, str)
  @overload(NoneType, str, str)
  def createPreviewPixmap(
      fw: Optional[QDesignerFormWindowInterface],
      styleName: str = '',
      appStyleSheet: str = '',
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    qdesigner_internal::QDesignerFormBuilder::createPreviewPixmap(const
    QDesignerFormWindowInterface *fw, const QString &styleName, const QString
    &appStyleSheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    styleName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    appStyleSheet : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap qdesigner_internal::QDesignerFormBuilder::createPreviewPixmap(
    #      const QDesignerFormWindowInterface *fw, const QString &styleName,
    #      const QString &appStyleSheet)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder19createPreview'
        'PixmapEPK28QDesignerFormWindowInterfaceRK7QStringS6_',
        CuteMixin._addressOf(fw), styleName, appStyleSheet,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerFormBuilder'

  #  The functions Qt calls itself that
  #  qdesigner_internal::QDesignerFormBuilder is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'createWidget': (
          ('_ZN18qdesigner_internal20QDesignerFormBuilder12createWidgetEP9D'
           'omWidgetP7QWidget',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtDesigner:DomWidget'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'nameToIcon': (
          ('_ZN18qdesigner_internal20QDesignerFormBuilder10nameToIconERK7QS'
           'tringS3_',
           ('address', 'value', 'QtGui:QIcon'),
           (
               ('address', 'text', ''),
               ('address', 'text', ''),
           )),
      ),
      'nameToPixmap': (
          ('_ZN18qdesigner_internal20QDesignerFormBuilder12nameToPixmapERK7'
           'QStringS3_',
           ('address', 'value', 'QtGui:QPixmap'),
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

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *qdesigner_internal::QDesignerFormBuilder::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface
    #      *qdesigner_internal::QDesignerFormBuilder::core() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal20QDesignerFormBuilder4coreEv',
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  def systemStyle(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::QDesignerFormBuilder::systemStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::QDesignerFormBuilder::systemStyle() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal20QDesignerFormBuilder11systemStyleE'
        'v',
    )

  def internalResourceSet(self) -> Optional[QtResourceSet]:
    """
    Calls Qt's 'QtResourceSet
    *qdesigner_internal::QDesignerFormBuilder::internalResourceSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Returns
    -------

    Optional[QtResourceSet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtResourceSet
    #      *qdesigner_internal::QDesignerFormBuilder::internalResourceSet()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal20QDesignerFormBuilder19internalReso'
        'urceSetEv',
    )
    from . import QtResourceSet
    return QtResourceSet._cuteAt(address)

  def deviceProfile(self) -> qdesigner_internal.DeviceProfile:
    """
    Calls Qt's 'DeviceProfile
    qdesigner_internal::QDesignerFormBuilder::deviceProfile() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Returns
    -------

    qdesigner_internal.DeviceProfile
      A new cute qdesigner_internal::DeviceProfile around the copy Qt gave
      back. Python owns it.
    """
    #  DeviceProfile
    #      qdesigner_internal::QDesignerFormBuilder::deviceProfile() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal20QDesignerFormBuilder13deviceProfil'
        'eEv',
    )
    return qdesigner_internal.DeviceProfile._cuteOwning(address)

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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  @overload(
      QDesignerFormEditorInterface, WAIT['qdesigner_internal.DeviceProfile'],
  )
  @overload(NoneType, WAIT['qdesigner_internal.DeviceProfile'])
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      deviceProfile: Optional[qdesigner_internal.DeviceProfile] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::QDesignerFormBuilder::QDesignerFormBuilder(
    QDesignerFormEditorInterface *core, const DeviceProfile &deviceProfile)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    deviceProfile : Optional[qdesigner_internal.DeviceProfile]
      Passed on as a value: Qt reads the C++
      qdesigner_internal::DeviceProfile, which stays Python's own. May be
      left out, as in Qt: a new 'qdesigner_internal.DeviceProfile()' is then
      passed on.
    """
    #  qdesigner_internal::QDesignerFormBuilder::QDesignerFormBuilder(
    #      QDesignerFormEditorInterface *core, const DeviceProfile
    #      &deviceProfile)
    if deviceProfile is None:
      deviceProfile = qdesigner_internal.DeviceProfile()
    self._noteCreation(QDesignerFormBuilder, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilderC1EP28QDesigner'
        'FormEditorInterfaceRKNS_13DeviceProfileE',
        self._addressOf(core), self._valueOf(deviceProfile),
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

  @overload(DomWidget)
  @overload(NoneType)
  @overload(DomWidget, QWidget)
  @overload(DomWidget, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def createWidget(
      self,
      ui_widget: Optional[DomWidget],
      parentWidget: Optional[QWidget] = None,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::QDesignerFormBuilder::createWidget(DomWidget
    *ui_widget, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget
    #      *qdesigner_internal::QDesignerFormBuilder::createWidget(DomWidget
    #      *ui_widget, QWidget *parentWidget)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder12createWidgetE'
        'P9DomWidgetP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder12createW'
          'idgetEP9DomWidgetP7QWidget')
    address = self.uglySide.call(
        ritual, self._addressOf(ui_widget), self._addressOf(parentWidget),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(str, QWidget, str)
  @overload(str, NoneType, str)
  def createWidget(
      self,
      widgetName: str,
      parentWidget: Optional[QWidget],
      name: str,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::QDesignerFormBuilder::createWidget(const QString
    &widgetName, QWidget *parentWidget, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    widgetName : str
      Passed on as it is: a QString is made of it for the call.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerFormBuilder::createWidget(const
    #      QString &widgetName, QWidget *parentWidget, const QString &name)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder12createWidgetE'
        'RK7QStringP7QWidgetS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder12createW'
          'idgetERK7QStringP7QWidgetS3_')
    address = self.uglySide.call(
        ritual, widgetName, self._addressOf(parentWidget), name,
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(DomUI, QWidget)
  @overload(DomUI, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def create(
      self,
      ui: Optional[DomUI],
      parentWidget: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::QDesignerFormBuilder::create(DomUI *ui, QWidget
    *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    ui : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerFormBuilder::create(DomUI *ui,
    #      QWidget *parentWidget)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder6createEP5DomUI'
        'P7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder6createEP'
          '5DomUIP7QWidget')
    address = self.uglySide.call(
        ritual, self._addressOf(ui), self._addressOf(parentWidget),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(DomWidget, QWidget)
  @overload(DomWidget, NoneType)
  def create(
      self,
      ui_widget: Optional[DomWidget],
      parentWidget: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget
    *qdesigner_internal::QDesignerFormBuilder::create(DomWidget *ui_widget,
    QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *qdesigner_internal::QDesignerFormBuilder::create(DomWidget
    #      *ui_widget, QWidget *parentWidget)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder6createEP9DomWi'
        'dgetP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder6createEP'
          '9DomWidgetP7QWidget')
    address = self.uglySide.call(
        ritual, self._addressOf(ui_widget), self._addressOf(parentWidget),
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  @overload(DomLayout, QLayout, QWidget)
  @overload(DomLayout, QLayout, NoneType)
  @overload(DomLayout, NoneType, QWidget)
  @overload(DomLayout, NoneType, NoneType)
  @overload(NoneType, QLayout, QWidget)
  @overload(NoneType, QLayout, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def create(
      self,
      ui_layout: Optional[DomLayout],
      layout: Optional[QLayout],
      parentWidget: Optional[QWidget],
  ) -> Optional[QLayout]:
    """
    Calls Qt's 'QLayout
    *qdesigner_internal::QDesignerFormBuilder::create(DomLayout *ui_layout,
    QLayout *layout, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    ui_layout : Optional[DomLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLayout]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayout *qdesigner_internal::QDesignerFormBuilder::create(DomLayout
    #      *ui_layout, QLayout *layout, QWidget *parentWidget)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder6createEP9DomLa'
        'youtP7QLayoutP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder6createEP'
          '9DomLayoutP7QLayoutP7QWidget')
    address = self.uglySide.call(
        ritual,
        self._addressOf(ui_layout), self._addressOf(layout),
        self._addressOf(parentWidget),
    )
    from ..QtWidgets import QLayout
    return QLayout._cuteAt(address)

  @overload(QWidget, DomWidget)
  @overload(QWidget, NoneType)
  @overload(NoneType, DomWidget)
  @overload(NoneType, NoneType)
  @overload(QWidget, DomWidget, bool)
  @overload(QWidget, NoneType, bool)
  @overload(NoneType, DomWidget, bool)
  @overload(NoneType, NoneType, bool)
  def createDom(
      self,
      widget: Optional[QWidget],
      ui_parentWidget: Optional[DomWidget],
      recursive: bool = True,
  ) -> Optional[DomWidget]:
    """
    Calls Qt's 'DomWidget
    *qdesigner_internal::QDesignerFormBuilder::createDom(QWidget *widget,
    DomWidget *ui_parentWidget, bool recursive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ui_parentWidget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    recursive : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[DomWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomWidget *qdesigner_internal::QDesignerFormBuilder::createDom(QWidget
    #      *widget, DomWidget *ui_parentWidget, bool recursive)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder9createDomEP7QW'
        'idgetP9DomWidgetb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder9createDo'
          'mEP7QWidgetP9DomWidgetb')
    address = self.uglySide.call(
        ritual,
        self._addressOf(widget), self._addressOf(ui_parentWidget), recursive,
    )
    from . import DomWidget
    return DomWidget._cuteAt(address)

  @overload(DomResources)
  @overload(NoneType)
  def createResources(self, resources: Optional[DomResources]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerFormBuilder::createResources(DomResources
    *resources)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    resources : Optional[DomResources]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QDesignerFormBuilder::createResources(
    #      DomResources *resources)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder15createResourc'
        'esEP12DomResources')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder15createR'
          'esourcesEP12DomResources')
    self.uglySide.call(ritual, self._addressOf(resources))

  @overload(DomWidget, QWidget, QWidget)
  @overload(DomWidget, QWidget, NoneType)
  @overload(DomWidget, NoneType, QWidget)
  @overload(DomWidget, NoneType, NoneType)
  @overload(NoneType, QWidget, QWidget)
  @overload(NoneType, QWidget, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def addItem(
      self,
      ui_widget: Optional[DomWidget],
      widget: Optional[QWidget],
      parentWidget: Optional[QWidget],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerFormBuilder::addItem(DomWidget *ui_widget,
    QWidget *widget, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerFormBuilder::addItem(DomWidget
    #      *ui_widget, QWidget *widget, QWidget *parentWidget)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder7addItemEP9DomW'
        'idgetP7QWidgetS4_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder7addItemE'
          'P9DomWidgetP7QWidgetS4_')
    return self.uglySide.call(
        ritual,
        self._addressOf(ui_widget), self._addressOf(widget),
        self._addressOf(parentWidget),
    )

  @overload(DomLayoutItem, QLayoutItem, QLayout)
  @overload(DomLayoutItem, QLayoutItem, NoneType)
  @overload(DomLayoutItem, NoneType, QLayout)
  @overload(DomLayoutItem, NoneType, NoneType)
  @overload(NoneType, QLayoutItem, QLayout)
  @overload(NoneType, QLayoutItem, NoneType)
  @overload(NoneType, NoneType, QLayout)
  def addItem(
      self,
      ui_item: Optional[DomLayoutItem],
      item: Optional[QLayoutItem],
      layout: Optional[QLayout],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::QDesignerFormBuilder::addItem(DomLayoutItem *ui_item,
    QLayoutItem *item, QLayout *layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    ui_item : Optional[DomLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::QDesignerFormBuilder::addItem(DomLayoutItem
    #      *ui_item, QLayoutItem *item, QLayout *layout)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder7addItemEP13Dom'
        'LayoutItemP11QLayoutItemP7QLayout')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder7addItemE'
          'P13DomLayoutItemP11QLayoutItemP7QLayout')
    return self.uglySide.call(
        ritual,
        self._addressOf(ui_item), self._addressOf(item, 'QLayoutItem'),
        self._addressOf(layout),
    )

  @overload(str, str)
  def nameToIcon(self, filePath: str, qrcPath: str) -> QIcon:
    """
    Calls Qt's 'QIcon
    qdesigner_internal::QDesignerFormBuilder::nameToIcon(const QString
    &filePath, const QString &qrcPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    qrcPath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon qdesigner_internal::QDesignerFormBuilder::nameToIcon(const
    #      QString &filePath, const QString &qrcPath)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder10nameToIconERK'
        '7QStringS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder10nameToI'
          'conERK7QStringS3_')
    address = self.uglySide.call(ritual, filePath, qrcPath)
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  @overload(str, str)
  def nameToPixmap(self, filePath: str, qrcPath: str) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    qdesigner_internal::QDesignerFormBuilder::nameToPixmap(const QString
    &filePath, const QString &qrcPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    qrcPath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap qdesigner_internal::QDesignerFormBuilder::nameToPixmap(const
    #      QString &filePath, const QString &qrcPath)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder12nameToPixmapE'
        'RK7QStringS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder12nameToP'
          'ixmapERK7QStringS3_')
    address = self.uglySide.call(ritual, filePath, qrcPath)
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  @overload(QObject, QList[DomProperty])
  @overload(NoneType, QList[DomProperty])
  def applyProperties(
      self,
      o: Optional[QObject],
      properties: QList[DomProperty],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerFormBuilder::applyProperties(QObject *o,
    const QList<DomProperty *> &properties)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    properties : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::QDesignerFormBuilder::applyProperties(QObject
    #      *o, const QList<DomProperty *> &properties)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder15applyProperti'
        'esEP7QObjectRK5QListIP11DomPropertyE',
        self._addressOf(o, 'QObject'), self._valueOf(properties),
    )

  @overload(DomWidget, QWidget, QWidget)
  @overload(DomWidget, QWidget, NoneType)
  @overload(DomWidget, NoneType, QWidget)
  @overload(DomWidget, NoneType, NoneType)
  @overload(NoneType, QWidget, QWidget)
  @overload(NoneType, QWidget, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def loadExtraInfo(
      self,
      ui_widget: Optional[DomWidget],
      widget: Optional[QWidget],
      parentWidget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerFormBuilder::loadExtraInfo(DomWidget
    *ui_widget, QWidget *widget, QWidget *parentWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformbuilder.html

    Parameters
    ----------

    ui_widget : Optional[DomWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::QDesignerFormBuilder::loadExtraInfo(DomWidget
    #      *ui_widget, QWidget *widget, QWidget *parentWidget)
    ritual = (
        'ritual_ZN18qdesigner_internal20QDesignerFormBuilder13loadExtraInfo'
        'EP9DomWidgetP7QWidgetS4_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal20QDesignerFormBuilder13loadExt'
          'raInfoEP9DomWidgetP7QWidgetS4_')
    self.uglySide.call(
        ritual,
        self._addressOf(ui_widget), self._addressOf(widget),
        self._addressOf(parentWidget),
    )
