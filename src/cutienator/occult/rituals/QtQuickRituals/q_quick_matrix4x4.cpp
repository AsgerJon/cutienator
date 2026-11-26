//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qmatrix4x4.h>

//  const QMetaObject *QQuickMatrix4x4::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickMatrix4x410metaObjectEv(
    const QQuickMatrix4x4 *self) {
  return self->metaObject();
}

//  void *QQuickMatrix4x4::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickMatrix4x411qt_metacastEPKc(
    QQuickMatrix4x4 *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMatrix4x4::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickMatrix4x411qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMatrix4x4 *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickMatrix4x4::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickMatrix4x42trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickMatrix4x4::tr(s, c, n));
}

//  QQuickMatrix4x4::QQuickMatrix4x4(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickMatrix4x4 *ritual_ZN15QQuickMatrix4x4C1EP7QObject(QObject *parent) {
  return new QQuickMatrix4x4(parent);
}

//  QMatrix4x4 QQuickMatrix4x4::matrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK15QQuickMatrix4x46matrixEv(
    const QQuickMatrix4x4 *self) {
  return new QMatrix4x4(self->matrix());
}

//  void QQuickMatrix4x4::setMatrix(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMatrix4x49setMatrixERK10QMatrix4x4(
    QQuickMatrix4x4 *self,
    const QMatrix4x4 *matrix) {
  self->setMatrix(*matrix);
}

//  void QQuickMatrix4x4::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQuickMatrix4x47applyToEP10QMatrix4x4(
    const QQuickMatrix4x4 *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}

//  void QQuickMatrix4x4::matrixChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickMatrix4x413matrixChangedEv(QQuickMatrix4x4 *self) {
  self->matrixChanged();
}

//  QQuickMatrix4x4Private *QQuickMatrix4x4::d_func()
extern "C" Q_DECL_EXPORT
QQuickMatrix4x4Private *ritual_ZN15QQuickMatrix4x46d_funcEv(
    QQuickMatrix4x4 *self) {
  return self->d_func();
}

//  const QQuickMatrix4x4Private *QQuickMatrix4x4::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickMatrix4x4Private *ritual_ZNK15QQuickMatrix4x46d_funcEv(
    const QQuickMatrix4x4 *self) {
  return self->d_func();
}

//  void QQuickMatrix4x4::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK15QQuickMatrix4x47applyToEP10QMatrix4x4(
    const QQuickMatrix4x4 *self,
    QMatrix4x4 *matrix) {
  self->QQuickMatrix4x4::applyTo(matrix);
}
