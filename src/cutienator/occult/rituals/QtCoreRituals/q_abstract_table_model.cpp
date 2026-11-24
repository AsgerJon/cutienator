//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAbstractTableModel that Python can take functions over in. Every QAbstractTableModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractTableModelCall0)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractTableModelCall1)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall2)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractTableModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractTableModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractTableModelCall6)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractTableModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQAbstractTableModelCall8)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall9)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQAbstractTableModelCall10)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall11)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall13)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractTableModelCall14)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractTableModelCall15)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall16)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall17)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall18)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall20)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall21)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractTableModelCall22)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall23)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractTableModelCall24)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractTableModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQAbstractTableModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractTableModelCall27)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractTableModelCall28)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractTableModelCall29)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractTableModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractTableModelCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractTableModelCall32)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTableModelCall33)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTableModelCall34)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTableModelCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTableModelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTableModelCall37)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractTableModel : public QAbstractTableModel {
public:
  using QAbstractTableModel::QAbstractTableModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
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
  //  QModelIndex QAbstractTableModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractTableModelCall0 call = reinterpret_cast<CuteQAbstractTableModelCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractTableModelCall1 call = reinterpret_cast<CuteQAbstractTableModelCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractTableModelCall2 call = reinterpret_cast<CuteQAbstractTableModelCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractTableModelCall3 call = reinterpret_cast<CuteQAbstractTableModelCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractTableModelCall4 call = reinterpret_cast<CuteQAbstractTableModelCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractTableModelCall5 call = reinterpret_cast<CuteQAbstractTableModelCall5>(taken[5]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractTableModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractItemModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractTableModelCall6 call = reinterpret_cast<CuteQAbstractTableModelCall6>(taken[6]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractItemModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractTableModelCall7 call = reinterpret_cast<CuteQAbstractTableModelCall7>(taken[7]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QAbstractItemModel::data(const QModelIndex &index, int role)
  //      const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractTableModelCall8 call = reinterpret_cast<CuteQAbstractTableModelCall8>(taken[8]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractTableModelCall9 call = reinterpret_cast<CuteQAbstractTableModelCall9>(taken[9]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QAbstractItemModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractTableModelCall10 call = reinterpret_cast<CuteQAbstractTableModelCall10>(taken[10]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::headerData(section, orientation, role);
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
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractTableModelCall11 call = reinterpret_cast<CuteQAbstractTableModelCall11>(taken[11]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractTableModelCall12 call = reinterpret_cast<CuteQAbstractTableModelCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractTableModelCall13 call = reinterpret_cast<CuteQAbstractTableModelCall13>(taken[13]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractTableModelCall14 call = reinterpret_cast<CuteQAbstractTableModelCall14>(taken[14]);
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
      CuteQAbstractTableModelCall15 call = reinterpret_cast<CuteQAbstractTableModelCall15>(taken[15]);
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
      CuteQAbstractTableModelCall16 call = reinterpret_cast<CuteQAbstractTableModelCall16>(taken[16]);
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
      CuteQAbstractTableModelCall17 call = reinterpret_cast<CuteQAbstractTableModelCall17>(taken[17]);
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
      CuteQAbstractTableModelCall18 call = reinterpret_cast<CuteQAbstractTableModelCall18>(taken[18]);
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
      CuteQAbstractTableModelCall19 call = reinterpret_cast<CuteQAbstractTableModelCall19>(taken[19]);
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
      CuteQAbstractTableModelCall20 call = reinterpret_cast<CuteQAbstractTableModelCall20>(taken[20]);
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
      CuteQAbstractTableModelCall21 call = reinterpret_cast<CuteQAbstractTableModelCall21>(taken[21]);
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
      CuteQAbstractTableModelCall22 call = reinterpret_cast<CuteQAbstractTableModelCall22>(taken[22]);
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
      CuteQAbstractTableModelCall23 call = reinterpret_cast<CuteQAbstractTableModelCall23>(taken[23]);
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
      CuteQAbstractTableModelCall24 call = reinterpret_cast<CuteQAbstractTableModelCall24>(taken[24]);
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
      CuteQAbstractTableModelCall25 call = reinterpret_cast<CuteQAbstractTableModelCall25>(taken[25]);
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
      CuteQAbstractTableModelCall26 call = reinterpret_cast<CuteQAbstractTableModelCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractTableModelCall27 call = reinterpret_cast<CuteQAbstractTableModelCall27>(taken[27]);
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
      CuteQAbstractTableModelCall28 call = reinterpret_cast<CuteQAbstractTableModelCall28>(taken[28]);
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
      CuteQAbstractTableModelCall29 call = reinterpret_cast<CuteQAbstractTableModelCall29>(taken[29]);
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
      CuteQAbstractTableModelCall30 call = reinterpret_cast<CuteQAbstractTableModelCall30>(taken[30]);
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
      CuteQAbstractTableModelCall31 call = reinterpret_cast<CuteQAbstractTableModelCall31>(taken[31]);
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
      CuteQAbstractTableModelCall32 call = reinterpret_cast<CuteQAbstractTableModelCall32>(taken[32]);
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
      CuteQAbstractTableModelCall33 call = reinterpret_cast<CuteQAbstractTableModelCall33>(taken[33]);
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
      CuteQAbstractTableModelCall34 call = reinterpret_cast<CuteQAbstractTableModelCall34>(taken[34]);
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
      CuteQAbstractTableModelCall35 call = reinterpret_cast<CuteQAbstractTableModelCall35>(taken[35]);
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
      CuteQAbstractTableModelCall36 call = reinterpret_cast<CuteQAbstractTableModelCall36>(taken[36]);
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
      CuteQAbstractTableModelCall37 call = reinterpret_cast<CuteQAbstractTableModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractTableModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAbstractTableModel10metaObjectEv(
    const QAbstractTableModel *self) {
  return self->metaObject();
}

//  QString QAbstractTableModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAbstractTableModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractTableModel::tr(s, c, n));
}

//  QAbstractTableModel::~QAbstractTableModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractTableModelD1Ev(QAbstractTableModel *self) {
  delete self;
}

