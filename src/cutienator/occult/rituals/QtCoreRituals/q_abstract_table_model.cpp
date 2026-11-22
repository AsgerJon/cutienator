//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAbstractTableModel that Python can take functions over in. Every QAbstractTableModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QModelIndex * (*CuteQAbstractTableModelCall0)(const void *, int, int, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQAbstractTableModelCall1)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractTableModelCall2)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef int (*CuteQAbstractTableModelCall3)(const void *, const QModelIndex *, int *);
typedef int (*CuteQAbstractTableModelCall4)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQAbstractTableModelCall5)(const void *, const QModelIndex *, int, int *);
typedef bool (*CuteQAbstractTableModelCall6)(const void *, const QModelIndex *, const QVariant *, int, int *);
typedef const QVariant * (*CuteQAbstractTableModelCall7)(const void *, int, int, int, int *);
typedef bool (*CuteQAbstractTableModelCall8)(const void *, int, int, const QVariant *, int, int *);
typedef bool (*CuteQAbstractTableModelCall9)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQAbstractTableModelCall10)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractTableModelCall11)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractTableModelCall12)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractTableModelCall13)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractTableModelCall14)(const void *, int, int, const QModelIndex *, int *);
typedef bool (*CuteQAbstractTableModelCall15)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef bool (*CuteQAbstractTableModelCall16)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
typedef void (*CuteQAbstractTableModelCall17)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQAbstractTableModelCall18)(const void *, const QModelIndex *, int *);
typedef void (*CuteQAbstractTableModelCall19)(const void *, int, int, int *);
typedef const QModelIndex * (*CuteQAbstractTableModelCall20)(const void *, const QModelIndex *, int *);
typedef const QSize * (*CuteQAbstractTableModelCall21)(const void *, const QModelIndex *, int *);
typedef void (*CuteQAbstractTableModelCall22)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
typedef bool (*CuteQAbstractTableModelCall23)(const void *, int *);
typedef void (*CuteQAbstractTableModelCall24)(const void *, int *);
typedef void (*CuteQAbstractTableModelCall25)(const void *, int *);
typedef bool (*CuteQAbstractTableModelCall26)(const void *, QEvent *, int *);
typedef bool (*CuteQAbstractTableModelCall27)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAbstractTableModelCall28)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAbstractTableModelCall29)(const void *, QChildEvent *, int *);
typedef void (*CuteQAbstractTableModelCall30)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractTableModelCall31)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAbstractTableModelCall32)(const void *, const QMetaMethod *, int *);
class CuteQAbstractTableModel : public QAbstractTableModel {
public:
  using QAbstractTableModel::QAbstractTableModel;
  void *taken[33] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel8rowCountERK11QModelIndex")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel11columnCountERK11QModelIndex")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6submitEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel6revertEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[32] = call;
      return true;
    }
    return false;
  }

  //  QModelIndex QAbstractTableModel::index(int row, int column, const
  //      QModelIndex &parent) const
  QModelIndex index(
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractTableModelCall0 call = reinterpret_cast<CuteQAbstractTableModelCall0>(taken[0]);
      const QModelIndex * given = call(this, row, column, &parent, &handled);
      if (handled && given) return *given;
    }
    return QAbstractTableModel::index(row, column, parent);
  }

  //  QModelIndex QAbstractTableModel::sibling(int row, int column, const
  //      QModelIndex &idx) const
  QModelIndex sibling(
      int row,
      int column,
      const QModelIndex &idx) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractTableModelCall1 call = reinterpret_cast<CuteQAbstractTableModelCall1>(taken[1]);
      const QModelIndex * given = call(this, row, column, &idx, &handled);
      if (handled && given) return *given;
    }
    return QAbstractTableModel::sibling(row, column, idx);
  }

  //  bool QAbstractTableModel::dropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractTableModelCall2 call = reinterpret_cast<CuteQAbstractTableModelCall2>(taken[2]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractTableModel::dropMimeData(data, action, row, column, parent);
  }

  //  int QAbstractItemModel::rowCount(const QModelIndex &parent) const
  int rowCount(const QModelIndex &parent) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractTableModelCall3 call = reinterpret_cast<CuteQAbstractTableModelCall3>(taken[3]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAbstractItemModel::columnCount(const QModelIndex &parent) const
  int columnCount(const QModelIndex &parent) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractTableModelCall4 call = reinterpret_cast<CuteQAbstractTableModelCall4>(taken[4]);
      int given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QVariant QAbstractItemModel::data(const QModelIndex &index, int role)
  //      const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractTableModelCall5 call = reinterpret_cast<CuteQAbstractTableModelCall5>(taken[5]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QAbstractItemModel::setData(const QModelIndex &index, const
  //      QVariant &value, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &value,
      int role) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractTableModelCall6 call = reinterpret_cast<CuteQAbstractTableModelCall6>(taken[6]);
      bool given = call(this, &index, &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setData(index, value, role);
  }

  //  QVariant QAbstractItemModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractTableModelCall7 call = reinterpret_cast<CuteQAbstractTableModelCall7>(taken[7]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::headerData(section, orientation, role);
  }

  //  bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &value, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &value,
      int role) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractTableModelCall8 call = reinterpret_cast<CuteQAbstractTableModelCall8>(taken[8]);
      bool given = call(this, section, static_cast<int>(orientation), &value, role, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::setHeaderData(section, orientation, value, role);
  }

  //  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractTableModelCall9 call = reinterpret_cast<CuteQAbstractTableModelCall9>(taken[9]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::clearItemData(index);
  }

  //  bool QAbstractItemModel::canDropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent) const
  bool canDropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractTableModelCall10 call = reinterpret_cast<CuteQAbstractTableModelCall10>(taken[10]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canDropMimeData(data, action, row, column, parent);
  }

  //  bool QAbstractItemModel::insertRows(int row, int count, const
  //      QModelIndex &parent)
  bool insertRows(int row, int count, const QModelIndex &parent) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractTableModelCall11 call = reinterpret_cast<CuteQAbstractTableModelCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractTableModelCall12 call = reinterpret_cast<CuteQAbstractTableModelCall12>(taken[12]);
      bool given = call(this, column, count, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::insertColumns(column, count, parent);
  }

  //  bool QAbstractItemModel::removeRows(int row, int count, const
  //      QModelIndex &parent)
  bool removeRows(int row, int count, const QModelIndex &parent) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractTableModelCall13 call = reinterpret_cast<CuteQAbstractTableModelCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractTableModelCall14 call = reinterpret_cast<CuteQAbstractTableModelCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractTableModelCall15 call = reinterpret_cast<CuteQAbstractTableModelCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractTableModelCall16 call = reinterpret_cast<CuteQAbstractTableModelCall16>(taken[16]);
      bool given = call(this, &sourceParent, sourceColumn, count, &destinationParent, destinationChild, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::moveColumns(sourceParent, sourceColumn, count, destinationParent, destinationChild);
  }

  //  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractTableModelCall17 call = reinterpret_cast<CuteQAbstractTableModelCall17>(taken[17]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QAbstractItemModel::fetchMore(parent);
  }

  //  bool QAbstractItemModel::canFetchMore(const QModelIndex &parent)
  //      const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractTableModelCall18 call = reinterpret_cast<CuteQAbstractTableModelCall18>(taken[18]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::canFetchMore(parent);
  }

  //  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractTableModelCall19 call = reinterpret_cast<CuteQAbstractTableModelCall19>(taken[19]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QAbstractItemModel::sort(column, order);
  }

  //  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractTableModelCall20 call = reinterpret_cast<CuteQAbstractTableModelCall20>(taken[20]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::buddy(index);
  }

  //  QSize QAbstractItemModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractTableModelCall21 call = reinterpret_cast<CuteQAbstractTableModelCall21>(taken[21]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemModel::span(index);
  }

  //  void QAbstractItemModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractTableModelCall22 call = reinterpret_cast<CuteQAbstractTableModelCall22>(taken[22]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QAbstractItemModel::multiData(index, roleDataSpan);
  }

  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractTableModelCall23 call = reinterpret_cast<CuteQAbstractTableModelCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }

  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractTableModelCall24 call = reinterpret_cast<CuteQAbstractTableModelCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }

  //  void QAbstractItemModel::resetInternalData()
  void resetInternalData() override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractTableModelCall25 call = reinterpret_cast<CuteQAbstractTableModelCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::resetInternalData();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractTableModelCall26 call = reinterpret_cast<CuteQAbstractTableModelCall26>(taken[26]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractTableModelCall27 call = reinterpret_cast<CuteQAbstractTableModelCall27>(taken[27]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractTableModelCall28 call = reinterpret_cast<CuteQAbstractTableModelCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractTableModelCall29 call = reinterpret_cast<CuteQAbstractTableModelCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractTableModelCall30 call = reinterpret_cast<CuteQAbstractTableModelCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractTableModelCall31 call = reinterpret_cast<CuteQAbstractTableModelCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractTableModelCall32 call = reinterpret_cast<CuteQAbstractTableModelCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QAbstractTableModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAbstractTableModel10metaObjectEv(
    const QAbstractTableModel *self) {
  return self->metaObject();
}

//  QString QAbstractTableModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAbstractTableModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractTableModel::tr(s, c, n));
}

//  QAbstractTableModel::~QAbstractTableModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractTableModelD1Ev(QAbstractTableModel *self) {
  delete self;
}

//  QModelIndex QAbstractTableModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractTableModel5indexEiiRK11QModelIndex(
    const QAbstractTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QAbstractTableModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractTableModel7siblingEiiRK11QModelIndex(
    const QAbstractTableModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  bool QAbstractTableModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractTableModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractTableModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::ItemFlags QAbstractTableModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractTableModel5flagsERK11QModelIndex(
    const QAbstractTableModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  a Python function taken by a CuteQAbstractTableModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractTableModel(
    QAbstractTableModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractTableModel *>(self)->take(key, call);
}

//  QModelIndex QAbstractTableModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QAbstractTableModel5indexEiiRK11QModelIndex(
    const QAbstractTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QAbstractTableModel::index(
          row,
          column,
          *parent));
}

//  QModelIndex QAbstractTableModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK19QAbstractTableModel7siblingEiiRK11QModelIndex(
    const QAbstractTableModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(
      self->QAbstractTableModel::sibling(
          row,
          column,
          *idx));
}

//  bool QAbstractTableModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractTableModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractTableModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QAbstractTableModel::dropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}
