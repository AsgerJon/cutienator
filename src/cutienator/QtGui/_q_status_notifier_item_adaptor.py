"""
QStatusNotifierItemAdaptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qstatusnotifieritemadaptor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QStatusNotifierItemAdaptor to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QXdgDBusImageStruct, QXdgDBusToolTipStruct
  from ..QtDBus import QDBusObjectPath


class QStatusNotifierItemAdaptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QStatusNotifierItemAdaptor: a plain Python object
  standing in front of one C++ QStatusNotifierItemAdaptor.

  What exists
  -----------

  Every function of Qt's QStatusNotifierItemAdaptor that has a ritual and
  that Python can call so far, 25 names in all: 'metaObject',
  'attentionIconName', 'attentionMovieName', 'category', 'iconName', 'id',
  'itemIsMenu', 'menu', 'overlayIconName', 'overlayIconPixmap', 'status',
  'title', 'toolTip', 'Activate', 'ContextMenu', 'ProvideXdgActivationToken',
  'Scroll', 'SecondaryActivate', 'NewAttentionIcon', 'NewIcon',
  'NewOverlayIcon', 'NewMenu', 'NewStatus', 'NewTitle', 'NewToolTip'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QStatusNotifierItemAdaptor::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QStatusNotifierItemAdaptor::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QStatusNotifierItemAdaptor::~QStatusNotifierItemAdaptor()': the
    destructor: Python never removes a C++ QStatusNotifierItemAdaptor.

  What has no ritual
  ------------------

  6 of the 34 functions Qt declares: 2 not a gap; 2 leans on
  'QStatusNotifierItemAdaptor; 2 leans on 'iconToQXdgDBusImageVector(QIcon
  const&)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken.

  What to expect
  --------------

  - The C++ QStatusNotifierItemAdaptor is created at the first use, not by
    'QStatusNotifierItemAdaptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStatusNotifierItemAdaptor.
  - Qt tells when it has removed the C++ QStatusNotifierItemAdaptor. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QStatusNotifierItemAdaptor that has no cute function
    yet, '__init__', 'attentionIconPixmap', 'iconPixmap', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStatusNotifierItemAdaptor'

  #  A C++ QStatusNotifierItemAdaptor Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStatusNotifierItemAdaptor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStatusNotifierItemAdaptor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStatusNotifierItemAdaptor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def attentionIconName(self) -> str:
    """
    Calls Qt's 'QString QStatusNotifierItemAdaptor::attentionIconName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#attentionIconName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStatusNotifierItemAdaptor::attentionIconName() const
    return self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor17attentionIconNameEv',
    )

  def attentionMovieName(self) -> str:
    """
    Calls Qt's 'QString QStatusNotifierItemAdaptor::attentionMovieName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#attentionMovieName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStatusNotifierItemAdaptor::attentionMovieName() const
    return self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor18attentionMovieNameEv',
    )

  def category(self) -> str:
    """
    Calls Qt's 'QString QStatusNotifierItemAdaptor::category() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#category

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStatusNotifierItemAdaptor::category() const
    return self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor8categoryEv',
    )

  def iconName(self) -> str:
    """
    Calls Qt's 'QString QStatusNotifierItemAdaptor::iconName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#iconName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStatusNotifierItemAdaptor::iconName() const
    return self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor8iconNameEv',
    )

  def id(self) -> str:
    """
    Calls Qt's 'QString QStatusNotifierItemAdaptor::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#id

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStatusNotifierItemAdaptor::id() const
    return self.uglySide.call('ritual_ZNK26QStatusNotifierItemAdaptor2idEv')

  def itemIsMenu(self) -> bool:
    """
    Calls Qt's 'bool QStatusNotifierItemAdaptor::itemIsMenu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#itemIsMenu
    """
    #  bool QStatusNotifierItemAdaptor::itemIsMenu() const
    return self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor10itemIsMenuEv',
    )

  def menu(self) -> QDBusObjectPath:
    """
    Calls Qt's 'QDBusObjectPath QStatusNotifierItemAdaptor::menu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#menu

    Returns
    -------

    QDBusObjectPath
      A new cute QDBusObjectPath around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusObjectPath QStatusNotifierItemAdaptor::menu() const
    address = self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor4menuEv',
    )
    from ..QtDBus import QDBusObjectPath
    return QDBusObjectPath._cuteOwning(address)

  def overlayIconName(self) -> str:
    """
    Calls Qt's 'QString QStatusNotifierItemAdaptor::overlayIconName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#overlayIconName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStatusNotifierItemAdaptor::overlayIconName() const
    return self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor15overlayIconNameEv',
    )

  def overlayIconPixmap(self) -> QList[QXdgDBusImageStruct]:
    """
    Calls Qt's 'QXdgDBusImageVector
    QStatusNotifierItemAdaptor::overlayIconPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#overlayIconPixmap

    Returns
    -------

    QList[QXdgDBusImageStruct]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QXdgDBusImageVector QStatusNotifierItemAdaptor::overlayIconPixmap()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor17overlayIconPixmapEv',
    )
    from . import QXdgDBusImageStruct
    return QList[QXdgDBusImageStruct]._cuteOwning(address)

  def status(self) -> str:
    """
    Calls Qt's 'QString QStatusNotifierItemAdaptor::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#status

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStatusNotifierItemAdaptor::status() const
    return self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor6statusEv',
    )

  def title(self) -> str:
    """
    Calls Qt's 'QString QStatusNotifierItemAdaptor::title() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStatusNotifierItemAdaptor::title() const
    return self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor5titleEv',
    )

  def toolTip(self) -> QXdgDBusToolTipStruct:
    """
    Calls Qt's 'QXdgDBusToolTipStruct QStatusNotifierItemAdaptor::toolTip()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#toolTip

    Returns
    -------

    QXdgDBusToolTipStruct
      A new cute QXdgDBusToolTipStruct around the copy Qt gave back. Python
      owns it.
    """
    #  QXdgDBusToolTipStruct QStatusNotifierItemAdaptor::toolTip() const
    address = self.uglySide.call(
        'ritual_ZNK26QStatusNotifierItemAdaptor7toolTipEv',
    )
    from . import QXdgDBusToolTipStruct
    return QXdgDBusToolTipStruct._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QStatusNotifierItemAdaptor::QStatusNotifierItemAdaptor(QDBusTrayIcon
    *parent)': leans on
    'QStatusNotifierItemAdaptor::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QStatusNotifierItemAdaptor.__init__' has no cute function yet. "
        "Qt's "
        "'QStatusNotifierItemAdaptor::QStatusNotifierItemAdaptor(QDBusTrayIc"
        "on *parent)': leans on "
        "'QStatusNotifierItemAdaptor::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(int, int)
  def Activate(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::Activate(int x, int y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#Activate

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QStatusNotifierItemAdaptor::Activate(int x, int y)
    self.uglySide.call(
        'ritual_ZN26QStatusNotifierItemAdaptor8ActivateEii', x, y,
    )

  @overload(int, int)
  def ContextMenu(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::ContextMenu(int x, int y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#ContextMenu

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QStatusNotifierItemAdaptor::ContextMenu(int x, int y)
    self.uglySide.call(
        'ritual_ZN26QStatusNotifierItemAdaptor11ContextMenuEii', x, y,
    )

  @overload(str)
  def ProvideXdgActivationToken(self, token: str) -> None:
    """
    Calls Qt's 'void
    QStatusNotifierItemAdaptor::ProvideXdgActivationToken(const QString
    &token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html

    Parameters
    ----------

    token : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStatusNotifierItemAdaptor::ProvideXdgActivationToken(const
    #      QString &token)
    self.uglySide.call(
        'ritual_ZN26QStatusNotifierItemAdaptor25ProvideXdgActivationTokenER'
        'K7QString',
        token,
    )

  @overload(int, str)
  def Scroll(self, delta: int, orientation: str) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::Scroll(int delta, const
    QString &orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#Scroll

    Parameters
    ----------

    delta : int
      Passed on as it is.

    orientation : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStatusNotifierItemAdaptor::Scroll(int delta, const QString
    #      &orientation)
    self.uglySide.call(
        'ritual_ZN26QStatusNotifierItemAdaptor6ScrollEiRK7QString',
        delta, orientation,
    )

  @overload(int, int)
  def SecondaryActivate(self, x: int, y: int) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::SecondaryActivate(int x, int
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#SecondaryActivate

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  void QStatusNotifierItemAdaptor::SecondaryActivate(int x, int y)
    self.uglySide.call(
        'ritual_ZN26QStatusNotifierItemAdaptor17SecondaryActivateEii', x, y,
    )

  def NewAttentionIcon(self) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::NewAttentionIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#NewAttentionIcon
    """
    #  void QStatusNotifierItemAdaptor::NewAttentionIcon()
    self.uglySide.call(
        'ritual_ZN26QStatusNotifierItemAdaptor16NewAttentionIconEv',
    )

  def NewIcon(self) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::NewIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#NewIcon
    """
    #  void QStatusNotifierItemAdaptor::NewIcon()
    self.uglySide.call('ritual_ZN26QStatusNotifierItemAdaptor7NewIconEv')

  def NewOverlayIcon(self) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::NewOverlayIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#NewOverlayIcon
    """
    #  void QStatusNotifierItemAdaptor::NewOverlayIcon()
    self.uglySide.call(
        'ritual_ZN26QStatusNotifierItemAdaptor14NewOverlayIconEv',
    )

  def NewMenu(self) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::NewMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#NewMenu
    """
    #  void QStatusNotifierItemAdaptor::NewMenu()
    self.uglySide.call('ritual_ZN26QStatusNotifierItemAdaptor7NewMenuEv')

  @overload(str)
  def NewStatus(self, status: str) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::NewStatus(const QString
    &status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#NewStatus

    Parameters
    ----------

    status : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QStatusNotifierItemAdaptor::NewStatus(const QString &status)
    self.uglySide.call(
        'ritual_ZN26QStatusNotifierItemAdaptor9NewStatusERK7QString', status,
    )

  def NewTitle(self) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::NewTitle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#NewTitle
    """
    #  void QStatusNotifierItemAdaptor::NewTitle()
    self.uglySide.call('ritual_ZN26QStatusNotifierItemAdaptor8NewTitleEv')

  def NewToolTip(self) -> None:
    """
    Calls Qt's 'void QStatusNotifierItemAdaptor::NewToolTip()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatusnotifieritemadaptor.html#NewToolTip
    """
    #  void QStatusNotifierItemAdaptor::NewToolTip()
    self.uglySide.call('ritual_ZN26QStatusNotifierItemAdaptor10NewToolTipEv')

  @staticmethod
  def attentionIconPixmap(*__, **_) -> Never:
    """
    Qt's 'QXdgDBusImageVector
    QStatusNotifierItemAdaptor::attentionIconPixmap() const': leans on
    'iconToQXdgDBusImageVector(QIcon const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QStatusNotifierItemAdaptor.attentionIconPixmap' has no cute "
        "function yet. Qt's 'QXdgDBusImageVector "
        "QStatusNotifierItemAdaptor::attentionIconPixmap() const': leans on "
        "'iconToQXdgDBusImageVector(QIcon const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def iconPixmap(*__, **_) -> Never:
    """
    Qt's 'QXdgDBusImageVector QStatusNotifierItemAdaptor::iconPixmap()
    const': leans on 'iconToQXdgDBusImageVector(QIcon const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QStatusNotifierItemAdaptor.iconPixmap' has no cute function yet. "
        "Qt's 'QXdgDBusImageVector QStatusNotifierItemAdaptor::iconPixmap() "
        "const': leans on 'iconToQXdgDBusImageVector(QIcon const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
