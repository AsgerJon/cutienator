//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsortfilterproxymodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(proxymodel) && QT_CONFIG(sortfilterproxymodel)
#if QT_CONFIG(sortfilterproxymodel)
#include <QtCore/qsortfilterproxymodel.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#if QT_CONFIG(itemmodel)
#include <QtCore/qitemselectionmodel.h>
#endif
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QBindable>
#include <QtCore/QRegularExpression>
#include <QtCore/Qt>

//  Only a class built on QSortFilterProxyModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSortFilterProxyModel : QSortFilterProxyModel {
  using QSortFilterProxyModel::filterAcceptsRow;
  using QSortFilterProxyModel::filterAcceptsColumn;
  using QSortFilterProxyModel::lessThan;
};

//  A QSortFilterProxyModel that Python can take functions over in. Every QSortFilterProxyModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef void (*CuteQSortFilterProxyModelCall0)(const void *, QAbstractItemModel *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QModelIndex * (*CuteQSortFilterProxyModelCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QModelIndex * (*CuteQSortFilterProxyModelCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QItemSelection * (*CuteQSortFilterProxyModelCall3)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QItemSelection * (*CuteQSortFilterProxyModelCall4)(const void *, const QItemSelection *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall5)(const void *, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall6)(const void *, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall7)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QModelIndex * (*CuteQSortFilterProxyModelCall8)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QModelIndex * (*CuteQSortFilterProxyModelCall9)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QModelIndex * (*CuteQSortFilterProxyModelCall10)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef int (*CuteQSortFilterProxyModelCall11)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef int (*CuteQSortFilterProxyModelCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QVariant * (*CuteQSortFilterProxyModelCall14)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall15)(const void *, const QModelIndex *, const QVariant *, int, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QVariant * (*CuteQSortFilterProxyModelCall16)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall17)(const void *, int, int, const QVariant *, int, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall18)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall19)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall20)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall21)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall22)(const void *, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef void (*CuteQSortFilterProxyModelCall23)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef bool (*CuteQSortFilterProxyModelCall24)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef int (*CuteQSortFilterProxyModelCall25)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QModelIndex * (*CuteQSortFilterProxyModelCall26)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef const QSize * (*CuteQSortFilterProxyModelCall27)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef void (*CuteQSortFilterProxyModelCall28)(const void *, int, int, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
typedef int (*CuteQSortFilterProxyModelCall29)(const void *, int *);
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQSortFilterProxyModelCall30)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef void (*CuteQSortFilterProxyModelCall31)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQSortFilterProxyModelCall32)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef bool (*CuteQSortFilterProxyModelCall33)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
typedef int (*CuteQSortFilterProxyModelCall34)(const void *, int *);
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSortFilterProxyModelCall35)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef bool (*CuteQSortFilterProxyModelCall36)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSortFilterProxyModelCall37)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQSortFilterProxyModelCall38)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSortFilterProxyModelCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSortFilterProxyModelCall40)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSortFilterProxyModelCall41)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSortFilterProxyModelCall42)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSortFilterProxyModelCall43)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSortFilterProxyModelCall44)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSortFilterProxyModelCall45)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSortFilterProxyModel : public QSortFilterProxyModel {
public:
  using QSortFilterProxyModel::QSortFilterProxyModel;
  void *taken[46] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZN19QAbstractProxyModel14setSourceModelEP18QAbstractItemModel")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel11mapToSourceERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel13mapFromSourceERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel20mapSelectionToSourceERK14QItemSelection")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel22mapSelectionFromSourceERK14QItemSelection")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK21QSortFilterProxyModel16filterAcceptsRowEiRK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK21QSortFilterProxyModel19filterAcceptsColumnEiRK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK21QSortFilterProxyModel8lessThanERK11QModelIndexS2_")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  void QSortFilterProxyModel::setSourceModel(QAbstractItemModel
  //      *sourceModel)
  void setSourceModel(QAbstractItemModel *sourceModel) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall0 call = reinterpret_cast<CuteQSortFilterProxyModelCall0>(taken[0]);
      call(this, sourceModel, &handled);
      if (handled) return;
    }
    QSortFilterProxyModel::setSourceModel(sourceModel);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QModelIndex QSortFilterProxyModel::mapToSource(const QModelIndex
  //      &proxyIndex) const
  QModelIndex mapToSource(const QModelIndex &proxyIndex) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall1 call = reinterpret_cast<CuteQSortFilterProxyModelCall1>(taken[1]);
      const QModelIndex * given = call(this, &proxyIndex, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::mapToSource(proxyIndex);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QModelIndex QSortFilterProxyModel::mapFromSource(const QModelIndex
  //      &sourceIndex) const
  QModelIndex mapFromSource(const QModelIndex &sourceIndex) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall2 call = reinterpret_cast<CuteQSortFilterProxyModelCall2>(taken[2]);
      const QModelIndex * given = call(this, &sourceIndex, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::mapFromSource(sourceIndex);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QItemSelection QSortFilterProxyModel::mapSelectionToSource(const
  //      QItemSelection &proxySelection) const
  QItemSelection mapSelectionToSource(
      const QItemSelection &proxySelection) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall3 call = reinterpret_cast<CuteQSortFilterProxyModelCall3>(taken[3]);
      const QItemSelection * given = call(this, &proxySelection, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::mapSelectionToSource(proxySelection);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(proxymodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QItemSelection QSortFilterProxyModel::mapSelectionFromSource(const
  //      QItemSelection &sourceSelection) const
  QItemSelection mapSelectionFromSource(
      const QItemSelection &sourceSelection) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall4 call = reinterpret_cast<CuteQSortFilterProxyModelCall4>(taken[4]);
      const QItemSelection * given = call(this, &sourceSelection, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::mapSelectionFromSource(sourceSelection);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel)

#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::filterAcceptsRow(int source_row, const
  //      QModelIndex &source_parent) const
  bool filterAcceptsRow(
      int source_row,
      const QModelIndex &source_parent) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall5 call = reinterpret_cast<CuteQSortFilterProxyModelCall5>(taken[5]);
      bool given = call(this, source_row, &source_parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::filterAcceptsRow(source_row, source_parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)

#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::filterAcceptsColumn(int source_column,
  //      const QModelIndex &source_parent) const
  bool filterAcceptsColumn(
      int source_column,
      const QModelIndex &source_parent) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall6 call = reinterpret_cast<CuteQSortFilterProxyModelCall6>(taken[6]);
      bool given = call(this, source_column, &source_parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::filterAcceptsColumn(source_column, source_parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)

#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::lessThan(const QModelIndex &source_left,
  //      const QModelIndex &source_right) const
  bool lessThan(
      const QModelIndex &source_left,
      const QModelIndex &source_right) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall7 call = reinterpret_cast<CuteQSortFilterProxyModelCall7>(taken[7]);
      bool given = call(this, &source_left, &source_right, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::lessThan(source_left, source_right);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QModelIndex QSortFilterProxyModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall8 call = reinterpret_cast<CuteQSortFilterProxyModelCall8>(taken[8]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::index(row, column, parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QModelIndex QSortFilterProxyModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall9 call = reinterpret_cast<CuteQSortFilterProxyModelCall9>(taken[9]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::parent(child);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QModelIndex QSortFilterProxyModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall10 call = reinterpret_cast<CuteQSortFilterProxyModelCall10>(taken[10]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::sibling(row, column, idx);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  int QSortFilterProxyModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall11 call = reinterpret_cast<CuteQSortFilterProxyModelCall11>(taken[11]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::rowCount(parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  int QSortFilterProxyModel::columnCount(const QModelIndex &parent)
  //      const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall12 call = reinterpret_cast<CuteQSortFilterProxyModelCall12>(taken[12]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::columnCount(parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::hasChildren(const QModelIndex &parent)
  //      const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall13 call = reinterpret_cast<CuteQSortFilterProxyModelCall13>(taken[13]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::hasChildren(parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QVariant QSortFilterProxyModel::data(const QModelIndex &index, int
  //      role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall14 call = reinterpret_cast<CuteQSortFilterProxyModelCall14>(taken[14]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::data(index, role);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall15 call = reinterpret_cast<CuteQSortFilterProxyModelCall15>(taken[15]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::setData(index, value, role);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QVariant QSortFilterProxyModel::headerData(int section,
  //      Qt::Orientation orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall16 call = reinterpret_cast<CuteQSortFilterProxyModelCall16>(taken[16]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::headerData(section, orientation, role);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::setHeaderData(int section,
  //      Qt::Orientation orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall17 call = reinterpret_cast<CuteQSortFilterProxyModelCall17>(taken[17]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::setHeaderData(section, orientation, value, role);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall18 call = reinterpret_cast<CuteQSortFilterProxyModelCall18>(taken[18]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::dropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall19 call = reinterpret_cast<CuteQSortFilterProxyModelCall19>(taken[19]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::insertRows(row, count, parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::insertColumns(int column, int count,
  //      const QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall20 call = reinterpret_cast<CuteQSortFilterProxyModelCall20>(taken[20]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::insertColumns(column, count, parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall21 call = reinterpret_cast<CuteQSortFilterProxyModelCall21>(taken[21]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::removeRows(row, count, parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::removeColumns(int column, int count,
  //      const QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall22 call = reinterpret_cast<CuteQSortFilterProxyModelCall22>(taken[22]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::removeColumns(column, count, parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  void QSortFilterProxyModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall23 call = reinterpret_cast<CuteQSortFilterProxyModelCall23>(taken[23]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QSortFilterProxyModel::fetchMore(parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  bool QSortFilterProxyModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall24 call = reinterpret_cast<CuteQSortFilterProxyModelCall24>(taken[24]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModel::canFetchMore(parent);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  Qt::ItemFlags QSortFilterProxyModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall25 call = reinterpret_cast<CuteQSortFilterProxyModelCall25>(taken[25]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QSortFilterProxyModel::flags(index);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QModelIndex QSortFilterProxyModel::buddy(const QModelIndex &index)
  //      const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall26 call = reinterpret_cast<CuteQSortFilterProxyModelCall26>(taken[26]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::buddy(index);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  QSize QSortFilterProxyModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall27 call = reinterpret_cast<CuteQSortFilterProxyModelCall27>(taken[27]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QSortFilterProxyModel::span(index);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  void QSortFilterProxyModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall28 call = reinterpret_cast<CuteQSortFilterProxyModelCall28>(taken[28]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QSortFilterProxyModel::sort(column, order);
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(sortfilterproxymodel)
  //  Qt::DropActions QSortFilterProxyModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall29 call = reinterpret_cast<CuteQSortFilterProxyModelCall29>(taken[29]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QSortFilterProxyModel::supportedDropActions();
  }
#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::submit()
  bool submit() override {
    if (taken[30]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall30 call = reinterpret_cast<CuteQSortFilterProxyModelCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall31 call = reinterpret_cast<CuteQSortFilterProxyModelCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::revert();
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  bool QAbstractProxyModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall32 call = reinterpret_cast<CuteQSortFilterProxyModelCall32>(taken[32]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::clearItemData(index);
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
    if (taken[33]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall33 call = reinterpret_cast<CuteQSortFilterProxyModelCall33>(taken[33]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::canDropMimeData(data, action, row, column, parent);
  }
#endif  // QT_CONFIG(proxymodel)
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
#if QT_CONFIG(proxymodel)
  //  Qt::DropActions QAbstractProxyModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall34 call = reinterpret_cast<CuteQSortFilterProxyModelCall34>(taken[34]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractProxyModel::supportedDragActions();
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
    if (taken[35]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall35 call = reinterpret_cast<CuteQSortFilterProxyModelCall35>(taken[35]);
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
    if (taken[36]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall36 call = reinterpret_cast<CuteQSortFilterProxyModelCall36>(taken[36]);
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
    if (taken[37]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall37 call = reinterpret_cast<CuteQSortFilterProxyModelCall37>(taken[37]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[38]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall38 call = reinterpret_cast<CuteQSortFilterProxyModelCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall39 call = reinterpret_cast<CuteQSortFilterProxyModelCall39>(taken[39]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall40 call = reinterpret_cast<CuteQSortFilterProxyModelCall40>(taken[40]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[41]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall41 call = reinterpret_cast<CuteQSortFilterProxyModelCall41>(taken[41]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[42]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall42 call = reinterpret_cast<CuteQSortFilterProxyModelCall42>(taken[42]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall43 call = reinterpret_cast<CuteQSortFilterProxyModelCall43>(taken[43]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[44]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall44 call = reinterpret_cast<CuteQSortFilterProxyModelCall44>(taken[44]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[45]) {
      int handled = 0;
      CuteQSortFilterProxyModelCall45 call = reinterpret_cast<CuteQSortFilterProxyModelCall45>(taken[45]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSortFilterProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QSortFilterProxyModel10metaObjectEv(
    const QSortFilterProxyModel *self) {
  return self->metaObject();
}

//  void *QSortFilterProxyModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QSortFilterProxyModel11qt_metacastEPKc(
    QSortFilterProxyModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSortFilterProxyModel::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QSortFilterProxyModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QSortFilterProxyModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSortFilterProxyModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QSortFilterProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSortFilterProxyModel::tr(s, c, n));
}

//  QSortFilterProxyModel::QSortFilterProxyModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QSortFilterProxyModel *ritual_ZN21QSortFilterProxyModelC1EP7QObject(
    QObject *parent) {
  return new CuteQSortFilterProxyModel(parent);
}

//  QSortFilterProxyModel::~QSortFilterProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModelD1Ev(QSortFilterProxyModel *self) {
  delete self;
}

//  void QSortFilterProxyModel::setSourceModel(QAbstractItemModel
//      *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel14setSourceModelEP18QAbstractItemModel(
    QSortFilterProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->setSourceModel(sourceModel);
}

//  QModelIndex QSortFilterProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel11mapToSourceERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QModelIndex QSortFilterProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel13mapFromSourceERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QItemSelection QSortFilterProxyModel::mapSelectionToSource(const
//      QItemSelection &proxySelection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK21QSortFilterProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QSortFilterProxyModel *self,
    const QItemSelection *proxySelection) {
  return new QItemSelection(self->mapSelectionToSource(*proxySelection));
}

//  QItemSelection QSortFilterProxyModel::mapSelectionFromSource(const
//      QItemSelection &sourceSelection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK21QSortFilterProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QSortFilterProxyModel *self,
    const QItemSelection *sourceSelection) {
  return new QItemSelection(self->mapSelectionFromSource(*sourceSelection));
}

//  QRegularExpression QSortFilterProxyModel::filterRegularExpression() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK21QSortFilterProxyModel23filterRegularExpressionEv(
    const QSortFilterProxyModel *self) {
  return new QRegularExpression(self->filterRegularExpression());
}

//  QBindable<QRegularExpression>
//      QSortFilterProxyModel::bindableFilterRegularExpression()
extern "C" Q_DECL_EXPORT
QBindable<QRegularExpression> *ritual_ZN21QSortFilterProxyModel31bindableFilterRegularExpressionEv(
    QSortFilterProxyModel *self) {
  return new QBindable<QRegularExpression>(
      self->bindableFilterRegularExpression());
}

//  int QSortFilterProxyModel::filterKeyColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel15filterKeyColumnEv(
    const QSortFilterProxyModel *self) {
  return self->filterKeyColumn();
}

//  void QSortFilterProxyModel::setFilterKeyColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel18setFilterKeyColumnEi(
    QSortFilterProxyModel *self,
    int column) {
  self->setFilterKeyColumn(column);
}

//  QBindable<int> QSortFilterProxyModel::bindableFilterKeyColumn()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN21QSortFilterProxyModel23bindableFilterKeyColumnEv(
    QSortFilterProxyModel *self) {
  return new QBindable<int>(self->bindableFilterKeyColumn());
}

//  Qt::CaseSensitivity QSortFilterProxyModel::filterCaseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK21QSortFilterProxyModel21filterCaseSensitivityEv(
    const QSortFilterProxyModel *self) {
  return self->filterCaseSensitivity();
}

//  void QSortFilterProxyModel::setFilterCaseSensitivity(Qt::CaseSensitivity
//      cs)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel24setFilterCaseSensitivityEN2Qt15CaseSensitivityE(
    QSortFilterProxyModel *self,
    Qt::CaseSensitivity cs) {
  self->setFilterCaseSensitivity(cs);
}

//  QBindable<Qt::CaseSensitivity>
//      QSortFilterProxyModel::bindableFilterCaseSensitivity()
extern "C" Q_DECL_EXPORT
QBindable<Qt::CaseSensitivity> *ritual_ZN21QSortFilterProxyModel29bindableFilterCaseSensitivityEv(
    QSortFilterProxyModel *self) {
  return new QBindable<Qt::CaseSensitivity>(
      self->bindableFilterCaseSensitivity());
}

//  Qt::CaseSensitivity QSortFilterProxyModel::sortCaseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK21QSortFilterProxyModel19sortCaseSensitivityEv(
    const QSortFilterProxyModel *self) {
  return self->sortCaseSensitivity();
}

//  void QSortFilterProxyModel::setSortCaseSensitivity(Qt::CaseSensitivity
//      cs)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel22setSortCaseSensitivityEN2Qt15CaseSensitivityE(
    QSortFilterProxyModel *self,
    Qt::CaseSensitivity cs) {
  self->setSortCaseSensitivity(cs);
}

//  QBindable<Qt::CaseSensitivity>
//      QSortFilterProxyModel::bindableSortCaseSensitivity()
extern "C" Q_DECL_EXPORT
QBindable<Qt::CaseSensitivity> *ritual_ZN21QSortFilterProxyModel27bindableSortCaseSensitivityEv(
    QSortFilterProxyModel *self) {
  return new QBindable<Qt::CaseSensitivity>(
      self->bindableSortCaseSensitivity());
}

//  bool QSortFilterProxyModel::isSortLocaleAware() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel17isSortLocaleAwareEv(
    const QSortFilterProxyModel *self) {
  return self->isSortLocaleAware();
}

//  void QSortFilterProxyModel::setSortLocaleAware(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel18setSortLocaleAwareEb(
    QSortFilterProxyModel *self,
    bool on) {
  self->setSortLocaleAware(on);
}

//  QBindable<bool> QSortFilterProxyModel::bindableIsSortLocaleAware()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN21QSortFilterProxyModel25bindableIsSortLocaleAwareEv(
    QSortFilterProxyModel *self) {
  return new QBindable<bool>(self->bindableIsSortLocaleAware());
}

//  int QSortFilterProxyModel::sortColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel10sortColumnEv(
    const QSortFilterProxyModel *self) {
  return self->sortColumn();
}

//  Qt::SortOrder QSortFilterProxyModel::sortOrder() const
extern "C" Q_DECL_EXPORT
Qt::SortOrder ritual_ZNK21QSortFilterProxyModel9sortOrderEv(
    const QSortFilterProxyModel *self) {
  return self->sortOrder();
}

//  bool QSortFilterProxyModel::dynamicSortFilter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel17dynamicSortFilterEv(
    const QSortFilterProxyModel *self) {
  return self->dynamicSortFilter();
}

//  void QSortFilterProxyModel::setDynamicSortFilter(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel20setDynamicSortFilterEb(
    QSortFilterProxyModel *self,
    bool enable) {
  self->setDynamicSortFilter(enable);
}

//  QBindable<bool> QSortFilterProxyModel::bindableDynamicSortFilter()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN21QSortFilterProxyModel25bindableDynamicSortFilterEv(
    QSortFilterProxyModel *self) {
  return new QBindable<bool>(self->bindableDynamicSortFilter());
}

//  int QSortFilterProxyModel::sortRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel8sortRoleEv(
    const QSortFilterProxyModel *self) {
  return self->sortRole();
}

//  void QSortFilterProxyModel::setSortRole(int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel11setSortRoleEi(
    QSortFilterProxyModel *self,
    int role) {
  self->setSortRole(role);
}

//  QBindable<int> QSortFilterProxyModel::bindableSortRole()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN21QSortFilterProxyModel16bindableSortRoleEv(
    QSortFilterProxyModel *self) {
  return new QBindable<int>(self->bindableSortRole());
}

//  int QSortFilterProxyModel::filterRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel10filterRoleEv(
    const QSortFilterProxyModel *self) {
  return self->filterRole();
}

//  void QSortFilterProxyModel::setFilterRole(int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel13setFilterRoleEi(
    QSortFilterProxyModel *self,
    int role) {
  self->setFilterRole(role);
}

//  QBindable<int> QSortFilterProxyModel::bindableFilterRole()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN21QSortFilterProxyModel18bindableFilterRoleEv(
    QSortFilterProxyModel *self) {
  return new QBindable<int>(self->bindableFilterRole());
}

//  bool QSortFilterProxyModel::isRecursiveFilteringEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel27isRecursiveFilteringEnabledEv(
    const QSortFilterProxyModel *self) {
  return self->isRecursiveFilteringEnabled();
}

//  void QSortFilterProxyModel::setRecursiveFilteringEnabled(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel28setRecursiveFilteringEnabledEb(
    QSortFilterProxyModel *self,
    bool recursive) {
  self->setRecursiveFilteringEnabled(recursive);
}

//  QBindable<bool>
//      QSortFilterProxyModel::bindableRecursiveFilteringEnabled()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN21QSortFilterProxyModel33bindableRecursiveFilteringEnabledEv(
    QSortFilterProxyModel *self) {
  return new QBindable<bool>(self->bindableRecursiveFilteringEnabled());
}

