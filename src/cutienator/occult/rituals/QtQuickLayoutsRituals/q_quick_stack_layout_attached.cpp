//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickstacklayout_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickstacklayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickStackLayoutAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickStackLayoutAttached10metaObjectEv(
    const QQuickStackLayoutAttached *self) {
  return self->metaObject();
}

//  QString QQuickStackLayoutAttached::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQuickStackLayoutAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStackLayoutAttached::tr(s, c, n));
}

//  QQuickStackLayoutAttached::QQuickStackLayoutAttached(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickStackLayoutAttached *ritual_ZN25QQuickStackLayoutAttachedC1EP7QObject(
    QObject *object) {
  return new QQuickStackLayoutAttached(object);
}

//  int QQuickStackLayoutAttached::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQuickStackLayoutAttached5indexEv(
    const QQuickStackLayoutAttached *self) {
  return self->index();
}

//  void QQuickStackLayoutAttached::setIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickStackLayoutAttached8setIndexEi(
    QQuickStackLayoutAttached *self,
    int index) {
  self->setIndex(index);
}

//  bool QQuickStackLayoutAttached::isCurrentItem() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickStackLayoutAttached13isCurrentItemEv(
    const QQuickStackLayoutAttached *self) {
  return self->isCurrentItem();
}

//  void QQuickStackLayoutAttached::setIsCurrentItem(bool isCurrentItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickStackLayoutAttached16setIsCurrentItemEb(
    QQuickStackLayoutAttached *self,
    bool isCurrentItem) {
  self->setIsCurrentItem(isCurrentItem);
}

//  QQuickStackLayout *QQuickStackLayoutAttached::layout() const
extern "C" Q_DECL_EXPORT
QQuickStackLayout *ritual_ZNK25QQuickStackLayoutAttached6layoutEv(
    const QQuickStackLayoutAttached *self) {
  return self->layout();
}

//  void QQuickStackLayoutAttached::setLayout(QQuickStackLayout *layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickStackLayoutAttached9setLayoutEP17QQuickStackLayout(
    QQuickStackLayoutAttached *self,
    QQuickStackLayout *layout) {
  self->setLayout(layout);
}
