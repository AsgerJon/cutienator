//  Written by dev_tooling.RitualGenerator from the records of
//  QtSql/qsqlquerymodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtSql/qtsqlglobal.h>
#if QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
#include <QtSql/qsqlquerymodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtSql/qsqlrecord.h>
#include <QtCore/qvariant.h>
#include <QtSql/qsqlquery.h>
#include <QtSql/qsqldatabase.h>
#include <QtCore/qnamespace.h>
#include <QtSql/qsqlerror.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QSqlQueryModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSqlQueryModel : QSqlQueryModel {
  using QSqlQueryModel::queryChange;
  using QSqlQueryModel::indexInQuery;
};

//  A QSqlQueryModel that Python can take functions over in. Every QSqlQueryModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef int (*CuteQSqlQueryModelCall0)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef int (*CuteQSqlQueryModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef const QVariant * (*CuteQSqlQueryModelCall2)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef const QVariant * (*CuteQSqlQueryModelCall3)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlQueryModelCall4)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlQueryModelCall5)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlQueryModelCall6)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlQueryModelCall7)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlQueryModelCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef bool (*CuteQSqlQueryModelCall9)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
typedef void (*CuteQSqlQueryModelCall10)(const void *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
typedef const QModelIndex * (*CuteQSqlQueryModelCall11)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlQueryModelCall12)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlQueryModelCall13)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlQueryModelCall14)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQSqlQueryModelCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlQueryModelCall16)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlQueryModelCall17)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlQueryModelCall18)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlQueryModelCall19)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlQueryModelCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQSqlQueryModelCall21)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQSqlQueryModelCall22)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlQueryModelCall23)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlQueryModelCall24)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlQueryModelCall25)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlQueryModelCall26)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSqlQueryModelCall27)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQSqlQueryModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQSqlQueryModelCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSqlQueryModelCall30)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSqlQueryModelCall31)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSqlQueryModelCall32)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSqlQueryModelCall33)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSqlQueryModelCall34)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSqlQueryModelCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlQueryModelCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlQueryModelCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlQueryModelCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlQueryModelCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSqlQueryModelCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSqlQueryModel : public QSqlQueryModel {
public:
  using QSqlQueryModel::QSqlQueryModel;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
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
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlQueryModel5clearEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZN14QSqlQueryModel11queryChangeEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(sqlmodel)
    if (!std::strcmp(key, "_ZNK14QSqlQueryModel12indexInQueryERK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(sqlmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  int QSqlQueryModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSqlQueryModelCall0 call = reinterpret_cast<CuteQSqlQueryModelCall0>(taken[0]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QSqlQueryModel::rowCount(parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  int QSqlQueryModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSqlQueryModelCall1 call = reinterpret_cast<CuteQSqlQueryModelCall1>(taken[1]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QSqlQueryModel::columnCount(parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  QVariant QSqlQueryModel::data(const QModelIndex &item, int role)
  //      const
  QVariant data(const QModelIndex &item, int role) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSqlQueryModelCall2 call = reinterpret_cast<CuteQSqlQueryModelCall2>(taken[2]);
      const QVariant * given = call(this, &item, role, &handled);
      if (handled && given) return *given;
    }
    return QSqlQueryModel::data(item, role);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  QVariant QSqlQueryModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSqlQueryModelCall3 call = reinterpret_cast<CuteQSqlQueryModelCall3>(taken[3]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QSqlQueryModel::headerData(section, orientation, role);
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
    if (taken[4]) {
      int handled = 0;
      CuteQSqlQueryModelCall4 call = reinterpret_cast<CuteQSqlQueryModelCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQSqlQueryModelCall5 call = reinterpret_cast<CuteQSqlQueryModelCall5>(taken[5]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QSqlQueryModel::insertColumns(column, count, parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  bool QSqlQueryModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSqlQueryModelCall6 call = reinterpret_cast<CuteQSqlQueryModelCall6>(taken[6]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QSqlQueryModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(sqlmodel)
  //  void QSqlQueryModel::clear()
  void clear() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSqlQueryModelCall7 call = reinterpret_cast<CuteQSqlQueryModelCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QSqlQueryModel::clear();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sqlmodel)
  //  void QSqlQueryModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSqlQueryModelCall8 call = reinterpret_cast<CuteQSqlQueryModelCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQSqlQueryModelCall9 call = reinterpret_cast<CuteQSqlQueryModelCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQSqlQueryModelCall10 call = reinterpret_cast<CuteQSqlQueryModelCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QSqlQueryModel::queryChange();
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(sqlmodel)
  //  QModelIndex QSqlQueryModel::indexInQuery(const QModelIndex &item)
  //      const
  QModelIndex indexInQuery(const QModelIndex &item) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSqlQueryModelCall11 call = reinterpret_cast<CuteQSqlQueryModelCall11>(taken[11]);
      const QModelIndex * given = call(this, &item, &handled);
      if (handled && given) return *given;
    }
    return QSqlQueryModel::indexInQuery(item);
  }
#endif  // QT_CONFIG(sqlmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractTableModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSqlQueryModelCall12 call = reinterpret_cast<CuteQSqlQueryModelCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQSqlQueryModelCall13 call = reinterpret_cast<CuteQSqlQueryModelCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQSqlQueryModelCall14 call = reinterpret_cast<CuteQSqlQueryModelCall14>(taken[14]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractTableModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::ItemFlags QAbstractTableModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSqlQueryModelCall15 call = reinterpret_cast<CuteQSqlQueryModelCall15>(taken[15]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QAbstractTableModel::flags(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractTableModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSqlQueryModelCall16 call = reinterpret_cast<CuteQSqlQueryModelCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQSqlQueryModelCall17 call = reinterpret_cast<CuteQSqlQueryModelCall17>(taken[17]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractTableModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSqlQueryModelCall18 call = reinterpret_cast<CuteQSqlQueryModelCall18>(taken[18]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSqlQueryModelCall19 call = reinterpret_cast<CuteQSqlQueryModelCall19>(taken[19]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::clearItemData(index);
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
    if (taken[20]) {
      int handled = 0;
      CuteQSqlQueryModelCall20 call = reinterpret_cast<CuteQSqlQueryModelCall20>(taken[20]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQSqlQueryModelCall21 call = reinterpret_cast<CuteQSqlQueryModelCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSqlQueryModelCall22 call = reinterpret_cast<CuteQSqlQueryModelCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDragActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSqlQueryModelCall23 call = reinterpret_cast<CuteQSqlQueryModelCall23>(taken[23]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSqlQueryModelCall24 call = reinterpret_cast<CuteQSqlQueryModelCall24>(taken[24]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeRows(row, count, parent);
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
    if (taken[25]) {
      int handled = 0;
      CuteQSqlQueryModelCall25 call = reinterpret_cast<CuteQSqlQueryModelCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQSqlQueryModelCall26 call = reinterpret_cast<CuteQSqlQueryModelCall26>(taken[26]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSqlQueryModelCall27 call = reinterpret_cast<CuteQSqlQueryModelCall27>(taken[27]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractItemModel::sort(column, order);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQSqlQueryModelCall28 call = reinterpret_cast<CuteQSqlQueryModelCall28>(taken[28]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQSqlQueryModelCall29 call = reinterpret_cast<CuteQSqlQueryModelCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQSqlQueryModelCall30 call = reinterpret_cast<CuteQSqlQueryModelCall30>(taken[30]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[31]) {
      int handled = 0;
      CuteQSqlQueryModelCall31 call = reinterpret_cast<CuteQSqlQueryModelCall31>(taken[31]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[32]) {
      int handled = 0;
      CuteQSqlQueryModelCall32 call = reinterpret_cast<CuteQSqlQueryModelCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[33]) {
      int handled = 0;
      CuteQSqlQueryModelCall33 call = reinterpret_cast<CuteQSqlQueryModelCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQSqlQueryModelCall34 call = reinterpret_cast<CuteQSqlQueryModelCall34>(taken[34]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQSqlQueryModelCall35 call = reinterpret_cast<CuteQSqlQueryModelCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQSqlQueryModelCall36 call = reinterpret_cast<CuteQSqlQueryModelCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQSqlQueryModelCall37 call = reinterpret_cast<CuteQSqlQueryModelCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQSqlQueryModelCall38 call = reinterpret_cast<CuteQSqlQueryModelCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteQSqlQueryModelCall39 call = reinterpret_cast<CuteQSqlQueryModelCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQSqlQueryModelCall40 call = reinterpret_cast<CuteQSqlQueryModelCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSqlQueryModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QSqlQueryModel10metaObjectEv(
    const QSqlQueryModel *self) {
  return self->metaObject();
}

//  QString QSqlQueryModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QSqlQueryModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSqlQueryModel::tr(s, c, n));
}

//  QSqlQueryModelPrivate *QSqlQueryModel::d_func()
extern "C" Q_DECL_EXPORT
QSqlQueryModelPrivate *ritual_ZN14QSqlQueryModel6d_funcEv(
    QSqlQueryModel *self) {
  return self->d_func();
}

//  const QSqlQueryModelPrivate *QSqlQueryModel::d_func() const
extern "C" Q_DECL_EXPORT
const QSqlQueryModelPrivate *ritual_ZNK14QSqlQueryModel6d_funcEv(
    const QSqlQueryModel *self) {
  return self->d_func();
}

//  QSqlQueryModel::QSqlQueryModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QSqlQueryModel *ritual_ZN14QSqlQueryModelC1EP7QObject(QObject *parent) {
  return new CuteQSqlQueryModel(parent);
}

//  QSqlQueryModel::~QSqlQueryModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModelD1Ev(QSqlQueryModel *self) {
  delete self;
}

//  int QSqlQueryModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSqlQueryModel8rowCountERK11QModelIndex(
    const QSqlQueryModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QSqlQueryModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSqlQueryModel11columnCountERK11QModelIndex(
    const QSqlQueryModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QSqlRecord QSqlQueryModel::record(int row) const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK14QSqlQueryModel6recordEi(
    const QSqlQueryModel *self,
    int row) {
  return new QSqlRecord(self->record(row));
}

//  QSqlRecord QSqlQueryModel::record() const
extern "C" Q_DECL_EXPORT
QSqlRecord *ritual_ZNK14QSqlQueryModel6recordEv(const QSqlQueryModel *self) {
  return new QSqlRecord(self->record());
}

//  QVariant QSqlQueryModel::data(const QModelIndex &item, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QSqlQueryModel4dataERK11QModelIndexi(
    const QSqlQueryModel *self,
    const QModelIndex *item,
    int role) {
  return new QVariant(self->data(*item, role));
}

//  QVariant QSqlQueryModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QSqlQueryModel10headerDataEiN2Qt11OrientationEi(
    const QSqlQueryModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QSqlQueryModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlQueryModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QSqlQueryModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  bool QSqlQueryModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlQueryModel13insertColumnsEiiRK11QModelIndex(
    QSqlQueryModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QSqlQueryModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QSqlQueryModel13removeColumnsEiiRK11QModelIndex(
    QSqlQueryModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

#if QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 2)
//  void QSqlQueryModel::setQuery(const QSqlQuery &query)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel8setQueryERK9QSqlQuery(
    QSqlQueryModel *self,
    const QSqlQuery *query) {
  self->setQuery(*query);
}
#endif  // QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 2)

//  void QSqlQueryModel::setQuery(const QString &query, const QSqlDatabase
//      &db)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel8setQueryERK7QStringRK12QSqlDatabase(
    QSqlQueryModel *self,
    const QString *query,
    const QSqlDatabase *db) {
  self->setQuery(*query, *db);
}

//  void QSqlQueryModel::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel7refreshEv(QSqlQueryModel *self) {
  self->refresh();
}

//  const QSqlQuery &QSqlQueryModel::query(Qt::Disambiguated_t a0) const
extern "C" Q_DECL_EXPORT
QSqlQuery *ritual_ZNK14QSqlQueryModel5queryEN2Qt15Disambiguated_tE(
    const QSqlQueryModel *self,
    const Qt::Disambiguated_t *a0) {
  return new QSqlQuery(self->query(*a0));
}

//  void QSqlQueryModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel5clearEv(QSqlQueryModel *self) {
  self->clear();
}

//  QSqlError QSqlQueryModel::lastError() const
extern "C" Q_DECL_EXPORT
QSqlError *ritual_ZNK14QSqlQueryModel9lastErrorEv(
    const QSqlQueryModel *self) {
  return new QSqlError(self->lastError());
}

//  void QSqlQueryModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel9fetchMoreERK11QModelIndex(
    QSqlQueryModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  bool QSqlQueryModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSqlQueryModel12canFetchMoreERK11QModelIndex(
    const QSqlQueryModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  QHash<int, QByteArray> QSqlQueryModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK14QSqlQueryModel9roleNamesEv(
    const QSqlQueryModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  void QSqlQueryModel::beginInsertRows(const QModelIndex &parent, int
//      first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel15beginInsertRowsERK11QModelIndexii(
    QSqlQueryModel *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginInsertRows(*parent, first, last);
}

//  void QSqlQueryModel::endInsertRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel13endInsertRowsEv(QSqlQueryModel *self) {
  self->endInsertRows();
}

//  void QSqlQueryModel::beginRemoveRows(const QModelIndex &parent, int
//      first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel15beginRemoveRowsERK11QModelIndexii(
    QSqlQueryModel *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginRemoveRows(*parent, first, last);
}

//  void QSqlQueryModel::endRemoveRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel13endRemoveRowsEv(QSqlQueryModel *self) {
  self->endRemoveRows();
}

//  void QSqlQueryModel::beginInsertColumns(const QModelIndex &parent, int
//      first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel18beginInsertColumnsERK11QModelIndexii(
    QSqlQueryModel *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginInsertColumns(*parent, first, last);
}

//  void QSqlQueryModel::endInsertColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel16endInsertColumnsEv(QSqlQueryModel *self) {
  self->endInsertColumns();
}

//  void QSqlQueryModel::beginRemoveColumns(const QModelIndex &parent, int
//      first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel18beginRemoveColumnsERK11QModelIndexii(
    QSqlQueryModel *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginRemoveColumns(*parent, first, last);
}

//  void QSqlQueryModel::endRemoveColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel16endRemoveColumnsEv(QSqlQueryModel *self) {
  self->endRemoveColumns();
}

//  void QSqlQueryModel::beginResetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel15beginResetModelEv(QSqlQueryModel *self) {
  self->beginResetModel();
}

//  void QSqlQueryModel::endResetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel13endResetModelEv(QSqlQueryModel *self) {
  self->endResetModel();
}

//  void QSqlQueryModel::queryChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel11queryChangeEv(QSqlQueryModel *self) {
  self->queryChange();
}

//  QModelIndex QSqlQueryModel::indexInQuery(const QModelIndex &item) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK14QSqlQueryModel12indexInQueryERK11QModelIndex(
    const QSqlQueryModel *self,
    const QModelIndex *item) {
  return new QModelIndex(self->indexInQuery(*item));
}

//  void QSqlQueryModel::setLastError(const QSqlError &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSqlQueryModel12setLastErrorERK9QSqlError(
    QSqlQueryModel *self,
    const QSqlError *error) {
  self->setLastError(*error);
}

