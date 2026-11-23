//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractproxymodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstractproxymodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QAbstractProxyModel that Python can take functions over in. Every QAbstractProxyModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractProxyModelCall0)(const void *, QAbstractItemModel *, int *);
typedef const QModelIndex * (*CuteQAbstractProxyModelCall1)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQAbstractProxyModelCall2)(const void *, const QModelIndex *, int *);
typedef const QItemSelection * (*CuteQAbstractProxyModelCall3)(const void *, const QItemSelection *, int *);
typedef const QItemSelection * (*CuteQAbstractProxyModelCall4)(const void *, const QItemSelection *, int *);
typedef bool (*CuteQAbstractProxyModelCall5)(const void *, int *);
typedef void (*CuteQAbstractProxyModelCall6)(const void *, int *);
typedef const QVariant * (*CuteQAbstractProxyModelCall7)(const void *, const QModelIndex *, int, int *);
typedef const QVariant * (*CuteQAbstractProxyModelCall8)(const void *, int, int, int, int *);
typedef int (*CuteQAbstractProxyModelCall9)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQAbstractProxyModelCall10)(const void *, const QModelIndex *, const QVariant *, int, int *);
typedef bool (*CuteQAbstractProxyModelCall11)(const void *, int, int, const QVariant *, int, int *);
typedef bool (*CuteQAbstractProxyModelCall12)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQAbstractProxyModelCall13)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQAbstractProxyModelCall14)(const void *, const QModelIndex *, int *);
typedef void (*CuteQAbstractProxyModelCall15)(const void *, const QModelIndex *, int *);
typedef void (*CuteQAbstractProxyModelCall16)(const void *, int, int, int *);
typedef const QSize * (*CuteQAbstractProxyModelCall17)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQAbstractProxyModelCall18)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQAbstractProxyModelCall19)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractProxyModelCall20)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractProxyModelCall21)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef int (*CuteQAbstractProxyModelCall22)(const void *, int *);
typedef int (*CuteQAbstractProxyModelCall23)(const void *, int *);
typedef const QModelIndex * (*CuteQAbstractProxyModelCall24)(const void *, int, int, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQAbstractProxyModelCall25)(const void *, const QModelIndex *, int *);
typedef int (*CuteQAbstractProxyModelCall26)(const void *, const QModelIndex *, int *);
typedef int (*CuteQAbstractProxyModelCall27)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQAbstractProxyModelCall28)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractProxyModelCall29)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractProxyModelCall30)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractProxyModelCall31)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractProxyModelCall32)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef bool (*CuteQAbstractProxyModelCall33)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteQAbstractProxyModelCall34)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
typedef void (*CuteQAbstractProxyModelCall35)(const void *, int *);
typedef bool (*CuteQAbstractProxyModelCall36)(const void *, QEvent *, int *);
typedef bool (*CuteQAbstractProxyModelCall37)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAbstractProxyModelCall38)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAbstractProxyModelCall39)(const void *, QChildEvent *, int *);
typedef void (*CuteQAbstractProxyModelCall40)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractProxyModelCall41)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAbstractProxyModelCall42)(const void *, const QMetaMethod *, int *);
class CuteQAbstractProxyModel : public QAbstractProxyModel {
public:
  using QAbstractProxyModel::QAbstractProxyModel;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QAbstractProxyModel14setSourceModelEP18QAbstractItemModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel11mapToSourceERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel13mapFromSourceERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel20mapSelectionToSourceERK14QItemSelection")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel22mapSelectionFromSourceERK14QItemSelection")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[42] = call;
      return true;
    }
    return false;
  }

  //  void QAbstractProxyModel::setSourceModel(QAbstractItemModel
  //      *sourceModel)
  void setSourceModel(QAbstractItemModel *sourceModel) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractProxyModelCall0 call = reinterpret_cast<CuteQAbstractProxyModelCall0>(taken[0]);
      call(this, sourceModel, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::setSourceModel(sourceModel);
  }

  //  QModelIndex QAbstractProxyModel::mapToSource(const QModelIndex
  //      &proxyIndex) const
  QModelIndex mapToSource(const QModelIndex &proxyIndex) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractProxyModelCall1 call = reinterpret_cast<CuteQAbstractProxyModelCall1>(taken[1]);
      const QModelIndex * given = call(this, &proxyIndex, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QModelIndex QAbstractProxyModel::mapFromSource(const QModelIndex
  //      &sourceIndex) const
  QModelIndex mapFromSource(const QModelIndex &sourceIndex) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractProxyModelCall2 call = reinterpret_cast<CuteQAbstractProxyModelCall2>(taken[2]);
      const QModelIndex * given = call(this, &sourceIndex, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QItemSelection QAbstractProxyModel::mapSelectionToSource(const
  //      QItemSelection &selection) const
  QItemSelection mapSelectionToSource(
      const QItemSelection &selection) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractProxyModelCall3 call = reinterpret_cast<CuteQAbstractProxyModelCall3>(taken[3]);
      const QItemSelection * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::mapSelectionToSource(selection);
  }

  //  QItemSelection QAbstractProxyModel::mapSelectionFromSource(const
  //      QItemSelection &selection) const
  QItemSelection mapSelectionFromSource(
      const QItemSelection &selection) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractProxyModelCall4 call = reinterpret_cast<CuteQAbstractProxyModelCall4>(taken[4]);
      const QItemSelection * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::mapSelectionFromSource(selection);
  }

  //  bool QAbstractProxyModel::submit()
  bool submit() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractProxyModelCall5 call = reinterpret_cast<CuteQAbstractProxyModelCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::submit();
  }

  //  void QAbstractProxyModel::revert()
  void revert() override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractProxyModelCall6 call = reinterpret_cast<CuteQAbstractProxyModelCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::revert();
  }

  //  QVariant QAbstractProxyModel::data(const QModelIndex &proxyIndex, int
  //      role) const
  QVariant data(const QModelIndex &proxyIndex, int role) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractProxyModelCall7 call = reinterpret_cast<CuteQAbstractProxyModelCall7>(taken[7]);
      const QVariant * given = call(this, &proxyIndex, role, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::data(proxyIndex, role);
  }

  //  QVariant QAbstractProxyModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractProxyModelCall8 call = reinterpret_cast<CuteQAbstractProxyModelCall8>(taken[8]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::headerData(section, orientation, role);
  }

  //  Qt::ItemFlags QAbstractProxyModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractProxyModelCall9 call = reinterpret_cast<CuteQAbstractProxyModelCall9>(taken[9]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QAbstractProxyModel::flags(index);
  }

  //  bool QAbstractProxyModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractProxyModelCall10 call = reinterpret_cast<CuteQAbstractProxyModelCall10>(taken[10]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::setData(index, value, role);
  }

  //  bool QAbstractProxyModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractProxyModelCall11 call = reinterpret_cast<CuteQAbstractProxyModelCall11>(taken[11]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::setHeaderData(section, orientation, value, role);
  }

  //  bool QAbstractProxyModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractProxyModelCall12 call = reinterpret_cast<CuteQAbstractProxyModelCall12>(taken[12]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::clearItemData(index);
  }

  //  QModelIndex QAbstractProxyModel::buddy(const QModelIndex &index)
  //      const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractProxyModelCall13 call = reinterpret_cast<CuteQAbstractProxyModelCall13>(taken[13]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::buddy(index);
  }

  //  bool QAbstractProxyModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractProxyModelCall14 call = reinterpret_cast<CuteQAbstractProxyModelCall14>(taken[14]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::canFetchMore(parent);
  }

  //  void QAbstractProxyModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractProxyModelCall15 call = reinterpret_cast<CuteQAbstractProxyModelCall15>(taken[15]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::fetchMore(parent);
  }

  //  void QAbstractProxyModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractProxyModelCall16 call = reinterpret_cast<CuteQAbstractProxyModelCall16>(taken[16]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractProxyModel::sort(column, order);
  }

  //  QSize QAbstractProxyModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractProxyModelCall17 call = reinterpret_cast<CuteQAbstractProxyModelCall17>(taken[17]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::span(index);
  }

  //  bool QAbstractProxyModel::hasChildren(const QModelIndex &parent)
  //      const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractProxyModelCall18 call = reinterpret_cast<CuteQAbstractProxyModelCall18>(taken[18]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::hasChildren(parent);
  }

  //  QModelIndex QAbstractProxyModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractProxyModelCall19 call = reinterpret_cast<CuteQAbstractProxyModelCall19>(taken[19]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::sibling(row, column, idx);
  }

  //  bool QAbstractProxyModel::canDropMimeData(const QMimeData *data,
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
      CuteQAbstractProxyModelCall20 call = reinterpret_cast<CuteQAbstractProxyModelCall20>(taken[20]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::canDropMimeData(data, action, row, column, parent);
  }

  //  bool QAbstractProxyModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractProxyModelCall21 call = reinterpret_cast<CuteQAbstractProxyModelCall21>(taken[21]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::dropMimeData(data, action, row, column, parent);
  }

  //  Qt::DropActions QAbstractProxyModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractProxyModelCall22 call = reinterpret_cast<CuteQAbstractProxyModelCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractProxyModel::supportedDragActions();
  }

  //  Qt::DropActions QAbstractProxyModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractProxyModelCall23 call = reinterpret_cast<CuteQAbstractProxyModelCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractProxyModel::supportedDropActions();
  }

  //  QModelIndex QAbstractItemModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractProxyModelCall24 call = reinterpret_cast<CuteQAbstractProxyModelCall24>(taken[24]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QModelIndex QAbstractItemModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractProxyModelCall25 call = reinterpret_cast<CuteQAbstractProxyModelCall25>(taken[25]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  int QAbstractItemModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractProxyModelCall26 call = reinterpret_cast<CuteQAbstractProxyModelCall26>(taken[26]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAbstractItemModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractProxyModelCall27 call = reinterpret_cast<CuteQAbstractProxyModelCall27>(taken[27]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QAbstractItemModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractProxyModelCall28 call = reinterpret_cast<CuteQAbstractProxyModelCall28>(taken[28]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertRows(row, count, parent);
  }

  //  bool QAbstractItemModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractProxyModelCall29 call = reinterpret_cast<CuteQAbstractProxyModelCall29>(taken[29]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertColumns(column, count, parent);
  }

  //  bool QAbstractItemModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractProxyModelCall30 call = reinterpret_cast<CuteQAbstractProxyModelCall30>(taken[30]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeRows(row, count, parent);
  }

  //  bool QAbstractItemModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractProxyModelCall31 call = reinterpret_cast<CuteQAbstractProxyModelCall31>(taken[31]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::removeColumns(column, count, parent);
  }

  //  bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent,
  //      int sourceRow, int count, const QModelIndex &destinationParent,
  //      int destinationChild)
  bool moveRows(
      const QModelIndex &sourceParent,
      int sourceRow,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractProxyModelCall32 call = reinterpret_cast<CuteQAbstractProxyModelCall32>(taken[32]);
      bool given = call(this, &sourceParent, sourceRow, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveRows(sourceParent, sourceRow, count, destinationParent, destinationChild);
  }

  //  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent,
  //      int sourceColumn, int count, const QModelIndex
  //      &destinationParent, int destinationChild)
  bool moveColumns(
      const QModelIndex &sourceParent,
      int sourceColumn,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAbstractProxyModelCall33 call = reinterpret_cast<CuteQAbstractProxyModelCall33>(taken[33]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }

  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQAbstractProxyModelCall34 call = reinterpret_cast<CuteQAbstractProxyModelCall34>(taken[34]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }

  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[35]) {
      int handled = 0;
      CuteQAbstractProxyModelCall35 call = reinterpret_cast<CuteQAbstractProxyModelCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQAbstractProxyModelCall36 call = reinterpret_cast<CuteQAbstractProxyModelCall36>(taken[36]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQAbstractProxyModelCall37 call = reinterpret_cast<CuteQAbstractProxyModelCall37>(taken[37]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQAbstractProxyModelCall38 call = reinterpret_cast<CuteQAbstractProxyModelCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQAbstractProxyModelCall39 call = reinterpret_cast<CuteQAbstractProxyModelCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQAbstractProxyModelCall40 call = reinterpret_cast<CuteQAbstractProxyModelCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQAbstractProxyModelCall41 call = reinterpret_cast<CuteQAbstractProxyModelCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[42]) {
      int handled = 0;
      CuteQAbstractProxyModelCall42 call = reinterpret_cast<CuteQAbstractProxyModelCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QAbstractProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAbstractProxyModel10metaObjectEv(
    const QAbstractProxyModel *self) {
  return self->metaObject();
}

//  QString QAbstractProxyModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAbstractProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractProxyModel::tr(s, c, n));
}

//  QAbstractProxyModel::~QAbstractProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractProxyModelD1Ev(QAbstractProxyModel *self) {
  delete self;
}

//  void QAbstractProxyModel::setSourceModel(QAbstractItemModel *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractProxyModel14setSourceModelEP18QAbstractItemModel(
    QAbstractProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->setSourceModel(sourceModel);
}

//  QAbstractItemModel *QAbstractProxyModel::sourceModel() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK19QAbstractProxyModel11sourceModelEv(
    const QAbstractProxyModel *self) {
  return self->sourceModel();
}

