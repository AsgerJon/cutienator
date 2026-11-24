//  Written by dev_tooling.RitualGenerator from the records of QtLocation/6.1
//  2.0/QtLocation/private/qdeclarativesearchsuggestionmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativesearchsuggestionmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtLocation/qplacesearchrequest.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QDeclarativeSearchSuggestionModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDeclarativeSearchSuggestionModel : QDeclarativeSearchSuggestionModel {
  using QDeclarativeSearchSuggestionModel::queryFinished;
  using QDeclarativeSearchSuggestionModel::sendQuery;
};

//  A QDeclarativeSearchSuggestionModel that Python can take functions over in. Every QDeclarativeSearchSuggestionModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeSearchSuggestionModelCall0)(const void *, bool, int *);
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchSuggestionModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQDeclarativeSearchSuggestionModelCall2)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall3)(const void *, int *);
typedef void * (*CuteQDeclarativeSearchSuggestionModelCall4)(const void *, QPlaceManager *, const QPlaceSearchRequest *, int *);
typedef void (*CuteQDeclarativeSearchSuggestionModelCall5)(const void *, int *);
typedef void (*CuteQDeclarativeSearchSuggestionModelCall6)(const void *, int *);
typedef void (*CuteQDeclarativeSearchSuggestionModelCall7)(const void *, QDeclarativeGeoServiceProvider *, int *);
typedef void (*CuteQDeclarativeSearchSuggestionModelCall8)(const void *, int *);
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchSuggestionModelCall9)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchSuggestionModelCall10)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall11)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchSuggestionModelCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchSuggestionModelCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchSuggestionModelCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall16)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QVariant * (*CuteQDeclarativeSearchSuggestionModelCall17)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall18)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall19)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchSuggestionModelCall21)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef int (*CuteQDeclarativeSearchSuggestionModelCall22)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall23)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall24)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall25)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall26)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall27)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall28)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall30)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall31)(const void *, int, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QModelIndex * (*CuteQDeclarativeSearchSuggestionModelCall32)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef const QSize * (*CuteQDeclarativeSearchSuggestionModelCall33)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall34)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall35)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall36)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall37)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeSearchSuggestionModelCall39)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall40)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall41)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall42)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSearchSuggestionModelCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeSearchSuggestionModel : public QDeclarativeSearchSuggestionModel {
public:
  using QDeclarativeSearchSuggestionModel::QDeclarativeSearchSuggestionModel;
  void *taken[45] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase9clearDataEb")) {
      taken[0] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase13queryFinishedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase9sendQueryEP13QPlaceManagerRK19QPlaceSearchRequest")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase16initializePluginEP30QDeclarativeGeoServiceProvider")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QDeclarativeSearchModelBase16onContentUpdatedEv")) {
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

  //  void QDeclarativeSearchSuggestionModel::clearData(bool
  //      suppressSignal)
  void clearData(bool suppressSignal) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeSearchSuggestionModelCall0 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall0>(taken[0]);
      call(this, suppressSignal, &handled);
      if (handled) return;
    }
    QDeclarativeSearchSuggestionModel::clearData(suppressSignal);
  }

#if QT_CONFIG(itemmodel)
  //  int QDeclarativeSearchSuggestionModel::rowCount(const QModelIndex
  //      &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeSearchSuggestionModelCall1 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall1>(taken[1]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QDeclarativeSearchSuggestionModel::rowCount(parent);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  QVariant QDeclarativeSearchSuggestionModel::data(const QModelIndex
  //      &index, int role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeSearchSuggestionModelCall2 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall2>(taken[2]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QDeclarativeSearchSuggestionModel::data(index, role);
  }
