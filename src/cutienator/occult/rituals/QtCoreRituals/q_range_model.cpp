//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrangemodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qrangemodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qcollator.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QRangeModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRangeModel : QRangeModel {
  using QRangeModel::resetInternalData;
  using QRangeModel::event;
  using QRangeModel::eventFilter;
};

//  A QRangeModel that Python can take functions over in. Every QRangeModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRangeModelCall0)(const void *, const QModelIndex *, int *);
typedef const QVariant * (*CuteQRangeModelCall1)(const void *, int, int, int, int *);
typedef bool (*CuteQRangeModelCall2)(const void *, int, int, const QVariant *, int, int *);
typedef const QVariant * (*CuteQRangeModelCall3)(const void *, const QModelIndex *, int, int *);
typedef bool (*CuteQRangeModelCall4)(const void *, const QModelIndex *, const QVariant *, int, int *);
typedef bool (*CuteQRangeModelCall5)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQRangeModelCall6)(const void *, const QModelIndex *, int *);
typedef void (*CuteQRangeModelCall7)(const void *, const QModelIndex *, int *);
typedef const QModelIndex * (*CuteQRangeModelCall8)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQRangeModelCall9)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef bool (*CuteQRangeModelCall10)(const void *, const QMimeData *, int, int, int, const QModelIndex *, int *);
typedef void (*CuteQRangeModelCall11)(const void *, const QModelIndex *, const QModelRoleDataSpan *, int *);
typedef void (*CuteQRangeModelCall12)(const void *, int, int, int *);
typedef const QSize * (*CuteQRangeModelCall13)(const void *, const QModelIndex *, int *);
typedef int (*CuteQRangeModelCall14)(const void *, int *);
typedef int (*CuteQRangeModelCall15)(const void *, int *);
typedef void (*CuteQRangeModelCall16)(const void *, int *);
typedef bool (*CuteQRangeModelCall17)(const void *, QEvent *, int *);
typedef bool (*CuteQRangeModelCall18)(const void *, QObject *, QEvent *, int *);
typedef bool (*CuteQRangeModelCall19)(const void *, int *);
typedef void (*CuteQRangeModelCall20)(const void *, int *);
typedef void (*CuteQRangeModelCall21)(const void *, QTimerEvent *, int *);
typedef void (*CuteQRangeModelCall22)(const void *, QChildEvent *, int *);
typedef void (*CuteQRangeModelCall23)(const void *, QEvent *, int *);
typedef void (*CuteQRangeModelCall24)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQRangeModelCall25)(const void *, const QMetaMethod *, int *);
class CuteQRangeModel : public QRangeModel {
public:
  using QRangeModel::QRangeModel;
  void *taken[26] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5flagsERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4dataERK11QModelIndexi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel5buddyERK11QModelIndex")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel4spanERK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDragActionsEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QAbstractItemModel20supportedDropActionsEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractItemModel17resetInternalDataEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
    return false;
  }

  //  Qt::ItemFlags QRangeModel::flags(const QModelIndex &index) const
  Qt::ItemFlags flags(const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRangeModelCall0 call = reinterpret_cast<CuteQRangeModelCall0>(taken[0]);
      int given = call(this, &index, &handled);
      if (handled) return QFlags<Qt::ItemFlag>::fromInt(given);
    }
    return QRangeModel::flags(index);
  }

  //  QVariant QRangeModel::headerData(int section, Qt::Orientation
  //      orientation, int role) const
  QVariant headerData(
      int section,
      Qt::Orientation orientation,
      int role) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRangeModelCall1 call = reinterpret_cast<CuteQRangeModelCall1>(taken[1]);
      const QVariant * given = call(this, section, static_cast<int>(orientation), role, &handled);
      if (handled && given) return *given;
    }
    return QRangeModel::headerData(section, orientation, role);
  }

  //  bool QRangeModel::setHeaderData(int section, Qt::Orientation
  //      orientation, const QVariant &data, int role)
  bool setHeaderData(
      int section,
      Qt::Orientation orientation,
      const QVariant &data,
      int role) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRangeModelCall2 call = reinterpret_cast<CuteQRangeModelCall2>(taken[2]);
      bool given = call(this, section, static_cast<int>(orientation), &data, role, &handled);
      if (handled) return given;
    }
    return QRangeModel::setHeaderData(section, orientation, data, role);
  }

  //  QVariant QRangeModel::data(const QModelIndex &index, int role) const
  QVariant data(const QModelIndex &index, int role) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRangeModelCall3 call = reinterpret_cast<CuteQRangeModelCall3>(taken[3]);
      const QVariant * given = call(this, &index, role, &handled);
      if (handled && given) return *given;
    }
    return QRangeModel::data(index, role);
  }

  //  bool QRangeModel::setData(const QModelIndex &index, const QVariant
  //      &data, int role)
  bool setData(
      const QModelIndex &index,
      const QVariant &data,
      int role) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRangeModelCall4 call = reinterpret_cast<CuteQRangeModelCall4>(taken[4]);
      bool given = call(this, &index, &data, role, &handled);
      if (handled) return given;
    }
    return QRangeModel::setData(index, data, role);
  }

  //  bool QRangeModel::clearItemData(const QModelIndex &index)
  bool clearItemData(const QModelIndex &index) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRangeModelCall5 call = reinterpret_cast<CuteQRangeModelCall5>(taken[5]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QRangeModel::clearItemData(index);
  }

  //  bool QRangeModel::canFetchMore(const QModelIndex &parent) const
  bool canFetchMore(const QModelIndex &parent) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQRangeModelCall6 call = reinterpret_cast<CuteQRangeModelCall6>(taken[6]);
      bool given = call(this, &parent, &handled);
      if (handled) return given;
    }
    return QRangeModel::canFetchMore(parent);
  }

  //  void QRangeModel::fetchMore(const QModelIndex &parent)
  void fetchMore(const QModelIndex &parent) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRangeModelCall7 call = reinterpret_cast<CuteQRangeModelCall7>(taken[7]);
      call(this, &parent, &handled);
      if (handled) return;
    }
    QRangeModel::fetchMore(parent);
  }

  //  QModelIndex QRangeModel::buddy(const QModelIndex &index) const
  QModelIndex buddy(const QModelIndex &index) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQRangeModelCall8 call = reinterpret_cast<CuteQRangeModelCall8>(taken[8]);
      const QModelIndex * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QRangeModel::buddy(index);
  }

  //  bool QRangeModel::canDropMimeData(const QMimeData *data,
  //      Qt::DropAction action, int row, int column, const QModelIndex
  //      &parent) const
  bool canDropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQRangeModelCall9 call = reinterpret_cast<CuteQRangeModelCall9>(taken[9]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QRangeModel::canDropMimeData(data, action, row, column, parent);
  }

  //  bool QRangeModel::dropMimeData(const QMimeData *data, Qt::DropAction
  //      action, int row, int column, const QModelIndex &parent)
  bool dropMimeData(
      const QMimeData *data,
      Qt::DropAction action,
      int row,
      int column,
      const QModelIndex &parent) override {
    if (taken[10]) {
      int handled = 0;
      CuteQRangeModelCall10 call = reinterpret_cast<CuteQRangeModelCall10>(taken[10]);
      bool given = call(this, data, static_cast<int>(action), row, column, &parent, &handled);
      if (handled) return given;
    }
    return QRangeModel::dropMimeData(data, action, row, column, parent);
  }

  //  void QRangeModel::multiData(const QModelIndex &index,
  //      QModelRoleDataSpan roleDataSpan) const
  void multiData(
      const QModelIndex &index,
      QModelRoleDataSpan roleDataSpan) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQRangeModelCall11 call = reinterpret_cast<CuteQRangeModelCall11>(taken[11]);
      call(this, &index, &roleDataSpan, &handled);
      if (handled) return;
    }
    QRangeModel::multiData(index, roleDataSpan);
  }

  //  void QRangeModel::sort(int column, Qt::SortOrder order)
  void sort(int column, Qt::SortOrder order) override {
    if (taken[12]) {
      int handled = 0;
      CuteQRangeModelCall12 call = reinterpret_cast<CuteQRangeModelCall12>(taken[12]);
      call(this, column, static_cast<int>(order), &handled);
      if (handled) return;
    }
    QRangeModel::sort(column, order);
  }

  //  QSize QRangeModel::span(const QModelIndex &index) const
  QSize span(const QModelIndex &index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQRangeModelCall13 call = reinterpret_cast<CuteQRangeModelCall13>(taken[13]);
      const QSize * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QRangeModel::span(index);
  }

  //  Qt::DropActions QRangeModel::supportedDragActions() const
  Qt::DropActions supportedDragActions() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQRangeModelCall14 call = reinterpret_cast<CuteQRangeModelCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QRangeModel::supportedDragActions();
  }

  //  Qt::DropActions QRangeModel::supportedDropActions() const
  Qt::DropActions supportedDropActions() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQRangeModelCall15 call = reinterpret_cast<CuteQRangeModelCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::DropAction>::fromInt(given);
    }
    return QRangeModel::supportedDropActions();
  }

  //  void QRangeModel::resetInternalData()
  void resetInternalData() override {
    if (taken[16]) {
      int handled = 0;
      CuteQRangeModelCall16 call = reinterpret_cast<CuteQRangeModelCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QRangeModel::resetInternalData();
  }

  //  bool QRangeModel::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQRangeModelCall17 call = reinterpret_cast<CuteQRangeModelCall17>(taken[17]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QRangeModel::event(a0);
  }

  //  bool QRangeModel::eventFilter(QObject *a0, QEvent *a1)
  bool eventFilter(QObject *a0, QEvent *a1) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRangeModelCall18 call = reinterpret_cast<CuteQRangeModelCall18>(taken[18]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QRangeModel::eventFilter(a0, a1);
  }

  //  bool QAbstractItemModel::submit()
  bool submit() override {
    if (taken[19]) {
      int handled = 0;
      CuteQRangeModelCall19 call = reinterpret_cast<CuteQRangeModelCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractItemModel::submit();
  }

  //  void QAbstractItemModel::revert()
  void revert() override {
    if (taken[20]) {
      int handled = 0;
      CuteQRangeModelCall20 call = reinterpret_cast<CuteQRangeModelCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemModel::revert();
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQRangeModelCall21 call = reinterpret_cast<CuteQRangeModelCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRangeModelCall22 call = reinterpret_cast<CuteQRangeModelCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRangeModelCall23 call = reinterpret_cast<CuteQRangeModelCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRangeModelCall24 call = reinterpret_cast<CuteQRangeModelCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQRangeModelCall25 call = reinterpret_cast<CuteQRangeModelCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QRangeModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QRangeModel10metaObjectEv(
    const QRangeModel *self) {
  return self->metaObject();
}

//  QString QRangeModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QRangeModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRangeModel::tr(s, c, n));
}

//  QRangeModel::~QRangeModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModelD1Ev(QRangeModel *self) {
  delete self;
}

//  QModelIndex QRangeModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QRangeModel5indexEiiRK11QModelIndex(
    const QRangeModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QRangeModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QRangeModel6parentERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  QModelIndex QRangeModel::sibling(int row, int column, const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QRangeModel7siblingEiiRK11QModelIndex(
    const QRangeModel *self,
    int row,
    int column,
    const QModelIndex *index) {
  return new QModelIndex(self->sibling(row, column, *index));
}

//  int QRangeModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel8rowCountERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QRangeModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel11columnCountERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  Qt::ItemFlags QRangeModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel5flagsERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  QVariant QRangeModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QRangeModel10headerDataEiN2Qt11OrientationEi(
    const QRangeModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QRangeModel::setHeaderData(int section, Qt::Orientation orientation,
//      const QVariant &data, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QRangeModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *data,
    int role) {
  return self->setHeaderData(section, orientation, *data, role);
}

//  QVariant QRangeModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QRangeModel4dataERK11QModelIndexi(
    const QRangeModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QRangeModel::setData(const QModelIndex &index, const QVariant &data,
//      int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel7setDataERK11QModelIndexRK8QVarianti(
    QRangeModel *self,
    const QModelIndex *index,
    const QVariant *data,
    int role) {
  return self->setData(*index, *data, role);
}

//  bool QRangeModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel13clearItemDataERK11QModelIndex(
    QRangeModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  bool QRangeModel::insertColumns(int column, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel13insertColumnsEiiRK11QModelIndex(
    QRangeModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QRangeModel::removeColumns(int column, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel13removeColumnsEiiRK11QModelIndex(
    QRangeModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  bool QRangeModel::moveColumns(const QModelIndex &sourceParent, int
//      sourceColumn, int count, const QModelIndex &destParent, int
//      destColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel11moveColumnsERK11QModelIndexiiS2_i(
    QRangeModel *self,
    const QModelIndex *sourceParent,
    int sourceColumn,
    int count,
    const QModelIndex *destParent,
    int destColumn) {
  return self->moveColumns(
      *sourceParent,
      sourceColumn,
      count,
      *destParent,
      destColumn);
}

//  bool QRangeModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel10insertRowsEiiRK11QModelIndex(
    QRangeModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QRangeModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel10removeRowsEiiRK11QModelIndex(
    QRangeModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QRangeModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destParent, int destRow)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel8moveRowsERK11QModelIndexiiS2_i(
    QRangeModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destParent,
    int destRow) {
  return self->moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destParent,
      destRow);
}

//  void QRangeModel::resetRoleNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel14resetRoleNamesEv(QRangeModel *self) {
  self->resetRoleNames();
}

//  bool QRangeModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QRangeModel12canFetchMoreERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  void QRangeModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel9fetchMoreERK11QModelIndex(
    QRangeModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  bool QRangeModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QRangeModel11hasChildrenERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QModelIndex QRangeModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QRangeModel5buddyERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->buddy(*index));
}

//  bool QRangeModel::canDropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QRangeModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QRangeModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->canDropMimeData(data, action, row, column, *parent);
}

//  bool QRangeModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QRangeModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  void QRangeModel::multiData(const QModelIndex &index, QModelRoleDataSpan
//      roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QRangeModel9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QRangeModel *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->multiData(*index, *roleDataSpan);
}

