//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qstandarditemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(standarditemmodel)
#include <QtGui/qstandarditemmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QStandardItemModel that Python can take functions over in. Every QStandardItemModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QModelIndex * (*CuteQStandardItemModelCall0)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QModelIndex * (*CuteQStandardItemModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*CuteQStandardItemModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*CuteQStandardItemModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQStandardItemModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QVariant * (*CuteQStandardItemModelCall5)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef void (*CuteQStandardItemModelCall6)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQStandardItemModelCall7)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQStandardItemModelCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef const QVariant * (*CuteQStandardItemModelCall9)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQStandardItemModelCall10)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQStandardItemModelCall11)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQStandardItemModelCall12)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQStandardItemModelCall13)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQStandardItemModelCall14)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*CuteQStandardItemModelCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef int (*CuteQStandardItemModelCall16)(const void *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef void (*CuteQStandardItemModelCall17)(const void *, int, int, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
typedef bool (*CuteQStandardItemModelCall18)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQStandardItemModelCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQStandardItemModelCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQStandardItemModelCall21)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQStandardItemModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQStandardItemModelCall23)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQStandardItemModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQStandardItemModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQStandardItemModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQStandardItemModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQStandardItemModelCall28)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQStandardItemModelCall29)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQStandardItemModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStandardItemModelCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStandardItemModelCall32)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStandardItemModelCall33)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStandardItemModelCall34)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStandardItemModelCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStandardItemModelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStandardItemModelCall37)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQStandardItemModel : public QStandardItemModel {
public:
  using QStandardItemModel::QStandardItemModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
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
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
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
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
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
#if QT_CONFIG(standarditemmodel)
  //  QModelIndex QStandardItemModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQStandardItemModelCall0 call = reinterpret_cast<CuteQStandardItemModelCall0>(taken[0]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  QModelIndex QStandardItemModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQStandardItemModelCall1 call = reinterpret_cast<CuteQStandardItemModelCall1>(taken[1]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::parent(child);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  int QStandardItemModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQStandardItemModelCall2 call = reinterpret_cast<CuteQStandardItemModelCall2>(taken[2]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::rowCount(parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  int QStandardItemModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQStandardItemModelCall3 call = reinterpret_cast<CuteQStandardItemModelCall3>(taken[3]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::columnCount(parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQStandardItemModelCall4 call = reinterpret_cast<CuteQStandardItemModelCall4>(taken[4]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  QVariant QStandardItemModel::data(const QModelIndex &index, int role)
  //      const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQStandardItemModelCall5 call = reinterpret_cast<CuteQStandardItemModelCall5>(taken[5]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::data(index, role);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  void QStandardItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQStandardItemModelCall6 call = reinterpret_cast<CuteQStandardItemModelCall6>(taken[6]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QStandardItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[7]) {
      int handled = 0;
      CuteQStandardItemModelCall7 call = reinterpret_cast<CuteQStandardItemModelCall7>(taken[7]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[8]) {
      int handled = 0;
      CuteQStandardItemModelCall8 call = reinterpret_cast<CuteQStandardItemModelCall8>(taken[8]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::clearItemData(index);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  QVariant QStandardItemModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQStandardItemModelCall9 call = reinterpret_cast<CuteQStandardItemModelCall9>(taken[9]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QStandardItemModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[10]) {
      int handled = 0;
      CuteQStandardItemModelCall10 call = reinterpret_cast<CuteQStandardItemModelCall10>(taken[10]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[11]) {
      int handled = 0;
      CuteQStandardItemModelCall11 call = reinterpret_cast<CuteQStandardItemModelCall11>(taken[11]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[12]) {
      int handled = 0;
      CuteQStandardItemModelCall12 call = reinterpret_cast<CuteQStandardItemModelCall12>(taken[12]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::insertColumns(column, count, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[13]) {
      int handled = 0;
      CuteQStandardItemModelCall13 call = reinterpret_cast<CuteQStandardItemModelCall13>(taken[13]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::removeRows(row, count, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[14]) {
      int handled = 0;
      CuteQStandardItemModelCall14 call = reinterpret_cast<CuteQStandardItemModelCall14>(taken[14]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  Qt::ItemFlags QStandardItemModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQStandardItemModelCall15 call = reinterpret_cast<CuteQStandardItemModelCall15>(taken[15]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QStandardItemModel::flags(index);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  Qt::DropActions QStandardItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQStandardItemModelCall16 call = reinterpret_cast<CuteQStandardItemModelCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QStandardItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  void QStandardItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[17]) {
      int handled = 0;
      CuteQStandardItemModelCall17 call = reinterpret_cast<CuteQStandardItemModelCall17>(taken[17]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QStandardItemModel::sort(column, order);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(standarditemmodel)
  //  bool QStandardItemModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[18]) {
      int handled = 0;
      CuteQStandardItemModelCall18 call = reinterpret_cast<CuteQStandardItemModelCall18>(taken[18]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QStandardItemModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(standarditemmodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQStandardItemModelCall19 call = reinterpret_cast<CuteQStandardItemModelCall19>(taken[19]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::sibling(row, column, idx);
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
      CuteQStandardItemModelCall20 call = reinterpret_cast<CuteQStandardItemModelCall20>(taken[20]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQStandardItemModelCall21 call = reinterpret_cast<CuteQStandardItemModelCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQStandardItemModelCall22 call = reinterpret_cast<CuteQStandardItemModelCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQStandardItemModelCall23 call = reinterpret_cast<CuteQStandardItemModelCall23>(taken[23]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[24]) {
      int handled = 0;
      CuteQStandardItemModelCall24 call = reinterpret_cast<CuteQStandardItemModelCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQStandardItemModelCall25 call = reinterpret_cast<CuteQStandardItemModelCall25>(taken[25]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQStandardItemModelCall26 call = reinterpret_cast<CuteQStandardItemModelCall26>(taken[26]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQStandardItemModelCall27 call = reinterpret_cast<CuteQStandardItemModelCall27>(taken[27]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::span(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[28]) {
      int handled = 0;
      CuteQStandardItemModelCall28 call = reinterpret_cast<CuteQStandardItemModelCall28>(taken[28]);
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
      CuteQStandardItemModelCall29 call = reinterpret_cast<CuteQStandardItemModelCall29>(taken[29]);
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
      CuteQStandardItemModelCall30 call = reinterpret_cast<CuteQStandardItemModelCall30>(taken[30]);
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
      CuteQStandardItemModelCall31 call = reinterpret_cast<CuteQStandardItemModelCall31>(taken[31]);
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
      CuteQStandardItemModelCall32 call = reinterpret_cast<CuteQStandardItemModelCall32>(taken[32]);
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
      CuteQStandardItemModelCall33 call = reinterpret_cast<CuteQStandardItemModelCall33>(taken[33]);
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
      CuteQStandardItemModelCall34 call = reinterpret_cast<CuteQStandardItemModelCall34>(taken[34]);
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
      CuteQStandardItemModelCall35 call = reinterpret_cast<CuteQStandardItemModelCall35>(taken[35]);
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
      CuteQStandardItemModelCall36 call = reinterpret_cast<CuteQStandardItemModelCall36>(taken[36]);
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
      CuteQStandardItemModelCall37 call = reinterpret_cast<CuteQStandardItemModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QStandardItemModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QStandardItemModel10metaObjectEv(
    const QStandardItemModel *self) {
  return self->metaObject();
}

//  QString QStandardItemModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QStandardItemModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStandardItemModel::tr(s, c, n));
}

//  QStandardItemModel::QStandardItemModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QStandardItemModel *ritual_ZN18QStandardItemModelC1EP7QObject(
    QObject *parent) {
  return new CuteQStandardItemModel(parent);
}

//  QStandardItemModel::QStandardItemModel(int rows, int columns, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QStandardItemModel *ritual_ZN18QStandardItemModelC1EiiP7QObject(
    int rows,
    int columns,
    QObject *parent) {
  return new CuteQStandardItemModel(rows, columns, parent);
}

//  QStandardItemModel::~QStandardItemModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModelD1Ev(QStandardItemModel *self) {
  delete self;
}

//  void QStandardItemModel::setItemRoleNames(const QHash<int, QByteArray>
//      &roleNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel16setItemRoleNamesERK5QHashIi10QByteArrayE(
    QStandardItemModel *self,
    const QHash<int, QByteArray> *roleNames) {
  self->setItemRoleNames(*roleNames);
}

//  QHash<int, QByteArray> QStandardItemModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK18QStandardItemModel9roleNamesEv(
    const QStandardItemModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QModelIndex QStandardItemModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QStandardItemModel5indexEiiRK11QModelIndex(
    const QStandardItemModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QStandardItemModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QStandardItemModel6parentERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  int QStandardItemModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QStandardItemModel8rowCountERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QStandardItemModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QStandardItemModel11columnCountERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  bool QStandardItemModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QStandardItemModel11hasChildrenERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QVariant QStandardItemModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QStandardItemModel4dataERK11QModelIndexi(
    const QStandardItemModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  void QStandardItemModel::multiData(const QModelIndex &index,
//      QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QStandardItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QStandardItemModel *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->multiData(*index, *roleDataSpan);
}

//  bool QStandardItemModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel7setDataERK11QModelIndexRK8QVarianti(
    QStandardItemModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  bool QStandardItemModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel13clearItemDataERK11QModelIndex(
    QStandardItemModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  QVariant QStandardItemModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QStandardItemModel10headerDataEiN2Qt11OrientationEi(
    const QStandardItemModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QStandardItemModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QStandardItemModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  bool QStandardItemModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel10insertRowsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QStandardItemModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel13insertColumnsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QStandardItemModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel10removeRowsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QStandardItemModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel13removeColumnsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  Qt::ItemFlags QStandardItemModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QStandardItemModel5flagsERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  Qt::DropActions QStandardItemModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QStandardItemModel20supportedDropActionsEv(
    const QStandardItemModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  QMap<int, QVariant> QStandardItemModel::itemData(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK18QStandardItemModel8itemDataERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *index) {
  return new QMap<int, QVariant>(self->itemData(*index));
}

//  bool QStandardItemModel::setItemData(const QModelIndex &index, const
//      QMap<int, QVariant> &roles)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel11setItemDataERK11QModelIndexRK4QMapIi8QVariantE(
    QStandardItemModel *self,
    const QModelIndex *index,
    const QMap<int, QVariant> *roles) {
  return self->setItemData(*index, *roles);
}

//  void QStandardItemModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel5clearEv(QStandardItemModel *self) {
  self->clear();
}

//  void QStandardItemModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel4sortEiN2Qt9SortOrderE(
    QStandardItemModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QStandardItem *QStandardItemModel::itemFromIndex(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK18QStandardItemModel13itemFromIndexERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *index) {
  return self->itemFromIndex(*index);
}

//  QModelIndex QStandardItemModel::indexFromItem(const QStandardItem *item)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QStandardItemModel13indexFromItemEPK13QStandardItem(
    const QStandardItemModel *self,
    const QStandardItem *item) {
  return new QModelIndex(self->indexFromItem(item));
}

//  QStandardItem *QStandardItemModel::item(int row, int column) const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK18QStandardItemModel4itemEii(
    const QStandardItemModel *self,
    int row,
    int column) {
  return self->item(row, column);
}

//  void QStandardItemModel::setItem(int row, int column, QStandardItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel7setItemEiiP13QStandardItem(
    QStandardItemModel *self,
    int row,
    int column,
    QStandardItem *item) {
  self->setItem(row, column, item);
}

//  void QStandardItemModel::setItem(int row, QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel7setItemEiP13QStandardItem(
    QStandardItemModel *self,
    int row,
    QStandardItem *item) {
  self->setItem(row, item);
}

//  QStandardItem *QStandardItemModel::invisibleRootItem() const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK18QStandardItemModel17invisibleRootItemEv(
    const QStandardItemModel *self) {
  return self->invisibleRootItem();
}

//  QStandardItem *QStandardItemModel::horizontalHeaderItem(int column) const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK18QStandardItemModel20horizontalHeaderItemEi(
    const QStandardItemModel *self,
    int column) {
  return self->horizontalHeaderItem(column);
}

//  void QStandardItemModel::setHorizontalHeaderItem(int column,
//      QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel23setHorizontalHeaderItemEiP13QStandardItem(
    QStandardItemModel *self,
    int column,
    QStandardItem *item) {
  self->setHorizontalHeaderItem(column, item);
}

//  QStandardItem *QStandardItemModel::verticalHeaderItem(int row) const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK18QStandardItemModel18verticalHeaderItemEi(
    const QStandardItemModel *self,
    int row) {
  return self->verticalHeaderItem(row);
}

//  void QStandardItemModel::setVerticalHeaderItem(int row, QStandardItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel21setVerticalHeaderItemEiP13QStandardItem(
    QStandardItemModel *self,
    int row,
    QStandardItem *item) {
  self->setVerticalHeaderItem(row, item);
}

//  void QStandardItemModel::setHorizontalHeaderLabels(const QStringList
//      &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel25setHorizontalHeaderLabelsERK5QListI7QStringE(
    QStandardItemModel *self,
    const QList<QString> *labels) {
  self->setHorizontalHeaderLabels(*labels);
}

//  void QStandardItemModel::setVerticalHeaderLabels(const QStringList
//      &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel23setVerticalHeaderLabelsERK5QListI7QStringE(
    QStandardItemModel *self,
    const QList<QString> *labels) {
  self->setVerticalHeaderLabels(*labels);
}

//  void QStandardItemModel::setRowCount(int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel11setRowCountEi(
    QStandardItemModel *self,
    int rows) {
  self->setRowCount(rows);
}

//  void QStandardItemModel::setColumnCount(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel14setColumnCountEi(
    QStandardItemModel *self,
    int columns) {
  self->setColumnCount(columns);
}

//  void QStandardItemModel::appendRow(const QList<QStandardItem *> &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel9appendRowERK5QListIP13QStandardItemE(
    QStandardItemModel *self,
    const QList<QStandardItem *> *items) {
  self->appendRow(*items);
}

//  void QStandardItemModel::appendColumn(const QList<QStandardItem *>
//      &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel12appendColumnERK5QListIP13QStandardItemE(
    QStandardItemModel *self,
    const QList<QStandardItem *> *items) {
  self->appendColumn(*items);
}

//  void QStandardItemModel::appendRow(QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel9appendRowEP13QStandardItem(
    QStandardItemModel *self,
    QStandardItem *item) {
  self->appendRow(item);
}

//  void QStandardItemModel::insertRow(int row, const QList<QStandardItem *>
//      &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel9insertRowEiRK5QListIP13QStandardItemE(
    QStandardItemModel *self,
    int row,
    const QList<QStandardItem *> *items) {
  self->insertRow(row, *items);
}

//  void QStandardItemModel::insertColumn(int column, const
//      QList<QStandardItem *> &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel12insertColumnEiRK5QListIP13QStandardItemE(
    QStandardItemModel *self,
    int column,
    const QList<QStandardItem *> *items) {
  self->insertColumn(column, *items);
}

//  void QStandardItemModel::insertRow(int row, QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel9insertRowEiP13QStandardItem(
    QStandardItemModel *self,
    int row,
    QStandardItem *item) {
  self->insertRow(row, item);
}

//  bool QStandardItemModel::insertRow(int row, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel9insertRowEiRK11QModelIndex(
    QStandardItemModel *self,
    int row,
    const QModelIndex *parent) {
  return self->insertRow(row, *parent);
}