//  bool QSortFilterProxyModel::autoAcceptChildRows() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel19autoAcceptChildRowsEv(
    const QSortFilterProxyModel *self) {
  return self->autoAcceptChildRows();
}

//  void QSortFilterProxyModel::setAutoAcceptChildRows(bool accept)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel22setAutoAcceptChildRowsEb(
    QSortFilterProxyModel *self,
    bool accept) {
  self->setAutoAcceptChildRows(accept);
}

//  QBindable<bool> QSortFilterProxyModel::bindableAutoAcceptChildRows()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN21QSortFilterProxyModel27bindableAutoAcceptChildRowsEv(
    QSortFilterProxyModel *self) {
  return new QBindable<bool>(self->bindableAutoAcceptChildRows());
}

//  void QSortFilterProxyModel::setFilterRegularExpression(const QString
//      &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel26setFilterRegularExpressionERK7QString(
    QSortFilterProxyModel *self,
    const QString *pattern) {
  self->setFilterRegularExpression(*pattern);
}

//  void QSortFilterProxyModel::setFilterRegularExpression(const
//      QRegularExpression &regularExpression)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel26setFilterRegularExpressionERK18QRegularExpression(
    QSortFilterProxyModel *self,
    const QRegularExpression *regularExpression) {
  self->setFilterRegularExpression(*regularExpression);
}

