//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qcompare.h>
#include <QtCore/qcollator.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QAbstractItemModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractItemModel : QAbstractItemModel {
  using QAbstractItemModel::resetInternalData;
};

//  A QAbstractItemModel that Python can take functions over in. Every QAbstractItemModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractItemModelCall0)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractItemModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractItemModelCall2)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractItemModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractItemModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQAbstractItemModelCall6)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall7)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQAbstractItemModelCall8)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall9)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall11)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall12)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractItemModelCall13)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractItemModelCall14)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall15)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall16)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall17)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall18)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall19)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall20)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelCall21)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall22)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQAbstractItemModelCall23)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelCall24)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQAbstractItemModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQAbstractItemModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelCall27)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQAbstractItemModelCall28)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelCall29)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQAbstractItemModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractItemModelCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractItemModelCall32)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelCall33)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelCall34)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelCall35)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelCall36)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractItemModelCall37)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractItemModel : public QAbstractItemModel {
public:
  using QAbstractItemModel::QAbstractItemModel;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
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
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
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
  //  QModelIndex QAbstractItemModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractItemModelCall0 call = reinterpret_cast<CuteQAbstractItemModelCall0>(taken[0]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractItemModelCall1 call = reinterpret_cast<CuteQAbstractItemModelCall1>(taken[1]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractItemModelCall2 call = reinterpret_cast<CuteQAbstractItemModelCall2>(taken[2]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractItemModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractItemModelCall3 call = reinterpret_cast<CuteQAbstractItemModelCall3>(taken[3]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractItemModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractItemModelCall4 call = reinterpret_cast<CuteQAbstractItemModelCall4>(taken[4]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractItemModelCall5 call = reinterpret_cast<CuteQAbstractItemModelCall5>(taken[5]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QAbstractItemModel::data(const QModelIndex &index, int role)
  //      const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractItemModelCall6 call = reinterpret_cast<CuteQAbstractItemModelCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractItemModelCall7 call = reinterpret_cast<CuteQAbstractItemModelCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractItemModelCall8 call = reinterpret_cast<CuteQAbstractItemModelCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractItemModelCall9 call = reinterpret_cast<CuteQAbstractItemModelCall9>(taken[9]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractItemModelCall10 call = reinterpret_cast<CuteQAbstractItemModelCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractItemModelCall11 call = reinterpret_cast<CuteQAbstractItemModelCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractItemModelCall12 call = reinterpret_cast<CuteQAbstractItemModelCall12>(taken[12]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractItemModelCall13 call = reinterpret_cast<CuteQAbstractItemModelCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractItemModelCall14 call = reinterpret_cast<CuteQAbstractItemModelCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractItemModelCall15 call = reinterpret_cast<CuteQAbstractItemModelCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractItemModelCall16 call = reinterpret_cast<CuteQAbstractItemModelCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractItemModelCall17 call = reinterpret_cast<CuteQAbstractItemModelCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractItemModelCall18 call = reinterpret_cast<CuteQAbstractItemModelCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractItemModelCall19 call = reinterpret_cast<CuteQAbstractItemModelCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractItemModelCall20 call = reinterpret_cast<CuteQAbstractItemModelCall20>(taken[20]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractItemModelCall21 call = reinterpret_cast<CuteQAbstractItemModelCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractItemModelCall22 call = reinterpret_cast<CuteQAbstractItemModelCall22>(taken[22]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::ItemFlags QAbstractItemModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractItemModelCall23 call = reinterpret_cast<CuteQAbstractItemModelCall23>(taken[23]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QAbstractItemModel::flags(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractItemModelCall24 call = reinterpret_cast<CuteQAbstractItemModelCall24>(taken[24]);
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
      CuteQAbstractItemModelCall25 call = reinterpret_cast<CuteQAbstractItemModelCall25>(taken[25]);
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
      CuteQAbstractItemModelCall26 call = reinterpret_cast<CuteQAbstractItemModelCall26>(taken[26]);
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
      CuteQAbstractItemModelCall27 call = reinterpret_cast<CuteQAbstractItemModelCall27>(taken[27]);
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
      CuteQAbstractItemModelCall28 call = reinterpret_cast<CuteQAbstractItemModelCall28>(taken[28]);
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
      CuteQAbstractItemModelCall29 call = reinterpret_cast<CuteQAbstractItemModelCall29>(taken[29]);
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
      CuteQAbstractItemModelCall30 call = reinterpret_cast<CuteQAbstractItemModelCall30>(taken[30]);
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
      CuteQAbstractItemModelCall31 call = reinterpret_cast<CuteQAbstractItemModelCall31>(taken[31]);
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
      CuteQAbstractItemModelCall32 call = reinterpret_cast<CuteQAbstractItemModelCall32>(taken[32]);
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
      CuteQAbstractItemModelCall33 call = reinterpret_cast<CuteQAbstractItemModelCall33>(taken[33]);
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
      CuteQAbstractItemModelCall34 call = reinterpret_cast<CuteQAbstractItemModelCall34>(taken[34]);
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
      CuteQAbstractItemModelCall35 call = reinterpret_cast<CuteQAbstractItemModelCall35>(taken[35]);
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
      CuteQAbstractItemModelCall36 call = reinterpret_cast<CuteQAbstractItemModelCall36>(taken[36]);
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
      CuteQAbstractItemModelCall37 call = reinterpret_cast<CuteQAbstractItemModelCall37>(taken[37]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractItemModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QAbstractItemModel10metaObjectEv(
    const QAbstractItemModel *self) {
  return self->metaObject();
}

//  QString QAbstractItemModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QAbstractItemModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractItemModel::tr(s, c, n));
}

