//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltablemodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtCore/qglobal.h>
#include <QtLabsQmlModels/qtlabsqmlmodelsexports.h>
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlmodelsglobal_p.h>
#include <QtLabsQmlModels/QtLabsQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltablemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQmlTableModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlTableModel : QQmlTableModel {
  using QQmlTableModel::firstRow;
  using QQmlTableModel::setInitialRows;
};

//  A QQmlTableModel that Python can take functions over in. Every QQmlTableModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
typedef const QModelIndex * (*CuteQQmlTableModelCall0)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
typedef int (*CuteQQmlTableModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
typedef int (*CuteQQmlTableModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
typedef const QModelIndex * (*CuteQQmlTableModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
typedef const QVariant * (*CuteQQmlTableModelCall4)(const void *, int *);
#endif  // QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
typedef void (*CuteQQmlTableModelCall5)(const void *, int *);
#endif  // QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
typedef const QVariant * (*CuteQQmlTableModelCall6)(const void *, const QModelIndex *, const QString *, int *);
#endif  // QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
typedef void (*CuteQQmlTableModelCall7)(const void *, const QModelIndex *, const QString *, const QVariant *, int *);
#endif  // QT_CONFIG(qml_table_model)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQQmlTableModelCall8)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall9)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlTableModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTableModelCall11)(const void *, int *);
typedef void (*CuteQQmlTableModelCall12)(const void *, int *);
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlTableModelCall13)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQQmlTableModelCall15)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall16)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall17)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall18)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall19)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlTableModelCall20)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlTableModelCall21)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall22)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall23)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall24)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall25)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall26)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall27)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTableModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTableModelCall30)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlTableModelCall31)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQQmlTableModelCall32)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTableModelCall33)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlTableModelCall34)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTableModelCall35)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlTableModelCall36)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlTableModelCall37)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlTableModelCall38)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableModelCall39)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableModelCall40)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableModelCall41)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableModelCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlTableModelCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlTableModel : public QQmlTableModel {
public:
  using QQmlTableModel::QQmlTableModel;
  void *taken[44] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZNK23QQmlAbstractColumnModel8firstRowEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN23QQmlAbstractColumnModel14setInitialRowsEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZNK23QQmlAbstractColumnModel11dataPrivateERK11QModelIndexRK7QString")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN23QQmlAbstractColumnModel14setDataPrivateERK11QModelIndexRK7QString8QVariant")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
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
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
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
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
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
#if QT_CONFIG(qml_table_model)
  //  QModelIndex QQmlTableModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlTableModelCall0 call = reinterpret_cast<CuteQQmlTableModelCall0>(taken[0]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QQmlTableModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
  //  int QQmlTableModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlTableModelCall1 call = reinterpret_cast<CuteQQmlTableModelCall1>(taken[1]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QQmlTableModel::rowCount(parent);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
  //  int QQmlTableModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlTableModelCall2 call = reinterpret_cast<CuteQQmlTableModelCall2>(taken[2]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QQmlTableModel::columnCount(parent);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_table_model)
  //  QModelIndex QQmlTableModel::parent(const QModelIndex &index) const
  QModelIndex parent(const QModelIndex &index) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlTableModelCall3 call = reinterpret_cast<CuteQQmlTableModelCall3>(taken[3]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QQmlTableModel::parent(index);
  }
#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(qml_table_model)
  //  QVariant QQmlTableModel::firstRow() const
  QVariant firstRow() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlTableModelCall4 call = reinterpret_cast<CuteQQmlTableModelCall4>(taken[4]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlTableModel::firstRow();
  }
#endif  // QT_CONFIG(qml_table_model)

#if QT_CONFIG(qml_table_model)
  //  void QQmlTableModel::setInitialRows()
  void setInitialRows() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlTableModelCall5 call = reinterpret_cast<CuteQQmlTableModelCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlTableModel::setInitialRows();
  }
#endif  // QT_CONFIG(qml_table_model)

#if QT_CONFIG(qml_table_model)
  //  QVariant QQmlTableModel::dataPrivate(const QModelIndex &index, const
  //      QString &roleName) const
  QVariant dataPrivate(
      const QModelIndex &index,
      const QString &roleName) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlTableModelCall6 call = reinterpret_cast<CuteQQmlTableModelCall6>(taken[6]);
      const QVariant * given = call(this, &index, &roleName, &handled);
      if (handled && given) return *given;
    }
    return QQmlTableModel::dataPrivate(index, roleName);
  }
