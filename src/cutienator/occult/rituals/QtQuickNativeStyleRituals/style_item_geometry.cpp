//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitem_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt builds QuickNativeStyle for macOS and Windows only, so the whole
//  file stands under that. Qt does not export the struct and its
//  header declares no function of it. The default constructor and the
//  destructor are the implicit ones, written as 'new' and 'delete'
//  for Python to make and free it.
//  Not written: the 'operator<<' to a QDebug, which Qt's library does
//  not offer. No file of QtWidgets is included, as 'QStyle' would
//  then be ambiguous in the headers of this part.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qquickstyleitem_p.h>

//  StyleItemGeometry::StyleItemGeometry()
extern "C" Q_DECL_EXPORT
StyleItemGeometry *ritual_ZN17StyleItemGeometryC1Ev() {
  return new StyleItemGeometry();
}

//  StyleItemGeometry::~StyleItemGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN17StyleItemGeometryD1Ev(StyleItemGeometry *self) {
  delete self;
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
