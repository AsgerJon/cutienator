//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltreemodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtCore/qglobal.h>
#include <QtLabsQmlModels/qtlabsqmlmodelsexports.h>
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_tree_model)
#if QT_CONFIG(qml_tree_model)
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlmodelsglobal_p.h>
#include <QtLabsQmlModels/QtLabsQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltreemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQmlTreeModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlTreeModel : QQmlTreeModel {
  using QQmlTreeModel::firstRow;
  using QQmlTreeModel::setInitialRows;
};

//  A QQmlTreeModel that Python can take functions over in. Every QQmlTreeModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
typedef bool (*CuteQQmlTreeModelCall0)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
typedef const QModelIndex * (*CuteQQmlTreeModelCall1)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
typedef int (*CuteQQmlTreeModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
typedef int (*CuteQQmlTreeModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
typedef const QModelIndex * (*CuteQQmlTreeModelCall4)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
typedef const QVariant * (*CuteQQmlTreeModelCall5)(const void *, int *);
#endif  // QT_CONFIG(qml_tree_model)
#if QT_CONFIG(qml_tree_model)
typedef void (*CuteQQmlTreeModelCall6)(const void *, int *);
#endif  // QT_CONFIG(qml_tree_model)
#if QT_CONFIG(qml_tree_model)
typedef const QVariant * (*CuteQQmlTreeModelCall7)(const void *, const QModelIndex *, const QString *, int *);
#endif  // QT_CONFIG(qml_tree_model)
#if QT_CONFIG(qml_tree_model)
typedef void (*CuteQQmlTreeModelCall8)(const void *, const QModelIndex *, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(qml_tree_model)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQQmlTreeModelCall9)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall10)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlTreeModelCall11)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTreeModelCall12)(const void *, int *);
typedef void (*CuteQQmlTreeModelCall13)(const void *, int *);
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlTreeModelCall14)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQQmlTreeModelCall16)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall17)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall18)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall19)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlTreeModelCall21)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlTreeModelCall22)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall23)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall24)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall25)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall26)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall27)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTreeModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTreeModelCall30)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlTreeModelCall31)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQQmlTreeModelCall32)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTreeModelCall33)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTreeModelCall34)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTreeModelCall35)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTreeModelCall36)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlTreeModelCall37)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlTreeModelCall38)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTreeModelCall39)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTreeModelCall40)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTreeModelCall41)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTreeModelCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTreeModelCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlTreeModel : public QQmlTreeModel {
public:
  using QQmlTreeModel::QQmlTreeModel;
  void *taken[44] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
    if (!std::strcmp(key, "_ZNK23QQmlAbstractColumnModel8firstRowEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_tree_model)
#if QT_CONFIG(qml_tree_model)
    if (!std::strcmp(key, "_ZN23QQmlAbstractColumnModel14setInitialRowsEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_tree_model)
#if QT_CONFIG(qml_tree_model)
    if (!std::strcmp(key, "_ZNK23QQmlAbstractColumnModel11dataPrivateERK11QModelIndexRK7QString")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_tree_model)
#if QT_CONFIG(qml_tree_model)
    if (!std::strcmp(key, "_ZN23QQmlAbstractColumnModel14setDataPrivateERK11QModelIndexRK7QString8QVariant")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_tree_model)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
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
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
  //  bool QQmlTreeModel::moveRows(const QModelIndex &fromIndex, int
  //      fromRowIndex, int rows, const QModelIndex &toIndex, int
  //      toRowIndex)
  bool moveRows(
      const QModelIndex &fromIndex,
      int fromRowIndex,
      int rows,
      const QModelIndex &toIndex,
      int toRowIndex) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlTreeModelCall0 call = reinterpret_cast<CuteQQmlTreeModelCall0>(taken[0]);
      bool given = call(this, &fromIndex, fromRowIndex, rows, &toIndex, toRowIndex, &handled);
      if (handled) return given;
    }
    return QQmlTreeModel::moveRows(fromIndex, fromRowIndex, rows, toIndex, toRowIndex);
  }
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
  //  QModelIndex QQmlTreeModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlTreeModelCall1 call = reinterpret_cast<CuteQQmlTreeModelCall1>(taken[1]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QQmlTreeModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
  //  int QQmlTreeModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlTreeModelCall2 call = reinterpret_cast<CuteQQmlTreeModelCall2>(taken[2]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QQmlTreeModel::rowCount(parent);
  }
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
  //  int QQmlTreeModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlTreeModelCall3 call = reinterpret_cast<CuteQQmlTreeModelCall3>(taken[3]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QQmlTreeModel::columnCount(parent);
  }
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_tree_model)
  //  QModelIndex QQmlTreeModel::parent(const QModelIndex &index) const
  QModelIndex parent(const QModelIndex &index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlTreeModelCall4 call = reinterpret_cast<CuteQQmlTreeModelCall4>(taken[4]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QQmlTreeModel::parent(index);
  }
#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(qml_tree_model)
  //  QVariant QQmlTreeModel::firstRow() const
  QVariant firstRow() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlTreeModelCall5 call = reinterpret_cast<CuteQQmlTreeModelCall5>(taken[5]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlTreeModel::firstRow();
  }
#endif  // QT_CONFIG(qml_tree_model)

#if QT_CONFIG(qml_tree_model)
  //  void QQmlTreeModel::setInitialRows()
  void setInitialRows() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlTreeModelCall6 call = reinterpret_cast<CuteQQmlTreeModelCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlTreeModel::setInitialRows();
  }
