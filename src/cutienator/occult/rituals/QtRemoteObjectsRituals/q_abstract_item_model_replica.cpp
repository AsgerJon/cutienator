//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectabstractitemmodelreplica.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtRemoteObjects/qremoteobjectabstractitemmodelreplica.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QAbstractItemModelReplica that Python can take functions over in. Every QAbstractItemModelReplica
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelReplicaCall0)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall1)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractItemModelReplicaCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractItemModelReplicaCall3)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractItemModelReplicaCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractItemModelReplicaCall6)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQAbstractItemModelReplicaCall7)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractItemModelReplicaCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractItemModelReplicaCall9)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall10)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall11)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall12)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall13)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractItemModelReplicaCall14)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractItemModelReplicaCall15)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall16)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall17)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall18)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall20)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall21)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelReplicaCall22)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall23)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelReplicaCall24)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractItemModelReplicaCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQAbstractItemModelReplicaCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelReplicaCall27)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelReplicaCall28)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelReplicaCall29)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractItemModelReplicaCall30)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractItemModelReplicaCall31)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelReplicaCall32)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelReplicaCall33)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelReplicaCall34)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelReplicaCall35)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelReplicaCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractItemModelReplica : public QAbstractItemModelReplica {
public:
  using QAbstractItemModelReplica::QAbstractItemModelReplica;
  void *taken[37] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModelReplica::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall0 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall0>(taken[0]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModelReplica::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModelReplica::setData(const QModelIndex &index,
  //      const QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall1 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall1>(taken[1]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModelReplica::setData(index, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModelReplica::parent(const QModelIndex
  //      &index) const
  QModelIndex parent(const QModelIndex &index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall2 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall2>(taken[2]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModelReplica::parent(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModelReplica::index(int row, int column,
  //      const QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall3 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall3>(taken[3]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModelReplica::index(row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModelReplica::hasChildren(const QModelIndex
  //      &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall4 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall4>(taken[4]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModelReplica::hasChildren(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractItemModelReplica::rowCount(const QModelIndex &parent)
  //      const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall5 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall5>(taken[5]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModelReplica::rowCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractItemModelReplica::columnCount(const QModelIndex &parent)
  //      const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall6 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall6>(taken[6]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModelReplica::columnCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QAbstractItemModelReplica::headerData(int section,
  //      Qt::Orientation orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall7 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall7>(taken[7]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModelReplica::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::ItemFlags QAbstractItemModelReplica::flags(const QModelIndex
  //      &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall8 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall8>(taken[8]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QAbstractItemModelReplica::flags(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall9 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall9>(taken[9]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall10 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall10>(taken[10]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall11 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall12 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall12>(taken[12]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall13 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall13>(taken[13]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall14 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall15 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall16 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall16>(taken[16]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall17 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall17>(taken[17]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertColumns(column, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall18 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall18>(taken[18]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeRows(row, count, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall19 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall19>(taken[19]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeColumns(column, count, parent);
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
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall20 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall21 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall21>(taken[21]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall22 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall22>(taken[22]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractItemModel::fetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall23 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall23>(taken[23]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall24 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall24>(taken[24]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractItemModel::sort(column, order);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall25 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall25>(taken[25]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall26 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall26>(taken[26]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::span(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall27 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall27>(taken[27]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall28 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall29 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall30 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall30>(taken[30]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall31 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall31>(taken[31]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall32 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall33 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall34 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[35]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall35 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall35>(taken[35]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[36]) {
      int handled = 0;
      CuteQAbstractItemModelReplicaCall36 call = reinterpret_cast<CuteQAbstractItemModelReplicaCall36>(taken[36]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractItemModelReplica::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QAbstractItemModelReplica10metaObjectEv(
    const QAbstractItemModelReplica *self) {
  return self->metaObject();
}

//  QString QAbstractItemModelReplica::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QAbstractItemModelReplica2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractItemModelReplica::tr(s, c, n));
}

//  QAbstractItemModelReplica::~QAbstractItemModelReplica()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelReplicaD1Ev(
    QAbstractItemModelReplica *self) {
  delete self;
}

//  QItemSelectionModel *QAbstractItemModelReplica::selectionModel() const
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZNK25QAbstractItemModelReplica14selectionModelEv(
    const QAbstractItemModelReplica *self) {
  return self->selectionModel();
}

//  QVariant QAbstractItemModelReplica::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAbstractItemModelReplica4dataERK11QModelIndexi(
    const QAbstractItemModelReplica *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  void QAbstractItemModelReplica::multiData(const QModelIndex &index,
//      QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QAbstractItemModelReplica9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QAbstractItemModelReplica *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->multiData(*index, *roleDataSpan);
}

//  bool QAbstractItemModelReplica::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractItemModelReplica7setDataERK11QModelIndexRK8QVarianti(
    QAbstractItemModelReplica *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QModelIndex QAbstractItemModelReplica::parent(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK25QAbstractItemModelReplica6parentERK11QModelIndex(
    const QAbstractItemModelReplica *self,
    const QModelIndex *index) {
  return new QModelIndex(self->parent(*index));
}

//  QModelIndex QAbstractItemModelReplica::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK25QAbstractItemModelReplica5indexEiiRK11QModelIndex(
    const QAbstractItemModelReplica *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  bool QAbstractItemModelReplica::hasChildren(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAbstractItemModelReplica11hasChildrenERK11QModelIndex(
    const QAbstractItemModelReplica *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  int QAbstractItemModelReplica::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAbstractItemModelReplica8rowCountERK11QModelIndex(
    const QAbstractItemModelReplica *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QAbstractItemModelReplica::columnCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAbstractItemModelReplica11columnCountERK11QModelIndex(
    const QAbstractItemModelReplica *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QVariant QAbstractItemModelReplica::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAbstractItemModelReplica10headerDataEiN2Qt11OrientationEi(
    const QAbstractItemModelReplica *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  Qt::ItemFlags QAbstractItemModelReplica::flags(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAbstractItemModelReplica5flagsERK11QModelIndex(
    const QAbstractItemModelReplica *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  QHash<int, QByteArray> QAbstractItemModelReplica::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK25QAbstractItemModelReplica9roleNamesEv(
    const QAbstractItemModelReplica *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  bool QAbstractItemModelReplica::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAbstractItemModelReplica13isInitializedEv(
    const QAbstractItemModelReplica *self) {
  return self->isInitialized();
}

//  bool QAbstractItemModelReplica::hasData(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAbstractItemModelReplica7hasDataERK11QModelIndexi(
    const QAbstractItemModelReplica *self,
    const QModelIndex *index,
    int role) {
  return self->hasData(*index, role);
}

//  void QAbstractItemModelReplica::setRootCacheSize(size_t rootCacheSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractItemModelReplica16setRootCacheSizeEm(
    QAbstractItemModelReplica *self,
    size_t rootCacheSize) {
  self->setRootCacheSize(rootCacheSize);
}

//  a Python function taken by a CuteQAbstractItemModelReplica, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractItemModelReplica(
    QAbstractItemModelReplica *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractItemModelReplica *>(self)->take(key, call);
}

//  void QAbstractItemModelReplica::multiData(const QModelIndex &index,
//      QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK25QAbstractItemModelReplica9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QAbstractItemModelReplica *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->QAbstractItemModelReplica::multiData(*index, *roleDataSpan);
}

//  bool QAbstractItemModelReplica::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QAbstractItemModelReplica7setDataERK11QModelIndexRK8QVarianti(
    QAbstractItemModelReplica *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QAbstractItemModelReplica::setData(*index, *value, role);
}

//  QModelIndex QAbstractItemModelReplica::parent(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK25QAbstractItemModelReplica6parentERK11QModelIndex(
    const QAbstractItemModelReplica *self,
    const QModelIndex *index) {
  return new QModelIndex(self->QAbstractItemModelReplica::parent(*index));
}

//  QModelIndex QAbstractItemModelReplica::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK25QAbstractItemModelReplica5indexEiiRK11QModelIndex(
    const QAbstractItemModelReplica *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QAbstractItemModelReplica::index(
          row,
          column,
          *parent));
}

//  bool QAbstractItemModelReplica::hasChildren(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QAbstractItemModelReplica11hasChildrenERK11QModelIndex(
    const QAbstractItemModelReplica *self,
    const QModelIndex *parent) {
  return self->QAbstractItemModelReplica::hasChildren(*parent);
}

//  int QAbstractItemModelReplica::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QAbstractItemModelReplica8rowCountERK11QModelIndex(
    const QAbstractItemModelReplica *self,
    const QModelIndex *parent) {
  return self->QAbstractItemModelReplica::rowCount(*parent);
}

//  int QAbstractItemModelReplica::columnCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QAbstractItemModelReplica11columnCountERK11QModelIndex(
    const QAbstractItemModelReplica *self,
    const QModelIndex *parent) {
  return self->QAbstractItemModelReplica::columnCount(*parent);
}

//  QVariant QAbstractItemModelReplica::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAbstractItemModelReplica10headerDataEiN2Qt11OrientationEi(
    const QAbstractItemModelReplica *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QAbstractItemModelReplica::headerData(
          section,
          orientation,
          role));
}

//  Qt::ItemFlags QAbstractItemModelReplica::flags(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QAbstractItemModelReplica5flagsERK11QModelIndex(
    const QAbstractItemModelReplica *self,
    const QModelIndex *index) {
  return static_cast<int>(
      self->QAbstractItemModelReplica::flags(
          *index).toInt());
}