//  void QSortFilterProxyModel::setFilterWildcard(const QString &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel17setFilterWildcardERK7QString(
    QSortFilterProxyModel *self,
    const QString *pattern) {
  self->setFilterWildcard(*pattern);
}

//  void QSortFilterProxyModel::setFilterFixedString(const QString &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel20setFilterFixedStringERK7QString(
    QSortFilterProxyModel *self,
    const QString *pattern) {
  self->setFilterFixedString(*pattern);
}

//  void QSortFilterProxyModel::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel10invalidateEv(
    QSortFilterProxyModel *self) {
  self->invalidate();
}

//  bool QSortFilterProxyModel::filterAcceptsRow(int source_row, const
//      QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel16filterAcceptsRowEiRK11QModelIndex(
    const QSortFilterProxyModel *self,
    int source_row,
    const QModelIndex *source_parent) {
  return self->filterAcceptsRow(source_row, *source_parent);
}

//  bool QSortFilterProxyModel::filterAcceptsColumn(int source_column, const
//      QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel19filterAcceptsColumnEiRK11QModelIndex(
    const QSortFilterProxyModel *self,
    int source_column,
    const QModelIndex *source_parent) {
  return self->filterAcceptsColumn(source_column, *source_parent);
}

//  bool QSortFilterProxyModel::lessThan(const QModelIndex &source_left,
//      const QModelIndex &source_right) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel8lessThanERK11QModelIndexS2_(
    const QSortFilterProxyModel *self,
    const QModelIndex *source_left,
    const QModelIndex *source_right) {
  return self->lessThan(*source_left, *source_right);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  DataChangeRelevanceFlags
//      QSortFilterProxyModel::dataChangeRelevanceFlags(const QModelIndex
//      &sourceTopLeft, const QModelIndex &sourceBottomRight, const
//      QList<int> &roles) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel24dataChangeRelevanceFlagsERK11QModelIndexS2_RK5QListIiE(
    const QSortFilterProxyModel *self,
    const QModelIndex *sourceTopLeft,
    const QModelIndex *sourceBottomRight,
    const QList<int> *roles) {
  return static_cast<int>(
      self->dataChangeRelevanceFlags(
          *sourceTopLeft,
          *sourceBottomRight,
          *roles).toInt());
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QSortFilterProxyModel::beginFilterChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel17beginFilterChangeEv(
    QSortFilterProxyModel *self) {
  self->beginFilterChange();
}

//  void QSortFilterProxyModel::endFilterChange(Directions directions)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel15endFilterChangeE6QFlagsINS_9DirectionEE(
    QSortFilterProxyModel *self,
    int directions) {
  self->endFilterChange(
      QFlags<QSortFilterProxyModel::Direction>::fromInt(directions));
}

