//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qidentityproxymodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qidentityproxymodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QIdentityProxyModel that Python can take functions over in. Every QIdentityProxyModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQIdentityProxyModelCall0)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQIdentityProxyModelCall1)(const void *, int, int, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQIdentityProxyModelCall2)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQIdentityProxyModelCall3)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQIdentityProxyModelCall4)(const void *, const QModelIndex *, int *);
typedef int (*CuteQIdentityProxyModelCall5)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQIdentityProxyModelCall6)(const void *, int, int, int, int *);
typedef bool (*CuteQIdentityProxyModelCall7)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQIdentityProxyModelCall8)(const void *, int, int, const QModelIndex *, int *);
typedef const QItemSelection * (*CuteQIdentityProxyModelCall9)(const void *, const QItemSelection *, int *);
typedef const QItemSelection * (*CuteQIdentityProxyModelCall10)(const void *, const QItemSelection *, int *);
typedef void (*CuteQIdentityProxyModelCall11)(const void *, QAbstractItemModel *, int *);
typedef bool (*CuteQIdentityProxyModelCall12)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQIdentityProxyModelCall13)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQIdentityProxyModelCall14)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQIdentityProxyModelCall15)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQIdentityProxyModelCall16)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef bool (*CuteQIdentityProxyModelCall17)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef bool (*CuteQIdentityProxyModelCall18)(const void *, int *);
typedef void (*CuteQIdentityProxyModelCall19)(const void *, int *);
typedef const QVariant * (*CuteQIdentityProxyModelCall20)(const void *, const QModelIndex *, int, int *);
typedef bool (*CuteQIdentityProxyModelCall21)(const void *, const QModelIndex *, const QVariant *, int, int *);
typedef bool (*CuteQIdentityProxyModelCall22)(const void *, int, int, const QVariant *, int, int *);
typedef bool (*CuteQIdentityProxyModelCall23)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQIdentityProxyModelCall24)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQIdentityProxyModelCall25)(const void *, const QModelIndex *, int *);
typedef void (*CuteQIdentityProxyModelCall26)(const void *, const QModelIndex *, int *);
typedef void (*CuteQIdentityProxyModelCall27)(const void *, int, int, int *);
typedef const QSize * (*CuteQIdentityProxyModelCall28)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQIdentityProxyModelCall29)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQIdentityProxyModelCall30)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef void (*CuteQIdentityProxyModelCall31)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
typedef void (*CuteQIdentityProxyModelCall32)(const void *, int *);
typedef bool (*CuteQIdentityProxyModelCall33)(const void *, QEvent *, int *);
typedef bool (*CuteQIdentityProxyModelCall34)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQIdentityProxyModelCall35)(const void *, QTimerEvent *, int *);
typedef void (*CuteQIdentityProxyModelCall36)(const void *, QChildEvent *, int *);
typedef void (*CuteQIdentityProxyModelCall37)(const void *, QEvent *, int *);
typedef void (*CuteQIdentityProxyModelCall38)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQIdentityProxyModelCall39)(const void *, const QMetaMethod *, int *);
class CuteQIdentityProxyModel : public QIdentityProxyModel {
public:
  using QIdentityProxyModel::QIdentityProxyModel;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel13mapFromSourceERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel11mapToSourceERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel22mapSelectionFromSourceERK14QItemSelection")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel20mapSelectionToSourceERK14QItemSelection")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractProxyModel14setSourceModelEP18QAbstractItemModel")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
    return false;
  }

  //  int QIdentityProxyModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQIdentityProxyModelCall0 call = reinterpret_cast<CuteQIdentityProxyModelCall0>(taken[0]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QIdentityProxyModel::columnCount(parent);
  }

  //  QModelIndex QIdentityProxyModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQIdentityProxyModelCall1 call = reinterpret_cast<CuteQIdentityProxyModelCall1>(taken[1]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QIdentityProxyModel::index(row, column, parent);
  }

  //  QModelIndex QIdentityProxyModel::mapFromSource(const QModelIndex
  //      &sourceIndex) const
  QModelIndex mapFromSource(const QModelIndex &sourceIndex) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQIdentityProxyModelCall2 call = reinterpret_cast<CuteQIdentityProxyModelCall2>(taken[2]);
      const QModelIndex * given = call(this, &sourceIndex, &handled);
      if (handled && given) return *given;
    }
    return QIdentityProxyModel::mapFromSource(sourceIndex);
  }

  //  QModelIndex QIdentityProxyModel::mapToSource(const QModelIndex
  //      &proxyIndex) const
  QModelIndex mapToSource(const QModelIndex &proxyIndex) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQIdentityProxyModelCall3 call = reinterpret_cast<CuteQIdentityProxyModelCall3>(taken[3]);
      const QModelIndex * given = call(this, &proxyIndex, &handled);
      if (handled && given) return *given;
    }
    return QIdentityProxyModel::mapToSource(proxyIndex);
  }

  //  QModelIndex QIdentityProxyModel::parent(const QModelIndex &child)
  //      const
  QModelIndex parent(const QModelIndex &child) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQIdentityProxyModelCall4 call = reinterpret_cast<CuteQIdentityProxyModelCall4>(taken[4]);
      const QModelIndex * given = call(this, &child, &handled);
      if (handled && given) return *given;
    }
    return QIdentityProxyModel::parent(child);
  }

  //  int QIdentityProxyModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQIdentityProxyModelCall5 call = reinterpret_cast<CuteQIdentityProxyModelCall5>(taken[5]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QIdentityProxyModel::rowCount(parent);
  }

  //  QVariant QIdentityProxyModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQIdentityProxyModelCall6 call = reinterpret_cast<CuteQIdentityProxyModelCall6>(taken[6]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QIdentityProxyModel::headerData(section, orientation, role);
  }

  //  bool QIdentityProxyModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[7]) {
      int handled = 0;
      CuteQIdentityProxyModelCall7 call = reinterpret_cast<CuteQIdentityProxyModelCall7>(taken[7]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QIdentityProxyModel::dropMimeData(data, action, row, column, parent);
  }

  //  QModelIndex QIdentityProxyModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQIdentityProxyModelCall8 call = reinterpret_cast<CuteQIdentityProxyModelCall8>(taken[8]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QIdentityProxyModel::sibling(row, column, idx);
  }

  //  QItemSelection QIdentityProxyModel::mapSelectionFromSource(const
  //      QItemSelection &selection) const
  QItemSelection mapSelectionFromSource(
      const QItemSelection &selection) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQIdentityProxyModelCall9 call = reinterpret_cast<CuteQIdentityProxyModelCall9>(taken[9]);
      const QItemSelection * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QIdentityProxyModel::mapSelectionFromSource(selection);
  }

  //  QItemSelection QIdentityProxyModel::mapSelectionToSource(const
  //      QItemSelection &selection) const
  QItemSelection mapSelectionToSource(
      const QItemSelection &selection) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQIdentityProxyModelCall10 call = reinterpret_cast<CuteQIdentityProxyModelCall10>(taken[10]);
      const QItemSelection * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QIdentityProxyModel::mapSelectionToSource(selection);
  }

  //  void QIdentityProxyModel::setSourceModel(QAbstractItemModel
  //      *sourceModel)
  void setSourceModel(QAbstractItemModel *sourceModel) override {
    if (taken[11]) {
      int handled = 0;
      CuteQIdentityProxyModelCall11 call = reinterpret_cast<CuteQIdentityProxyModelCall11>(taken[11]);
      call(this, sourceModel, &handled);
      if (handled) return;
    }
    QIdentityProxyModel::setSourceModel(sourceModel);
  }

  //  bool QIdentityProxyModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[12]) {
      int handled = 0;
      CuteQIdentityProxyModelCall12 call = reinterpret_cast<CuteQIdentityProxyModelCall12>(taken[12]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QIdentityProxyModel::insertColumns(column, count, parent);
  }

  //  bool QIdentityProxyModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[13]) {
      int handled = 0;
      CuteQIdentityProxyModelCall13 call = reinterpret_cast<CuteQIdentityProxyModelCall13>(taken[13]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QIdentityProxyModel::insertRows(row, count, parent);
  }

  //  bool QIdentityProxyModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[14]) {
      int handled = 0;
      CuteQIdentityProxyModelCall14 call = reinterpret_cast<CuteQIdentityProxyModelCall14>(taken[14]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QIdentityProxyModel::removeColumns(column, count, parent);
  }

  //  bool QIdentityProxyModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[15]) {
      int handled = 0;
      CuteQIdentityProxyModelCall15 call = reinterpret_cast<CuteQIdentityProxyModelCall15>(taken[15]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QIdentityProxyModel::removeRows(row, count, parent);
  }

  //  bool QIdentityProxyModel::moveRows(const QModelIndex &sourceParent,
  //      int sourceRow, int count, const QModelIndex &destinationParent,
  //      int destinationChild)
  bool moveRows(
      const QModelIndex &sourceParent,
      int sourceRow,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[16]) {
      int handled = 0;
      CuteQIdentityProxyModelCall16 call = reinterpret_cast<CuteQIdentityProxyModelCall16>(taken[16]);
      bool given = call(this, &sourceParent, sourceRow, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QIdentityProxyModel::moveRows(sourceParent, sourceRow, count, destinationParent, destinationChild);
  }

  //  bool QIdentityProxyModel::moveColumns(const QModelIndex
  //      &sourceParent, int sourceColumn, int count, const QModelIndex
  //      &destinationParent, int destinationChild)
  bool moveColumns(
      const QModelIndex &sourceParent,
      int sourceColumn,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[17]) {
      int handled = 0;
      CuteQIdentityProxyModelCall17 call = reinterpret_cast<CuteQIdentityProxyModelCall17>(taken[17]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QIdentityProxyModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }

  //  bool QAbstractProxyModel::submit()
  bool submit() override {
    if (taken[18]) {
      int handled = 0;
      CuteQIdentityProxyModelCall18 call = reinterpret_cast<CuteQIdentityProxyModelCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::submit();
  }

  //  void QAbstractProxyModel::revert()
  void revert() override {
    if (taken[19]) {
      int handled = 0;
      CuteQIdentityProxyModelCall19 call = reinterpret_cast<CuteQIdentityProxyModelCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::revert();
  }

  //  QVariant QAbstractProxyModel::data(const QModelIndex &proxyIndex, int
  //      role) const
  QVariant data(const QModelIndex &proxyIndex, int role) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQIdentityProxyModelCall20 call = reinterpret_cast<CuteQIdentityProxyModelCall20>(taken[20]);
      const QVariant * given = call(this, &proxyIndex, role, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::data(proxyIndex, role);
  }

  //  bool QAbstractProxyModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[21]) {
      int handled = 0;
      CuteQIdentityProxyModelCall21 call = reinterpret_cast<CuteQIdentityProxyModelCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQIdentityProxyModelCall22 call = reinterpret_cast<CuteQIdentityProxyModelCall22>(taken[22]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::setHeaderData(section, orientation, value, role);
  }

  //  bool QAbstractProxyModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[23]) {
      int handled = 0;
      CuteQIdentityProxyModelCall23 call = reinterpret_cast<CuteQIdentityProxyModelCall23>(taken[23]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::clearItemData(index);
  }

  //  QModelIndex QAbstractProxyModel::buddy(const QModelIndex &index)
  //      const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQIdentityProxyModelCall24 call = reinterpret_cast<CuteQIdentityProxyModelCall24>(taken[24]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::buddy(index);
  }

  //  bool QAbstractProxyModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQIdentityProxyModelCall25 call = reinterpret_cast<CuteQIdentityProxyModelCall25>(taken[25]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::canFetchMore(parent);
  }

  //  void QAbstractProxyModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[26]) {
      int handled = 0;
      CuteQIdentityProxyModelCall26 call = reinterpret_cast<CuteQIdentityProxyModelCall26>(taken[26]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::fetchMore(parent);
  }

  //  void QAbstractProxyModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[27]) {
      int handled = 0;
      CuteQIdentityProxyModelCall27 call = reinterpret_cast<CuteQIdentityProxyModelCall27>(taken[27]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractProxyModel::sort(column, order);
  }

  //  QSize QAbstractProxyModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQIdentityProxyModelCall28 call = reinterpret_cast<CuteQIdentityProxyModelCall28>(taken[28]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::span(index);
  }

  //  bool QAbstractProxyModel::hasChildren(const QModelIndex &parent)
  //      const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQIdentityProxyModelCall29 call = reinterpret_cast<CuteQIdentityProxyModelCall29>(taken[29]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::hasChildren(parent);
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
    if (taken[30]) {
      int handled = 0;
      CuteQIdentityProxyModelCall30 call = reinterpret_cast<CuteQIdentityProxyModelCall30>(taken[30]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::canDropMimeData(data, action, row, column, parent);
  }

  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQIdentityProxyModelCall31 call = reinterpret_cast<CuteQIdentityProxyModelCall31>(taken[31]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }

  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[32]) {
      int handled = 0;
      CuteQIdentityProxyModelCall32 call = reinterpret_cast<CuteQIdentityProxyModelCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteQIdentityProxyModelCall33 call = reinterpret_cast<CuteQIdentityProxyModelCall33>(taken[33]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteQIdentityProxyModelCall34 call = reinterpret_cast<CuteQIdentityProxyModelCall34>(taken[34]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQIdentityProxyModelCall35 call = reinterpret_cast<CuteQIdentityProxyModelCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQIdentityProxyModelCall36 call = reinterpret_cast<CuteQIdentityProxyModelCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQIdentityProxyModelCall37 call = reinterpret_cast<CuteQIdentityProxyModelCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[38]) {
      int handled = 0;
      CuteQIdentityProxyModelCall38 call = reinterpret_cast<CuteQIdentityProxyModelCall38>(taken[38]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteQIdentityProxyModelCall39 call = reinterpret_cast<CuteQIdentityProxyModelCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QIdentityProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QIdentityProxyModel10metaObjectEv(
    const QIdentityProxyModel *self) {
  return self->metaObject();
}

//  QString QIdentityProxyModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QIdentityProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIdentityProxyModel::tr(s, c, n));
}

//  QIdentityProxyModel::QIdentityProxyModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QIdentityProxyModel *ritual_ZN19QIdentityProxyModelC1EP7QObject(
    QObject *parent) {
  return new CuteQIdentityProxyModel(parent);
}

//  QIdentityProxyModel::~QIdentityProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIdentityProxyModelD1Ev(QIdentityProxyModel *self) {
  delete self;
}

//  int QIdentityProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QIdentityProxyModel11columnCountERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QModelIndex QIdentityProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QIdentityProxyModel5indexEiiRK11QModelIndex(
    const QIdentityProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QIdentityProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QIdentityProxyModel13mapFromSourceERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QModelIndex QIdentityProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QIdentityProxyModel11mapToSourceERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QModelIndex QIdentityProxyModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QIdentityProxyModel6parentERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  int QIdentityProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QIdentityProxyModel8rowCountERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QIdentityProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QIdentityProxyModel10headerDataEiN2Qt11OrientationEi(
    const QIdentityProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QIdentityProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  QModelIndex QIdentityProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QIdentityProxyModel7siblingEiiRK11QModelIndex(
    const QIdentityProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  QItemSelection QIdentityProxyModel::mapSelectionFromSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK19QIdentityProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QIdentityProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(self->mapSelectionFromSource(*selection));
}

//  QItemSelection QIdentityProxyModel::mapSelectionToSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK19QIdentityProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QIdentityProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(self->mapSelectionToSource(*selection));
}

//  void QIdentityProxyModel::setSourceModel(QAbstractItemModel *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIdentityProxyModel14setSourceModelEP18QAbstractItemModel(
    QIdentityProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->setSourceModel(sourceModel);
}

//  bool QIdentityProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel13insertColumnsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QIdentityProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel10insertRowsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QIdentityProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel13removeColumnsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  bool QIdentityProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel10removeRowsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QIdentityProxyModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel8moveRowsERK11QModelIndexiiS2_i(
    QIdentityProxyModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destinationParent,
      destinationChild);
}

