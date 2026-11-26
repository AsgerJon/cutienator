//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/promotionmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/promotionmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/private/promotionmodel_p.h>
#include <QtDesigner/private/widgetdatabase_p.h>
#include <QtDesigner/abstractwidgetdatabase.h>
#include <QtDesigner/abstractpromotioninterface.h>
#include <QtDesigner/abstractformeditor.h>
#include <QtGui/qstandarditemmodel.h>
#include <QtCore/qcoreapplication.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qttools/src/designer/src/lib/shared/promotionmodel.cpp, line 18, as local:promotionmodel.cpp:StandardItemList
namespace {
using StandardItemList = QList<QStandardItem *>;
}  // namespace

//  from ../qttools/src/designer/src/lib/shared/promotionmodel.cpp, line 21, as local:promotionmodel.cpp:NumColumns
namespace {
enum { ClassNameColumn, IncludeFileColumn, IncludeTypeColumn, ReferencedColumn, NumColumns };
}  // namespace

//  from ../qttools/src/designer/src/lib/shared/promotionmodel.cpp, line 131, as _ZN18qdesigner_internal14PromotionModel15slotItemChangedEP13QStandardItem
namespace qdesigner_internal {
inline void PromotionModel::slotItemChanged(QStandardItem * changedItem) {
        // Retrieve DB item
        const ModelData data = modelData(changedItem);
        Q_ASSERT(data.isValid());
        QDesignerWidgetDataBaseItemInterface *dbItem = data.promotedItem;
        // Change header or type
        switch (changedItem->column()) {
        case ClassNameColumn:
            emit classNameChanged(dbItem,  changedItem->text());
            break;
        case IncludeTypeColumn:
        case IncludeFileColumn: {
            // Get both file and type items via parent.
            const QStandardItem *baseClassItem = changedItem->parent();
            const QStandardItem *fileItem = baseClassItem->child(changedItem->row(), IncludeFileColumn);
            const QStandardItem *typeItem =  baseClassItem->child(changedItem->row(), IncludeTypeColumn);
            emit includeFileChanged(dbItem, buildIncludeFile(fileItem->text(), typeItem->checkState() == Qt::Checked ? IncludeGlobal : IncludeLocal));
        }
            break;
        }
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/promotionmodel.cpp, line 159, as _ZNK18qdesigner_internal14PromotionModel9modelDataERK11QModelIndex
namespace qdesigner_internal {
inline PromotionModel::ModelData PromotionModel::modelData(const QModelIndex &index) const
    {
        return index.isValid() ? modelData(itemFromIndex(index)) : ModelData();
    }
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/promotionmodel.cpp, line 153, as _ZNK18qdesigner_internal14PromotionModel9modelDataEPK13QStandardItem
namespace qdesigner_internal {
inline PromotionModel::ModelData PromotionModel::modelData(const QStandardItem *item) const
    {
        const QVariant userData = item->data();
        return userData.canConvert<ModelData>() ? userData.value<ModelData>() : ModelData();
    }
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  const QMetaObject *qdesigner_internal::PromotionModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal14PromotionModel10metaObjectEv(
    const qdesigner_internal::PromotionModel *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::PromotionModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal14PromotionModel11qt_metacastEPKc(
    qdesigner_internal::PromotionModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::PromotionModel::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal14PromotionModel11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::PromotionModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  ModelData qdesigner_internal::PromotionModel::modelData(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PromotionModel::ModelData *ritual_ZNK18qdesigner_internal14PromotionModel9modelDataERK11QModelIndex(
    const qdesigner_internal::PromotionModel *self,
    const QModelIndex *index) {
  return new qdesigner_internal::PromotionModel::ModelData(
      self->modelData(
          *index));
}

//  ModelData qdesigner_internal::PromotionModel::modelData(const
//      QStandardItem *item) const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PromotionModel::ModelData *ritual_ZNK18qdesigner_internal14PromotionModel9modelDataEPK13QStandardItem(
    const qdesigner_internal::PromotionModel *self,
    const QStandardItem *item) {
  return new qdesigner_internal::PromotionModel::ModelData(
      self->modelData(
          item));
}

//  void qdesigner_internal::PromotionModel::includeFileChanged(QDesignerWidg
//      etDataBaseItemInterface *a0, const QString &includeFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14PromotionModel18includeFileChangedEP36QDesignerWidgetDataBaseItemInterfaceRK7QString(
    qdesigner_internal::PromotionModel *self,
    QDesignerWidgetDataBaseItemInterface *a0,
    const QString *includeFile) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::PromotionModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "includeFileChanged(QDesignerWidgetDataBaseItemInterface *,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "includeFileChanged(QDesignerWidgetDataBaseItemInterface *,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(includeFile)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::PromotionModel::classNameChanged(QDesignerWidget
//      DataBaseItemInterface *a0, const QString &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14PromotionModel16classNameChangedEP36QDesignerWidgetDataBaseItemInterfaceRK7QString(
    qdesigner_internal::PromotionModel *self,
    QDesignerWidgetDataBaseItemInterface *a0,
    const QString *newName) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::PromotionModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "classNameChanged(QDesignerWidgetDataBaseItemInterface *,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "classNameChanged(QDesignerWidgetDataBaseItemInterface *,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
      const_cast<void *>(static_cast<const void *>(newName)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void qdesigner_internal::PromotionModel::slotItemChanged(QStandardItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14PromotionModel15slotItemChangedEP13QStandardItem(
    qdesigner_internal::PromotionModel *self,
    QStandardItem *item) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "qdesigner_internal::PromotionModel")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "slotItemChanged(QStandardItem *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "slotItemChanged(QStandardItem *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&item)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
