//  Written by dev_tooling.RitualGenerator from the records of QtLabsQmlModel
//  s/6.12.0/QtLabsQmlModels/private/qqmlabstractcolumnmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtCore/qglobal.h>
#include <QtLabsQmlModels/qtlabsqmlmodelsexports.h>
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_table_model)
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlmodelsglobal_p.h>
#include <QtLabsQmlModels/QtLabsQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlabstractcolumnmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlatin1stringview.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QString>
#include <optional>
#include <QtCore/QVariantList>
#include <QtCore/QVariant>

//  Only a class built on QQmlAbstractColumnModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlAbstractColumnModel : QQmlAbstractColumnModel {
  using QQmlAbstractColumnModel::classBegin;
  using QQmlAbstractColumnModel::componentComplete;
};

//  A QQmlAbstractColumnModel that Python can take functions over in. Every QQmlAbstractColumnModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQQmlAbstractColumnModelCall0)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall1)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlAbstractColumnModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
typedef void (*CuteQQmlAbstractColumnModelCall3)(const void *, int *);
typedef void (*CuteQQmlAbstractColumnModelCall4)(const void *, int *);
typedef const QVariant * (*CuteQQmlAbstractColumnModelCall5)(const void *, int *);
typedef void (*CuteQQmlAbstractColumnModelCall6)(const void *, int *);
typedef const QVariant * (*CuteQQmlAbstractColumnModelCall7)(const void *, const QModelIndex *, const QString *, int *);
typedef void (*CuteQQmlAbstractColumnModelCall8)(const void *, const QModelIndex *, const QString *, const QVariant *, int *);
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlAbstractColumnModelCall9)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlAbstractColumnModelCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlAbstractColumnModelCall11)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlAbstractColumnModelCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlAbstractColumnModelCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQQmlAbstractColumnModelCall15)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall16)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall17)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall18)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall19)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlAbstractColumnModelCall20)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQQmlAbstractColumnModelCall21)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall22)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall23)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall24)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall25)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall26)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall27)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlAbstractColumnModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlAbstractColumnModelCall30)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQQmlAbstractColumnModelCall31)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQQmlAbstractColumnModelCall32)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlAbstractColumnModelCall33)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlAbstractColumnModelCall34)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlAbstractColumnModelCall35)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlAbstractColumnModelCall36)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAbstractColumnModelCall37)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAbstractColumnModelCall38)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractColumnModelCall39)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractColumnModelCall40)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractColumnModelCall41)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractColumnModelCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractColumnModelCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlAbstractColumnModel : public QQmlAbstractColumnModel {
public:
  using QQmlAbstractColumnModel::QQmlAbstractColumnModel;
  void *taken[44] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
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
    if (!std::strcmp(key, "_ZNK23QQmlAbstractColumnModel8firstRowEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQmlAbstractColumnModel14setInitialRowsEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QQmlAbstractColumnModel11dataPrivateERK11QModelIndexRK7QString")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QQmlAbstractColumnModel14setDataPrivateERK11QModelIndexRK7QString8QVariant")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
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
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
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
  //  QVariant QQmlAbstractColumnModel::data(const QModelIndex &index, int
  //      role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall0 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall1 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall2 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall2>(taken[2]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QQmlAbstractColumnModel::flags(index);
  }
#endif  // QT_CONFIG(itemmodel)

  //  void QQmlAbstractColumnModel::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall3 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlAbstractColumnModel::classBegin();
  }

  //  void QQmlAbstractColumnModel::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall4 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlAbstractColumnModel::componentComplete();
  }

  //  QVariant QQmlAbstractColumnModel::firstRow() const
  QVariant firstRow() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall5 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall5>(taken[5]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QQmlAbstractColumnModel::setInitialRows()
  void setInitialRows() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall6 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QVariant QQmlAbstractColumnModel::dataPrivate(const QModelIndex
  //      &index, const QString &roleName) const
  QVariant dataPrivate(
      const QModelIndex &index,
      const QString &roleName) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall7 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall7>(taken[7]);
      const QVariant * given = call(this, &index, &roleName, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QQmlAbstractColumnModel::setDataPrivate(const QModelIndex
  //      &index, const QString &roleName, QVariant value)
  void setDataPrivate(
      const QModelIndex &index,
      const QString &roleName,
      QVariant value) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall8 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall8>(taken[8]);
      call(this, &index, &roleName, &value, &handled);
      if (handled) return;
    }
  }

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall9 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall10 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall11 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall11>(taken[11]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractItemModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall12 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall12>(taken[12]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractItemModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall13 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall13>(taken[13]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlAbstractColumnModelCall14 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall14>(taken[14]);
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
      CuteQQmlAbstractColumnModelCall15 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall15>(taken[15]);
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
      CuteQQmlAbstractColumnModelCall16 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall16>(taken[16]);
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
      CuteQQmlAbstractColumnModelCall17 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall17>(taken[17]);
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
      CuteQQmlAbstractColumnModelCall18 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall18>(taken[18]);
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
      CuteQQmlAbstractColumnModelCall19 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall19>(taken[19]);
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
      CuteQQmlAbstractColumnModelCall20 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall20>(taken[20]);
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
      CuteQQmlAbstractColumnModelCall21 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall21>(taken[21]);
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
      CuteQQmlAbstractColumnModelCall22 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall22>(taken[22]);
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
      CuteQQmlAbstractColumnModelCall23 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall23>(taken[23]);
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
      CuteQQmlAbstractColumnModelCall24 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall24>(taken[24]);
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
      CuteQQmlAbstractColumnModelCall25 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall25>(taken[25]);
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
      CuteQQmlAbstractColumnModelCall26 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall26>(taken[26]);
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
      CuteQQmlAbstractColumnModelCall27 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall27>(taken[27]);
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
      CuteQQmlAbstractColumnModelCall28 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall28>(taken[28]);
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
      CuteQQmlAbstractColumnModelCall29 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall29>(taken[29]);
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
      CuteQQmlAbstractColumnModelCall30 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall30>(taken[30]);
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
      CuteQQmlAbstractColumnModelCall31 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall31>(taken[31]);
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
      CuteQQmlAbstractColumnModelCall32 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall32>(taken[32]);
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
      CuteQQmlAbstractColumnModelCall33 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall33>(taken[33]);
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
      CuteQQmlAbstractColumnModelCall34 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall34>(taken[34]);
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
      CuteQQmlAbstractColumnModelCall35 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall35>(taken[35]);
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
      CuteQQmlAbstractColumnModelCall36 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall36>(taken[36]);
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
      CuteQQmlAbstractColumnModelCall37 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall37>(taken[37]);
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
      CuteQQmlAbstractColumnModelCall38 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall38>(taken[38]);
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
      CuteQQmlAbstractColumnModelCall39 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall39>(taken[39]);
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
      CuteQQmlAbstractColumnModelCall40 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall40>(taken[40]);
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
      CuteQQmlAbstractColumnModelCall41 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall41>(taken[41]);
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
      CuteQQmlAbstractColumnModelCall42 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall42>(taken[42]);
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
      CuteQQmlAbstractColumnModelCall43 call = reinterpret_cast<CuteQQmlAbstractColumnModelCall43>(taken[43]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlAbstractColumnModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQmlAbstractColumnModel10metaObjectEv(
    const QQmlAbstractColumnModel *self) {
  return self->metaObject();
}

//  void *QQmlAbstractColumnModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQmlAbstractColumnModel11qt_metacastEPKc(
    QQmlAbstractColumnModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlAbstractColumnModel::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQmlAbstractColumnModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlAbstractColumnModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlAbstractColumnModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQmlAbstractColumnModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlAbstractColumnModel::tr(s, c, n));
}

//  void QQmlAbstractColumnModel::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel22qt_qmlMarker_anonymousEv(
    QQmlAbstractColumnModel *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQmlAbstractColumnModel::QQmlAbstractColumnModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlAbstractColumnModel *ritual_ZN23QQmlAbstractColumnModelC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlAbstractColumnModel(parent);
}

//  QQmlAbstractColumnModel::~QQmlAbstractColumnModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModelD1Ev(QQmlAbstractColumnModel *self) {
  delete self;
}

//  QQmlListProperty<QQmlTableModelColumn> QQmlAbstractColumnModel::columns()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQmlTableModelColumn> *ritual_ZN23QQmlAbstractColumnModel7columnsEv(
    QQmlAbstractColumnModel *self) {
  return new QQmlListProperty<QQmlTableModelColumn>(self->columns());
}

//  void QQmlAbstractColumnModel::columns_append(QQmlListProperty<QQmlTableMo
//      delColumn> *property, QQmlTableModelColumn *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel14columns_appendEP16QQmlListPropertyI20QQmlTableModelColumnEPS1_(
    QQmlListProperty<QQmlTableModelColumn> *property,
    QQmlTableModelColumn *value) {
  QQmlAbstractColumnModel::columns_append(property, value);
}

