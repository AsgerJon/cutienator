//  Written by dev_tooling.RitualGenerator from the records of QtQuickNativeS
//  tyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the includes of the headers
//  'QtQuickNativeStyle/qtquicknativestyleexports.h' and
//  'QtQuickNativeStyle/QtQuickNativeStyle' are taken out, no Qt
//  installs them. Qt builds the part for macOS and Windows only
//  (quickcontrols2-macos, quickcontrols2-windows), so the whole file
//  stands under that condition as well as under the 'quick_itemview'
//  of the class. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#if QT_CONFIG(quick_itemview)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qstyleoption_p.h>

#endif  // QT_CONFIG(quick_itemview)
#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
