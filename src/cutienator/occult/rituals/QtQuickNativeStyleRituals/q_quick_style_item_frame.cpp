//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemframe_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator
//  runs again.
//  Qt does not export this class, and builds it for macOS and Windows
//  only (quickcontrols2-macos, quickcontrols2-windows). Qt's library
//  offers nothing of it by name: only its virtual functions are
//  called, through the object.
//  Not written: the constructor, 'tr', 'qt_metacast', 'qt_metacall'
//  and the private 'initStyleOption', which is no virtual function.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemframe_p.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItemFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickStyleItemFrame10metaObjectEv(
    const QQuickStyleItemFrame *self) {
  return self->metaObject();
}

//  QQuickStyleItemFrame::~QQuickStyleItemFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickStyleItemFrameD1Ev(
    QQuickStyleItemFrame *self) {
  delete self;
}

//  void QQuickStyleItemFrame::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QQuickStyleItemFrame10paintEventEP8QPainter(
    const QQuickStyleItemFrame *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemFrame::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN20QQuickStyleItemFrame17calculateGeometryEv(
    QQuickStyleItemFrame *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
