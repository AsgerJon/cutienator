"""
QQmlIRLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirloader_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlIRLoader to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4, QmlIR

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlIRLoader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlIRLoader: a plain Python object standing in front
  of one C++ QQmlIRLoader.

  C++ hands a QQmlIRLoader around as a copy, so every C++ QQmlIRLoader behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlIRLoader that has a ritual and that Python can
  call so far, 2 names in all: 'load', 'loadObject'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlIRLoader::~QQmlIRLoader()': the destructor: Python removes its
    C++ QQmlIRLoader by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlIRLoader is created at the first use, not by
    'QQmlIRLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlIRLoader back gives a copy the ritual made for
    Python, in a new cute QQmlIRLoader.
  - Each name of Qt's QQmlIRLoader that has no cute function yet, 'New',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlIRLoader'

  #  Qt's '~QQmlIRLoader()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlIRLoader behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QQmlIRLoaderD1Ev'

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

  @overload(WAIT['QV4.CompiledData.Unit'], WAIT['QmlIR.Document'])
  @overload(WAIT['QV4.CompiledData.Unit'], NoneType)
  @overload(NoneType, WAIT['QmlIR.Document'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      unit: Optional[QV4.CompiledData.Unit],
      output: Optional[QmlIR.Document],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlIRLoader::QQmlIRLoader(const
    QV4::CompiledData::Unit *unit, QmlIR::Document *output)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlirloader.html#QQmlIRLoader

    Parameters
    ----------

    unit : Optional[QV4.CompiledData.Unit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    output : Optional[QmlIR.Document]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlIRLoader::QQmlIRLoader(const QV4::CompiledData::Unit *unit,
    #      QmlIR::Document *output)
    self._noteCreation(QQmlIRLoader, lambda: Rituals.call(
        'ritual_ZN12QQmlIRLoaderC1EPKN3QV412CompiledData4UnitEPN5QmlIR8Docu'
        'mentE',
        self._addressOf(unit), self._addressOf(output),
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

  def load(self) -> None:
    """
    Calls Qt's 'void QQmlIRLoader::load()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlirloader.html#load
    """
    #  void QQmlIRLoader::load()
    self.uglySide.call('ritual_ZN12QQmlIRLoader4loadEv')

  @overload(WAIT['QV4.CompiledData.Object'])
  @overload(NoneType)
  def loadObject(
      self,
      serializedObject: Optional[QV4.CompiledData.Object],
  ) -> Optional[QmlIR.Object]:
    """
    Calls Qt's 'QmlIR::Object *QQmlIRLoader::loadObject(const
    QV4::CompiledData::Object *serializedObject)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlirloader.html#loadObject

    Parameters
    ----------

    serializedObject : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QmlIR.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QmlIR::Object *QQmlIRLoader::loadObject(const
    #      QV4::CompiledData::Object *serializedObject)
    address = self.uglySide.call(
        'ritual_ZN12QQmlIRLoader10loadObjectEPKN3QV412CompiledData6ObjectE',
        self._addressOf(serializedObject),
    )
    return QmlIR.Object._cuteAt(address)

  @staticmethod
  def New(*__, **_) -> Never:
    """
    Qt's 'QQmlIRLoader::New': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlIRLoader.New' has no cute function yet. Qt's "
        "'QQmlIRLoader::New': a template: a pattern and no single function.")