//  a Python function taken by a CuteQSqlQueryModel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSqlQueryModel(
    QSqlQueryModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSqlQueryModel *>(self)->take(key, call);
}

//  int QSqlQueryModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QSqlQueryModel8rowCountERK11QModelIndex(
    const QSqlQueryModel *self,
    const QModelIndex *parent) {
  return self->QSqlQueryModel::rowCount(*parent);
}

//  int QSqlQueryModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QSqlQueryModel11columnCountERK11QModelIndex(
    const QSqlQueryModel *self,
    const QModelIndex *parent) {
  return self->QSqlQueryModel::columnCount(*parent);
}

//  QVariant QSqlQueryModel::data(const QModelIndex &item, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QSqlQueryModel4dataERK11QModelIndexi(
    const QSqlQueryModel *self,
    const QModelIndex *item,
    int role) {
  return new QVariant(self->QSqlQueryModel::data(*item, role));
}

//  QVariant QSqlQueryModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QSqlQueryModel10headerDataEiN2Qt11OrientationEi(
    const QSqlQueryModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QSqlQueryModel::headerData(
          section,
          orientation,
          role));
}

//  bool QSqlQueryModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlQueryModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QSqlQueryModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->QSqlQueryModel::setHeaderData(
      section,
      orientation,
      *value,
      role);
}

