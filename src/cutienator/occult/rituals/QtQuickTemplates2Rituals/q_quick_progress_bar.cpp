//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickprogressbar_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickprogressbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickProgressBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickProgressBar : QQuickProgressBar {
  using QQuickProgressBar::mirrorChange;
  using QQuickProgressBar::componentComplete;
  using QQuickProgressBar::accessibleRole;
};

//  const QMetaObject *QQuickProgressBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickProgressBar10metaObjectEv(
    const QQuickProgressBar *self) {
  return self->metaObject();
}

//  QString QQuickProgressBar::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickProgressBar2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickProgressBar::tr(s, c, n));
}

//  QQuickProgressBar::QQuickProgressBar(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickProgressBar *ritual_ZN17QQuickProgressBarC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickProgressBar(parent);
}

//  qreal QQuickProgressBar::from() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickProgressBar4fromEv(const QQuickProgressBar *self) {
  return self->from();
}

//  void QQuickProgressBar::setFrom(qreal from)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickProgressBar7setFromEd(
    QQuickProgressBar *self,
    qreal from) {
  self->setFrom(from);
}

//  qreal QQuickProgressBar::to() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickProgressBar2toEv(const QQuickProgressBar *self) {
  return self->to();
}

//  void QQuickProgressBar::setTo(qreal to)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickProgressBar5setToEd(
    QQuickProgressBar *self,
    qreal to) {
  self->setTo(to);
}

//  qreal QQuickProgressBar::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickProgressBar5valueEv(const QQuickProgressBar *self) {
  return self->value();
}

//  void QQuickProgressBar::setValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickProgressBar8setValueEd(
    QQuickProgressBar *self,
    qreal value) {
  self->setValue(value);
}

//  qreal QQuickProgressBar::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickProgressBar8positionEv(
    const QQuickProgressBar *self) {
  return self->position();
}

//  qreal QQuickProgressBar::visualPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickProgressBar14visualPositionEv(
    const QQuickProgressBar *self) {
  return self->visualPosition();
}

//  bool QQuickProgressBar::isIndeterminate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickProgressBar15isIndeterminateEv(
    const QQuickProgressBar *self) {
  return self->isIndeterminate();
}

//  void QQuickProgressBar::setIndeterminate(bool indeterminate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickProgressBar16setIndeterminateEb(
    QQuickProgressBar *self,
    bool indeterminate) {
  self->setIndeterminate(indeterminate);
}

//  void QQuickProgressBar::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickProgressBar12mirrorChangeEv(QQuickProgressBar *self) {
  self->mirrorChange();
}

//  void QQuickProgressBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickProgressBar17componentCompleteEv(
    QQuickProgressBar *self) {
  self->componentComplete();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickProgressBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK17QQuickProgressBar14accessibleRoleEv(
    const QQuickProgressBar *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickProgressBar::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickProgressBar12mirrorChangeEv(
    QQuickProgressBar *self) {
  static_cast<OwnQQuickProgressBar *>(self)->OwnQQuickProgressBar::mirrorChange();
}

//  void QQuickProgressBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickProgressBar17componentCompleteEv(
    QQuickProgressBar *self) {
  static_cast<OwnQQuickProgressBar *>(self)->OwnQQuickProgressBar::componentComplete();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickProgressBar::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK17QQuickProgressBar14accessibleRoleEv(
    const QQuickProgressBar *self) {
  return static_cast<const OwnQQuickProgressBar *>(self)->OwnQQuickProgressBar::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