//  bool QStandardItemModel::insertColumn(int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel12insertColumnEiRK11QModelIndex(
    QStandardItemModel *self,
    int column,
    const QModelIndex *parent) {
  return self->insertColumn(column, *parent);
}

//  QStandardItem *QStandardItemModel::takeItem(int row, int column)
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN18QStandardItemModel8takeItemEii(
    QStandardItemModel *self,
    int row,
    int column) {
  return self->takeItem(row, column);
}

//  QList<QStandardItem *> QStandardItemModel::takeRow(int row)
extern "C" Q_DECL_EXPORT
QList<QStandardItem *> *ritual_ZN18QStandardItemModel7takeRowEi(
    QStandardItemModel *self,
    int row) {
  return new QList<QStandardItem *>(self->takeRow(row));
}

//  QList<QStandardItem *> QStandardItemModel::takeColumn(int column)
extern "C" Q_DECL_EXPORT
QList<QStandardItem *> *ritual_ZN18QStandardItemModel10takeColumnEi(
    QStandardItemModel *self,
    int column) {
  return new QList<QStandardItem *>(self->takeColumn(column));
}

//  QStandardItem *QStandardItemModel::takeHorizontalHeaderItem(int column)
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN18QStandardItemModel24takeHorizontalHeaderItemEi(
    QStandardItemModel *self,
    int column) {
  return self->takeHorizontalHeaderItem(column);
}

