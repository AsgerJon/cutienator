//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtCore/qglobal.h>
#include <QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qtqmlxmllistmodelglobal_p.h>
#include <QtQmlXmlListModel/QtQmlXmlListModel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlXmlListModel/6.12.0/QtQmlXmlListModel/private/qqmlxmllistmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQmlXmlListModel that Python can take functions over in. Every QQmlXmlListModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlXmlListModelCall0)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlXmlListModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQQmlXmlListModelCall2)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
typedef void (*CuteQQmlXmlListModelCall3)(const void *, int *);
typedef void (*CuteQQmlXmlListModelCall4)(const void *, int *);
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlXmlListModelCall5)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall6)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlXmlListModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlXmlListModelCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlXmlListModelCall9)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall11)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQQmlXmlListModelCall12)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall13)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall15)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlXmlListModelCall16)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlXmlListModelCall17)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall18)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall20)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall21)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall23)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlXmlListModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlXmlListModelCall26)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlXmlListModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQQmlXmlListModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlXmlListModelCall29)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlXmlListModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlXmlListModelCall31)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlXmlListModelCall32)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlXmlListModelCall33)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlXmlListModelCall34)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlXmlListModelCall35)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlXmlListModelCall36)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlXmlListModelCall37)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlXmlListModelCall38)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlXmlListModelCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlXmlListModel : public QQmlXmlListModel {
public:
  using QQmlXmlListModel::QQmlXmlListModel;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
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

#if QT_CONFIG(itemmodel)
  //  QModelIndex QQmlXmlListModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlXmlListModelCall0 call = reinterpret_cast<CuteQQmlXmlListModelCall0>(taken[0]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QQmlXmlListModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QQmlXmlListModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlXmlListModelCall1 call = reinterpret_cast<CuteQQmlXmlListModelCall1>(taken[1]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QQmlXmlListModel::rowCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QQmlXmlListModel::data(const QModelIndex &index, int role)
  //      const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlXmlListModelCall2 call = reinterpret_cast<CuteQQmlXmlListModelCall2>(taken[2]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QQmlXmlListModel::data(index, role);
  }