#endif  // QT_CONFIG(itemmodel)

  //  void QDeclarativeSearchSuggestionModel::queryFinished()
  void queryFinished() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeSearchSuggestionModelCall3 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchSuggestionModel::queryFinished();
  }

  //  QPlaceReply
  //      *QDeclarativeSearchSuggestionModel::sendQuery(QPlaceManager
  //      *manager, const QPlaceSearchRequest &request)
  QPlaceReply *sendQuery(
      QPlaceManager *manager,
      const QPlaceSearchRequest &request) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeSearchSuggestionModelCall4 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall4>(taken[4]);
      void * given = call(this, manager, &request, &handled);
      if (handled) return static_cast<QPlaceReply *>(given);
    }
    return QDeclarativeSearchSuggestionModel::sendQuery(manager, request);
  }

  //  void QDeclarativeSearchModelBase::classBegin()
  void classBegin() override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeSearchSuggestionModelCall5 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::classBegin();
  }

  //  void QDeclarativeSearchModelBase::componentComplete()
  void componentComplete() override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeSearchSuggestionModelCall6 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::componentComplete();
  }

  //  void QDeclarativeSearchModelBase::initializePlugin(QDeclarativeGeoSer
  //      viceProvider *plugin)
  void initializePlugin(QDeclarativeGeoServiceProvider *plugin) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeSearchSuggestionModelCall7 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall7>(taken[7]);
      call(this, plugin, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::initializePlugin(plugin);
  }

  //  void QDeclarativeSearchModelBase::onContentUpdated()
  void onContentUpdated() override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeSearchSuggestionModelCall8 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSearchModelBase::onContentUpdated();
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
      CuteQDeclarativeSearchSuggestionModelCall9 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall9>(taken[9]);
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
      CuteQDeclarativeSearchSuggestionModelCall10 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall10>(taken[10]);
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
      CuteQDeclarativeSearchSuggestionModelCall11 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall11>(taken[11]);
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
      CuteQDeclarativeSearchSuggestionModelCall12 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall12>(taken[12]);
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
      CuteQDeclarativeSearchSuggestionModelCall13 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall13>(taken[13]);
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
      CuteQDeclarativeSearchSuggestionModelCall14 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall14>(taken[14]);
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
      CuteQDeclarativeSearchSuggestionModelCall15 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall15>(taken[15]);
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
      CuteQDeclarativeSearchSuggestionModelCall16 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall16>(taken[16]);
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
      CuteQDeclarativeSearchSuggestionModelCall17 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall17>(taken[17]);
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
      CuteQDeclarativeSearchSuggestionModelCall18 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall18>(taken[18]);
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
      CuteQDeclarativeSearchSuggestionModelCall19 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall19>(taken[19]);
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
      CuteQDeclarativeSearchSuggestionModelCall20 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall20>(taken[20]);
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
      CuteQDeclarativeSearchSuggestionModelCall21 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall21>(taken[21]);
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
      CuteQDeclarativeSearchSuggestionModelCall22 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall22>(taken[22]);
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
      CuteQDeclarativeSearchSuggestionModelCall23 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall23>(taken[23]);
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
      CuteQDeclarativeSearchSuggestionModelCall24 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall24>(taken[24]);
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
      CuteQDeclarativeSearchSuggestionModelCall25 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall25>(taken[25]);
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
      CuteQDeclarativeSearchSuggestionModelCall26 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall26>(taken[26]);
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
      CuteQDeclarativeSearchSuggestionModelCall27 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall27>(taken[27]);
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
      CuteQDeclarativeSearchSuggestionModelCall28 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall28>(taken[28]);
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
      CuteQDeclarativeSearchSuggestionModelCall29 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall29>(taken[29]);
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
      CuteQDeclarativeSearchSuggestionModelCall30 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall30>(taken[30]);
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
      CuteQDeclarativeSearchSuggestionModelCall31 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall31>(taken[31]);
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
      CuteQDeclarativeSearchSuggestionModelCall32 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall32>(taken[32]);
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
      CuteQDeclarativeSearchSuggestionModelCall33 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall33>(taken[33]);
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
      CuteQDeclarativeSearchSuggestionModelCall34 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall34>(taken[34]);
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
      CuteQDeclarativeSearchSuggestionModelCall35 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall35>(taken[35]);
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
      CuteQDeclarativeSearchSuggestionModelCall36 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall36>(taken[36]);
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
      CuteQDeclarativeSearchSuggestionModelCall37 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall37>(taken[37]);
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
      CuteQDeclarativeSearchSuggestionModelCall38 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall38>(taken[38]);
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
      CuteQDeclarativeSearchSuggestionModelCall39 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall39>(taken[39]);
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
      CuteQDeclarativeSearchSuggestionModelCall40 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall40>(taken[40]);
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
      CuteQDeclarativeSearchSuggestionModelCall41 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall41>(taken[41]);
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
      CuteQDeclarativeSearchSuggestionModelCall42 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall42>(taken[42]);
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
      CuteQDeclarativeSearchSuggestionModelCall43 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall43>(taken[43]);
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
      CuteQDeclarativeSearchSuggestionModelCall44 call = reinterpret_cast<CuteQDeclarativeSearchSuggestionModelCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeSearchSuggestionModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK33QDeclarativeSearchSuggestionModel10metaObjectEv(
    const QDeclarativeSearchSuggestionModel *self) {
  return self->metaObject();
}

//  QString QDeclarativeSearchSuggestionModel::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN33QDeclarativeSearchSuggestionModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeSearchSuggestionModel::tr(s, c, n));
}

//  QDeclarativeSearchSuggestionModel::QDeclarativeSearchSuggestionModel(QObj
//      ect *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeSearchSuggestionModel *ritual_ZN33QDeclarativeSearchSuggestionModelC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativeSearchSuggestionModel(parent);
}