//  void QRangeModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel4sortEiN2Qt9SortOrderE(
    QRangeModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QCollator QRangeModel::sortCollator() const
extern "C" Q_DECL_EXPORT
QCollator *ritual_ZNK11QRangeModel12sortCollatorEv(const QRangeModel *self) {
  return new QCollator(self->sortCollator());
}

//  void QRangeModel::setSortCollator(const QCollator &collator)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel15setSortCollatorERK9QCollator(
    QRangeModel *self,
    const QCollator *collator) {
  self->setSortCollator(*collator);
}

//  void QRangeModel::resetSortCollator()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel17resetSortCollatorEv(QRangeModel *self) {
  self->resetSortCollator();
}

//  int QRangeModel::sortRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel8sortRoleEv(const QRangeModel *self) {
  return self->sortRole();
}

//  void QRangeModel::setSortRole(int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel11setSortRoleEi(QRangeModel *self, int role) {
  self->setSortRole(role);
}

//  void QRangeModel::resetSortRole()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel13resetSortRoleEv(QRangeModel *self) {
  self->resetSortRole();
}

//  QSize QRangeModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QRangeModel4spanERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  Qt::DropActions QRangeModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel20supportedDragActionsEv(
    const QRangeModel *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  void QRangeModel::setSupportedDragActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel23setSupportedDragActionsE6QFlagsIN2Qt10DropActionEE(
    QRangeModel *self,
    int actions) {
  self->setSupportedDragActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  void QRangeModel::resetSupportedDragActions()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel25resetSupportedDragActionsEv(QRangeModel *self) {
  self->resetSupportedDragActions();
}

//  Qt::DropActions QRangeModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel20supportedDropActionsEv(
    const QRangeModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  void QRangeModel::setSupportedDropActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel23setSupportedDropActionsE6QFlagsIN2Qt10DropActionEE(
    QRangeModel *self,
    int actions) {
  self->setSupportedDropActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  void QRangeModel::resetSupportedDropActions()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel25resetSupportedDropActionsEv(QRangeModel *self) {
  self->resetSupportedDropActions();
}

//  AutoConnectPolicy QRangeModel::autoConnectPolicy() const
extern "C" Q_DECL_EXPORT
QRangeModel::AutoConnectPolicy ritual_ZNK11QRangeModel17autoConnectPolicyEv(
    const QRangeModel *self) {
  return self->autoConnectPolicy();
}

//  void QRangeModel::setAutoConnectPolicy(AutoConnectPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel20setAutoConnectPolicyENS_17AutoConnectPolicyE(
    QRangeModel *self,
    QRangeModel::AutoConnectPolicy policy) {
  self->setAutoConnectPolicy(policy);
}

//  a Python function taken by a CuteQRangeModel, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRangeModel(
    QRangeModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRangeModel *>(self)->take(key, call);
}

