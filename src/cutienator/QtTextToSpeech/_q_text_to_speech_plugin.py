"""
QTextToSpeechPlugin binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTextToSpeech/qtexttospeechplugin.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QString, QVariant
  from . import QTextToSpeechEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QString = WAIT['QString']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextToSpeechPlugin(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextToSpeechPlugin: a plain Python object standing
  in front of one C++ QTextToSpeechPlugin.

  C++ hands a QTextToSpeechPlugin around as a copy, so every C++
  QTextToSpeechPlugin behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextToSpeechPlugin that has a ritual and that
  Python can call so far, 1 name in all: 'createTextToSpeechEngine'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextToSpeechPlugin::~QTextToSpeechPlugin()': the destructor:
    Python removes its C++ QTextToSpeechPlugin by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QTextToSpeechPlugin is created at the first use, not by
    'QTextToSpeechPlugin(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextToSpeechPlugin back gives a copy the ritual made
    for Python, in a new cute QTextToSpeechPlugin.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextToSpeechPlugin'

  #  The functions Qt calls itself that QTextToSpeechPlugin is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createTextToSpeechEngine': (
          'QTextToSpeechEngine '
          '*QTextToSpeechPlugin::createTextToSpeechEngine(const '
          'QVariantMap &, QObject *, QString *) const',
      ),
  }

  #  Qt's '~QTextToSpeechPlugin()'. Naming it makes this a value class:
  #  Python owns every C++ QTextToSpeechPlugin behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QTextToSpeechPluginD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMap[str, QVariant], QObject, QString)
  @overload(QMap[str, QVariant], QObject, NoneType)
  @overload(QMap[str, QVariant], NoneType, QString)
  @overload(QMap[str, QVariant], NoneType, NoneType)
  def createTextToSpeechEngine(
      self,
      parameters: QMap[str, QVariant],
      parent: Optional[QObject],
      errorString: Optional[QString],
  ) -> Optional[QTextToSpeechEngine]:
    """
    Calls Qt's 'QTextToSpeechEngine
    *QTextToSpeechPlugin::createTextToSpeechEngine(const QVariantMap
    &parameters, QObject *parent, QString *errorString) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechplugin.html#createTextToSpeechEngine

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorString : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTextToSpeechEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextToSpeechEngine
    #      *QTextToSpeechPlugin::createTextToSpeechEngine(const QVariantMap
    #      &parameters, QObject *parent, QString *errorString) const
    address = self.uglySide.call(
        'ritual_ZNK19QTextToSpeechPlugin24createTextToSpeechEngineERK4QMapI'
        '7QString8QVariantEP7QObjectPS1_',
        self._valueOf(parameters), self._addressOf(parent, 'QObject'),
        self._addressOf(errorString),
    )
    from . import QTextToSpeechEngine
    return QTextToSpeechEngine._cuteAt(address)

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
