//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qconcatenatetablesproxymodel.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(concatenatetablesproxymodel) && QT_CONFIG(proxymodel)
#if QT_CONFIG(concatenatetablesproxymodel)
#include <QtCore/qconcatenatetablesproxymodel.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QConcatenateTablesProxyModel that Python can take functions over in. Every QConcatenateTablesProxyModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef const QVariant * (*CuteQConcatenateTablesProxyModelCall0)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall1)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef int (*CuteQConcatenateTablesProxyModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef const QModelIndex * (*CuteQConcatenateTablesProxyModelCall3)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef const QModelIndex * (*CuteQConcatenateTablesProxyModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef int (*CuteQConcatenateTablesProxyModelCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef const QVariant * (*CuteQConcatenateTablesProxyModelCall6)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef int (*CuteQConcatenateTablesProxyModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall8)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall9)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
typedef const QSize * (*CuteQConcatenateTablesProxyModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQConcatenateTablesProxyModelCall11)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall13)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQConcatenateTablesProxyModelCall15)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQConcatenateTablesProxyModelCall16)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall17)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall18)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall20)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall21)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQConcatenateTablesProxyModelCall23)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQConcatenateTablesProxyModelCall25)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQConcatenateTablesProxyModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQConcatenateTablesProxyModelCall27)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQConcatenateTablesProxyModelCall28)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQConcatenateTablesProxyModelCall29)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQConcatenateTablesProxyModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQConcatenateTablesProxyModelCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQConcatenateTablesProxyModelCall32)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQConcatenateTablesProxyModelCall33)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQConcatenateTablesProxyModelCall34)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQConcatenateTablesProxyModelCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQConcatenateTablesProxyModelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQConcatenateTablesProxyModelCall37)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQConcatenateTablesProxyModel : public QConcatenateTablesProxyModel {
public:
  using QConcatenateTablesProxyModel::QConcatenateTablesProxyModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  QVariant QConcatenateTablesProxyModel::data(const QModelIndex &index,
  //      int role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall0 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall0>(taken[0]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QConcatenateTablesProxyModel::data(index, role);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  bool QConcatenateTablesProxyModel::setData(const QModelIndex &index,
  //      const QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[1]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall1 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall1>(taken[1]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QConcatenateTablesProxyModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  Qt::ItemFlags QConcatenateTablesProxyModel::flags(const QModelIndex
  //      &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall2 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall2>(taken[2]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QConcatenateTablesProxyModel::flags(index);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  QModelIndex QConcatenateTablesProxyModel::index(int row, int column,
  //      const QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall3 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall3>(taken[3]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QConcatenateTablesProxyModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  QModelIndex QConcatenateTablesProxyModel::parent(const QModelIndex
  //      &index) const
  QModelIndex parent(const QModelIndex &index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall4 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall4>(taken[4]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QConcatenateTablesProxyModel::parent(index);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  int QConcatenateTablesProxyModel::rowCount(const QModelIndex &parent)
  //      const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall5 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall5>(taken[5]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QConcatenateTablesProxyModel::rowCount(parent);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  QVariant QConcatenateTablesProxyModel::headerData(int section,
  //      Qt::Orientation orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall6 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall6>(taken[6]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QConcatenateTablesProxyModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  int QConcatenateTablesProxyModel::columnCount(const QModelIndex
  //      &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall7 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall7>(taken[7]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QConcatenateTablesProxyModel::columnCount(parent);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  bool QConcatenateTablesProxyModel::canDropMimeData(const QMimeData
  //      *data, Qt::DropAction action, int row, int column, const
  //      QModelIndex &parent) const
  bool canDropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall8 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall8>(taken[8]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QConcatenateTablesProxyModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  bool QConcatenateTablesProxyModel::dropMimeData(const QMimeData
  //      *data, Qt::DropAction action, int row, int column, const
  //      QModelIndex &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[9]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall9 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall9>(taken[9]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QConcatenateTablesProxyModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(concatenatetablesproxymodel)
  //  QSize QConcatenateTablesProxyModel::span(const QModelIndex &index)
  //      const
  QSize span(const QModelIndex &index) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall10 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall10>(taken[10]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QConcatenateTablesProxyModel::span(index);
  }
#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall11 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall11>(taken[11]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall12 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall12>(taken[12]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::hasChildren(parent);
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
    if (taken[13]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall13 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall13>(taken[13]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[14]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall14 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall14>(taken[14]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::clearItemData(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall15 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall16 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall17 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall18 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall19 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall20 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall21 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall22 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall22>(taken[22]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[23]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall23 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall24 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall24>(taken[24]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[25]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall25 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall25>(taken[25]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractItemModel::sort(column, order);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall26 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall26>(taken[26]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall27 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall27>(taken[27]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[28]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall28 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall28>(taken[28]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[29]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall29 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[30]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall30 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall31 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall31>(taken[31]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall32 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall32>(taken[32]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall33 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall34 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall35 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[36]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall36 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall36>(taken[36]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[37]) {
      int handled = 0;
      CuteQConcatenateTablesProxyModelCall37 call = reinterpret_cast<CuteQConcatenateTablesProxyModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QConcatenateTablesProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QConcatenateTablesProxyModel10metaObjectEv(
    const QConcatenateTablesProxyModel *self) {
  return self->metaObject();
}

//  void *QConcatenateTablesProxyModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QConcatenateTablesProxyModel11qt_metacastEPKc(
    QConcatenateTablesProxyModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QConcatenateTablesProxyModel::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QConcatenateTablesProxyModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QConcatenateTablesProxyModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QConcatenateTablesProxyModel::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QConcatenateTablesProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QConcatenateTablesProxyModel::tr(s, c, n));
}

//  QConcatenateTablesProxyModel::QConcatenateTablesProxyModel(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QConcatenateTablesProxyModel *ritual_ZN28QConcatenateTablesProxyModelC1EP7QObject(
    QObject *parent) {
  return new CuteQConcatenateTablesProxyModel(parent);
}

//  QConcatenateTablesProxyModel::~QConcatenateTablesProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QConcatenateTablesProxyModelD1Ev(
    QConcatenateTablesProxyModel *self) {
  delete self;
}

//  QList<QAbstractItemModel *> QConcatenateTablesProxyModel::sourceModels()
//      const
extern "C" Q_DECL_EXPORT
QList<QAbstractItemModel *> *ritual_ZNK28QConcatenateTablesProxyModel12sourceModelsEv(
    const QConcatenateTablesProxyModel *self) {
  return new QList<QAbstractItemModel *>(self->sourceModels());
}

//  void QConcatenateTablesProxyModel::addSourceModel(QAbstractItemModel
//      *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QConcatenateTablesProxyModel14addSourceModelEP18QAbstractItemModel(
    QConcatenateTablesProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->addSourceModel(sourceModel);
}

//  void QConcatenateTablesProxyModel::removeSourceModel(QAbstractItemModel
//      *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QConcatenateTablesProxyModel17removeSourceModelEP18QAbstractItemModel(
    QConcatenateTablesProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->removeSourceModel(sourceModel);
}

//  QModelIndex QConcatenateTablesProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK28QConcatenateTablesProxyModel13mapFromSourceERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QModelIndex QConcatenateTablesProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK28QConcatenateTablesProxyModel11mapToSourceERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QVariant QConcatenateTablesProxyModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK28QConcatenateTablesProxyModel4dataERK11QModelIndexi(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QConcatenateTablesProxyModel::setData(const QModelIndex &index,
//      const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QConcatenateTablesProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QConcatenateTablesProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QMap<int, QVariant> QConcatenateTablesProxyModel::itemData(const
//      QModelIndex &proxyIndex) const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK28QConcatenateTablesProxyModel8itemDataERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QMap<int, QVariant>(self->itemData(*proxyIndex));
}

//  bool QConcatenateTablesProxyModel::setItemData(const QModelIndex &index,
//      const QMap<int, QVariant> &roles)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QConcatenateTablesProxyModel11setItemDataERK11QModelIndexRK4QMapIi8QVariantE(
    QConcatenateTablesProxyModel *self,
    const QModelIndex *index,
    const QMap<int, QVariant> *roles) {
  return self->setItemData(*index, *roles);
}

//  Qt::ItemFlags QConcatenateTablesProxyModel::flags(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QConcatenateTablesProxyModel5flagsERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  QModelIndex QConcatenateTablesProxyModel::index(int row, int column,
//      const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK28QConcatenateTablesProxyModel5indexEiiRK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QConcatenateTablesProxyModel::parent(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK28QConcatenateTablesProxyModel6parentERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->parent(*index));
}

//  int QConcatenateTablesProxyModel::rowCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QConcatenateTablesProxyModel8rowCountERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QConcatenateTablesProxyModel::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK28QConcatenateTablesProxyModel10headerDataEiN2Qt11OrientationEi(
    const QConcatenateTablesProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  int QConcatenateTablesProxyModel::columnCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QConcatenateTablesProxyModel11columnCountERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QStringList QConcatenateTablesProxyModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QConcatenateTablesProxyModel9mimeTypesEv(
    const QConcatenateTablesProxyModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  QMimeData *QConcatenateTablesProxyModel::mimeData(const QModelIndexList
//      &indexes) const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK28QConcatenateTablesProxyModel8mimeDataERK5QListI11QModelIndexE(
    const QConcatenateTablesProxyModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  bool QConcatenateTablesProxyModel::canDropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QConcatenateTablesProxyModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->canDropMimeData(data, action, row, column, *parent);
}

//  bool QConcatenateTablesProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QConcatenateTablesProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QConcatenateTablesProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  QSize QConcatenateTablesProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK28QConcatenateTablesProxyModel4spanERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  QHash<int, QByteArray> QConcatenateTablesProxyModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK28QConcatenateTablesProxyModel9roleNamesEv(
    const QConcatenateTablesProxyModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QConcatenateTablesProxyModelPrivate
//      *QConcatenateTablesProxyModel::d_func()
extern "C" Q_DECL_EXPORT
QConcatenateTablesProxyModelPrivate *ritual_ZN28QConcatenateTablesProxyModel6d_funcEv(
    QConcatenateTablesProxyModel *self) {
  return self->d_func();
}

//  const QConcatenateTablesProxyModelPrivate
//      *QConcatenateTablesProxyModel::d_func() const
extern "C" Q_DECL_EXPORT
const QConcatenateTablesProxyModelPrivate *ritual_ZNK28QConcatenateTablesProxyModel6d_funcEv(
    const QConcatenateTablesProxyModel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQConcatenateTablesProxyModel, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QConcatenateTablesProxyModel(
    QConcatenateTablesProxyModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQConcatenateTablesProxyModel *>(self)->take(key, call);
}

//  QVariant QConcatenateTablesProxyModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK28QConcatenateTablesProxyModel4dataERK11QModelIndexi(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(
      self->QConcatenateTablesProxyModel::data(
          *index,
          role));
}

//  bool QConcatenateTablesProxyModel::setData(const QModelIndex &index,
//      const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QConcatenateTablesProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QConcatenateTablesProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QConcatenateTablesProxyModel::setData(*index, *value, role);
}

//  Qt::ItemFlags QConcatenateTablesProxyModel::flags(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK28QConcatenateTablesProxyModel5flagsERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index) {
  return static_cast<int>(
      self->QConcatenateTablesProxyModel::flags(
          *index).toInt());
}

//  QModelIndex QConcatenateTablesProxyModel::index(int row, int column,
//      const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK28QConcatenateTablesProxyModel5indexEiiRK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QConcatenateTablesProxyModel::index(
          row,
          column,
          *parent));
}

//  QModelIndex QConcatenateTablesProxyModel::parent(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK28QConcatenateTablesProxyModel6parentERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->QConcatenateTablesProxyModel::parent(*index));
}

//  int QConcatenateTablesProxyModel::rowCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK28QConcatenateTablesProxyModel8rowCountERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *parent) {
  return self->QConcatenateTablesProxyModel::rowCount(*parent);
}

//  QVariant QConcatenateTablesProxyModel::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK28QConcatenateTablesProxyModel10headerDataEiN2Qt11OrientationEi(
    const QConcatenateTablesProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QConcatenateTablesProxyModel::headerData(
          section,
          orientation,
          role));
}

//  int QConcatenateTablesProxyModel::columnCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK28QConcatenateTablesProxyModel11columnCountERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *parent) {
  return self->QConcatenateTablesProxyModel::columnCount(*parent);
}

//  bool QConcatenateTablesProxyModel::canDropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK28QConcatenateTablesProxyModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QConcatenateTablesProxyModel::canDropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  bool QConcatenateTablesProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QConcatenateTablesProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QConcatenateTablesProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QConcatenateTablesProxyModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  QSize QConcatenateTablesProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK28QConcatenateTablesProxyModel4spanERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->QConcatenateTablesProxyModel::span(*index));
}

#endif  // QT_CONFIG(concatenatetablesproxymodel)
#endif  // QT_CONFIG(concatenatetablesproxymodel) && QT_CONFIG(proxymodel)
