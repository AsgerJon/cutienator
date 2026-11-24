//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativepolylinemapitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativepolylinemapitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>

//  const QMetaObject *QDeclarativeMapLineProperties::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QDeclarativeMapLineProperties10metaObjectEv(
    const QDeclarativeMapLineProperties *self) {
  return self->metaObject();
}

//  QString QDeclarativeMapLineProperties::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QDeclarativeMapLineProperties2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeMapLineProperties::tr(s, c, n));
}

//  void QDeclarativeMapLineProperties::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeMapLineProperties22qt_qmlMarker_anonymousEv(
    QDeclarativeMapLineProperties *self) {
  self->qt_qmlMarker_anonymous();
}

//  QDeclarativeMapLineProperties::QDeclarativeMapLineProperties(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeMapLineProperties *ritual_ZN29QDeclarativeMapLinePropertiesC1EP7QObject(
    QObject *parent) {
  return new QDeclarativeMapLineProperties(parent);
}

//  QColor QDeclarativeMapLineProperties::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK29QDeclarativeMapLineProperties5colorEv(
    const QDeclarativeMapLineProperties *self) {
  return new QColor(self->color());
}

//  void QDeclarativeMapLineProperties::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeMapLineProperties8setColorERK6QColor(
    QDeclarativeMapLineProperties *self,
    const QColor *color) {
  self->setColor(*color);
}

//  qreal QDeclarativeMapLineProperties::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK29QDeclarativeMapLineProperties5widthEv(
    const QDeclarativeMapLineProperties *self) {
  return self->width();
}

//  void QDeclarativeMapLineProperties::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDeclarativeMapLineProperties8setWidthEd(
    QDeclarativeMapLineProperties *self,
    qreal width) {
  self->setWidth(width);
}
