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

//  void QQmlSizeValueType::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlSizeValueType22qt_qmlMarker_anonymousEv(
    QQmlSizeValueType *self) {
  self->qt_qmlMarker_anonymous();
}

//  void QQmlSizeValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlSizeValueType20qt_qmlMarker_foreignEv(
    QQmlSizeValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQmlSizeValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlSizeValueType21qt_qmlMarker_extendedEv(
    QQmlSizeValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QQmlSizeValueType::QQmlSizeValueType()
extern "C" Q_DECL_EXPORT
QQmlSizeValueType *ritual_ZN17QQmlSizeValueTypeC1Ev() {
  return new QQmlSizeValueType();
}

//  QQmlSizeValueType::QQmlSizeValueType(const QSize &size)
extern "C" Q_DECL_EXPORT
QQmlSizeValueType *ritual_ZN17QQmlSizeValueTypeC1ERK5QSize(
    const QSize *size) {
  return new QQmlSizeValueType(*size);
}

//  QQmlSizeValueType::QQmlSizeValueType(const QSizeF &size)
extern "C" Q_DECL_EXPORT
QQmlSizeValueType *ritual_ZN17QQmlSizeValueTypeC1ERK6QSizeF(
    const QSizeF *size) {
  return new QQmlSizeValueType(*size);
}

//  QString QQmlSizeValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQmlSizeValueType8toStringEv(
    const QQmlSizeValueType *self) {
  return new QString(self->toString());
}

//  int QQmlSizeValueType::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlSizeValueType5widthEv(const QQmlSizeValueType *self) {
  return self->width();
}

//  int QQmlSizeValueType::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlSizeValueType6heightEv(const QQmlSizeValueType *self) {
  return self->height();
}

//  void QQmlSizeValueType::setWidth(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlSizeValueType8setWidthEi(
    QQmlSizeValueType *self,
    int a0) {
  self->setWidth(a0);
}

//  void QQmlSizeValueType::setHeight(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlSizeValueType9setHeightEi(
    QQmlSizeValueType *self,
    int a0) {
  self->setHeight(a0);
}

//  QQmlSizeValueType::~QQmlSizeValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlSizeValueTypeD1Ev(QQmlSizeValueType *self) {
  delete self;
}