#endif  // QT_CONFIG(itemmodel)

  //  void QQmlXmlListModel::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlXmlListModelCall3 call = reinterpret_cast<CuteQQmlXmlListModelCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlXmlListModel::classBegin();
  }

  //  void QQmlXmlListModel::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlXmlListModelCall4 call = reinterpret_cast<CuteQQmlXmlListModelCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlXmlListModel::componentComplete();
  }

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractListModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlXmlListModelCall5 call = reinterpret_cast<CuteQQmlXmlListModelCall5>(taken[5]);
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
      CuteQQmlXmlListModelCall6 call = reinterpret_cast<CuteQQmlXmlListModelCall6>(taken[6]);
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
      CuteQQmlXmlListModelCall7 call = reinterpret_cast<CuteQQmlXmlListModelCall7>(taken[7]);
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
      CuteQQmlXmlListModelCall8 call = reinterpret_cast<CuteQQmlXmlListModelCall8>(taken[8]);
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
      CuteQQmlXmlListModelCall9 call = reinterpret_cast<CuteQQmlXmlListModelCall9>(taken[9]);
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
      CuteQQmlXmlListModelCall10 call = reinterpret_cast<CuteQQmlXmlListModelCall10>(taken[10]);
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
      CuteQQmlXmlListModelCall11 call = reinterpret_cast<CuteQQmlXmlListModelCall11>(taken[11]);
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
      CuteQQmlXmlListModelCall12 call = reinterpret_cast<CuteQQmlXmlListModelCall12>(taken[12]);
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
      CuteQQmlXmlListModelCall13 call = reinterpret_cast<CuteQQmlXmlListModelCall13>(taken[13]);
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
      CuteQQmlXmlListModelCall14 call = reinterpret_cast<CuteQQmlXmlListModelCall14>(taken[14]);
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
      CuteQQmlXmlListModelCall15 call = reinterpret_cast<CuteQQmlXmlListModelCall15>(taken[15]);
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
      CuteQQmlXmlListModelCall16 call = reinterpret_cast<CuteQQmlXmlListModelCall16>(taken[16]);
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
      CuteQQmlXmlListModelCall17 call = reinterpret_cast<CuteQQmlXmlListModelCall17>(taken[17]);
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
      CuteQQmlXmlListModelCall18 call = reinterpret_cast<CuteQQmlXmlListModelCall18>(taken[18]);
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
      CuteQQmlXmlListModelCall19 call = reinterpret_cast<CuteQQmlXmlListModelCall19>(taken[19]);
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
      CuteQQmlXmlListModelCall20 call = reinterpret_cast<CuteQQmlXmlListModelCall20>(taken[20]);
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
      CuteQQmlXmlListModelCall21 call = reinterpret_cast<CuteQQmlXmlListModelCall21>(taken[21]);
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
      CuteQQmlXmlListModelCall22 call = reinterpret_cast<CuteQQmlXmlListModelCall22>(taken[22]);
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
      CuteQQmlXmlListModelCall23 call = reinterpret_cast<CuteQQmlXmlListModelCall23>(taken[23]);
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
      CuteQQmlXmlListModelCall24 call = reinterpret_cast<CuteQQmlXmlListModelCall24>(taken[24]);
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
      CuteQQmlXmlListModelCall25 call = reinterpret_cast<CuteQQmlXmlListModelCall25>(taken[25]);
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
      CuteQQmlXmlListModelCall26 call = reinterpret_cast<CuteQQmlXmlListModelCall26>(taken[26]);
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
      CuteQQmlXmlListModelCall27 call = reinterpret_cast<CuteQQmlXmlListModelCall27>(taken[27]);
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
      CuteQQmlXmlListModelCall28 call = reinterpret_cast<CuteQQmlXmlListModelCall28>(taken[28]);
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
      CuteQQmlXmlListModelCall29 call = reinterpret_cast<CuteQQmlXmlListModelCall29>(taken[29]);
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
      CuteQQmlXmlListModelCall30 call = reinterpret_cast<CuteQQmlXmlListModelCall30>(taken[30]);
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
      CuteQQmlXmlListModelCall31 call = reinterpret_cast<CuteQQmlXmlListModelCall31>(taken[31]);
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
      CuteQQmlXmlListModelCall32 call = reinterpret_cast<CuteQQmlXmlListModelCall32>(taken[32]);
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
      CuteQQmlXmlListModelCall33 call = reinterpret_cast<CuteQQmlXmlListModelCall33>(taken[33]);
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
      CuteQQmlXmlListModelCall34 call = reinterpret_cast<CuteQQmlXmlListModelCall34>(taken[34]);
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
      CuteQQmlXmlListModelCall35 call = reinterpret_cast<CuteQQmlXmlListModelCall35>(taken[35]);
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
      CuteQQmlXmlListModelCall36 call = reinterpret_cast<CuteQQmlXmlListModelCall36>(taken[36]);
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
      CuteQQmlXmlListModelCall37 call = reinterpret_cast<CuteQQmlXmlListModelCall37>(taken[37]);
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
      CuteQQmlXmlListModelCall38 call = reinterpret_cast<CuteQQmlXmlListModelCall38>(taken[38]);
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
      CuteQQmlXmlListModelCall39 call = reinterpret_cast<CuteQQmlXmlListModelCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlXmlListModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlXmlListModel10metaObjectEv(
    const QQmlXmlListModel *self) {
  return self->metaObject();
}

//  QString QQmlXmlListModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlXmlListModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlXmlListModel::tr(s, c, n));
}

//  QQmlXmlListModel::QQmlXmlListModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlXmlListModel *ritual_ZN16QQmlXmlListModelC1EP7QObject(QObject *parent) {
  return new CuteQQmlXmlListModel(parent);
}

//  QQmlXmlListModel::~QQmlXmlListModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModelD1Ev(QQmlXmlListModel *self) {
  delete self;
}

//  QModelIndex QQmlXmlListModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QQmlXmlListModel5indexEiiRK11QModelIndex(
    const QQmlXmlListModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  int QQmlXmlListModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlXmlListModel8rowCountERK11QModelIndex(
    const QQmlXmlListModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QQmlXmlListModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QQmlXmlListModel4dataERK11QModelIndexi(
    const QQmlXmlListModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QHash<int, QByteArray> QQmlXmlListModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK16QQmlXmlListModel9roleNamesEv(
    const QQmlXmlListModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  int QQmlXmlListModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlXmlListModel5countEv(const QQmlXmlListModel *self) {
  return self->count();
}

//  QUrl QQmlXmlListModel::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QQmlXmlListModel6sourceEv(const QQmlXmlListModel *self) {
  return new QUrl(self->source());
}

//  void QQmlXmlListModel::setSource(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel9setSourceERK4QUrl(
    QQmlXmlListModel *self,
    const QUrl *a0) {
  self->setSource(*a0);
}

//  QString QQmlXmlListModel::query() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlXmlListModel5queryEv(const QQmlXmlListModel *self) {
  return new QString(self->query());
}

//  void QQmlXmlListModel::setQuery(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel8setQueryERK7QString(
    QQmlXmlListModel *self,
    const QString *a0) {
  self->setQuery(*a0);
}

