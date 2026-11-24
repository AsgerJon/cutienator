//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>

//  void QQmlSizeFValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlSizeFValueType20qt_qmlMarker_foreignEv(
    QQmlSizeFValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQmlSizeFValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlSizeFValueType21qt_qmlMarker_extendedEv(
    QQmlSizeFValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QQmlSizeFValueType::QQmlSizeFValueType()
extern "C" Q_DECL_EXPORT
QQmlSizeFValueType *ritual_ZN18QQmlSizeFValueTypeC1Ev() {
  return new QQmlSizeFValueType();
}

//  QQmlSizeFValueType::QQmlSizeFValueType(const QSizeF &size)
extern "C" Q_DECL_EXPORT
QQmlSizeFValueType *ritual_ZN18QQmlSizeFValueTypeC1ERK6QSizeF(
    const QSizeF *size) {
  return new QQmlSizeFValueType(*size);
}

//  QQmlSizeFValueType::QQmlSizeFValueType(const QSize &size)
extern "C" Q_DECL_EXPORT
QQmlSizeFValueType *ritual_ZN18QQmlSizeFValueTypeC1ERK5QSize(
    const QSize *size) {
  return new QQmlSizeFValueType(*size);
}

//  QString QQmlSizeFValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlSizeFValueType8toStringEv(
    const QQmlSizeFValueType *self) {
  return new QString(self->toString());
}

//  qreal QQmlSizeFValueType::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQmlSizeFValueType5widthEv(
    const QQmlSizeFValueType *self) {
  return self->width();
}

//  qreal QQmlSizeFValueType::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQmlSizeFValueType6heightEv(
    const QQmlSizeFValueType *self) {
  return self->height();
}

//  void QQmlSizeFValueType::setWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlSizeFValueType8setWidthEd(
    QQmlSizeFValueType *self,
    qreal a0) {
  self->setWidth(a0);
}

//  void QQmlSizeFValueType::setHeight(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlSizeFValueType9setHeightEd(
    QQmlSizeFValueType *self,
    qreal a0) {
  self->setHeight(a0);
}

//  QQmlSizeFValueType::~QQmlSizeFValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlSizeFValueTypeD1Ev(QQmlSizeFValueType *self) {
  delete self;
}
