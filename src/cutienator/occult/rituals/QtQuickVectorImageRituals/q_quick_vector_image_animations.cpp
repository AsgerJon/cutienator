//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimage_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25: the ritual of 'qt_metacast'
//  is taken out, with its row, as no ritual file has one (the older file
//  of the package had none). The code compiles alone against Qt's Linux
//  kit; the test build's message was cut off inside 'qquickanimation_p.h'
//  (line 28), which this file cannot change. Kept as it is when the
//  generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickVectorImage/QtQuickVectorImage>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickVectorImage/6.12.0/QtQuickVectorImage/private/qquickvectorimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickVectorImageAnimations::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickVectorImageAnimations10metaObjectEv(
    const QQuickVectorImageAnimations *self) {
  return self->metaObject();
}

//  QString QQuickVectorImageAnimations::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQuickVectorImageAnimations2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickVectorImageAnimations::tr(s, c, n));
}

//  void QQuickVectorImageAnimations::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickVectorImageAnimations22qt_qmlMarker_anonymousEv(
    QQuickVectorImageAnimations *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickVectorImageAnimations::QQuickVectorImageAnimations(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickVectorImageAnimations *ritual_ZN27QQuickVectorImageAnimationsC1EP7QObject(
    QObject *parent) {
  return new QQuickVectorImageAnimations(parent);
}

//  int QQuickVectorImageAnimations::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QQuickVectorImageAnimations5loopsEv(
    const QQuickVectorImageAnimations *self) {
  return self->loops();
}

//  void QQuickVectorImageAnimations::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickVectorImageAnimations8setLoopsEi(
    QQuickVectorImageAnimations *self,
    int loops) {
  self->setLoops(loops);
}

//  bool QQuickVectorImageAnimations::paused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickVectorImageAnimations6pausedEv(
    const QQuickVectorImageAnimations *self) {
  return self->paused();
}

//  void QQuickVectorImageAnimations::setPaused(bool paused)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickVectorImageAnimations9setPausedEb(
    QQuickVectorImageAnimations *self,
    bool paused) {
  self->setPaused(paused);
}

//  void QQuickVectorImageAnimations::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickVectorImageAnimations7restartEv(
    QQuickVectorImageAnimations *self) {
  self->restart();
}
