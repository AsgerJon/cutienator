//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativesearchresultmodel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativesearchresultmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qbytearray.h>
#include <QtLocation/qplacesearchrequest.h>
#include <QtLocation/qplace.h>
#include <QtLocation/qplacesearchresult.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QDeclarativeSearchResultModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativeSearchResultModel : QDeclarativeSearchResultModel {
  using QDeclarativeSearchResultModel::sendQuery;
  using QDeclarativeSearchResultModel::initializePlugin;
  using QDeclarativeSearchResultModel::queryFinished;
  using QDeclarativeSearchResultModel::onContentUpdated;
};

//  A QDeclarativeSearchResultModel that Python can take functions over in. Every QDeclarativeSearchResultModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchResultModelCall0)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchResultModelCall1)(const void *, bool, int *);
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQDeclarativeSearchResultModelCall2)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
typedef void * (*CuteQDeclarativeSearchResultModelCall3)(const void *, QPlaceManager *, const QPlaceSearchRequest *, int *);
typedef void (*CuteQDeclarativeSearchResultModelCall4)(const void *, QDeclarativeGeoServiceProvider *, int *);
typedef void (*CuteQDeclarativeSearchResultModelCall5)(const void *, int *);
typedef void (*CuteQDeclarativeSearchResultModelCall6)(const void *, int *);
typedef void (*CuteQDeclarativeSearchResultModelCall7)(const void *, int *);
typedef void (*CuteQDeclarativeSearchResultModelCall8)(const void *, int *);
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchResultModelCall9)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchResultModelCall10)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall11)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchResultModelCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchResultModelCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchResultModelCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall16)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQDeclarativeSearchResultModelCall17)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall18)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall19)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchResultModelCall21)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchResultModelCall22)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall23)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall24)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall25)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall26)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall27)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall28)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchResultModelCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall30)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchResultModelCall31)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchResultModelCall32)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQDeclarativeSearchResultModelCall33)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchResultModelCall34)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchResultModelCall35)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchResultModelCall36)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchResultModelCall37)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeSearchResultModelCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeSearchResultModelCall39)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchResultModelCall40)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchResultModelCall41)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchResultModelCall42)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchResultModelCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchResultModelCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeSearchResultModel : public QDeclarativeSearchResultModel {
public:
  using QDeclarativeSearchResultModel::QDeclarativeSearchResultModel;
  void *taken[45] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase9clearDataEb")) {
      taken[1] = call;
      return true;
    }
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase9sendQueryEP13QPlaceManagerRK19QPlaceSearchRequest")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase16initializePluginEP30QDeclarativeGeoServiceProvider")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase13queryFinishedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase16onContentUpdatedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
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

#if QT_CONFIG(itemmodel)
  //  int QDeclarativeSearchResultModel::rowCount(const QModelIndex
  //      &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall0 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall0>(taken[0]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QDeclarativeSearchResultModel::rowCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

  //  void QDeclarativeSearchResultModel::clearData(bool suppressSignal)
  void clearData(bool suppressSignal) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall1 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall1>(taken[1]);
      call(this, suppressSignal, &handled);
      if (handled) return;
    }
    QDeclarativeSearchResultModel::clearData(suppressSignal);
  }

#if QT_CONFIG(itemmodel)
  //  QVariant QDeclarativeSearchResultModel::data(const QModelIndex
  //      &index, int role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall2 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall2>(taken[2]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QDeclarativeSearchResultModel::data(index, role);
  }
#endif  // QT_CONFIG(itemmodel)

  //  QPlaceReply *QDeclarativeSearchResultModel::sendQuery(QPlaceManager
  //      *manager, const QPlaceSearchRequest &request)
  QPlaceReply *sendQuery(
      QPlaceManager *manager,
      const QPlaceSearchRequest &request) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall3 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall3>(taken[3]);
      void * given = call(this, manager, &request, &handled);
      if (handled) return static_cast<QPlaceReply *>(given);
    }
    return QDeclarativeSearchResultModel::sendQuery(manager, request);
  }

  //  void QDeclarativeSearchResultModel::initializePlugin(QDeclarativeGeoS
  //      erviceProvider *plugin)
  void initializePlugin(QDeclarativeGeoServiceProvider *plugin) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall4 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall4>(taken[4]);
      call(this, plugin, &handled);
      if (handled) return;
    }
    QDeclarativeSearchResultModel::initializePlugin(plugin);
  }

  //  void QDeclarativeSearchResultModel::queryFinished()
  void queryFinished() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall5 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchResultModel::queryFinished();
  }

  //  void QDeclarativeSearchResultModel::onContentUpdated()
  void onContentUpdated() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall6 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchResultModel::onContentUpdated();
  }

  //  void QDeclarativeSearchModelBase::classBegin()
  void classBegin() override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall7 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::classBegin();
  }

  //  void QDeclarativeSearchModelBase::componentComplete()
  void componentComplete() override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall8 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::componentComplete();
  }