//  QModelIndex QAbstractProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractProxyModel11mapToSourceERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QModelIndex QAbstractProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractProxyModel13mapFromSourceERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QItemSelection QAbstractProxyModel::mapSelectionToSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK19QAbstractProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QAbstractProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(self->mapSelectionToSource(*selection));
}

//  QItemSelection QAbstractProxyModel::mapSelectionFromSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK19QAbstractProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QAbstractProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(self->mapSelectionFromSource(*selection));
}

//  bool QAbstractProxyModel::submit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel6submitEv(QAbstractProxyModel *self) {
  return self->submit();
}

//  void QAbstractProxyModel::revert()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractProxyModel6revertEv(QAbstractProxyModel *self) {
  self->revert();
}

//  QVariant QAbstractProxyModel::data(const QModelIndex &proxyIndex, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QAbstractProxyModel4dataERK11QModelIndexi(
    const QAbstractProxyModel *self,
    const QModelIndex *proxyIndex,
    int role) {
  return new QVariant(self->data(*proxyIndex, role));
}

//  QVariant QAbstractProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QAbstractProxyModel10headerDataEiN2Qt11OrientationEi(
    const QAbstractProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  QMap<int, QVariant> QAbstractProxyModel::itemData(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK19QAbstractProxyModel8itemDataERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *index) {
  return new QMap<int, QVariant>(self->itemData(*index));
}

