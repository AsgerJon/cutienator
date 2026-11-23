//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtransposeproxymodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtransposeproxymodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QTransposeProxyModel that Python can take functions over in. Every QTransposeProxyModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTransposeProxyModelCall0)(const void *, QAbstractItemModel *, int *);
typedef int (*CuteQTransposeProxyModelCall1)(const void *, const QModelIndex *, int *);
typedef int (*CuteQTransposeProxyModelCall2)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQTransposeProxyModelCall3)(const void *, int, int, int, int *);
typedef bool (*CuteQTransposeProxyModelCall4)(const void *, int, int, const QVariant *, int, int *);
typedef const QSize * (*CuteQTransposeProxyModelCall5)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQTransposeProxyModelCall6)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQTransposeProxyModelCall7)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQTransposeProxyModelCall8)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQTransposeProxyModelCall9)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQTransposeProxyModelCall10)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQTransposeProxyModelCall11)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQTransposeProxyModelCall12)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef bool (*CuteQTransposeProxyModelCall13)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQTransposeProxyModelCall14)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQTransposeProxyModelCall15)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteQTransposeProxyModelCall16)(const void *, int, int, int *);
typedef const QItemSelection * (*CuteQTransposeProxyModelCall17)(const void *, const QItemSelection *, int *);
typedef const QItemSelection * (*CuteQTransposeProxyModelCall18)(const void *, const QItemSelection *, int *);
typedef bool (*CuteQTransposeProxyModelCall19)(const void *, int *);
typedef void (*CuteQTransposeProxyModelCall20)(const void *, int *);
typedef const QVariant * (*CuteQTransposeProxyModelCall21)(const void *, const QModelIndex *, int, int *);
typedef int (*CuteQTransposeProxyModelCall22)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQTransposeProxyModelCall23)(const void *, const QModelIndex *, const QVariant *, int, int *);
typedef bool (*CuteQTransposeProxyModelCall24)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQTransposeProxyModelCall25)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQTransposeProxyModelCall26)(const void *, const QModelIndex *, int *);
typedef void (*CuteQTransposeProxyModelCall27)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQTransposeProxyModelCall28)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQTransposeProxyModelCall29)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQTransposeProxyModelCall30)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef bool (*CuteQTransposeProxyModelCall31)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef int (*CuteQTransposeProxyModelCall32)(const void *, int *);
typedef int (*CuteQTransposeProxyModelCall33)(const void *, int *);
typedef void (*CuteQTransposeProxyModelCall34)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
typedef void (*CuteQTransposeProxyModelCall35)(const void *, int *);
typedef bool (*CuteQTransposeProxyModelCall36)(const void *, QEvent *, int *);
typedef bool (*CuteQTransposeProxyModelCall37)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQTransposeProxyModelCall38)(const void *, QTimerEvent *, int *);
typedef void (*CuteQTransposeProxyModelCall39)(const void *, QChildEvent *, int *);
typedef void (*CuteQTransposeProxyModelCall40)(const void *, QEvent *, int *);
typedef void (*CuteQTransposeProxyModelCall41)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTransposeProxyModelCall42)(const void *, const QMetaMethod *, int *);
class CuteQTransposeProxyModel : public QTransposeProxyModel {
public:
  using QTransposeProxyModel::QTransposeProxyModel;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QAbstractProxyModel14setSourceModelEP18QAbstractItemModel")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel13mapFromSourceERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel11mapToSourceERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel6parentERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel20mapSelectionToSourceERK14QItemSelection")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractProxyModel22mapSelectionFromSourceERK14QItemSelection")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
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

  //  void QTransposeProxyModel::setSourceModel(QAbstractItemModel
  //      *newSourceModel)
  void setSourceModel(QAbstractItemModel *newSourceModel) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTransposeProxyModelCall0 call = reinterpret_cast<CuteQTransposeProxyModelCall0>(taken[0]);
      call(this, newSourceModel, &handled);
      if (handled) return;
    }
    QTransposeProxyModel::setSourceModel(newSourceModel);
  }

  //  int QTransposeProxyModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTransposeProxyModelCall1 call = reinterpret_cast<CuteQTransposeProxyModelCall1>(taken[1]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QTransposeProxyModel::rowCount(parent);
  }

  //  int QTransposeProxyModel::columnCount(const QModelIndex &parent)
  //      const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTransposeProxyModelCall2 call = reinterpret_cast<CuteQTransposeProxyModelCall2>(taken[2]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QTransposeProxyModel::columnCount(parent);
  }

  //  QVariant QTransposeProxyModel::headerData(int section,
  //      Qt::Orientation orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTransposeProxyModelCall3 call = reinterpret_cast<CuteQTransposeProxyModelCall3>(taken[3]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QTransposeProxyModel::headerData(section, orientation, role);
  }

  //  bool QTransposeProxyModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTransposeProxyModelCall4 call = reinterpret_cast<CuteQTransposeProxyModelCall4>(taken[4]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QTransposeProxyModel::setHeaderData(section, orientation, value, role);
  }

  //  QSize QTransposeProxyModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTransposeProxyModelCall5 call = reinterpret_cast<CuteQTransposeProxyModelCall5>(taken[5]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QTransposeProxyModel::span(index);
  }

  //  QModelIndex QTransposeProxyModel::mapFromSource(const QModelIndex
  //      &sourceIndex) const
  QModelIndex mapFromSource(const QModelIndex &sourceIndex) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTransposeProxyModelCall6 call = reinterpret_cast<CuteQTransposeProxyModelCall6>(taken[6]);
      const QModelIndex * given = call(this, &sourceIndex, &handled);
      if (handled && given) return *given;
    }
    return QTransposeProxyModel::mapFromSource(sourceIndex);
  }

  //  QModelIndex QTransposeProxyModel::mapToSource(const QModelIndex
  //      &proxyIndex) const
  QModelIndex mapToSource(const QModelIndex &proxyIndex) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTransposeProxyModelCall7 call = reinterpret_cast<CuteQTransposeProxyModelCall7>(taken[7]);
      const QModelIndex * given = call(this, &proxyIndex, &handled);
      if (handled && given) return *given;
    }
    return QTransposeProxyModel::mapToSource(proxyIndex);
  }

  //  QModelIndex QTransposeProxyModel::parent(const QModelIndex &index)
  //      const
  QModelIndex parent(const QModelIndex &index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTransposeProxyModelCall8 call = reinterpret_cast<CuteQTransposeProxyModelCall8>(taken[8]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QTransposeProxyModel::parent(index);
  }

  //  QModelIndex QTransposeProxyModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQTransposeProxyModelCall9 call = reinterpret_cast<CuteQTransposeProxyModelCall9>(taken[9]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QTransposeProxyModel::index(row, column, parent);
  }

  //  bool QTransposeProxyModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[10]) {
      int handled = 0;
      CuteQTransposeProxyModelCall10 call = reinterpret_cast<CuteQTransposeProxyModelCall10>(taken[10]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QTransposeProxyModel::insertRows(row, count, parent);
  }

  //  bool QTransposeProxyModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTransposeProxyModelCall11 call = reinterpret_cast<CuteQTransposeProxyModelCall11>(taken[11]);
      bool given = call(this, row, count, &parent, &handled);
      if (handled) return given;
    }
    return QTransposeProxyModel::removeRows(row, count, parent);
  }

  //  bool QTransposeProxyModel::moveRows(const QModelIndex &sourceParent,
  //      int sourceRow, int count, const QModelIndex &destinationParent,
  //      int destinationChild)
  bool moveRows(
      const QModelIndex &sourceParent,
      int sourceRow,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTransposeProxyModelCall12 call = reinterpret_cast<CuteQTransposeProxyModelCall12>(taken[12]);
      bool given = call(this, &sourceParent, sourceRow, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QTransposeProxyModel::moveRows(sourceParent, sourceRow, count, destinationParent, destinationChild);
  }

  //  bool QTransposeProxyModel::insertColumns(int column, int count, const
  //      QModelIndex &parent)
  bool insertColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTransposeProxyModelCall13 call = reinterpret_cast<CuteQTransposeProxyModelCall13>(taken[13]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QTransposeProxyModel::insertColumns(column, count, parent);
  }

  //  bool QTransposeProxyModel::removeColumns(int column, int count, const
  //      QModelIndex &parent)
  bool removeColumns(
      int column,
      int count,
      const QModelIndex &parent) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTransposeProxyModelCall14 call = reinterpret_cast<CuteQTransposeProxyModelCall14>(taken[14]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QTransposeProxyModel::removeColumns(column, count, parent);
  }

  //  bool QTransposeProxyModel::moveColumns(const QModelIndex
  //      &sourceParent, int sourceColumn, int count, const QModelIndex
  //      &destinationParent, int destinationChild)
  bool moveColumns(
      const QModelIndex &sourceParent,
      int sourceColumn,
      int count,
      const QModelIndex &destinationParent,
      int destinationChild) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTransposeProxyModelCall15 call = reinterpret_cast<CuteQTransposeProxyModelCall15>(taken[15]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QTransposeProxyModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }

  //  void QTransposeProxyModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[16]) {
      int handled = 0;
      CuteQTransposeProxyModelCall16 call = reinterpret_cast<CuteQTransposeProxyModelCall16>(taken[16]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QTransposeProxyModel::sort(column, order);
  }

  //  QItemSelection QAbstractProxyModel::mapSelectionToSource(const
  //      QItemSelection &selection) const
  QItemSelection mapSelectionToSource(
      const QItemSelection &selection) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQTransposeProxyModelCall17 call = reinterpret_cast<CuteQTransposeProxyModelCall17>(taken[17]);
      const QItemSelection * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::mapSelectionToSource(selection);
  }

  //  QItemSelection QAbstractProxyModel::mapSelectionFromSource(const
  //      QItemSelection &selection) const
  QItemSelection mapSelectionFromSource(
      const QItemSelection &selection) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQTransposeProxyModelCall18 call = reinterpret_cast<CuteQTransposeProxyModelCall18>(taken[18]);
      const QItemSelection * given = call(this, &selection, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::mapSelectionFromSource(selection);
  }

  //  bool QAbstractProxyModel::submit()
  bool submit() override {
    if (taken[19]) {
      int handled = 0;
      CuteQTransposeProxyModelCall19 call = reinterpret_cast<CuteQTransposeProxyModelCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::submit();
  }

  //  void QAbstractProxyModel::revert()
  void revert() override {
    if (taken[20]) {
      int handled = 0;
      CuteQTransposeProxyModelCall20 call = reinterpret_cast<CuteQTransposeProxyModelCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::revert();
  }

  //  QVariant QAbstractProxyModel::data(const QModelIndex &proxyIndex, int
  //      role) const
  QVariant data(const QModelIndex &proxyIndex, int role) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQTransposeProxyModelCall21 call = reinterpret_cast<CuteQTransposeProxyModelCall21>(taken[21]);
      const QVariant * given = call(this, &proxyIndex, role, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::data(proxyIndex, role);
  }

  //  Qt::ItemFlags QAbstractProxyModel::flags(const QModelIndex &index)
  //      const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQTransposeProxyModelCall22 call = reinterpret_cast<CuteQTransposeProxyModelCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQTransposeProxyModelCall23 call = reinterpret_cast<CuteQTransposeProxyModelCall23>(taken[23]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::setData(index, value, role);
  }

  //  bool QAbstractProxyModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTransposeProxyModelCall24 call = reinterpret_cast<CuteQTransposeProxyModelCall24>(taken[24]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::clearItemData(index);
  }

  //  QModelIndex QAbstractProxyModel::buddy(const QModelIndex &index)
  //      const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQTransposeProxyModelCall25 call = reinterpret_cast<CuteQTransposeProxyModelCall25>(taken[25]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractProxyModel::buddy(index);
  }

  //  bool QAbstractProxyModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQTransposeProxyModelCall26 call = reinterpret_cast<CuteQTransposeProxyModelCall26>(taken[26]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::canFetchMore(parent);
  }

  //  void QAbstractProxyModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTransposeProxyModelCall27 call = reinterpret_cast<CuteQTransposeProxyModelCall27>(taken[27]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractProxyModel::fetchMore(parent);
  }

  //  bool QAbstractProxyModel::hasChildren(const QModelIndex &parent)
  //      const
  bool hasChildren(const QModelIndex &parent) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQTransposeProxyModelCall28 call = reinterpret_cast<CuteQTransposeProxyModelCall28>(taken[28]);
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
    if (taken[29]) {
      int handled = 0;
      CuteQTransposeProxyModelCall29 call = reinterpret_cast<CuteQTransposeProxyModelCall29>(taken[29]);
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
    if (taken[30]) {
      int handled = 0;
      CuteQTransposeProxyModelCall30 call = reinterpret_cast<CuteQTransposeProxyModelCall30>(taken[30]);
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
    if (taken[31]) {
      int handled = 0;
      CuteQTransposeProxyModelCall31 call = reinterpret_cast<CuteQTransposeProxyModelCall31>(taken[31]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractProxyModel::dropMimeData(data, action, row, column, parent);
  }

  //  Qt::DropActions QAbstractProxyModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQTransposeProxyModelCall32 call = reinterpret_cast<CuteQTransposeProxyModelCall32>(taken[32]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractProxyModel::supportedDragActions();
  }

  //  Qt::DropActions QAbstractProxyModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQTransposeProxyModelCall33 call = reinterpret_cast<CuteQTransposeProxyModelCall33>(taken[33]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QAbstractProxyModel::supportedDropActions();
  }

  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[34]) {
      int handled = 0;
      CuteQTransposeProxyModelCall34 call = reinterpret_cast<CuteQTransposeProxyModelCall34>(taken[34]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }

  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[35]) {
      int handled = 0;
      CuteQTransposeProxyModelCall35 call = reinterpret_cast<CuteQTransposeProxyModelCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQTransposeProxyModelCall36 call = reinterpret_cast<CuteQTransposeProxyModelCall36>(taken[36]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQTransposeProxyModelCall37 call = reinterpret_cast<CuteQTransposeProxyModelCall37>(taken[37]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQTransposeProxyModelCall38 call = reinterpret_cast<CuteQTransposeProxyModelCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQTransposeProxyModelCall39 call = reinterpret_cast<CuteQTransposeProxyModelCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQTransposeProxyModelCall40 call = reinterpret_cast<CuteQTransposeProxyModelCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQTransposeProxyModelCall41 call = reinterpret_cast<CuteQTransposeProxyModelCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[42]) {
      int handled = 0;
      CuteQTransposeProxyModelCall42 call = reinterpret_cast<CuteQTransposeProxyModelCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QTransposeProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QTransposeProxyModel10metaObjectEv(
    const QTransposeProxyModel *self) {
  return self->metaObject();
}

//  QString QTransposeProxyModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QTransposeProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTransposeProxyModel::tr(s, c, n));
}

//  QTransposeProxyModel::QTransposeProxyModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QTransposeProxyModel *ritual_ZN20QTransposeProxyModelC1EP7QObject(
    QObject *parent) {
  return new CuteQTransposeProxyModel(parent);
}

//  QTransposeProxyModel::~QTransposeProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTransposeProxyModelD1Ev(QTransposeProxyModel *self) {
  delete self;
}

