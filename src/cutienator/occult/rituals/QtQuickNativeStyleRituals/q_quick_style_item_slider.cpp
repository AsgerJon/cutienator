//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemslider_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it (Qt
//  builds the part for those two only). Kept as it is when the
//  generator runs again.
//  Qt does not export this class: only its virtual functions are called,
//  through the object.
//  Not written: the constructor, 'tr' and the destructor (Qt declares none),
//  and 'initStyleOption', a private function that is not virtual.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemslider_p.h>
#include <QtGui/qfont.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *QQuickStyleItemSlider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickStyleItemSlider10metaObjectEv(
    const QQuickStyleItemSlider *self) {
  return self->metaObject();
}

//  QFont QQuickStyleItemSlider::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK21QQuickStyleItemSlider9styleFontEP10QQuickItem(
    const QQuickStyleItemSlider *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemSlider::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickStyleItemSlider16connectToControlEv(
    const QQuickStyleItemSlider *self) {
  self->connectToControl();
}

//  void QQuickStyleItemSlider::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QQuickStyleItemSlider10paintEventEP8QPainter(
    const QQuickStyleItemSlider *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemSlider::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN21QQuickStyleItemSlider17calculateGeometryEv(
    QQuickStyleItemSlider *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // Qt builds it for macOS and Windows
