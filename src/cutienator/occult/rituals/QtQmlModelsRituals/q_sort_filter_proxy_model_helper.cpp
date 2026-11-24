//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qsortfilterproxymodelhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QSortFilterProxyModelHelper may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSortFilterProxyModelHelper : QSortFilterProxyModelHelper {
  using QSortFilterProxyModelHelper::beginInsertRows;
  using QSortFilterProxyModelHelper::beginInsertColumns;
  using QSortFilterProxyModelHelper::endInsertRows;
  using QSortFilterProxyModelHelper::endInsertColumns;
  using QSortFilterProxyModelHelper::beginRemoveRows;
  using QSortFilterProxyModelHelper::beginRemoveColumns;
  using QSortFilterProxyModelHelper::endRemoveRows;
  using QSortFilterProxyModelHelper::endRemoveColumns;
  using QSortFilterProxyModelHelper::beginResetModel;
  using QSortFilterProxyModelHelper::endResetModel;
  using QSortFilterProxyModelHelper::filterAcceptsRowInternal;
  using QSortFilterProxyModelHelper::filterAcceptsRow;
  using QSortFilterProxyModelHelper::filterAcceptsColumnInternal;
  using QSortFilterProxyModelHelper::filterAcceptsColumn;
  using QSortFilterProxyModelHelper::lessThan;
};

