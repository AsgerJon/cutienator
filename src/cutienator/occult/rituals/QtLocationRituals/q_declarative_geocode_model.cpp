//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeocodemodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeocodemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtPositioning/qgeolocation.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QDeclarativeGeocodeModel that Python can take functions over in. Every QDeclarativeGeocodeModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeGeocodeModelCall0)(const void *, int *);
typedef void (*CuteQDeclarativeGeocodeModelCall1)(const void *, int *);
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeGeocodeModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQDeclarativeGeocodeModelCall3)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeGeocodeModelCall4)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeGeocodeModelCall5)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall6)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeGeocodeModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeGeocodeModelCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeGeocodeModelCall9)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall11)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQDeclarativeGeocodeModelCall12)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall13)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall15)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeGeocodeModelCall16)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeGeocodeModelCall17)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall18)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall20)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall21)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall23)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeGeocodeModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeGeocodeModelCall26)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeGeocodeModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQDeclarativeGeocodeModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeGeocodeModelCall29)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeGeocodeModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeGeocodeModelCall31)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeGeocodeModelCall32)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeocodeModelCall33)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeocodeModelCall34)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeocodeModelCall35)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeocodeModelCall36)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeocodeModelCall37)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeocodeModelCall38)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeocodeModelCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeocodeModel : public QDeclarativeGeocodeModel {
public:
  using QDeclarativeGeocodeModel::QDeclarativeGeocodeModel;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
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
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
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

  //  void QDeclarativeGeocodeModel::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall0 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeocodeModel::classBegin();
  }

  //  void QDeclarativeGeocodeModel::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall1 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeocodeModel::componentComplete();
  }

#if QT_CONFIG(itemmodel)
  //  int QDeclarativeGeocodeModel::rowCount(const QModelIndex &parent)
  //      const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall2 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall2>(taken[2]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QDeclarativeGeocodeModel::rowCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QDeclarativeGeocodeModel::data(const QModelIndex &index, int
  //      role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall3 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall3>(taken[3]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QDeclarativeGeocodeModel::data(index, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractListModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall4 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall5 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall6 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall7 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall8 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall8>(taken[8]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QAbstractListModel::parent(child);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractListModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall9 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall9>(taken[9]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractListModel::columnCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractListModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall10 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall11 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall12 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall13 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall13>(taken[13]);
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
      CuteQDeclarativeGeocodeModelCall14 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall15 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall15>(taken[15]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall16 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall17 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall18 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall19 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall20 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall21 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall22 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall22>(taken[22]);
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
      CuteQDeclarativeGeocodeModelCall23 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall23>(taken[23]);
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
      CuteQDeclarativeGeocodeModelCall24 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall24>(taken[24]);
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
      CuteQDeclarativeGeocodeModelCall25 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall25>(taken[25]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDeclarativeGeocodeModelCall26 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall26>(taken[26]);
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
      CuteQDeclarativeGeocodeModelCall27 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall27>(taken[27]);
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
      CuteQDeclarativeGeocodeModelCall28 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall28>(taken[28]);
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
      CuteQDeclarativeGeocodeModelCall29 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall29>(taken[29]);
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
      CuteQDeclarativeGeocodeModelCall30 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall30>(taken[30]);
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
      CuteQDeclarativeGeocodeModelCall31 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall31>(taken[31]);
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
      CuteQDeclarativeGeocodeModelCall32 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall32>(taken[32]);
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
      CuteQDeclarativeGeocodeModelCall33 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall33>(taken[33]);
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
      CuteQDeclarativeGeocodeModelCall34 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall34>(taken[34]);
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
      CuteQDeclarativeGeocodeModelCall35 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall35>(taken[35]);
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
      CuteQDeclarativeGeocodeModelCall36 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall36>(taken[36]);
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
      CuteQDeclarativeGeocodeModelCall37 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall37>(taken[37]);
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
      CuteQDeclarativeGeocodeModelCall38 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall38>(taken[38]);
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
      CuteQDeclarativeGeocodeModelCall39 call = reinterpret_cast<CuteQDeclarativeGeocodeModelCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeGeocodeModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QDeclarativeGeocodeModel10metaObjectEv(
    const QDeclarativeGeocodeModel *self) {
  return self->metaObject();
}

//  void *QDeclarativeGeocodeModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QDeclarativeGeocodeModel11qt_metacastEPKc(
    QDeclarativeGeocodeModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeGeocodeModel::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QDeclarativeGeocodeModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeGeocodeModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeGeocodeModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QDeclarativeGeocodeModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeocodeModel::tr(s, c, n));
}

//  QDeclarativeGeocodeModel::QDeclarativeGeocodeModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeocodeModel *ritual_ZN24QDeclarativeGeocodeModelC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativeGeocodeModel(parent);
}