//  QStandardItem *QStandardItemModel::takeVerticalHeaderItem(int row)
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN18QStandardItemModel22takeVerticalHeaderItemEi(
    QStandardItemModel *self,
    int row) {
  return self->takeVerticalHeaderItem(row);
}

//  const QStandardItem *QStandardItemModel::itemPrototype() const
extern "C" Q_DECL_EXPORT
const QStandardItem *ritual_ZNK18QStandardItemModel13itemPrototypeEv(
    const QStandardItemModel *self) {
  return self->itemPrototype();
}

//  void QStandardItemModel::setItemPrototype(const QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel16setItemPrototypeEPK13QStandardItem(
    QStandardItemModel *self,
    const QStandardItem *item) {
  self->setItemPrototype(item);
}

//  QList<QStandardItem *> QStandardItemModel::findItems(const QString &text,
//      Qt::MatchFlags flags, int column) const
extern "C" Q_DECL_EXPORT
QList<QStandardItem *> *ritual_ZNK18QStandardItemModel9findItemsERK7QString6QFlagsIN2Qt9MatchFlagEEi(
    const QStandardItemModel *self,
    const QString *text,
    int flags,
    int column) {
  return new QList<QStandardItem *>(
      self->findItems(
          *text,
          QFlags<Qt::MatchFlag>::fromInt(flags),
          column));
}

