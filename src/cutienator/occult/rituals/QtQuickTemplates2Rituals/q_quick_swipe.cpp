//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipe_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickSwipe::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickSwipe10metaObjectEv(
    const QQuickSwipe *self) {
  return self->metaObject();
}

//  QString QQuickSwipe::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickSwipe2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSwipe::tr(s, c, n));
}

//  void QQuickSwipe::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe22qt_qmlMarker_anonymousEv(QQuickSwipe *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickSwipe::QQuickSwipe(QQuickSwipeDelegate *control)
extern "C" Q_DECL_EXPORT
QQuickSwipe *ritual_ZN11QQuickSwipeC1EP19QQuickSwipeDelegate(
    QQuickSwipeDelegate *control) {
  return new QQuickSwipe(control);
}

//  qreal QQuickSwipe::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QQuickSwipe8positionEv(const QQuickSwipe *self) {
  return self->position();
}

//  void QQuickSwipe::setPosition(qreal position)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe11setPositionEd(
    QQuickSwipe *self,
    qreal position) {
  self->setPosition(position);
}

//  bool QQuickSwipe::isComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickSwipe10isCompleteEv(const QQuickSwipe *self) {
  return self->isComplete();
}

//  void QQuickSwipe::setComplete(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe11setCompleteEb(
    QQuickSwipe *self,
    bool complete) {
  self->setComplete(complete);
}

//  QQmlComponent *QQuickSwipe::left() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK11QQuickSwipe4leftEv(const QQuickSwipe *self) {
  return self->left();
}

//  void QQuickSwipe::setLeft(QQmlComponent *left)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe7setLeftEP13QQmlComponent(
    QQuickSwipe *self,
    QQmlComponent *left) {
  self->setLeft(left);
}

//  QQmlComponent *QQuickSwipe::behind() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK11QQuickSwipe6behindEv(const QQuickSwipe *self) {
  return self->behind();
}

//  void QQuickSwipe::setBehind(QQmlComponent *behind)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe9setBehindEP13QQmlComponent(
    QQuickSwipe *self,
    QQmlComponent *behind) {
  self->setBehind(behind);
}

//  QQmlComponent *QQuickSwipe::right() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK11QQuickSwipe5rightEv(const QQuickSwipe *self) {
  return self->right();
}

//  void QQuickSwipe::setRight(QQmlComponent *right)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe8setRightEP13QQmlComponent(
    QQuickSwipe *self,
    QQmlComponent *right) {
  self->setRight(right);
}

//  QQuickItem *QQuickSwipe::leftItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickSwipe8leftItemEv(const QQuickSwipe *self) {
  return self->leftItem();
}

//  void QQuickSwipe::setLeftItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe11setLeftItemEP10QQuickItem(
    QQuickSwipe *self,
    QQuickItem *item) {
  self->setLeftItem(item);
}

//  QQuickItem *QQuickSwipe::behindItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickSwipe10behindItemEv(const QQuickSwipe *self) {
  return self->behindItem();
}

//  void QQuickSwipe::setBehindItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe13setBehindItemEP10QQuickItem(
    QQuickSwipe *self,
    QQuickItem *item) {
  self->setBehindItem(item);
}

//  QQuickItem *QQuickSwipe::rightItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK11QQuickSwipe9rightItemEv(const QQuickSwipe *self) {
  return self->rightItem();
}

//  void QQuickSwipe::setRightItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe12setRightItemEP10QQuickItem(
    QQuickSwipe *self,
    QQuickItem *item) {
  self->setRightItem(item);
}

//  void QQuickSwipe::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe5closeEv(QQuickSwipe *self) {
  self->close();
}

//  bool QQuickSwipe::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickSwipe9isEnabledEv(const QQuickSwipe *self) {
  return self->isEnabled();
}

//  void QQuickSwipe::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe10setEnabledEb(QQuickSwipe *self, bool enabled) {
  self->setEnabled(enabled);
}

//  QQuickTransition *QQuickSwipe::transition() const
extern "C" Q_DECL_EXPORT
QQuickTransition *ritual_ZNK11QQuickSwipe10transitionEv(
    const QQuickSwipe *self) {
  return self->transition();
}

//  void QQuickSwipe::setTransition(QQuickTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe13setTransitionEP16QQuickTransition(
    QQuickSwipe *self,
    QQuickTransition *transition) {
  self->setTransition(transition);
}

//  void QQuickSwipe::open(QQuickSwipeDelegate::Side side)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickSwipe4openEN19QQuickSwipeDelegate4SideE(
    QQuickSwipe *self,
    QQuickSwipeDelegate::Side side) {
  self->open(side);
}
