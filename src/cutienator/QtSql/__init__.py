"""
The 'cutienator.QtSql' package provides the cute classes of the part of
Qt named QtSql, under the name PySide6 has for it.

  from cutienator.QtSql import QSqlDatabaseDefaultConnectionName, QSqlDriverCreatorBase

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
    'QSqlDatabaseDefaultConnectionName',
    'QSqlDriverCreatorBase',
    'QHolder',
    'QSqlError',
    'QSqlQueryModelSql',
    'QSqlRelation',
    'QSqlDriverPlugin',
    'QSqlField',
    'QSqlQueryModelPrivate',
    'QSqlRecord',
    'QSqlDriver',
    'QSqlDriverPrivate',
    'QSqlIndex',
    'QSqlTableModelPrivate',
    'QSqlDatabase',
    'QSqlNullDriver',
    'QSqlResult',
    'QSqlResultPrivate',
    'QSqlCachedResultPrivate',
    'QSqlNullResult',
    'QSqlQuery',
    'QSqlCachedResult',
    'QSqlQueryModel',
    'QSqlTableModel',
    'QSqlRelationalTableModel',
    'QSql',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_sql_database_default_connection_name import QSqlDatabaseDefaultConnectionName
  from ._q_sql_driver_creator_base import QSqlDriverCreatorBase
  from ._q_holder import QHolder
  from ._q_sql_error import QSqlError
  from ._q_sql_query_model_sql import QSqlQueryModelSql
  from ._q_sql_relation import QSqlRelation
  from ._q_sql_driver_plugin import QSqlDriverPlugin
  from ._q_sql_field import QSqlField
  from ._q_sql_query_model_private import QSqlQueryModelPrivate
  from ._q_sql_record import QSqlRecord
  from ._q_sql_driver import QSqlDriver
  from ._q_sql_driver_private import QSqlDriverPrivate
  from ._q_sql_index import QSqlIndex
  from ._q_sql_table_model_private import QSqlTableModelPrivate
  from ._q_sql_database import QSqlDatabase
  from ._q_sql_null_driver import QSqlNullDriver
  from ._q_sql_result import QSqlResult
  from ._q_sql_result_private import QSqlResultPrivate
  from ._q_sql_cached_result_private import QSqlCachedResultPrivate
  from ._q_sql_null_result import QSqlNullResult
  from ._q_sql_query import QSqlQuery
  from ._q_sql_cached_result import QSqlCachedResult
  from ._q_sql_query_model import QSqlQueryModel
  from ._q_sql_table_model import QSqlTableModel
  from ._q_sql_relational_table_model import QSqlRelationalTableModel
  from . import QSql
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QSqlDatabaseDefaultConnectionName': '_q_sql_database_default_connection_name',
      'QSqlDriverCreatorBase': '_q_sql_driver_creator_base',
      'QHolder': '_q_holder',
      'QSqlError': '_q_sql_error',
      'QSqlQueryModelSql': '_q_sql_query_model_sql',
      'QSqlRelation': '_q_sql_relation',
      'QSqlDriverPlugin': '_q_sql_driver_plugin',
      'QSqlField': '_q_sql_field',
      'QSqlQueryModelPrivate': '_q_sql_query_model_private',
      'QSqlRecord': '_q_sql_record',
      'QSqlDriver': '_q_sql_driver',
      'QSqlDriverPrivate': '_q_sql_driver_private',
      'QSqlIndex': '_q_sql_index',
      'QSqlTableModelPrivate': '_q_sql_table_model_private',
      'QSqlDatabase': '_q_sql_database',
      'QSqlNullDriver': '_q_sql_null_driver',
      'QSqlResult': '_q_sql_result',
      'QSqlResultPrivate': '_q_sql_result_private',
      'QSqlCachedResultPrivate': '_q_sql_cached_result_private',
      'QSqlNullResult': '_q_sql_null_result',
      'QSqlQuery': '_q_sql_query',
      'QSqlCachedResult': '_q_sql_cached_result',
      'QSqlQueryModel': '_q_sql_query_model',
      'QSqlTableModel': '_q_sql_table_model',
      'QSqlRelationalTableModel': '_q_sql_relational_table_model',
  }
  #  The namespaces of the part, each a package of its own.
  __space_packages__ = ('QSql',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtSql import QSqlRelationalTableModel'. Python calls
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