#if QT_DEPRECATED_SINCE(6, 13)
//  void QSortFilterProxyModel::invalidateFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel16invalidateFilterEv(
    QSortFilterProxyModel *self) {
  self->invalidateFilter();
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  void QSortFilterProxyModel::invalidateRowsFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel20invalidateRowsFilterEv(
    QSortFilterProxyModel *self) {
  self->invalidateRowsFilter();
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

#if QT_DEPRECATED_SINCE(6, 13)
//  void QSortFilterProxyModel::invalidateColumnsFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel23invalidateColumnsFilterEv(
    QSortFilterProxyModel *self) {
  self->invalidateColumnsFilter();
}
#endif  // QT_DEPRECATED_SINCE(6, 13)

//  QModelIndex QSortFilterProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel5indexEiiRK11QModelIndex(
    const QSortFilterProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QSortFilterProxyModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel6parentERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  QModelIndex QSortFilterProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel7siblingEiiRK11QModelIndex(
    const QSortFilterProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  int QSortFilterProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel8rowCountERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QSortFilterProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel11columnCountERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  bool QSortFilterProxyModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel11hasChildrenERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QVariant QSortFilterProxyModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QSortFilterProxyModel4dataERK11QModelIndexi(
    const QSortFilterProxyModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QSortFilterProxyModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QSortFilterProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QVariant QSortFilterProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QSortFilterProxyModel10headerDataEiN2Qt11OrientationEi(
    const QSortFilterProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QSortFilterProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QSortFilterProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  QMimeData *QSortFilterProxyModel::mimeData(const QModelIndexList
//      &indexes) const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK21QSortFilterProxyModel8mimeDataERK5QListI11QModelIndexE(
    const QSortFilterProxyModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  bool QSortFilterProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  bool QSortFilterProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel10insertRowsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QSortFilterProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel13insertColumnsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QSortFilterProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel10removeRowsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QSortFilterProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel13removeColumnsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  void QSortFilterProxyModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel9fetchMoreERK11QModelIndex(
    QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  bool QSortFilterProxyModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel12canFetchMoreERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  Qt::ItemFlags QSortFilterProxyModel::flags(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel5flagsERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  QModelIndex QSortFilterProxyModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel5buddyERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->buddy(*index));
}

//  QModelIndexList QSortFilterProxyModel::match(const QModelIndex &start,
//      int role, const QVariant &value, int hits, Qt::MatchFlags flags)
//      const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK21QSortFilterProxyModel5matchERK11QModelIndexiRK8QVarianti6QFlagsIN2Qt9MatchFlagEE(
    const QSortFilterProxyModel *self,
    const QModelIndex *start,
    int role,
    const QVariant *value,
    int hits,
    int flags) {
  return new QList<QModelIndex>(
      self->match(
          *start,
          role,
          *value,
          hits,
          QFlags<Qt::MatchFlag>::fromInt(flags)));
}

//  QSize QSortFilterProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QSortFilterProxyModel4spanERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  void QSortFilterProxyModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel4sortEiN2Qt9SortOrderE(
    QSortFilterProxyModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QStringList QSortFilterProxyModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QSortFilterProxyModel9mimeTypesEv(
    const QSortFilterProxyModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  Qt::DropActions QSortFilterProxyModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel20supportedDropActionsEv(
    const QSortFilterProxyModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  void QSortFilterProxyModel::dynamicSortFilterChanged(bool
//      dynamicSortFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel24dynamicSortFilterChangedEb(
    QSortFilterProxyModel *self,
    bool dynamicSortFilter) {
  self->dynamicSortFilterChanged(dynamicSortFilter);
}

//  void
//      QSortFilterProxyModel::filterCaseSensitivityChanged(Qt::CaseSensitivi
//      ty filterCaseSensitivity)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel28filterCaseSensitivityChangedEN2Qt15CaseSensitivityE(
    QSortFilterProxyModel *self,
    Qt::CaseSensitivity filterCaseSensitivity) {
  self->filterCaseSensitivityChanged(filterCaseSensitivity);
}

//  void
//      QSortFilterProxyModel::sortCaseSensitivityChanged(Qt::CaseSensitivity
//      sortCaseSensitivity)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel26sortCaseSensitivityChangedEN2Qt15CaseSensitivityE(
    QSortFilterProxyModel *self,
    Qt::CaseSensitivity sortCaseSensitivity) {
  self->sortCaseSensitivityChanged(sortCaseSensitivity);
}

//  void QSortFilterProxyModel::sortLocaleAwareChanged(bool sortLocaleAware)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel22sortLocaleAwareChangedEb(
    QSortFilterProxyModel *self,
    bool sortLocaleAware) {
  self->sortLocaleAwareChanged(sortLocaleAware);
}

//  void QSortFilterProxyModel::sortRoleChanged(int sortRole)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel15sortRoleChangedEi(
    QSortFilterProxyModel *self,
    int sortRole) {
  self->sortRoleChanged(sortRole);
}

//  void QSortFilterProxyModel::filterRoleChanged(int filterRole)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel17filterRoleChangedEi(
    QSortFilterProxyModel *self,
    int filterRole) {
  self->filterRoleChanged(filterRole);
}

//  void QSortFilterProxyModel::recursiveFilteringEnabledChanged(bool
//      recursiveFilteringEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel32recursiveFilteringEnabledChangedEb(
    QSortFilterProxyModel *self,
    bool recursiveFilteringEnabled) {
  self->recursiveFilteringEnabledChanged(recursiveFilteringEnabled);
}

