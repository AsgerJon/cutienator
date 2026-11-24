//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickscalegrid_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickscalegrid_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickScaleGrid::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickScaleGrid10metaObjectEv(
    const QQuickScaleGrid *self) {
  return self->metaObject();
}

//  QString QQuickScaleGrid::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickScaleGrid2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScaleGrid::tr(s, c, n));
}

//  void QQuickScaleGrid::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScaleGrid22qt_qmlMarker_anonymousEv(
    QQuickScaleGrid *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickScaleGrid::QQuickScaleGrid(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickScaleGrid *ritual_ZN15QQuickScaleGridC1EP7QObject(QObject *parent) {
  return new QQuickScaleGrid(parent);
}

//  bool QQuickScaleGrid::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickScaleGrid6isNullEv(const QQuickScaleGrid *self) {
  return self->isNull();
}

//  int QQuickScaleGrid::left() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickScaleGrid4leftEv(const QQuickScaleGrid *self) {
  return self->left();
}

//  void QQuickScaleGrid::setLeft(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScaleGrid7setLeftEi(QQuickScaleGrid *self, int a0) {
  self->setLeft(a0);
}

//  int QQuickScaleGrid::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickScaleGrid3topEv(const QQuickScaleGrid *self) {
  return self->top();
}

//  void QQuickScaleGrid::setTop(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScaleGrid6setTopEi(QQuickScaleGrid *self, int a0) {
  self->setTop(a0);
}

//  int QQuickScaleGrid::right() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickScaleGrid5rightEv(const QQuickScaleGrid *self) {
  return self->right();
}

//  void QQuickScaleGrid::setRight(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScaleGrid8setRightEi(QQuickScaleGrid *self, int a0) {
  self->setRight(a0);
}

//  int QQuickScaleGrid::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickScaleGrid6bottomEv(const QQuickScaleGrid *self) {
  return self->bottom();
}

//  void QQuickScaleGrid::setBottom(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickScaleGrid9setBottomEi(QQuickScaleGrid *self, int a0) {
  self->setBottom(a0);
}
