//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickselectionrectangle_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickselectionrectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickSelectionRectangleAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuickSelectionRectangleAttached10metaObjectEv(
    const QQuickSelectionRectangleAttached *self) {
  return self->metaObject();
}

//  void *QQuickSelectionRectangleAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QQuickSelectionRectangleAttached11qt_metacastEPKc(
    QQuickSelectionRectangleAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSelectionRectangleAttached::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QQuickSelectionRectangleAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSelectionRectangleAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSelectionRectangleAttached::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QQuickSelectionRectangleAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSelectionRectangleAttached::tr(s, c, n));
}

//  QQuickSelectionRectangleAttached::QQuickSelectionRectangleAttached(QObjec
//      t *parent)
extern "C" Q_DECL_EXPORT
QQuickSelectionRectangleAttached *ritual_ZN32QQuickSelectionRectangleAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickSelectionRectangleAttached(parent);
}

//  QQuickSelectionRectangle *QQuickSelectionRectangleAttached::control()
//      const
extern "C" Q_DECL_EXPORT
QQuickSelectionRectangle *ritual_ZNK32QQuickSelectionRectangleAttached7controlEv(
    const QQuickSelectionRectangleAttached *self) {
  return self->control();
}

//  void
//      QQuickSelectionRectangleAttached::setControl(QQuickSelectionRectangle
//      *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickSelectionRectangleAttached10setControlEP24QQuickSelectionRectangle(
    QQuickSelectionRectangleAttached *self,
    QQuickSelectionRectangle *control) {
  self->setControl(control);
}

//  bool QQuickSelectionRectangleAttached::dragging() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickSelectionRectangleAttached8draggingEv(
    const QQuickSelectionRectangleAttached *self) {
  return self->dragging();
}

//  void QQuickSelectionRectangleAttached::setDragging(bool dragging)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickSelectionRectangleAttached11setDraggingEb(
    QQuickSelectionRectangleAttached *self,
    bool dragging) {
  self->setDragging(dragging);
}

//  void QQuickSelectionRectangleAttached::controlChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickSelectionRectangleAttached14controlChangedEv(
    QQuickSelectionRectangleAttached *self) {
  self->controlChanged();
}

//  void QQuickSelectionRectangleAttached::draggingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickSelectionRectangleAttached15draggingChangedEv(
    QQuickSelectionRectangleAttached *self) {
  self->draggingChanged();
}

#endif  // QT_CONFIG(quick_tableview)
