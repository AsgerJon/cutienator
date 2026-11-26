//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickstacklayout_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickstacklayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QQuickStackLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickStackLayout10metaObjectEv(
    const QQuickStackLayout *self) {
  return self->metaObject();
}

//  void *QQuickStackLayout::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickStackLayout11qt_metacastEPKc(
    QQuickStackLayout *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickStackLayout::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickStackLayout11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickStackLayout *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickStackLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickStackLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStackLayout::tr(s, c, n));
}

//  void QQuickStackLayout::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout21qt_qmlMarker_attachedEv(
    QQuickStackLayout *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickStackLayout::QQuickStackLayout(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickStackLayout *ritual_ZN17QQuickStackLayoutC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickStackLayout(parent);
}

//  int QQuickStackLayout::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickStackLayout5countEv(const QQuickStackLayout *self) {
  return self->count();
}

//  int QQuickStackLayout::currentIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickStackLayout12currentIndexEv(
    const QQuickStackLayout *self) {
  return self->currentIndex();
}

//  void QQuickStackLayout::setCurrentIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout15setCurrentIndexEi(
    QQuickStackLayout *self,
    int index) {
  self->setCurrentIndex(index);
}

//  void QQuickStackLayout::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout17componentCompleteEv(
    QQuickStackLayout *self) {
  self->componentComplete();
}

//  void QQuickStackLayout::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickStackLayout *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  QSizeF QQuickStackLayout::sizeHint(Qt::SizeHint whichSizeHint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK17QQuickStackLayout8sizeHintEN2Qt8SizeHintE(
    const QQuickStackLayout *self,
    Qt::SizeHint whichSizeHint) {
  return new QSizeF(self->sizeHint(whichSizeHint));
}

//  void QQuickStackLayout::setAlignment(QQuickItem *item, Qt::Alignment
//      align)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout12setAlignmentEP10QQuickItem6QFlagsIN2Qt13AlignmentFlagEE(
    QQuickStackLayout *self,
    QQuickItem *item,
    int align) {
  self->setAlignment(item, QFlags<Qt::AlignmentFlag>::fromInt(align));
}

//  void QQuickStackLayout::invalidate(QQuickItem *childItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout10invalidateEP10QQuickItem(
    QQuickStackLayout *self,
    QQuickItem *childItem) {
  self->invalidate(childItem);
}

//  void QQuickStackLayout::updateLayoutItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout17updateLayoutItemsEv(
    QQuickStackLayout *self) {
  self->updateLayoutItems();
}

//  void QQuickStackLayout::rearrange(const QSizeF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout9rearrangeERK6QSizeF(
    QQuickStackLayout *self,
    const QSizeF *a0) {
  self->rearrange(*a0);
}

//  void QQuickStackLayout::setStretchFactor(QQuickItem *item, int
//      stretchFactor, Qt::Orientation orient)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout16setStretchFactorEP10QQuickItemiN2Qt11OrientationE(
    QQuickStackLayout *self,
    QQuickItem *item,
    int stretchFactor,
    Qt::Orientation orient) {
  self->setStretchFactor(item, stretchFactor, orient);
}

//  QQuickItem *QQuickStackLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK17QQuickStackLayout6itemAtEi(
    const QQuickStackLayout *self,
    int index) {
  return self->itemAt(index);
}

//  int QQuickStackLayout::itemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickStackLayout9itemCountEv(
    const QQuickStackLayout *self) {
  return self->itemCount();
}

//  int QQuickStackLayout::indexOf(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickStackLayout7indexOfEP10QQuickItem(
    const QQuickStackLayout *self,
    QQuickItem *item) {
  return self->indexOf(item);
}

//  void QQuickStackLayout::itemSiblingOrderChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout23itemSiblingOrderChangedEP10QQuickItem(
    QQuickStackLayout *self,
    QQuickItem *item) {
  self->itemSiblingOrderChanged(item);
}

//  QQuickStackLayoutAttached
//      *QQuickStackLayout::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickStackLayoutAttached *ritual_ZN17QQuickStackLayout21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickStackLayout::qmlAttachedProperties(object);
}

//  void QQuickStackLayout::currentIndexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout19currentIndexChangedEv(
    QQuickStackLayout *self) {
  self->currentIndexChanged();
}

//  void QQuickStackLayout::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout12countChangedEv(QQuickStackLayout *self) {
  self->countChanged();
}

//  void QQuickStackLayout::collectItemSizeHints(QQuickItem *item, QSizeF
//      *sizeHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout20collectItemSizeHintsEP10QQuickItemP6QSizeF(
    QQuickItem *item,
    QSizeF *sizeHints) {
  QQuickStackLayout::collectItemSizeHints(item, sizeHints);
}