//  QDeclarativeGeocodeModel::~QDeclarativeGeocodeModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModelD1Ev(
    QDeclarativeGeocodeModel *self) {
  delete self;
}

//  void QDeclarativeGeocodeModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel10classBeginEv(
    QDeclarativeGeocodeModel *self) {
  self->classBegin();
}

//  void QDeclarativeGeocodeModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel17componentCompleteEv(
    QDeclarativeGeocodeModel *self) {
  self->componentComplete();
}

//  int QDeclarativeGeocodeModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QDeclarativeGeocodeModel8rowCountERK11QModelIndex(
    const QDeclarativeGeocodeModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QDeclarativeGeocodeModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QDeclarativeGeocodeModel4dataERK11QModelIndexi(
    const QDeclarativeGeocodeModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QHash<int, QByteArray> QDeclarativeGeocodeModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK24QDeclarativeGeocodeModel9roleNamesEv(
    const QDeclarativeGeocodeModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  void QDeclarativeGeocodeModel::setPlugin(QDeclarativeGeoServiceProvider
//      *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel9setPluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativeGeocodeModel *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->setPlugin(plugin);
}

//  QDeclarativeGeoServiceProvider *QDeclarativeGeocodeModel::plugin() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoServiceProvider *ritual_ZNK24QDeclarativeGeocodeModel6pluginEv(
    const QDeclarativeGeocodeModel *self) {
  return self->plugin();
}

//  void QDeclarativeGeocodeModel::setBounds(const QVariant &boundingArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel9setBoundsERK8QVariant(
    QDeclarativeGeocodeModel *self,
    const QVariant *boundingArea) {
  self->setBounds(*boundingArea);
}

//  QVariant QDeclarativeGeocodeModel::bounds() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QDeclarativeGeocodeModel6boundsEv(
    const QDeclarativeGeocodeModel *self) {
  return new QVariant(self->bounds());
}

//  Status QDeclarativeGeocodeModel::status() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeocodeModel::Status ritual_ZNK24QDeclarativeGeocodeModel6statusEv(
    const QDeclarativeGeocodeModel *self) {
  return self->status();
}

//  QString QDeclarativeGeocodeModel::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QDeclarativeGeocodeModel11errorStringEv(
    const QDeclarativeGeocodeModel *self) {
  return new QString(self->errorString());
}

//  GeocodeError QDeclarativeGeocodeModel::error() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeocodeModel::GeocodeError ritual_ZNK24QDeclarativeGeocodeModel5errorEv(
    const QDeclarativeGeocodeModel *self) {
  return self->error();
}

//  bool QDeclarativeGeocodeModel::autoUpdate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QDeclarativeGeocodeModel10autoUpdateEv(
    const QDeclarativeGeocodeModel *self) {
  return self->autoUpdate();
}

//  void QDeclarativeGeocodeModel::setAutoUpdate(bool update)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel13setAutoUpdateEb(
    QDeclarativeGeocodeModel *self,
    bool update) {
  self->setAutoUpdate(update);
}

//  int QDeclarativeGeocodeModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QDeclarativeGeocodeModel5countEv(
    const QDeclarativeGeocodeModel *self) {
  return self->count();
}

//  QDeclarativeGeoLocation *QDeclarativeGeocodeModel::get(int index)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoLocation *ritual_ZN24QDeclarativeGeocodeModel3getEi(
    QDeclarativeGeocodeModel *self,
    int index) {
  return self->get(index);
}

//  int QDeclarativeGeocodeModel::limit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QDeclarativeGeocodeModel5limitEv(
    const QDeclarativeGeocodeModel *self) {
  return self->limit();
}

//  void QDeclarativeGeocodeModel::setLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel8setLimitEi(
    QDeclarativeGeocodeModel *self,
    int limit) {
  self->setLimit(limit);
}

//  int QDeclarativeGeocodeModel::offset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QDeclarativeGeocodeModel6offsetEv(
    const QDeclarativeGeocodeModel *self) {
  return self->offset();
}

//  void QDeclarativeGeocodeModel::setOffset(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel9setOffsetEi(
    QDeclarativeGeocodeModel *self,
    int offset) {
  self->setOffset(offset);
}

//  QVariant QDeclarativeGeocodeModel::query() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QDeclarativeGeocodeModel5queryEv(
    const QDeclarativeGeocodeModel *self) {
  return new QVariant(self->query());
}

//  void QDeclarativeGeocodeModel::setQuery(const QVariant &query)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel8setQueryERK8QVariant(
    QDeclarativeGeocodeModel *self,
    const QVariant *query) {
  self->setQuery(*query);
}