//  A QSortFilterProxyModelHelper that Python can take functions over in. Every QSortFilterProxyModelHelper
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSortFilterProxyModelHelperCall0)(const void *, int, const QModelIndex *, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall1)(const void *, const QModelIndex *, int, int, int, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall2)(const void *, const QModelIndex *, int, int, int, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall3)(const void *, const QModelIndex *, int, int, int, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall4)(const void *, int *);
typedef void * (*CuteQSortFilterProxyModelHelperCall5)(const void *, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall6)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall7)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall8)(const void *, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall9)(const void *, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall10)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall11)(const void *, const QModelIndex *, int, int, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall12)(const void *, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall13)(const void *, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall14)(const void *, int *);
typedef void (*CuteQSortFilterProxyModelHelperCall15)(const void *, int *);
typedef bool (*CuteQSortFilterProxyModelHelperCall16)(const void *, int, const QModelIndex *, int *);
typedef bool (*CuteQSortFilterProxyModelHelperCall17)(const void *, int, const QModelIndex *, int *);
typedef bool (*CuteQSortFilterProxyModelHelperCall18)(const void *, int, const QModelIndex *, int *);
typedef bool (*CuteQSortFilterProxyModelHelperCall19)(const void *, int, const QModelIndex *, int *);
typedef bool (*CuteQSortFilterProxyModelHelperCall20)(const void *, const QModelIndex *, const QModelIndex *, int *);
class CuteQSortFilterProxyModelHelper : public QSortFilterProxyModelHelper {
public:
  using QSortFilterProxyModelHelper::QSortFilterProxyModelHelper;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper14filter_changedENS_9DirectionERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper21source_items_insertedERK11QModelIndexiiNS_9DirectionE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper32source_items_about_to_be_removedERK11QModelIndexiiNS_9DirectionE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper20source_items_removedERK11QModelIndexiiNS_9DirectionE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper4sortEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper10proxyModelEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper15beginInsertRowsERK11QModelIndexii")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper18beginInsertColumnsERK11QModelIndexii")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper13endInsertRowsEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper16endInsertColumnsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper15beginRemoveRowsERK11QModelIndexii")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper18beginRemoveColumnsERK11QModelIndexii")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper13endRemoveRowsEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper16endRemoveColumnsEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper15beginResetModelEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QSortFilterProxyModelHelper13endResetModelEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper24filterAcceptsRowInternalEiRK11QModelIndex")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper16filterAcceptsRowEiRK11QModelIndex")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper27filterAcceptsColumnInternalEiRK11QModelIndex")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper19filterAcceptsColumnEiRK11QModelIndex")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QSortFilterProxyModelHelper8lessThanERK11QModelIndexS2_")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

  //  void QSortFilterProxyModelHelper::filter_changed(Direction dir, const
  //      QModelIndex &source_parent)
  void filter_changed(
      QSortFilterProxyModelHelper::Direction dir,
      const QModelIndex &source_parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall0 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall0>(taken[0]);
      call(this, static_cast<int>(dir), &source_parent, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::filter_changed(dir, source_parent);
  }

  //  void QSortFilterProxyModelHelper::source_items_inserted(const
  //      QModelIndex &source_parent, int start, int end, Direction
  //      direction)
  void source_items_inserted(
      const QModelIndex &source_parent,
      int start,
      int end,
      QSortFilterProxyModelHelper::Direction direction) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall1 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall1>(taken[1]);
      call(this, &source_parent, start, end, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::source_items_inserted(source_parent, start, end, direction);
  }

  //  void
  //      QSortFilterProxyModelHelper::source_items_about_to_be_removed(con
  //      st QModelIndex &source_parent, int start, int end, Direction
  //      direction)
  void source_items_about_to_be_removed(
      const QModelIndex &source_parent,
      int start,
      int end,
      QSortFilterProxyModelHelper::Direction direction) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall2 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall2>(taken[2]);
      call(this, &source_parent, start, end, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::source_items_about_to_be_removed(source_parent, start, end, direction);
  }

  //  void QSortFilterProxyModelHelper::source_items_removed(const
  //      QModelIndex &source_parent, int start, int end, Direction
  //      direction)
  void source_items_removed(
      const QModelIndex &source_parent,
      int start,
      int end,
      QSortFilterProxyModelHelper::Direction direction) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall3 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall3>(taken[3]);
      call(this, &source_parent, start, end, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::source_items_removed(source_parent, start, end, direction);
  }

  //  void QSortFilterProxyModelHelper::sort()
  void sort() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall4 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::sort();
  }

  //  const QAbstractProxyModel *QSortFilterProxyModelHelper::proxyModel()
  //      const
  const QAbstractProxyModel *proxyModel() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall5 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QAbstractProxyModel *>(given);
    }
    return {};
  }

  //  void QSortFilterProxyModelHelper::beginInsertRows(const QModelIndex
  //      &a0, int a1, int a2)
  void beginInsertRows(const QModelIndex &a0, int a1, int a2) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall6 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall6>(taken[6]);
      call(this, &a0, a1, a2, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::beginInsertRows(a0, a1, a2);
  }

  //  void QSortFilterProxyModelHelper::beginInsertColumns(const
  //      QModelIndex &a0, int a1, int a2)
  void beginInsertColumns(const QModelIndex &a0, int a1, int a2) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall7 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall7>(taken[7]);
      call(this, &a0, a1, a2, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::beginInsertColumns(a0, a1, a2);
  }

  //  void QSortFilterProxyModelHelper::endInsertRows()
  void endInsertRows() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall8 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::endInsertRows();
  }

  //  void QSortFilterProxyModelHelper::endInsertColumns()
  void endInsertColumns() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall9 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::endInsertColumns();
  }

  //  void QSortFilterProxyModelHelper::beginRemoveRows(const QModelIndex
  //      &a0, int a1, int a2)
  void beginRemoveRows(const QModelIndex &a0, int a1, int a2) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall10 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall10>(taken[10]);
      call(this, &a0, a1, a2, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::beginRemoveRows(a0, a1, a2);
  }

  //  void QSortFilterProxyModelHelper::beginRemoveColumns(const
  //      QModelIndex &a0, int a1, int a2)
  void beginRemoveColumns(const QModelIndex &a0, int a1, int a2) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall11 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall11>(taken[11]);
      call(this, &a0, a1, a2, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::beginRemoveColumns(a0, a1, a2);
  }

  //  void QSortFilterProxyModelHelper::endRemoveRows()
  void endRemoveRows() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall12 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::endRemoveRows();
  }

  //  void QSortFilterProxyModelHelper::endRemoveColumns()
  void endRemoveColumns() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall13 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::endRemoveColumns();
  }

  //  void QSortFilterProxyModelHelper::beginResetModel()
  void beginResetModel() override {
    if (taken[14]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall14 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::beginResetModel();
  }

  //  void QSortFilterProxyModelHelper::endResetModel()
  void endResetModel() override {
    if (taken[15]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall15 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QSortFilterProxyModelHelper::endResetModel();
  }

  //  bool QSortFilterProxyModelHelper::filterAcceptsRowInternal(int a0,
  //      const QModelIndex &a1) const
  bool filterAcceptsRowInternal(
      int a0,
      const QModelIndex &a1) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall16 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall16>(taken[16]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModelHelper::filterAcceptsRowInternal(a0, a1);
  }

  //  bool QSortFilterProxyModelHelper::filterAcceptsRow(int a0, const
  //      QModelIndex &a1) const
  bool filterAcceptsRow(int a0, const QModelIndex &a1) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall17 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall17>(taken[17]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModelHelper::filterAcceptsRow(a0, a1);
  }

  //  bool QSortFilterProxyModelHelper::filterAcceptsColumnInternal(int a0,
  //      const QModelIndex &a1) const
  bool filterAcceptsColumnInternal(
      int a0,
      const QModelIndex &a1) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall18 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall18>(taken[18]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModelHelper::filterAcceptsColumnInternal(a0, a1);
  }

  //  bool QSortFilterProxyModelHelper::filterAcceptsColumn(int a0, const
  //      QModelIndex &a1) const
  bool filterAcceptsColumn(int a0, const QModelIndex &a1) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall19 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall19>(taken[19]);
      bool given = call(this, a0, &a1, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModelHelper::filterAcceptsColumn(a0, a1);
  }

  //  bool QSortFilterProxyModelHelper::lessThan(const QModelIndex &a0,
  //      const QModelIndex &a1) const
  bool lessThan(
      const QModelIndex &a0,
      const QModelIndex &a1) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSortFilterProxyModelHelperCall20 call = reinterpret_cast<CuteQSortFilterProxyModelHelperCall20>(taken[20]);
      bool given = call(this, &a0, &a1, &handled);
      if (handled) return given;
    }
    return QSortFilterProxyModelHelper::lessThan(a0, a1);
  }
};