//  QModelIndex QAbstractTableModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractTableModel5indexEiiRK11QModelIndex(
    const QAbstractTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QAbstractTableModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractTableModel7siblingEiiRK11QModelIndex(
    const QAbstractTableModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  bool QAbstractTableModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractTableModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractTableModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::ItemFlags QAbstractTableModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractTableModel5flagsERK11QModelIndex(
    const QAbstractTableModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  QAbstractItemModelPrivate *QAbstractTableModel::d_func()
extern "C" Q_DECL_EXPORT
QAbstractItemModelPrivate *ritual_ZN19QAbstractTableModel6d_funcEv(
    QAbstractTableModel *self) {
  return self->d_func();
}

//  const QAbstractItemModelPrivate *QAbstractTableModel::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModelPrivate *ritual_ZNK19QAbstractTableModel6d_funcEv(
    const QAbstractTableModel *self) {
  return self->d_func();
}

//  QModelIndex QAbstractTableModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractTableModel6parentERK11QModelIndex(
    const QAbstractTableModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  bool QAbstractTableModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractTableModel11hasChildrenERK11QModelIndex(
    const QAbstractTableModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  a Python function taken by a CuteQAbstractTableModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractTableModel(
    QAbstractTableModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractTableModel *>(self)->take(key, call);
}

//  QModelIndex QAbstractTableModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QAbstractTableModel5indexEiiRK11QModelIndex(
    const QAbstractTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QAbstractTableModel::index(
          row,
          column,
          *parent));
}

//  QModelIndex QAbstractTableModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QAbstractTableModel7siblingEiiRK11QModelIndex(
    const QAbstractTableModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(
      self->QAbstractTableModel::sibling(
          row,
          column,
          *idx));
}

//  bool QAbstractTableModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractTableModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractTableModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QAbstractTableModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  Qt::ItemFlags QAbstractTableModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAbstractTableModel5flagsERK11QModelIndex(
    const QAbstractTableModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QAbstractTableModel::flags(*index).toInt());
}

//  QModelIndex QAbstractTableModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QAbstractTableModel6parentERK11QModelIndex(
    const QAbstractTableModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->QAbstractTableModel::parent(*child));
}

//  bool QAbstractTableModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QAbstractTableModel11hasChildrenERK11QModelIndex(
    const QAbstractTableModel *self,
    const QModelIndex *parent) {
  return self->QAbstractTableModel::hasChildren(*parent);
}

#endif  // QT_CONFIG(itemmodel)
