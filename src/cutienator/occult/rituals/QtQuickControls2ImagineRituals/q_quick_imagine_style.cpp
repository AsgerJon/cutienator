//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Imagine/6.12.0/QtQuickControls2Imagine/private/qquickimaginestyle_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2Imagine/QtQuickControls2Imagine>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Imagine/6.12.0/QtQuickControls2Imagine/private/qquickimaginestyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  Only a class built on QQuickImagineStyle may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickImagineStyle : QQuickImagineStyle {
  using QQuickImagineStyle::attachedParentChange;
};

//  const QMetaObject *QQuickImagineStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickImagineStyle10metaObjectEv(
    const QQuickImagineStyle *self) {
  return self->metaObject();
}

//  QString QQuickImagineStyle::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickImagineStyle2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickImagineStyle::tr(s, c, n));
}

//  void QQuickImagineStyle::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImagineStyle21qt_qmlMarker_attachedEv(
    QQuickImagineStyle *self) {
  self->qt_qmlMarker_attached();
}

//  void QQuickImagineStyle::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImagineStyle24qt_qmlMarker_uncreatableEv(
    QQuickImagineStyle *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickImagineStyle::QQuickImagineStyle(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickImagineStyle *ritual_ZN18QQuickImagineStyleC1EP7QObject(
    QObject *parent) {
  return new QQuickImagineStyle(parent);
}

//  QQuickImagineStyle *QQuickImagineStyle::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickImagineStyle *ritual_ZN18QQuickImagineStyle21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickImagineStyle::qmlAttachedProperties(object);
}

//  QString QQuickImagineStyle::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQuickImagineStyle4pathEv(
    const QQuickImagineStyle *self) {
  return new QString(self->path());
}

//  void QQuickImagineStyle::setPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImagineStyle7setPathERK7QString(
    QQuickImagineStyle *self,
    const QString *path) {
  self->setPath(*path);
}

//  void QQuickImagineStyle::inheritPath(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImagineStyle11inheritPathERK7QString(
    QQuickImagineStyle *self,
    const QString *path) {
  self->inheritPath(*path);
}

//  void QQuickImagineStyle::propagatePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImagineStyle13propagatePathEv(
    QQuickImagineStyle *self) {
  self->propagatePath();
}

//  void QQuickImagineStyle::resetPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImagineStyle9resetPathEv(QQuickImagineStyle *self) {
  self->resetPath();
}

//  QUrl QQuickImagineStyle::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQuickImagineStyle3urlEv(const QQuickImagineStyle *self) {
  return new QUrl(self->url());
}

//  void
//      QQuickImagineStyle::attachedParentChange(QQuickAttachedPropertyPropag
//      ator *newParent, QQuickAttachedPropertyPropagator *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImagineStyle20attachedParentChangeEP32QQuickAttachedPropertyPropagatorS1_(
    QQuickImagineStyle *self,
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent) {
  self->attachedParentChange(newParent, oldParent);
}

//  void QQuickImagineStyle::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickImagineStyle4initEv(QQuickImagineStyle *self) {
  self->init();
}

//  void
//      QQuickImagineStyle::attachedParentChange(QQuickAttachedPropertyPropag
//      ator *newParent, QQuickAttachedPropertyPropagator *oldParent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickImagineStyle20attachedParentChangeEP32QQuickAttachedPropertyPropagatorS1_(
    QQuickImagineStyle *self,
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent) {
  static_cast<OwnQQuickImagineStyle *>(self)->OwnQQuickImagineStyle::attachedParentChange(
      newParent,
      oldParent);
}