//  qsizetype QQmlAbstractColumnModel::columns_count(QQmlListProperty<QQmlTab
//      leModelColumn> *property)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN23QQmlAbstractColumnModel13columns_countEP16QQmlListPropertyI20QQmlTableModelColumnE(
    QQmlListProperty<QQmlTableModelColumn> *property) {
  return QQmlAbstractColumnModel::columns_count(property);
}

//  QQmlTableModelColumn *QQmlAbstractColumnModel::columns_at(QQmlListPropert
//      y<QQmlTableModelColumn> *property, qsizetype index)
extern "C" Q_DECL_EXPORT
QQmlTableModelColumn *ritual_ZN23QQmlAbstractColumnModel10columns_atEP16QQmlListPropertyI20QQmlTableModelColumnEx(
    QQmlListProperty<QQmlTableModelColumn> *property,
    qsizetype index) {
  return QQmlAbstractColumnModel::columns_at(property, index);
}

//  void QQmlAbstractColumnModel::columns_clear(QQmlListProperty<QQmlTableMod
//      elColumn> *property)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel13columns_clearEP16QQmlListPropertyI20QQmlTableModelColumnE(
    QQmlListProperty<QQmlTableModelColumn> *property) {
  QQmlAbstractColumnModel::columns_clear(property);
}

