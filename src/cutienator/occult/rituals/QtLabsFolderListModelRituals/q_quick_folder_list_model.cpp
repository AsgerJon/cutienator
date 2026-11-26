//  Written by dev_tooling.RitualGenerator from the records of QtLabsFolderLi
//  stModel/6.12.0/QtLabsFolderListModel/private/qquickfolderlistmodel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtLabsFolderListModel/6.12.0/QtLabsFolderListModel/private/qquickfolderlistmodelglobal_p.h>
#include <QtLabsFolderListModel/QtLabsFolderListModel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsFolderListModel/6.12.0/QtLabsFolderListModel/private/qquickfolderlistmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQuickFolderListModel that Python can take functions over in. Every QQuickFolderListModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQuickFolderListModelCall0)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQuickFolderListModelCall1)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQQuickFolderListModelCall2)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
typedef void (*CuteQQuickFolderListModelCall3)(const void *, int *);
typedef void (*CuteQQuickFolderListModelCall4)(const void *, int *);
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQuickFolderListModelCall5)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall6)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQuickFolderListModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQuickFolderListModelCall8)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQuickFolderListModelCall9)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall11)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQQuickFolderListModelCall12)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall13)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall15)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQuickFolderListModelCall16)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQuickFolderListModelCall17)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall18)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall20)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall21)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall22)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall23)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQuickFolderListModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQuickFolderListModelCall26)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQuickFolderListModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQQuickFolderListModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQuickFolderListModelCall29)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQuickFolderListModelCall30)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQuickFolderListModelCall31)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQuickFolderListModelCall32)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFolderListModelCall33)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFolderListModelCall34)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFolderListModelCall35)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFolderListModelCall36)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFolderListModelCall37)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFolderListModelCall38)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFolderListModelCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickFolderListModel : public QQuickFolderListModel {
public:
  using QQuickFolderListModel::QQuickFolderListModel;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
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
  //  int QQuickFolderListModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFolderListModelCall0 call = reinterpret_cast<CuteQQuickFolderListModelCall0>(taken[0]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QQuickFolderListModel::rowCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QQuickFolderListModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFolderListModelCall1 call = reinterpret_cast<CuteQQuickFolderListModelCall1>(taken[1]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QQuickFolderListModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QQuickFolderListModel::data(const QModelIndex &index, int
  //      role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFolderListModelCall2 call = reinterpret_cast<CuteQQuickFolderListModelCall2>(taken[2]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QQuickFolderListModel::data(index, role);
  }