//  QSortFilterProxyModelHelper::~QSortFilterProxyModelHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelperD1Ev(
    QSortFilterProxyModelHelper *self) {
  delete self;
}

//  void QSortFilterProxyModelHelper::setProperties(QVariant *target, const
//      QQmlSortFilterProxyModel *proxyModel, const QModelIndex &sourceIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper13setPropertiesEP8QVariantPK24QQmlSortFilterProxyModelRK11QModelIndex(
    QVariant *target,
    const QQmlSortFilterProxyModel *proxyModel,
    const QModelIndex *sourceIndex) {
  QSortFilterProxyModelHelper::setProperties(
      target,
      proxyModel,
      *sourceIndex);
}

//  bool QSortFilterProxyModelHelper::can_create_mapping(const QModelIndex
//      &source_parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSortFilterProxyModelHelper18can_create_mappingERK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    const QModelIndex *source_parent) {
  return self->can_create_mapping(*source_parent);
}

//  void QSortFilterProxyModelHelper::remove_from_mapping(const QModelIndex
//      &source_parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper19remove_from_mappingERK11QModelIndex(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *source_parent) {
  self->remove_from_mapping(*source_parent);
}

//  void QSortFilterProxyModelHelper::clearSourceIndexMapping()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper23clearSourceIndexMappingEv(
    QSortFilterProxyModelHelper *self) {
  self->clearSourceIndexMapping();
}

//  QModelIndex QSortFilterProxyModelHelper::source_to_proxy(const
//      QModelIndex &source_index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK27QSortFilterProxyModelHelper15source_to_proxyERK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    const QModelIndex *source_index) {
  return new QModelIndex(self->source_to_proxy(*source_index));
}

//  QModelIndex QSortFilterProxyModelHelper::proxy_to_source(const
//      QModelIndex &proxy_index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK27QSortFilterProxyModelHelper15proxy_to_sourceERK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    const QModelIndex *proxy_index) {
  return new QModelIndex(self->proxy_to_source(*proxy_index));
}