//  void QTransposeProxyModel::setSourceModel(QAbstractItemModel
//      *newSourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTransposeProxyModel14setSourceModelEP18QAbstractItemModel(
    QTransposeProxyModel *self,
    QAbstractItemModel *newSourceModel) {
  self->setSourceModel(newSourceModel);
}

//  int QTransposeProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTransposeProxyModel8rowCountERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QTransposeProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTransposeProxyModel11columnCountERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QVariant QTransposeProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QTransposeProxyModel10headerDataEiN2Qt11OrientationEi(
    const QTransposeProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QTransposeProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QTransposeProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  bool QTransposeProxyModel::setItemData(const QModelIndex &index, const
//      QMap<int, QVariant> &roles)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel11setItemDataERK11QModelIndexRK4QMapIi8QVariantE(
    QTransposeProxyModel *self,
    const QModelIndex *index,
    const QMap<int, QVariant> *roles) {
  return self->setItemData(*index, *roles);
}

//  QSize QTransposeProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK20QTransposeProxyModel4spanERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  QMap<int, QVariant> QTransposeProxyModel::itemData(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK20QTransposeProxyModel8itemDataERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *index) {
  return new QMap<int, QVariant>(self->itemData(*index));
}

//  QModelIndex QTransposeProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK20QTransposeProxyModel13mapFromSourceERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QModelIndex QTransposeProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK20QTransposeProxyModel11mapToSourceERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QModelIndex QTransposeProxyModel::parent(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK20QTransposeProxyModel6parentERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->parent(*index));
}

