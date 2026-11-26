//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickflexboxlayout_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickLayouts/qtquicklayoutsexports.h>
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#if !defined(Q_OS_INTEGRITY)
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickflexboxlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickFlexboxLayoutAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickFlexboxLayoutAttached10metaObjectEv(
    const QQuickFlexboxLayoutAttached *self) {
  return self->metaObject();
}

//  void *QQuickFlexboxLayoutAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQuickFlexboxLayoutAttached11qt_metacastEPKc(
    QQuickFlexboxLayoutAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFlexboxLayoutAttached::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQuickFlexboxLayoutAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFlexboxLayoutAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFlexboxLayoutAttached::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQuickFlexboxLayoutAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFlexboxLayoutAttached::tr(s, c, n));
}

//  QQuickFlexboxLayoutAttached::QQuickFlexboxLayoutAttached(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickFlexboxLayoutAttached *ritual_ZN27QQuickFlexboxLayoutAttachedC1EP7QObject(
    QObject *object) {
  return new QQuickFlexboxLayoutAttached(object);
}

//  QQuickFlexboxLayout::FlexboxAlignment
//      QQuickFlexboxLayoutAttached::alignSelf() const
extern "C" Q_DECL_EXPORT
QQuickFlexboxLayout::FlexboxAlignment ritual_ZNK27QQuickFlexboxLayoutAttached9alignSelfEv(
    const QQuickFlexboxLayoutAttached *self) {
  return self->alignSelf();
}

//  void QQuickFlexboxLayoutAttached::setAlignSelf(const
//      QQuickFlexboxLayout::FlexboxAlignment a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFlexboxLayoutAttached12setAlignSelfEN19QQuickFlexboxLayout16FlexboxAlignmentE(
    QQuickFlexboxLayoutAttached *self,
    const QQuickFlexboxLayout::FlexboxAlignment *a0) {
  self->setAlignSelf(*a0);
}

//  void QQuickFlexboxLayoutAttached::alignSelfChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFlexboxLayoutAttached16alignSelfChangedEv(
    QQuickFlexboxLayoutAttached *self) {
  self->alignSelfChanged();
}

#endif  // !defined(Q_OS_INTEGRITY)
