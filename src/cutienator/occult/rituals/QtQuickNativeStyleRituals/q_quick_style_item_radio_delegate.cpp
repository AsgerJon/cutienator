//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemradiodelegate_p.h,
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
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitemradiodelegate_p.h>
#include <QtGui/qfont.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmetaobject.h>

//  const QMetaObject *QQuickStyleItemRadioDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickStyleItemRadioDelegate10metaObjectEv(
    const QQuickStyleItemRadioDelegate *self) {
  return self->metaObject();
}

//  void QQuickStyleItemRadioDelegate::connectToControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QQuickStyleItemRadioDelegate16connectToControlEv(
    const QQuickStyleItemRadioDelegate *self) {
  self->connectToControl();
}

//  void QQuickStyleItemRadioDelegate::initStyleOption(QStyleOptionButton
//      &styleOption) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QQuickStyleItemRadioDelegate15initStyleOptionERN4QQC218QStyleOptionButtonE(
    const QQuickStyleItemRadioDelegate *self,
    QQC2::QStyleOptionButton *styleOption) {
  self->initStyleOption(*styleOption);
}

#endif  // Qt builds it for macOS and Windows
