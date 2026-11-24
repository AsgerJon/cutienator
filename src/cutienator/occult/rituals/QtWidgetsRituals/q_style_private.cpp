//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qstyle_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qwidget.h>
#include <QtGui/qbitmap.h>
#include <QtGui/qpixmapcache.h>
#include <QtCore/qset.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/private/qstyle_p.h>
#include <QtWidgets/private/qstylehelper_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#ifndef QT_NO_DEBUG
#include <QtCore/qdebug.h>
#endif
#include <QtCore/q20utility.h>
#include <limits.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/styles/qstyle.cpp, line 2475, as _ZN13QStylePrivate21useFullScreenForPopupEv
inline bool QStylePrivate::useFullScreenForPopup()
{
    auto theme = QGuiApplicationPrivate::platformTheme();
    return theme && theme->themeHint(QPlatformTheme::UseFullScreenForPopupMenu).toBool();
}
//  -----------------------------------------------------------------------

//  QStyle *QStylePrivate::q_func()
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZN13QStylePrivate6q_funcEv(QStylePrivate *self) {
  return self->q_func();
}

//  const QStyle *QStylePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QStyle *ritual_ZNK13QStylePrivate6q_funcEv(const QStylePrivate *self) {
  return self->q_func();
}

//  QStylePrivate *QStylePrivate::get(QStyle *s)
extern "C" Q_DECL_EXPORT
QStylePrivate *ritual_ZN13QStylePrivate3getEP6QStyle(QStyle *s) {
  return QStylePrivate::get(s);
}

//  const QStylePrivate *QStylePrivate::get(const QStyle *s)
extern "C" Q_DECL_EXPORT
const QStylePrivate *ritual_ZN13QStylePrivate3getEPK6QStyle(
    const QStyle *s) {
  return QStylePrivate::get(s);
}

//  bool QStylePrivate::useFullScreenForPopup()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QStylePrivate21useFullScreenForPopupEv() {
  return QStylePrivate::useFullScreenForPopup();
}