#endif  // QT_CONFIG(qml_table_model)

#if QT_CONFIG(qml_table_model)
  //  void QQmlTableModel::setDataPrivate(const QModelIndex &index, const
  //      QString &roleName, QVariant value)
  void setDataPrivate(
      const QModelIndex &index,
      const QString &roleName,
      QVariant value) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlTableModelCall7 call = reinterpret_cast<CuteQQmlTableModelCall7>(taken[7]);
      call(this, &index, &roleName, &value, &handled);
      if (handled) return;
    }
    QQmlTableModel::setDataPrivate(index, roleName, value);
  }
#endif  // QT_CONFIG(qml_table_model)

#if QT_CONFIG(itemmodel)
  //  QVariant QQmlAbstractColumnModel::data(const QModelIndex &index, int
  //      role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlTableModelCall8 call = reinterpret_cast<CuteQQmlTableModelCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQQmlTableModelCall9 call = reinterpret_cast<CuteQQmlTableModelCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQQmlTableModelCall10 call = reinterpret_cast<CuteQQmlTableModelCall10>(taken[10]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QQmlAbstractColumnModel::flags(index);
  }
#endif  // QT_CONFIG(itemmodel)

  //  void QQmlAbstractColumnModel::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlTableModelCall11 call = reinterpret_cast<CuteQQmlTableModelCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlAbstractColumnModel::classBegin();
  }

  //  void QQmlAbstractColumnModel::componentComplete()
  void componentComplete() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlTableModelCall12 call = reinterpret_cast<CuteQQmlTableModelCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQQmlTableModelCall13 call = reinterpret_cast<CuteQQmlTableModelCall13>(taken[13]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlTableModelCall14 call = reinterpret_cast<CuteQQmlTableModelCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQQmlTableModelCall15 call = reinterpret_cast<CuteQQmlTableModelCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQQmlTableModelCall16 call = reinterpret_cast<CuteQQmlTableModelCall16>(taken[16]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlTableModelCall17 call = reinterpret_cast<CuteQQmlTableModelCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQQmlTableModelCall18 call = reinterpret_cast<CuteQQmlTableModelCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQQmlTableModelCall19 call = reinterpret_cast<CuteQQmlTableModelCall19>(taken[19]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlTableModelCall20 call = reinterpret_cast<CuteQQmlTableModelCall20>(taken[20]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractItemModel::supportedDropActions();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlTableModelCall21 call = reinterpret_cast<CuteQQmlTableModelCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQQmlTableModelCall22 call = reinterpret_cast<CuteQQmlTableModelCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQQmlTableModelCall23 call = reinterpret_cast<CuteQQmlTableModelCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQQmlTableModelCall24 call = reinterpret_cast<CuteQQmlTableModelCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQQmlTableModelCall25 call = reinterpret_cast<CuteQQmlTableModelCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQQmlTableModelCall26 call = reinterpret_cast<CuteQQmlTableModelCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQQmlTableModelCall27 call = reinterpret_cast<CuteQQmlTableModelCall27>(taken[27]);
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
      CuteQQmlTableModelCall28 call = reinterpret_cast<CuteQQmlTableModelCall28>(taken[28]);
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
      CuteQQmlTableModelCall29 call = reinterpret_cast<CuteQQmlTableModelCall29>(taken[29]);
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
      CuteQQmlTableModelCall30 call = reinterpret_cast<CuteQQmlTableModelCall30>(taken[30]);
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
      CuteQQmlTableModelCall31 call = reinterpret_cast<CuteQQmlTableModelCall31>(taken[31]);
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
      CuteQQmlTableModelCall32 call = reinterpret_cast<CuteQQmlTableModelCall32>(taken[32]);
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
      CuteQQmlTableModelCall33 call = reinterpret_cast<CuteQQmlTableModelCall33>(taken[33]);
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
      CuteQQmlTableModelCall34 call = reinterpret_cast<CuteQQmlTableModelCall34>(taken[34]);
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
      CuteQQmlTableModelCall35 call = reinterpret_cast<CuteQQmlTableModelCall35>(taken[35]);
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
      CuteQQmlTableModelCall36 call = reinterpret_cast<CuteQQmlTableModelCall36>(taken[36]);
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
      CuteQQmlTableModelCall37 call = reinterpret_cast<CuteQQmlTableModelCall37>(taken[37]);
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
      CuteQQmlTableModelCall38 call = reinterpret_cast<CuteQQmlTableModelCall38>(taken[38]);
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
      CuteQQmlTableModelCall39 call = reinterpret_cast<CuteQQmlTableModelCall39>(taken[39]);
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
      CuteQQmlTableModelCall40 call = reinterpret_cast<CuteQQmlTableModelCall40>(taken[40]);
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
      CuteQQmlTableModelCall41 call = reinterpret_cast<CuteQQmlTableModelCall41>(taken[41]);
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
      CuteQQmlTableModelCall42 call = reinterpret_cast<CuteQQmlTableModelCall42>(taken[42]);
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
      CuteQQmlTableModelCall43 call = reinterpret_cast<CuteQQmlTableModelCall43>(taken[43]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlTableModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQmlTableModel10metaObjectEv(
    const QQmlTableModel *self) {
  return self->metaObject();
}

//  void *QQmlTableModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQmlTableModel11qt_metacastEPKc(
    QQmlTableModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlTableModel::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQmlTableModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlTableModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlTableModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQmlTableModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlTableModel::tr(s, c, n));
}

//  QQmlTableModel::QQmlTableModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlTableModel *ritual_ZN14QQmlTableModelC1EP7QObject(QObject *parent) {
  return new CuteQQmlTableModel(parent);
}

//  QQmlTableModel::~QQmlTableModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModelD1Ev(QQmlTableModel *self) {
  delete self;
}

//  QVariant QQmlTableModel::rows() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQmlTableModel4rowsEv(const QQmlTableModel *self) {
  return new QVariant(self->rows());
}