//  QModelIndex QTransposeProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK20QTransposeProxyModel5indexEiiRK11QModelIndex(
    const QTransposeProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  bool QTransposeProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel10insertRowsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QTransposeProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel10removeRowsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QTransposeProxyModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel8moveRowsERK11QModelIndexiiS2_i(
    QTransposeProxyModel *self,
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

//  bool QTransposeProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel13insertColumnsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QTransposeProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel13removeColumnsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  bool QTransposeProxyModel::moveColumns(const QModelIndex &sourceParent,
//      int sourceColumn, int count, const QModelIndex &destinationParent,
//      int destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel11moveColumnsERK11QModelIndexiiS2_i(
    QTransposeProxyModel *self,
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

//  void QTransposeProxyModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTransposeProxyModel4sortEiN2Qt9SortOrderE(
    QTransposeProxyModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  a Python function taken by a CuteQTransposeProxyModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTransposeProxyModel(
    QTransposeProxyModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTransposeProxyModel *>(self)->take(key, call);
}

//  void QTransposeProxyModel::setSourceModel(QAbstractItemModel
//      *newSourceModel)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QTransposeProxyModel14setSourceModelEP18QAbstractItemModel(
    QTransposeProxyModel *self,
    QAbstractItemModel *newSourceModel) {
  self->QTransposeProxyModel::setSourceModel(newSourceModel);
}

