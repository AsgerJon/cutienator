//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqltablemodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtSql/qtsqlglobal.h>
#if QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
#include <QtSql/qsqltablemodel.h>
#include <QtCore/qstring.h>
#include <QtSql/qsqldatabase.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtSql/qsqlrecord.h>
#include <QtCore/qvariant.h>
#include <QtSql/qsqlindex.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSqlTableModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSqlTableModel : QSqlTableModel {
  using QSqlTableModel::updateRowInTable;
  using QSqlTableModel::insertRowIntoTable;
  using QSqlTableModel::deleteRowFromTable;
  using QSqlTableModel::orderByClause;
  using QSqlTableModel::selectStatement;
  using QSqlTableModel::indexInQuery;
};

//  A QSqlTableModel that Python can take functions over in. Every QSqlTableModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelCall0)(const void *, const QString *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef int (*CuteQSqlTableModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef const QVariant * (*CuteQSqlTableModelCall2)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall3)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef const QVariant * (*CuteQSqlTableModelCall5)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelCall6)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelCall7)(const void *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelCall8)(const void *, int, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelCall9)(const void *, int, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelCall10)(const void *, const QString *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef int (*CuteQSqlTableModelCall11)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall12)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall13)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall14)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelCall15)(const void *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall16)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall17)(const void *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall18)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelCall19)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall20)(const void *, int, const QSqlRecord *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall21)(const void *, const QSqlRecord *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall22)(const void *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef QString * (*CuteQSqlTableModelCall23)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef QString * (*CuteQSqlTableModelCall24)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef const QModelIndex * (*CuteQSqlTableModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef int (*CuteQSqlTableModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall27)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall28)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlTableModelCall30)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlTableModelCall31)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlTableModelCall32)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlTableModelCall33)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlTableModelCall34)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlTableModelCall35)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlTableModelCall36)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlTableModelCall37)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQSqlTableModelCall38)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQSqlTableModelCall39)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlTableModelCall40)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlTableModelCall41)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlTableModelCall42)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQSqlTableModelCall43)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSqlTableModelCall44)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSqlTableModelCall45)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSqlTableModelCall46)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSqlTableModelCall47)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlTableModelCall48)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlTableModelCall49)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlTableModelCall50)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlTableModelCall51)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlTableModelCall52)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSqlTableModel : public QSqlTableModel {
public:
  using QSqlTableModel::QSqlTableModel;
  void *taken[53] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel8setTableERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlQueryModel5clearEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel15setEditStrategyENS_12EditStrategyE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel7setSortEiN2Qt9SortOrderE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel9setFilterERK7QString")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel9revertRowEi")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel6selectEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel9selectRowEi")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel16updateRowInTableEiRK10QSqlRecord")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel18insertRowIntoTableERK10QSqlRecord")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel18deleteRowFromTableEi")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK14QSqlTableModel13orderByClauseEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK14QSqlTableModel15selectStatementEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK14QSqlQueryModel12indexInQueryERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlQueryModel11queryChangeEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModel::setTable(const QString &tableName)
  void setTable(const QString &tableName) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlTableModelCall0 call = reinterpret_cast<CuteQSqlTableModelCall0>(taken[0]);
      call(this, &tableName, &handled);
      if (handled) return;
    }
    QSqlTableModel::setTable(tableName);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  Qt::ItemFlags QSqlTableModel::flags(const QModelIndex &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSqlTableModelCall1 call = reinterpret_cast<CuteQSqlTableModelCall1>(taken[1]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QSqlTableModel::flags(index);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  QVariant QSqlTableModel::data(const QModelIndex &idx, int role) const
  QVariant data(const QModelIndex &idx, int role) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSqlTableModelCall2 call = reinterpret_cast<CuteQSqlTableModelCall2>(taken[2]);
      const QVariant * given = call(this, &idx, role, &handled);
      if (handled && given) return *given;
    }
    return QSqlTableModel::data(idx, role);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::setData(const QModelIndex &index, const QVariant
  //      &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSqlTableModelCall3 call = reinterpret_cast<CuteQSqlTableModelCall3>(taken[3]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSqlTableModelCall4 call = reinterpret_cast<CuteQSqlTableModelCall4>(taken[4]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::clearItemData(index);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  QVariant QSqlTableModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSqlTableModelCall5 call = reinterpret_cast<CuteQSqlTableModelCall5>(taken[5]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QSqlTableModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModel::clear()
  void clear() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSqlTableModelCall6 call = reinterpret_cast<CuteQSqlTableModelCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QSqlTableModel::clear();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModel::setEditStrategy(EditStrategy strategy)
  void setEditStrategy(QSqlTableModel::EditStrategy strategy) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSqlTableModelCall7 call = reinterpret_cast<CuteQSqlTableModelCall7>(taken[7]);
      call(this, static_cast<int>(strategy), &handled);
      if (handled) return;
    }
    QSqlTableModel::setEditStrategy(strategy);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSqlTableModelCall8 call = reinterpret_cast<CuteQSqlTableModelCall8>(taken[8]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QSqlTableModel::sort(column, order);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModel::setSort(int column, Qt::SortOrder order)
  void setSort(int column, Qt::SortOrder order) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSqlTableModelCall9 call = reinterpret_cast<CuteQSqlTableModelCall9>(taken[9]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QSqlTableModel::setSort(column, order);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModel::setFilter(const QString &filter)
  void setFilter(const QString &filter) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSqlTableModelCall10 call = reinterpret_cast<CuteQSqlTableModelCall10>(taken[10]);
      call(this, &filter, &handled);
      if (handled) return;
    }
    QSqlTableModel::setFilter(filter);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  int QSqlTableModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSqlTableModelCall11 call = reinterpret_cast<CuteQSqlTableModelCall11>(taken[11]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::rowCount(parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSqlTableModelCall12 call = reinterpret_cast<CuteQSqlTableModelCall12>(taken[12]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::removeRows(int row, int count, const QModelIndex
  //      &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSqlTableModelCall13 call = reinterpret_cast<CuteQSqlTableModelCall13>(taken[13]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::removeRows(row, count, parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::insertRows(int row, int count, const QModelIndex
  //      &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSqlTableModelCall14 call = reinterpret_cast<CuteQSqlTableModelCall14>(taken[14]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModel::revertRow(int row)
  void revertRow(int row) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSqlTableModelCall15 call = reinterpret_cast<CuteQSqlTableModelCall15>(taken[15]);
      call(this, row, &handled);
      if (handled) return;
    }
    QSqlTableModel::revertRow(row);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::select()
  bool select() override {
    if (taken[16]) {
      int handled = 0;
      CuteQSqlTableModelCall16 call = reinterpret_cast<CuteQSqlTableModelCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::select();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::selectRow(int row)
  bool selectRow(int row) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSqlTableModelCall17 call = reinterpret_cast<CuteQSqlTableModelCall17>(taken[17]);
      bool given = call(this, row, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::selectRow(row);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::submit()
  bool submit() override {
    if (taken[18]) {
      int handled = 0;
      CuteQSqlTableModelCall18 call = reinterpret_cast<CuteQSqlTableModelCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::submit();
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModel::revert()
  void revert() override {
    if (taken[19]) {
      int handled = 0;
      CuteQSqlTableModelCall19 call = reinterpret_cast<CuteQSqlTableModelCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QSqlTableModel::revert();
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::updateRowInTable(int row, const QSqlRecord
  //      &values)
  bool updateRowInTable(int row, const QSqlRecord &values) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSqlTableModelCall20 call = reinterpret_cast<CuteQSqlTableModelCall20>(taken[20]);
      bool given = call(this, row, &values, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::updateRowInTable(row, values);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::insertRowIntoTable(const QSqlRecord &values)
  bool insertRowIntoTable(const QSqlRecord &values) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSqlTableModelCall21 call = reinterpret_cast<CuteQSqlTableModelCall21>(taken[21]);
      bool given = call(this, &values, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::insertRowIntoTable(values);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::deleteRowFromTable(int row)
  bool deleteRowFromTable(int row) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSqlTableModelCall22 call = reinterpret_cast<CuteQSqlTableModelCall22>(taken[22]);
      bool given = call(this, row, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::deleteRowFromTable(row);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  QString QSqlTableModel::orderByClause() const
  QString orderByClause() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQSqlTableModelCall23 call = reinterpret_cast<CuteQSqlTableModelCall23>(taken[23]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSqlTableModel::orderByClause();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  QString QSqlTableModel::selectStatement() const
  QString selectStatement() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQSqlTableModelCall24 call = reinterpret_cast<CuteQSqlTableModelCall24>(taken[24]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSqlTableModel::selectStatement();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  QModelIndex QSqlTableModel::indexInQuery(const QModelIndex &item)
  //      const
  QModelIndex indexInQuery(const QModelIndex &item) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQSqlTableModelCall25 call = reinterpret_cast<CuteQSqlTableModelCall25>(taken[25]);
      const QModelIndex * given = call(this, &item, &handled);
      if (handled && given) return *given;
    }
    return QSqlTableModel::indexInQuery(item);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  int QSqlQueryModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQSqlTableModelCall26 call = reinterpret_cast<CuteQSqlTableModelCall26>(taken[26]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QSqlQueryModel::columnCount(parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlQueryModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSqlTableModelCall27 call = reinterpret_cast<CuteQSqlTableModelCall27>(taken[27]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QSqlQueryModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlQueryModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSqlTableModelCall28 call = reinterpret_cast<CuteQSqlTableModelCall28>(taken[28]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QSqlQueryModel::insertColumns(column, count, parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  void QSqlQueryModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSqlTableModelCall29 call = reinterpret_cast<CuteQSqlTableModelCall29>(taken[29]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QSqlQueryModel::fetchMore(parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlQueryModel::canFetchMore(const QModelIndex &parent) const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[30]) {
      int handled = 0;
      CuteQSqlTableModelCall30 call = reinterpret_cast<CuteQSqlTableModelCall30>(taken[30]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QSqlQueryModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlQueryModel::queryChange()
  void queryChange() override {
    if (taken[31]) {
      int handled = 0;
      CuteQSqlTableModelCall31 call = reinterpret_cast<CuteQSqlTableModelCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QSqlQueryModel::queryChange();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractTableModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQSqlTableModelCall32 call = reinterpret_cast<CuteQSqlTableModelCall32>(taken[32]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QAbstractTableModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractTableModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQSqlTableModelCall33 call = reinterpret_cast<CuteQSqlTableModelCall33>(taken[33]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractTableModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractTableModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[34]) {
      int handled = 0;
      CuteQSqlTableModelCall34 call = reinterpret_cast<CuteQSqlTableModelCall34>(taken[34]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractTableModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractTableModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[35]) {
      int handled = 0;
      CuteQSqlTableModelCall35 call = reinterpret_cast<CuteQSqlTableModelCall35>(taken[35]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QAbstractTableModel::parent(child);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractTableModel::hasChildren(const QModelIndex &parent)
  //      const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQSqlTableModelCall36 call = reinterpret_cast<CuteQSqlTableModelCall36>(taken[36]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractTableModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::canDropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent) const
  bool canDropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQSqlTableModelCall37 call = reinterpret_cast<CuteQSqlTableModelCall37>(taken[37]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[38]) {
      int handled = 0;
      CuteQSqlTableModelCall38 call = reinterpret_cast<CuteQSqlTableModelCall38>(taken[38]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[39]) {
      int handled = 0;
      CuteQSqlTableModelCall39 call = reinterpret_cast<CuteQSqlTableModelCall39>(taken[39]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDragActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent,
  //      int sourceRow, int count, const QModelIndex &destinationParent,
  //      int destinationChild)
  bool moveRows(
      const QModelIndex &sourceParent,
      int sourceRow,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[40]) {
      int handled = 0;
      CuteQSqlTableModelCall40 call = reinterpret_cast<CuteQSqlTableModelCall40>(taken[40]);
      bool given = call(this, &sourceParent, sourceRow, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveRows(sourceParent, sourceRow, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent,
  //      int sourceColumn, int count, const QModelIndex
  //      &destinationParent, int destinationChild)
  bool moveColumns(
      const QModelIndex &sourceParent,
      int sourceColumn,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[41]) {
      int handled = 0;
      CuteQSqlTableModelCall41 call = reinterpret_cast<CuteQSqlTableModelCall41>(taken[41]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[42]) {
      int handled = 0;
      CuteQSqlTableModelCall42 call = reinterpret_cast<CuteQSqlTableModelCall42>(taken[42]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[43]) {
      int handled = 0;
      CuteQSqlTableModelCall43 call = reinterpret_cast<CuteQSqlTableModelCall43>(taken[43]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::span(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQSqlTableModelCall44 call = reinterpret_cast<CuteQSqlTableModelCall44>(taken[44]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[45]) {
      int handled = 0;
      CuteQSqlTableModelCall45 call = reinterpret_cast<CuteQSqlTableModelCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteQSqlTableModelCall46 call = reinterpret_cast<CuteQSqlTableModelCall46>(taken[46]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[47]) {
      int handled = 0;
      CuteQSqlTableModelCall47 call = reinterpret_cast<CuteQSqlTableModelCall47>(taken[47]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQSqlTableModelCall48 call = reinterpret_cast<CuteQSqlTableModelCall48>(taken[48]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQSqlTableModelCall49 call = reinterpret_cast<CuteQSqlTableModelCall49>(taken[49]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQSqlTableModelCall50 call = reinterpret_cast<CuteQSqlTableModelCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[51]) {
      int handled = 0;
      CuteQSqlTableModelCall51 call = reinterpret_cast<CuteQSqlTableModelCall51>(taken[51]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[52]) {
      int handled = 0;
      CuteQSqlTableModelCall52 call = reinterpret_cast<CuteQSqlTableModelCall52>(taken[52]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSqlTableModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QSqlTableModel10metaObjectEv(
    const QSqlTableModel *self) {
  return self->metaObject();
}

//  QString QSqlTableModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QSqlTableModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSqlTableModel::tr(s, c, n));
}

//  QSqlTableModelPrivate *QSqlTableModel::d_func()
extern "C" Q_DECL_EXPORT
QSqlTableModelPrivate *ritual_ZN14QSqlTableModel6d_funcEv(
    QSqlTableModel *self) {
  return self->d_func();
}

//  const QSqlTableModelPrivate *QSqlTableModel::d_func() const
extern "C" Q_DECL_EXPORT
const QSqlTableModelPrivate *ritual_ZNK14QSqlTableModel6d_funcEv(
    const QSqlTableModel *self) {
  return self->d_func();
}

//  QSqlTableModel::QSqlTableModel(QObject *parent, const QSqlDatabase &db)
extern "C" Q_DECL_EXPORT
QSqlTableModel *ritual_ZN14QSqlTableModelC1EP7QObjectRK12QSqlDatabase(
    QObject *parent,
    const QSqlDatabase *db) {
  return new CuteQSqlTableModel(parent, *db);
}

//  QSqlTableModel::~QSqlTableModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModelD1Ev(QSqlTableModel *self) {
  delete self;
}

//  void QSqlTableModel::setTable(const QString &tableName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModel8setTableERK7QString(
    QSqlTableModel *self,
    const QString *tableName) {
  self->setTable(*tableName);
}

//  QString QSqlTableModel::tableName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QSqlTableModel9tableNameEv(const QSqlTableModel *self) {
  return new QString(self->tableName());
}

//  Qt::ItemFlags QSqlTableModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSqlTableModel5flagsERK11QModelIndex(
    const QSqlTableModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  QSqlRecord QSqlTableModel::record() const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK14QSqlTableModel6recordEv(const QSqlTableModel *self) {
  return new QSqlRecord(self->record());
}

//  QSqlRecord QSqlTableModel::record(int row) const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK14QSqlTableModel6recordEi(
    const QSqlTableModel *self,
    int row) {
  return new QSqlRecord(self->record(row));
}

//  QVariant QSqlTableModel::data(const QModelIndex &idx, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QSqlTableModel4dataERK11QModelIndexi(
    const QSqlTableModel *self,
    const QModelIndex *idx,
    int role) {
  return new QVariant(self->data(*idx, role));
}

//  bool QSqlTableModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel7setDataERK11QModelIndexRK8QVarianti(
    QSqlTableModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  bool QSqlTableModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel13clearItemDataERK11QModelIndex(
    QSqlTableModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  QVariant QSqlTableModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QSqlTableModel10headerDataEiN2Qt11OrientationEi(
    const QSqlTableModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QSqlTableModel::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSqlTableModel7isDirtyEv(const QSqlTableModel *self) {
  return self->isDirty();
}

//  bool QSqlTableModel::isDirty(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSqlTableModel7isDirtyERK11QModelIndex(
    const QSqlTableModel *self,
    const QModelIndex *index) {
  return self->isDirty(*index);
}

//  void QSqlTableModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModel5clearEv(QSqlTableModel *self) {
  self->clear();
}

//  void QSqlTableModel::setEditStrategy(EditStrategy strategy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModel15setEditStrategyENS_12EditStrategyE(
    QSqlTableModel *self,
    QSqlTableModel::EditStrategy strategy) {
  self->setEditStrategy(strategy);
}

//  EditStrategy QSqlTableModel::editStrategy() const
extern "C" Q_DECL_EXPORT
QSqlTableModel::EditStrategy ritual_ZNK14QSqlTableModel12editStrategyEv(
    const QSqlTableModel *self) {
  return self->editStrategy();
}

//  QSqlIndex QSqlTableModel::primaryKey() const
extern "C" Q_DECL_EXPORT
QSqlIndex *ritual_ZNK14QSqlTableModel10primaryKeyEv(
    const QSqlTableModel *self) {
  return new QSqlIndex(self->primaryKey());
}

//  QSqlDatabase QSqlTableModel::database() const
extern "C" Q_DECL_EXPORT
QSqlDatabase *ritual_ZNK14QSqlTableModel8databaseEv(
    const QSqlTableModel *self) {
  return new QSqlDatabase(self->database());
}

//  int QSqlTableModel::fieldIndex(const QString &fieldName) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSqlTableModel10fieldIndexERK7QString(
    const QSqlTableModel *self,
    const QString *fieldName) {
  return self->fieldIndex(*fieldName);
}

//  void QSqlTableModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModel4sortEiN2Qt9SortOrderE(
    QSqlTableModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  void QSqlTableModel::setSort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModel7setSortEiN2Qt9SortOrderE(
    QSqlTableModel *self,
    int column,
    Qt::SortOrder order) {
  self->setSort(column, order);
}

//  QString QSqlTableModel::filter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QSqlTableModel6filterEv(const QSqlTableModel *self) {
  return new QString(self->filter());
}

//  void QSqlTableModel::setFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModel9setFilterERK7QString(
    QSqlTableModel *self,
    const QString *filter) {
  self->setFilter(*filter);
}

//  int QSqlTableModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSqlTableModel8rowCountERK11QModelIndex(
    const QSqlTableModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  bool QSqlTableModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel13removeColumnsEiiRK11QModelIndex(
    QSqlTableModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  bool QSqlTableModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel10removeRowsEiiRK11QModelIndex(
    QSqlTableModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QSqlTableModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel10insertRowsEiiRK11QModelIndex(
    QSqlTableModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QSqlTableModel::insertRecord(int row, const QSqlRecord &record)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel12insertRecordEiRK10QSqlRecord(
    QSqlTableModel *self,
    int row,
    const QSqlRecord *record) {
  return self->insertRecord(row, *record);
}

//  bool QSqlTableModel::setRecord(int row, const QSqlRecord &record)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel9setRecordEiRK10QSqlRecord(
    QSqlTableModel *self,
    int row,
    const QSqlRecord *record) {
  return self->setRecord(row, *record);
}

//  void QSqlTableModel::revertRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModel9revertRowEi(QSqlTableModel *self, int row) {
  self->revertRow(row);
}

//  bool QSqlTableModel::select()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel6selectEv(QSqlTableModel *self) {
  return self->select();
}

//  bool QSqlTableModel::selectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel9selectRowEi(QSqlTableModel *self, int row) {
  return self->selectRow(row);
}

//  bool QSqlTableModel::submit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel6submitEv(QSqlTableModel *self) {
  return self->submit();
}

//  void QSqlTableModel::revert()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModel6revertEv(QSqlTableModel *self) {
  self->revert();
}

//  bool QSqlTableModel::submitAll()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel9submitAllEv(QSqlTableModel *self) {
  return self->submitAll();
}

//  void QSqlTableModel::revertAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModel9revertAllEv(QSqlTableModel *self) {
  self->revertAll();
}

//  bool QSqlTableModel::updateRowInTable(int row, const QSqlRecord &values)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel16updateRowInTableEiRK10QSqlRecord(
    QSqlTableModel *self,
    int row,
    const QSqlRecord *values) {
  return self->updateRowInTable(row, *values);
}

//  bool QSqlTableModel::insertRowIntoTable(const QSqlRecord &values)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel18insertRowIntoTableERK10QSqlRecord(
    QSqlTableModel *self,
    const QSqlRecord *values) {
  return self->insertRowIntoTable(*values);
}

//  bool QSqlTableModel::deleteRowFromTable(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlTableModel18deleteRowFromTableEi(
    QSqlTableModel *self,
    int row) {
  return self->deleteRowFromTable(row);
}

//  QString QSqlTableModel::orderByClause() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QSqlTableModel13orderByClauseEv(
    const QSqlTableModel *self) {
  return new QString(self->orderByClause());
}

//  QString QSqlTableModel::selectStatement() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QSqlTableModel15selectStatementEv(
    const QSqlTableModel *self) {
  return new QString(self->selectStatement());
}

//  void QSqlTableModel::setPrimaryKey(const QSqlIndex &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlTableModel13setPrimaryKeyERK9QSqlIndex(
    QSqlTableModel *self,
    const QSqlIndex *key) {
  self->setPrimaryKey(*key);
}

//  QModelIndex QSqlTableModel::indexInQuery(const QModelIndex &item) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK14QSqlTableModel12indexInQueryERK11QModelIndex(
    const QSqlTableModel *self,
    const QModelIndex *item) {
  return new QModelIndex(self->indexInQuery(*item));
}

//  QSqlRecord QSqlTableModel::primaryValues(int row) const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK14QSqlTableModel13primaryValuesEi(
    const QSqlTableModel *self,
    int row) {
  return new QSqlRecord(self->primaryValues(row));
}

//  a Python function taken by a CuteQSqlTableModel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlTableModel(
    QSqlTableModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSqlTableModel *>(self)->take(key, call);
}

//  void QSqlTableModel::setTable(const QString &tableName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlTableModel8setTableERK7QString(
    QSqlTableModel *self,
    const QString *tableName) {
  self->QSqlTableModel::setTable(*tableName);
}

//  Qt::ItemFlags QSqlTableModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QSqlTableModel5flagsERK11QModelIndex(
    const QSqlTableModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QSqlTableModel::flags(*index).toInt());
}

//  QVariant QSqlTableModel::data(const QModelIndex &idx, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QSqlTableModel4dataERK11QModelIndexi(
    const QSqlTableModel *self,
    const QModelIndex *idx,
    int role) {
  return new QVariant(self->QSqlTableModel::data(*idx, role));
}

//  bool QSqlTableModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel7setDataERK11QModelIndexRK8QVarianti(
    QSqlTableModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QSqlTableModel::setData(*index, *value, role);
}

//  bool QSqlTableModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel13clearItemDataERK11QModelIndex(
    QSqlTableModel *self,
    const QModelIndex *index) {
  return self->QSqlTableModel::clearItemData(*index);
}

//  QVariant QSqlTableModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QSqlTableModel10headerDataEiN2Qt11OrientationEi(
    const QSqlTableModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QSqlTableModel::headerData(
          section,
          orientation,
          role));
}

//  void QSqlTableModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlTableModel5clearEv(QSqlTableModel *self) {
  self->QSqlTableModel::clear();
}

//  void QSqlTableModel::setEditStrategy(EditStrategy strategy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlTableModel15setEditStrategyENS_12EditStrategyE(
    QSqlTableModel *self,
    QSqlTableModel::EditStrategy strategy) {
  self->QSqlTableModel::setEditStrategy(strategy);
}

//  void QSqlTableModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlTableModel4sortEiN2Qt9SortOrderE(
    QSqlTableModel *self,
    int column,
    Qt::SortOrder order) {
  self->QSqlTableModel::sort(column, order);
}

//  void QSqlTableModel::setSort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlTableModel7setSortEiN2Qt9SortOrderE(
    QSqlTableModel *self,
    int column,
    Qt::SortOrder order) {
  self->QSqlTableModel::setSort(column, order);
}

//  void QSqlTableModel::setFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlTableModel9setFilterERK7QString(
    QSqlTableModel *self,
    const QString *filter) {
  self->QSqlTableModel::setFilter(*filter);
}

//  int QSqlTableModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QSqlTableModel8rowCountERK11QModelIndex(
    const QSqlTableModel *self,
    const QModelIndex *parent) {
  return self->QSqlTableModel::rowCount(*parent);
}

//  bool QSqlTableModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel13removeColumnsEiiRK11QModelIndex(
    QSqlTableModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QSqlTableModel::removeColumns(column, count, *parent);
}

//  bool QSqlTableModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel10removeRowsEiiRK11QModelIndex(
    QSqlTableModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QSqlTableModel::removeRows(row, count, *parent);
}

//  bool QSqlTableModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel10insertRowsEiiRK11QModelIndex(
    QSqlTableModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QSqlTableModel::insertRows(row, count, *parent);
}

//  void QSqlTableModel::revertRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlTableModel9revertRowEi(
    QSqlTableModel *self,
    int row) {
  self->QSqlTableModel::revertRow(row);
}

//  bool QSqlTableModel::select()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel6selectEv(QSqlTableModel *self) {
  return self->QSqlTableModel::select();
}

//  bool QSqlTableModel::selectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel9selectRowEi(
    QSqlTableModel *self,
    int row) {
  return self->QSqlTableModel::selectRow(row);
}

//  bool QSqlTableModel::submit()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel6submitEv(QSqlTableModel *self) {
  return self->QSqlTableModel::submit();
}

//  void QSqlTableModel::revert()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlTableModel6revertEv(QSqlTableModel *self) {
  self->QSqlTableModel::revert();
}

//  bool QSqlTableModel::updateRowInTable(int row, const QSqlRecord &values)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel16updateRowInTableEiRK10QSqlRecord(
    QSqlTableModel *self,
    int row,
    const QSqlRecord *values) {
  return static_cast<OwnQSqlTableModel *>(self)->OwnQSqlTableModel::updateRowInTable(
      row,
      *values);
}

//  bool QSqlTableModel::insertRowIntoTable(const QSqlRecord &values)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel18insertRowIntoTableERK10QSqlRecord(
    QSqlTableModel *self,
    const QSqlRecord *values) {
  return static_cast<OwnQSqlTableModel *>(self)->OwnQSqlTableModel::insertRowIntoTable(
      *values);
}

//  bool QSqlTableModel::deleteRowFromTable(int row)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlTableModel18deleteRowFromTableEi(
    QSqlTableModel *self,
    int row) {
  return static_cast<OwnQSqlTableModel *>(self)->OwnQSqlTableModel::deleteRowFromTable(
      row);
}

//  QString QSqlTableModel::orderByClause() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QSqlTableModel13orderByClauseEv(
    const QSqlTableModel *self) {
  return new QString(
      static_cast<const OwnQSqlTableModel *>(self)->OwnQSqlTableModel::orderByClause());
}

//  QString QSqlTableModel::selectStatement() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QSqlTableModel15selectStatementEv(
    const QSqlTableModel *self) {
  return new QString(
      static_cast<const OwnQSqlTableModel *>(self)->OwnQSqlTableModel::selectStatement());
}

//  QModelIndex QSqlTableModel::indexInQuery(const QModelIndex &item) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK14QSqlTableModel12indexInQueryERK11QModelIndex(
    const QSqlTableModel *self,
    const QModelIndex *item) {
  return new QModelIndex(
      static_cast<const OwnQSqlTableModel *>(self)->OwnQSqlTableModel::indexInQuery(
          *item));
}

#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(sqlmodel)
