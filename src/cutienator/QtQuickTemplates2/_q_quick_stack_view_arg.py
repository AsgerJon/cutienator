"""
QQuickStackViewArg binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickStackViewArg to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl, QVariant
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQuickItem = WAIT['QQuickItem']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickStackViewArg(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickStackViewArg: a plain Python object standing in
  front of one C++ QQuickStackViewArg.

  C++ hands a QQuickStackViewArg around as a copy, so every C++
  QQuickStackViewArg behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQuickStackViewArg yet. It can be made from Python, in
  5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickStackViewArg::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQuickStackViewArg::~QQuickStackViewArg()': the destructor: Python
    removes its C++ QQuickStackViewArg by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 3 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickStackViewArg is created at the first use, not by
    'QQuickStackViewArg(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickStackViewArg back gives a copy the ritual made
    for Python, in a new cute QQuickStackViewArg.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStackViewArg'

  #  Qt's '~QQuickStackViewArg()'. Naming it makes this a value class: Python
  #  owns every C++ QQuickStackViewArg behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQuickStackViewArgD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QQuickStackViewArg::QQuickStackViewArg()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewarg.html#QQuickStackViewArg
    """
    #  QQuickStackViewArg::QQuickStackViewArg()
    self._noteCreation(QQuickStackViewArg, lambda: Rituals.call(
        'ritual_ZN18QQuickStackViewArgC1Ev',
    ))

  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, item: Optional[QQuickItem]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStackViewArg::QQuickStackViewArg(QQuickItem *item)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewarg.html#QQuickStackViewArg

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickStackViewArg::QQuickStackViewArg(QQuickItem *item)
    self._noteCreation(QQuickStackViewArg, lambda: Rituals.call(
        'ritual_ZN18QQuickStackViewArgC1EP10QQuickItem',
        self._addressOf(item),
    ))

  @overload(QUrl)
  def __init__(self, url: QUrl) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStackViewArg::QQuickStackViewArg(const QUrl &url)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewarg.html#QQuickStackViewArg

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  QQuickStackViewArg::QQuickStackViewArg(const QUrl &url)
    self._noteCreation(QQuickStackViewArg, lambda: Rituals.call(
        'ritual_ZN18QQuickStackViewArgC1ERK4QUrl', self._valueOf(url),
    ))

  @overload(QQmlComponent)
  def __init__(self, component: Optional[QQmlComponent]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStackViewArg::QQuickStackViewArg(QQmlComponent *component)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewarg.html#QQuickStackViewArg

    Parameters
    ----------

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickStackViewArg::QQuickStackViewArg(QQmlComponent *component)
    self._noteCreation(QQuickStackViewArg, lambda: Rituals.call(
        'ritual_ZN18QQuickStackViewArgC1EP13QQmlComponent',
        self._addressOf(component),
    ))

  @overload(QMap[str, QVariant])
  def __init__(self, properties: QMap[str, QVariant]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickStackViewArg::QQuickStackViewArg(const QVariantMap &properties)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstackviewarg.html#QQuickStackViewArg

    Parameters
    ----------

    properties : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  QQuickStackViewArg::QQuickStackViewArg(const QVariantMap &properties)
    self._noteCreation(QQuickStackViewArg, lambda: Rituals.call(
        'ritual_ZN18QQuickStackViewArgC1ERK4QMapI7QString8QVariantE',
        self._valueOf(properties),
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


#  Qt's 'QList<QQuickStackViewArg>': the list of QQuickStackViewArg, which
#  'QList[QQuickStackViewArg]' gives. It is made here, so that there is one
#  as soon as there can be a QQuickStackViewArg.
QList.createKind(
    QQuickStackViewArg, 'value',
    make='ritual_list_make_QQuickStackViewArg',
    add='ritual_list_add_QQuickStackViewArg',
    size='ritual_list_size_QQuickStackViewArg',
    at='ritual_list_at_QQuickStackViewArg',
    drop='ritual_list_drop_QQuickStackViewArg',
)