//  int QTransposeProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QTransposeProxyModel8rowCountERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *parent) {
  return self->QTransposeProxyModel::rowCount(*parent);
}

//  int QTransposeProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QTransposeProxyModel11columnCountERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *parent) {
  return self->QTransposeProxyModel::columnCount(*parent);
}

//  QVariant QTransposeProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QTransposeProxyModel10headerDataEiN2Qt11OrientationEi(
    const QTransposeProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QTransposeProxyModel::headerData(
          section,
          orientation,
          role));
}

//  bool QTransposeProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QTransposeProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QTransposeProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->QTransposeProxyModel::setHeaderData(
      section,
      orientation,
      *value,
      role);
}

//  QSize QTransposeProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK20QTransposeProxyModel4spanERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->QTransposeProxyModel::span(*index));
}

//  QModelIndex QTransposeProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK20QTransposeProxyModel13mapFromSourceERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(
      self->QTransposeProxyModel::mapFromSource(
          *sourceIndex));
}

//  QModelIndex QTransposeProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK20QTransposeProxyModel11mapToSourceERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(
      self->QTransposeProxyModel::mapToSource(
          *proxyIndex));
}

//  QModelIndex QTransposeProxyModel::parent(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK20QTransposeProxyModel6parentERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->QTransposeProxyModel::parent(*index));
}