//  void QQmlTableModel::setRows(const QVariant &rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel7setRowsERK8QVariant(
    QQmlTableModel *self,
    const QVariant *rows) {
  self->setRows(*rows);
}

//  void QQmlTableModel::appendRow(const QVariant &row)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel9appendRowERK8QVariant(
    QQmlTableModel *self,
    const QVariant *row) {
  self->appendRow(*row);
}

//  void QQmlTableModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel5clearEv(QQmlTableModel *self) {
  self->clear();
}

//  QVariant QQmlTableModel::getRow(int rowIndex)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN14QQmlTableModel6getRowEi(
    QQmlTableModel *self,
    int rowIndex) {
  return new QVariant(self->getRow(rowIndex));
}

//  void QQmlTableModel::insertRow(int rowIndex, const QVariant &row)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel9insertRowEiRK8QVariant(
    QQmlTableModel *self,
    int rowIndex,
    const QVariant *row) {
  self->insertRow(rowIndex, *row);
}

//  void QQmlTableModel::moveRow(int fromRowIndex, int toRowIndex, int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel7moveRowEiii(
    QQmlTableModel *self,
    int fromRowIndex,
    int toRowIndex,
    int rows) {
  self->moveRow(fromRowIndex, toRowIndex, rows);
}

//  void QQmlTableModel::removeRow(int rowIndex, int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel9removeRowEii(
    QQmlTableModel *self,
    int rowIndex,
    int rows) {
  self->removeRow(rowIndex, rows);
}

//  void QQmlTableModel::setRow(int rowIndex, const QVariant &row)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel6setRowEiRK8QVariant(
    QQmlTableModel *self,
    int rowIndex,
    const QVariant *row) {
  self->setRow(rowIndex, *row);
}

//  QModelIndex QQmlTableModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK14QQmlTableModel5indexEiiRK11QModelIndex(
    const QQmlTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  int QQmlTableModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlTableModel8rowCountERK11QModelIndex(
    const QQmlTableModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QQmlTableModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlTableModel11columnCountERK11QModelIndex(
    const QQmlTableModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QModelIndex QQmlTableModel::parent(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK14QQmlTableModel6parentERK11QModelIndex(
    const QQmlTableModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->parent(*index));
}

//  void QQmlTableModel::rowCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel15rowCountChangedEv(QQmlTableModel *self) {
  self->rowCountChanged();
}

//  QVariant QQmlTableModel::firstRow() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQmlTableModel8firstRowEv(const QQmlTableModel *self) {
  return new QVariant(self->firstRow());
}