#endif  // QT_CONFIG(qml_tree_model)

#if QT_CONFIG(qml_tree_model)
  //  QVariant QQmlTreeModel::dataPrivate(const QModelIndex &index, const
  //      QString &roleName) const
  QVariant dataPrivate(
      const QModelIndex &index,
      const QString &roleName) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlTreeModelCall7 call = reinterpret_cast<CuteQQmlTreeModelCall7>(taken[7]);
      const QVariant * given = call(this, &index, &roleName, &handled);
      if (handled && given) return *given;
    }
    return QQmlTreeModel::dataPrivate(index, roleName);
  }
#endif  // QT_CONFIG(qml_tree_model)

#if QT_CONFIG(qml_tree_model)
  //  void QQmlTreeModel::setDataPrivate(const QModelIndex &index, const
  //      QString &roleName, QVariant value)
  void setDataPrivate(
      const QModelIndex &index,
      const QString &roleName,
      QVariant value) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlTreeModelCall8 call = reinterpret_cast<CuteQQmlTreeModelCall8>(taken[8]);
      call(this, &index, &roleName, &value, &handled);
      if (handled) return;
    }
    QQmlTreeModel::setDataPrivate(index, roleName, value);
  }
#endif  // QT_CONFIG(qml_tree_model)

#if QT_CONFIG(itemmodel)
  //  QVariant QQmlAbstractColumnModel::data(const QModelIndex &index, int
  //      role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlTreeModelCall9 call = reinterpret_cast<CuteQQmlTreeModelCall9>(taken[9]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QQmlAbstractColumnModel::data(index, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QQmlAbstractColumnModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlTreeModelCall10 call = reinterpret_cast<CuteQQmlTreeModelCall10>(taken[10]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QQmlAbstractColumnModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::ItemFlags QQmlAbstractColumnModel::flags(const QModelIndex
  //      &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlTreeModelCall11 call = reinterpret_cast<CuteQQmlTreeModelCall11>(taken[11]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QQmlAbstractColumnModel::flags(index);
  }
