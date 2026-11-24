//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmargins.h>
#include <QtCore/qstring.h>

//  void QQmlMarginsValueType::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlMarginsValueType22qt_qmlMarker_anonymousEv(
    QQmlMarginsValueType *self) {
  self->qt_qmlMarker_anonymous();
}

//  void QQmlMarginsValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlMarginsValueType20qt_qmlMarker_foreignEv(
    QQmlMarginsValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQmlMarginsValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlMarginsValueType21qt_qmlMarker_extendedEv(
    QQmlMarginsValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QQmlMarginsValueType::QQmlMarginsValueType()
extern "C" Q_DECL_EXPORT
QQmlMarginsValueType *ritual_ZN20QQmlMarginsValueTypeC1Ev() {
  return new QQmlMarginsValueType();
}

//  QQmlMarginsValueType::QQmlMarginsValueType(const QMargins &margins)
extern "C" Q_DECL_EXPORT
QQmlMarginsValueType *ritual_ZN20QQmlMarginsValueTypeC1ERK8QMargins(
    const QMargins *margins) {
  return new QQmlMarginsValueType(*margins);
}

//  QQmlMarginsValueType::QQmlMarginsValueType(const QMarginsF &margins)
extern "C" Q_DECL_EXPORT
QQmlMarginsValueType *ritual_ZN20QQmlMarginsValueTypeC1ERK9QMarginsF(
    const QMarginsF *margins) {
  return new QQmlMarginsValueType(*margins);
}

//  QString QQmlMarginsValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQmlMarginsValueType8toStringEv(
    const QQmlMarginsValueType *self) {
  return new QString(self->toString());
}

//  int QQmlMarginsValueType::left() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQmlMarginsValueType4leftEv(
    const QQmlMarginsValueType *self) {
  return self->left();
}

//  int QQmlMarginsValueType::right() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQmlMarginsValueType5rightEv(
    const QQmlMarginsValueType *self) {
  return self->right();
}

//  int QQmlMarginsValueType::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQmlMarginsValueType3topEv(
    const QQmlMarginsValueType *self) {
  return self->top();
}

//  int QQmlMarginsValueType::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQmlMarginsValueType6bottomEv(
    const QQmlMarginsValueType *self) {
  return self->bottom();
}

//  void QQmlMarginsValueType::setLeft(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlMarginsValueType7setLeftEi(
    QQmlMarginsValueType *self,
    int a0) {
  self->setLeft(a0);
}

//  void QQmlMarginsValueType::setRight(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlMarginsValueType8setRightEi(
    QQmlMarginsValueType *self,
    int a0) {
  self->setRight(a0);
}

//  void QQmlMarginsValueType::setTop(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlMarginsValueType6setTopEi(
    QQmlMarginsValueType *self,
    int a0) {
  self->setTop(a0);
}

//  void QQmlMarginsValueType::setBottom(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlMarginsValueType9setBottomEi(
    QQmlMarginsValueType *self,
    int a0) {
  self->setBottom(a0);
}

//  QQmlMarginsValueType::~QQmlMarginsValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlMarginsValueTypeD1Ev(QQmlMarginsValueType *self) {
  delete self;
}
