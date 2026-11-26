//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemgroupbox_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator
//  runs again.
//  Qt does not export this class, and builds it for macOS and Windows
//  only (quickcontrols2-macos, quickcontrols2-windows). Qt's library
//  offers nothing of it by name: only its virtual functions are
//  called, through the object.
//  Not written: the constructor, 'tr', 'qt_metacast', 'qt_metacall'
//  and the private 'initStyleOption', which is no virtual function.
//  Also not written: 'groupBoxPadding', 'labelPos' and the signals.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemgroupbox_p.h>
#include <QtGui/qfont.h>

//  const QMetaObject *QQuickStyleItemGroupBox::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickStyleItemGroupBox10metaObjectEv(
    const QQuickStyleItemGroupBox *self) {
  return self->metaObject();
}

//  QQuickStyleItemGroupBox::~QQuickStyleItemGroupBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickStyleItemGroupBoxD1Ev(
    QQuickStyleItemGroupBox *self) {
  delete self;
}

//  QFont QQuickStyleItemGroupBox::styleFont(QQuickItem *control) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK23QQuickStyleItemGroupBox9styleFontEP10QQuickItem(
    const QQuickStyleItemGroupBox *self,
    QQuickItem *control) {
  return new QFont(self->styleFont(control));
}

//  void QQuickStyleItemGroupBox::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QQuickStyleItemGroupBox10paintEventEP8QPainter(
    const QQuickStyleItemGroupBox *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemGroupBox::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN23QQuickStyleItemGroupBox17calculateGeometryEv(
    QQuickStyleItemGroupBox *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
