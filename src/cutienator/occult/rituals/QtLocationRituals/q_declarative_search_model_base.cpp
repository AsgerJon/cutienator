//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativesearchmodelbase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativesearchmodelbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtLocation/qplacesearchrequest.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QDeclarativeSearchModelBase may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativeSearchModelBase : QDeclarativeSearchModelBase {
  using QDeclarativeSearchModelBase::initializePlugin;
  using QDeclarativeSearchModelBase::onContentUpdated;
};

//  A QDeclarativeSearchModelBase that Python can take functions over in. Every QDeclarativeSearchModelBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeSearchModelBaseCall0)(const void *, bool, int *);
typedef void (*CuteQDeclarativeSearchModelBaseCall1)(const void *, int *);
typedef void (*CuteQDeclarativeSearchModelBaseCall2)(const void *, int *);
typedef void (*CuteQDeclarativeSearchModelBaseCall3)(const void *, QDeclarativeGeoServiceProvider *, int *);
typedef void (*CuteQDeclarativeSearchModelBaseCall4)(const void *, int *);
typedef void (*CuteQDeclarativeSearchModelBaseCall5)(const void *, int *);
typedef void * (*CuteQDeclarativeSearchModelBaseCall6)(const void *, QPlaceManager *, const QPlaceSearchRequest *, int *);
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchModelBaseCall7)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchModelBaseCall8)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall9)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchModelBaseCall10)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchModelBaseCall11)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchModelBaseCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchModelBaseCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQDeclarativeSearchModelBaseCall15)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall16)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQDeclarativeSearchModelBaseCall17)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall18)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall19)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchModelBaseCall21)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchModelBaseCall22)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall23)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall24)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall25)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall26)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall27)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall28)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchModelBaseCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall30)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchModelBaseCall31)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchModelBaseCall32)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQDeclarativeSearchModelBaseCall33)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchModelBaseCall34)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchModelBaseCall35)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchModelBaseCall36)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchModelBaseCall37)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeSearchModelBaseCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeSearchModelBaseCall39)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchModelBaseCall40)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchModelBaseCall41)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchModelBaseCall42)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchModelBaseCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchModelBaseCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeSearchModelBase : public QDeclarativeSearchModelBase {
public:
  using QDeclarativeSearchModelBase::QDeclarativeSearchModelBase;
  void *taken[45] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase9clearDataEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase16initializePluginEP30QDeclarativeGeoServiceProvider")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase13queryFinishedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase16onContentUpdatedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase9sendQueryEP13QPlaceManagerRK19QPlaceSearchRequest")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
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
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
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
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QDeclarativeSearchModelBase::clearData(bool suppressSignal)
  void clearData(bool suppressSignal) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall0 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall0>(taken[0]);
      call(this, suppressSignal, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::clearData(suppressSignal);
  }

  //  void QDeclarativeSearchModelBase::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall1 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::classBegin();
  }

  //  void QDeclarativeSearchModelBase::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall2 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::componentComplete();
  }

  //  void QDeclarativeSearchModelBase::initializePlugin(QDeclarativeGeoSer
  //      viceProvider *plugin)
  void initializePlugin(QDeclarativeGeoServiceProvider *plugin) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall3 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall3>(taken[3]);
      call(this, plugin, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::initializePlugin(plugin);
  }

  //  void QDeclarativeSearchModelBase::queryFinished()
  void queryFinished() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall4 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QDeclarativeSearchModelBase::onContentUpdated()
  void onContentUpdated() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall5 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::onContentUpdated();
  }

  //  QPlaceReply *QDeclarativeSearchModelBase::sendQuery(QPlaceManager
  //      *manager, const QPlaceSearchRequest &request)
  QPlaceReply *sendQuery(
      QPlaceManager *manager,
      const QPlaceSearchRequest &request) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall6 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall6>(taken[6]);
      void * given = call(this, manager, &request, &handled);
      if (handled) return static_cast<QPlaceReply *>(given);
    }
    return {};
  }

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractListModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall7 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall8 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall9 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall10 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall11 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall11>(taken[11]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QAbstractListModel::parent(child);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractListModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall12 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall12>(taken[12]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractListModel::columnCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractListModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall13 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall13>(taken[13]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractListModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractItemModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall14 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall15 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall16 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall17 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall18 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall18>(taken[18]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall19 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall20 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall20>(taken[20]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  Qt::DropActions QAbstractItemModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall21 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall21>(taken[21]);
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
      CuteQDeclarativeSearchModelBaseCall22 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall22>(taken[22]);
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
      CuteQDeclarativeSearchModelBaseCall23 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall23>(taken[23]);
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
      CuteQDeclarativeSearchModelBaseCall24 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall24>(taken[24]);
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
      CuteQDeclarativeSearchModelBaseCall25 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall25>(taken[25]);
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
      CuteQDeclarativeSearchModelBaseCall26 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall27 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall28 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall28>(taken[28]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[29]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall29 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall30 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall30>(taken[30]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[31]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall31 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall31>(taken[31]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractItemModel::sort(column, order);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[32]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall32 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall32>(taken[32]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[33]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall33 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall33>(taken[33]);
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
    if (taken[34]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall34 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall34>(taken[34]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[35]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall35 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[36]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall36 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[37]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall37 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall38 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall38>(taken[38]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall39 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall39>(taken[39]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall40 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall41 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall42 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[43]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall43 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall43>(taken[43]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQDeclarativeSearchModelBaseCall44 call = reinterpret_cast<CuteQDeclarativeSearchModelBaseCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeSearchModelBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QDeclarativeSearchModelBase10metaObjectEv(
    const QDeclarativeSearchModelBase *self) {
  return self->metaObject();
}

//  QString QDeclarativeSearchModelBase::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDeclarativeSearchModelBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeSearchModelBase::tr(s, c, n));
}

//  QDeclarativeSearchModelBase::~QDeclarativeSearchModelBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBaseD1Ev(
    QDeclarativeSearchModelBase *self) {
  delete self;
}

//  QDeclarativeGeoServiceProvider *QDeclarativeSearchModelBase::plugin()
//      const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoServiceProvider *ritual_ZNK27QDeclarativeSearchModelBase6pluginEv(
    const QDeclarativeSearchModelBase *self) {
  return self->plugin();
}

//  void
//      QDeclarativeSearchModelBase::setPlugin(QDeclarativeGeoServiceProvider
//      *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase9setPluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativeSearchModelBase *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->setPlugin(plugin);
}

//  QVariant QDeclarativeSearchModelBase::searchArea() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27QDeclarativeSearchModelBase10searchAreaEv(
    const QDeclarativeSearchModelBase *self) {
  return new QVariant(self->searchArea());
}

//  void QDeclarativeSearchModelBase::setSearchArea(const QVariant
//      &searchArea)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase13setSearchAreaERK8QVariant(
    QDeclarativeSearchModelBase *self,
    const QVariant *searchArea) {
  self->setSearchArea(*searchArea);
}

//  int QDeclarativeSearchModelBase::limit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QDeclarativeSearchModelBase5limitEv(
    const QDeclarativeSearchModelBase *self) {
  return self->limit();
}

//  void QDeclarativeSearchModelBase::setLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase8setLimitEi(
    QDeclarativeSearchModelBase *self,
    int limit) {
  self->setLimit(limit);
}

//  bool QDeclarativeSearchModelBase::previousPagesAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDeclarativeSearchModelBase22previousPagesAvailableEv(
    const QDeclarativeSearchModelBase *self) {
  return self->previousPagesAvailable();
}

//  bool QDeclarativeSearchModelBase::nextPagesAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDeclarativeSearchModelBase18nextPagesAvailableEv(
    const QDeclarativeSearchModelBase *self) {
  return self->nextPagesAvailable();
}

//  Status QDeclarativeSearchModelBase::status() const
extern "C" Q_DECL_EXPORT
QDeclarativeSearchModelBase::Status ritual_ZNK27QDeclarativeSearchModelBase6statusEv(
    const QDeclarativeSearchModelBase *self) {
  return self->status();
}

//  void QDeclarativeSearchModelBase::setStatus(Status status, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase9setStatusENS_6StatusERK7QString(
    QDeclarativeSearchModelBase *self,
    QDeclarativeSearchModelBase::Status status,
    const QString *errorString) {
  self->setStatus(status, *errorString);
}

//  void QDeclarativeSearchModelBase::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase6updateEv(
    QDeclarativeSearchModelBase *self) {
  self->update();
}

//  void QDeclarativeSearchModelBase::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase6cancelEv(
    QDeclarativeSearchModelBase *self) {
  self->cancel();
}

//  void QDeclarativeSearchModelBase::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase5resetEv(
    QDeclarativeSearchModelBase *self) {
  self->reset();
}