//  void QQmlAbstractColumnModel::columns_replace(QQmlListProperty<QQmlTableM
//      odelColumn> *property, qsizetype index, QQmlTableModelColumn *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel15columns_replaceEP16QQmlListPropertyI20QQmlTableModelColumnExPS1_(
    QQmlListProperty<QQmlTableModelColumn> *property,
    qsizetype index,
    QQmlTableModelColumn *value) {
  QQmlAbstractColumnModel::columns_replace(property, index, value);
}

//  void QQmlAbstractColumnModel::columns_removeLast(QQmlListProperty<QQmlTab
//      leModelColumn> *property)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel18columns_removeLastEP16QQmlListPropertyI20QQmlTableModelColumnE(
    QQmlListProperty<QQmlTableModelColumn> *property) {
  QQmlAbstractColumnModel::columns_removeLast(property);
}

//  QVariant QQmlAbstractColumnModel::data(const QModelIndex &index, const
//      QString &role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QQmlAbstractColumnModel4dataERK11QModelIndexRK7QString(
    const QQmlAbstractColumnModel *self,
    const QModelIndex *index,
    const QString *role) {
  return new QVariant(self->data(*index, *role));
}

//  QVariant QQmlAbstractColumnModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QQmlAbstractColumnModel4dataERK11QModelIndexi(
    const QQmlAbstractColumnModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QQmlAbstractColumnModel::setData(const QModelIndex &index, const
//      QVariant &value, const QString &role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQmlAbstractColumnModel7setDataERK11QModelIndexRK8QVariantRK7QString(
    QQmlAbstractColumnModel *self,
    const QModelIndex *index,
    const QVariant *value,
    const QString *role) {
  return self->setData(*index, *value, *role);
}

