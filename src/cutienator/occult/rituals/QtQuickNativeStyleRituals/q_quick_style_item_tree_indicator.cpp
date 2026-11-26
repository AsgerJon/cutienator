//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemtreeindicator_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it (Qt
//  builds the part for those two only). Kept as it is when the
//  generator runs again.
//  Qt does not export this class: only its virtual functions are called,
//  through the object.
//  Not written: the constructor, 'tr' and the destructor (Qt declares none),
//  and 'initStyleOption', a private function that is not virtual.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquick-config_p.h>
#if (defined(Q_OS_MACOS) || defined(Q_OS_WIN)) \
    && QT_CONFIG(quick_treeview)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemtreeindicator_p.h>
#include <QtGui/qfont.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *QQuickStyleItemTreeIndicator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickStyleItemTreeIndicator10metaObjectEv(
    const QQuickStyleItemTreeIndicator *self) {
  return self->metaObject();
}

//  void QQuickStyleItemTreeIndicator::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QQuickStyleItemTreeIndicator16connectToControlEv(
    const QQuickStyleItemTreeIndicator *self) {
  self->connectToControl();
}

//  void QQuickStyleItemTreeIndicator::paintEvent(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QQuickStyleItemTreeIndicator10paintEventEP8QPainter(
    const QQuickStyleItemTreeIndicator *self,
    QPainter *painter) {
  self->paintEvent(painter);
}

//  StyleItemGeometry QQuickStyleItemTreeIndicator::calculateGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN28QQuickStyleItemTreeIndicator17calculateGeometryEv(
    QQuickStyleItemTreeIndicator *self) {
  return new StyleItemGeometry(self->calculateGeometry());
}

#endif  // Qt builds it for macOS and Windows
