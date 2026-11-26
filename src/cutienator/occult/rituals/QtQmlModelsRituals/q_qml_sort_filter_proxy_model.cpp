//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortfilterproxymodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlsortfilterproxymodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qvariant.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qitemselectionmodel.h>
#endif
#include <QtCore/qbytearray.h>
#include <QtCore/qcompare.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/Qt>

//  Only a class built on QQmlSortFilterProxyModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlSortFilterProxyModel : QQmlSortFilterProxyModel {
  using QQmlSortFilterProxyModel::sort;
};

//  A QQmlSortFilterProxyModel that Python can take functions over in. Every QQmlSortFilterProxyModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
typedef const QModelIndex * (*CuteQQmlSortFilterProxyModelCall0)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
typedef const QModelIndex * (*CuteQQmlSortFilterProxyModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef const QModelIndex * (*CuteQQmlSortFilterProxyModelCall2)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef const QModelIndex * (*CuteQQmlSortFilterProxyModelCall3)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef const QModelIndex * (*CuteQQmlSortFilterProxyModelCall4)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef bool (*CuteQQmlSortFilterProxyModelCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef int (*CuteQQmlSortFilterProxyModelCall6)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef int (*CuteQQmlSortFilterProxyModelCall7)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef const QVariant * (*CuteQQmlSortFilterProxyModelCall8)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef bool (*CuteQQmlSortFilterProxyModelCall9)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef const QVariant * (*CuteQQmlSortFilterProxyModelCall10)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef bool (*CuteQQmlSortFilterProxyModelCall11)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef bool (*CuteQQmlSortFilterProxyModelCall12)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef bool (*CuteQQmlSortFilterProxyModelCall13)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef bool (*CuteQQmlSortFilterProxyModelCall14)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef bool (*CuteQQmlSortFilterProxyModelCall15)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
typedef const QItemSelection * (*CuteQQmlSortFilterProxyModelCall16)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
typedef const QItemSelection * (*CuteQQmlSortFilterProxyModelCall17)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
typedef void (*CuteQQmlSortFilterProxyModelCall18)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef void (*CuteQQmlSortFilterProxyModelCall19)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
typedef void (*CuteQQmlSortFilterProxyModelCall20)(const void *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#if QT_CONFIG(qml_sfpm_model)
typedef void (*CuteQQmlSortFilterProxyModelCall21)(const void *, int *);
#endif  // QT_CONFIG(qml_sfpm_model)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQQmlSortFilterProxyModelCall22)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef void (*CuteQQmlSortFilterProxyModelCall23)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef int (*CuteQQmlSortFilterProxyModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQQmlSortFilterProxyModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef const QModelIndex * (*CuteQQmlSortFilterProxyModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQQmlSortFilterProxyModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef void (*CuteQQmlSortFilterProxyModelCall28)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef const QSize * (*CuteQQmlSortFilterProxyModelCall29)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQQmlSortFilterProxyModelCall30)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQQmlSortFilterProxyModelCall31)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef int (*CuteQQmlSortFilterProxyModelCall32)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef int (*CuteQQmlSortFilterProxyModelCall33)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlSortFilterProxyModelCall34)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQQmlSortFilterProxyModelCall35)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlSortFilterProxyModelCall36)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQQmlSortFilterProxyModelCall37)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSortFilterProxyModelCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlSortFilterProxyModelCall39)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSortFilterProxyModelCall40)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSortFilterProxyModelCall41)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSortFilterProxyModelCall42)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSortFilterProxyModelCall43)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlSortFilterProxyModelCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlSortFilterProxyModel : public QQmlSortFilterProxyModel {
public:
  using QQmlSortFilterProxyModel::QQmlSortFilterProxyModel;
  void *taken[45] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel11mapToSourceERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel13mapFromSourceERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel20mapSelectionToSourceERK14QItemSelection")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel22mapSelectionFromSourceERK14QItemSelection")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZN19QAbstractProxyModel14setSourceModelEP18QAbstractItemModel")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#if QT_CONFIG(qml_sfpm_model)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_sfpm_model)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
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

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
  //  QModelIndex QQmlSortFilterProxyModel::mapToSource(const QModelIndex
  //      &proxyIndex) const
  QModelIndex mapToSource(const QModelIndex &proxyIndex) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall0 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall0>(taken[0]);
      const QModelIndex * given = call(this, &proxyIndex, &handled);
      if (handled && given) return *given;
    }
    return QQmlSortFilterProxyModel::mapToSource(proxyIndex);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
  //  QModelIndex QQmlSortFilterProxyModel::mapFromSource(const QModelIndex
  //      &sourceIndex) const
  QModelIndex mapFromSource(const QModelIndex &sourceIndex) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall1 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall1>(taken[1]);
      const QModelIndex * given = call(this, &sourceIndex, &handled);
      if (handled && given) return *given;
    }
    return QQmlSortFilterProxyModel::mapFromSource(sourceIndex);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  QModelIndex QQmlSortFilterProxyModel::index(int row, int column,
  //      const QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall2 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall2>(taken[2]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QQmlSortFilterProxyModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  QModelIndex QQmlSortFilterProxyModel::parent(const QModelIndex
  //      &child) const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall3 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall3>(taken[3]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QQmlSortFilterProxyModel::parent(child);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  QModelIndex QQmlSortFilterProxyModel::sibling(int row, int column,
  //      const QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall4 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall4>(taken[4]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QQmlSortFilterProxyModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  bool QQmlSortFilterProxyModel::hasChildren(const QModelIndex &parent)
  //      const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall5 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall5>(taken[5]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  int QQmlSortFilterProxyModel::columnCount(const QModelIndex &parent)
  //      const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall6 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall6>(taken[6]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModel::columnCount(parent);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  int QQmlSortFilterProxyModel::rowCount(const QModelIndex &parent)
  //      const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall7 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall7>(taken[7]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModel::rowCount(parent);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  QVariant QQmlSortFilterProxyModel::data(const QModelIndex &index, int
  //      role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall8 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall8>(taken[8]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QQmlSortFilterProxyModel::data(index, role);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  bool QQmlSortFilterProxyModel::setData(const QModelIndex &index,
  //      const QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall9 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall9>(taken[9]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  QVariant QQmlSortFilterProxyModel::headerData(int section,
  //      Qt::Orientation orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall10 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall10>(taken[10]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QQmlSortFilterProxyModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  bool QQmlSortFilterProxyModel::setHeaderData(int section,
  //      Qt::Orientation orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall11 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall11>(taken[11]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  bool QQmlSortFilterProxyModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall12 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall12>(taken[12]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  bool QQmlSortFilterProxyModel::insertColumns(int column, int count,
  //      const QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall13 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall13>(taken[13]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModel::insertColumns(column, count, parent);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  bool QQmlSortFilterProxyModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall14 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall14>(taken[14]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModel::removeRows(row, count, parent);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  bool QQmlSortFilterProxyModel::removeColumns(int column, int count,
  //      const QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall15 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall15>(taken[15]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QQmlSortFilterProxyModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
  //  QItemSelection QQmlSortFilterProxyModel::mapSelectionToSource(const
  //      QItemSelection &proxySelection) const
  QItemSelection mapSelectionToSource(
      const QItemSelection &proxySelection) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall16 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall16>(taken[16]);
      const QItemSelection * given = call(this, &proxySelection, &handled);
      if (handled && given) return *given;
    }
    return QQmlSortFilterProxyModel::mapSelectionToSource(proxySelection);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
  //  QItemSelection QQmlSortFilterProxyModel::mapSelectionFromSource(const
  //      QItemSelection &sourceSelection) const
  QItemSelection mapSelectionFromSource(
      const QItemSelection &sourceSelection) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall17 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall17>(taken[17]);
      const QItemSelection * given = call(this, &sourceSelection, &handled);
      if (handled && given) return *given;
    }
    return QQmlSortFilterProxyModel::mapSelectionFromSource(sourceSelection);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(qml_sfpm_model)
  //  void QQmlSortFilterProxyModel::setSourceModel(QAbstractItemModel
  //      *sourceModel)
  void setSourceModel(QAbstractItemModel *sourceModel) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall18 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall18>(taken[18]);
      call(this, sourceModel, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModel::setSourceModel(sourceModel);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(qml_sfpm_model)
  //  void QQmlSortFilterProxyModel::sort(int column, Qt::SortOrder
  //      sortOrder)
  void sort(int column, Qt::SortOrder sortOrder) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall19 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall19>(taken[19]);
      call(this, column, static_cast<int>(sortOrder), &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModel::sort(column, sortOrder);
  }
#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(qml_sfpm_model)
  //  void QQmlSortFilterProxyModel::classBegin()
  void classBegin() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall20 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModel::classBegin();
  }