//  QString QDeclarativeSearchModelBase::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QDeclarativeSearchModelBase11errorStringEv(
    const QDeclarativeSearchModelBase *self) {
  return new QString(self->errorString());
}

//  void QDeclarativeSearchModelBase::previousPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase12previousPageEv(
    QDeclarativeSearchModelBase *self) {
  self->previousPage();
}

//  void QDeclarativeSearchModelBase::nextPage()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase8nextPageEv(
    QDeclarativeSearchModelBase *self) {
  self->nextPage();
}

//  void QDeclarativeSearchModelBase::clearData(bool suppressSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase9clearDataEb(
    QDeclarativeSearchModelBase *self,
    bool suppressSignal) {
  self->clearData(suppressSignal);
}

//  void QDeclarativeSearchModelBase::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase10classBeginEv(
    QDeclarativeSearchModelBase *self) {
  self->classBegin();
}

//  void QDeclarativeSearchModelBase::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase17componentCompleteEv(
    QDeclarativeSearchModelBase *self) {
  self->componentComplete();
}

//  void QDeclarativeSearchModelBase::initializePlugin(QDeclarativeGeoService
//      Provider *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase16initializePluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativeSearchModelBase *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->initializePlugin(plugin);
}

//  void QDeclarativeSearchModelBase::queryFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase13queryFinishedEv(
    QDeclarativeSearchModelBase *self) {
  self->queryFinished();
}