#if QT_CONFIG(itemmodel)
  //  QModelIndex QAbstractListModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall9 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall10 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall11 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall12 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall13 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall13>(taken[13]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QAbstractListModel::parent(child);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  int QAbstractListModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall14 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall14>(taken[14]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractListModel::columnCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  bool QAbstractListModel::hasChildren(const QModelIndex &parent) const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall15 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQDeclarativeSearchResultModelCall16 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall16>(taken[16]);
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
      CuteQDeclarativeSearchResultModelCall17 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall17>(taken[17]);
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
      CuteQDeclarativeSearchResultModelCall18 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall18>(taken[18]);
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
      CuteQDeclarativeSearchResultModelCall19 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall19>(taken[19]);
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
      CuteQDeclarativeSearchResultModelCall20 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall20>(taken[20]);
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
      CuteQDeclarativeSearchResultModelCall21 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall21>(taken[21]);
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
      CuteQDeclarativeSearchResultModelCall22 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall22>(taken[22]);
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
      CuteQDeclarativeSearchResultModelCall23 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall23>(taken[23]);
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
      CuteQDeclarativeSearchResultModelCall24 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall24>(taken[24]);
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
      CuteQDeclarativeSearchResultModelCall25 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall25>(taken[25]);
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
      CuteQDeclarativeSearchResultModelCall26 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall26>(taken[26]);
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
      CuteQDeclarativeSearchResultModelCall27 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall27>(taken[27]);
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
      CuteQDeclarativeSearchResultModelCall28 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall28>(taken[28]);
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
      CuteQDeclarativeSearchResultModelCall29 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall29>(taken[29]);
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
      CuteQDeclarativeSearchResultModelCall30 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall30>(taken[30]);
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
      CuteQDeclarativeSearchResultModelCall31 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall31>(taken[31]);
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
      CuteQDeclarativeSearchResultModelCall32 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall32>(taken[32]);
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
      CuteQDeclarativeSearchResultModelCall33 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall33>(taken[33]);
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
      CuteQDeclarativeSearchResultModelCall34 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall34>(taken[34]);
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
      CuteQDeclarativeSearchResultModelCall35 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall35>(taken[35]);
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
      CuteQDeclarativeSearchResultModelCall36 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall36>(taken[36]);
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
      CuteQDeclarativeSearchResultModelCall37 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall37>(taken[37]);
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
      CuteQDeclarativeSearchResultModelCall38 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall38>(taken[38]);
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
      CuteQDeclarativeSearchResultModelCall39 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall39>(taken[39]);
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
      CuteQDeclarativeSearchResultModelCall40 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall40>(taken[40]);
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
      CuteQDeclarativeSearchResultModelCall41 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall41>(taken[41]);
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
      CuteQDeclarativeSearchResultModelCall42 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall42>(taken[42]);
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
      CuteQDeclarativeSearchResultModelCall43 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall43>(taken[43]);
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
      CuteQDeclarativeSearchResultModelCall44 call = reinterpret_cast<CuteQDeclarativeSearchResultModelCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeSearchResultModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QDeclarativeSearchResultModel10metaObjectEv(
    const QDeclarativeSearchResultModel *self) {
  return self->metaObject();
}

//  QString QDeclarativeSearchResultModel::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QDeclarativeSearchResultModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeSearchResultModel::tr(s, c, n));
}

//  QDeclarativeSearchResultModel::QDeclarativeSearchResultModel(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeSearchResultModel *ritual_ZN29QDeclarativeSearchResultModelC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativeSearchResultModel(parent);
}

//  QDeclarativeSearchResultModel::~QDeclarativeSearchResultModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModelD1Ev(
    QDeclarativeSearchResultModel *self) {
  delete self;
}

//  QString QDeclarativeSearchResultModel::searchTerm() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QDeclarativeSearchResultModel10searchTermEv(
    const QDeclarativeSearchResultModel *self) {
  return new QString(self->searchTerm());
}

//  void QDeclarativeSearchResultModel::setSearchTerm(const QString
//      &searchTerm)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel13setSearchTermERK7QString(
    QDeclarativeSearchResultModel *self,
    const QString *searchTerm) {
  self->setSearchTerm(*searchTerm);
}

//  QString QDeclarativeSearchResultModel::recommendationId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QDeclarativeSearchResultModel16recommendationIdEv(
    const QDeclarativeSearchResultModel *self) {
  return new QString(self->recommendationId());
}

//  void QDeclarativeSearchResultModel::setRecommendationId(const QString
//      &recommendationId)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel19setRecommendationIdERK7QString(
    QDeclarativeSearchResultModel *self,
    const QString *recommendationId) {
  self->setRecommendationId(*recommendationId);
}