//  void QSortFilterProxyModelHelper::updateChildrenMapping(const QModelIndex
//      &source_parent, Mapping *parent_mapping, Direction direction, int
//      start, int end, int delta_item_count, bool remove)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper21updateChildrenMappingERK11QModelIndexPNS_7MappingENS_9DirectionEiiib(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *source_parent,
    QSortFilterProxyModelHelper::Mapping *parent_mapping,
    QSortFilterProxyModelHelper::Direction direction,
    int start,
    int end,
    int delta_item_count,
    bool remove) {
  self->updateChildrenMapping(
      *source_parent,
      parent_mapping,
      direction,
      start,
      end,
      delta_item_count,
      remove);
}

//  void QSortFilterProxyModelHelper::filter_changed(Direction dir, const
//      QModelIndex &source_parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper14filter_changedENS_9DirectionERK11QModelIndex(
    QSortFilterProxyModelHelper *self,
    QSortFilterProxyModelHelper::Direction dir,
    const QModelIndex *source_parent) {
  self->filter_changed(dir, *source_parent);
}

//  void QSortFilterProxyModelHelper::source_items_inserted(const QModelIndex
//      &source_parent, int start, int end, Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper21source_items_insertedERK11QModelIndexiiNS_9DirectionE(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *source_parent,
    int start,
    int end,
    QSortFilterProxyModelHelper::Direction direction) {
  self->source_items_inserted(*source_parent, start, end, direction);
}

//  void QSortFilterProxyModelHelper::source_items_about_to_be_removed(const
//      QModelIndex &source_parent, int start, int end, Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper32source_items_about_to_be_removedERK11QModelIndexiiNS_9DirectionE(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *source_parent,
    int start,
    int end,
    QSortFilterProxyModelHelper::Direction direction) {
  self->source_items_about_to_be_removed(
      *source_parent,
      start,
      end,
      direction);
}

//  void QSortFilterProxyModelHelper::source_items_removed(const QModelIndex
//      &source_parent, int start, int end, Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper20source_items_removedERK11QModelIndexiiNS_9DirectionE(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *source_parent,
    int start,
    int end,
    QSortFilterProxyModelHelper::Direction direction) {
  self->source_items_removed(*source_parent, start, end, direction);
}

//  void QSortFilterProxyModelHelper::sort()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper4sortEv(
    QSortFilterProxyModelHelper *self) {
  self->sort();
}

//  const QAbstractProxyModel *QSortFilterProxyModelHelper::proxyModel()
//      const
extern "C" Q_DECL_EXPORT
const QAbstractProxyModel *ritual_ZNK27QSortFilterProxyModelHelper10proxyModelEv(
    const QSortFilterProxyModelHelper *self) {
  return self->proxyModel();
}

//  void QSortFilterProxyModelHelper::beginInsertRows(const QModelIndex &a0,
//      int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper15beginInsertRowsERK11QModelIndexii(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->beginInsertRows(*a0, a1, a2);
}

//  void QSortFilterProxyModelHelper::beginInsertColumns(const QModelIndex
//      &a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper18beginInsertColumnsERK11QModelIndexii(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->beginInsertColumns(*a0, a1, a2);
}

//  void QSortFilterProxyModelHelper::endInsertRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper13endInsertRowsEv(
    QSortFilterProxyModelHelper *self) {
  self->endInsertRows();
}

//  void QSortFilterProxyModelHelper::endInsertColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper16endInsertColumnsEv(
    QSortFilterProxyModelHelper *self) {
  self->endInsertColumns();
}

//  void QSortFilterProxyModelHelper::beginRemoveRows(const QModelIndex &a0,
//      int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper15beginRemoveRowsERK11QModelIndexii(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->beginRemoveRows(*a0, a1, a2);
}

//  void QSortFilterProxyModelHelper::beginRemoveColumns(const QModelIndex
//      &a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper18beginRemoveColumnsERK11QModelIndexii(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->beginRemoveColumns(*a0, a1, a2);
}

//  void QSortFilterProxyModelHelper::endRemoveRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper13endRemoveRowsEv(
    QSortFilterProxyModelHelper *self) {
  self->endRemoveRows();
}

//  void QSortFilterProxyModelHelper::endRemoveColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper16endRemoveColumnsEv(
    QSortFilterProxyModelHelper *self) {
  self->endRemoveColumns();
}

//  void QSortFilterProxyModelHelper::beginResetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper15beginResetModelEv(
    QSortFilterProxyModelHelper *self) {
  self->beginResetModel();
}