//  bool QQuickStackLayout::shouldIgnoreItem(QQuickItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickStackLayout16shouldIgnoreItemEP10QQuickItem(
    const QQuickStackLayout *self,
    QQuickItem *item) {
  return self->shouldIgnoreItem(item);
}

//  void QQuickStackLayout::childItemsChanged(AdjustCurrentIndexPolicy
//      adjustCurrentIndexPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStackLayout17childItemsChangedENS_24AdjustCurrentIndexPolicyE(
    QQuickStackLayout *self,
    QQuickStackLayout::AdjustCurrentIndexPolicy adjustCurrentIndexPolicy) {
  self->childItemsChanged(adjustCurrentIndexPolicy);
}

//  QQuickStackLayoutPrivate *QQuickStackLayout::d_func()
extern "C" Q_DECL_EXPORT
QQuickStackLayoutPrivate *ritual_ZN17QQuickStackLayout6d_funcEv(
    QQuickStackLayout *self) {
  return self->d_func();
}

//  const QQuickStackLayoutPrivate *QQuickStackLayout::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickStackLayoutPrivate *ritual_ZNK17QQuickStackLayout6d_funcEv(
    const QQuickStackLayout *self) {
  return self->d_func();
}

//  SizeHints &QQuickStackLayout::cachedItemSizeHints(int index) const
extern "C" Q_DECL_EXPORT
QQuickStackLayout::SizeHints *ritual_ZNK17QQuickStackLayout19cachedItemSizeHintsEi(
    const QQuickStackLayout *self,
    int index) {
  return &(self->cachedItemSizeHints(index));
}

//  void QQuickStackLayout::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickStackLayout17componentCompleteEv(
    QQuickStackLayout *self) {
  self->QQuickStackLayout::componentComplete();
}

//  void QQuickStackLayout::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickStackLayout10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickStackLayout *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->QQuickStackLayout::itemChange(change, *value);
}

//  QSizeF QQuickStackLayout::sizeHint(Qt::SizeHint whichSizeHint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK17QQuickStackLayout8sizeHintEN2Qt8SizeHintE(
    const QQuickStackLayout *self,
    Qt::SizeHint whichSizeHint) {
  return new QSizeF(self->QQuickStackLayout::sizeHint(whichSizeHint));
}

//  void QQuickStackLayout::setAlignment(QQuickItem *item, Qt::Alignment
//      align)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickStackLayout12setAlignmentEP10QQuickItem6QFlagsIN2Qt13AlignmentFlagEE(
    QQuickStackLayout *self,
    QQuickItem *item,
    int align) {
  self->QQuickStackLayout::setAlignment(
      item,
      QFlags<Qt::AlignmentFlag>::fromInt(align));
}

//  void QQuickStackLayout::invalidate(QQuickItem *childItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickStackLayout10invalidateEP10QQuickItem(
    QQuickStackLayout *self,
    QQuickItem *childItem) {
  self->QQuickStackLayout::invalidate(childItem);
}

//  void QQuickStackLayout::updateLayoutItems()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickStackLayout17updateLayoutItemsEv(
    QQuickStackLayout *self) {
  self->QQuickStackLayout::updateLayoutItems();
}

//  void QQuickStackLayout::rearrange(const QSizeF &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickStackLayout9rearrangeERK6QSizeF(
    QQuickStackLayout *self,
    const QSizeF *a0) {
  self->QQuickStackLayout::rearrange(*a0);
}

//  void QQuickStackLayout::setStretchFactor(QQuickItem *item, int
//      stretchFactor, Qt::Orientation orient)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickStackLayout16setStretchFactorEP10QQuickItemiN2Qt11OrientationE(
    QQuickStackLayout *self,
    QQuickItem *item,
    int stretchFactor,
    Qt::Orientation orient) {
  self->QQuickStackLayout::setStretchFactor(item, stretchFactor, orient);
}

//  QQuickItem *QQuickStackLayout::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_own_ZNK17QQuickStackLayout6itemAtEi(
    const QQuickStackLayout *self,
    int index) {
  return self->QQuickStackLayout::itemAt(index);
}

//  int QQuickStackLayout::itemCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QQuickStackLayout9itemCountEv(
    const QQuickStackLayout *self) {
  return self->QQuickStackLayout::itemCount();
}

//  void QQuickStackLayout::itemSiblingOrderChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickStackLayout23itemSiblingOrderChangedEP10QQuickItem(
    QQuickStackLayout *self,
    QQuickItem *item) {
  self->QQuickStackLayout::itemSiblingOrderChanged(item);
}