//  bool QQmlAbstractColumnModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQmlAbstractColumnModel7setDataERK11QModelIndexRK8QVarianti(
    QQmlAbstractColumnModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QHash<int, QByteArray> QQmlAbstractColumnModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK23QQmlAbstractColumnModel9roleNamesEv(
    const QQmlAbstractColumnModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  Qt::ItemFlags QQmlAbstractColumnModel::flags(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQmlAbstractColumnModel5flagsERK11QModelIndex(
    const QQmlAbstractColumnModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  void QQmlAbstractColumnModel::columnCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel18columnCountChangedEv(
    QQmlAbstractColumnModel *self) {
  self->columnCountChanged();
}

//  void QQmlAbstractColumnModel::rowsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel11rowsChangedEv(
    QQmlAbstractColumnModel *self) {
  self->rowsChanged();
}

//  void QQmlAbstractColumnModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel10classBeginEv(
    QQmlAbstractColumnModel *self) {
  self->classBegin();
}

//  void QQmlAbstractColumnModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel17componentCompleteEv(
    QQmlAbstractColumnModel *self) {
  self->componentComplete();
}

//  QVariant QQmlAbstractColumnModel::firstRow() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QQmlAbstractColumnModel8firstRowEv(
    const QQmlAbstractColumnModel *self) {
  return new QVariant(self->firstRow());
}

//  void QQmlAbstractColumnModel::setInitialRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel14setInitialRowsEv(
    QQmlAbstractColumnModel *self) {
  self->setInitialRows();
}

//  QVariant QQmlAbstractColumnModel::dataPrivate(const QModelIndex &index,
//      const QString &roleName) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QQmlAbstractColumnModel11dataPrivateERK11QModelIndexRK7QString(
    const QQmlAbstractColumnModel *self,
    const QModelIndex *index,
    const QString *roleName) {
  return new QVariant(self->dataPrivate(*index, *roleName));
}

//  void QQmlAbstractColumnModel::setDataPrivate(const QModelIndex &index,
//      const QString &roleName, QVariant value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel14setDataPrivateERK11QModelIndexRK7QString8QVariant(
    QQmlAbstractColumnModel *self,
    const QModelIndex *index,
    const QString *roleName,
    const QVariant *value) {
  self->setDataPrivate(*index, *roleName, *value);
}

//  ColumnRoleMetadata QQmlAbstractColumnModel::fetchColumnRoleData(const
//      QString &roleNameKey, QQmlTableModelColumn *tableModelColumn, int
//      columnIndex) const
extern "C" Q_DECL_EXPORT
QQmlAbstractColumnModel::ColumnRoleMetadata *ritual_ZNK23QQmlAbstractColumnModel19fetchColumnRoleDataERK7QStringP20QQmlTableModelColumni(
    const QQmlAbstractColumnModel *self,
    const QString *roleNameKey,
    QQmlTableModelColumn *tableModelColumn,
    int columnIndex) {
  return new QQmlAbstractColumnModel::ColumnRoleMetadata(
      self->fetchColumnRoleData(
          *roleNameKey,
          tableModelColumn,
          columnIndex));
}

//  void QQmlAbstractColumnModel::fetchColumnMetadata()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlAbstractColumnModel19fetchColumnMetadataEv(
    QQmlAbstractColumnModel *self) {
  self->fetchColumnMetadata();
}

//  bool QQmlAbstractColumnModel::validateRowType(QLatin1StringView
//      functionName, const QVariant &row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQmlAbstractColumnModel15validateRowTypeE13QLatin1StringRK8QVariant(
    const QQmlAbstractColumnModel *self,
    const QLatin1String *functionName,
    const QVariant *row) {
  return self->validateRowType(*functionName, *row);
}

