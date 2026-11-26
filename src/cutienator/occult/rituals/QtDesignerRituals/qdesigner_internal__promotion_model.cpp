//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/promotionmodel_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'qdesigner_internal::PromotionModel' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 3 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/promotionmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
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

//  from QtDesigner__qdesigner_internal_PromotionModel.cpp, line 1, as moc:qdesigner_internal::PromotionModel
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18qdesigner_internal14PromotionModelE_t {};
} // unnamed namespace

template <> constexpr inline auto qdesigner_internal::PromotionModel::qt_create_metaobjectdata<qt_meta_tag_ZN18qdesigner_internal14PromotionModelE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "qdesigner_internal::PromotionModel",
        "includeFileChanged",
        "",
        "QDesignerWidgetDataBaseItemInterface*",
        "includeFile",
        "classNameChanged",
        "newName",
        "slotItemChanged",
        "QStandardItem*",
        "item"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'includeFileChanged'
        QtMocHelpers::SignalData<void(QDesignerWidgetDataBaseItemInterface *, const QString &)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 2 }, { QMetaType::QString, 4 },
        }}),
        // Signal 'classNameChanged'
        QtMocHelpers::SignalData<void(QDesignerWidgetDataBaseItemInterface *, const QString &)>(5, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 2 }, { QMetaType::QString, 6 },
        }}),
        // Slot 'slotItemChanged'
        QtMocHelpers::SlotData<void(QStandardItem *)>(7, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 8, 9 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<PromotionModel, qt_meta_tag_ZN18qdesigner_internal14PromotionModelE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject qdesigner_internal::PromotionModel::staticMetaObject = { {
    QMetaObject::SuperData::link<QStandardItemModel::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal14PromotionModelE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal14PromotionModelE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18qdesigner_internal14PromotionModelE_t>.metaTypes,
    nullptr
} };

void qdesigner_internal::PromotionModel::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<PromotionModel *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->includeFileChanged((*reinterpret_cast<std::add_pointer_t<QDesignerWidgetDataBaseItemInterface*>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2]))); break;
        case 1: _t->classNameChanged((*reinterpret_cast<std::add_pointer_t<QDesignerWidgetDataBaseItemInterface*>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2]))); break;
        case 2: _t->slotItemChanged((*reinterpret_cast<std::add_pointer_t<QStandardItem*>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (PromotionModel::*)(QDesignerWidgetDataBaseItemInterface * , const QString & )>(_a, &PromotionModel::includeFileChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (PromotionModel::*)(QDesignerWidgetDataBaseItemInterface * , const QString & )>(_a, &PromotionModel::classNameChanged, 1))
            return;
    }
}

const QMetaObject *qdesigner_internal::PromotionModel::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *qdesigner_internal::PromotionModel::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal14PromotionModelE_t>.strings))
        return static_cast<void*>(this);
    return QStandardItemModel::qt_metacast(_clname);
}

int qdesigner_internal::PromotionModel::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QStandardItemModel::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void qdesigner_internal::PromotionModel::includeFileChanged(QDesignerWidgetDataBaseItemInterface * _t1, const QString & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1, _t2);
}

// SIGNAL 1
void qdesigner_internal::PromotionModel::classNameChanged(QDesignerWidgetDataBaseItemInterface * _t1, const QString & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1, _t2);
}
QT_WARNING_POP

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

//  from ../qttools/src/designer/src/lib/shared/promotionmodel.cpp, line 83, as _ZN18qdesigner_internal14PromotionModelC1EP28QDesignerFormEditorInterface
namespace qdesigner_internal {
inline PromotionModel::PromotionModel(QDesignerFormEditorInterface *core) :
        m_core(core)
    {
        connect(this, &QStandardItemModel::itemChanged, this, &PromotionModel::slotItemChanged);
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

//  from ../qttools/src/designer/src/lib/shared/promotionmodel.cpp, line 89, as _ZN18qdesigner_internal14PromotionModel17initializeHeadersEv
namespace qdesigner_internal {
inline void PromotionModel::initializeHeaders() {
        setColumnCount(NumColumns);
        QStringList horizontalLabels(tr("Name"));
        horizontalLabels += tr("Header file");
        horizontalLabels += tr("Global include");
        horizontalLabels += tr("Usage");
        setHorizontalHeaderLabels (horizontalLabels);
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

//  QString qdesigner_internal::PromotionModel::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal14PromotionModel2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::PromotionModel::tr(s, c, n));
}

//  qdesigner_internal::PromotionModel::PromotionModel(QDesignerFormEditorInt
//      erface *core)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PromotionModel *ritual_ZN18qdesigner_internal14PromotionModelC1EP28QDesignerFormEditorInterface(
    QDesignerFormEditorInterface *core) {
  return new qdesigner_internal::PromotionModel(core);
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

//  void qdesigner_internal::PromotionModel::initializeHeaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal14PromotionModel17initializeHeadersEv(
    qdesigner_internal::PromotionModel *self) {
  self->initializeHeaders();
}