//  void QSortFilterProxyModel::autoAcceptChildRowsChanged(bool
//      autoAcceptChildRows)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel26autoAcceptChildRowsChangedEb(
    QSortFilterProxyModel *self,
    bool autoAcceptChildRows) {
  self->autoAcceptChildRowsChanged(autoAcceptChildRows);
}

//  QSortFilterProxyModelPrivate *QSortFilterProxyModel::d_func()
extern "C" Q_DECL_EXPORT
QSortFilterProxyModelPrivate *ritual_ZN21QSortFilterProxyModel6d_funcEv(
    QSortFilterProxyModel *self) {
  return self->d_func();
}

//  const QSortFilterProxyModelPrivate *QSortFilterProxyModel::d_func() const
extern "C" Q_DECL_EXPORT
const QSortFilterProxyModelPrivate *ritual_ZNK21QSortFilterProxyModel6d_funcEv(
    const QSortFilterProxyModel *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSortFilterProxyModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSortFilterProxyModel(
    QSortFilterProxyModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSortFilterProxyModel *>(self)->take(key, call);
}

//  void QSortFilterProxyModel::setSourceModel(QAbstractItemModel
//      *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSortFilterProxyModel14setSourceModelEP18QAbstractItemModel(
    QSortFilterProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->QSortFilterProxyModel::setSourceModel(sourceModel);
}