//  bool QQmlAbstractColumnModel::validateNewRow(QLatin1StringView
//      functionName, const QVariant &row, NewRowOperationFlag operation)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQmlAbstractColumnModel14validateNewRowE13QLatin1StringRK8QVariantNS_19NewRowOperationFlagE(
    const QQmlAbstractColumnModel *self,
    const QLatin1String *functionName,
    const QVariant *row,
    QQmlAbstractColumnModel::NewRowOperationFlag operation) {
  return self->validateNewRow(*functionName, *row, operation);
}

//  QLatin1StringView QQmlAbstractColumnModel::jsTypeName(const QJSValue &v)
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZN23QQmlAbstractColumnModel10jsTypeNameERK8QJSValue(
    const QJSValue *v) {
  return new QLatin1String(QQmlAbstractColumnModel::jsTypeName(*v));
}

//  std::optional<QVariantList>
//      QQmlAbstractColumnModel::validateRowsArgument(const QVariant &rows)
//      const
extern "C" Q_DECL_EXPORT
std::optional<QVariantList> *ritual_ZNK23QQmlAbstractColumnModel20validateRowsArgumentERK8QVariant(
    const QQmlAbstractColumnModel *self,
    const QVariant *rows) {
  return new std::optional<QVariantList>(self->validateRowsArgument(*rows));
}

//  QQmlAbstractColumnModel as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlAbstractColumnModel_QQmlParserStatus(
    QQmlAbstractColumnModel *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlAbstractColumnModel, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlAbstractColumnModel(
    QQmlAbstractColumnModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlAbstractColumnModel *>(self)->take(key, call);
}

//  QVariant QQmlAbstractColumnModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QQmlAbstractColumnModel4dataERK11QModelIndexi(
    const QQmlAbstractColumnModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QQmlAbstractColumnModel::data(*index, role));
}

//  bool QQmlAbstractColumnModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QQmlAbstractColumnModel7setDataERK11QModelIndexRK8QVarianti(
    QQmlAbstractColumnModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QQmlAbstractColumnModel::setData(*index, *value, role);
}

//  Qt::ItemFlags QQmlAbstractColumnModel::flags(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QQmlAbstractColumnModel5flagsERK11QModelIndex(
    const QQmlAbstractColumnModel *self,
    const QModelIndex *index) {
  return static_cast<int>(
      self->QQmlAbstractColumnModel::flags(
          *index).toInt());
}

//  void QQmlAbstractColumnModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQmlAbstractColumnModel10classBeginEv(
    QQmlAbstractColumnModel *self) {
  static_cast<OwnQQmlAbstractColumnModel *>(self)->OwnQQmlAbstractColumnModel::classBegin();
}

//  void QQmlAbstractColumnModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QQmlAbstractColumnModel17componentCompleteEv(
    QQmlAbstractColumnModel *self) {
  static_cast<OwnQQmlAbstractColumnModel *>(self)->OwnQQmlAbstractColumnModel::componentComplete();
}

//  a QQmlListProperty<QQmlTableModelColumn> a ritual of
//      QQmlAbstractColumnModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlAbstractColumnModel__QQmlListProperty_QQmlTableModelColumn(
    QQmlListProperty<QQmlTableModelColumn> *self) {
  delete self;
}

//  a QQmlAbstractColumnModel::ColumnRoleMetadata a ritual of
//      QQmlAbstractColumnModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlAbstractColumnModel__QQmlAbstractColumnModel_ColumnRoleMetadata(
    QQmlAbstractColumnModel::ColumnRoleMetadata *self) {
  delete self;
}

//  a std::optional<QVariantList> a ritual of QQmlAbstractColumnModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlAbstractColumnModel__std_optional_QVariantList(
    std::optional<QVariantList> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_table_model)