#endif  // QT_CONFIG(qml_sfpm_model)

#if QT_CONFIG(qml_sfpm_model)
  //  void QQmlSortFilterProxyModel::componentComplete()
  void componentComplete() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall21 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlSortFilterProxyModel::componentComplete();
  }
#endif  // QT_CONFIG(qml_sfpm_model)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::submit()
  bool submit() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall22 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::submit();
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  void QAbstractProxyModel::revert()
  void revert() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall23 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::revert();
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  Qt::ItemFlags QAbstractProxyModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall24 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall24>(taken[24]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QAbstractProxyModel::flags(index);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall25 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall25>(taken[25]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::clearItemData(index);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  QModelIndex QAbstractProxyModel::buddy(const QModelIndex &index)
  //      const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall26 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall26>(taken[26]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::buddy(index);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall27 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall27>(taken[27]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  void QAbstractProxyModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall28 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall28>(taken[28]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::fetchMore(parent);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  QSize QAbstractProxyModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall29 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall29>(taken[29]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::span(index);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::canDropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent) const
  bool canDropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall30 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall30>(taken[30]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall31 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall31>(taken[31]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  Qt::DropActions QAbstractProxyModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall32 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall32>(taken[32]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractProxyModel::supportedDragActions();
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  Qt::DropActions QAbstractProxyModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall33 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall33>(taken[33]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractProxyModel::supportedDropActions();
  }
#endif  // QT_CONFIG(proxymodel)
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
    if (taken[34]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall34 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall34>(taken[34]);
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
    if (taken[35]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall35 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall35>(taken[35]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall36 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall36>(taken[36]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlSortFilterProxyModelCall37 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall37>(taken[37]);
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
      CuteQQmlSortFilterProxyModelCall38 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall38>(taken[38]);
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
      CuteQQmlSortFilterProxyModelCall39 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall39>(taken[39]);
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
      CuteQQmlSortFilterProxyModelCall40 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall40>(taken[40]);
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
      CuteQQmlSortFilterProxyModelCall41 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall41>(taken[41]);
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
      CuteQQmlSortFilterProxyModelCall42 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall42>(taken[42]);
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
      CuteQQmlSortFilterProxyModelCall43 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall43>(taken[43]);
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
      CuteQQmlSortFilterProxyModelCall44 call = reinterpret_cast<CuteQQmlSortFilterProxyModelCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlSortFilterProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQmlSortFilterProxyModel10metaObjectEv(
    const QQmlSortFilterProxyModel *self) {
  return self->metaObject();
}

//  void *QQmlSortFilterProxyModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQmlSortFilterProxyModel11qt_metacastEPKc(
    QQmlSortFilterProxyModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlSortFilterProxyModel::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQmlSortFilterProxyModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlSortFilterProxyModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlSortFilterProxyModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQmlSortFilterProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlSortFilterProxyModel::tr(s, c, n));
}

//  QQmlSortFilterProxyModel::QQmlSortFilterProxyModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlSortFilterProxyModel *ritual_ZN24QQmlSortFilterProxyModelC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlSortFilterProxyModel(parent);
}

//  QQmlSortFilterProxyModel::~QQmlSortFilterProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModelD1Ev(
    QQmlSortFilterProxyModel *self) {
  delete self;
}

//  QQmlListProperty<QQmlFilterBase> QQmlSortFilterProxyModel::filters()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQmlFilterBase> *ritual_ZN24QQmlSortFilterProxyModel7filtersEv(
    QQmlSortFilterProxyModel *self) {
  return new QQmlListProperty<QQmlFilterBase>(self->filters());
}

//  QQmlListProperty<QQmlSorterBase> QQmlSortFilterProxyModel::sorters()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQmlSorterBase> *ritual_ZN24QQmlSortFilterProxyModel7sortersEv(
    QQmlSortFilterProxyModel *self) {
  return new QQmlListProperty<QQmlSorterBase>(self->sorters());
}

#if QT_DEPRECATED_SINCE(6, 12)
//  QAbstractItemModel *QQmlSortFilterProxyModel::model()
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZN24QQmlSortFilterProxyModel5modelEv(
    QQmlSortFilterProxyModel *self) {
  return self->model();
}
#endif  // QT_DEPRECATED_SINCE(6, 12)

#if QT_DEPRECATED_SINCE(6, 12)
//  void QQmlSortFilterProxyModel::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel8setModelEP18QAbstractItemModel(
    QQmlSortFilterProxyModel *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}
#endif  // QT_DEPRECATED_SINCE(6, 12)

//  bool QQmlSortFilterProxyModel::dynamicSortFilter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlSortFilterProxyModel17dynamicSortFilterEv(
    const QQmlSortFilterProxyModel *self) {
  return self->dynamicSortFilter();
}

//  void QQmlSortFilterProxyModel::setDynamicSortFilter(const bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel20setDynamicSortFilterEb(
    QQmlSortFilterProxyModel *self,
    bool enabled) {
  self->setDynamicSortFilter(enabled);
}