//  QModelIndex QSortFilterProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK21QSortFilterProxyModel11mapToSourceERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(
      self->QSortFilterProxyModel::mapToSource(
          *proxyIndex));
}

//  QModelIndex QSortFilterProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK21QSortFilterProxyModel13mapFromSourceERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(
      self->QSortFilterProxyModel::mapFromSource(
          *sourceIndex));
}

//  QItemSelection QSortFilterProxyModel::mapSelectionToSource(const
//      QItemSelection &proxySelection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_own_ZNK21QSortFilterProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QSortFilterProxyModel *self,
    const QItemSelection *proxySelection) {
  return new QItemSelection(
      self->QSortFilterProxyModel::mapSelectionToSource(
          *proxySelection));
}

//  QItemSelection QSortFilterProxyModel::mapSelectionFromSource(const
//      QItemSelection &sourceSelection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_own_ZNK21QSortFilterProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QSortFilterProxyModel *self,
    const QItemSelection *sourceSelection) {
  return new QItemSelection(
      self->QSortFilterProxyModel::mapSelectionFromSource(
          *sourceSelection));
}

//  bool QSortFilterProxyModel::filterAcceptsRow(int source_row, const
//      QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QSortFilterProxyModel16filterAcceptsRowEiRK11QModelIndex(
    const QSortFilterProxyModel *self,
    int source_row,
    const QModelIndex *source_parent) {
  return static_cast<const OwnQSortFilterProxyModel *>(self)->OwnQSortFilterProxyModel::filterAcceptsRow(
      source_row,
      *source_parent);
}