//  int QStandardItemModel::sortRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QStandardItemModel8sortRoleEv(
    const QStandardItemModel *self) {
  return self->sortRole();
}

//  void QStandardItemModel::setSortRole(int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel11setSortRoleEi(
    QStandardItemModel *self,
    int role) {
  self->setSortRole(role);
}

//  QStringList QStandardItemModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QStandardItemModel9mimeTypesEv(
    const QStandardItemModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  QMimeData *QStandardItemModel::mimeData(const QModelIndexList &indexes)
//      const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK18QStandardItemModel8mimeDataERK5QListI11QModelIndexE(
    const QStandardItemModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  bool QStandardItemModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QStandardItemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  QStandardItemModelPrivate *QStandardItemModel::d_func()
extern "C" Q_DECL_EXPORT
QStandardItemModelPrivate *ritual_ZN18QStandardItemModel6d_funcEv(
    QStandardItemModel *self) {
  return self->d_func();
}

//  const QStandardItemModelPrivate *QStandardItemModel::d_func() const
extern "C" Q_DECL_EXPORT
const QStandardItemModelPrivate *ritual_ZNK18QStandardItemModel6d_funcEv(
    const QStandardItemModel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQStandardItemModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStandardItemModel(
    QStandardItemModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStandardItemModel *>(self)->take(key, call);
}

//  QModelIndex QStandardItemModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK18QStandardItemModel5indexEiiRK11QModelIndex(
    const QStandardItemModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QStandardItemModel::index(
          row,
          column,
          *parent));
}

