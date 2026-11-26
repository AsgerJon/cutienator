//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemdelaybutton_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it (Qt
//  builds the part for those two only). Kept as it is when the
//  generator runs again.
//  Qt does not export this class: only its virtual functions are called,
//  through the object.
//  Not written: the constructor, 'tr', and the destructor (Qt declares
//  none).
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemdelaybutton_p.h>
#include <QtGui/qfont.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *QQuickStyleItemDelayButton::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickStyleItemDelayButton10metaObjectEv(
    const QQuickStyleItemDelayButton *self) {
  return self->metaObject();
}

//  void QQuickStyleItemDelayButton::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QQuickStyleItemDelayButton16connectToControlEv(
    const QQuickStyleItemDelayButton *self) {
  self->connectToControl();
}

//  void QQuickStyleItemDelayButton::initStyleOption(QStyleOptionButton
//      &styleOption) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QQuickStyleItemDelayButton15initStyleOptionERN4QQC218QStyleOptionButtonE(
    const QQuickStyleItemDelayButton *self,
    QQC2::QStyleOptionButton *styleOption) {
  self->initStyleOption(*styleOption);
}

#endif  // Qt builds it for macOS and Windows
