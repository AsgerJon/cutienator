"""
QQuick3DPropertyChangedTracker binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DPropertyChangedTracker to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaProperty
  from . import QQuick3DObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaProperty = WAIT['QMetaProperty']
  QQuick3DObject = WAIT['QQuick3DObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DPropertyChangedTracker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DPropertyChangedTracker: a plain Python object
  standing in front of one C++ QQuick3DPropertyChangedTracker.

  What exists
  -----------

  Every function of Qt's QQuick3DPropertyChangedTracker that has a ritual and
  that Python can call so far, 2 names in all: 'addPropertyWatcher',
  'markTrackedPropertyDirty'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuick3DPropertyChangedTracker::~QQuick3DPropertyChangedTracker()':
    the destructor: Python never removes a C++
    QQuick3DPropertyChangedTracker.
  - Qt's 'QList<UniformProperty>
    QQuick3DPropertyChangedTracker::extractProperties()': gives a type Python
    has no way to take yet.
  - Qt's 'std::optional<UniformProperty>
    QQuick3DPropertyChangedTracker::createOrUpdateTrackedProperty(const
    QMetaProperty property, bool addWatchers)': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQuick3DPropertyChangedTracker is created at the first use, not
    by 'QQuick3DPropertyChangedTracker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DPropertyChangedTracker.
  - Each name of Qt's QQuick3DPropertyChangedTracker that has no cute
    function yet, '__init__', 'createOrUpdateTrackedProperty',
    'extractProperties', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DPropertyChangedTracker, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class DirtyPropertyHint(CuteNum, scoped=True):
    """
    The enum 'QQuick3DPropertyChangedTracker::DirtyPropertyHint' of Qt, with
    the 2 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Value = Kee[int](0)
    Reference = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DPropertyChangedTracker'

  #  A C++ QQuick3DPropertyChangedTracker Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DPropertyChangedTracker'

  #  The functions Qt calls itself that QQuick3DPropertyChangedTracker is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'markTrackedPropertyDirty': (
          ('_ZN30QQuick3DPropertyChangedTracker24markTrackedPropertyDirtyE1'
           '3QMetaPropertyNS_17DirtyPropertyHintE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMetaProperty'),
               ('int', 'enum',
                'QtQuick3D:QQuick3DPropertyChangedTracker.DirtyPropertyHint'),
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
    Qt's 'QQuick3DPropertyChangedTracker::QQuick3DPropertyChangedTracker': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQuick3DPropertyChangedTracker.__init__' has no cute function "
        "yet. Qt's "
        "'QQuick3DPropertyChangedTracker::QQuick3DPropertyChangedTracker': "
        "a template: a pattern and no single function.")

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

  @overload(QMetaProperty, DirtyPropertyHint)
  @overload(QMetaProperty, DirtyPropertyHint, QQuick3DObject)
  @overload(QMetaProperty, DirtyPropertyHint, NoneType)
  def addPropertyWatcher(
      self,
      property: QMetaProperty,
      hint: DirtyPropertyHint,
      object: Optional[QQuick3DObject] = None,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPropertyChangedTracker::addPropertyWatcher(QMetaProperty
    property, DirtyPropertyHint hint, QQuick3DObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpropertychangedtracker.html

    Parameters
    ----------

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    hint : DirtyPropertyHint
      Passed on as its number.

    object : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuick3DPropertyChangedTracker::addPropertyWatcher(QMetaProperty
    #      property, DirtyPropertyHint hint, QQuick3DObject *object)
    self._callAs(
        'QQuick3DPropertyChangedTracker',
        'ritual_ZN30QQuick3DPropertyChangedTracker18addPropertyWatcherE13QM'
        'etaPropertyNS_17DirtyPropertyHintEP14QQuick3DObject',
        self._valueOf(property), hint.value, self._addressOf(object),
    )

  @overload(QMetaProperty, DirtyPropertyHint)
  def markTrackedPropertyDirty(
      self,
      property: QMetaProperty,
      hint: DirtyPropertyHint,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DPropertyChangedTracker::markTrackedPropertyDirty(QMetaProperty
    property, DirtyPropertyHint hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dpropertychangedtracker.html

    Parameters
    ----------

    property : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    hint : DirtyPropertyHint
      Passed on as its number.
    """
    #  void QQuick3DPropertyChangedTracker::markTrackedPropertyDirty(
    #      QMetaProperty property, DirtyPropertyHint hint)
    self._callAs(
        'QQuick3DPropertyChangedTracker',
        'ritual_ZN30QQuick3DPropertyChangedTracker24markTrackedPropertyDirt'
        'yE13QMetaPropertyNS_17DirtyPropertyHintE',
        self._valueOf(property), hint.value,
    )

  @staticmethod
  def createOrUpdateTrackedProperty(*__, **_) -> Never:
    """
    Qt's 'std::optional<UniformProperty>
    QQuick3DPropertyChangedTracker::createOrUpdateTrackedProperty(const
    QMetaProperty property, bool addWatchers)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DPropertyChangedTracker.createOrUpdateTrackedProperty' has "
        "no cute function yet. Qt's 'std::optional<UniformProperty> "
        "QQuick3DPropertyChangedTracker::createOrUpdateTrackedProperty(const"
        " QMetaProperty property, bool addWatchers)': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def extractProperties(*__, **_) -> Never:
    """
    Qt's 'QList<UniformProperty>
    QQuick3DPropertyChangedTracker::extractProperties()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DPropertyChangedTracker.extractProperties' has no cute "
        "function yet. Qt's 'QList<UniformProperty> "
        "QQuick3DPropertyChangedTracker::extractProperties()': gives a type "
        "Python has no way to take yet.")