//  QAbstractItemModel::~QAbstractItemModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModelD1Ev(QAbstractItemModel *self) {
  delete self;
}

//  bool QAbstractItemModel::hasIndex(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractItemModel8hasIndexEiiRK11QModelIndex(
    const QAbstractItemModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->hasIndex(row, column, *parent);
}

//  QModelIndex QAbstractItemModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex(
    const QAbstractItemModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QAbstractItemModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractItemModel6parentERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  QModelIndex QAbstractItemModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex(
    const QAbstractItemModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  int QAbstractItemModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractItemModel8rowCountERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QAbstractItemModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractItemModel11columnCountERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  bool QAbstractItemModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QVariant QAbstractItemModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QAbstractItemModel4dataERK11QModelIndexi(
    const QAbstractItemModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QAbstractItemModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti(
    QAbstractItemModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QVariant QAbstractItemModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi(
    const QAbstractItemModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QAbstractItemModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  QMap<int, QVariant> QAbstractItemModel::itemData(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK18QAbstractItemModel8itemDataERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *index) {
  return new QMap<int, QVariant>(self->itemData(*index));
}

//  bool QAbstractItemModel::setItemData(const QModelIndex &index, const
//      QMap<int, QVariant> &roles)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel11setItemDataERK11QModelIndexRK4QMapIi8QVariantE(
    QAbstractItemModel *self,
    const QModelIndex *index,
    const QMap<int, QVariant> *roles) {
  return self->setItemData(*index, *roles);
}

//  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex(
    QAbstractItemModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  QStringList QAbstractItemModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QAbstractItemModel9mimeTypesEv(
    const QAbstractItemModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  QMimeData *QAbstractItemModel::mimeData(const QModelIndexList &indexes)
//      const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK18QAbstractItemModel8mimeDataERK5QListI11QModelIndexE(
    const QAbstractItemModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  bool QAbstractItemModel::canDropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QAbstractItemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->canDropMimeData(data, action, row, column, *parent);
}

//  bool QAbstractItemModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractItemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QAbstractItemModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractItemModel20supportedDropActionsEv(
    const QAbstractItemModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  Qt::DropActions QAbstractItemModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractItemModel20supportedDragActionsEv(
    const QAbstractItemModel *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  bool QAbstractItemModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QAbstractItemModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QAbstractItemModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QAbstractItemModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destinationParent,
      destinationChild);
}

//  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent, int
//      sourceColumn, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceColumn,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveColumns(
      *sourceParent,
      sourceColumn,
      count,
      *destinationParent,
      destinationChild);
}

//  bool QAbstractItemModel::insertRow(int row, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel9insertRowEiRK11QModelIndex(
    QAbstractItemModel *self,
    int row,
    const QModelIndex *parent) {
  return self->insertRow(row, *parent);
}

//  bool QAbstractItemModel::insertColumn(int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel12insertColumnEiRK11QModelIndex(
    QAbstractItemModel *self,
    int column,
    const QModelIndex *parent) {
  return self->insertColumn(column, *parent);
}

//  bool QAbstractItemModel::removeRow(int row, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel9removeRowEiRK11QModelIndex(
    QAbstractItemModel *self,
    int row,
    const QModelIndex *parent) {
  return self->removeRow(row, *parent);
}

//  bool QAbstractItemModel::removeColumn(int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel12removeColumnEiRK11QModelIndex(
    QAbstractItemModel *self,
    int column,
    const QModelIndex *parent) {
  return self->removeColumn(column, *parent);
}

