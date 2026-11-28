"""
QQmlPropertyToPropertyBinding binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertytopropertybinding_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlPropertyToPropertyBinding to be private: it declares the
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

  from ..QtCore import QMetaProperty
  from . import QQmlAnyBinding, QQmlEngine, QQmlNotifierEndpoint
  from . import QQmlProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaProperty = WAIT['QMetaProperty']
  QQmlEngine = WAIT['QQmlEngine']
  QQmlNotifierEndpoint = WAIT['QQmlNotifierEndpoint']
  QQmlProperty = WAIT['QQmlProperty']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyToPropertyBinding(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyToPropertyBinding: a plain Python object
  standing in front of one C++ QQmlPropertyToPropertyBinding.

  C++ hands a QQmlPropertyToPropertyBinding around as a copy, so every C++
  QQmlPropertyToPropertyBinding behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlPropertyToPropertyBinding that has a ritual and
  that Python can call so far, 2 names in all: 'create', 'doConnectNotify'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlPropertyToPropertyBinding::~QQmlPropertyToPropertyBinding()':
    the destructor: Python removes its C++ QQmlPropertyToPropertyBinding by
    it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlPropertyToPropertyBinding is created at the first use, not by
    'QQmlPropertyToPropertyBinding(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlPropertyToPropertyBinding back gives a copy the
    ritual made for Python, in a new cute QQmlPropertyToPropertyBinding.
  - Each name of Qt's QQmlPropertyToPropertyBinding that has no cute function
    yet, 'readSourceValue', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlEngine, QQmlProperty, QQmlProperty)
  @overload(NoneType, QQmlProperty, QQmlProperty)
  def create(
      engine: Optional[QQmlEngine],
      source: QQmlProperty,
      target: QQmlProperty,
  ) -> QQmlAnyBinding:
    """
    Calls Qt's 'QQmlAnyBinding
    QQmlPropertyToPropertyBinding::create(QQmlEngine *engine, const
    QQmlProperty &source, const QQmlProperty &target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytopropertybinding.html#create

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    source : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    target : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    Returns
    -------

    QQmlAnyBinding
      A new cute QQmlAnyBinding around the copy Qt gave back. Python owns it.
    """
    #  QQmlAnyBinding QQmlPropertyToPropertyBinding::create(QQmlEngine
    #      *engine, const QQmlProperty &source, const QQmlProperty &target)
    address = Rituals.call(
        'ritual_ZN29QQmlPropertyToPropertyBinding6createEP10QQmlEngineRK12Q'
        'QmlPropertyS4_',
        CuteMixin._addressOf(engine), CuteMixin._valueOf(source),
        CuteMixin._valueOf(target),
    )
    from . import QQmlAnyBinding
    return QQmlAnyBinding._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyToPropertyBinding'

  #  Qt's '~QQmlPropertyToPropertyBinding()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlPropertyToPropertyBinding behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QQmlPropertyToPropertyBindingD1Ev'

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

  @overload(QQmlEngine, QQmlProperty)
  @overload(NoneType, QQmlProperty)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      source: QQmlProperty,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlPropertyToPropertyBinding::QQmlPropertyToPropertyBinding(QQmlEngine
    *engine, const QQmlProperty &source)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytopropertybinding.html

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    source : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  QQmlPropertyToPropertyBinding::QQmlPropertyToPropertyBinding(
    #      QQmlEngine *engine, const QQmlProperty &source)
    self._noteCreation(QQmlPropertyToPropertyBinding, lambda: Rituals.call(
        'ritual_ZN29QQmlPropertyToPropertyBindingC1EP10QQmlEngineRK12QQmlPr'
        'operty',
        self._addressOf(engine), self._valueOf(source),
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

  @overload(QQmlNotifierEndpoint, QMetaProperty)
  @overload(NoneType, QMetaProperty)
  def doConnectNotify(
      self,
      endpoint: Optional[QQmlNotifierEndpoint],
      property: QMetaProperty,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlPropertyToPropertyBinding::doConnectNotify(QQmlNotifierEndpoint
    *endpoint, const QMetaProperty &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertytopropertybinding.html#doConnectNotify

    Parameters
    ----------

    endpoint : Optional[QQmlNotifierEndpoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.
    """
    #  void QQmlPropertyToPropertyBinding::doConnectNotify(
    #      QQmlNotifierEndpoint *endpoint, const QMetaProperty &property)
    self.uglySide.call(
        'ritual_ZN29QQmlPropertyToPropertyBinding15doConnectNotifyEP20QQmlN'
        'otifierEndpointRK13QMetaProperty',
        self._addressOf(endpoint, 'QQmlNotifierEndpoint'),
        self._valueOf(property),
    )

  @staticmethod
  def readSourceValue(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyToPropertyBinding::readSourceValue': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlPropertyToPropertyBinding.readSourceValue' has no cute "
        "function yet. Qt's "
        "'QQmlPropertyToPropertyBinding::readSourceValue': a template: a "
        "pattern and no single function.")