//  void QSortFilterProxyModelHelper::endResetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper13endResetModelEv(
    QSortFilterProxyModelHelper *self) {
  self->endResetModel();
}

//  void QSortFilterProxyModelHelper::changePersistentIndexList(const
//      QModelIndexList &a0, const QModelIndexList &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSortFilterProxyModelHelper25changePersistentIndexListERK5QListI11QModelIndexES4_(
    QSortFilterProxyModelHelper *self,
    const QList<QModelIndex> *a0,
    const QList<QModelIndex> *a1) {
  self->changePersistentIndexList(*a0, *a1);
}

//  bool QSortFilterProxyModelHelper::filterAcceptsRowInternal(int a0, const
//      QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSortFilterProxyModelHelper24filterAcceptsRowInternalEiRK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    int a0,
    const QModelIndex *a1) {
  return self->filterAcceptsRowInternal(a0, *a1);
}

//  bool QSortFilterProxyModelHelper::filterAcceptsRow(int a0, const
//      QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSortFilterProxyModelHelper16filterAcceptsRowEiRK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    int a0,
    const QModelIndex *a1) {
  return self->filterAcceptsRow(a0, *a1);
}

//  bool QSortFilterProxyModelHelper::filterAcceptsColumnInternal(int a0,
//      const QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSortFilterProxyModelHelper27filterAcceptsColumnInternalEiRK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    int a0,
    const QModelIndex *a1) {
  return self->filterAcceptsColumnInternal(a0, *a1);
}

//  bool QSortFilterProxyModelHelper::filterAcceptsColumn(int a0, const
//      QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSortFilterProxyModelHelper19filterAcceptsColumnEiRK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    int a0,
    const QModelIndex *a1) {
  return self->filterAcceptsColumn(a0, *a1);
}

//  bool QSortFilterProxyModelHelper::lessThan(const QModelIndex &a0, const
//      QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QSortFilterProxyModelHelper8lessThanERK11QModelIndexS2_(
    const QSortFilterProxyModelHelper *self,
    const QModelIndex *a0,
    const QModelIndex *a1) {
  return self->lessThan(*a0, *a1);
}

//  a Python function taken by a CuteQSortFilterProxyModelHelper, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSortFilterProxyModelHelper(
    QSortFilterProxyModelHelper *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSortFilterProxyModelHelper *>(self)->take(key, call);
}

//  void QSortFilterProxyModelHelper::filter_changed(Direction dir, const
//      QModelIndex &source_parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper14filter_changedENS_9DirectionERK11QModelIndex(
    QSortFilterProxyModelHelper *self,
    QSortFilterProxyModelHelper::Direction dir,
    const QModelIndex *source_parent) {
  self->QSortFilterProxyModelHelper::filter_changed(dir, *source_parent);
}

//  void QSortFilterProxyModelHelper::source_items_inserted(const QModelIndex
//      &source_parent, int start, int end, Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper21source_items_insertedERK11QModelIndexiiNS_9DirectionE(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *source_parent,
    int start,
    int end,
    QSortFilterProxyModelHelper::Direction direction) {
  self->QSortFilterProxyModelHelper::source_items_inserted(
      *source_parent,
      start,
      end,
      direction);
}

//  void QSortFilterProxyModelHelper::source_items_about_to_be_removed(const
//      QModelIndex &source_parent, int start, int end, Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper32source_items_about_to_be_removedERK11QModelIndexiiNS_9DirectionE(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *source_parent,
    int start,
    int end,
    QSortFilterProxyModelHelper::Direction direction) {
  self->QSortFilterProxyModelHelper::source_items_about_to_be_removed(
      *source_parent,
      start,
      end,
      direction);
}

//  void QSortFilterProxyModelHelper::source_items_removed(const QModelIndex
//      &source_parent, int start, int end, Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper20source_items_removedERK11QModelIndexiiNS_9DirectionE(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *source_parent,
    int start,
    int end,
    QSortFilterProxyModelHelper::Direction direction) {
  self->QSortFilterProxyModelHelper::source_items_removed(
      *source_parent,
      start,
      end,
      direction);
}

//  void QSortFilterProxyModelHelper::sort()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper4sortEv(
    QSortFilterProxyModelHelper *self) {
  self->QSortFilterProxyModelHelper::sort();
}

