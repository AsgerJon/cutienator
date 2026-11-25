//  Written by hand on 2026-11-25 from
//  QtQuickControls2IOSStyleImpl/6.12.0/QtQuickControls2IOSStyleImpl/private/
//  qquickiosstyle_p.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again.
//  Qt builds this part only with its feature 'quickcontrols2-ios',
//  for macOS and iOS. Qt's library offers nothing of this class by
//  name: only its virtual functions are called, through the object,
//  and the destructor C++ writes for it, virtual through QObject,
//  through 'delete'.
//  Not written: the constructor, 'tr' and 'url', which are defined
//  outside the header.
#include <QtCore/qglobal.h>
#include <QtQuickControls2/6.12.0/QtQuickControls2/private/qtquickcontrols2-config_p.h>
#if QT_CONFIG(quickcontrols2_ios)
#include <QtQuickControls2IOSStyleImpl/qtquickcontrols2iosstyleimplexports.h>
#include <QtQuickControls2IOSStyleImpl/6.12.0/QtQuickControls2IOSStyleImpl/private/qquickiosstyle_p.h>

//  const QMetaObject *QQuickIOSStyle::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickIOSStyle10metaObjectEv(
    const QQuickIOSStyle *self) {
  return self->metaObject();
}

//  QQuickIOSStyle::~QQuickIOSStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickIOSStyleD1Ev(QQuickIOSStyle *self) {
  delete self;
}

#endif  // QT_CONFIG(quickcontrols2_ios)