//  bool QQmlSortFilterProxyModel::recursiveFiltering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlSortFilterProxyModel18recursiveFilteringEv(
    const QQmlSortFilterProxyModel *self) {
  return self->recursiveFiltering();
}

//  void QQmlSortFilterProxyModel::setRecursiveFiltering(const bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel21setRecursiveFilteringEb(
    QQmlSortFilterProxyModel *self,
    bool enabled) {
  self->setRecursiveFiltering(enabled);
}

//  bool QQmlSortFilterProxyModel::autoAcceptChildRows() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlSortFilterProxyModel19autoAcceptChildRowsEv(
    const QQmlSortFilterProxyModel *self) {
  return self->autoAcceptChildRows();
}

//  void QQmlSortFilterProxyModel::setAutoAcceptChildRows(const bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel22setAutoAcceptChildRowsEb(
    QQmlSortFilterProxyModel *self,
    bool enabled) {
  self->setAutoAcceptChildRows(enabled);
}

//  void QQmlSortFilterProxyModel::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel10invalidateEv(
    QQmlSortFilterProxyModel *self) {
  self->invalidate();
}

//  void QQmlSortFilterProxyModel::invalidateSorter()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel16invalidateSorterEv(
    QQmlSortFilterProxyModel *self) {
  self->invalidateSorter();
}