//  bool QAbstractItemModel::moveRow(const QModelIndex &sourceParent, int
//      sourceRow, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel7moveRowERK11QModelIndexiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveRow(
      *sourceParent,
      sourceRow,
      *destinationParent,
      destinationChild);
}

//  bool QAbstractItemModel::moveColumn(const QModelIndex &sourceParent, int
//      sourceColumn, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel10moveColumnERK11QModelIndexiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceColumn,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveColumn(
      *sourceParent,
      sourceColumn,
      *destinationParent,
      destinationChild);
}

//  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex(
    QAbstractItemModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  bool QAbstractItemModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  Qt::ItemFlags QAbstractItemModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractItemModel5flagsERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE(
    QAbstractItemModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractItemModel5buddyERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->buddy(*index));
}

//  QModelIndexList QAbstractItemModel::match(const QModelIndex &start, int
//      role, const QVariant &value, int hits, Qt::MatchFlags flags) const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK18QAbstractItemModel5matchERK11QModelIndexiRK8QVarianti6QFlagsIN2Qt9MatchFlagEE(
    const QAbstractItemModel *self,
    const QModelIndex *start,
    int role,
    const QVariant *value,
    int hits,
    int flags) {
  return new QList<QModelIndex>(
      self->match(
          *start,
          role,
          *value,
          hits,
          QFlags<Qt::MatchFlag>::fromInt(flags)));
}

//  QSize QAbstractItemModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QAbstractItemModel4spanERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  QHash<int, QByteArray> QAbstractItemModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK18QAbstractItemModel9roleNamesEv(
    const QAbstractItemModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  bool QAbstractItemModel::checkIndex(const QModelIndex &index,
//      CheckIndexOptions options) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractItemModel10checkIndexERK11QModelIndex6QFlagsINS_16CheckIndexOptionEE(
    const QAbstractItemModel *self,
    const QModelIndex *index,
    int options) {
  return self->checkIndex(
      *index,
      QFlags<QAbstractItemModel::CheckIndexOption>::fromInt(options));
}

//  void QAbstractItemModel::multiData(const QModelIndex &index,
//      QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QAbstractItemModel *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->multiData(*index, *roleDataSpan);
}

//  bool QAbstractItemModel::submit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel6submitEv(QAbstractItemModel *self) {
  return self->submit();
}

//  void QAbstractItemModel::revert()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel6revertEv(QAbstractItemModel *self) {
  self->revert();
}

//  void QAbstractItemModel::resetInternalData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel17resetInternalDataEv(
    QAbstractItemModel *self) {
  self->resetInternalData();
}

//  QModelIndex QAbstractItemModel::createIndex(int row, int column, quintptr
//      id) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractItemModel11createIndexEiiy(
    const QAbstractItemModel *self,
    int row,
    int column,
    quintptr id) {
  return new QModelIndex(self->createIndex(row, column, id));
}

//  void QAbstractItemModel::beginInsertRows(const QModelIndex &parent, int
//      first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel15beginInsertRowsERK11QModelIndexii(
    QAbstractItemModel *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginInsertRows(*parent, first, last);
}

//  void QAbstractItemModel::endInsertRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel13endInsertRowsEv(
    QAbstractItemModel *self) {
  self->endInsertRows();
}

//  void QAbstractItemModel::beginRemoveRows(const QModelIndex &parent, int
//      first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel15beginRemoveRowsERK11QModelIndexii(
    QAbstractItemModel *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginRemoveRows(*parent, first, last);
}

//  void QAbstractItemModel::endRemoveRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel13endRemoveRowsEv(
    QAbstractItemModel *self) {
  self->endRemoveRows();
}

//  bool QAbstractItemModel::beginMoveRows(const QModelIndex &sourceParent,
//      int sourceFirst, int sourceLast, const QModelIndex
//      &destinationParent, int destinationRow)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel13beginMoveRowsERK11QModelIndexiiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceFirst,
    int sourceLast,
    const QModelIndex *destinationParent,
    int destinationRow) {
  return self->beginMoveRows(
      *sourceParent,
      sourceFirst,
      sourceLast,
      *destinationParent,
      destinationRow);
}

//  void QAbstractItemModel::endMoveRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel11endMoveRowsEv(QAbstractItemModel *self) {
  self->endMoveRows();
}

//  void QAbstractItemModel::beginInsertColumns(const QModelIndex &parent,
//      int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel18beginInsertColumnsERK11QModelIndexii(
    QAbstractItemModel *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginInsertColumns(*parent, first, last);
}

//  void QAbstractItemModel::endInsertColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel16endInsertColumnsEv(
    QAbstractItemModel *self) {
  self->endInsertColumns();
}