//  QDeclarativeSearchResultModel::RelevanceHint
//      QDeclarativeSearchResultModel::relevanceHint() const
extern "C" Q_DECL_EXPORT
QDeclarativeSearchResultModel::RelevanceHint ritual_ZNK29QDeclarativeSearchResultModel13relevanceHintEv(
    const QDeclarativeSearchResultModel *self) {
  return self->relevanceHint();
}

//  void QDeclarativeSearchResultModel::setRelevanceHint(QDeclarativeSearchRe
//      sultModel::RelevanceHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel16setRelevanceHintENS_13RelevanceHintE(
    QDeclarativeSearchResultModel *self,
    QDeclarativeSearchResultModel::RelevanceHint hint) {
  self->setRelevanceHint(hint);
}

//  QDeclarativePlace::Visibility
//      QDeclarativeSearchResultModel::visibilityScope() const
extern "C" Q_DECL_EXPORT
QDeclarativePlace::Visibility ritual_ZNK29QDeclarativeSearchResultModel15visibilityScopeEv(
    const QDeclarativeSearchResultModel *self) {
  return self->visibilityScope();
}

//  void QDeclarativeSearchResultModel::setVisibilityScope(QDeclarativePlace:
//      :Visibility visibilityScope)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel18setVisibilityScopeEN17QDeclarativePlace10VisibilityE(
    QDeclarativeSearchResultModel *self,
    QDeclarativePlace::Visibility visibilityScope) {
  self->setVisibilityScope(visibilityScope);
}

//  QDeclarativeGeoServiceProvider
//      *QDeclarativeSearchResultModel::favoritesPlugin() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoServiceProvider *ritual_ZNK29QDeclarativeSearchResultModel15favoritesPluginEv(
    const QDeclarativeSearchResultModel *self) {
  return self->favoritesPlugin();
}

//  void QDeclarativeSearchResultModel::setFavoritesPlugin(QDeclarativeGeoSer
//      viceProvider *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel18setFavoritesPluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativeSearchResultModel *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->setFavoritesPlugin(plugin);
}

//  QVariantMap QDeclarativeSearchResultModel::favoritesMatchParameters()
//      const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK29QDeclarativeSearchResultModel24favoritesMatchParametersEv(
    const QDeclarativeSearchResultModel *self) {
  return new QMap<QString, QVariant>(self->favoritesMatchParameters());
}

//  void QDeclarativeSearchResultModel::setFavoritesMatchParameters(const
//      QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel27setFavoritesMatchParametersERK4QMapI7QString8QVariantE(
    QDeclarativeSearchResultModel *self,
    const QMap<QString, QVariant> *parameters) {
  self->setFavoritesMatchParameters(*parameters);
}

//  int QDeclarativeSearchResultModel::rowCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QDeclarativeSearchResultModel8rowCountERK11QModelIndex(
    const QDeclarativeSearchResultModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  void QDeclarativeSearchResultModel::clearData(bool suppressSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel9clearDataEb(
    QDeclarativeSearchResultModel *self,
    bool suppressSignal) {
  self->clearData(suppressSignal);
}

//  QVariant QDeclarativeSearchResultModel::data(const QModelIndex &index,
//      int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK29QDeclarativeSearchResultModel4dataERK11QModelIndexi(
    const QDeclarativeSearchResultModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QVariant QDeclarativeSearchResultModel::data(int index, const QString
//      &roleName) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK29QDeclarativeSearchResultModel4dataEiRK7QString(
    const QDeclarativeSearchResultModel *self,
    int index,
    const QString *roleName) {
  return new QVariant(self->data(index, *roleName));
}

//  QHash<int, QByteArray> QDeclarativeSearchResultModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK29QDeclarativeSearchResultModel9roleNamesEv(
    const QDeclarativeSearchResultModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  void QDeclarativeSearchResultModel::updateWith(int proposedSearchIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel10updateWithEi(
    QDeclarativeSearchResultModel *self,
    int proposedSearchIndex) {
  self->updateWith(proposedSearchIndex);
}

//  QPlaceReply *QDeclarativeSearchResultModel::sendQuery(QPlaceManager
//      *manager, const QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceReply *ritual_ZN29QDeclarativeSearchResultModel9sendQueryEP13QPlaceManagerRK19QPlaceSearchRequest(
    QDeclarativeSearchResultModel *self,
    QPlaceManager *manager,
    const QPlaceSearchRequest *request) {
  return self->sendQuery(manager, *request);
}

//  void QDeclarativeSearchResultModel::initializePlugin(QDeclarativeGeoServi
//      ceProvider *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel16initializePluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativeSearchResultModel *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->initializePlugin(plugin);
}