//  bool QSortFilterProxyModel::filterAcceptsColumn(int source_column, const
//      QModelIndex &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QSortFilterProxyModel19filterAcceptsColumnEiRK11QModelIndex(
    const QSortFilterProxyModel *self,
    int source_column,
    const QModelIndex *source_parent) {
  return static_cast<const OwnQSortFilterProxyModel *>(self)->OwnQSortFilterProxyModel::filterAcceptsColumn(
      source_column,
      *source_parent);
}

//  bool QSortFilterProxyModel::lessThan(const QModelIndex &source_left,
//      const QModelIndex &source_right) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QSortFilterProxyModel8lessThanERK11QModelIndexS2_(
    const QSortFilterProxyModel *self,
    const QModelIndex *source_left,
    const QModelIndex *source_right) {
  return static_cast<const OwnQSortFilterProxyModel *>(self)->OwnQSortFilterProxyModel::lessThan(
      *source_left,
      *source_right);
}

//  QModelIndex QSortFilterProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK21QSortFilterProxyModel5indexEiiRK11QModelIndex(
    const QSortFilterProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QSortFilterProxyModel::index(
          row,
          column,
          *parent));
}

//  QModelIndex QSortFilterProxyModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK21QSortFilterProxyModel6parentERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->QSortFilterProxyModel::parent(*child));
}