//  Qt::ItemFlags QRangeModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QRangeModel5flagsERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QRangeModel::flags(*index).toInt());
}

//  QVariant QRangeModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK11QRangeModel10headerDataEiN2Qt11OrientationEi(
    const QRangeModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QRangeModel::headerData(
          section,
          orientation,
          role));
}

//  bool QRangeModel::setHeaderData(int section, Qt::Orientation orientation,
//      const QVariant &data, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QRangeModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QRangeModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *data,
    int role) {
  return self->QRangeModel::setHeaderData(section, orientation, *data, role);
}

//  QVariant QRangeModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK11QRangeModel4dataERK11QModelIndexi(
    const QRangeModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QRangeModel::data(*index, role));
}

//  bool QRangeModel::setData(const QModelIndex &index, const QVariant &data,
//      int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QRangeModel7setDataERK11QModelIndexRK8QVarianti(
    QRangeModel *self,
    const QModelIndex *index,
    const QVariant *data,
    int role) {
  return self->QRangeModel::setData(*index, *data, role);
}

//  bool QRangeModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QRangeModel13clearItemDataERK11QModelIndex(
    QRangeModel *self,
    const QModelIndex *index) {
  return self->QRangeModel::clearItemData(*index);
}

//  bool QRangeModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QRangeModel12canFetchMoreERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *parent) {
  return self->QRangeModel::canFetchMore(*parent);
}