//  void QQmlTableModel::setInitialRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel14setInitialRowsEv(QQmlTableModel *self) {
  self->setInitialRows();
}

//  void QQmlTableModel::setRowsPrivate(const QVariantList
//      &rowsAsVariantList)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel14setRowsPrivateERK5QListI8QVariantE(
    QQmlTableModel *self,
    const QList<QVariant> *rowsAsVariantList) {
  self->setRowsPrivate(*rowsAsVariantList);
}

//  QVariant QQmlTableModel::dataPrivate(const QModelIndex &index, const
//      QString &roleName) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQmlTableModel11dataPrivateERK11QModelIndexRK7QString(
    const QQmlTableModel *self,
    const QModelIndex *index,
    const QString *roleName) {
  return new QVariant(self->dataPrivate(*index, *roleName));
}

//  void QQmlTableModel::setDataPrivate(const QModelIndex &index, const
//      QString &roleName, QVariant value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel14setDataPrivateERK11QModelIndexRK7QString8QVariant(
    QQmlTableModel *self,
    const QModelIndex *index,
    const QString *roleName,
    const QVariant *value) {
  self->setDataPrivate(*index, *roleName, *value);
}

//  bool QQmlTableModel::validateRowIndex(QLatin1StringView functionName,
//      QLatin1StringView argumentName, int rowIndex, RowOption operation)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlTableModel16validateRowIndexE13QLatin1StringS0_iNS_9RowOptionE(
    const QQmlTableModel *self,
    const QLatin1String *functionName,
    const QLatin1String *argumentName,
    int rowIndex,
    QQmlTableModel::RowOption operation) {
  return self->validateRowIndex(
      *functionName,
      *argumentName,
      rowIndex,
      operation);
}

//  void QQmlTableModel::doInsert(int rowIndex, const QVariant &row)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlTableModel8doInsertEiRK8QVariant(
    QQmlTableModel *self,
    int rowIndex,
    const QVariant *row) {
  self->doInsert(rowIndex, *row);
}

//  a Python function taken by a CuteQQmlTableModel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlTableModel(
    QQmlTableModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlTableModel *>(self)->take(key, call);
}

//  QModelIndex QQmlTableModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK14QQmlTableModel5indexEiiRK11QModelIndex(
    const QQmlTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->QQmlTableModel::index(row, column, *parent));
}

//  int QQmlTableModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QQmlTableModel8rowCountERK11QModelIndex(
    const QQmlTableModel *self,
    const QModelIndex *parent) {
  return self->QQmlTableModel::rowCount(*parent);
}

//  int QQmlTableModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QQmlTableModel11columnCountERK11QModelIndex(
    const QQmlTableModel *self,
    const QModelIndex *parent) {
  return self->QQmlTableModel::columnCount(*parent);
}

//  QModelIndex QQmlTableModel::parent(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK14QQmlTableModel6parentERK11QModelIndex(
    const QQmlTableModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->QQmlTableModel::parent(*index));
}

//  QVariant QQmlTableModel::firstRow() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QQmlTableModel8firstRowEv(
    const QQmlTableModel *self) {
  return new QVariant(
      static_cast<const OwnQQmlTableModel *>(self)->OwnQQmlTableModel::firstRow());
}

//  void QQmlTableModel::setInitialRows()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQmlTableModel14setInitialRowsEv(QQmlTableModel *self) {
  static_cast<OwnQQmlTableModel *>(self)->OwnQQmlTableModel::setInitialRows();
}

//  QVariant QQmlTableModel::dataPrivate(const QModelIndex &index, const
//      QString &roleName) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QQmlTableModel11dataPrivateERK11QModelIndexRK7QString(
    const QQmlTableModel *self,
    const QModelIndex *index,
    const QString *roleName) {
  return new QVariant(self->QQmlTableModel::dataPrivate(*index, *roleName));
}

//  void QQmlTableModel::setDataPrivate(const QModelIndex &index, const
//      QString &roleName, QVariant value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQmlTableModel14setDataPrivateERK11QModelIndexRK7QString8QVariant(
    QQmlTableModel *self,
    const QModelIndex *index,
    const QString *roleName,
    const QVariant *value) {
  self->QQmlTableModel::setDataPrivate(*index, *roleName, *value);
}

#endif  // QT_CONFIG(qml_table_model)
#endif  // QT_CONFIG(qml_table_model)