//  bool QIdentityProxyModel::moveColumns(const QModelIndex &sourceParent,
//      int sourceColumn, int count, const QModelIndex &destinationParent,
//      int destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel11moveColumnsERK11QModelIndexiiS2_i(
    QIdentityProxyModel *self,
    const QModelIndex *sourceParent,
    int sourceColumn,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveColumns(
      *sourceParent,
      sourceColumn,
      count,
      *destinationParent,
      destinationChild);
}

//  bool QIdentityProxyModel::handleSourceLayoutChanges() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QIdentityProxyModel25handleSourceLayoutChangesEv(
    const QIdentityProxyModel *self) {
  return self->handleSourceLayoutChanges();
}

//  bool QIdentityProxyModel::handleSourceDataChanges() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QIdentityProxyModel23handleSourceDataChangesEv(
    const QIdentityProxyModel *self) {
  return self->handleSourceDataChanges();
}

//  a Python function taken by a CuteQIdentityProxyModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIdentityProxyModel(
    QIdentityProxyModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIdentityProxyModel *>(self)->take(key, call);
}

//  int QIdentityProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QIdentityProxyModel11columnCountERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *parent) {
  return self->QIdentityProxyModel::columnCount(*parent);
}

//  QModelIndex QIdentityProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QIdentityProxyModel5indexEiiRK11QModelIndex(
    const QIdentityProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QIdentityProxyModel::index(
          row,
          column,
          *parent));
}