#endif  // QT_CONFIG(itemmodel)

  //  void QQuickFolderListModel::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickFolderListModelCall3 call = reinterpret_cast<CuteQQuickFolderListModelCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFolderListModel::classBegin();
  }

  //  void QQuickFolderListModel::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickFolderListModelCall4 call = reinterpret_cast<CuteQQuickFolderListModelCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFolderListModel::componentComplete();
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
      CuteQQuickFolderListModelCall5 call = reinterpret_cast<CuteQQuickFolderListModelCall5>(taken[5]);
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
      CuteQQuickFolderListModelCall6 call = reinterpret_cast<CuteQQuickFolderListModelCall6>(taken[6]);
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
      CuteQQuickFolderListModelCall7 call = reinterpret_cast<CuteQQuickFolderListModelCall7>(taken[7]);
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
      CuteQQuickFolderListModelCall8 call = reinterpret_cast<CuteQQuickFolderListModelCall8>(taken[8]);
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
      CuteQQuickFolderListModelCall9 call = reinterpret_cast<CuteQQuickFolderListModelCall9>(taken[9]);
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
      CuteQQuickFolderListModelCall10 call = reinterpret_cast<CuteQQuickFolderListModelCall10>(taken[10]);
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
      CuteQQuickFolderListModelCall11 call = reinterpret_cast<CuteQQuickFolderListModelCall11>(taken[11]);
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
      CuteQQuickFolderListModelCall12 call = reinterpret_cast<CuteQQuickFolderListModelCall12>(taken[12]);
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
      CuteQQuickFolderListModelCall13 call = reinterpret_cast<CuteQQuickFolderListModelCall13>(taken[13]);
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
      CuteQQuickFolderListModelCall14 call = reinterpret_cast<CuteQQuickFolderListModelCall14>(taken[14]);
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
      CuteQQuickFolderListModelCall15 call = reinterpret_cast<CuteQQuickFolderListModelCall15>(taken[15]);
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
      CuteQQuickFolderListModelCall16 call = reinterpret_cast<CuteQQuickFolderListModelCall16>(taken[16]);
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
      CuteQQuickFolderListModelCall17 call = reinterpret_cast<CuteQQuickFolderListModelCall17>(taken[17]);
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
      CuteQQuickFolderListModelCall18 call = reinterpret_cast<CuteQQuickFolderListModelCall18>(taken[18]);
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
      CuteQQuickFolderListModelCall19 call = reinterpret_cast<CuteQQuickFolderListModelCall19>(taken[19]);
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
      CuteQQuickFolderListModelCall20 call = reinterpret_cast<CuteQQuickFolderListModelCall20>(taken[20]);
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
      CuteQQuickFolderListModelCall21 call = reinterpret_cast<CuteQQuickFolderListModelCall21>(taken[21]);
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
      CuteQQuickFolderListModelCall22 call = reinterpret_cast<CuteQQuickFolderListModelCall22>(taken[22]);
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
      CuteQQuickFolderListModelCall23 call = reinterpret_cast<CuteQQuickFolderListModelCall23>(taken[23]);
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
      CuteQQuickFolderListModelCall24 call = reinterpret_cast<CuteQQuickFolderListModelCall24>(taken[24]);
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
      CuteQQuickFolderListModelCall25 call = reinterpret_cast<CuteQQuickFolderListModelCall25>(taken[25]);
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
      CuteQQuickFolderListModelCall26 call = reinterpret_cast<CuteQQuickFolderListModelCall26>(taken[26]);
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
      CuteQQuickFolderListModelCall27 call = reinterpret_cast<CuteQQuickFolderListModelCall27>(taken[27]);
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
      CuteQQuickFolderListModelCall28 call = reinterpret_cast<CuteQQuickFolderListModelCall28>(taken[28]);
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
      CuteQQuickFolderListModelCall29 call = reinterpret_cast<CuteQQuickFolderListModelCall29>(taken[29]);
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
      CuteQQuickFolderListModelCall30 call = reinterpret_cast<CuteQQuickFolderListModelCall30>(taken[30]);
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
      CuteQQuickFolderListModelCall31 call = reinterpret_cast<CuteQQuickFolderListModelCall31>(taken[31]);
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
      CuteQQuickFolderListModelCall32 call = reinterpret_cast<CuteQQuickFolderListModelCall32>(taken[32]);
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
      CuteQQuickFolderListModelCall33 call = reinterpret_cast<CuteQQuickFolderListModelCall33>(taken[33]);
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
      CuteQQuickFolderListModelCall34 call = reinterpret_cast<CuteQQuickFolderListModelCall34>(taken[34]);
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
      CuteQQuickFolderListModelCall35 call = reinterpret_cast<CuteQQuickFolderListModelCall35>(taken[35]);
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
      CuteQQuickFolderListModelCall36 call = reinterpret_cast<CuteQQuickFolderListModelCall36>(taken[36]);
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
      CuteQQuickFolderListModelCall37 call = reinterpret_cast<CuteQQuickFolderListModelCall37>(taken[37]);
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
      CuteQQuickFolderListModelCall38 call = reinterpret_cast<CuteQQuickFolderListModelCall38>(taken[38]);
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
      CuteQQuickFolderListModelCall39 call = reinterpret_cast<CuteQQuickFolderListModelCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickFolderListModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickFolderListModel10metaObjectEv(
    const QQuickFolderListModel *self) {
  return self->metaObject();
}

//  void *QQuickFolderListModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickFolderListModel11qt_metacastEPKc(
    QQuickFolderListModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFolderListModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickFolderListModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFolderListModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFolderListModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickFolderListModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFolderListModel::tr(s, c, n));
}

//  QQuickFolderListModel::QQuickFolderListModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFolderListModel *ritual_ZN21QQuickFolderListModelC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickFolderListModel(parent);
}

//  QQuickFolderListModel::~QQuickFolderListModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModelD1Ev(QQuickFolderListModel *self) {
  delete self;
}