#endif  // QT_CONFIG(itemmodel)

  //  void QQmlAbstractColumnModel::classBegin()
  void classBegin() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlTreeModelCall12 call = reinterpret_cast<CuteQQmlTreeModelCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlAbstractColumnModel::classBegin();
  }

  //  void QQmlAbstractColumnModel::componentComplete()
  void componentComplete() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlTreeModelCall13 call = reinterpret_cast<CuteQQmlTreeModelCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlAbstractColumnModel::componentComplete();
  }

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlTreeModelCall14 call = reinterpret_cast<CuteQQmlTreeModelCall14>(taken[14]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlTreeModelCall15 call = reinterpret_cast<CuteQQmlTreeModelCall15>(taken[15]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QAbstractItemModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlTreeModelCall16 call = reinterpret_cast<CuteQQmlTreeModelCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQQmlTreeModelCall17 call = reinterpret_cast<CuteQQmlTreeModelCall17>(taken[17]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlTreeModelCall18 call = reinterpret_cast<CuteQQmlTreeModelCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQQmlTreeModelCall19 call = reinterpret_cast<CuteQQmlTreeModelCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQQmlTreeModelCall20 call = reinterpret_cast<CuteQQmlTreeModelCall20>(taken[20]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlTreeModelCall21 call = reinterpret_cast<CuteQQmlTreeModelCall21>(taken[21]);
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
      CuteQQmlTreeModelCall22 call = reinterpret_cast<CuteQQmlTreeModelCall22>(taken[22]);
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
      CuteQQmlTreeModelCall23 call = reinterpret_cast<CuteQQmlTreeModelCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQQmlTreeModelCall24 call = reinterpret_cast<CuteQQmlTreeModelCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQQmlTreeModelCall25 call = reinterpret_cast<CuteQQmlTreeModelCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQQmlTreeModelCall26 call = reinterpret_cast<CuteQQmlTreeModelCall26>(taken[26]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeColumns(column, count, parent);
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
    if (taken[27]) {
      int handled = 0;
      CuteQQmlTreeModelCall27 call = reinterpret_cast<CuteQQmlTreeModelCall27>(taken[27]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlTreeModelCall28 call = reinterpret_cast<CuteQQmlTreeModelCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQQmlTreeModelCall29 call = reinterpret_cast<CuteQQmlTreeModelCall29>(taken[29]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlTreeModelCall30 call = reinterpret_cast<CuteQQmlTreeModelCall30>(taken[30]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractItemModel::sort(column, order);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlTreeModelCall31 call = reinterpret_cast<CuteQQmlTreeModelCall31>(taken[31]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlTreeModelCall32 call = reinterpret_cast<CuteQQmlTreeModelCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQQmlTreeModelCall33 call = reinterpret_cast<CuteQQmlTreeModelCall33>(taken[33]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlTreeModelCall34 call = reinterpret_cast<CuteQQmlTreeModelCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQmlTreeModelCall35 call = reinterpret_cast<CuteQQmlTreeModelCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlTreeModelCall36 call = reinterpret_cast<CuteQQmlTreeModelCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlTreeModelCall37 call = reinterpret_cast<CuteQQmlTreeModelCall37>(taken[37]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlTreeModelCall38 call = reinterpret_cast<CuteQQmlTreeModelCall38>(taken[38]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlTreeModelCall39 call = reinterpret_cast<CuteQQmlTreeModelCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlTreeModelCall40 call = reinterpret_cast<CuteQQmlTreeModelCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlTreeModelCall41 call = reinterpret_cast<CuteQQmlTreeModelCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlTreeModelCall42 call = reinterpret_cast<CuteQQmlTreeModelCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlTreeModelCall43 call = reinterpret_cast<CuteQQmlTreeModelCall43>(taken[43]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlTreeModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QQmlTreeModel10metaObjectEv(
    const QQmlTreeModel *self) {
  return self->metaObject();
}

//  QString QQmlTreeModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQmlTreeModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlTreeModel::tr(s, c, n));
}

//  QQmlTreeModel::QQmlTreeModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlTreeModel *ritual_ZN13QQmlTreeModelC1EP7QObject(QObject *parent) {
  return new CuteQQmlTreeModel(parent);
}

//  QQmlTreeModel::~QQmlTreeModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModelD1Ev(QQmlTreeModel *self) {
  delete self;
}

//  QVariant QQmlTreeModel::rows() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QQmlTreeModel4rowsEv(const QQmlTreeModel *self) {
  return new QVariant(self->rows());
}

//  void QQmlTreeModel::setRows(const QVariant &rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel7setRowsERK8QVariant(
    QQmlTreeModel *self,
    const QVariant *rows) {
  self->setRows(*rows);
}

//  void QQmlTreeModel::appendRow(QModelIndex parent, const QVariant &row)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel9appendRowE11QModelIndexRK8QVariant(
    QQmlTreeModel *self,
    const QModelIndex *parent,
    const QVariant *row) {
  self->appendRow(*parent, *row);
}

//  void QQmlTreeModel::appendRow(const QVariant &row)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel9appendRowERK8QVariant(
    QQmlTreeModel *self,
    const QVariant *row) {
  self->appendRow(*row);
}

//  void QQmlTreeModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel5clearEv(QQmlTreeModel *self) {
  self->clear();
}

//  QVariant QQmlTreeModel::getRow(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QQmlTreeModel6getRowERK11QModelIndex(
    const QQmlTreeModel *self,
    const QModelIndex *index) {
  return new QVariant(self->getRow(*index));
}

//  void QQmlTreeModel::insertRow(int rowIndex, QModelIndex parent, const
//      QVariant &row)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel9insertRowEi11QModelIndexRK8QVariant(
    QQmlTreeModel *self,
    int rowIndex,
    const QModelIndex *parent,
    const QVariant *row) {
  self->insertRow(rowIndex, *parent, *row);
}

//  void QQmlTreeModel::insertRow(int rowIndex, const QVariant &row)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel9insertRowEiRK8QVariant(
    QQmlTreeModel *self,
    int rowIndex,
    const QVariant *row) {
  self->insertRow(rowIndex, *row);
}

//  bool QQmlTreeModel::moveRows(const QModelIndex &fromIndex, int
//      fromRowIndex, int rows, const QModelIndex &toIndex, int toRowIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QQmlTreeModel8moveRowsERK11QModelIndexiiS2_i(
    QQmlTreeModel *self,
    const QModelIndex *fromIndex,
    int fromRowIndex,
    int rows,
    const QModelIndex *toIndex,
    int toRowIndex) {
  return self->moveRows(
      *fromIndex,
      fromRowIndex,
      rows,
      *toIndex,
      toRowIndex);
}

//  void QQmlTreeModel::removeRow(QModelIndex index)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel9removeRowE11QModelIndex(
    QQmlTreeModel *self,
    const QModelIndex *index) {
  self->removeRow(*index);
}

//  void QQmlTreeModel::setRow(QModelIndex index, const QVariant &rowData)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel6setRowE11QModelIndexRK8QVariant(
    QQmlTreeModel *self,
    const QModelIndex *index,
    const QVariant *rowData) {
  self->setRow(*index, *rowData);
}

