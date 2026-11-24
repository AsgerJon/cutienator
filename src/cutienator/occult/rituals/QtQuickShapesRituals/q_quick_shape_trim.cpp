//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickShapeTrim::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickShapeTrim10metaObjectEv(
    const QQuickShapeTrim *self) {
  return self->metaObject();
}

//  QString QQuickShapeTrim::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickShapeTrim2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickShapeTrim::tr(s, c, n));
}

//  void QQuickShapeTrim::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapeTrim22qt_qmlMarker_anonymousEv(
    QQuickShapeTrim *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickShapeTrim::QQuickShapeTrim(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickShapeTrim *ritual_ZN15QQuickShapeTrimC1EP7QObject(QObject *parent) {
  return new QQuickShapeTrim(parent);
}

//  qreal QQuickShapeTrim::start() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickShapeTrim5startEv(const QQuickShapeTrim *self) {
  return self->start();
}

//  void QQuickShapeTrim::setStart(qreal t)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapeTrim8setStartEd(QQuickShapeTrim *self, qreal t) {
  self->setStart(t);
}

//  qreal QQuickShapeTrim::end() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickShapeTrim3endEv(const QQuickShapeTrim *self) {
  return self->end();
}

//  void QQuickShapeTrim::setEnd(qreal t)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapeTrim6setEndEd(QQuickShapeTrim *self, qreal t) {
  self->setEnd(t);
}

//  qreal QQuickShapeTrim::offset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickShapeTrim6offsetEv(const QQuickShapeTrim *self) {
  return self->offset();
}

//  void QQuickShapeTrim::setOffset(qreal t)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickShapeTrim9setOffsetEd(QQuickShapeTrim *self, qreal t) {
  self->setOffset(t);
}