//  int QQuickFolderListModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickFolderListModel8rowCountERK11QModelIndex(
    const QQuickFolderListModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QModelIndex QQuickFolderListModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QQuickFolderListModel5indexEiiRK11QModelIndex(
    const QQuickFolderListModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QVariant QQuickFolderListModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QQuickFolderListModel4dataERK11QModelIndexi(
    const QQuickFolderListModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QHash<int, QByteArray> QQuickFolderListModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK21QQuickFolderListModel9roleNamesEv(
    const QQuickFolderListModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  int QQuickFolderListModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickFolderListModel5countEv(
    const QQuickFolderListModel *self) {
  return self->count();
}

//  QUrl QQuickFolderListModel::folder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QQuickFolderListModel6folderEv(
    const QQuickFolderListModel *self) {
  return new QUrl(self->folder());
}

//  void QQuickFolderListModel::setFolder(const QUrl &folder)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel9setFolderERK4QUrl(
    QQuickFolderListModel *self,
    const QUrl *folder) {
  self->setFolder(*folder);
}

//  QUrl QQuickFolderListModel::rootFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QQuickFolderListModel10rootFolderEv(
    const QQuickFolderListModel *self) {
  return new QUrl(self->rootFolder());
}

//  void QQuickFolderListModel::setRootFolder(const QUrl &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel13setRootFolderERK4QUrl(
    QQuickFolderListModel *self,
    const QUrl *path) {
  self->setRootFolder(*path);
}

//  QUrl QQuickFolderListModel::parentFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QQuickFolderListModel12parentFolderEv(
    const QQuickFolderListModel *self) {
  return new QUrl(self->parentFolder());
}

//  QStringList QQuickFolderListModel::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QQuickFolderListModel11nameFiltersEv(
    const QQuickFolderListModel *self) {
  return new QList<QString>(self->nameFilters());
}

//  void QQuickFolderListModel::setNameFilters(const QStringList &filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel14setNameFiltersERK5QListI7QStringE(
    QQuickFolderListModel *self,
    const QList<QString> *filters) {
  self->setNameFilters(*filters);
}

//  SortField QQuickFolderListModel::sortField() const
extern "C" Q_DECL_EXPORT
QQuickFolderListModel::SortField ritual_ZNK21QQuickFolderListModel9sortFieldEv(
    const QQuickFolderListModel *self) {
  return self->sortField();
}

//  void QQuickFolderListModel::setSortField(SortField field)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel12setSortFieldENS_9SortFieldE(
    QQuickFolderListModel *self,
    QQuickFolderListModel::SortField field) {
  self->setSortField(field);
}

//  bool QQuickFolderListModel::sortReversed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel12sortReversedEv(
    const QQuickFolderListModel *self) {
  return self->sortReversed();
}

//  void QQuickFolderListModel::setSortReversed(bool rev)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel15setSortReversedEb(
    QQuickFolderListModel *self,
    bool rev) {
  self->setSortReversed(rev);
}

//  bool QQuickFolderListModel::showFiles() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel9showFilesEv(
    const QQuickFolderListModel *self) {
  return self->showFiles();
}

//  void QQuickFolderListModel::setShowFiles(bool showFiles)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel12setShowFilesEb(
    QQuickFolderListModel *self,
    bool showFiles) {
  self->setShowFiles(showFiles);
}

//  bool QQuickFolderListModel::showDirs() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel8showDirsEv(
    const QQuickFolderListModel *self) {
  return self->showDirs();
}

//  void QQuickFolderListModel::setShowDirs(bool showDirs)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel11setShowDirsEb(
    QQuickFolderListModel *self,
    bool showDirs) {
  self->setShowDirs(showDirs);
}

//  bool QQuickFolderListModel::showDirsFirst() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel13showDirsFirstEv(
    const QQuickFolderListModel *self) {
  return self->showDirsFirst();
}

//  void QQuickFolderListModel::setShowDirsFirst(bool showDirsFirst)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel16setShowDirsFirstEb(
    QQuickFolderListModel *self,
    bool showDirsFirst) {
  self->setShowDirsFirst(showDirsFirst);
}

//  bool QQuickFolderListModel::showDotAndDotDot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel16showDotAndDotDotEv(
    const QQuickFolderListModel *self) {
  return self->showDotAndDotDot();
}

