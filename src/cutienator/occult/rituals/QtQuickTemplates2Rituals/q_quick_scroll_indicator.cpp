//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickscrollindicator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollindicator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickScrollIndicator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickScrollIndicator : QQuickScrollIndicator {
  using QQuickScrollIndicator::touchEvent;
  using QQuickScrollIndicator::accessibleRole;
};

//  const QMetaObject *QQuickScrollIndicator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickScrollIndicator10metaObjectEv(
    const QQuickScrollIndicator *self) {
  return self->metaObject();
}

//  QString QQuickScrollIndicator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickScrollIndicator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScrollIndicator::tr(s, c, n));
}

//  void QQuickScrollIndicator::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickScrollIndicator21qt_qmlMarker_attachedEv(
    QQuickScrollIndicator *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickScrollIndicator::QQuickScrollIndicator(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickScrollIndicator *ritual_ZN21QQuickScrollIndicatorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickScrollIndicator(parent);
}

//  QQuickScrollIndicatorAttached
//      *QQuickScrollIndicator::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickScrollIndicatorAttached *ritual_ZN21QQuickScrollIndicator21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickScrollIndicator::qmlAttachedProperties(object);
}

//  qreal QQuickScrollIndicator::size() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickScrollIndicator4sizeEv(
    const QQuickScrollIndicator *self) {
  return self->size();
}

//  qreal QQuickScrollIndicator::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickScrollIndicator8positionEv(
    const QQuickScrollIndicator *self) {
  return self->position();
}

//  bool QQuickScrollIndicator::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickScrollIndicator8isActiveEv(
    const QQuickScrollIndicator *self) {
  return self->isActive();
}

//  void QQuickScrollIndicator::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickScrollIndicator9setActiveEb(
    QQuickScrollIndicator *self,
    bool active) {
  self->setActive(active);
}

//  Qt::Orientation QQuickScrollIndicator::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK21QQuickScrollIndicator11orientationEv(
    const QQuickScrollIndicator *self) {
  return self->orientation();
}

//  void QQuickScrollIndicator::setOrientation(Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickScrollIndicator14setOrientationEN2Qt11OrientationE(
    QQuickScrollIndicator *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  bool QQuickScrollIndicator::isHorizontal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickScrollIndicator12isHorizontalEv(
    const QQuickScrollIndicator *self) {
  return self->isHorizontal();
}

//  bool QQuickScrollIndicator::isVertical() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickScrollIndicator10isVerticalEv(
    const QQuickScrollIndicator *self) {
  return self->isVertical();
}

//  qreal QQuickScrollIndicator::minimumSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickScrollIndicator11minimumSizeEv(
    const QQuickScrollIndicator *self) {
  return self->minimumSize();
}

//  void QQuickScrollIndicator::setMinimumSize(qreal minimumSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickScrollIndicator14setMinimumSizeEd(
    QQuickScrollIndicator *self,
    qreal minimumSize) {
  self->setMinimumSize(minimumSize);
}

//  qreal QQuickScrollIndicator::visualSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickScrollIndicator10visualSizeEv(
    const QQuickScrollIndicator *self) {
  return self->visualSize();
}

//  qreal QQuickScrollIndicator::visualPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickScrollIndicator14visualPositionEv(
    const QQuickScrollIndicator *self) {
  return self->visualPosition();
}

//  void QQuickScrollIndicator::setSize(qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickScrollIndicator7setSizeEd(
    QQuickScrollIndicator *self,
    qreal size) {
  self->setSize(size);
}

//  void QQuickScrollIndicator::setPosition(qreal position)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickScrollIndicator11setPositionEd(
    QQuickScrollIndicator *self,
    qreal position) {
  self->setPosition(position);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickScrollIndicator::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickScrollIndicator10touchEventEP11QTouchEvent(
    QQuickScrollIndicator *self,
    QTouchEvent *event) {
  self->touchEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickScrollIndicator::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK21QQuickScrollIndicator14accessibleRoleEv(
    const QQuickScrollIndicator *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(quicktemplates2_multitouch)
//  void QQuickScrollIndicator::touchEvent(QTouchEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickScrollIndicator10touchEventEP11QTouchEvent(
    QQuickScrollIndicator *self,
    QTouchEvent *event) {
  static_cast<OwnQQuickScrollIndicator *>(self)->OwnQQuickScrollIndicator::touchEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickScrollIndicator::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK21QQuickScrollIndicator14accessibleRoleEv(
    const QQuickScrollIndicator *self) {
  return static_cast<const OwnQQuickScrollIndicator *>(self)->OwnQQuickScrollIndicator::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
