//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qstring.h>

//  void QQmlPointValueType::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlPointValueType22qt_qmlMarker_anonymousEv(
    QQmlPointValueType *self) {
  self->qt_qmlMarker_anonymous();
}

//  void QQmlPointValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlPointValueType20qt_qmlMarker_foreignEv(
    QQmlPointValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQmlPointValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlPointValueType21qt_qmlMarker_extendedEv(
    QQmlPointValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QQmlPointValueType::QQmlPointValueType()
extern "C" Q_DECL_EXPORT
QQmlPointValueType *ritual_ZN18QQmlPointValueTypeC1Ev() {
  return new QQmlPointValueType();
}

//  QQmlPointValueType::QQmlPointValueType(const QPoint &point)
extern "C" Q_DECL_EXPORT
QQmlPointValueType *ritual_ZN18QQmlPointValueTypeC1ERK6QPoint(
    const QPoint *point) {
  return new QQmlPointValueType(*point);
}

//  QQmlPointValueType::QQmlPointValueType(const QPointF &point)
extern "C" Q_DECL_EXPORT
QQmlPointValueType *ritual_ZN18QQmlPointValueTypeC1ERK7QPointF(
    const QPointF *point) {
  return new QQmlPointValueType(*point);
}

//  QString QQmlPointValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlPointValueType8toStringEv(
    const QQmlPointValueType *self) {
  return new QString(self->toString());
}

//  int QQmlPointValueType::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlPointValueType1xEv(const QQmlPointValueType *self) {
  return self->x();
}

//  int QQmlPointValueType::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQmlPointValueType1yEv(const QQmlPointValueType *self) {
  return self->y();
}

//  void QQmlPointValueType::setX(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlPointValueType4setXEi(QQmlPointValueType *self, int a0) {
  self->setX(a0);
}

//  void QQmlPointValueType::setY(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlPointValueType4setYEi(QQmlPointValueType *self, int a0) {
  self->setY(a0);
}

//  QQmlPointValueType::~QQmlPointValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlPointValueTypeD1Ev(QQmlPointValueType *self) {
  delete self;
}
