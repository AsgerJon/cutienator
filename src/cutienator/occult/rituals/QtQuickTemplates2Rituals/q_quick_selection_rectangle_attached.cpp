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

#endif  // QT_CONFIG(quick_tableview)
