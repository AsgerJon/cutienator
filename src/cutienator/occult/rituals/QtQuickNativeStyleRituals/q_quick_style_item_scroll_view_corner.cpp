//  Written by dev_tooling.RitualGenerator from the records of QtQuickNativeS
//  tyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemscrollviewcorner_p.
//  h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the includes of the headers
//  'QtQuickNativeStyle/qtquicknativestyleexports.h' and
//  'QtQuickNativeStyle/QtQuickNativeStyle' are taken out, no Qt
//  installs them. Qt does not export this class, so what the generator
//  took from Qt's source (the bodies of 'paintEvent',
//  'calculateGeometry' and 'initStyleOption', which call functions of
//  Qt's library that are not exported), the 'own_' rituals and the
//  rituals of 'tr' and 'qt_metacast' are taken out: only the virtual
//  functions called through the object are left. The private
//  'initStyleOption' is no virtual function and goes with them.
//  Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemscrollviewcorner_p.h>

//  const QMetaObject *QQuickStyleItemScrollViewCorner::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickStyleItemScrollViewCorner10metaObjectEv(
    const QQuickStyleItemScrollViewCorner *self) {
  return self->metaObject();
}

//  QQuickStyleItemScrollViewCorner::~QQuickStyleItemScrollViewCorner()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickStyleItemScrollViewCornerD1Ev(
    QQuickStyleItemScrollViewCorner *self) {
  delete self;
}

//  void QQuickStyleItemScrollViewCorner::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK31QQuickStyleItemScrollViewCorner10paintEventEP8QPainter(
    const QQuickStyleItemScrollViewCorner *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemScrollViewCorner::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN31QQuickStyleItemScrollViewCorner17calculateGeometryEv(
    QQuickStyleItemScrollViewCorner *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // defined(Q_OS_MACOS)
