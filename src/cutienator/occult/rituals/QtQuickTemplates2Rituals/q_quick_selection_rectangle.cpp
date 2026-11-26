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

//  const QMetaObject *QQuickSelectionRectangle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickSelectionRectangle10metaObjectEv(
    const QQuickSelectionRectangle *self) {
  return self->metaObject();
}

//  void *QQuickSelectionRectangle::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuickSelectionRectangle11qt_metacastEPKc(
    QQuickSelectionRectangle *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSelectionRectangle::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickSelectionRectangle11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSelectionRectangle *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSelectionRectangle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickSelectionRectangle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSelectionRectangle::tr(s, c, n));
}

//  void QQuickSelectionRectangle::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle21qt_qmlMarker_attachedEv(
    QQuickSelectionRectangle *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickSelectionRectangle::QQuickSelectionRectangle(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSelectionRectangle *ritual_ZN24QQuickSelectionRectangleC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickSelectionRectangle(parent);
}

//  QQuickItem *QQuickSelectionRectangle::target() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK24QQuickSelectionRectangle6targetEv(
    const QQuickSelectionRectangle *self) {
  return self->target();
}

//  void QQuickSelectionRectangle::setTarget(QQuickItem *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle9setTargetEP10QQuickItem(
    QQuickSelectionRectangle *self,
    QQuickItem *target) {
  self->setTarget(target);
}

//  bool QQuickSelectionRectangle::active()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickSelectionRectangle6activeEv(
    QQuickSelectionRectangle *self) {
  return self->active();
}

//  bool QQuickSelectionRectangle::dragging()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickSelectionRectangle8draggingEv(
    QQuickSelectionRectangle *self) {
  return self->dragging();
}

//  SelectionMode QQuickSelectionRectangle::selectionMode() const
extern "C" Q_DECL_EXPORT
QQuickSelectionRectangle::SelectionMode ritual_ZNK24QQuickSelectionRectangle13selectionModeEv(
    const QQuickSelectionRectangle *self) {
  return self->selectionMode();
}

//  void QQuickSelectionRectangle::setSelectionMode(SelectionMode
//      selectionMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle16setSelectionModeENS_13SelectionModeE(
    QQuickSelectionRectangle *self,
    QQuickSelectionRectangle::SelectionMode selectionMode) {
  self->setSelectionMode(selectionMode);
}

//  QQmlComponent *QQuickSelectionRectangle::topLeftHandle() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK24QQuickSelectionRectangle13topLeftHandleEv(
    const QQuickSelectionRectangle *self) {
  return self->topLeftHandle();
}

//  void QQuickSelectionRectangle::setTopLeftHandle(QQmlComponent
//      *topLeftHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle16setTopLeftHandleEP13QQmlComponent(
    QQuickSelectionRectangle *self,
    QQmlComponent *topLeftHandle) {
  self->setTopLeftHandle(topLeftHandle);
}

//  QQmlComponent *QQuickSelectionRectangle::bottomRightHandle() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK24QQuickSelectionRectangle17bottomRightHandleEv(
    const QQuickSelectionRectangle *self) {
  return self->bottomRightHandle();
}

//  void QQuickSelectionRectangle::setBottomRightHandle(QQmlComponent
//      *bottomRightHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle20setBottomRightHandleEP13QQmlComponent(
    QQuickSelectionRectangle *self,
    QQmlComponent *bottomRightHandle) {
  self->setBottomRightHandle(bottomRightHandle);
}

//  QQuickSelectionRectangleAttached
//      *QQuickSelectionRectangle::qmlAttachedProperties(QObject *obj)
extern "C" Q_DECL_EXPORT
QQuickSelectionRectangleAttached *ritual_ZN24QQuickSelectionRectangle21qmlAttachedPropertiesEP7QObject(
    QObject *obj) {
  return QQuickSelectionRectangle::qmlAttachedProperties(obj);
}

//  void QQuickSelectionRectangle::targetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle13targetChangedEv(
    QQuickSelectionRectangle *self) {
  self->targetChanged();
}

//  void QQuickSelectionRectangle::activeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle13activeChangedEv(
    QQuickSelectionRectangle *self) {
  self->activeChanged();
}

//  void QQuickSelectionRectangle::draggingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle15draggingChangedEv(
    QQuickSelectionRectangle *self) {
  self->draggingChanged();
}

//  void QQuickSelectionRectangle::topLeftHandleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle20topLeftHandleChangedEv(
    QQuickSelectionRectangle *self) {
  self->topLeftHandleChanged();
}

//  void QQuickSelectionRectangle::bottomRightHandleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle24bottomRightHandleChangedEv(
    QQuickSelectionRectangle *self) {
  self->bottomRightHandleChanged();
}

//  void QQuickSelectionRectangle::selectionModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSelectionRectangle20selectionModeChangedEv(
    QQuickSelectionRectangle *self) {
  self->selectionModeChanged();
}

//  QQuickSelectionRectanglePrivate *QQuickSelectionRectangle::d_func()
extern "C" Q_DECL_EXPORT
QQuickSelectionRectanglePrivate *ritual_ZN24QQuickSelectionRectangle6d_funcEv(
    QQuickSelectionRectangle *self) {
  return self->d_func();
}

//  const QQuickSelectionRectanglePrivate *QQuickSelectionRectangle::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickSelectionRectanglePrivate *ritual_ZNK24QQuickSelectionRectangle6d_funcEv(
    const QQuickSelectionRectangle *self) {
  return self->d_func();
}

#endif  // QT_CONFIG(quick_tableview)