//  bool QSqlQueryModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlQueryModel13insertColumnsEiiRK11QModelIndex(
    QSqlQueryModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QSqlQueryModel::insertColumns(column, count, *parent);
}

//  bool QSqlQueryModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QSqlQueryModel13removeColumnsEiiRK11QModelIndex(
    QSqlQueryModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QSqlQueryModel::removeColumns(column, count, *parent);
}

//  void QSqlQueryModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlQueryModel5clearEv(QSqlQueryModel *self) {
  self->QSqlQueryModel::clear();
}

//  void QSqlQueryModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlQueryModel9fetchMoreERK11QModelIndex(
    QSqlQueryModel *self,
    const QModelIndex *parent) {
  self->QSqlQueryModel::fetchMore(*parent);
}

//  bool QSqlQueryModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QSqlQueryModel12canFetchMoreERK11QModelIndex(
    const QSqlQueryModel *self,
    const QModelIndex *parent) {
  return self->QSqlQueryModel::canFetchMore(*parent);
}

//  void QSqlQueryModel::queryChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSqlQueryModel11queryChangeEv(QSqlQueryModel *self) {
  static_cast<OwnQSqlQueryModel *>(self)->OwnQSqlQueryModel::queryChange();
}

//  QModelIndex QSqlQueryModel::indexInQuery(const QModelIndex &item) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK14QSqlQueryModel12indexInQueryERK11QModelIndex(
    const QSqlQueryModel *self,
    const QModelIndex *item) {
  return new QModelIndex(
      static_cast<const OwnQSqlQueryModel *>(self)->OwnQSqlQueryModel::indexInQuery(
          *item));
}

#endif  // QT_CONFIG(sqlmodel)
#endif  // QT_CONFIG(sqlmodel)
