//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsxpstyle_p_p.h,
//  Qt 6.12.0, as the Qt of Windows installs it. Kept as it is when
//  the generator runs again. Qt's library offers nothing of this
//  class by name: only what its header writes out.
//  An 'HDC' is passed as an address. Not written: the constructor
//  and the destructor, which call 'init' and 'cleanup', which
//  Qt's library offers not, and 'hasTheme', which reads the class's
//  'm_themes', which it offers not either.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickwindowsxpstyle_p_p.h>

//  HDC QQC2::QWindowsXPStylePrivate::bufferHDC()
extern "C" Q_DECL_EXPORT
HDC ritual_ZN4QQC222QWindowsXPStylePrivate9bufferHDCEv(
    QQC2::QWindowsXPStylePrivate *self) {
  return self->bufferHDC();
}

#endif  // defined(Q_OS_WIN)