//  QDeclarativeSearchSuggestionModel::~QDeclarativeSearchSuggestionModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeSearchSuggestionModelD1Ev(
    QDeclarativeSearchSuggestionModel *self) {
  delete self;
}

//  QString QDeclarativeSearchSuggestionModel::searchTerm() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK33QDeclarativeSearchSuggestionModel10searchTermEv(
    const QDeclarativeSearchSuggestionModel *self) {
  return new QString(self->searchTerm());
}

//  void QDeclarativeSearchSuggestionModel::setSearchTerm(const QString
//      &searchTerm)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeSearchSuggestionModel13setSearchTermERK7QString(
    QDeclarativeSearchSuggestionModel *self,
    const QString *searchTerm) {
  self->setSearchTerm(*searchTerm);
}

//  QStringList QDeclarativeSearchSuggestionModel::suggestions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK33QDeclarativeSearchSuggestionModel11suggestionsEv(
    const QDeclarativeSearchSuggestionModel *self) {
  return new QList<QString>(self->suggestions());
}

//  void QDeclarativeSearchSuggestionModel::clearData(bool suppressSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeSearchSuggestionModel9clearDataEb(
    QDeclarativeSearchSuggestionModel *self,
    bool suppressSignal) {
  self->clearData(suppressSignal);
}

//  int QDeclarativeSearchSuggestionModel::rowCount(const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QDeclarativeSearchSuggestionModel8rowCountERK11QModelIndex(
    const QDeclarativeSearchSuggestionModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QDeclarativeSearchSuggestionModel::data(const QModelIndex
//      &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK33QDeclarativeSearchSuggestionModel4dataERK11QModelIndexi(
    const QDeclarativeSearchSuggestionModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QHash<int, QByteArray> QDeclarativeSearchSuggestionModel::roleNames()
//      const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK33QDeclarativeSearchSuggestionModel9roleNamesEv(
    const QDeclarativeSearchSuggestionModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  void QDeclarativeSearchSuggestionModel::queryFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QDeclarativeSearchSuggestionModel13queryFinishedEv(
    QDeclarativeSearchSuggestionModel *self) {
  self->queryFinished();
}

//  QPlaceReply *QDeclarativeSearchSuggestionModel::sendQuery(QPlaceManager
//      *manager, const QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceReply *ritual_ZN33QDeclarativeSearchSuggestionModel9sendQueryEP13QPlaceManagerRK19QPlaceSearchRequest(
    QDeclarativeSearchSuggestionModel *self,
    QPlaceManager *manager,
    const QPlaceSearchRequest *request) {
  return self->sendQuery(manager, *request);
}

//  a Python function taken by a CuteQDeclarativeSearchSuggestionModel, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeSearchSuggestionModel(
    QDeclarativeSearchSuggestionModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeSearchSuggestionModel *>(self)->take(key, call);
}

//  void QDeclarativeSearchSuggestionModel::clearData(bool suppressSignal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN33QDeclarativeSearchSuggestionModel9clearDataEb(
    QDeclarativeSearchSuggestionModel *self,
    bool suppressSignal) {
  self->QDeclarativeSearchSuggestionModel::clearData(suppressSignal);
}

//  int QDeclarativeSearchSuggestionModel::rowCount(const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK33QDeclarativeSearchSuggestionModel8rowCountERK11QModelIndex(
    const QDeclarativeSearchSuggestionModel *self,
    const QModelIndex *parent) {
  return self->QDeclarativeSearchSuggestionModel::rowCount(*parent);
}

//  QVariant QDeclarativeSearchSuggestionModel::data(const QModelIndex
//      &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK33QDeclarativeSearchSuggestionModel4dataERK11QModelIndexi(
    const QDeclarativeSearchSuggestionModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(
      self->QDeclarativeSearchSuggestionModel::data(
          *index,
          role));
}

//  void QDeclarativeSearchSuggestionModel::queryFinished()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN33QDeclarativeSearchSuggestionModel13queryFinishedEv(
    QDeclarativeSearchSuggestionModel *self) {
  static_cast<OwnQDeclarativeSearchSuggestionModel *>(self)->OwnQDeclarativeSearchSuggestionModel::queryFinished();
}

//  QPlaceReply *QDeclarativeSearchSuggestionModel::sendQuery(QPlaceManager
//      *manager, const QPlaceSearchRequest &request)
extern "C" Q_DECL_EXPORT
QPlaceReply *ritual_own_ZN33QDeclarativeSearchSuggestionModel9sendQueryEP13QPlaceManagerRK19QPlaceSearchRequest(
    QDeclarativeSearchSuggestionModel *self,
    QPlaceManager *manager,
    const QPlaceSearchRequest *request) {
  return static_cast<OwnQDeclarativeSearchSuggestionModel *>(self)->OwnQDeclarativeSearchSuggestionModel::sendQuery(
      manager,
      *request);
}