//  void QAbstractItemModel::beginRemoveColumns(const QModelIndex &parent,
//      int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel18beginRemoveColumnsERK11QModelIndexii(
    QAbstractItemModel *self,
    const QModelIndex *parent,
    int first,
    int last) {
  self->beginRemoveColumns(*parent, first, last);
}

//  void QAbstractItemModel::endRemoveColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel16endRemoveColumnsEv(
    QAbstractItemModel *self) {
  self->endRemoveColumns();
}

//  bool QAbstractItemModel::beginMoveColumns(const QModelIndex
//      &sourceParent, int sourceFirst, int sourceLast, const QModelIndex
//      &destinationParent, int destinationColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel16beginMoveColumnsERK11QModelIndexiiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceFirst,
    int sourceLast,
    const QModelIndex *destinationParent,
    int destinationColumn) {
  return self->beginMoveColumns(
      *sourceParent,
      sourceFirst,
      sourceLast,
      *destinationParent,
      destinationColumn);
}

//  void QAbstractItemModel::endMoveColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel14endMoveColumnsEv(
    QAbstractItemModel *self) {
  self->endMoveColumns();
}

//  void QAbstractItemModel::beginResetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel15beginResetModelEv(
    QAbstractItemModel *self) {
  self->beginResetModel();
}

//  void QAbstractItemModel::endResetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel13endResetModelEv(
    QAbstractItemModel *self) {
  self->endResetModel();
}

//  void QAbstractItemModel::changePersistentIndex(const QModelIndex &from,
//      const QModelIndex &to)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel21changePersistentIndexERK11QModelIndexS2_(
    QAbstractItemModel *self,
    const QModelIndex *from,
    const QModelIndex *to) {
  self->changePersistentIndex(*from, *to);
}

//  void QAbstractItemModel::changePersistentIndexList(const QModelIndexList
//      &from, const QModelIndexList &to)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel25changePersistentIndexListERK5QListI11QModelIndexES4_(
    QAbstractItemModel *self,
    const QList<QModelIndex> *from,
    const QList<QModelIndex> *to) {
  self->changePersistentIndexList(*from, *to);
}

//  QModelIndexList QAbstractItemModel::persistentIndexList() const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK18QAbstractItemModel19persistentIndexListEv(
    const QAbstractItemModel *self) {
  return new QList<QModelIndex>(self->persistentIndexList());
}

//  Qt::weak_ordering QAbstractItemModel::compareData(const QVariant &left,
//      const QVariant &right)
extern "C" Q_DECL_EXPORT
Qt::weak_ordering *ritual_ZN18QAbstractItemModel11compareDataERK8QVariantS2_(
    const QVariant *left,
    const QVariant *right) {
  return new Qt::weak_ordering(
      QAbstractItemModel::compareData(
          *left,
          *right));
}

//  Qt::weak_ordering QAbstractItemModel::compareData(const QVariant &left,
//      const QVariant &right, const QCollator &collator)
extern "C" Q_DECL_EXPORT
Qt::weak_ordering *ritual_ZN18QAbstractItemModel11compareDataERK8QVariantS2_RK9QCollator(
    const QVariant *left,
    const QVariant *right,
    const QCollator *collator) {
  return new Qt::weak_ordering(
      QAbstractItemModel::compareData(
          *left,
          *right,
          *collator));
}

//  QAbstractItemModelPrivate *QAbstractItemModel::d_func()
extern "C" Q_DECL_EXPORT
QAbstractItemModelPrivate *ritual_ZN18QAbstractItemModel6d_funcEv(
    QAbstractItemModel *self) {
  return self->d_func();
}

//  const QAbstractItemModelPrivate *QAbstractItemModel::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModelPrivate *ritual_ZNK18QAbstractItemModel6d_funcEv(
    const QAbstractItemModel *self) {
  return self->d_func();
}

//  Qt::weak_ordering QAbstractItemModel::compareDataImpl(const QVariant
//      &left, const QVariant &right, const QCollator *collator)
extern "C" Q_DECL_EXPORT
Qt::weak_ordering *ritual_ZN18QAbstractItemModel15compareDataImplERK8QVariantS2_PK9QCollator(
    const QVariant *left,
    const QVariant *right,
    const QCollator *collator) {
  return new Qt::weak_ordering(
      QAbstractItemModel::compareDataImpl(
          *left,
          *right,
          collator));
}

//  a Python function taken by a CuteQAbstractItemModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractItemModel(
    QAbstractItemModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractItemModel *>(self)->take(key, call);
}

//  QModelIndex QAbstractItemModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex(
    const QAbstractItemModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(
      self->QAbstractItemModel::sibling(
          row,
          column,
          *idx));
}