//  void QQmlXmlListModel::appendRole(QQmlXmlListModelRole *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel10appendRoleEP20QQmlXmlListModelRole(
    QQmlXmlListModel *self,
    QQmlXmlListModelRole *a0) {
  self->appendRole(a0);
}

//  void QQmlXmlListModel::clearRole()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel9clearRoleEv(QQmlXmlListModel *self) {
  self->clearRole();
}

//  Status QQmlXmlListModel::status() const
extern "C" Q_DECL_EXPORT
QQmlXmlListModel::Status ritual_ZNK16QQmlXmlListModel6statusEv(
    const QQmlXmlListModel *self) {
  return self->status();
}

//  qreal QQmlXmlListModel::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQmlXmlListModel8progressEv(const QQmlXmlListModel *self) {
  return self->progress();
}

//  QString QQmlXmlListModel::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlXmlListModel11errorStringEv(
    const QQmlXmlListModel *self) {
  return new QString(self->errorString());
}

//  void QQmlXmlListModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel10classBeginEv(QQmlXmlListModel *self) {
  self->classBegin();
}

//  void QQmlXmlListModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel17componentCompleteEv(
    QQmlXmlListModel *self) {
  self->componentComplete();
}

//  void QQmlXmlListModel::reload()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel6reloadEv(QQmlXmlListModel *self) {
  self->reload();
}

#if QT_CONFIG(qml_network)
//  void QQmlXmlListModel::requestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel15requestFinishedEv(QQmlXmlListModel *self) {
  self->requestFinished();
}
#endif  // QT_CONFIG(qml_network)

//  void QQmlXmlListModel::requestProgress(qint64 a0, qint64 a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel15requestProgressExx(
    QQmlXmlListModel *self,
    qint64 a0,
    qint64 a1) {
  self->requestProgress(a0, a1);
}

//  void QQmlXmlListModel::dataCleared()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel11dataClearedEv(QQmlXmlListModel *self) {
  self->dataCleared();
}

//  void QQmlXmlListModel::queryCompleted(const QQmlXmlListModelQueryResult
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel14queryCompletedERK27QQmlXmlListModelQueryResult(
    QQmlXmlListModel *self,
    const QQmlXmlListModelQueryResult *a0) {
  self->queryCompleted(*a0);
}

//  void QQmlXmlListModel::notifyQueryStarted(bool remoteSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel18notifyQueryStartedEb(
    QQmlXmlListModel *self,
    bool remoteSource) {
  self->notifyQueryStarted(remoteSource);
}

//  void QQmlXmlListModel::tryExecuteQuery(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel15tryExecuteQueryERK10QByteArray(
    QQmlXmlListModel *self,
    const QByteArray *data) {
  self->tryExecuteQuery(*data);
}

//  QQmlXmlListModelQueryJob QQmlXmlListModel::createJob(const QByteArray
//      &data)
extern "C" Q_DECL_EXPORT
QQmlXmlListModelQueryJob *ritual_ZN16QQmlXmlListModel9createJobERK10QByteArray(
    QQmlXmlListModel *self,
    const QByteArray *data) {
  return new QQmlXmlListModelQueryJob(self->createJob(*data));
}

//  int QQmlXmlListModel::nextQueryId()
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQmlXmlListModel11nextQueryIdEv(QQmlXmlListModel *self) {
  return self->nextQueryId();
}

#if QT_CONFIG(qml_network)
//  void QQmlXmlListModel::deleteReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlXmlListModel11deleteReplyEv(QQmlXmlListModel *self) {
  self->deleteReply();
}
#endif  // QT_CONFIG(qml_network)

//  QQmlXmlListModel as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlXmlListModel_QQmlParserStatus(
    QQmlXmlListModel *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlXmlListModel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlXmlListModel(
    QQmlXmlListModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlXmlListModel *>(self)->take(key, call);
}

//  QModelIndex QQmlXmlListModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK16QQmlXmlListModel5indexEiiRK11QModelIndex(
    const QQmlXmlListModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QQmlXmlListModel::index(
          row,
          column,
          *parent));
}

//  int QQmlXmlListModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QQmlXmlListModel8rowCountERK11QModelIndex(
    const QQmlXmlListModel *self,
    const QModelIndex *parent) {
  return self->QQmlXmlListModel::rowCount(*parent);
}

//  QVariant QQmlXmlListModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK16QQmlXmlListModel4dataERK11QModelIndexi(
    const QQmlXmlListModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QQmlXmlListModel::data(*index, role));
}

//  void QQmlXmlListModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlXmlListModel10classBeginEv(QQmlXmlListModel *self) {
  self->QQmlXmlListModel::classBegin();
}

//  void QQmlXmlListModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlXmlListModel17componentCompleteEv(
    QQmlXmlListModel *self) {
  self->QQmlXmlListModel::componentComplete();
}
