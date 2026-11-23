//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h>

//  const QMetaObject *QAbstractScrollAreaFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QAbstractScrollAreaFilter10metaObjectEv(
    const QAbstractScrollAreaFilter *self) {
  return self->metaObject();
}

//  bool QAbstractScrollAreaFilter::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAbstractScrollAreaFilter11eventFilterEP7QObjectP6QEvent(
    QAbstractScrollAreaFilter *self,
    QObject *o,
    QEvent *e) {
  return self->eventFilter(o, e);
}

//  bool QAbstractScrollAreaFilter::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QAbstractScrollAreaFilter11eventFilterEP7QObjectP6QEvent(
    QAbstractScrollAreaFilter *self,
    QObject *o,
    QEvent *e) {
  return self->QAbstractScrollAreaFilter::eventFilter(o, e);
}