//  void QQmlSortFilterProxyModel::setPrimarySorter(QQmlSorterBase *sorter)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel16setPrimarySorterEP14QQmlSorterBase(
    QQmlSortFilterProxyModel *self,
    QQmlSorterBase *sorter) {
  self->setPrimarySorter(sorter);
}

//  QModelIndex QQmlSortFilterProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK24QQmlSortFilterProxyModel11mapToSourceERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QModelIndex QQmlSortFilterProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK24QQmlSortFilterProxyModel13mapFromSourceERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QModelIndex QQmlSortFilterProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK24QQmlSortFilterProxyModel5indexEiiRK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QQmlSortFilterProxyModel::parent(const QModelIndex &child)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK24QQmlSortFilterProxyModel6parentERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  QModelIndex QQmlSortFilterProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK24QQmlSortFilterProxyModel7siblingEiiRK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  bool QQmlSortFilterProxyModel::hasChildren(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlSortFilterProxyModel11hasChildrenERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  int QQmlSortFilterProxyModel::columnCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQmlSortFilterProxyModel11columnCountERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  int QQmlSortFilterProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQmlSortFilterProxyModel8rowCountERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QQmlSortFilterProxyModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QQmlSortFilterProxyModel4dataERK11QModelIndexi(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QQmlSortFilterProxyModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQmlSortFilterProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QQmlSortFilterProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QVariant QQmlSortFilterProxyModel::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QQmlSortFilterProxyModel10headerDataEiN2Qt11OrientationEi(
    const QQmlSortFilterProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QQmlSortFilterProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQmlSortFilterProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QQmlSortFilterProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  bool QQmlSortFilterProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQmlSortFilterProxyModel10insertRowsEiiRK11QModelIndex(
    QQmlSortFilterProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QQmlSortFilterProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQmlSortFilterProxyModel13insertColumnsEiiRK11QModelIndex(
    QQmlSortFilterProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QQmlSortFilterProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQmlSortFilterProxyModel10removeRowsEiiRK11QModelIndex(
    QQmlSortFilterProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QQmlSortFilterProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQmlSortFilterProxyModel13removeColumnsEiiRK11QModelIndex(
    QQmlSortFilterProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  QItemSelection QQmlSortFilterProxyModel::mapSelectionToSource(const
//      QItemSelection &proxySelection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK24QQmlSortFilterProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QQmlSortFilterProxyModel *self,
    const QItemSelection *proxySelection) {
  return new QItemSelection(self->mapSelectionToSource(*proxySelection));
}

//  QItemSelection QQmlSortFilterProxyModel::mapSelectionFromSource(const
//      QItemSelection &sourceSelection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK24QQmlSortFilterProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QQmlSortFilterProxyModel *self,
    const QItemSelection *sourceSelection) {
  return new QItemSelection(self->mapSelectionFromSource(*sourceSelection));
}

//  void QQmlSortFilterProxyModel::setSourceModel(QAbstractItemModel
//      *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel14setSourceModelEP18QAbstractItemModel(
    QQmlSortFilterProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->setSourceModel(sourceModel);
}

//  void QQmlSortFilterProxyModel::setPrimarySortColumn(const int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel20setPrimarySortColumnEi(
    QQmlSortFilterProxyModel *self,
    int column) {
  self->setPrimarySortColumn(column);
}

//  void QQmlSortFilterProxyModel::setPrimarySortOrder(const Qt::SortOrder
//      sortOrder)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel19setPrimarySortOrderEN2Qt9SortOrderE(
    QQmlSortFilterProxyModel *self,
    const Qt::SortOrder *sortOrder) {
  self->setPrimarySortOrder(*sortOrder);
}