//  QModelIndex QSortFilterProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK21QSortFilterProxyModel7siblingEiiRK11QModelIndex(
    const QSortFilterProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(
      self->QSortFilterProxyModel::sibling(
          row,
          column,
          *idx));
}

//  int QSortFilterProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QSortFilterProxyModel8rowCountERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->QSortFilterProxyModel::rowCount(*parent);
}

//  int QSortFilterProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QSortFilterProxyModel11columnCountERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->QSortFilterProxyModel::columnCount(*parent);
}

//  bool QSortFilterProxyModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QSortFilterProxyModel11hasChildrenERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->QSortFilterProxyModel::hasChildren(*parent);
}

//  QVariant QSortFilterProxyModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK21QSortFilterProxyModel4dataERK11QModelIndexi(
    const QSortFilterProxyModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QSortFilterProxyModel::data(*index, role));
}

//  bool QSortFilterProxyModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QSortFilterProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QSortFilterProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QSortFilterProxyModel::setData(*index, *value, role);
}

//  QVariant QSortFilterProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK21QSortFilterProxyModel10headerDataEiN2Qt11OrientationEi(
    const QSortFilterProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QSortFilterProxyModel::headerData(
          section,
          orientation,
          role));
}

//  bool QSortFilterProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QSortFilterProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QSortFilterProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->QSortFilterProxyModel::setHeaderData(
      section,
      orientation,
      *value,
      role);
}

//  bool QSortFilterProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QSortFilterProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QSortFilterProxyModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  bool QSortFilterProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QSortFilterProxyModel10insertRowsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QSortFilterProxyModel::insertRows(row, count, *parent);
}

//  bool QSortFilterProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QSortFilterProxyModel13insertColumnsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QSortFilterProxyModel::insertColumns(column, count, *parent);
}

//  bool QSortFilterProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QSortFilterProxyModel10removeRowsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QSortFilterProxyModel::removeRows(row, count, *parent);
}

//  bool QSortFilterProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QSortFilterProxyModel13removeColumnsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QSortFilterProxyModel::removeColumns(column, count, *parent);
}

//  void QSortFilterProxyModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSortFilterProxyModel9fetchMoreERK11QModelIndex(
    QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  self->QSortFilterProxyModel::fetchMore(*parent);
}

//  bool QSortFilterProxyModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QSortFilterProxyModel12canFetchMoreERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->QSortFilterProxyModel::canFetchMore(*parent);
}

//  Qt::ItemFlags QSortFilterProxyModel::flags(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QSortFilterProxyModel5flagsERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *index) {
  return static_cast<int>(
      self->QSortFilterProxyModel::flags(
          *index).toInt());
}

//  QModelIndex QSortFilterProxyModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK21QSortFilterProxyModel5buddyERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->QSortFilterProxyModel::buddy(*index));
}

//  QSize QSortFilterProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK21QSortFilterProxyModel4spanERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->QSortFilterProxyModel::span(*index));
}

//  void QSortFilterProxyModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSortFilterProxyModel4sortEiN2Qt9SortOrderE(
    QSortFilterProxyModel *self,
    int column,
    Qt::SortOrder order) {
  self->QSortFilterProxyModel::sort(column, order);
}

//  Qt::DropActions QSortFilterProxyModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QSortFilterProxyModel20supportedDropActionsEv(
    const QSortFilterProxyModel *self) {
  return static_cast<int>(
      self->QSortFilterProxyModel::supportedDropActions().toInt());
}

//  a QBindable<QRegularExpression> a ritual of QSortFilterProxyModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSortFilterProxyModel__QBindable_QRegularExpression(
    QBindable<QRegularExpression> *self) {
  delete self;
}

//  a QBindable<int> a ritual of QSortFilterProxyModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSortFilterProxyModel__QBindable_int(QBindable<int> *self) {
  delete self;
}

//  a QBindable<Qt::CaseSensitivity> a ritual of QSortFilterProxyModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSortFilterProxyModel__QBindable_Qt_CaseSensitivity(
    QBindable<Qt::CaseSensitivity> *self) {
  delete self;
}

//  a QBindable<bool> a ritual of QSortFilterProxyModel gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSortFilterProxyModel__QBindable_bool(
    QBindable<bool> *self) {
  delete self;
}

#endif  // QT_CONFIG(sortfilterproxymodel)
#endif  // QT_CONFIG(proxymodel) && QT_CONFIG(sortfilterproxymodel)
