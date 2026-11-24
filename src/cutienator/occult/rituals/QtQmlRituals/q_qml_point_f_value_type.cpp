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

//  void QQmlPointFValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPointFValueType20qt_qmlMarker_foreignEv(
    QQmlPointFValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQmlPointFValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPointFValueType21qt_qmlMarker_extendedEv(
    QQmlPointFValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QQmlPointFValueType::QQmlPointFValueType()
extern "C" Q_DECL_EXPORT
QQmlPointFValueType *ritual_ZN19QQmlPointFValueTypeC1Ev() {
  return new QQmlPointFValueType();
}

//  QQmlPointFValueType::QQmlPointFValueType(const QPointF &point)
extern "C" Q_DECL_EXPORT
QQmlPointFValueType *ritual_ZN19QQmlPointFValueTypeC1ERK7QPointF(
    const QPointF *point) {
  return new QQmlPointFValueType(*point);
}

//  QQmlPointFValueType::QQmlPointFValueType(const QPoint &point)
extern "C" Q_DECL_EXPORT
QQmlPointFValueType *ritual_ZN19QQmlPointFValueTypeC1ERK6QPoint(
    const QPoint *point) {
  return new QQmlPointFValueType(*point);
}

//  QString QQmlPointFValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlPointFValueType8toStringEv(
    const QQmlPointFValueType *self) {
  return new QString(self->toString());
}

//  qreal QQmlPointFValueType::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQmlPointFValueType1xEv(const QQmlPointFValueType *self) {
  return self->x();
}

//  qreal QQmlPointFValueType::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQmlPointFValueType1yEv(const QQmlPointFValueType *self) {
  return self->y();
}

//  void QQmlPointFValueType::setX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPointFValueType4setXEd(
    QQmlPointFValueType *self,
    qreal a0) {
  self->setX(a0);
}

//  void QQmlPointFValueType::setY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPointFValueType4setYEd(
    QQmlPointFValueType *self,
    qreal a0) {
  self->setY(a0);
}

//  QQmlPointFValueType::~QQmlPointFValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlPointFValueTypeD1Ev(QQmlPointFValueType *self) {
  delete self;
}
