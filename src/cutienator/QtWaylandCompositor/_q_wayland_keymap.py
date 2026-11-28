"""
QWaylandKeymap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandkeymap.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QWaylandKeymapPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandKeymap(QObject):
  """
  The cute side of Qt's QWaylandKeymap: a plain Python object standing in
  front of one C++ QWaylandKeymap.

  It is built on the cute 'QObject', as Qt's QWaylandKeymap is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandKeymap that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'd_func', 'layout',
  'setLayout', 'variant', 'setVariant', 'options', 'setOptions', 'rules',
  'setRules', 'model', 'setModel', 'layoutChanged', 'variantChanged',
  'optionsChanged', 'rulesChanged', 'modelChanged'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandKeymap::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWaylandKeymap::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QWaylandKeymapPrivate *QWaylandKeymap::d_func() const': takes
    in Python what 'QWaylandKeymapPrivate *QWaylandKeymap::d_func()' takes.
  - Qt's 'QQmlListProperty<QObject> QWaylandKeymap::data()': gives a type
    Python has no way to take yet.
  - Qt's 'void QWaylandKeymap::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'qsizetype QWaylandKeymap::countFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QWaylandKeymap::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'void QWaylandKeymap::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandKeymap is created at the first use, not by
    'QWaylandKeymap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandKeymap.
  - Qt tells when it has removed the C++ QWaylandKeymap. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandKeymap that has no cute function yet,
    'appendFunction', 'atFunction', 'clearFunction', 'countFunction', 'data',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

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
    Calls Qt's 'QString QWaylandKeymap::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#tr

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
    #  QString QWaylandKeymap::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QWaylandKeymap2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandKeymap'

  #  A C++ QWaylandKeymap Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandKeymap'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandKeymap::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandKeymap::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QWaylandKeymap10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def layout(self) -> str:
    """
    Calls Qt's 'QString QWaylandKeymap::layout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#layout

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandKeymap::layout() const
    return self.uglySide.call('ritual_ZNK14QWaylandKeymap6layoutEv')

  def variant(self) -> str:
    """
    Calls Qt's 'QString QWaylandKeymap::variant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#variant

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandKeymap::variant() const
    return self.uglySide.call('ritual_ZNK14QWaylandKeymap7variantEv')

  def options(self) -> str:
    """
    Calls Qt's 'QString QWaylandKeymap::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#options

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandKeymap::options() const
    return self.uglySide.call('ritual_ZNK14QWaylandKeymap7optionsEv')

  def rules(self) -> str:
    """
    Calls Qt's 'QString QWaylandKeymap::rules() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#rules

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandKeymap::rules() const
    return self.uglySide.call('ritual_ZNK14QWaylandKeymap5rulesEv')

  def model(self) -> str:
    """
    Calls Qt's 'QString QWaylandKeymap::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#model

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandKeymap::model() const
    return self.uglySide.call('ritual_ZNK14QWaylandKeymap5modelEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLayout(self, layout: str) -> None:
    """
    Calls Qt's 'void QWaylandKeymap::setLayout(const QString &layout)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#setLayout

    Parameters
    ----------

    layout : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWaylandKeymap::setLayout(const QString &layout)
    self.uglySide.call(
        'ritual_ZN14QWaylandKeymap9setLayoutERK7QString', layout,
    )

  @overload(str)
  def setVariant(self, variant: str) -> None:
    """
    Calls Qt's 'void QWaylandKeymap::setVariant(const QString &variant)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#setVariant

    Parameters
    ----------

    variant : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWaylandKeymap::setVariant(const QString &variant)
    self.uglySide.call(
        'ritual_ZN14QWaylandKeymap10setVariantERK7QString', variant,
    )

  @overload(str)
  def setOptions(self, options: str) -> None:
    """
    Calls Qt's 'void QWaylandKeymap::setOptions(const QString &options)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#setOptions

    Parameters
    ----------

    options : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWaylandKeymap::setOptions(const QString &options)
    self.uglySide.call(
        'ritual_ZN14QWaylandKeymap10setOptionsERK7QString', options,
    )

  @overload(str)
  def setRules(self, rules: str) -> None:
    """
    Calls Qt's 'void QWaylandKeymap::setRules(const QString &rules)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#setRules

    Parameters
    ----------

    rules : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWaylandKeymap::setRules(const QString &rules)
    self.uglySide.call(
        'ritual_ZN14QWaylandKeymap8setRulesERK7QString', rules,
    )

  @overload(str)
  def setModel(self, model: str) -> None:
    """
    Calls Qt's 'void QWaylandKeymap::setModel(const QString &model)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#setModel

    Parameters
    ----------

    model : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWaylandKeymap::setModel(const QString &model)
    self.uglySide.call(
        'ritual_ZN14QWaylandKeymap8setModelERK7QString', model,
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

  @overload()
  @overload(str)
  @overload(str, str)
  @overload(str, str, str)
  @overload(str, str, str, str)
  @overload(str, str, str, str, str)
  @overload(str, str, str, str, str, QObject)
  @overload(str, str, str, str, str, NoneType)
  def __init__(
      self,
      layout: str = '',
      variant: str = '',
      options: str = '',
      model: str = '',
      rules: str = '',
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QWaylandKeymap::QWaylandKeymap(const
    QString &layout, const QString &variant, const QString &options, const
    QString &model, const QString &rules, QObject *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#QWaylandKeymap

    Parameters
    ----------

    layout : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    variant : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    options : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    model : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    rules : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandKeymap::QWaylandKeymap(const QString &layout, const QString
    #      &variant, const QString &options, const QString &model, const
    #      QString &rules, QObject *parent)
    self._noteCreation(QWaylandKeymap, lambda: Rituals.call(
        'ritual_ZN14QWaylandKeymapC1ERK7QStringS2_S2_S2_S2_P7QObject',
        layout, variant, options, model, rules, self._addressOf(parent,
        'QObject'),
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

  def d_func(self) -> Optional[QWaylandKeymapPrivate]:
    """
    Calls Qt's 'QWaylandKeymapPrivate *QWaylandKeymap::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#d_func

    Returns
    -------

    Optional[QWaylandKeymapPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandKeymapPrivate *QWaylandKeymap::d_func()
    address = self.uglySide.call('ritual_ZN14QWaylandKeymap6d_funcEv')
    from . import QWaylandKeymapPrivate
    return QWaylandKeymapPrivate._cuteAt(address)

  def layoutChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandKeymap::layoutChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#layoutChanged
    """
    #  void QWaylandKeymap::layoutChanged()
    self.uglySide.call('ritual_ZN14QWaylandKeymap13layoutChangedEv')

  def variantChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandKeymap::variantChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#variantChanged
    """
    #  void QWaylandKeymap::variantChanged()
    self.uglySide.call('ritual_ZN14QWaylandKeymap14variantChangedEv')

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandKeymap::optionsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#optionsChanged
    """
    #  void QWaylandKeymap::optionsChanged()
    self.uglySide.call('ritual_ZN14QWaylandKeymap14optionsChangedEv')

  def rulesChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandKeymap::rulesChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#rulesChanged
    """
    #  void QWaylandKeymap::rulesChanged()
    self.uglySide.call('ritual_ZN14QWaylandKeymap12rulesChangedEv')

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandKeymap::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeymap.html#modelChanged
    """
    #  void QWaylandKeymap::modelChanged()
    self.uglySide.call('ritual_ZN14QWaylandKeymap12modelChangedEv')

  @staticmethod
  def appendFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandKeymap::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandKeymap.appendFunction' has no cute function yet. Qt's "
        "'void QWaylandKeymap::appendFunction(QQmlListProperty<QObject> "
        "*list, QObject *object)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def atFunction(*__, **_) -> Never:
    """
    Qt's 'QObject *QWaylandKeymap::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandKeymap.atFunction' has no cute function yet. Qt's "
        "'QObject *QWaylandKeymap::atFunction(QQmlListProperty<QObject> "
        "*list, qsizetype index)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def clearFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandKeymap::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandKeymap.clearFunction' has no cute function yet. Qt's "
        "'void QWaylandKeymap::clearFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def countFunction(*__, **_) -> Never:
    """
    Qt's 'qsizetype QWaylandKeymap::countFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandKeymap.countFunction' has no cute function yet. Qt's "
        "'qsizetype QWaylandKeymap::countFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QWaylandKeymap::data()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandKeymap.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QWaylandKeymap::data()': gives a type "
        "Python has no way to take yet.")
