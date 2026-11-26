//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqlrelationaltablemodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtSql/qtsqlglobal.h>
#if QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
#include <QtSql/qsqlrelationaltablemodel.h>
#include <QtCore/qstring.h>
#include <QtSql/qsqldatabase.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qvariant.h>
#include <QtSql/qsqlrecord.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSqlRelationalTableModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSqlRelationalTableModel : QSqlRelationalTableModel {
  using QSqlRelationalTableModel::selectStatement;
  using QSqlRelationalTableModel::updateRowInTable;
  using QSqlRelationalTableModel::insertRowIntoTable;
  using QSqlRelationalTableModel::orderByClause;
};

//  A QSqlRelationalTableModel that Python can take functions over in. Every QSqlRelationalTableModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef const QVariant * (*CuteQSqlRelationalTableModelCall0)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall1)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall2)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall3)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall4)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall5)(const void *, const QString *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall6)(const void *, int, const QSqlRelation *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef void * (*CuteQSqlRelationalTableModelCall7)(const void *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall8)(const void *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef QString * (*CuteQSqlRelationalTableModelCall9)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall10)(const void *, int, const QSqlRecord *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall11)(const void *, const QSqlRecord *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef QString * (*CuteQSqlRelationalTableModelCall12)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef int (*CuteQSqlRelationalTableModelCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef const QVariant * (*CuteQSqlRelationalTableModelCall15)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall16)(const void *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall17)(const void *, int, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall19)(const void *, const QString *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef int (*CuteQSqlRelationalTableModelCall20)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall21)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall22)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall23)(const void *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall24)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall25)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall26)(const void *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef const QModelIndex * (*CuteQSqlRelationalTableModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef int (*CuteQSqlRelationalTableModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall29)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall30)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall31)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlRelationalTableModelCall32)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlRelationalTableModelCall33)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlRelationalTableModelCall34)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlRelationalTableModelCall35)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlRelationalTableModelCall36)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlRelationalTableModelCall37)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlRelationalTableModelCall38)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlRelationalTableModelCall39)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQSqlRelationalTableModelCall40)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQSqlRelationalTableModelCall41)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlRelationalTableModelCall42)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlRelationalTableModelCall43)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlRelationalTableModelCall44)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQSqlRelationalTableModelCall45)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSqlRelationalTableModelCall46)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSqlRelationalTableModelCall47)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSqlRelationalTableModelCall48)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSqlRelationalTableModelCall49)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlRelationalTableModelCall50)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlRelationalTableModelCall51)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlRelationalTableModelCall52)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlRelationalTableModelCall53)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlRelationalTableModelCall54)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSqlRelationalTableModel : public QSqlRelationalTableModel {
public:
  using QSqlRelationalTableModel::QSqlRelationalTableModel;
  void *taken[55] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlQueryModel5clearEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel6selectEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel8setTableERK7QString")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN24QSqlRelationalTableModel11setRelationEiRK12QSqlRelation")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK24QSqlRelationalTableModel13relationModelEi")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel9revertRowEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK14QSqlTableModel15selectStatementEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel16updateRowInTableEiRK10QSqlRecord")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel18insertRowIntoTableERK10QSqlRecord")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK14QSqlTableModel13orderByClauseEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel15setEditStrategyENS_12EditStrategyE")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel7setSortEiN2Qt9SortOrderE")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel9setFilterERK7QString")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel9selectRowEi")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlTableModel18deleteRowFromTableEi")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK14QSqlQueryModel12indexInQueryERK11QModelIndex")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlQueryModel11queryChangeEv")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[41] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[42] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[43] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[44] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[45] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[46] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[47] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[49] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[50] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[51] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[52] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[53] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[54] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  QVariant QSqlRelationalTableModel::data(const QModelIndex &item, int
  //      role) const
  QVariant data(const QModelIndex &item, int role) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall0 call = reinterpret_cast<CuteQSqlRelationalTableModelCall0>(taken[0]);
      const QVariant * given = call(this, &item, role, &handled);
      if (handled && given) return *given;
    }
    return QSqlRelationalTableModel::data(item, role);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlRelationalTableModel::setData(const QModelIndex &item, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &item,
      const QVariant &value,
      int role) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall1 call = reinterpret_cast<CuteQSqlRelationalTableModelCall1>(taken[1]);
      bool given = call(this, &item, &value, role, &handled);
      if (handled) return given;
    }
    return QSqlRelationalTableModel::setData(item, value, role);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlRelationalTableModel::removeColumns(int column, int count,
  //      const QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall2 call = reinterpret_cast<CuteQSqlRelationalTableModelCall2>(taken[2]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QSqlRelationalTableModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlRelationalTableModel::clear()
  void clear() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall3 call = reinterpret_cast<CuteQSqlRelationalTableModelCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QSqlRelationalTableModel::clear();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  bool QSqlRelationalTableModel::select()
  bool select() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall4 call = reinterpret_cast<CuteQSqlRelationalTableModelCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSqlRelationalTableModel::select();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlRelationalTableModel::setTable(const QString &tableName)
  void setTable(const QString &tableName) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall5 call = reinterpret_cast<CuteQSqlRelationalTableModelCall5>(taken[5]);
      call(this, &tableName, &handled);
      if (handled) return;
    }
    QSqlRelationalTableModel::setTable(tableName);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlRelationalTableModel::setRelation(int column, const
  //      QSqlRelation &relation)
  void setRelation(int column, const QSqlRelation &relation) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall6 call = reinterpret_cast<CuteQSqlRelationalTableModelCall6>(taken[6]);
      call(this, column, &relation, &handled);
      if (handled) return;
    }
    QSqlRelationalTableModel::setRelation(column, relation);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  QSqlTableModel *QSqlRelationalTableModel::relationModel(int column)
  //      const
  QSqlTableModel *relationModel(int column) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall7 call = reinterpret_cast<CuteQSqlRelationalTableModelCall7>(taken[7]);
      void * given = call(this, column, &handled);
      if (handled) return static_cast<QSqlTableModel *>(given);
    }
    return QSqlRelationalTableModel::relationModel(column);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlRelationalTableModel::revertRow(int row)
  void revertRow(int row) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall8 call = reinterpret_cast<CuteQSqlRelationalTableModelCall8>(taken[8]);
      call(this, row, &handled);
      if (handled) return;
    }
    QSqlRelationalTableModel::revertRow(row);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  QString QSqlRelationalTableModel::selectStatement() const
  QString selectStatement() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall9 call = reinterpret_cast<CuteQSqlRelationalTableModelCall9>(taken[9]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSqlRelationalTableModel::selectStatement();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  bool QSqlRelationalTableModel::updateRowInTable(int row, const
  //      QSqlRecord &values)
  bool updateRowInTable(int row, const QSqlRecord &values) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall10 call = reinterpret_cast<CuteQSqlRelationalTableModelCall10>(taken[10]);
      bool given = call(this, row, &values, &handled);
      if (handled) return given;
    }
    return QSqlRelationalTableModel::updateRowInTable(row, values);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  bool QSqlRelationalTableModel::insertRowIntoTable(const QSqlRecord
  //      &values)
  bool insertRowIntoTable(const QSqlRecord &values) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall11 call = reinterpret_cast<CuteQSqlRelationalTableModelCall11>(taken[11]);
      bool given = call(this, &values, &handled);
      if (handled) return given;
    }
    return QSqlRelationalTableModel::insertRowIntoTable(values);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  QString QSqlRelationalTableModel::orderByClause() const
  QString orderByClause() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall12 call = reinterpret_cast<CuteQSqlRelationalTableModelCall12>(taken[12]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSqlRelationalTableModel::orderByClause();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  Qt::ItemFlags QSqlTableModel::flags(const QModelIndex &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall13 call = reinterpret_cast<CuteQSqlRelationalTableModelCall13>(taken[13]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QSqlTableModel::flags(index);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall14 call = reinterpret_cast<CuteQSqlRelationalTableModelCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall15 call = reinterpret_cast<CuteQSqlRelationalTableModelCall15>(taken[15]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QSqlTableModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModel::setEditStrategy(EditStrategy strategy)
  void setEditStrategy(QSqlTableModel::EditStrategy strategy) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall16 call = reinterpret_cast<CuteQSqlRelationalTableModelCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall17 call = reinterpret_cast<CuteQSqlRelationalTableModelCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall18 call = reinterpret_cast<CuteQSqlRelationalTableModelCall18>(taken[18]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QSqlTableModel::setSort(column, order);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlTableModel::setFilter(const QString &filter)
  void setFilter(const QString &filter) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall19 call = reinterpret_cast<CuteQSqlRelationalTableModelCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall20 call = reinterpret_cast<CuteQSqlRelationalTableModelCall20>(taken[20]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::rowCount(parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::removeRows(int row, int count, const QModelIndex
  //      &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall21 call = reinterpret_cast<CuteQSqlRelationalTableModelCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall22 call = reinterpret_cast<CuteQSqlRelationalTableModelCall22>(taken[22]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::selectRow(int row)
  bool selectRow(int row) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall23 call = reinterpret_cast<CuteQSqlRelationalTableModelCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall24 call = reinterpret_cast<CuteQSqlRelationalTableModelCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall25 call = reinterpret_cast<CuteQSqlRelationalTableModelCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QSqlTableModel::revert();
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(sqlmodel)
  //  bool QSqlTableModel::deleteRowFromTable(int row)
  bool deleteRowFromTable(int row) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall26 call = reinterpret_cast<CuteQSqlRelationalTableModelCall26>(taken[26]);
      bool given = call(this, row, &handled);
      if (handled) return given;
    }
    return QSqlTableModel::deleteRowFromTable(row);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  QModelIndex QSqlTableModel::indexInQuery(const QModelIndex &item)
  //      const
  QModelIndex indexInQuery(const QModelIndex &item) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall27 call = reinterpret_cast<CuteQSqlRelationalTableModelCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall28 call = reinterpret_cast<CuteQSqlRelationalTableModelCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall29 call = reinterpret_cast<CuteQSqlRelationalTableModelCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall30 call = reinterpret_cast<CuteQSqlRelationalTableModelCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall31 call = reinterpret_cast<CuteQSqlRelationalTableModelCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall32 call = reinterpret_cast<CuteQSqlRelationalTableModelCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall33 call = reinterpret_cast<CuteQSqlRelationalTableModelCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall34 call = reinterpret_cast<CuteQSqlRelationalTableModelCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall35 call = reinterpret_cast<CuteQSqlRelationalTableModelCall35>(taken[35]);
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
    if (taken[36]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall36 call = reinterpret_cast<CuteQSqlRelationalTableModelCall36>(taken[36]);
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
    if (taken[37]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall37 call = reinterpret_cast<CuteQSqlRelationalTableModelCall37>(taken[37]);
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
    if (taken[38]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall38 call = reinterpret_cast<CuteQSqlRelationalTableModelCall38>(taken[38]);
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
    if (taken[39]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall39 call = reinterpret_cast<CuteQSqlRelationalTableModelCall39>(taken[39]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[40]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall40 call = reinterpret_cast<CuteQSqlRelationalTableModelCall40>(taken[40]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[41]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall41 call = reinterpret_cast<CuteQSqlRelationalTableModelCall41>(taken[41]);
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
    if (taken[42]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall42 call = reinterpret_cast<CuteQSqlRelationalTableModelCall42>(taken[42]);
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
    if (taken[43]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall43 call = reinterpret_cast<CuteQSqlRelationalTableModelCall43>(taken[43]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[44]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall44 call = reinterpret_cast<CuteQSqlRelationalTableModelCall44>(taken[44]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[45]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall45 call = reinterpret_cast<CuteQSqlRelationalTableModelCall45>(taken[45]);
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
    if (taken[46]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall46 call = reinterpret_cast<CuteQSqlRelationalTableModelCall46>(taken[46]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[47]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall47 call = reinterpret_cast<CuteQSqlRelationalTableModelCall47>(taken[47]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[48]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall48 call = reinterpret_cast<CuteQSqlRelationalTableModelCall48>(taken[48]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[49]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall49 call = reinterpret_cast<CuteQSqlRelationalTableModelCall49>(taken[49]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[50]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall50 call = reinterpret_cast<CuteQSqlRelationalTableModelCall50>(taken[50]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[51]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall51 call = reinterpret_cast<CuteQSqlRelationalTableModelCall51>(taken[51]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[52]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall52 call = reinterpret_cast<CuteQSqlRelationalTableModelCall52>(taken[52]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[53]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall53 call = reinterpret_cast<CuteQSqlRelationalTableModelCall53>(taken[53]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[54]) {
      int handled = 0;
      CuteQSqlRelationalTableModelCall54 call = reinterpret_cast<CuteQSqlRelationalTableModelCall54>(taken[54]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSqlRelationalTableModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QSqlRelationalTableModel10metaObjectEv(
    const QSqlRelationalTableModel *self) {
  return self->metaObject();
}

//  void *QSqlRelationalTableModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QSqlRelationalTableModel11qt_metacastEPKc(
    QSqlRelationalTableModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSqlRelationalTableModel::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QSqlRelationalTableModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QSqlRelationalTableModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSqlRelationalTableModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QSqlRelationalTableModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSqlRelationalTableModel::tr(s, c, n));
}

//  QSqlRelationalTableModel::QSqlRelationalTableModel(QObject *parent, const
//      QSqlDatabase &db)
extern "C" Q_DECL_EXPORT
QSqlRelationalTableModel *ritual_ZN24QSqlRelationalTableModelC1EP7QObjectRK12QSqlDatabase(
    QObject *parent,
    const QSqlDatabase *db) {
  return new CuteQSqlRelationalTableModel(parent, *db);
}

//  QSqlRelationalTableModel::~QSqlRelationalTableModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSqlRelationalTableModelD1Ev(
    QSqlRelationalTableModel *self) {
  delete self;
}

//  QVariant QSqlRelationalTableModel::data(const QModelIndex &item, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QSqlRelationalTableModel4dataERK11QModelIndexi(
    const QSqlRelationalTableModel *self,
    const QModelIndex *item,
    int role) {
  return new QVariant(self->data(*item, role));
}

//  bool QSqlRelationalTableModel::setData(const QModelIndex &item, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QSqlRelationalTableModel7setDataERK11QModelIndexRK8QVarianti(
    QSqlRelationalTableModel *self,
    const QModelIndex *item,
    const QVariant *value,
    int role) {
  return self->setData(*item, *value, role);
}

//  bool QSqlRelationalTableModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QSqlRelationalTableModel13removeColumnsEiiRK11QModelIndex(
    QSqlRelationalTableModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  void QSqlRelationalTableModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSqlRelationalTableModel5clearEv(
    QSqlRelationalTableModel *self) {
  self->clear();
}

//  bool QSqlRelationalTableModel::select()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QSqlRelationalTableModel6selectEv(
    QSqlRelationalTableModel *self) {
  return self->select();
}

//  void QSqlRelationalTableModel::setTable(const QString &tableName)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSqlRelationalTableModel8setTableERK7QString(
    QSqlRelationalTableModel *self,
    const QString *tableName) {
  self->setTable(*tableName);
}

//  void QSqlRelationalTableModel::setRelation(int column, const QSqlRelation
//      &relation)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSqlRelationalTableModel11setRelationEiRK12QSqlRelation(
    QSqlRelationalTableModel *self,
    int column,
    const QSqlRelation *relation) {
  self->setRelation(column, *relation);
}

//  QSqlRelation QSqlRelationalTableModel::relation(int column) const
extern "C" Q_DECL_EXPORT
QSqlRelation *ritual_ZNK24QSqlRelationalTableModel8relationEi(
    const QSqlRelationalTableModel *self,
    int column) {
  return new QSqlRelation(self->relation(column));
}

//  QSqlTableModel *QSqlRelationalTableModel::relationModel(int column) const
extern "C" Q_DECL_EXPORT
QSqlTableModel *ritual_ZNK24QSqlRelationalTableModel13relationModelEi(
    const QSqlRelationalTableModel *self,
    int column) {
  return self->relationModel(column);
}

//  void
//      QSqlRelationalTableModel::setJoinMode(QSqlRelationalTableModel::JoinM
//      ode joinMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSqlRelationalTableModel11setJoinModeENS_8JoinModeE(
    QSqlRelationalTableModel *self,
    QSqlRelationalTableModel::JoinMode joinMode) {
  self->setJoinMode(joinMode);
}

//  void QSqlRelationalTableModel::revertRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSqlRelationalTableModel9revertRowEi(
    QSqlRelationalTableModel *self,
    int row) {
  self->revertRow(row);
}

//  QString QSqlRelationalTableModel::selectStatement() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QSqlRelationalTableModel15selectStatementEv(
    const QSqlRelationalTableModel *self) {
  return new QString(self->selectStatement());
}

//  bool QSqlRelationalTableModel::updateRowInTable(int row, const QSqlRecord
//      &values)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QSqlRelationalTableModel16updateRowInTableEiRK10QSqlRecord(
    QSqlRelationalTableModel *self,
    int row,
    const QSqlRecord *values) {
  return self->updateRowInTable(row, *values);
}

//  bool QSqlRelationalTableModel::insertRowIntoTable(const QSqlRecord
//      &values)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QSqlRelationalTableModel18insertRowIntoTableERK10QSqlRecord(
    QSqlRelationalTableModel *self,
    const QSqlRecord *values) {
  return self->insertRowIntoTable(*values);
}

//  QString QSqlRelationalTableModel::orderByClause() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QSqlRelationalTableModel13orderByClauseEv(
    const QSqlRelationalTableModel *self) {
  return new QString(self->orderByClause());
}

//  QSqlRelationalTableModelPrivate *QSqlRelationalTableModel::d_func()
extern "C" Q_DECL_EXPORT
QSqlRelationalTableModelPrivate *ritual_ZN24QSqlRelationalTableModel6d_funcEv(
    QSqlRelationalTableModel *self) {
  return self->d_func();
}

//  const QSqlRelationalTableModelPrivate *QSqlRelationalTableModel::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QSqlRelationalTableModelPrivate *ritual_ZNK24QSqlRelationalTableModel6d_funcEv(
    const QSqlRelationalTableModel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSqlRelationalTableModel, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlRelationalTableModel(
    QSqlRelationalTableModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSqlRelationalTableModel *>(self)->take(key, call);
}

//  QVariant QSqlRelationalTableModel::data(const QModelIndex &item, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK24QSqlRelationalTableModel4dataERK11QModelIndexi(
    const QSqlRelationalTableModel *self,
    const QModelIndex *item,
    int role) {
  return new QVariant(self->QSqlRelationalTableModel::data(*item, role));
}

//  bool QSqlRelationalTableModel::setData(const QModelIndex &item, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QSqlRelationalTableModel7setDataERK11QModelIndexRK8QVarianti(
    QSqlRelationalTableModel *self,
    const QModelIndex *item,
    const QVariant *value,
    int role) {
  return self->QSqlRelationalTableModel::setData(*item, *value, role);
}

//  bool QSqlRelationalTableModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QSqlRelationalTableModel13removeColumnsEiiRK11QModelIndex(
    QSqlRelationalTableModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QSqlRelationalTableModel::removeColumns(
      column,
      count,
      *parent);
}

//  void QSqlRelationalTableModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSqlRelationalTableModel5clearEv(
    QSqlRelationalTableModel *self) {
  self->QSqlRelationalTableModel::clear();
}

//  bool QSqlRelationalTableModel::select()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QSqlRelationalTableModel6selectEv(
    QSqlRelationalTableModel *self) {
  return self->QSqlRelationalTableModel::select();
}

//  void QSqlRelationalTableModel::setTable(const QString &tableName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSqlRelationalTableModel8setTableERK7QString(
    QSqlRelationalTableModel *self,
    const QString *tableName) {
  self->QSqlRelationalTableModel::setTable(*tableName);
}

//  void QSqlRelationalTableModel::setRelation(int column, const QSqlRelation
//      &relation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSqlRelationalTableModel11setRelationEiRK12QSqlRelation(
    QSqlRelationalTableModel *self,
    int column,
    const QSqlRelation *relation) {
  self->QSqlRelationalTableModel::setRelation(column, *relation);
}

//  QSqlTableModel *QSqlRelationalTableModel::relationModel(int column) const
extern "C" Q_DECL_EXPORT
QSqlTableModel *ritual_own_ZNK24QSqlRelationalTableModel13relationModelEi(
    const QSqlRelationalTableModel *self,
    int column) {
  return self->QSqlRelationalTableModel::relationModel(column);
}

//  void QSqlRelationalTableModel::revertRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSqlRelationalTableModel9revertRowEi(
    QSqlRelationalTableModel *self,
    int row) {
  self->QSqlRelationalTableModel::revertRow(row);
}

//  QString QSqlRelationalTableModel::selectStatement() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK24QSqlRelationalTableModel15selectStatementEv(
    const QSqlRelationalTableModel *self) {
  return new QString(
      static_cast<const OwnQSqlRelationalTableModel *>(self)->OwnQSqlRelationalTableModel::selectStatement());
}

//  bool QSqlRelationalTableModel::updateRowInTable(int row, const QSqlRecord
//      &values)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QSqlRelationalTableModel16updateRowInTableEiRK10QSqlRecord(
    QSqlRelationalTableModel *self,
    int row,
    const QSqlRecord *values) {
  return static_cast<OwnQSqlRelationalTableModel *>(self)->OwnQSqlRelationalTableModel::updateRowInTable(
      row,
      *values);
}

//  bool QSqlRelationalTableModel::insertRowIntoTable(const QSqlRecord
//      &values)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QSqlRelationalTableModel18insertRowIntoTableERK10QSqlRecord(
    QSqlRelationalTableModel *self,
    const QSqlRecord *values) {
  return static_cast<OwnQSqlRelationalTableModel *>(self)->OwnQSqlRelationalTableModel::insertRowIntoTable(
      *values);
}

//  QString QSqlRelationalTableModel::orderByClause() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK24QSqlRelationalTableModel13orderByClauseEv(
    const QSqlRelationalTableModel *self) {
  return new QString(
      static_cast<const OwnQSqlRelationalTableModel *>(self)->OwnQSqlRelationalTableModel::orderByClause());
}

#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(sqlmodel)
