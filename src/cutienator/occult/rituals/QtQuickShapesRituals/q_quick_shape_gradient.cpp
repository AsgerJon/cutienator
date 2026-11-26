//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickShapeGradient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickShapeGradient10metaObjectEv(
    const QQuickShapeGradient *self) {
  return self->metaObject();
}

//  void *QQuickShapeGradient::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuickShapeGradient11qt_metacastEPKc(
    QQuickShapeGradient *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickShapeGradient::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickShapeGradient11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickShapeGradient *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickShapeGradient::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuickShapeGradient2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickShapeGradient::tr(s, c, n));
}

//  void QQuickShapeGradient::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickShapeGradient24qt_qmlMarker_uncreatableEv(
    QQuickShapeGradient *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickShapeGradient::QQuickShapeGradient(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickShapeGradient *ritual_ZN19QQuickShapeGradientC1EP7QObject(
    QObject *parent) {
  return new QQuickShapeGradient(parent);
}

//  SpreadMode QQuickShapeGradient::spread() const
extern "C" Q_DECL_EXPORT
QQuickShapeGradient::SpreadMode ritual_ZNK19QQuickShapeGradient6spreadEv(
    const QQuickShapeGradient *self) {
  return self->spread();
}

//  void QQuickShapeGradient::setSpread(SpreadMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickShapeGradient9setSpreadENS_10SpreadModeE(
    QQuickShapeGradient *self,
    QQuickShapeGradient::SpreadMode mode) {
  self->setSpread(mode);
}

//  void QQuickShapeGradient::spreadChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickShapeGradient13spreadChangedEv(
    QQuickShapeGradient *self) {
  self->spreadChanged();
}
