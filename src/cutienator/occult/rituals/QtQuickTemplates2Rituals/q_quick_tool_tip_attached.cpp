//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktooltip_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktooltip_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickToolTipAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickToolTipAttached10metaObjectEv(
    const QQuickToolTipAttached *self) {
  return self->metaObject();
}

//  QString QQuickToolTipAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickToolTipAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickToolTipAttached::tr(s, c, n));
}

//  void QQuickToolTipAttached::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached22qt_qmlMarker_anonymousEv(
    QQuickToolTipAttached *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickToolTipAttached::QQuickToolTipAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickToolTipAttached *ritual_ZN21QQuickToolTipAttachedC1EP7QObject(
    QObject *parent) {
  return new QQuickToolTipAttached(parent);
}

//  QString QQuickToolTipAttached::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QQuickToolTipAttached4textEv(
    const QQuickToolTipAttached *self) {
  return new QString(self->text());
}

//  void QQuickToolTipAttached::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached7setTextERK7QString(
    QQuickToolTipAttached *self,
    const QString *text) {
  self->setText(*text);
}

//  int QQuickToolTipAttached::delay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickToolTipAttached5delayEv(
    const QQuickToolTipAttached *self) {
  return self->delay();
}

//  void QQuickToolTipAttached::setDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached8setDelayEi(
    QQuickToolTipAttached *self,
    int delay) {
  self->setDelay(delay);
}

//  int QQuickToolTipAttached::timeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickToolTipAttached7timeoutEv(
    const QQuickToolTipAttached *self) {
  return self->timeout();
}

//  void QQuickToolTipAttached::setTimeout(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached10setTimeoutEi(
    QQuickToolTipAttached *self,
    int timeout) {
  self->setTimeout(timeout);
}

//  bool QQuickToolTipAttached::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickToolTipAttached9isVisibleEv(
    const QQuickToolTipAttached *self) {
  return self->isVisible();
}

//  void QQuickToolTipAttached::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached10setVisibleEb(
    QQuickToolTipAttached *self,
    bool visible) {
  self->setVisible(visible);
}

//  QQuickToolTip *QQuickToolTipAttached::toolTip() const
extern "C" Q_DECL_EXPORT
QQuickToolTip *ritual_ZNK21QQuickToolTipAttached7toolTipEv(
    const QQuickToolTipAttached *self) {
  return self->toolTip();
}

//  QQuickToolTip::Policy QQuickToolTipAttached::policy() const
extern "C" Q_DECL_EXPORT
QQuickToolTip::Policy ritual_ZNK21QQuickToolTipAttached6policyEv(
    const QQuickToolTipAttached *self) {
  return self->policy();
}

//  void QQuickToolTipAttached::setVisiblePolicy(QQuickToolTip::Policy
//      policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached16setVisiblePolicyEN13QQuickToolTip6PolicyE(
    QQuickToolTipAttached *self,
    QQuickToolTip::Policy policy) {
  self->setVisiblePolicy(policy);
}

//  void QQuickToolTipAttached::resetVisiblePolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached18resetVisiblePolicyEv(
    QQuickToolTipAttached *self) {
  self->resetVisiblePolicy();
}

//  void QQuickToolTipAttached::show(const QString &text, int ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached4showERK7QStringi(
    QQuickToolTipAttached *self,
    const QString *text,
    int ms) {
  self->show(*text, ms);
}

//  void QQuickToolTipAttached::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached4hideEv(QQuickToolTipAttached *self) {
  self->hide();
}

//  void QQuickToolTipAttached::attachedParentChange(QQuickAttachedPropertyPr
//      opagator *newParent, QQuickAttachedPropertyPropagator *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached20attachedParentChangeEPN9QtPrivate32QQuickAttachedPropertyPropagatorES2_(
    QQuickToolTipAttached *self,
    QtPrivate::QQuickAttachedPropertyPropagator *newParent,
    QtPrivate::QQuickAttachedPropertyPropagator *oldParent) {
  self->attachedParentChange(newParent, oldParent);
}

//  void QQuickToolTipAttached::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached10classBeginEv(
    QQuickToolTipAttached *self) {
  self->classBegin();
}

//  void QQuickToolTipAttached::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickToolTipAttached17componentCompleteEv(
    QQuickToolTipAttached *self) {
  self->componentComplete();
}

//  QQuickToolTipAttachedPrivate *QQuickToolTipAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickToolTipAttachedPrivate *ritual_ZN21QQuickToolTipAttached6d_funcEv(
    QQuickToolTipAttached *self) {
  return self->d_func();
}

//  const QQuickToolTipAttachedPrivate *QQuickToolTipAttached::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickToolTipAttachedPrivate *ritual_ZNK21QQuickToolTipAttached6d_funcEv(
    const QQuickToolTipAttached *self) {
  return self->d_func();
}

//  QQuickToolTipAttached as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickToolTipAttached_QQmlParserStatus(
    QQuickToolTipAttached *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QQuickToolTipAttached::attachedParentChange(QQuickAttachedPropertyPr
//      opagator *newParent, QQuickAttachedPropertyPropagator *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickToolTipAttached20attachedParentChangeEPN9QtPrivate32QQuickAttachedPropertyPropagatorES2_(
    QQuickToolTipAttached *self,
    QtPrivate::QQuickAttachedPropertyPropagator *newParent,
    QtPrivate::QQuickAttachedPropertyPropagator *oldParent) {
  self->QQuickToolTipAttached::attachedParentChange(newParent, oldParent);
}

//  void QQuickToolTipAttached::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickToolTipAttached10classBeginEv(
    QQuickToolTipAttached *self) {
  self->QQuickToolTipAttached::classBegin();
}

//  void QQuickToolTipAttached::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickToolTipAttached17componentCompleteEv(
    QQuickToolTipAttached *self) {
  self->QQuickToolTipAttached::componentComplete();
}