//  QModelIndex QIdentityProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QIdentityProxyModel13mapFromSourceERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(
      self->QIdentityProxyModel::mapFromSource(
          *sourceIndex));
}

//  QModelIndex QIdentityProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QIdentityProxyModel11mapToSourceERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(
      self->QIdentityProxyModel::mapToSource(
          *proxyIndex));
}

//  QModelIndex QIdentityProxyModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QIdentityProxyModel6parentERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->QIdentityProxyModel::parent(*child));
}

//  int QIdentityProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QIdentityProxyModel8rowCountERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *parent) {
  return self->QIdentityProxyModel::rowCount(*parent);
}

//  QVariant QIdentityProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK19QIdentityProxyModel10headerDataEiN2Qt11OrientationEi(
    const QIdentityProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QIdentityProxyModel::headerData(
          section,
          orientation,
          role));
}

//  bool QIdentityProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QIdentityProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QIdentityProxyModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  QModelIndex QIdentityProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QIdentityProxyModel7siblingEiiRK11QModelIndex(
    const QIdentityProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(
      self->QIdentityProxyModel::sibling(
          row,
          column,
          *idx));
}

//  QItemSelection QIdentityProxyModel::mapSelectionFromSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_own_ZNK19QIdentityProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QIdentityProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(
      self->QIdentityProxyModel::mapSelectionFromSource(
          *selection));
}

