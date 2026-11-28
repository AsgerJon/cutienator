"""
The namespace 'QtTaskTree' of Qt, a package of 'cutienator.QtTaskTree':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtTaskTree import QtTaskTree
  QtTaskTree.Do

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

from .._qt_task_tree import QtTaskTree as _Enums

#  The enums of the namespace, and the names of their
#  members, as names of the package itself, where C++ has
#  them: 'Qt.AlignLeft'.
globals().update({
    name: value for name, value in _Enums.__dict__.items()
    if not name.startswith('_')})

__all__ = (
    'Do',
    'Else',
    'ElseIf',
    'ElseIfItem',
    'ElseItem',
    'For',
    'GroupItem',
    'If',
    'Iterator',
    'QParallelTaskTreeRunner',
    'QSequentialTaskTreeRunner',
    'QSingleTaskTreeRunner',
    'QTaskTreeTaskAdapter',
    'QTimeoutTaskAdapter',
    'StorageBase',
    'Then',
    'ThenItem',
    'When',
    'ExecutionMode',
    'ForeverIterator',
    'RepeatIterator',
    'UntilIterator',
    'ParallelLimit',
    'ExecutableItem',
    'Forever',
    'Group',
    'QSyncTask',
    'QBarrier',
    'QTaskInterface',
    'QTaskTree',
    'QProcessTaskAdapter',
    'QProcessTaskDeleter',
    'QStartedBarrier',
    'QTcpSocketWrapper',
    'QThreadFunctionBase',
    'QNetworkReplyWrapper',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt_task_tree__do import Do
  from .._qt_task_tree__else import Else
  from .._qt_task_tree__else_if import ElseIf
  from .._qt_task_tree__else_if_item import ElseIfItem
  from .._qt_task_tree__else_item import ElseItem
  from .._qt_task_tree__for import For
  from .._qt_task_tree__group_item import GroupItem
  from .._qt_task_tree__if import If
  from .._qt_task_tree__iterator import Iterator
  from .._qt_task_tree__q_parallel_task_tree_runner import QParallelTaskTreeRunner
  from .._qt_task_tree__q_sequential_task_tree_runner import QSequentialTaskTreeRunner
  from .._qt_task_tree__q_single_task_tree_runner import QSingleTaskTreeRunner
  from .._qt_task_tree__q_task_tree_task_adapter import QTaskTreeTaskAdapter
  from .._qt_task_tree__q_timeout_task_adapter import QTimeoutTaskAdapter
  from .._qt_task_tree__storage_base import StorageBase
  from .._qt_task_tree__then import Then
  from .._qt_task_tree__then_item import ThenItem
  from .._qt_task_tree__when import When
  from .._qt_task_tree__execution_mode import ExecutionMode
  from .._qt_task_tree__forever_iterator import ForeverIterator
  from .._qt_task_tree__repeat_iterator import RepeatIterator
  from .._qt_task_tree__until_iterator import UntilIterator
  from .._qt_task_tree__parallel_limit import ParallelLimit
  from .._qt_task_tree__executable_item import ExecutableItem
  from .._qt_task_tree__forever import Forever
  from .._qt_task_tree__group import Group
  from .._qt_task_tree__q_sync_task import QSyncTask
  from .._qt_task_tree__q_barrier import QBarrier
  from .._qt_task_tree__q_task_interface import QTaskInterface
  from .._qt_task_tree__q_task_tree import QTaskTree
  from .._qt_task_tree__q_process_task_adapter import QProcessTaskAdapter
  from .._qt_task_tree__q_process_task_deleter import QProcessTaskDeleter
  from .._qt_task_tree__q_started_barrier import QStartedBarrier
  from .._qt_task_tree__q_tcp_socket_wrapper import QTcpSocketWrapper
  from .._qt_task_tree__q_thread_function_base import QThreadFunctionBase
  from .._qt_task_tree__q_network_reply_wrapper import QNetworkReplyWrapper
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'Do': '_qt_task_tree__do',
      'Else': '_qt_task_tree__else',
      'ElseIf': '_qt_task_tree__else_if',
      'ElseIfItem': '_qt_task_tree__else_if_item',
      'ElseItem': '_qt_task_tree__else_item',
      'For': '_qt_task_tree__for',
      'GroupItem': '_qt_task_tree__group_item',
      'If': '_qt_task_tree__if',
      'Iterator': '_qt_task_tree__iterator',
      'QParallelTaskTreeRunner': '_qt_task_tree__q_parallel_task_tree_runner',
      'QSequentialTaskTreeRunner': '_qt_task_tree__q_sequential_task_tree_runner',
      'QSingleTaskTreeRunner': '_qt_task_tree__q_single_task_tree_runner',
      'QTaskTreeTaskAdapter': '_qt_task_tree__q_task_tree_task_adapter',
      'QTimeoutTaskAdapter': '_qt_task_tree__q_timeout_task_adapter',
      'StorageBase': '_qt_task_tree__storage_base',
      'Then': '_qt_task_tree__then',
      'ThenItem': '_qt_task_tree__then_item',
      'When': '_qt_task_tree__when',
      'ExecutionMode': '_qt_task_tree__execution_mode',
      'ForeverIterator': '_qt_task_tree__forever_iterator',
      'RepeatIterator': '_qt_task_tree__repeat_iterator',
      'UntilIterator': '_qt_task_tree__until_iterator',
      'ParallelLimit': '_qt_task_tree__parallel_limit',
      'ExecutableItem': '_qt_task_tree__executable_item',
      'Forever': '_qt_task_tree__forever',
      'Group': '_qt_task_tree__group',
      'QSyncTask': '_qt_task_tree__q_sync_task',
      'QBarrier': '_qt_task_tree__q_barrier',
      'QTaskInterface': '_qt_task_tree__q_task_interface',
      'QTaskTree': '_qt_task_tree__q_task_tree',
      'QProcessTaskAdapter': '_qt_task_tree__q_process_task_adapter',
      'QProcessTaskDeleter': '_qt_task_tree__q_process_task_deleter',
      'QStartedBarrier': '_qt_task_tree__q_started_barrier',
      'QTcpSocketWrapper': '_qt_task_tree__q_tcp_socket_wrapper',
      'QThreadFunctionBase': '_qt_task_tree__q_thread_function_base',
      'QNetworkReplyWrapper': '_qt_task_tree__q_network_reply_wrapper',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QtTaskTree.Do'. Python calls this for a name the
    package does not hold yet, and what it gives is kept here for the next
    time.

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