//  QModelIndex QStandardItemModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK18QStandardItemModel6parentERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->QStandardItemModel::parent(*child));
}

//  int QStandardItemModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QStandardItemModel8rowCountERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *parent) {
  return self->QStandardItemModel::rowCount(*parent);
}

//  int QStandardItemModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QStandardItemModel11columnCountERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *parent) {
  return self->QStandardItemModel::columnCount(*parent);
}

//  bool QStandardItemModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QStandardItemModel11hasChildrenERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *parent) {
  return self->QStandardItemModel::hasChildren(*parent);
}

//  QVariant QStandardItemModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK18QStandardItemModel4dataERK11QModelIndexi(
    const QStandardItemModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QStandardItemModel::data(*index, role));
}

//  void QStandardItemModel::multiData(const QModelIndex &index,
//      QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK18QStandardItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QStandardItemModel *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->QStandardItemModel::multiData(*index, *roleDataSpan);
}

//  bool QStandardItemModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QStandardItemModel7setDataERK11QModelIndexRK8QVarianti(
    QStandardItemModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QStandardItemModel::setData(*index, *value, role);
}

//  bool QStandardItemModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QStandardItemModel13clearItemDataERK11QModelIndex(
    QStandardItemModel *self,
    const QModelIndex *index) {
  return self->QStandardItemModel::clearItemData(*index);
}

//  QVariant QStandardItemModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK18QStandardItemModel10headerDataEiN2Qt11OrientationEi(
    const QStandardItemModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QStandardItemModel::headerData(
          section,
          orientation,
          role));
}

//  bool QStandardItemModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QStandardItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QStandardItemModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->QStandardItemModel::setHeaderData(
      section,
      orientation,
      *value,
      role);
}

//  bool QStandardItemModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QStandardItemModel10insertRowsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QStandardItemModel::insertRows(row, count, *parent);
}

//  bool QStandardItemModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QStandardItemModel13insertColumnsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QStandardItemModel::insertColumns(column, count, *parent);
}

//  bool QStandardItemModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QStandardItemModel10removeRowsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QStandardItemModel::removeRows(row, count, *parent);
}

//  bool QStandardItemModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QStandardItemModel13removeColumnsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QStandardItemModel::removeColumns(column, count, *parent);
}

//  Qt::ItemFlags QStandardItemModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QStandardItemModel5flagsERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QStandardItemModel::flags(*index).toInt());
}

//  Qt::DropActions QStandardItemModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QStandardItemModel20supportedDropActionsEv(
    const QStandardItemModel *self) {
  return static_cast<int>(
      self->QStandardItemModel::supportedDropActions().toInt());
}

//  void QStandardItemModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QStandardItemModel4sortEiN2Qt9SortOrderE(
    QStandardItemModel *self,
    int column,
    Qt::SortOrder order) {
  self->QStandardItemModel::sort(column, order);
}

//  bool QStandardItemModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QStandardItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QStandardItemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QStandardItemModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

#endif  // QT_CONFIG(standarditemmodel)