//  QItemSelection QIdentityProxyModel::mapSelectionToSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_own_ZNK19QIdentityProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QIdentityProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(
      self->QIdentityProxyModel::mapSelectionToSource(
          *selection));
}

//  void QIdentityProxyModel::setSourceModel(QAbstractItemModel *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QIdentityProxyModel14setSourceModelEP18QAbstractItemModel(
    QIdentityProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->QIdentityProxyModel::setSourceModel(sourceModel);
}

//  bool QIdentityProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QIdentityProxyModel13insertColumnsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QIdentityProxyModel::insertColumns(column, count, *parent);
}

//  bool QIdentityProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QIdentityProxyModel10insertRowsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QIdentityProxyModel::insertRows(row, count, *parent);
}

//  bool QIdentityProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QIdentityProxyModel13removeColumnsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QIdentityProxyModel::removeColumns(column, count, *parent);
}

//  bool QIdentityProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QIdentityProxyModel10removeRowsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QIdentityProxyModel::removeRows(row, count, *parent);
}

//  bool QIdentityProxyModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QIdentityProxyModel8moveRowsERK11QModelIndexiiS2_i(
    QIdentityProxyModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->QIdentityProxyModel::moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destinationParent,
      destinationChild);
}

//  bool QIdentityProxyModel::moveColumns(const QModelIndex &sourceParent,
//      int sourceColumn, int count, const QModelIndex &destinationParent,
//      int destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QIdentityProxyModel11moveColumnsERK11QModelIndexiiS2_i(
    QIdentityProxyModel *self,
    const QModelIndex *sourceParent,
    int sourceColumn,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->QIdentityProxyModel::moveColumns(
      *sourceParent,
      sourceColumn,
      count,
      *destinationParent,
      destinationChild);
}
