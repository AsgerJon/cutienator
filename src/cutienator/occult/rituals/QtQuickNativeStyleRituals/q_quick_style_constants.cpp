//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleconstants_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25:
//  the includes stand under the '#if' now, as Qt's Linux kit lacks
//  them, with no export header and no module header of
//  QtQuickNativeStyle before the header, which is included by its
//  own path. Qt does not export the class, so its Cute class,
//  'take', 'qt_metacast' and 'tr' are gone, and only 'metaObject'
//  and the inline function 'qt_qmlMarker_singleton' are left. Qt
//  builds the class for macOS only.
//  Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleconstants_p.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *QQuickStyleConstants::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickStyleConstants10metaObjectEv(
    const QQuickStyleConstants *self) {
  return self->metaObject();
}

//  void QQuickStyleConstants::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickStyleConstants22qt_qmlMarker_singletonEv(
    QQuickStyleConstants *self) {
  self->qt_qmlMarker_singleton();
}

#endif  // defined(Q_OS_MACOS)