//  void QSortFilterProxyModelHelper::beginInsertRows(const QModelIndex &a0,
//      int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper15beginInsertRowsERK11QModelIndexii(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  static_cast<OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::beginInsertRows(
      *a0,
      a1,
      a2);
}

//  void QSortFilterProxyModelHelper::beginInsertColumns(const QModelIndex
//      &a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper18beginInsertColumnsERK11QModelIndexii(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  static_cast<OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::beginInsertColumns(
      *a0,
      a1,
      a2);
}

//  void QSortFilterProxyModelHelper::endInsertRows()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper13endInsertRowsEv(
    QSortFilterProxyModelHelper *self) {
  static_cast<OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::endInsertRows();
}

//  void QSortFilterProxyModelHelper::endInsertColumns()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper16endInsertColumnsEv(
    QSortFilterProxyModelHelper *self) {
  static_cast<OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::endInsertColumns();
}

//  void QSortFilterProxyModelHelper::beginRemoveRows(const QModelIndex &a0,
//      int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper15beginRemoveRowsERK11QModelIndexii(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  static_cast<OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::beginRemoveRows(
      *a0,
      a1,
      a2);
}

//  void QSortFilterProxyModelHelper::beginRemoveColumns(const QModelIndex
//      &a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper18beginRemoveColumnsERK11QModelIndexii(
    QSortFilterProxyModelHelper *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  static_cast<OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::beginRemoveColumns(
      *a0,
      a1,
      a2);
}

//  void QSortFilterProxyModelHelper::endRemoveRows()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper13endRemoveRowsEv(
    QSortFilterProxyModelHelper *self) {
  static_cast<OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::endRemoveRows();
}

//  void QSortFilterProxyModelHelper::endRemoveColumns()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper16endRemoveColumnsEv(
    QSortFilterProxyModelHelper *self) {
  static_cast<OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::endRemoveColumns();
}

//  void QSortFilterProxyModelHelper::beginResetModel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper15beginResetModelEv(
    QSortFilterProxyModelHelper *self) {
  static_cast<OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::beginResetModel();
}

//  void QSortFilterProxyModelHelper::endResetModel()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QSortFilterProxyModelHelper13endResetModelEv(
    QSortFilterProxyModelHelper *self) {
  static_cast<OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::endResetModel();
}

//  bool QSortFilterProxyModelHelper::filterAcceptsRowInternal(int a0, const
//      QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QSortFilterProxyModelHelper24filterAcceptsRowInternalEiRK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    int a0,
    const QModelIndex *a1) {
  return static_cast<const OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::filterAcceptsRowInternal(
      a0,
      *a1);
}

//  bool QSortFilterProxyModelHelper::filterAcceptsRow(int a0, const
//      QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QSortFilterProxyModelHelper16filterAcceptsRowEiRK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    int a0,
    const QModelIndex *a1) {
  return static_cast<const OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::filterAcceptsRow(
      a0,
      *a1);
}

//  bool QSortFilterProxyModelHelper::filterAcceptsColumnInternal(int a0,
//      const QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QSortFilterProxyModelHelper27filterAcceptsColumnInternalEiRK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    int a0,
    const QModelIndex *a1) {
  return static_cast<const OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::filterAcceptsColumnInternal(
      a0,
      *a1);
}

//  bool QSortFilterProxyModelHelper::filterAcceptsColumn(int a0, const
//      QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QSortFilterProxyModelHelper19filterAcceptsColumnEiRK11QModelIndex(
    const QSortFilterProxyModelHelper *self,
    int a0,
    const QModelIndex *a1) {
  return static_cast<const OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::filterAcceptsColumn(
      a0,
      *a1);
}

//  bool QSortFilterProxyModelHelper::lessThan(const QModelIndex &a0, const
//      QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QSortFilterProxyModelHelper8lessThanERK11QModelIndexS2_(
    const QSortFilterProxyModelHelper *self,
    const QModelIndex *a0,
    const QModelIndex *a1) {
  return static_cast<const OwnQSortFilterProxyModelHelper *>(self)->OwnQSortFilterProxyModelHelper::lessThan(
      *a0,
      *a1);
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