//  QModelIndex QTransposeProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK20QTransposeProxyModel5indexEiiRK11QModelIndex(
    const QTransposeProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QTransposeProxyModel::index(
          row,
          column,
          *parent));
}

//  bool QTransposeProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QTransposeProxyModel10insertRowsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QTransposeProxyModel::insertRows(row, count, *parent);
}

//  bool QTransposeProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QTransposeProxyModel10removeRowsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QTransposeProxyModel::removeRows(row, count, *parent);
}

//  bool QTransposeProxyModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QTransposeProxyModel8moveRowsERK11QModelIndexiiS2_i(
    QTransposeProxyModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->QTransposeProxyModel::moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destinationParent,
      destinationChild);
}

//  bool QTransposeProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QTransposeProxyModel13insertColumnsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QTransposeProxyModel::insertColumns(column, count, *parent);
}

//  bool QTransposeProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QTransposeProxyModel13removeColumnsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->QTransposeProxyModel::removeColumns(column, count, *parent);
}

//  bool QTransposeProxyModel::moveColumns(const QModelIndex &sourceParent,
//      int sourceColumn, int count, const QModelIndex &destinationParent,
//      int destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QTransposeProxyModel11moveColumnsERK11QModelIndexiiS2_i(
    QTransposeProxyModel *self,
    const QModelIndex *sourceParent,
    int sourceColumn,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->QTransposeProxyModel::moveColumns(
      *sourceParent,
      sourceColumn,
      count,
      *destinationParent,
      destinationChild);
}

//  void QTransposeProxyModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QTransposeProxyModel4sortEiN2Qt9SortOrderE(
    QTransposeProxyModel *self,
    int column,
    Qt::SortOrder order) {
  self->QTransposeProxyModel::sort(column, order);
}
