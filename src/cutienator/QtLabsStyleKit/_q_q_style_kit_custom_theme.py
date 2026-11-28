"""
QQStyleKitCustomTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomtheme_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitCustomTheme to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlComponent


class QQStyleKitCustomTheme(QObject):
  """
  The cute side of Qt's QQStyleKitCustomTheme: a plain Python object standing
  in front of one C++ QQStyleKitCustomTheme.

  It is built on the cute 'QObject', as Qt's QQStyleKitCustomTheme is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitCustomTheme that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'name', 'theme',
  'nameChanged', 'themeChanged'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitCustomTheme::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQStyleKitCustomTheme::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  8 of the 15 functions Qt declares: 3 leans on 'QQStyleKitCustomTheme; 2 not
  a gap; 2 forbidden; 1 leans on 'vtable for QQStyleKitCustomTheme', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QQStyleKitCustomTheme is created at the first use, not by
    'QQStyleKitCustomTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitCustomTheme.
  - Qt tells when it has removed the C++ QQStyleKitCustomTheme. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitCustomTheme that has no cute function yet,
    '__init__', 'setName', 'setTheme', holds a function that raises
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
  __qt_class__ = 'QQStyleKitCustomTheme'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitCustomTheme::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcustomtheme.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitCustomTheme::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQStyleKitCustomTheme10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQStyleKitCustomTheme::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcustomtheme.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQStyleKitCustomTheme::name() const
    return self.uglySide.call('ritual_ZNK21QQStyleKitCustomTheme4nameEv')

  def theme(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQStyleKitCustomTheme::theme() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcustomtheme.html#theme

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQStyleKitCustomTheme::theme() const
    address = self.uglySide.call('ritual_ZNK21QQStyleKitCustomTheme5themeEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

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
    Qt's 'QQStyleKitCustomTheme::QQStyleKitCustomTheme(QObject *parent)':
    leans on 'vtable for QQStyleKitCustomTheme', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitCustomTheme.__init__' has no cute function yet. Qt's "
        "'QQStyleKitCustomTheme::QQStyleKitCustomTheme(QObject *parent)': "
        "leans on 'vtable for QQStyleKitCustomTheme', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitCustomTheme::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcustomtheme.html#nameChanged
    """
    #  void QQStyleKitCustomTheme::nameChanged()
    self.uglySide.call('ritual_ZN21QQStyleKitCustomTheme11nameChangedEv')

  def themeChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitCustomTheme::themeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcustomtheme.html#themeChanged
    """
    #  void QQStyleKitCustomTheme::themeChanged()
    self.uglySide.call('ritual_ZN21QQStyleKitCustomTheme12themeChangedEv')

  @staticmethod
  def setName(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitCustomTheme::setName(const QString &newName)': leans
    on 'QQStyleKitCustomTheme::nameChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitCustomTheme.setName' has no cute function yet. Qt's "
        "'void QQStyleKitCustomTheme::setName(const QString &newName)': "
        "leans on 'QQStyleKitCustomTheme::nameChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setTheme(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitCustomTheme::setTheme(QQmlComponent *newTheme)':
    leans on 'QQStyleKitCustomTheme::themeChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitCustomTheme.setTheme' has no cute function yet. Qt's "
        "'void QQStyleKitCustomTheme::setTheme(QQmlComponent *newTheme)': "
        "leans on 'QQStyleKitCustomTheme::themeChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")


#  Qt's 'QList<QQStyleKitCustomTheme *>': the list of QQStyleKitCustomTheme,
#  which 'QList[QQStyleKitCustomTheme]' gives. It is made here, so that there
#  is one as soon as there can be a QQStyleKitCustomTheme.
QList.createKind(
    QQStyleKitCustomTheme, 'address',
    make='ritual_list_make_QQStyleKitCustomTheme_ptr',
    add='ritual_list_add_QQStyleKitCustomTheme_ptr',
    size='ritual_list_size_QQStyleKitCustomTheme_ptr',
    at='ritual_list_at_QQStyleKitCustomTheme_ptr',
    drop='ritual_list_drop_QQStyleKitCustomTheme_ptr',
)
