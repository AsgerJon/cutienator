//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebengine_accessible_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWebEngineQuick/qtwebenginequickglobal.h>
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#if QT_CONFIG(accessibility)
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineview_p.h>
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengine_accessible_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/private/qquickwebengine_accessible_p.h>
#include <QtQuick/QQuickItem>
#include <QtQuick/QQuickWindow>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 19, as _ZNK29QQuickWebEngineViewAccessible7isValidEv
inline bool QQuickWebEngineViewAccessible::isValid() const
{
    if (!QAccessibleObject::isValid())
        return false;

    if (!engineView() || !engineView()->d_func())
        return false;

    return true;
}

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 39, as _ZNK29QQuickWebEngineViewAccessible10focusChildEv
inline QAccessibleInterface *QQuickWebEngineViewAccessible::focusChild() const
{
    if (child(0) && child(0)->focusChild())
        return child(0)->focusChild();
    return const_cast<QQuickWebEngineViewAccessible *>(this);
}

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 46, as _ZNK29QQuickWebEngineViewAccessible10childCountEv
inline int QQuickWebEngineViewAccessible::childCount() const
{
    return child(0) ? 1 : 0;
}

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 58, as _ZNK29QQuickWebEngineViewAccessible12indexOfChildEPK20QAccessibleInterface
inline int QQuickWebEngineViewAccessible::indexOfChild(const QAccessibleInterface *c) const
{
    if (child(0) && c == child(0))
        return 0;
    return -1;
}

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 65, as _ZNK29QQuickWebEngineViewAccessible4textEN11QAccessible4TextE
inline QString QQuickWebEngineViewAccessible::text(QAccessible::Text) const
{
    return QString();
}

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 70, as _ZNK29QQuickWebEngineViewAccessible4roleEv
inline QAccessible::Role QQuickWebEngineViewAccessible::role() const
{
    return QAccessible::Client;
}

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 75, as _ZNK29QQuickWebEngineViewAccessible5stateEv
inline QAccessible::State QQuickWebEngineViewAccessible::state() const
{
    QAccessible::State s;
    return s;
}

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 81, as _ZNK29QQuickWebEngineViewAccessible10engineViewEv
inline QQuickWebEngineView *QQuickWebEngineViewAccessible::engineView() const
{
    return static_cast<QQuickWebEngineView*>(object());
}
//  -----------------------------------------------------------------------

//  bool QQuickWebEngineViewAccessible::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickWebEngineViewAccessible7isValidEv(
    const QQuickWebEngineViewAccessible *self) {
  return self->isValid();
}

//  QAccessibleInterface *QQuickWebEngineViewAccessible::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK29QQuickWebEngineViewAccessible6parentEv(
    const QQuickWebEngineViewAccessible *self) {
  return self->parent();
}

//  QAccessibleInterface *QQuickWebEngineViewAccessible::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK29QQuickWebEngineViewAccessible10focusChildEv(
    const QQuickWebEngineViewAccessible *self) {
  return self->focusChild();
}

//  int QQuickWebEngineViewAccessible::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickWebEngineViewAccessible10childCountEv(
    const QQuickWebEngineViewAccessible *self) {
  return self->childCount();
}

//  QAccessibleInterface *QQuickWebEngineViewAccessible::child(int index)
//      const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK29QQuickWebEngineViewAccessible5childEi(
    const QQuickWebEngineViewAccessible *self,
    int index) {
  return self->child(index);
}

//  int QQuickWebEngineViewAccessible::indexOfChild(const
//      QAccessibleInterface *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickWebEngineViewAccessible12indexOfChildEPK20QAccessibleInterface(
    const QQuickWebEngineViewAccessible *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  QString QQuickWebEngineViewAccessible::text(QAccessible::Text a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QQuickWebEngineViewAccessible4textEN11QAccessible4TextE(
    const QQuickWebEngineViewAccessible *self,
    QAccessible::Text a0) {
  return new QString(self->text(a0));
}

//  QAccessible::Role QQuickWebEngineViewAccessible::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK29QQuickWebEngineViewAccessible4roleEv(
    const QQuickWebEngineViewAccessible *self) {
  return self->role();
}

//  QAccessible::State QQuickWebEngineViewAccessible::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK29QQuickWebEngineViewAccessible5stateEv(
    const QQuickWebEngineViewAccessible *self) {
  return new QAccessible::State(self->state());
}

//  bool QQuickWebEngineViewAccessible::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QQuickWebEngineViewAccessible7isValidEv(
    const QQuickWebEngineViewAccessible *self) {
  return self->QQuickWebEngineViewAccessible::isValid();
}

//  QAccessibleInterface *QQuickWebEngineViewAccessible::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK29QQuickWebEngineViewAccessible10focusChildEv(
    const QQuickWebEngineViewAccessible *self) {
  return self->QQuickWebEngineViewAccessible::focusChild();
}

//  int QQuickWebEngineViewAccessible::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QQuickWebEngineViewAccessible10childCountEv(
    const QQuickWebEngineViewAccessible *self) {
  return self->QQuickWebEngineViewAccessible::childCount();
}

//  int QQuickWebEngineViewAccessible::indexOfChild(const
//      QAccessibleInterface *a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QQuickWebEngineViewAccessible12indexOfChildEPK20QAccessibleInterface(
    const QQuickWebEngineViewAccessible *self,
    const QAccessibleInterface *a0) {
  return self->QQuickWebEngineViewAccessible::indexOfChild(a0);
}

//  QString QQuickWebEngineViewAccessible::text(QAccessible::Text a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK29QQuickWebEngineViewAccessible4textEN11QAccessible4TextE(
    const QQuickWebEngineViewAccessible *self,
    QAccessible::Text a0) {
  return new QString(self->QQuickWebEngineViewAccessible::text(a0));
}

//  QAccessible::Role QQuickWebEngineViewAccessible::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK29QQuickWebEngineViewAccessible4roleEv(
    const QQuickWebEngineViewAccessible *self) {
  return self->QQuickWebEngineViewAccessible::role();
}

//  QAccessible::State QQuickWebEngineViewAccessible::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK29QQuickWebEngineViewAccessible5stateEv(
    const QQuickWebEngineViewAccessible *self) {
  return new QAccessible::State(
      self->QQuickWebEngineViewAccessible::state());
}

#endif  // QT_CONFIG(accessibility)