//  void QDeclarativeGeocodeModel::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel5resetEv(
    QDeclarativeGeocodeModel *self) {
  self->reset();
}

//  void QDeclarativeGeocodeModel::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel6cancelEv(
    QDeclarativeGeocodeModel *self) {
  self->cancel();
}

//  void QDeclarativeGeocodeModel::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel12countChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->countChanged();
}

//  void QDeclarativeGeocodeModel::pluginChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel13pluginChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->pluginChanged();
}

//  void QDeclarativeGeocodeModel::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel13statusChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->statusChanged();
}

//  void QDeclarativeGeocodeModel::errorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel12errorChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->errorChanged();
}

//  void QDeclarativeGeocodeModel::locationsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel16locationsChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->locationsChanged();
}

//  void QDeclarativeGeocodeModel::autoUpdateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel17autoUpdateChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->autoUpdateChanged();
}

//  void QDeclarativeGeocodeModel::boundsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel13boundsChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->boundsChanged();
}

//  void QDeclarativeGeocodeModel::queryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel12queryChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->queryChanged();
}

//  void QDeclarativeGeocodeModel::limitChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel12limitChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->limitChanged();
}

//  void QDeclarativeGeocodeModel::offsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel13offsetChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->offsetChanged();
}

//  void QDeclarativeGeocodeModel::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel6updateEv(
    QDeclarativeGeocodeModel *self) {
  self->update();
}

//  void QDeclarativeGeocodeModel::queryContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel19queryContentChangedEv(
    QDeclarativeGeocodeModel *self) {
  self->queryContentChanged();
}

//  void QDeclarativeGeocodeModel::geocodeFinished(QGeoCodeReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel15geocodeFinishedEP13QGeoCodeReply(
    QDeclarativeGeocodeModel *self,
    QGeoCodeReply *reply) {
  self->geocodeFinished(reply);
}

//  void QDeclarativeGeocodeModel::geocodeError(QGeoCodeReply *reply,
//      QGeoCodeReply::Error error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel12geocodeErrorEP13QGeoCodeReplyNS0_5ErrorERK7QString(
    QDeclarativeGeocodeModel *self,
    QGeoCodeReply *reply,
    QGeoCodeReply::Error error,
    const QString *errorString) {
  self->geocodeError(reply, error, *errorString);
}

//  void QDeclarativeGeocodeModel::pluginReady()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel11pluginReadyEv(
    QDeclarativeGeocodeModel *self) {
  self->pluginReady();
}

//  void QDeclarativeGeocodeModel::setStatus(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel9setStatusENS_6StatusE(
    QDeclarativeGeocodeModel *self,
    QDeclarativeGeocodeModel::Status status) {
  self->setStatus(status);
}

//  void QDeclarativeGeocodeModel::setError(GeocodeError error, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel8setErrorENS_12GeocodeErrorERK7QString(
    QDeclarativeGeocodeModel *self,
    QDeclarativeGeocodeModel::GeocodeError error,
    const QString *errorString) {
  self->setError(error, *errorString);
}

//  void QDeclarativeGeocodeModel::setLocations(const QList<QGeoLocation>
//      &locations)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel12setLocationsERK5QListI12QGeoLocationE(
    QDeclarativeGeocodeModel *self,
    const QList<QGeoLocation> *locations) {
  self->setLocations(*locations);
}

//  void QDeclarativeGeocodeModel::abortRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDeclarativeGeocodeModel12abortRequestEv(
    QDeclarativeGeocodeModel *self) {
  self->abortRequest();
}

//  QDeclarativeGeocodeModel as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QDeclarativeGeocodeModel_QQmlParserStatus(
    QDeclarativeGeocodeModel *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQDeclarativeGeocodeModel, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeocodeModel(
    QDeclarativeGeocodeModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeocodeModel *>(self)->take(key, call);
}

//  void QDeclarativeGeocodeModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QDeclarativeGeocodeModel10classBeginEv(
    QDeclarativeGeocodeModel *self) {
  self->QDeclarativeGeocodeModel::classBegin();
}

//  void QDeclarativeGeocodeModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QDeclarativeGeocodeModel17componentCompleteEv(
    QDeclarativeGeocodeModel *self) {
  self->QDeclarativeGeocodeModel::componentComplete();
}

//  int QDeclarativeGeocodeModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QDeclarativeGeocodeModel8rowCountERK11QModelIndex(
    const QDeclarativeGeocodeModel *self,
    const QModelIndex *parent) {
  return self->QDeclarativeGeocodeModel::rowCount(*parent);
}

//  QVariant QDeclarativeGeocodeModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK24QDeclarativeGeocodeModel4dataERK11QModelIndexi(
    const QDeclarativeGeocodeModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QDeclarativeGeocodeModel::data(*index, role));
}