//  bool QAbstractItemModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *parent) {
  return self->QAbstractItemModel::hasChildren(*parent);
}

//  bool QAbstractItemModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti(
    QAbstractItemModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QAbstractItemModel::setData(*index, *value, role);
}

//  QVariant QAbstractItemModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi(
    const QAbstractItemModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QAbstractItemModel::headerData(
          section,
          orientation,
          role));
}

//  bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QAbstractItemModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->QAbstractItemModel::setHeaderData(
      section,
      orientation,
      *value,
      role);
}

//  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex(
    QAbstractItemModel *self,
    const QModelIndex *index) {
  return self->QAbstractItemModel::clearItemData(*index);
}

//  bool QAbstractItemModel::canDropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QAbstractItemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QAbstractItemModel::canDropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  bool QAbstractItemModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractItemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QAbstractItemModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  Qt::DropActions QAbstractItemModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QAbstractItemModel20supportedDropActionsEv(
    const QAbstractItemModel *self) {
  return static_cast<int>(
      self->QAbstractItemModel::supportedDropActions().toInt());
}

//  Qt::DropActions QAbstractItemModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QAbstractItemModel20supportedDragActionsEv(
    const QAbstractItemModel *self) {
  return static_cast<int>(
      self->QAbstractItemModel::supportedDragActions().toInt());
}

//  bool QAbstractItemModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QAbstractItemModel::insertRows(row, count, *parent);
}

//  bool QAbstractItemModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QAbstractItemModel::insertColumns(column, count, *parent);
}

//  bool QAbstractItemModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QAbstractItemModel::removeRows(row, count, *parent);
}

//  bool QAbstractItemModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QAbstractItemModel::removeColumns(column, count, *parent);
}

//  bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->QAbstractItemModel::moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destinationParent,
      destinationChild);
}

//  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent, int
//      sourceColumn, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceColumn,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->QAbstractItemModel::moveColumns(
      *sourceParent,
      sourceColumn,
      count,
      *destinationParent,
      destinationChild);
}

//  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex(
    QAbstractItemModel *self,
    const QModelIndex *parent) {
  self->QAbstractItemModel::fetchMore(*parent);
}

//  bool QAbstractItemModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *parent) {
  return self->QAbstractItemModel::canFetchMore(*parent);
}

//  Qt::ItemFlags QAbstractItemModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QAbstractItemModel5flagsERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QAbstractItemModel::flags(*index).toInt());
}

//  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE(
    QAbstractItemModel *self,
    int column,
    Qt::SortOrder order) {
  self->QAbstractItemModel::sort(column, order);
}

//  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK18QAbstractItemModel5buddyERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->QAbstractItemModel::buddy(*index));
}

//  QSize QAbstractItemModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18QAbstractItemModel4spanERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *index) {
  return new QSize(self->QAbstractItemModel::span(*index));
}

//  void QAbstractItemModel::multiData(const QModelIndex &index,
//      QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QAbstractItemModel *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->QAbstractItemModel::multiData(*index, *roleDataSpan);
}

//  bool QAbstractItemModel::submit()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractItemModel6submitEv(QAbstractItemModel *self) {
  return self->QAbstractItemModel::submit();
}

//  void QAbstractItemModel::revert()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAbstractItemModel6revertEv(QAbstractItemModel *self) {
  self->QAbstractItemModel::revert();
}

//  void QAbstractItemModel::resetInternalData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAbstractItemModel17resetInternalDataEv(
    QAbstractItemModel *self) {
  static_cast<OwnQAbstractItemModel *>(self)->OwnQAbstractItemModel::resetInternalData();
}

//  QList<QAbstractItemModel *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAbstractItemModel *> *ritual_list_make_QAbstractItemModel_ptr() {
  return new QList<QAbstractItemModel *>();
}

//  void QList<QAbstractItemModel *>::append(const QAbstractItemModel *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAbstractItemModel_ptr(
    QList<QAbstractItemModel *> *self,
    QAbstractItemModel *element) {
  self->append(element);
}

//  qsizetype QList<QAbstractItemModel *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAbstractItemModel_ptr(
    const QList<QAbstractItemModel *> *self) {
  return self->size();
}

//  const QAbstractItemModel * &QList<QAbstractItemModel *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_list_at_QAbstractItemModel_ptr(
    const QList<QAbstractItemModel *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAbstractItemModel *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAbstractItemModel_ptr(
    QList<QAbstractItemModel *> *self) {
  delete self;
}

#endif  // QT_CONFIG(itemmodel)
#endif  // QT_CONFIG(itemmodel)