//  void QDeclarativeSearchModelBase::onContentUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase16onContentUpdatedEv(
    QDeclarativeSearchModelBase *self) {
  self->onContentUpdated();
}

//  void QDeclarativeSearchModelBase::pluginNameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase17pluginNameChangedEv(
    QDeclarativeSearchModelBase *self) {
  self->pluginNameChanged();
}

//  QPlaceReply *QDeclarativeSearchModelBase::sendQuery(QPlaceManager
//      *manager, const QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceReply *ritual_ZN27QDeclarativeSearchModelBase9sendQueryEP13QPlaceManagerRK19QPlaceSearchRequest(
    QDeclarativeSearchModelBase *self,
    QPlaceManager *manager,
    const QPlaceSearchRequest *request) {
  return self->sendQuery(manager, *request);
}

//  void QDeclarativeSearchModelBase::setPreviousPageRequest(const
//      QPlaceSearchRequest &previous)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase22setPreviousPageRequestERK19QPlaceSearchRequest(
    QDeclarativeSearchModelBase *self,
    const QPlaceSearchRequest *previous) {
  self->setPreviousPageRequest(*previous);
}

//  void QDeclarativeSearchModelBase::setNextPageRequest(const
//      QPlaceSearchRequest &next)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSearchModelBase18setNextPageRequestERK19QPlaceSearchRequest(
    QDeclarativeSearchModelBase *self,
    const QPlaceSearchRequest *next) {
  self->setNextPageRequest(*next);
}

//  QDeclarativeSearchModelBase as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QDeclarativeSearchModelBase_QQmlParserStatus(
    QDeclarativeSearchModelBase *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQDeclarativeSearchModelBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeSearchModelBase(
    QDeclarativeSearchModelBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeSearchModelBase *>(self)->take(key, call);
}

//  void QDeclarativeSearchModelBase::clearData(bool suppressSignal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeSearchModelBase9clearDataEb(
    QDeclarativeSearchModelBase *self,
    bool suppressSignal) {
  self->QDeclarativeSearchModelBase::clearData(suppressSignal);
}

//  void QDeclarativeSearchModelBase::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeSearchModelBase10classBeginEv(
    QDeclarativeSearchModelBase *self) {
  self->QDeclarativeSearchModelBase::classBegin();
}

//  void QDeclarativeSearchModelBase::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeSearchModelBase17componentCompleteEv(
    QDeclarativeSearchModelBase *self) {
  self->QDeclarativeSearchModelBase::componentComplete();
}

//  void QDeclarativeSearchModelBase::initializePlugin(QDeclarativeGeoService
//      Provider *plugin)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeSearchModelBase16initializePluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativeSearchModelBase *self,
    QDeclarativeGeoServiceProvider *plugin) {
  static_cast<OwnQDeclarativeSearchModelBase *>(self)->OwnQDeclarativeSearchModelBase::initializePlugin(
      plugin);
}

//  void QDeclarativeSearchModelBase::onContentUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeSearchModelBase16onContentUpdatedEv(
    QDeclarativeSearchModelBase *self) {
  static_cast<OwnQDeclarativeSearchModelBase *>(self)->OwnQDeclarativeSearchModelBase::onContentUpdated();
}