//  void QRangeModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QRangeModel9fetchMoreERK11QModelIndex(
    QRangeModel *self,
    const QModelIndex *parent) {
  self->QRangeModel::fetchMore(*parent);
}

//  QModelIndex QRangeModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK11QRangeModel5buddyERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->QRangeModel::buddy(*index));
}

//  bool QRangeModel::canDropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QRangeModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QRangeModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QRangeModel::canDropMimeData(
      data,
      action,
      row,
      column,
      *parent);
}

//  bool QRangeModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QRangeModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QRangeModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->QRangeModel::dropMimeData(data, action, row, column, *parent);
}

//  void QRangeModel::multiData(const QModelIndex &index, QModelRoleDataSpan
//      roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK11QRangeModel9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QRangeModel *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->QRangeModel::multiData(*index, *roleDataSpan);
}

//  void QRangeModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QRangeModel4sortEiN2Qt9SortOrderE(
    QRangeModel *self,
    int column,
    Qt::SortOrder order) {
  self->QRangeModel::sort(column, order);
}

//  QSize QRangeModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QRangeModel4spanERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *index) {
  return new QSize(self->QRangeModel::span(*index));
}

//  Qt::DropActions QRangeModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QRangeModel20supportedDragActionsEv(
    const QRangeModel *self) {
  return static_cast<int>(self->QRangeModel::supportedDragActions().toInt());
}

//  Qt::DropActions QRangeModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QRangeModel20supportedDropActionsEv(
    const QRangeModel *self) {
  return static_cast<int>(self->QRangeModel::supportedDropActions().toInt());
}

//  void QRangeModel::resetInternalData()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QRangeModel17resetInternalDataEv(QRangeModel *self) {
  static_cast<OwnQRangeModel *>(self)->OwnQRangeModel::resetInternalData();
}

//  bool QRangeModel::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QRangeModel5eventEP6QEvent(
    QRangeModel *self,
    QEvent *a0) {
  return static_cast<OwnQRangeModel *>(self)->OwnQRangeModel::event(a0);
}

//  bool QRangeModel::eventFilter(QObject *a0, QEvent *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QRangeModel11eventFilterEP7QObjectP6QEvent(
    QRangeModel *self,
    QObject *a0,
    QEvent *a1) {
  return static_cast<OwnQRangeModel *>(self)->OwnQRangeModel::eventFilter(
      a0,
      a1);
}