//  Qt::ItemFlags QAbstractProxyModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractProxyModel5flagsERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  bool QAbstractProxyModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QAbstractProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  bool QAbstractProxyModel::setItemData(const QModelIndex &index, const
//      QMap<int, QVariant> &roles)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel11setItemDataERK11QModelIndexRK4QMapIi8QVariantE(
    QAbstractProxyModel *self,
    const QModelIndex *index,
    const QMap<int, QVariant> *roles) {
  return self->setItemData(*index, *roles);
}

//  bool QAbstractProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QAbstractProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  bool QAbstractProxyModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel13clearItemDataERK11QModelIndex(
    QAbstractProxyModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  QModelIndex QAbstractProxyModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractProxyModel5buddyERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->buddy(*index));
}

//  bool QAbstractProxyModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractProxyModel12canFetchMoreERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  void QAbstractProxyModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractProxyModel9fetchMoreERK11QModelIndex(
    QAbstractProxyModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  void QAbstractProxyModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractProxyModel4sortEiN2Qt9SortOrderE(
    QAbstractProxyModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QSize QAbstractProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QAbstractProxyModel4spanERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  bool QAbstractProxyModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractProxyModel11hasChildrenERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QModelIndex QAbstractProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractProxyModel7siblingEiiRK11QModelIndex(
    const QAbstractProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  QMimeData *QAbstractProxyModel::mimeData(const QModelIndexList &indexes)
//      const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK19QAbstractProxyModel8mimeDataERK5QListI11QModelIndexE(
    const QAbstractProxyModel *self,
    const QList<QModelIndex> *indexes) {
  return self->mimeData(*indexes);
}

//  bool QAbstractProxyModel::canDropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractProxyModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QAbstractProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->canDropMimeData(data, action, row, column, *parent);
}