//  void QQuickFolderListModel::setShowDotAndDotDot(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel19setShowDotAndDotDotEb(
    QQuickFolderListModel *self,
    bool on) {
  self->setShowDotAndDotDot(on);
}

//  bool QQuickFolderListModel::showDot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel7showDotEv(
    const QQuickFolderListModel *self) {
  return self->showDot();
}

//  void QQuickFolderListModel::setShowDot(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel10setShowDotEb(
    QQuickFolderListModel *self,
    bool on) {
  self->setShowDot(on);
}

//  bool QQuickFolderListModel::showDotDot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel10showDotDotEv(
    const QQuickFolderListModel *self) {
  return self->showDotDot();
}

//  void QQuickFolderListModel::setShowDotDot(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel13setShowDotDotEb(
    QQuickFolderListModel *self,
    bool on) {
  self->setShowDotDot(on);
}

//  bool QQuickFolderListModel::showHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel10showHiddenEv(
    const QQuickFolderListModel *self) {
  return self->showHidden();
}

//  void QQuickFolderListModel::setShowHidden(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel13setShowHiddenEb(
    QQuickFolderListModel *self,
    bool on) {
  self->setShowHidden(on);
}

//  bool QQuickFolderListModel::showOnlyReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel16showOnlyReadableEv(
    const QQuickFolderListModel *self) {
  return self->showOnlyReadable();
}

//  void QQuickFolderListModel::setShowOnlyReadable(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel19setShowOnlyReadableEb(
    QQuickFolderListModel *self,
    bool on) {
  self->setShowOnlyReadable(on);
}

//  bool QQuickFolderListModel::caseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel13caseSensitiveEv(
    const QQuickFolderListModel *self) {
  return self->caseSensitive();
}

//  void QQuickFolderListModel::setCaseSensitive(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel16setCaseSensitiveEb(
    QQuickFolderListModel *self,
    bool on) {
  self->setCaseSensitive(on);
}

//  Status QQuickFolderListModel::status() const
extern "C" Q_DECL_EXPORT
QQuickFolderListModel::Status ritual_ZNK21QQuickFolderListModel6statusEv(
    const QQuickFolderListModel *self) {
  return self->status();
}

//  bool QQuickFolderListModel::sortCaseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel17sortCaseSensitiveEv(
    const QQuickFolderListModel *self) {
  return self->sortCaseSensitive();
}

//  void QQuickFolderListModel::setSortCaseSensitive(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel20setSortCaseSensitiveEb(
    QQuickFolderListModel *self,
    bool on) {
  self->setSortCaseSensitive(on);
}

//  bool QQuickFolderListModel::isFolder(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickFolderListModel8isFolderEi(
    const QQuickFolderListModel *self,
    int index) {
  return self->isFolder(index);
}

//  QVariant QQuickFolderListModel::get(int idx, const QString &property)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QQuickFolderListModel3getEiRK7QString(
    const QQuickFolderListModel *self,
    int idx,
    const QString *property) {
  return new QVariant(self->get(idx, *property));
}

//  int QQuickFolderListModel::indexOf(const QUrl &file) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickFolderListModel7indexOfERK4QUrl(
    const QQuickFolderListModel *self,
    const QUrl *file) {
  return self->indexOf(*file);
}

//  void QQuickFolderListModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel10classBeginEv(
    QQuickFolderListModel *self) {
  self->classBegin();
}

//  void QQuickFolderListModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel17componentCompleteEv(
    QQuickFolderListModel *self) {
  self->componentComplete();
}

//  int QQuickFolderListModel::roleFromString(const QString &roleName) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickFolderListModel14roleFromStringERK7QString(
    const QQuickFolderListModel *self,
    const QString *roleName) {
  return self->roleFromString(*roleName);
}

//  void QQuickFolderListModel::folderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel13folderChangedEv(
    QQuickFolderListModel *self) {
  self->folderChanged();
}

//  void QQuickFolderListModel::rowCountChanged() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickFolderListModel15rowCountChangedEv(
    const QQuickFolderListModel *self) {
  self->rowCountChanged();
}

//  void QQuickFolderListModel::rootFolderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel17rootFolderChangedEv(
    QQuickFolderListModel *self) {
  self->rootFolderChanged();
}

