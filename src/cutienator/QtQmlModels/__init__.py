"""
The 'cutienator.QtQmlModels' package provides the cute classes of the
part of Qt named QtQmlModels, under the name PySide6 has for it.

  from cutienator.QtQmlModels import QQmlListCompositor, ListLayout

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QQmlListCompositor',
    'ListLayout',
    'QAbstractItemModelForeign',
    'QAbstractListModelForeign',
    'QItemSelectionForeign',
    'QItemSelectionModelForeign',
    'QModelIndexListForeign',
    'QModelIndexStdVectorForeign',
    'QQmlChangeSet',
    'QQmlFilterBasePrivate',
    'QQmlListAccessor',
    'QQmlListElement',
    'QQmlModelIndexValueType',
    'QQmlObjectModelAttached',
    'QQmlPersistentModelIndexValueType',
    'QQmlSorterBasePrivate',
    'QQmlTreeModelToTableModel',
    'QQuickPackage',
    'QQuickPackageAttached',
    'QRowsRemoval',
    'QSortFilterProxyModelDataChanged',
    'QQmlDelegateModelGroupEmitter',
    'QQmlFilterCompositorPrivate',
    'QQmlFunctionFilterPrivate',
    'QQmlInstanceModel',
    'QQmlItemSelectionRangeValueType',
    'QQmlRoleFilterPrivate',
    'QQmlRoleSorterPrivate',
    'QQmlCompositeFilterBasePrivate',
    'QQmlFunctionSorterPrivate',
    'QQmlObjectModel',
    'QQmlRangeFilterPrivate',
    'QQmlRegExpFilterPrivate',
    'QQmlStringSorterPrivate',
    'QQmlValueFilterPrivate',
    'QQmlAllOfFilterPrivate',
    'QQmlAnyOfFilterPrivate',
    'QQmlSortFilterProxyModel',
    'QQmlSorterBase',
    'QQmlFilterBase',
    'QQmlFunctionSorter',
    'QQmlRoleSorter',
    'QQmlSorterCompositor',
    'QQmlSorterCompositorPrivate',
    'QSortFilterProxyModelHelper',
    'QQmlFilterCompositor',
    'QQmlFunctionFilter',
    'QQmlRoleFilter',
    'QQmlSortFilterProxyModelGreaterThan',
    'QQmlSortFilterProxyModelLessThan',
    'QQmlSortFilterProxyModelPrivate',
    'QQmlStringSorter',
    'DynamicRoleModelNodeMetaObject',
    'QQmlCompositeFilterBase',
    'QQmlDelegateModelPartsMetaObject',
    'QQmlRangeFilter',
    'QQmlRegExpFilter',
    'QQmlValueFilter',
    'QQmlAllOfFilter',
    'QQmlAnyOfFilter',
    'ListModel',
    'QQmlListModel',
    'QQmlListModelWorkerAgent',
    'QQmlAdaptorModelEngineData',
    'QQmlDelegateChoice',
    'QQmlDelegateModel',
    'QQmlDelegateModelItemObject',
    'ListElement',
    'ModelNodeMetaObject',
    'QQmlDelegateModelGroup',
    'QQmlDelegateModelParts',
    'QQmlDelegateModelPointer',
    'QQmlInstantiator',
    'QQmlListModelParser',
    'QQmlPartsModel',
    'StringOrTranslation',
    'QQmlDelegateModelItem',
    'QQmlAdaptorModel',
    'QQmlTableInstanceModel',
    'QQmlDelegateModelItemMetaType',
    'QQDMIncubationTask',
    'QQmlDelegateModelPrivate',
    'QQmlTableInstanceModelIncubationTask',
    'QQmlDelegateModelGroupPrivate',
    'QQmlInstantiatorPrivate',
    'QQmlAbstractDelegateComponent',
    'QQmlDMAbstractItemModelData',
    'VDMAbstractItemModelDataType',
    'QQmlDMListAccessorData',
    'VDMListDelegateDataType',
    'QQmlDelegateModelAttached',
    'QQmlDelegateModelAttachedMetaObject',
    'QQmlReusableDelegateModelItemsPool',
    'VDMObjectDelegateDataType',
    'QQmlDMObjectData',
    'QQmlDelegateChooser',
    'QQmlDMObjectDataMetaObject',
    'QV4',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_qml_list_compositor import QQmlListCompositor
  from ._list_layout import ListLayout
  from ._q_abstract_item_model_foreign import QAbstractItemModelForeign
  from ._q_abstract_list_model_foreign import QAbstractListModelForeign
  from ._q_item_selection_foreign import QItemSelectionForeign
  from ._q_item_selection_model_foreign import QItemSelectionModelForeign
  from ._q_model_index_list_foreign import QModelIndexListForeign
  from ._q_model_index_std_vector_foreign import QModelIndexStdVectorForeign
  from ._q_qml_change_set import QQmlChangeSet
  from ._q_qml_filter_base_private import QQmlFilterBasePrivate
  from ._q_qml_list_accessor import QQmlListAccessor
  from ._q_qml_list_element import QQmlListElement
  from ._q_qml_model_index_value_type import QQmlModelIndexValueType
  from ._q_qml_object_model_attached import QQmlObjectModelAttached
  from ._q_qml_persistent_model_index_value_type import QQmlPersistentModelIndexValueType
  from ._q_qml_sorter_base_private import QQmlSorterBasePrivate
  from ._q_qml_tree_model_to_table_model import QQmlTreeModelToTableModel
  from ._q_quick_package import QQuickPackage
  from ._q_quick_package_attached import QQuickPackageAttached
  from ._q_rows_removal import QRowsRemoval
  from ._q_sort_filter_proxy_model_data_changed import QSortFilterProxyModelDataChanged
  from ._q_qml_delegate_model_group_emitter import QQmlDelegateModelGroupEmitter
  from ._q_qml_filter_compositor_private import QQmlFilterCompositorPrivate
  from ._q_qml_function_filter_private import QQmlFunctionFilterPrivate
  from ._q_qml_instance_model import QQmlInstanceModel
  from ._q_qml_item_selection_range_value_type import QQmlItemSelectionRangeValueType
  from ._q_qml_role_filter_private import QQmlRoleFilterPrivate
  from ._q_qml_role_sorter_private import QQmlRoleSorterPrivate
  from ._q_qml_composite_filter_base_private import QQmlCompositeFilterBasePrivate
  from ._q_qml_function_sorter_private import QQmlFunctionSorterPrivate
  from ._q_qml_object_model import QQmlObjectModel
  from ._q_qml_range_filter_private import QQmlRangeFilterPrivate
  from ._q_qml_reg_exp_filter_private import QQmlRegExpFilterPrivate
  from ._q_qml_string_sorter_private import QQmlStringSorterPrivate
  from ._q_qml_value_filter_private import QQmlValueFilterPrivate
  from ._q_qml_all_of_filter_private import QQmlAllOfFilterPrivate
  from ._q_qml_any_of_filter_private import QQmlAnyOfFilterPrivate
  from ._q_qml_sort_filter_proxy_model import QQmlSortFilterProxyModel
  from ._q_qml_sorter_base import QQmlSorterBase
  from ._q_qml_filter_base import QQmlFilterBase
  from ._q_qml_function_sorter import QQmlFunctionSorter
  from ._q_qml_role_sorter import QQmlRoleSorter
  from ._q_qml_sorter_compositor import QQmlSorterCompositor
  from ._q_qml_sorter_compositor_private import QQmlSorterCompositorPrivate
  from ._q_sort_filter_proxy_model_helper import QSortFilterProxyModelHelper
  from ._q_qml_filter_compositor import QQmlFilterCompositor
  from ._q_qml_function_filter import QQmlFunctionFilter
  from ._q_qml_role_filter import QQmlRoleFilter
  from ._q_qml_sort_filter_proxy_model_greater_than import QQmlSortFilterProxyModelGreaterThan
  from ._q_qml_sort_filter_proxy_model_less_than import QQmlSortFilterProxyModelLessThan
  from ._q_qml_sort_filter_proxy_model_private import QQmlSortFilterProxyModelPrivate
  from ._q_qml_string_sorter import QQmlStringSorter
  from ._dynamic_role_model_node_meta_object import DynamicRoleModelNodeMetaObject
  from ._q_qml_composite_filter_base import QQmlCompositeFilterBase
  from ._q_qml_delegate_model_parts_meta_object import QQmlDelegateModelPartsMetaObject
  from ._q_qml_range_filter import QQmlRangeFilter
  from ._q_qml_reg_exp_filter import QQmlRegExpFilter
  from ._q_qml_value_filter import QQmlValueFilter
  from ._q_qml_all_of_filter import QQmlAllOfFilter
  from ._q_qml_any_of_filter import QQmlAnyOfFilter
  from ._list_model import ListModel
  from ._q_qml_list_model import QQmlListModel
  from ._q_qml_list_model_worker_agent import QQmlListModelWorkerAgent
  from ._q_qml_adaptor_model_engine_data import QQmlAdaptorModelEngineData
  from ._q_qml_delegate_choice import QQmlDelegateChoice
  from ._q_qml_delegate_model import QQmlDelegateModel
  from ._q_qml_delegate_model_item_object import QQmlDelegateModelItemObject
  from ._list_element import ListElement
  from ._model_node_meta_object import ModelNodeMetaObject
  from ._q_qml_delegate_model_group import QQmlDelegateModelGroup
  from ._q_qml_delegate_model_parts import QQmlDelegateModelParts
  from ._q_qml_delegate_model_pointer import QQmlDelegateModelPointer
  from ._q_qml_instantiator import QQmlInstantiator
  from ._q_qml_list_model_parser import QQmlListModelParser
  from ._q_qml_parts_model import QQmlPartsModel
  from ._string_or_translation import StringOrTranslation
  from ._q_qml_delegate_model_item import QQmlDelegateModelItem
  from ._q_qml_adaptor_model import QQmlAdaptorModel
  from ._q_qml_table_instance_model import QQmlTableInstanceModel
  from ._q_qml_delegate_model_item_meta_type import QQmlDelegateModelItemMetaType
  from ._q_q_d_m_incubation_task import QQDMIncubationTask
  from ._q_qml_delegate_model_private import QQmlDelegateModelPrivate
  from ._q_qml_table_instance_model_incubation_task import QQmlTableInstanceModelIncubationTask
  from ._q_qml_delegate_model_group_private import QQmlDelegateModelGroupPrivate
  from ._q_qml_instantiator_private import QQmlInstantiatorPrivate
  from ._q_qml_abstract_delegate_component import QQmlAbstractDelegateComponent
  from ._q_qml_d_m_abstract_item_model_data import QQmlDMAbstractItemModelData
  from ._v_d_m_abstract_item_model_data_type import VDMAbstractItemModelDataType
  from ._q_qml_d_m_list_accessor_data import QQmlDMListAccessorData
  from ._v_d_m_list_delegate_data_type import VDMListDelegateDataType
  from ._q_qml_delegate_model_attached import QQmlDelegateModelAttached
  from ._q_qml_delegate_model_attached_meta_object import QQmlDelegateModelAttachedMetaObject
  from ._q_qml_reusable_delegate_model_items_pool import QQmlReusableDelegateModelItemsPool
  from ._v_d_m_object_delegate_data_type import VDMObjectDelegateDataType
  from ._q_qml_d_m_object_data import QQmlDMObjectData
  from ._q_qml_delegate_chooser import QQmlDelegateChooser
  from ._q_qml_d_m_object_data_meta_object import QQmlDMObjectDataMetaObject
  from . import QV4
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQmlListCompositor': '_q_qml_list_compositor',
      'ListLayout': '_list_layout',
      'QAbstractItemModelForeign': '_q_abstract_item_model_foreign',
      'QAbstractListModelForeign': '_q_abstract_list_model_foreign',
      'QItemSelectionForeign': '_q_item_selection_foreign',
      'QItemSelectionModelForeign': '_q_item_selection_model_foreign',
      'QModelIndexListForeign': '_q_model_index_list_foreign',
      'QModelIndexStdVectorForeign': '_q_model_index_std_vector_foreign',
      'QQmlChangeSet': '_q_qml_change_set',
      'QQmlFilterBasePrivate': '_q_qml_filter_base_private',
      'QQmlListAccessor': '_q_qml_list_accessor',
      'QQmlListElement': '_q_qml_list_element',
      'QQmlModelIndexValueType': '_q_qml_model_index_value_type',
      'QQmlObjectModelAttached': '_q_qml_object_model_attached',
      'QQmlPersistentModelIndexValueType': '_q_qml_persistent_model_index_value_type',
      'QQmlSorterBasePrivate': '_q_qml_sorter_base_private',
      'QQmlTreeModelToTableModel': '_q_qml_tree_model_to_table_model',
      'QQuickPackage': '_q_quick_package',
      'QQuickPackageAttached': '_q_quick_package_attached',
      'QRowsRemoval': '_q_rows_removal',
      'QSortFilterProxyModelDataChanged': '_q_sort_filter_proxy_model_data_changed',
      'QQmlDelegateModelGroupEmitter': '_q_qml_delegate_model_group_emitter',
      'QQmlFilterCompositorPrivate': '_q_qml_filter_compositor_private',
      'QQmlFunctionFilterPrivate': '_q_qml_function_filter_private',
      'QQmlInstanceModel': '_q_qml_instance_model',
      'QQmlItemSelectionRangeValueType': '_q_qml_item_selection_range_value_type',
      'QQmlRoleFilterPrivate': '_q_qml_role_filter_private',
      'QQmlRoleSorterPrivate': '_q_qml_role_sorter_private',
      'QQmlCompositeFilterBasePrivate': '_q_qml_composite_filter_base_private',
      'QQmlFunctionSorterPrivate': '_q_qml_function_sorter_private',
      'QQmlObjectModel': '_q_qml_object_model',
      'QQmlRangeFilterPrivate': '_q_qml_range_filter_private',
      'QQmlRegExpFilterPrivate': '_q_qml_reg_exp_filter_private',
      'QQmlStringSorterPrivate': '_q_qml_string_sorter_private',
      'QQmlValueFilterPrivate': '_q_qml_value_filter_private',
      'QQmlAllOfFilterPrivate': '_q_qml_all_of_filter_private',
      'QQmlAnyOfFilterPrivate': '_q_qml_any_of_filter_private',
      'QQmlSortFilterProxyModel': '_q_qml_sort_filter_proxy_model',
      'QQmlSorterBase': '_q_qml_sorter_base',
      'QQmlFilterBase': '_q_qml_filter_base',
      'QQmlFunctionSorter': '_q_qml_function_sorter',
      'QQmlRoleSorter': '_q_qml_role_sorter',
      'QQmlSorterCompositor': '_q_qml_sorter_compositor',
      'QQmlSorterCompositorPrivate': '_q_qml_sorter_compositor_private',
      'QSortFilterProxyModelHelper': '_q_sort_filter_proxy_model_helper',
      'QQmlFilterCompositor': '_q_qml_filter_compositor',
      'QQmlFunctionFilter': '_q_qml_function_filter',
      'QQmlRoleFilter': '_q_qml_role_filter',
      'QQmlSortFilterProxyModelGreaterThan': '_q_qml_sort_filter_proxy_model_greater_than',
      'QQmlSortFilterProxyModelLessThan': '_q_qml_sort_filter_proxy_model_less_than',
      'QQmlSortFilterProxyModelPrivate': '_q_qml_sort_filter_proxy_model_private',
      'QQmlStringSorter': '_q_qml_string_sorter',
      'DynamicRoleModelNodeMetaObject': '_dynamic_role_model_node_meta_object',
      'QQmlCompositeFilterBase': '_q_qml_composite_filter_base',
      'QQmlDelegateModelPartsMetaObject': '_q_qml_delegate_model_parts_meta_object',
      'QQmlRangeFilter': '_q_qml_range_filter',
      'QQmlRegExpFilter': '_q_qml_reg_exp_filter',
      'QQmlValueFilter': '_q_qml_value_filter',
      'QQmlAllOfFilter': '_q_qml_all_of_filter',
      'QQmlAnyOfFilter': '_q_qml_any_of_filter',
      'ListModel': '_list_model',
      'QQmlListModel': '_q_qml_list_model',
      'QQmlListModelWorkerAgent': '_q_qml_list_model_worker_agent',
      'QQmlAdaptorModelEngineData': '_q_qml_adaptor_model_engine_data',
      'QQmlDelegateChoice': '_q_qml_delegate_choice',
      'QQmlDelegateModel': '_q_qml_delegate_model',
      'QQmlDelegateModelItemObject': '_q_qml_delegate_model_item_object',
      'ListElement': '_list_element',
      'ModelNodeMetaObject': '_model_node_meta_object',
      'QQmlDelegateModelGroup': '_q_qml_delegate_model_group',
      'QQmlDelegateModelParts': '_q_qml_delegate_model_parts',
      'QQmlDelegateModelPointer': '_q_qml_delegate_model_pointer',
      'QQmlInstantiator': '_q_qml_instantiator',
      'QQmlListModelParser': '_q_qml_list_model_parser',
      'QQmlPartsModel': '_q_qml_parts_model',
      'StringOrTranslation': '_string_or_translation',
      'QQmlDelegateModelItem': '_q_qml_delegate_model_item',
      'QQmlAdaptorModel': '_q_qml_adaptor_model',
      'QQmlTableInstanceModel': '_q_qml_table_instance_model',
      'QQmlDelegateModelItemMetaType': '_q_qml_delegate_model_item_meta_type',
      'QQDMIncubationTask': '_q_q_d_m_incubation_task',
      'QQmlDelegateModelPrivate': '_q_qml_delegate_model_private',
      'QQmlTableInstanceModelIncubationTask': '_q_qml_table_instance_model_incubation_task',
      'QQmlDelegateModelGroupPrivate': '_q_qml_delegate_model_group_private',
      'QQmlInstantiatorPrivate': '_q_qml_instantiator_private',
      'QQmlAbstractDelegateComponent': '_q_qml_abstract_delegate_component',
      'QQmlDMAbstractItemModelData': '_q_qml_d_m_abstract_item_model_data',
      'VDMAbstractItemModelDataType': '_v_d_m_abstract_item_model_data_type',
      'QQmlDMListAccessorData': '_q_qml_d_m_list_accessor_data',
      'VDMListDelegateDataType': '_v_d_m_list_delegate_data_type',
      'QQmlDelegateModelAttached': '_q_qml_delegate_model_attached',
      'QQmlDelegateModelAttachedMetaObject': '_q_qml_delegate_model_attached_meta_object',
      'QQmlReusableDelegateModelItemsPool': '_q_qml_reusable_delegate_model_items_pool',
      'VDMObjectDelegateDataType': '_v_d_m_object_delegate_data_type',
      'QQmlDMObjectData': '_q_qml_d_m_object_data',
      'QQmlDelegateChooser': '_q_qml_delegate_chooser',
      'QQmlDMObjectDataMetaObject': '_q_qml_d_m_object_data_meta_object',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QV4',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtQmlModels import QQmlDMObjectDataMetaObject'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
      globals()[name] = value
      return value
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]
