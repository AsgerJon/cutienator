//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineWid
//  gets/6.12.0/QtWebEngineWidgets/private/qwebengine_accessible_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-27: the constructor's ritual and the
//  copy of the constructor are taken out. Making one needs the table of
//  virtual functions of QWebEngineViewAccessible, which Qt's library does
//  not offer, and two of those functions, isValid and child, call
//  WebEngine's Chromium side (QWebEnginePagePrivate, WebContentsAdapter),
//  whose headers Qt does not install, so they cannot be copied; the other
//  rituals work on an object Qt gives. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtWebEngineWidgets/qtwebenginewidgetsglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(accessibility)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebEngineWidgets/QtWebEngineWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineWidgets/6.12.0/QtWebEngineWidgets/private/qwebengine_accessible_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineWidgets/private/qwebengine_accessible_p.h>
#include <QtWebEngineWidgets/qwebengineview.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 29, as _ZNK24QWebEngineViewAccessible10focusChildEv
inline QAccessibleInterface *QWebEngineViewAccessible::focusChild() const
{
    if (child(0) && child(0)->focusChild())
        return child(0)->focusChild();
    return const_cast<QWebEngineViewAccessible *>(this);
}

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 36, as _ZNK24QWebEngineViewAccessible10childCountEv
inline int QWebEngineViewAccessible::childCount() const
{
    return child(0) ? 1 : 0;
}

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 48, as _ZNK24QWebEngineViewAccessible12indexOfChildEPK20QAccessibleInterface
inline int QWebEngineViewAccessible::indexOfChild(const QAccessibleInterface *c) const
{
    if (child(0) && c == child(0))
        return 0;
    return -1;
}

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 55, as _ZNK24QWebEngineViewAccessible4viewEv
inline QWebEngineView *QWebEngineViewAccessible::view() const
{
    return static_cast<QWebEngineView *>(object());
}
//  -----------------------------------------------------------------------

//  bool QWebEngineViewAccessible::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QWebEngineViewAccessible7isValidEv(
    const QWebEngineViewAccessible *self) {
  return self->isValid();
}

//  QAccessibleInterface *QWebEngineViewAccessible::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK24QWebEngineViewAccessible10focusChildEv(
    const QWebEngineViewAccessible *self) {
  return self->focusChild();
}

//  int QWebEngineViewAccessible::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QWebEngineViewAccessible10childCountEv(
    const QWebEngineViewAccessible *self) {
  return self->childCount();
}

//  QAccessibleInterface *QWebEngineViewAccessible::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK24QWebEngineViewAccessible5childEi(
    const QWebEngineViewAccessible *self,
    int index) {
  return self->child(index);
}

//  int QWebEngineViewAccessible::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QWebEngineViewAccessible12indexOfChildEPK20QAccessibleInterface(
    const QWebEngineViewAccessible *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  QWebEngineView *QWebEngineViewAccessible::view() const
extern "C" Q_DECL_EXPORT
QWebEngineView *ritual_ZNK24QWebEngineViewAccessible4viewEv(
    const QWebEngineViewAccessible *self) {
  return self->view();
}

//  QAccessibleInterface *QWebEngineViewAccessible::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK24QWebEngineViewAccessible10focusChildEv(
    const QWebEngineViewAccessible *self) {
  return self->QWebEngineViewAccessible::focusChild();
}

//  int QWebEngineViewAccessible::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QWebEngineViewAccessible10childCountEv(
    const QWebEngineViewAccessible *self) {
  return self->QWebEngineViewAccessible::childCount();
}

//  int QWebEngineViewAccessible::indexOfChild(const QAccessibleInterface
//      *child) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QWebEngineViewAccessible12indexOfChildEPK20QAccessibleInterface(
    const QWebEngineViewAccessible *self,
    const QAccessibleInterface *child) {
  return self->QWebEngineViewAccessible::indexOfChild(child);
}

#endif  // QT_CONFIG(accessibility)
