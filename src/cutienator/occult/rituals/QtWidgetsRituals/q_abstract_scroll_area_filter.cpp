//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QAbstractScrollAreaFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QAbstractScrollAreaFilter10metaObjectEv(
    const QAbstractScrollAreaFilter *self) {
  return self->metaObject();
}

//  void *QAbstractScrollAreaFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QAbstractScrollAreaFilter11qt_metacastEPKc(
    QAbstractScrollAreaFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractScrollAreaFilter::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QAbstractScrollAreaFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractScrollAreaFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

#endif  // QT_CONFIG(scrollarea)