//  QModelIndex QQmlTreeModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK13QQmlTreeModel5indexEiiRK11QModelIndex(
    const QQmlTreeModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  int QQmlTreeModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQmlTreeModel8rowCountERK11QModelIndex(
    const QQmlTreeModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QQmlTreeModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQmlTreeModel11columnCountERK11QModelIndex(
    const QQmlTreeModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QModelIndex QQmlTreeModel::parent(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK13QQmlTreeModel6parentERK11QModelIndex(
    const QQmlTreeModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->parent(*index));
}

//  QVariant QQmlTreeModel::firstRow() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QQmlTreeModel8firstRowEv(const QQmlTreeModel *self) {
  return new QVariant(self->firstRow());
}

//  void QQmlTreeModel::setInitialRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel14setInitialRowsEv(QQmlTreeModel *self) {
  self->setInitialRows();
}

//  int QQmlTreeModel::treeSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QQmlTreeModel8treeSizeEv(const QQmlTreeModel *self) {
  return self->treeSize();
}

//  void QQmlTreeModel::setRowsPrivate(const QVariantList &rowsAsVariantList)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel14setRowsPrivateERK5QListI8QVariantE(
    QQmlTreeModel *self,
    const QList<QVariant> *rowsAsVariantList) {
  self->setRowsPrivate(*rowsAsVariantList);
}

//  QVariant QQmlTreeModel::dataPrivate(const QModelIndex &index, const
//      QString &roleName) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QQmlTreeModel11dataPrivateERK11QModelIndexRK7QString(
    const QQmlTreeModel *self,
    const QModelIndex *index,
    const QString *roleName) {
  return new QVariant(self->dataPrivate(*index, *roleName));
}

//  void QQmlTreeModel::setDataPrivate(const QModelIndex &index, const
//      QString &roleName, QVariant value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel14setDataPrivateERK11QModelIndexRK7QString8QVariant(
    QQmlTreeModel *self,
    const QModelIndex *index,
    const QString *roleName,
    const QVariant *value) {
  self->setDataPrivate(*index, *roleName, *value);
}

