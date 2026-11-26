//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickroundbutton_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickroundbutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  Only a class built on QQuickRoundButton may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRoundButton : QQuickRoundButton {
  using QQuickRoundButton::geometryChange;
};

//  const QMetaObject *QQuickRoundButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickRoundButton10metaObjectEv(
    const QQuickRoundButton *self) {
  return self->metaObject();
}

//  void *QQuickRoundButton::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickRoundButton11qt_metacastEPKc(
    QQuickRoundButton *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickRoundButton::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickRoundButton11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickRoundButton *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickRoundButton::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickRoundButton2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRoundButton::tr(s, c, n));
}

//  QQuickRoundButton::QQuickRoundButton(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRoundButton *ritual_ZN17QQuickRoundButtonC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickRoundButton(parent);
}

//  qreal QQuickRoundButton::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickRoundButton6radiusEv(const QQuickRoundButton *self) {
  return self->radius();
}

//  void QQuickRoundButton::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRoundButton9setRadiusEd(
    QQuickRoundButton *self,
    qreal radius) {
  self->setRadius(radius);
}

//  void QQuickRoundButton::resetRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRoundButton11resetRadiusEv(QQuickRoundButton *self) {
  self->resetRadius();
}

//  void QQuickRoundButton::radiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRoundButton13radiusChangedEv(QQuickRoundButton *self) {
  self->radiusChanged();
}

//  void QQuickRoundButton::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickRoundButton14geometryChangeERK6QRectFS2_(
    QQuickRoundButton *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QQuickRoundButtonPrivate *QQuickRoundButton::d_func()
extern "C" Q_DECL_EXPORT
QQuickRoundButtonPrivate *ritual_ZN17QQuickRoundButton6d_funcEv(
    QQuickRoundButton *self) {
  return self->d_func();
}

//  const QQuickRoundButtonPrivate *QQuickRoundButton::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickRoundButtonPrivate *ritual_ZNK17QQuickRoundButton6d_funcEv(
    const QQuickRoundButton *self) {
  return self->d_func();
}

//  void QQuickRoundButton::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickRoundButton14geometryChangeERK6QRectFS2_(
    QQuickRoundButton *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickRoundButton *>(self)->OwnQQuickRoundButton::geometryChange(
      *newGeometry,
      *oldGeometry);
}