//  bool QAbstractProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  QStringList QAbstractProxyModel::mimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QAbstractProxyModel9mimeTypesEv(
    const QAbstractProxyModel *self) {
  return new QList<QString>(self->mimeTypes());
}

//  Qt::DropActions QAbstractProxyModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractProxyModel20supportedDragActionsEv(
    const QAbstractProxyModel *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  Qt::DropActions QAbstractProxyModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractProxyModel20supportedDropActionsEv(
    const QAbstractProxyModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  QHash<int, QByteArray> QAbstractProxyModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK19QAbstractProxyModel9roleNamesEv(
    const QAbstractProxyModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  a Python function taken by a CuteQAbstractProxyModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractProxyModel(
    QAbstractProxyModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractProxyModel *>(self)->take(key, call);
}

//  void QAbstractProxyModel::setSourceModel(QAbstractItemModel *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractProxyModel14setSourceModelEP18QAbstractItemModel(
    QAbstractProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->QAbstractProxyModel::setSourceModel(sourceModel);
}

//  QItemSelection QAbstractProxyModel::mapSelectionToSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_own_ZNK19QAbstractProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QAbstractProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(
      self->QAbstractProxyModel::mapSelectionToSource(
          *selection));
}

//  QItemSelection QAbstractProxyModel::mapSelectionFromSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_own_ZNK19QAbstractProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QAbstractProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(
      self->QAbstractProxyModel::mapSelectionFromSource(
          *selection));
}

