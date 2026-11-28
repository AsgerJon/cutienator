"""
The namespace 'QQmlPrivate' of Qt, a package of 'cutienator.QtQml':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtQml import QQmlPrivate
  QQmlPrivate.AOTCompiledFunction

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._q_qml_private import QQmlPrivate as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'AOTCompiledFunction',
    'CachedQmlUnit',
    'RegisterAutoParent',
    'RegisterCompositeSingletonType',
    'RegisterCompositeType',
    'RegisterInterface',
    'RegisterQmlUnitCacheHook',
    'RegisterSequentialContainer',
    'RegisterSequentialContainerAndRevisions',
    'RegisterSingletonType',
    'RegisterSingletonTypeAndRevisions',
    'RegisterType',
    'RegisterTypeAndRevisions',
    'AOTTrackedLocalsStorage',
    'AOTCompiledContext',
    'SingletonFunctor',
    'SingletonInstanceFunctor',
    'AOTLookupValidation',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_qml_private__a_o_t_compiled_function import AOTCompiledFunction
  from .._q_qml_private__cached_qml_unit import CachedQmlUnit
  from .._q_qml_private__register_auto_parent import RegisterAutoParent
  from .._q_qml_private__register_composite_singleton_type import RegisterCompositeSingletonType
  from .._q_qml_private__register_composite_type import RegisterCompositeType
  from .._q_qml_private__register_interface import RegisterInterface
  from .._q_qml_private__register_qml_unit_cache_hook import RegisterQmlUnitCacheHook
  from .._q_qml_private__register_sequential_container import RegisterSequentialContainer
  from .._q_qml_private__register_sequential_container_and_revisions import RegisterSequentialContainerAndRevisions
  from .._q_qml_private__register_singleton_type import RegisterSingletonType
  from .._q_qml_private__register_singleton_type_and_revisions import RegisterSingletonTypeAndRevisions
  from .._q_qml_private__register_type import RegisterType
  from .._q_qml_private__register_type_and_revisions import RegisterTypeAndRevisions
  from .._q_qml_private__a_o_t_tracked_locals_storage import AOTTrackedLocalsStorage
  from .._q_qml_private__a_o_t_compiled_context import AOTCompiledContext
  from .._q_qml_private__singleton_functor import SingletonFunctor
  from .._q_qml_private__singleton_instance_functor import SingletonInstanceFunctor
  from . import AOTLookupValidation
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'AOTCompiledFunction': '_q_qml_private__a_o_t_compiled_function',
      'CachedQmlUnit': '_q_qml_private__cached_qml_unit',
      'RegisterAutoParent': '_q_qml_private__register_auto_parent',
      'RegisterCompositeSingletonType': '_q_qml_private__register_composite_singleton_type',
      'RegisterCompositeType': '_q_qml_private__register_composite_type',
      'RegisterInterface': '_q_qml_private__register_interface',
      'RegisterQmlUnitCacheHook': '_q_qml_private__register_qml_unit_cache_hook',
      'RegisterSequentialContainer': '_q_qml_private__register_sequential_container',
      'RegisterSequentialContainerAndRevisions': '_q_qml_private__register_sequential_container_and_revisions',
      'RegisterSingletonType': '_q_qml_private__register_singleton_type',
      'RegisterSingletonTypeAndRevisions': '_q_qml_private__register_singleton_type_and_revisions',
      'RegisterType': '_q_qml_private__register_type',
      'RegisterTypeAndRevisions': '_q_qml_private__register_type_and_revisions',
      'AOTTrackedLocalsStorage': '_q_qml_private__a_o_t_tracked_locals_storage',
      'AOTCompiledContext': '_q_qml_private__a_o_t_compiled_context',
      'SingletonFunctor': '_q_qml_private__singleton_functor',
      'SingletonInstanceFunctor': '_q_qml_private__singleton_instance_functor',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('AOTLookupValidation',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QQmlPrivate.AOTCompiledFunction'. Python calls this for
    a name the package does not hold yet, and what it gives is kept here for
    the next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__, *(
        name for name in _Enums.__dict__ if not name.startswith('_'))]