//  void QQuickFolderListModel::nameFilterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel17nameFilterChangedEv(
    QQuickFolderListModel *self) {
  self->nameFilterChanged();
}

//  void QQuickFolderListModel::sortFieldChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel16sortFieldChangedEv(
    QQuickFolderListModel *self) {
  self->sortFieldChanged();
}

//  void QQuickFolderListModel::sortReversedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel19sortReversedChangedEv(
    QQuickFolderListModel *self) {
  self->sortReversedChanged();
}

//  void QQuickFolderListModel::showFilesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel16showFilesChangedEv(
    QQuickFolderListModel *self) {
  self->showFilesChanged();
}

//  void QQuickFolderListModel::showDirsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel15showDirsChangedEv(
    QQuickFolderListModel *self) {
  self->showDirsChanged();
}

//  void QQuickFolderListModel::showDirsFirstChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel20showDirsFirstChangedEv(
    QQuickFolderListModel *self) {
  self->showDirsFirstChanged();
}

//  void QQuickFolderListModel::showDotAndDotDotChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel23showDotAndDotDotChangedEv(
    QQuickFolderListModel *self) {
  self->showDotAndDotDotChanged();
}

//  void QQuickFolderListModel::showDotChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel14showDotChangedEv(
    QQuickFolderListModel *self) {
  self->showDotChanged();
}

//  void QQuickFolderListModel::showDotDotChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel17showDotDotChangedEv(
    QQuickFolderListModel *self) {
  self->showDotDotChanged();
}

//  void QQuickFolderListModel::showHiddenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel17showHiddenChangedEv(
    QQuickFolderListModel *self) {
  self->showHiddenChanged();
}

//  void QQuickFolderListModel::showOnlyReadableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel23showOnlyReadableChangedEv(
    QQuickFolderListModel *self) {
  self->showOnlyReadableChanged();
}

//  void QQuickFolderListModel::caseSensitiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel20caseSensitiveChangedEv(
    QQuickFolderListModel *self) {
  self->caseSensitiveChanged();
}

//  void QQuickFolderListModel::sortCaseSensitiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel24sortCaseSensitiveChangedEv(
    QQuickFolderListModel *self) {
  self->sortCaseSensitiveChanged();
}

//  void QQuickFolderListModel::countChanged() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickFolderListModel12countChangedEv(
    const QQuickFolderListModel *self) {
  self->countChanged();
}

//  void QQuickFolderListModel::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickFolderListModel13statusChangedEv(
    QQuickFolderListModel *self) {
  self->statusChanged();
}

//  QQuickFolderListModelPrivate *QQuickFolderListModel::d_func()
extern "C" Q_DECL_EXPORT
QQuickFolderListModelPrivate *ritual_ZN21QQuickFolderListModel6d_funcEv(
    QQuickFolderListModel *self) {
  return self->d_func();
}

//  const QQuickFolderListModelPrivate *QQuickFolderListModel::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFolderListModelPrivate *ritual_ZNK21QQuickFolderListModel6d_funcEv(
    const QQuickFolderListModel *self) {
  return self->d_func();
}

//  QQuickFolderListModel as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickFolderListModel_QQmlParserStatus(
    QQuickFolderListModel *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickFolderListModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFolderListModel(
    QQuickFolderListModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFolderListModel *>(self)->take(key, call);
}

//  int QQuickFolderListModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QQuickFolderListModel8rowCountERK11QModelIndex(
    const QQuickFolderListModel *self,
    const QModelIndex *parent) {
  return self->QQuickFolderListModel::rowCount(*parent);
}

//  QModelIndex QQuickFolderListModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK21QQuickFolderListModel5indexEiiRK11QModelIndex(
    const QQuickFolderListModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QQuickFolderListModel::index(
          row,
          column,
          *parent));
}

//  QVariant QQuickFolderListModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK21QQuickFolderListModel4dataERK11QModelIndexi(
    const QQuickFolderListModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QQuickFolderListModel::data(*index, role));
}

//  void QQuickFolderListModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickFolderListModel10classBeginEv(
    QQuickFolderListModel *self) {
  self->QQuickFolderListModel::classBegin();
}

//  void QQuickFolderListModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickFolderListModel17componentCompleteEv(
    QQuickFolderListModel *self) {
  self->QQuickFolderListModel::componentComplete();
}
