//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativeplacecontentmodel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativeplacecontentmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtLocation/qplacecontent.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QDeclarativePlaceContentModel that Python can take functions over in. Every QDeclarativePlaceContentModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativePlaceContentModelCall0)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQDeclarativePlaceContentModelCall1)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativePlaceContentModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativePlaceContentModelCall4)(const void *, int *);
typedef void (*CuteQDeclarativePlaceContentModelCall5)(const void *, int *);
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativePlaceContentModelCall6)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativePlaceContentModelCall7)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall8)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativePlaceContentModelCall9)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativePlaceContentModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativePlaceContentModelCall11)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall13)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQDeclarativePlaceContentModelCall14)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall15)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall16)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall17)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativePlaceContentModelCall18)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativePlaceContentModelCall19)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall20)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall21)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall22)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall23)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall24)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall25)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativePlaceContentModelCall26)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativePlaceContentModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQDeclarativePlaceContentModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativePlaceContentModelCall29)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativePlaceContentModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativePlaceContentModelCall31)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativePlaceContentModelCall32)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePlaceContentModelCall33)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePlaceContentModelCall34)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePlaceContentModelCall35)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePlaceContentModelCall36)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePlaceContentModelCall37)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePlaceContentModelCall38)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePlaceContentModelCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativePlaceContentModel : public QDeclarativePlaceContentModel {
public:
  using QDeclarativePlaceContentModel::QDeclarativePlaceContentModel;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
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
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemmodel)
  //  int QDeclarativePlaceContentModel::rowCount(const QModelIndex
  //      &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall0 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall0>(taken[0]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QDeclarativePlaceContentModel::rowCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QDeclarativePlaceContentModel::data(const QModelIndex
  //      &index, int role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall1 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall1>(taken[1]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QDeclarativePlaceContentModel::data(index, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QDeclarativePlaceContentModel::canFetchMore(const QModelIndex
  //      &parent) const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall2 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall2>(taken[2]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QDeclarativePlaceContentModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QDeclarativePlaceContentModel::fetchMore(const QModelIndex
  //      &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall3 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall3>(taken[3]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QDeclarativePlaceContentModel::fetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

  //  void QDeclarativePlaceContentModel::classBegin()
  void classBegin() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall4 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePlaceContentModel::classBegin();
  }

  //  void QDeclarativePlaceContentModel::componentComplete()
  void componentComplete() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall5 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePlaceContentModel::componentComplete();
  }

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractListModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall6 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall6>(taken[6]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QAbstractListModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractListModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall7 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall7>(taken[7]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractListModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractListModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall8 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall8>(taken[8]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractListModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::ItemFlags QAbstractListModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall9 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall9>(taken[9]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QAbstractListModel::flags(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractListModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall10 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall10>(taken[10]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QAbstractListModel::parent(child);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractListModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall11 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall11>(taken[11]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractListModel::columnCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractListModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall12 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall12>(taken[12]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractListModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall13 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall14 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall15 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall15>(taken[15]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall16 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall17 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall17>(taken[17]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall18 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall19 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall20 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall21 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall22 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall23 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall24 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall25 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall25>(taken[25]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall26 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall26>(taken[26]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractItemModel::sort(column, order);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall27 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall27>(taken[27]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall28 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall29 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall29>(taken[29]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[30]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall30 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall30>(taken[30]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[31]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall31 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[32]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall32 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall33 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall33>(taken[33]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall34 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall34>(taken[34]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall35 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall36 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall37 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall38 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall38>(taken[38]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDeclarativePlaceContentModelCall39 call = reinterpret_cast<CuteQDeclarativePlaceContentModelCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativePlaceContentModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QDeclarativePlaceContentModel10metaObjectEv(
    const QDeclarativePlaceContentModel *self) {
  return self->metaObject();
}

//  QString QDeclarativePlaceContentModel::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QDeclarativePlaceContentModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativePlaceContentModel::tr(s, c, n));
}

//  QDeclarativePlaceContentModel::QDeclarativePlaceContentModel(QPlaceConten
//      t::Type type, QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativePlaceContentModel *ritual_ZN29QDeclarativePlaceContentModelC1EN13QPlaceContent4TypeEP7QObject(
    QPlaceContent::Type type,
    QObject *parent) {
  return new CuteQDeclarativePlaceContentModel(type, parent);
}

//  QDeclarativePlaceContentModel::~QDeclarativePlaceContentModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativePlaceContentModelD1Ev(
    QDeclarativePlaceContentModel *self) {
  delete self;
}

//  QDeclarativePlace *QDeclarativePlaceContentModel::place() const
extern "C" Q_DECL_EXPORT
QDeclarativePlace *ritual_ZNK29QDeclarativePlaceContentModel5placeEv(
    const QDeclarativePlaceContentModel *self) {
  return self->place();
}

//  void QDeclarativePlaceContentModel::setPlace(QDeclarativePlace *place)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativePlaceContentModel8setPlaceEP17QDeclarativePlace(
    QDeclarativePlaceContentModel *self,
    QDeclarativePlace *place) {
  self->setPlace(place);
}

//  int QDeclarativePlaceContentModel::batchSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QDeclarativePlaceContentModel9batchSizeEv(
    const QDeclarativePlaceContentModel *self) {
  return self->batchSize();
}

//  void QDeclarativePlaceContentModel::setBatchSize(int batchSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativePlaceContentModel12setBatchSizeEi(
    QDeclarativePlaceContentModel *self,
    int batchSize) {
  self->setBatchSize(batchSize);
}

//  int QDeclarativePlaceContentModel::totalCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QDeclarativePlaceContentModel10totalCountEv(
    const QDeclarativePlaceContentModel *self) {
  return self->totalCount();
}

//  void QDeclarativePlaceContentModel::clearData()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativePlaceContentModel9clearDataEv(
    QDeclarativePlaceContentModel *self) {
  self->clearData();
}

//  void QDeclarativePlaceContentModel::initializeCollection(int totalCount,
//      const QPlaceContent::Collection &collection)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativePlaceContentModel20initializeCollectionEiRK4QMapIi13QPlaceContentE(
    QDeclarativePlaceContentModel *self,
    int totalCount,
    const QMap<int, QPlaceContent> *collection) {
  self->initializeCollection(totalCount, *collection);
}

//  int QDeclarativePlaceContentModel::rowCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QDeclarativePlaceContentModel8rowCountERK11QModelIndex(
    const QDeclarativePlaceContentModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QDeclarativePlaceContentModel::data(const QModelIndex &index,
//      int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK29QDeclarativePlaceContentModel4dataERK11QModelIndexi(
    const QDeclarativePlaceContentModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QHash<int, QByteArray> QDeclarativePlaceContentModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK29QDeclarativePlaceContentModel9roleNamesEv(
    const QDeclarativePlaceContentModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  bool QDeclarativePlaceContentModel::canFetchMore(const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QDeclarativePlaceContentModel12canFetchMoreERK11QModelIndex(
    const QDeclarativePlaceContentModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  void QDeclarativePlaceContentModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativePlaceContentModel9fetchMoreERK11QModelIndex(
    QDeclarativePlaceContentModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  void QDeclarativePlaceContentModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativePlaceContentModel10classBeginEv(
    QDeclarativePlaceContentModel *self) {
  self->classBegin();
}

//  void QDeclarativePlaceContentModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativePlaceContentModel17componentCompleteEv(
    QDeclarativePlaceContentModel *self) {
  self->componentComplete();
}

//  void QDeclarativePlaceContentModel::fetchFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativePlaceContentModel13fetchFinishedEv(
    QDeclarativePlaceContentModel *self) {
  self->fetchFinished();
}

//  QDeclarativePlaceContentModel as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QDeclarativePlaceContentModel_QQmlParserStatus(
    QDeclarativePlaceContentModel *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQDeclarativePlaceContentModel, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativePlaceContentModel(
    QDeclarativePlaceContentModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativePlaceContentModel *>(self)->take(key, call);
}

//  int QDeclarativePlaceContentModel::rowCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QDeclarativePlaceContentModel8rowCountERK11QModelIndex(
    const QDeclarativePlaceContentModel *self,
    const QModelIndex *parent) {
  return self->QDeclarativePlaceContentModel::rowCount(*parent);
}

//  QVariant QDeclarativePlaceContentModel::data(const QModelIndex &index,
//      int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK29QDeclarativePlaceContentModel4dataERK11QModelIndexi(
    const QDeclarativePlaceContentModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(
      self->QDeclarativePlaceContentModel::data(
          *index,
          role));
}

//  bool QDeclarativePlaceContentModel::canFetchMore(const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QDeclarativePlaceContentModel12canFetchMoreERK11QModelIndex(
    const QDeclarativePlaceContentModel *self,
    const QModelIndex *parent) {
  return self->QDeclarativePlaceContentModel::canFetchMore(*parent);
}

//  void QDeclarativePlaceContentModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QDeclarativePlaceContentModel9fetchMoreERK11QModelIndex(
    QDeclarativePlaceContentModel *self,
    const QModelIndex *parent) {
  self->QDeclarativePlaceContentModel::fetchMore(*parent);
}

//  void QDeclarativePlaceContentModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QDeclarativePlaceContentModel10classBeginEv(
    QDeclarativePlaceContentModel *self) {
  self->QDeclarativePlaceContentModel::classBegin();
}

//  void QDeclarativePlaceContentModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QDeclarativePlaceContentModel17componentCompleteEv(
    QDeclarativePlaceContentModel *self) {
  self->QDeclarativePlaceContentModel::componentComplete();
}