//  bool QQmlTreeModel::validateNewRow(QLatin1StringView functionName, const
//      QVariant &row, NewRowOperationFlag a2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlTreeModel14validateNewRowE13QLatin1StringRK8QVariantN23QQmlAbstractColumnModel19NewRowOperationFlagE(
    const QQmlTreeModel *self,
    const QLatin1String *functionName,
    const QVariant *row,
    QQmlAbstractColumnModel::NewRowOperationFlag a2) {
  return self->validateNewRow(*functionName, *row, a2);
}

//  void QQmlTreeModel::doInsert(const QModelIndex &index, int rowIndex,
//      const QVariant &row)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlTreeModel8doInsertERK11QModelIndexiRK8QVariant(
    QQmlTreeModel *self,
    const QModelIndex *index,
    int rowIndex,
    const QVariant *row) {
  self->doInsert(*index, rowIndex, *row);
}

//  a Python function taken by a CuteQQmlTreeModel, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlTreeModel(
    QQmlTreeModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlTreeModel *>(self)->take(key, call);
}

//  bool QQmlTreeModel::moveRows(const QModelIndex &fromIndex, int
//      fromRowIndex, int rows, const QModelIndex &toIndex, int toRowIndex)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QQmlTreeModel8moveRowsERK11QModelIndexiiS2_i(
    QQmlTreeModel *self,
    const QModelIndex *fromIndex,
    int fromRowIndex,
    int rows,
    const QModelIndex *toIndex,
    int toRowIndex) {
  return self->QQmlTreeModel::moveRows(
      *fromIndex,
      fromRowIndex,
      rows,
      *toIndex,
      toRowIndex);
}

//  QModelIndex QQmlTreeModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK13QQmlTreeModel5indexEiiRK11QModelIndex(
    const QQmlTreeModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->QQmlTreeModel::index(row, column, *parent));
}

//  int QQmlTreeModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QQmlTreeModel8rowCountERK11QModelIndex(
    const QQmlTreeModel *self,
    const QModelIndex *parent) {
  return self->QQmlTreeModel::rowCount(*parent);
}

//  int QQmlTreeModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QQmlTreeModel11columnCountERK11QModelIndex(
    const QQmlTreeModel *self,
    const QModelIndex *parent) {
  return self->QQmlTreeModel::columnCount(*parent);
}

//  QModelIndex QQmlTreeModel::parent(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK13QQmlTreeModel6parentERK11QModelIndex(
    const QQmlTreeModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->QQmlTreeModel::parent(*index));
}

//  QVariant QQmlTreeModel::firstRow() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK13QQmlTreeModel8firstRowEv(
    const QQmlTreeModel *self) {
  return new QVariant(
      static_cast<const OwnQQmlTreeModel *>(self)->OwnQQmlTreeModel::firstRow());
}

//  void QQmlTreeModel::setInitialRows()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQmlTreeModel14setInitialRowsEv(QQmlTreeModel *self) {
  static_cast<OwnQQmlTreeModel *>(self)->OwnQQmlTreeModel::setInitialRows();
}

//  QVariant QQmlTreeModel::dataPrivate(const QModelIndex &index, const
//      QString &roleName) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK13QQmlTreeModel11dataPrivateERK11QModelIndexRK7QString(
    const QQmlTreeModel *self,
    const QModelIndex *index,
    const QString *roleName) {
  return new QVariant(self->QQmlTreeModel::dataPrivate(*index, *roleName));
}

//  void QQmlTreeModel::setDataPrivate(const QModelIndex &index, const
//      QString &roleName, QVariant value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QQmlTreeModel14setDataPrivateERK11QModelIndexRK7QString8QVariant(
    QQmlTreeModel *self,
    const QModelIndex *index,
    const QString *roleName,
    const QVariant *value) {
  self->QQmlTreeModel::setDataPrivate(*index, *roleName, *value);
}

#endif  // QT_CONFIG(qml_tree_model)
#endif  // QT_CONFIG(qml_tree_model)