//  bool QAbstractProxyModel::submit()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractProxyModel6submitEv(QAbstractProxyModel *self) {
  return self->QAbstractProxyModel::submit();
}

//  void QAbstractProxyModel::revert()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractProxyModel6revertEv(QAbstractProxyModel *self) {
  self->QAbstractProxyModel::revert();
}

//  QVariant QAbstractProxyModel::data(const QModelIndex &proxyIndex, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK19QAbstractProxyModel4dataERK11QModelIndexi(
    const QAbstractProxyModel *self,
    const QModelIndex *proxyIndex,
    int role) {
  return new QVariant(self->QAbstractProxyModel::data(*proxyIndex, role));
}

//  QVariant QAbstractProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK19QAbstractProxyModel10headerDataEiN2Qt11OrientationEi(
    const QAbstractProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QAbstractProxyModel::headerData(
          section,
          orientation,
          role));
}

//  Qt::ItemFlags QAbstractProxyModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAbstractProxyModel5flagsERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QAbstractProxyModel::flags(*index).toInt());
}

//  bool QAbstractProxyModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QAbstractProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QAbstractProxyModel::setData(*index, *value, role);
}

//  bool QAbstractProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QAbstractProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->QAbstractProxyModel::setHeaderData(
      section,
      orientation,
      *value,
      role);
}

//  bool QAbstractProxyModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractProxyModel13clearItemDataERK11QModelIndex(
    QAbstractProxyModel *self,
    const QModelIndex *index) {
  return self->QAbstractProxyModel::clearItemData(*index);
}

//  QModelIndex QAbstractProxyModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QAbstractProxyModel5buddyERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->QAbstractProxyModel::buddy(*index));
}

//  bool QAbstractProxyModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QAbstractProxyModel12canFetchMoreERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *parent) {
  return self->QAbstractProxyModel::canFetchMore(*parent);
}

//  void QAbstractProxyModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractProxyModel9fetchMoreERK11QModelIndex(
    QAbstractProxyModel *self,
    const QModelIndex *parent) {
  self->QAbstractProxyModel::fetchMore(*parent);
}

//  void QAbstractProxyModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractProxyModel4sortEiN2Qt9SortOrderE(
    QAbstractProxyModel *self,
    int column,
    Qt::SortOrder order) {
  self->QAbstractProxyModel::sort(column, order);
}

//  QSize QAbstractProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK19QAbstractProxyModel4spanERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->QAbstractProxyModel::span(*index));
}

//  bool QAbstractProxyModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QAbstractProxyModel11hasChildrenERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *parent) {
  return self->QAbstractProxyModel::hasChildren(*parent);
}

//  QModelIndex QAbstractProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QAbstractProxyModel7siblingEiiRK11QModelIndex(
    const QAbstractProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(
      self->QAbstractProxyModel::sibling(
          row,
          column,
          *idx));
}

//  bool QAbstractProxyModel::canDropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QAbstractProxyModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QAbstractProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QAbstractProxyModel::canDropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  bool QAbstractProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QAbstractProxyModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  Qt::DropActions QAbstractProxyModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAbstractProxyModel20supportedDragActionsEv(
    const QAbstractProxyModel *self) {
  return static_cast<int>(
      self->QAbstractProxyModel::supportedDragActions().toInt());
}

//  Qt::DropActions QAbstractProxyModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAbstractProxyModel20supportedDropActionsEv(
    const QAbstractProxyModel *self) {
  return static_cast<int>(
      self->QAbstractProxyModel::supportedDropActions().toInt());
}