//  void QDeclarativeSearchResultModel::queryFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel13queryFinishedEv(
    QDeclarativeSearchResultModel *self) {
  self->queryFinished();
}

//  void QDeclarativeSearchResultModel::onContentUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel16onContentUpdatedEv(
    QDeclarativeSearchResultModel *self) {
  self->onContentUpdated();
}

//  void QDeclarativeSearchResultModel::updateLayout(const QList<QPlace>
//      &favoritePlaces)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel12updateLayoutERK5QListI6QPlaceE(
    QDeclarativeSearchResultModel *self,
    const QList<QPlace> *favoritePlaces) {
  self->updateLayout(*favoritePlaces);
}

//  void QDeclarativeSearchResultModel::placeUpdated(const QString &placeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel12placeUpdatedERK7QString(
    QDeclarativeSearchResultModel *self,
    const QString *placeId) {
  self->placeUpdated(*placeId);
}

//  void QDeclarativeSearchResultModel::placeRemoved(const QString &placeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel12placeRemovedERK7QString(
    QDeclarativeSearchResultModel *self,
    const QString *placeId) {
  self->placeRemoved(*placeId);
}

//  int QDeclarativeSearchResultModel::getRow(const QString &placeId) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QDeclarativeSearchResultModel6getRowERK7QString(
    const QDeclarativeSearchResultModel *self,
    const QString *placeId) {
  return self->getRow(*placeId);
}

//  QList<QPlaceSearchResult>
//      QDeclarativeSearchResultModel::resultsFromPages() const
extern "C" Q_DECL_EXPORT
QList<QPlaceSearchResult> *ritual_ZNK29QDeclarativeSearchResultModel16resultsFromPagesEv(
    const QDeclarativeSearchResultModel *self) {
  return new QList<QPlaceSearchResult>(self->resultsFromPages());
}

//  void QDeclarativeSearchResultModel::removePageRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeSearchResultModel13removePageRowEi(
    QDeclarativeSearchResultModel *self,
    int row) {
  self->removePageRow(row);
}

//  a Python function taken by a CuteQDeclarativeSearchResultModel, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeSearchResultModel(
    QDeclarativeSearchResultModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeSearchResultModel *>(self)->take(key, call);
}

//  int QDeclarativeSearchResultModel::rowCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QDeclarativeSearchResultModel8rowCountERK11QModelIndex(
    const QDeclarativeSearchResultModel *self,
    const QModelIndex *parent) {
  return self->QDeclarativeSearchResultModel::rowCount(*parent);
}

//  void QDeclarativeSearchResultModel::clearData(bool suppressSignal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QDeclarativeSearchResultModel9clearDataEb(
    QDeclarativeSearchResultModel *self,
    bool suppressSignal) {
  self->QDeclarativeSearchResultModel::clearData(suppressSignal);
}

//  QVariant QDeclarativeSearchResultModel::data(const QModelIndex &index,
//      int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK29QDeclarativeSearchResultModel4dataERK11QModelIndexi(
    const QDeclarativeSearchResultModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(
      self->QDeclarativeSearchResultModel::data(
          *index,
          role));
}

//  QPlaceReply *QDeclarativeSearchResultModel::sendQuery(QPlaceManager
//      *manager, const QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceReply *ritual_own_ZN29QDeclarativeSearchResultModel9sendQueryEP13QPlaceManagerRK19QPlaceSearchRequest(
    QDeclarativeSearchResultModel *self,
    QPlaceManager *manager,
    const QPlaceSearchRequest *request) {
  return static_cast<OwnQDeclarativeSearchResultModel *>(self)->OwnQDeclarativeSearchResultModel::sendQuery(
      manager,
      *request);
}

//  void QDeclarativeSearchResultModel::initializePlugin(QDeclarativeGeoServi
//      ceProvider *plugin)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QDeclarativeSearchResultModel16initializePluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativeSearchResultModel *self,
    QDeclarativeGeoServiceProvider *plugin) {
  static_cast<OwnQDeclarativeSearchResultModel *>(self)->OwnQDeclarativeSearchResultModel::initializePlugin(
      plugin);
}

//  void QDeclarativeSearchResultModel::queryFinished()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QDeclarativeSearchResultModel13queryFinishedEv(
    QDeclarativeSearchResultModel *self) {
  static_cast<OwnQDeclarativeSearchResultModel *>(self)->OwnQDeclarativeSearchResultModel::queryFinished();
}

//  void QDeclarativeSearchResultModel::onContentUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QDeclarativeSearchResultModel16onContentUpdatedEv(
    QDeclarativeSearchResultModel *self) {
  static_cast<OwnQDeclarativeSearchResultModel *>(self)->OwnQDeclarativeSearchResultModel::onContentUpdated();
}