//  QVariant QQmlSortFilterProxyModel::sourceData(const QModelIndex
//      &sourceIndex, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QQmlSortFilterProxyModel10sourceDataERK11QModelIndexi(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *sourceIndex,
    int role) {
  return new QVariant(self->sourceData(*sourceIndex, role));
}

//  QHash<int, QByteArray> QQmlSortFilterProxyModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK24QQmlSortFilterProxyModel9roleNamesEv(
    const QQmlSortFilterProxyModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  int QQmlSortFilterProxyModel::itemRoleForName(const QString &roleName)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQmlSortFilterProxyModel15itemRoleForNameERK7QString(
    const QQmlSortFilterProxyModel *self,
    const QString *roleName) {
  return self->itemRoleForName(*roleName);
}

//  Qt::weak_ordering QQmlSortFilterProxyModel::compareData(const QVariant
//      &lhs, const QVariant &rhs)
extern "C" Q_DECL_EXPORT
Qt::weak_ordering *ritual_ZN24QQmlSortFilterProxyModel11compareDataERK8QVariantS2_(
    QQmlSortFilterProxyModel *self,
    const QVariant *lhs,
    const QVariant *rhs) {
  return new Qt::weak_ordering(self->compareData(*lhs, *rhs));
}

//  bool QQmlSortFilterProxyModel::filterAcceptsRow(int sourceRow, const
//      QModelIndex &sourceParent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlSortFilterProxyModel16filterAcceptsRowEiRK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    int sourceRow,
    const QModelIndex *sourceParent) {
  return self->filterAcceptsRow(sourceRow, *sourceParent);
}

//  bool QQmlSortFilterProxyModel::filterAcceptsColumn(int sourceColumn,
//      const QModelIndex &sourceParent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlSortFilterProxyModel19filterAcceptsColumnEiRK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    int sourceColumn,
    const QModelIndex *sourceParent) {
  return self->filterAcceptsColumn(sourceColumn, *sourceParent);
}

//  bool QQmlSortFilterProxyModel::lessThan(const QModelIndex &sourceLeft,
//      const QModelIndex &sourceRight) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlSortFilterProxyModel8lessThanERK11QModelIndexS2_(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *sourceLeft,
    const QModelIndex *sourceRight) {
  return self->lessThan(*sourceLeft, *sourceRight);
}

//  void QQmlSortFilterProxyModel::sort(int column, Qt::SortOrder sortOrder)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel4sortEiN2Qt9SortOrderE(
    QQmlSortFilterProxyModel *self,
    int column,
    Qt::SortOrder sortOrder) {
  self->sort(column, sortOrder);
}

//  void QQmlSortFilterProxyModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel10classBeginEv(
    QQmlSortFilterProxyModel *self) {
  self->classBegin();
}

//  void QQmlSortFilterProxyModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel17componentCompleteEv(
    QQmlSortFilterProxyModel *self) {
  self->componentComplete();
}

//  void QQmlSortFilterProxyModel::invalidateFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel16invalidateFilterEv(
    QQmlSortFilterProxyModel *self) {
  self->invalidateFilter();
}

//  void QQmlSortFilterProxyModel::dynamicSortFilterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel24dynamicSortFilterChangedEv(
    QQmlSortFilterProxyModel *self) {
  self->dynamicSortFilterChanged();
}

//  void QQmlSortFilterProxyModel::recursiveFilteringChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel25recursiveFilteringChangedEv(
    QQmlSortFilterProxyModel *self) {
  self->recursiveFilteringChanged();
}

//  void QQmlSortFilterProxyModel::autoAcceptChildRowsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel26autoAcceptChildRowsChangedEv(
    QQmlSortFilterProxyModel *self) {
  self->autoAcceptChildRowsChanged();
}

//  void QQmlSortFilterProxyModel::filtersChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel14filtersChangedEv(
    QQmlSortFilterProxyModel *self) {
  self->filtersChanged();
}

//  void QQmlSortFilterProxyModel::sortersChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel14sortersChangedEv(
    QQmlSortFilterProxyModel *self) {
  self->sortersChanged();
}

//  void QQmlSortFilterProxyModel::modelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel12modelChangedEv(
    QQmlSortFilterProxyModel *self) {
  self->modelChanged();
}

//  void QQmlSortFilterProxyModel::primarySorterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlSortFilterProxyModel20primarySorterChangedEv(
    QQmlSortFilterProxyModel *self) {
  self->primarySorterChanged();
}

//  QQmlSortFilterProxyModelPrivate *QQmlSortFilterProxyModel::d_func()
extern "C" Q_DECL_EXPORT
QQmlSortFilterProxyModelPrivate *ritual_ZN24QQmlSortFilterProxyModel6d_funcEv(
    QQmlSortFilterProxyModel *self) {
  return self->d_func();
}

//  const QQmlSortFilterProxyModelPrivate *QQmlSortFilterProxyModel::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQmlSortFilterProxyModelPrivate *ritual_ZNK24QQmlSortFilterProxyModel6d_funcEv(
    const QQmlSortFilterProxyModel *self) {
  return self->d_func();
}

//  QQmlSortFilterProxyModel as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQmlSortFilterProxyModel_QQmlParserStatus(
    QQmlSortFilterProxyModel *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQmlSortFilterProxyModel, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSortFilterProxyModel(
    QQmlSortFilterProxyModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSortFilterProxyModel *>(self)->take(key, call);
}

//  QModelIndex QQmlSortFilterProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK24QQmlSortFilterProxyModel11mapToSourceERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(
      self->QQmlSortFilterProxyModel::mapToSource(
          *proxyIndex));
}

//  QModelIndex QQmlSortFilterProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK24QQmlSortFilterProxyModel13mapFromSourceERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(
      self->QQmlSortFilterProxyModel::mapFromSource(
          *sourceIndex));
}

//  QModelIndex QQmlSortFilterProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK24QQmlSortFilterProxyModel5indexEiiRK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QQmlSortFilterProxyModel::index(
          row,
          column,
          *parent));
}

//  QModelIndex QQmlSortFilterProxyModel::parent(const QModelIndex &child)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK24QQmlSortFilterProxyModel6parentERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->QQmlSortFilterProxyModel::parent(*child));
}

//  QModelIndex QQmlSortFilterProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK24QQmlSortFilterProxyModel7siblingEiiRK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(
      self->QQmlSortFilterProxyModel::sibling(
          row,
          column,
          *idx));
}

//  bool QQmlSortFilterProxyModel::hasChildren(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QQmlSortFilterProxyModel11hasChildrenERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->QQmlSortFilterProxyModel::hasChildren(*parent);
}

//  int QQmlSortFilterProxyModel::columnCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QQmlSortFilterProxyModel11columnCountERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->QQmlSortFilterProxyModel::columnCount(*parent);
}

//  int QQmlSortFilterProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QQmlSortFilterProxyModel8rowCountERK11QModelIndex(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->QQmlSortFilterProxyModel::rowCount(*parent);
}

//  QVariant QQmlSortFilterProxyModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK24QQmlSortFilterProxyModel4dataERK11QModelIndexi(
    const QQmlSortFilterProxyModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QQmlSortFilterProxyModel::data(*index, role));
}

//  bool QQmlSortFilterProxyModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQmlSortFilterProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QQmlSortFilterProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QQmlSortFilterProxyModel::setData(*index, *value, role);
}

//  QVariant QQmlSortFilterProxyModel::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK24QQmlSortFilterProxyModel10headerDataEiN2Qt11OrientationEi(
    const QQmlSortFilterProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QQmlSortFilterProxyModel::headerData(
          section,
          orientation,
          role));
}

//  bool QQmlSortFilterProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQmlSortFilterProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QQmlSortFilterProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->QQmlSortFilterProxyModel::setHeaderData(
      section,
      orientation,
      *value,
      role);
}

//  bool QQmlSortFilterProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQmlSortFilterProxyModel10insertRowsEiiRK11QModelIndex(
    QQmlSortFilterProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QQmlSortFilterProxyModel::insertRows(row, count, *parent);
}

//  bool QQmlSortFilterProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQmlSortFilterProxyModel13insertColumnsEiiRK11QModelIndex(
    QQmlSortFilterProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QQmlSortFilterProxyModel::insertColumns(
      column,
      count,
      *parent);
}

//  bool QQmlSortFilterProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQmlSortFilterProxyModel10removeRowsEiiRK11QModelIndex(
    QQmlSortFilterProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QQmlSortFilterProxyModel::removeRows(row, count, *parent);
}

//  bool QQmlSortFilterProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQmlSortFilterProxyModel13removeColumnsEiiRK11QModelIndex(
    QQmlSortFilterProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QQmlSortFilterProxyModel::removeColumns(
      column,
      count,
      *parent);
}

//  QItemSelection QQmlSortFilterProxyModel::mapSelectionToSource(const
//      QItemSelection &proxySelection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_own_ZNK24QQmlSortFilterProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QQmlSortFilterProxyModel *self,
    const QItemSelection *proxySelection) {
  return new QItemSelection(
      self->QQmlSortFilterProxyModel::mapSelectionToSource(
          *proxySelection));
}

//  QItemSelection QQmlSortFilterProxyModel::mapSelectionFromSource(const
//      QItemSelection &sourceSelection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_own_ZNK24QQmlSortFilterProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QQmlSortFilterProxyModel *self,
    const QItemSelection *sourceSelection) {
  return new QItemSelection(
      self->QQmlSortFilterProxyModel::mapSelectionFromSource(
          *sourceSelection));
}

//  void QQmlSortFilterProxyModel::setSourceModel(QAbstractItemModel
//      *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQmlSortFilterProxyModel14setSourceModelEP18QAbstractItemModel(
    QQmlSortFilterProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->QQmlSortFilterProxyModel::setSourceModel(sourceModel);
}

//  void QQmlSortFilterProxyModel::sort(int column, Qt::SortOrder sortOrder)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQmlSortFilterProxyModel4sortEiN2Qt9SortOrderE(
    QQmlSortFilterProxyModel *self,
    int column,
    Qt::SortOrder sortOrder) {
  static_cast<OwnQQmlSortFilterProxyModel *>(self)->OwnQQmlSortFilterProxyModel::sort(
      column,
      sortOrder);
}

//  void QQmlSortFilterProxyModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQmlSortFilterProxyModel10classBeginEv(
    QQmlSortFilterProxyModel *self) {
  self->QQmlSortFilterProxyModel::classBegin();
}

//  void QQmlSortFilterProxyModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQmlSortFilterProxyModel17componentCompleteEv(
    QQmlSortFilterProxyModel *self) {
  self->QQmlSortFilterProxyModel::componentComplete();
}

//  a QQmlListProperty<QQmlFilterBase> a ritual of QQmlSortFilterProxyModel
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSortFilterProxyModel__QQmlListProperty_QQmlFilterBase(
    QQmlListProperty<QQmlFilterBase> *self) {
  delete self;
}

//  a QQmlListProperty<QQmlSorterBase> a ritual of QQmlSortFilterProxyModel
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSortFilterProxyModel__QQmlListProperty_QQmlSorterBase(
    QQmlListProperty<QQmlSorterBase> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_sfpm_model)
#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
